# -*- coding: utf-8 -*-
"""前端能不能載入的守門測試。

## 為什麼需要這一支

2026-08-21 出過一次事故：`static/app.js` 有一個字串字面值被真正的換行切斷
（`alert(x + '` 後面直接斷行），整支 JS 因語法錯誤無法解析，瀏覽器拒載，
**畫面只剩靜態外殼**——按鈕、連線嚮導、對話全部不會動。
而且這個壞掉的版本被推上公開 GitHub、也打包進發給使用者的三個安裝包。

漏掉的原因很具體：改完前端後，唯一跑過的檢查是「首頁回不回 HTTP 200」。
**首頁永遠會回 200，即使 app.js 整支壞掉**——HTML 照樣送得出去。

所以這裡守兩層：
    L1  語法層：node --check，最快、最便宜，抓死語法錯誤
    L2  行為層：真的用瀏覽器載入頁面，確認關鍵函式活著、console 沒有錯誤
        （L2 才抓得到「語法沒錯但執行就爆」的那類，例如漏掉的元素、錯的選擇器）

跑法：python tests/test_frontend.py
"""
import os
import shutil
import socket
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

JS_FILES = sorted((ROOT / "static").glob("*.js"))
# 頁面活著就必須存在的東西。挑的是「壞掉時第一個會沒反應」的那些。
REQUIRED_FUNCS = ["mdToHtml", "addMessage", "send", "loadState", "renderCites"]
REQUIRED_NODES = ["#input", "#btn-send", "#starters .starter", "#status-conn"]


# ── L1 語法層 ────────────────────────────────────────────────────────────
def test_js_syntax():
    node = shutil.which("node")
    if not node:
        print("      （找不到 node，語法層跳過——L2 仍會抓到）")
        return
    assert JS_FILES, "static/ 底下找不到任何 .js"
    for f in JS_FILES:
        r = subprocess.run([node, "--check", str(f)], capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=60)
        assert r.returncode == 0, "%s 語法錯誤：\n%s" % (f.name, (r.stderr or "")[:400])


def test_no_control_bytes():
    """出貨的文字檔不該含 NUL 等控制位元組。

    也是實際踩過的：`app.js` 的 markdown 佔位符 `\\u0000BLOCK…` 一度是真的 NUL 位元組。
    功能上沒壞（產生端與比對端用同一個位元組），但 git 會把整個檔案當二進位——
    不能 diff、不能 blame，等於這個檔案在版控裡是個黑盒子。
    要用控制字元當標記可以，但必須寫成跳脫序列，別讓它成為檔案裡的真實位元組。
    """
    targets = JS_FILES + sorted((ROOT / "static").glob("*.css")) \
        + sorted((ROOT / "templates").glob("*.html"))
    for f in targets:
        raw = f.read_bytes()
        bad = {b: raw.count(bytes([b])) for b in (0, 1, 2, 11, 12) if raw.count(bytes([b]))}
        assert not bad, "%s 含控制位元組 %s（會讓 git 判定為二進位）" % (f.name, bad)


def test_no_raw_newline_in_string_literal():
    """專門守住出過事的那一類：字串字面值被真正的換行切斷。

    這條刻意跟 node --check 重複——因為建置機不一定有 node，
    而這個特定錯誤又是我們實際踩過的，值得一道不依賴外部工具的防線。
    """
    node = shutil.which("node")
    if node:
        return          # 有 node 的話上面那條更準，不必重複判斷
    for f in JS_FILES:
        text = f.read_text(encoding="utf-8")
        # 極簡判斷：整份檔案裡，未跳脫的單引號總數應為偶數
        stripped = text.replace("\\'", "")
        assert stripped.count("'") % 2 == 0, \
            "%s 的單引號數量是奇數，可能有字串被換行切斷" % f.name


# ── L2 行為層 ────────────────────────────────────────────────────────────
def _free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def test_page_actually_runs():
    """真的開瀏覽器載入頁面，確認 JS 有跑起來。

    這是唯一能證明「使用者打開會看到活的畫面」的檢查。
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("      （沒裝 playwright，行為層跳過）")
        return

    port = _free_port()
    env = dict(os.environ)
    env["XS_NO_BROWSER"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
    env["XS_PORT"] = str(port)
    proc = subprocess.Popen([sys.executable, "app.py"], cwd=str(ROOT), env=env,
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        import urllib.request
        base = None
        # app.py 5101 被占會自動往上找，所以逐一試
        for _ in range(40):
            time.sleep(0.5)
            for p in range(5101, 5121):
                try:
                    urllib.request.urlopen("http://127.0.0.1:%d/" % p, timeout=1)
                    base = "http://127.0.0.1:%d/" % p
                    break
                except Exception:
                    continue
            if base:
                break
        assert base, "伺服器沒起來"

        errors = []
        with sync_playwright() as p:
            b = p.chromium.launch(channel="chrome")
            page = b.new_page()
            page.on("pageerror", lambda e: errors.append("PAGEERROR: %s" % e))
            page.on("console", lambda m: errors.append("CONSOLE: %s" % m.text)
                    if m.type == "error" else None)
            page.goto(base, wait_until="networkidle")
            page.wait_for_timeout(1500)

            missing = [fn for fn in REQUIRED_FUNCS
                       if page.evaluate("typeof %s" % fn) != "function"]
            empty = [sel for sel in REQUIRED_NODES
                     if page.locator(sel).count() == 0]
            b.close()

        assert not errors, "頁面有 JS 錯誤：\n  " + "\n  ".join(errors[:5])
        assert not missing, "這些函式沒定義（JS 沒載進來）：%s" % missing
        assert not empty, "這些元素沒被渲染出來：%s" % empty
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if not name.startswith("test_") or not callable(fn):
            continue
        try:
            fn()
            print("PASS", name)
        except AssertionError as e:
            failures += 1
            print("FAIL", name, "->", e)
    print("-" * 50)
    print("失敗 %d 項" % failures)
    sys.exit(1 if failures else 0)
