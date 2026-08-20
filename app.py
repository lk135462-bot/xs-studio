# -*- coding: utf-8 -*-
"""XS 工坊 XS Studio —— 本機伺服器。

一支 Flask 應用，開在 127.0.0.1，只服務本機瀏覽器。
使用者的 API Key 只存在自己電腦的 secrets.json，不經過任何第三方。
"""
import json
import os
import socket
import sys
import threading
import webbrowser
from pathlib import Path

from flask import Flask, Response, jsonify, render_template, request

APP_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(APP_DIR))

from xs import config as cfgmod          # noqa: E402
from xs import llm                       # noqa: E402
from xs import prompt as promptmod       # noqa: E402
from xs.knowledge import get_kb          # noqa: E402
from xs.paths import bundle_dir, data_dir  # noqa: E402

APP_NAME = "XS 工坊 XS Studio"
VERSION = "0.1.0"
DEFAULT_PORT = 5101
PORT_SCAN = 20            # 5101 被佔就往上找，最多找 20 個

# 明確給絕對路徑：打包成 EXE 後 Flask 自己推的 root_path 會指到解壓目錄的錯層
_BUNDLE = bundle_dir()
app = Flask(__name__,
            static_folder=str(_BUNDLE / "static"),
            template_folder=str(_BUNDLE / "templates"))
app.json.ensure_ascii = False      # Flask 3 起改用這個；JSON_AS_ASCII 已移除

# 金鑰欄位名 → 對應哪個 provider。前端只會拿到遮罩後的值。
KEY_FIELDS = {"anthropic_api_key": "anthropic_api", "openrouter_key": "openrouter"}


def _sse(payload: dict) -> str:
    return "data: " + json.dumps(payload, ensure_ascii=False) + "\n\n"


@app.after_request
def _no_store(resp):
    # 本機開發型應用，改了前端就該立刻看到，不要被瀏覽器快取騙
    resp.headers["Cache-Control"] = "no-store"
    return resp


@app.route("/")
def index():
    return render_template("index.html", app_name=APP_NAME, version=VERSION)


@app.route("/api/state")
def api_state():
    """開場給前端的一切：知識庫狀態、目前連線設定、有沒有走過嚮導。"""
    cfg = cfgmod.load_config()
    secrets = cfgmod.load_secrets()
    kb = get_kb()
    stats = kb.stats()
    return jsonify({
        "app": APP_NAME, "version": VERSION,
        "knowledge": {
            "ready": stats["ready"],
            "files": stats["files"],
            "records": stats["records"],
            "always_chars": stats["always_chars"],
            "detail": stats["detail"],
            "path": str(kb.root),
        },
        "config": {
            "provider": cfg["provider"],
            "model": cfg["model"],
            "local_base_url": cfg["local_base_url"],
            "local_model": cfg["local_model"],
            "onboarded": cfg["onboarded"],
        },
        "keys": {k: cfgmod.mask(secrets.get(k, "")) for k in KEY_FIELDS},
    })


@app.route("/api/config", methods=["POST"])
def api_config():
    """存連線設定。金鑰寫 secrets.json，其餘寫 config.json。"""
    body = request.get_json(silent=True) or {}
    if not isinstance(body, dict):
        return jsonify({"ok": False, "error": "格式錯誤"}), 400

    cfg = cfgmod.load_config()
    for k in ("provider", "model", "local_base_url", "local_model"):
        if k in body and isinstance(body[k], str):
            cfg[k] = body[k].strip()
    if cfg["provider"] not in llm.PROVIDERS:
        return jsonify({"ok": False, "error": "不認得的連線方式"}), 400
    if "onboarded" in body:
        cfg["onboarded"] = bool(body["onboarded"])
    cfgmod.save_config(cfg)

    secrets = cfgmod.load_secrets()
    changed = False
    for field in KEY_FIELDS:
        val = body.get(field)
        if isinstance(val, str) and val.strip() and "…" not in val:
            # 前端把遮罩值原樣送回來時不覆蓋——那代表使用者沒改這一欄
            secrets[field] = val.strip()
            changed = True
        elif val == "":
            secrets.pop(field, None)
            changed = True
    if changed:
        cfgmod.save_secrets(secrets)

    return jsonify({"ok": True})


@app.route("/api/probe")
def api_probe():
    """連線嚮導：偵測本機有什麼可用。實際去問，不用猜的。"""
    return jsonify({
        "claude_cli": llm.probe_claude_cli(),
        "local": llm.probe_local(),
    })


@app.route("/api/claude_login", methods=["POST"])
def api_claude_login():
    """另開終端機跑 Claude 登入。互動流程不代跑，只負責把視窗開起來。"""
    return jsonify(llm.claude_login())


@app.route("/api/test", methods=["POST"])
def api_test():
    """真的送一次極短請求，確認這條連線走得通。"""
    body = request.get_json(silent=True) or {}
    cfg = cfgmod.load_config()
    for k in ("provider", "model", "local_base_url", "local_model"):
        if isinstance(body.get(k), str) and body[k].strip():
            cfg[k] = body[k].strip()
    secrets = cfgmod.load_secrets()
    for field in KEY_FIELDS:
        val = body.get(field)
        if isinstance(val, str) and val.strip() and "…" not in val:
            secrets[field] = val.strip()
    return jsonify(llm.test_connection(cfg, secrets))


@app.route("/api/chat", methods=["POST"])
def api_chat():
    """一輪對話。SSE 串流回前端。

    事件種類：
        {"cite": [...]}          本輪參考了知識庫哪些段落
        {"lookup": "關鍵字"}      軍師要求重查手冊，前端顯示「翻手冊中」
        {"t": "…"}               逐字內容
        {"error": "…","hint":…}  失敗，附白話建議
        {"end": true}            結束
    """
    body = request.get_json(silent=True) or {}
    user_text = (body.get("message") or "").strip()
    history = body.get("history") or []
    if not user_text:
        return jsonify({"error": "訊息是空的"}), 400
    if len(user_text) > 60000:
        return jsonify({"error": "訊息太長，請分段貼上"}), 400

    cfg = cfgmod.load_config()
    secrets = cfgmod.load_secrets()
    kb = get_kb()
    if not kb.stats()["ready"]:
        return jsonify({"error": "找不到 XS 知識庫",
                        "hint": "knowledge/ 資料夾不見了，請重新安裝 XS 工坊。"}), 500

    messages = promptmod.to_messages(history, user_text)

    def generate():
        extra_terms, rounds = None, 0
        while True:
            system, hits = promptmod.build_system(kb, user_text, extra_terms, rounds)
            yield _sse({"cite": [{"source": h.source, "title": h.title} for h in hits],
                        "round": rounds})

            # 先扣住開頭，確認這不是 [LOOKUP] 指令再放行給前端。
            # 不扣住的話，模型要求查手冊的那行會直接出現在對話裡，很怪。
            # 就算重查次數已用完也照樣扣——次數用完不代表模型不會再喊一次，
            # 那時要把標記剝掉而不是原樣秀給使用者看。
            buf, holding, lookup = "", True, None
            exhausted = rounds >= promptmod.MAX_LOOKUP_ROUNDS
            failed = False
            for ev in llm.stream(cfg, secrets, system, messages):
                if ev.get("error"):
                    if holding and buf:
                        yield _sse({"t": buf})
                        buf, holding = "", False
                    failed = True
                    yield _sse({"error": ev["error"], "hint": ev.get("hint", "")})
                    continue
                if ev.get("end"):
                    break
                piece = ev.get("t")
                if not piece:
                    continue
                if not holding:
                    yield _sse({"t": piece})
                    continue
                buf += piece
                stripped = buf.lstrip()
                found = promptmod.detect_lookup(buf)
                if found and not exhausted:
                    lookup = found
                    break
                if found and exhausted:
                    # 次數用完還在喊查詢：剝掉標記照常放行，剩下的內容照樣是答案
                    holding = False
                    rest = promptmod.LOOKUP_RE.sub("", buf).strip()
                    if rest:
                        yield _sse({"t": rest})
                    buf = ""
                    continue
                still_possible = (stripped.startswith("[LOOKUP]")
                                  or "[LOOKUP]".startswith(stripped[:8]))
                if not still_possible or len(buf) > 400:
                    holding = False
                    yield _sse({"t": buf})
                    buf = ""

            if lookup:
                rounds += 1
                extra_terms = lookup
                yield _sse({"lookup": lookup, "round": rounds})
                continue          # 換一份 prompt 重問，這一輪的半截輸出丟掉

            if holding and buf:   # 回應短到沒觸發放行，收尾時補吐
                tail = promptmod.LOOKUP_RE.sub("", buf).strip() if exhausted else buf
                if tail:
                    yield _sse({"t": tail})
            if not failed:
                yield _sse({"end": True})
            else:
                yield _sse({"end": True, "failed": True})
            return

    return Response(generate(), mimetype="text/event-stream",
                    headers={"X-Accel-Buffering": "no", "Cache-Control": "no-store"})


# ── 啟動 ─────────────────────────────────────────────────────────────────────

def pick_port(start=DEFAULT_PORT, scan=PORT_SCAN):
    """找一個沒人用的埠。使用者機器上什麼都可能佔著 5101，不該因此開不起來。"""
    for port in range(start, start + scan):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    return None


def _fix_console_encoding():
    """讓主控台吃得下中文。

    Windows 主控台預設是 cp950，我們的訊息是 UTF-8——不改的話使用者雙擊開起來
    第一眼看到的就是一整片亂碼，第一印象直接毀掉。
    """
    if os.name != "nt":
        return
    try:
        import ctypes
        ctypes.windll.kernel32.SetConsoleOutputCP(65001)
        ctypes.windll.kernel32.SetConsoleCP(65001)
    except Exception:
        pass
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def main():
    _fix_console_encoding()
    port = pick_port()
    if port is None:
        print("[錯誤] 找不到可用的連接埠（已試 %d–%d）。"
              % (DEFAULT_PORT, DEFAULT_PORT + PORT_SCAN - 1))
        input("按 Enter 關閉。")
        return 1

    kb = get_kb()
    stats = kb.stats()
    url = "http://127.0.0.1:%d/" % port
    print("=" * 58)
    print("  %s  v%s" % (APP_NAME, VERSION))
    print("  網址：%s" % url)
    if stats["ready"]:
        print("  知識庫：%d 份文件、%d 條索引已掛載" % (stats["files"], stats["records"]))
    else:
        print("  [警告] 找不到 knowledge/ 知識庫資料夾")
    print("  ※ 保持此視窗開啟＝運行中；關掉就結束。")
    print("=" * 58)

    if os.environ.get("XS_NO_BROWSER") != "1":
        threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    app.run(host="127.0.0.1", port=port, debug=False, threaded=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
