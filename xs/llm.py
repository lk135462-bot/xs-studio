# -*- coding: utf-8 -*-
"""四種 AI 後端 ＋ dispatcher ＋ 連線偵測。

    claude_sdk      本機 Claude Code（claude login 的訂閱額度）—— 預設、對有訂閱者零額外花費
    anthropic_api   Anthropic API key（預付餘額）
    openrouter      OpenRouter API key（一把 key 通吃各家模型）
    local           任何 OpenAI 相容端點（Ollama / LM Studio / vLLM）

Windows 上跑 Claude Agent SDK 的幾個坑已在此處理：找不到 claude 執行檔、
CMD argv 8191 字元上限裝不下 system prompt、SDK 需要 git-bash。
這段做法沿用萬界 OmniWorld 的 omni/llm.py（已在實機長期運行驗證）。
"""
import json
import os
from pathlib import Path

import requests

ANTHROPIC_ENDPOINT = "https://api.anthropic.com/v1/messages"
OPENROUTER_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"

DEFAULT_ANTHROPIC_MODEL = "claude-sonnet-4-6"
DEFAULT_OPENROUTER_MODEL = "anthropic/claude-sonnet-4.5"
DEFAULT_PROVIDER = "claude_sdk"

PROVIDERS = ("claude_sdk", "anthropic_api", "openrouter", "local")

# 本地推論常見預設埠。偵測時逐一探，探到哪個算哪個。
LOCAL_CANDIDATES = [
    ("Ollama", "http://127.0.0.1:11434/v1"),
    ("LM Studio", "http://127.0.0.1:1234/v1"),
    ("vLLM / 其他 OpenAI 相容", "http://127.0.0.1:8000/v1"),
]


class LLMError(RuntimeError):
    """帶「給使用者看的白話說明」的錯誤。前端直接顯示 hint。"""

    def __init__(self, message, hint=""):
        super().__init__(message)
        self.hint = hint


# ── Anthropic API（直連 HTTP，吃預付餘額）────────────────────────────────────

def _anthropic_headers(secrets, config):
    key = (secrets.get("anthropic_api_key") or os.environ.get("ANTHROPIC_API_KEY") or "")
    if not key:
        raise LLMError("尚未設定 Anthropic API Key",
                       "到右上角「AI 連線」貼上你的 API Key（sk-ant- 開頭）。")
    return {
        "x-api-key": key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json; charset=utf-8",
    }


def _anthropic_payload(config, system, messages, stream):
    body = {
        "model": config.get("model") or DEFAULT_ANTHROPIC_MODEL,
        "max_tokens": int(config.get("max_tokens") or 8000),
        "temperature": float(config.get("temperature") or 0.3),
        "messages": messages,
        "stream": stream,
    }
    if system:
        # 常駐層（規範＋速查＋注意事項，約 23K 字）永遠在 system 最前段、逐輪一模一樣，
        # 前綴快取真的吃得到；檢索層每輪不同、排在後面，本來就快取不到。
        body["system"] = [{"type": "text", "text": system,
                           "cache_control": {"type": "ephemeral"}}]
    return json.dumps(body, ensure_ascii=False).encode("utf-8")


def _anthropic_stream(config, secrets, system, messages, timeout=180):
    with requests.post(ANTHROPIC_ENDPOINT,
                       headers=_anthropic_headers(secrets, config),
                       data=_anthropic_payload(config, system, messages, True),
                       stream=True, timeout=timeout) as resp:
        if not resp.ok:
            yield {"error": _http_hint("Anthropic", resp)}
            return
        for raw in resp.iter_lines():
            if not raw:
                continue
            s = raw.decode("utf-8", "replace")
            if not s.startswith("data: "):
                continue
            try:
                parsed = json.loads(s[6:])
            except Exception:
                continue
            t = parsed.get("type")
            if t == "content_block_delta":
                d = parsed.get("delta") or {}
                if d.get("type") == "text_delta" and d.get("text"):
                    yield {"t": d["text"]}
            elif t == "message_delta" and parsed.get("usage"):
                yield {"usage": parsed["usage"]}
            elif t == "message_stop":
                yield {"end": True}
            elif t == "error":
                yield {"error": str(parsed.get("error"))}


# ── OpenAI 相容（OpenRouter 與本地模型共用同一套協定）──────────────────────

def _oai_payload(model, system, messages, config, stream):
    msgs = ([{"role": "system", "content": system}] if system else []) + messages
    return json.dumps({
        "model": model,
        "messages": msgs,
        "max_tokens": int(config.get("max_tokens") or 8000),
        "temperature": float(config.get("temperature") or 0.3),
        "stream": stream,
    }, ensure_ascii=False).encode("utf-8")


def _oai_stream(url, headers, model, config, system, messages, label, timeout=300):
    with requests.post(url, headers=headers,
                       data=_oai_payload(model, system, messages, config, True),
                       stream=True, timeout=timeout) as resp:
        if not resp.ok:
            yield {"error": _http_hint(label, resp)}
            return
        for raw in resp.iter_lines():
            if not raw:
                continue
            s = raw.decode("utf-8", "replace")
            if not s.startswith("data: "):
                continue
            chunk = s[6:].strip()
            if chunk == "[DONE]":
                yield {"end": True}
                return
            try:
                parsed = json.loads(chunk)
                choices = parsed.get("choices") or []
                if not choices:
                    continue
                delta = (choices[0].get("delta") or {}).get("content") or ""
                if delta:
                    yield {"t": delta}
            except Exception:
                continue
        yield {"end": True}


def _openrouter_stream(config, secrets, system, messages, timeout=300):
    key = (secrets.get("openrouter_key") or os.environ.get("OPENROUTER_API_KEY") or "")
    if not key:
        yield {"error": "尚未設定 OpenRouter API Key",
               "hint": "到右上角「AI 連線」貼上 OpenRouter 的 key（sk-or- 開頭）。"}
        return
    headers = {
        "Authorization": "Bearer " + key,
        "Content-Type": "application/json; charset=utf-8",
        "HTTP-Referer": "https://xq.com.tw",
        "X-Title": "XS Studio",
    }
    yield from _oai_stream(OPENROUTER_ENDPOINT, headers,
                           config.get("model") or DEFAULT_OPENROUTER_MODEL,
                           config, system, messages, "OpenRouter", timeout)


def _local_stream(config, secrets, system, messages, timeout=600):
    base = (config.get("local_base_url") or "").rstrip("/")
    if not base:
        yield {"error": "尚未設定本地模型位址",
               "hint": "到右上角「AI 連線」→ 本地模型，按「自動偵測」。"}
        return
    model = config.get("local_model") or config.get("model") or "local-model"
    headers = {"Content-Type": "application/json; charset=utf-8",
               "Authorization": "Bearer local"}   # LM Studio 會檢查有沒有這個標頭
    yield from _oai_stream(base + "/chat/completions", headers, model,
                           config, system, messages, "本地模型", timeout)


# ── Claude Agent SDK（吃本機 claude login 的訂閱額度）────────────────────────

_SDK_PREFIX = (
    "【執行指示】system prompt 已含完整 XS 知識庫與所有規則。"
    "**絕對不要呼叫任何工具**（不要 Read、Bash、Grep、WebSearch、MCP），不要讀取任何檔案。"
    "直接以純文字作答。\n\n"
)


def _bundled_claude_cli():
    """claude-agent-sdk 套件裡自帶的一份 Claude Code 執行檔。

    這是綠色免安裝版能一鍵上手的關鍵：很多人有 Claude 訂閱、卻從沒裝過 Claude Code。
    有這一份，他們只要登入就能用，不必先去裝 Node 再裝 CLI。
    """
    try:
        import claude_agent_sdk
        p = Path(claude_agent_sdk.__file__).resolve().parent / "_bundled" / "claude.exe"
        return str(p) if p.exists() else ""
    except Exception:
        return ""


def _native_claude_exe():
    """使用者自己裝的**原生** claude.exe（官方安裝程式裝的那種）。

    刻意只認 .exe，不認 .cmd——理由見 _find_claude_cli。
    """
    import shutil
    cand = shutil.which("claude.exe")
    if cand and cand.lower().endswith(".exe"):
        return cand
    for base in (os.path.expandvars(r"%LOCALAPPDATA%\Programs\claude"),
                 os.path.expandvars(r"%LOCALAPPDATA%\claude"),
                 os.path.expandvars(r"%PROGRAMFILES%\claude")):
        p = Path(base) / "claude.exe"
        if p.exists():
            return str(p)
    return ""


def _find_claude_cli():
    """找出要驅動的 claude 執行檔。順序：原生 exe → 內附 exe → 最後才輪到 .cmd。

    **為什麼把 npm 裝的 claude.cmd 排到最後**（這條踩過）：
    claude-agent-sdk 自 0.2.142 起會拒絕執行 .bat/.cmd——
    「Windows runs .bat/.cmd files via cmd.exe, which can execute commands
    injected through CLI arguments」，那是它刻意的安全設計，不是 bug。
    舊版（0.2.93）還吃 .cmd，所以在開發機上一切看起來正常，
    使用者裝到新版就整條斷掉。優先給原生 exe 才是對的。

    .cmd 仍留在最後一順位：probe／login 是我們自己開子進程跑的，
    那條路 .cmd 沒問題，總比「什麼都找不到」好。
    """
    cached = getattr(_find_claude_cli, "_cached", "unset")
    if cached != "unset":
        return cached
    cand = _native_claude_exe() or _bundled_claude_cli()
    if not cand:
        import shutil
        cand = shutil.which("claude.cmd") or shutil.which("claude") or ""
    if not cand:
        p = Path(os.path.expandvars("%APPDATA%")) / "npm" / "claude.cmd"
        cand = str(p) if p.exists() else ""
    _find_claude_cli._cached = cand
    return cand


def find_git_bash():
    """找 git-bash。Claude Code 在 Windows 沒有它（或 PowerShell 7）就跑不起來。

    從 Explorer 雙擊啟動時的 PATH 跟開發者終端機裡的 PATH 不一樣，
    只靠 which 會漏掉一堆實際裝了 Git 的機器，所以常見安裝位置也要掃。
    """
    import shutil
    cands = [os.environ.get("CLAUDE_CODE_GIT_BASH_PATH"),
             shutil.which("bash.exe"), shutil.which("bash")]
    for base in (r"C:\Program Files\Git",
                 r"C:\Program Files (x86)\Git",
                 os.path.expandvars(r"%LOCALAPPDATA%\Programs\Git"),
                 os.path.expandvars(r"%ProgramW6432%\Git")):
        cands += [str(Path(base) / "bin" / "bash.exe"),
                  str(Path(base) / "usr" / "bin" / "bash.exe")]
    for cand in cands:
        if cand and Path(cand).exists():
            return str(cand)
    return ""


def find_pwsh():
    """PowerShell 7。Claude Code 接受它作為 git-bash 的替代。"""
    import shutil
    cand = shutil.which("pwsh")
    if cand:
        return cand
    for base in (r"C:\Program Files\PowerShell",
                 os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\PowerShell")):
        p = Path(base)
        if p.is_dir():
            for sub in sorted(p.iterdir(), reverse=True):
                exe = sub / "pwsh.exe"
                if exe.exists():
                    return str(exe)
    return ""


def _sdk_bash_env():
    """交給 SDK 的環境變數覆寫。找不到就不覆寫，讓 CLI 自己去找 PowerShell。"""
    b = find_git_bash()
    return {"CLAUDE_CODE_GIT_BASH_PATH": b} if b else {}


def _cli_env():
    """跑 claude CLI 子進程時用的完整環境（繼承目前環境 ＋ 補上 bash 路徑）。"""
    env = dict(os.environ)
    env.update(_sdk_bash_env())
    return env


def _sdk_system_file(system):
    """system prompt 寫進暫存檔再交給 SDK。

    SDK 是用 CLI argv 傳 system prompt 的，Windows CMD 有 8191 字元上限，
    而我們的 system 光常駐層就 23K 字——不落檔一定被截斷。
    """
    import tempfile
    if not system:
        return None, None
    f = tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8")
    f.write(system)
    f.close()
    return f.name, {"type": "file", "path": f.name}


def _sdk_stream(config, secrets, system, messages, timeout=600):
    import asyncio
    import queue as _queue
    import threading
    try:
        from claude_agent_sdk import (query, ClaudeAgentOptions, ResultMessage,
                                      AssistantMessage, TextBlock, StreamEvent)
    except ImportError:
        yield {"error": "找不到 claude-agent-sdk 套件",
               "hint": "這是內部相依缺失，請重新安裝 XS 工坊；或先改用 API Key 路線。"}
        return

    cli = _find_claude_cli()
    if not cli:
        yield {"error": "找不到本機的 Claude Code",
               "hint": "請先安裝 Claude Code 並執行一次 claude login；"
                       "或改用 API Key／本地模型路線。"}
        return

    prompt_parts = [_SDK_PREFIX]
    for m in messages:
        tag = "[使用者] " if m["role"] == "user" else "[軍師] "
        prompt_parts.append(tag + m["content"])
    prompt = "\n\n".join(prompt_parts)

    sp_file, sp_arg = _sdk_system_file(system)
    options = ClaudeAgentOptions(
        model=config.get("model") or DEFAULT_ANTHROPIC_MODEL,
        allowed_tools=[], disallowed_tools=["*"], tools=[],
        mcp_servers={}, agents={}, plugins=[], skills=[],
        max_turns=1, system_prompt=sp_arg, max_thinking_tokens=0,
        cli_path=cli, env=_sdk_bash_env(),
        setting_sources=[],            # 不吃使用者 ~/.claude 的設定，避免互相污染
        include_partial_messages=True,
    )

    q = _queue.Queue()
    DONE = object()

    def _worker():
        async def _go():
            streamed = False
            try:
                async for msg in query(prompt=prompt, options=options):
                    if isinstance(msg, StreamEvent):
                        ev = msg.event or {}
                        if ev.get("type") == "content_block_delta":
                            d = ev.get("delta") or {}
                            if d.get("type") == "text_delta" and d.get("text"):
                                streamed = True
                                q.put(("t", d["text"]))
                    elif isinstance(msg, AssistantMessage):
                        if not streamed:   # 這台機器沒吐 partial，整段補一次
                            txt = "".join(b.text or "" for b in (msg.content or [])
                                          if isinstance(b, TextBlock))
                            if txt:
                                streamed = True
                                q.put(("t", txt))
                    elif isinstance(msg, ResultMessage):
                        if not streamed and msg.result:
                            streamed = True
                            q.put(("t", msg.result))
            except Exception as e:
                q.put(("error", "Claude Code 呼叫失敗：" + str(e)))

        try:
            asyncio.run(_go())
        except Exception as e:
            q.put(("error", "Claude Code 呼叫失敗：" + str(e)))
        finally:
            q.put((DONE, None))
            # 由 worker 自己刪暫存檔——確保 SDK 讀完才刪，不跟主執行緒搶
            if sp_file:
                try:
                    os.unlink(sp_file)
                except OSError:
                    pass

    threading.Thread(target=_worker, daemon=True).start()
    while True:
        kind, payload = q.get()
        if kind is DONE:
            break
        if kind == "error":
            yield {"error": payload,
                   "hint": "若是首次使用，請先在終端機執行 claude login 完成登入。"}
            continue
        yield {"t": payload}
    yield {"end": True}


# ── dispatcher ───────────────────────────────────────────────────────────────

def _http_hint(label, resp):
    code = resp.status_code
    body = (resp.text or "")[:300]
    if code in (401, 403):
        return label + " 拒絕連線（" + str(code) + "）：API Key 不正確或已失效。"
    if code == 429:
        return label + " 額度用盡或請求過快（429）。請稍候再試，或改用其他連線方式。"
    if code >= 500:
        return label + " 伺服器忙碌（" + str(code) + "），稍後再試。"
    return label + " 回應 " + str(code) + "：" + body


def stream(config, secrets, system, messages):
    """統一入口：回傳 {'t':…} / {'usage':…} / {'error':…,'hint':…} / {'end':True}。"""
    provider = (config.get("provider") or DEFAULT_PROVIDER).strip()
    try:
        if provider == "anthropic_api":
            gen = _anthropic_stream(config, secrets, system, messages)
        elif provider == "openrouter":
            gen = _openrouter_stream(config, secrets, system, messages)
        elif provider == "local":
            gen = _local_stream(config, secrets, system, messages)
        else:
            gen = _sdk_stream(config, secrets, system, messages)
        for ev in gen:
            yield ev
    except LLMError as e:
        yield {"error": str(e), "hint": e.hint}
    except requests.exceptions.ConnectionError:
        yield {"error": "連不上 AI 服務",
               "hint": "檢查網路連線；若用本地模型，確認 Ollama／LM Studio 已經啟動。"}
    except requests.exceptions.Timeout:
        yield {"error": "AI 回應逾時", "hint": "題目較大時可再試一次，或換更快的模型。"}
    except Exception as e:
        yield {"error": "呼叫 AI 時發生未預期錯誤：" + str(e), "hint": ""}


# ── 連線嚮導用的偵測與測試 ───────────────────────────────────────────────────

def _no_window():
    """Windows 上開子進程不要閃出黑框。非 Windows 回空 dict。"""
    import subprocess
    if os.name != "nt":
        return {}
    return {"creationflags": getattr(subprocess, "CREATE_NO_WINDOW", 0)}


def probe_claude_cli():
    """偵測本機 Claude Code：找得到執行檔嗎？登入了嗎？是誰？

    登入狀態直接問 `claude auth status`（回 JSON），不用猜、也不用等使用者
    送出第一句話才發現沒登入。
    """
    import subprocess
    cli = _find_claude_cli()
    if not cli:
        return {"found": False, "logged_in": False, "path": "", "bundled": False,
                "detail": "找不到 claude 指令"}
    bundled = cli == _bundled_claude_cli()
    shell = find_git_bash() or find_pwsh()
    info = {"found": True, "logged_in": None, "path": cli, "bundled": bundled,
            "shell": shell, "detail": "內附版本" if bundled else "已安裝"}
    if os.name == "nt" and not shell:
        # 這是硬性前提，不是我們能繞過的：Claude Code 在 Windows 需要
        # git-bash 或 PowerShell 7 才啟動得了。早點講清楚，別讓人卡在測試連線。
        info["logged_in"] = False
        info["missing_shell"] = True
        info["detail"] = "缺少 Git for Windows 或 PowerShell 7"
        return info
    try:
        r = subprocess.run([cli, "auth", "status"], capture_output=True, text=True,
                           timeout=60, encoding="utf-8", errors="replace",
                           env=_cli_env(), **_no_window())
        data = json.loads((r.stdout or "").strip())
    except Exception:
        # 版本較舊沒有 auth status、或執行失敗——降級成「裝了但不確定登入」，
        # 由使用者按「測試連線」問到底。這裡不冒充知道。
        return info
    info["logged_in"] = bool(data.get("loggedIn"))
    info["email"] = data.get("email") or ""
    info["plan"] = data.get("subscriptionType") or data.get("authMethod") or ""
    if info["logged_in"]:
        who = info["email"] or "已登入帳號"
        info["detail"] = "已登入 " + who + ("（%s 訂閱）" % info["plan"] if info["plan"] else "")
    else:
        info["detail"] = "已就緒，但尚未登入 Claude 帳號"
    return info


def claude_login():
    """另開一個終端機視窗跑 Claude 登入流程。

    登入是互動流程（會開瀏覽器、要貼授權碼），塞在網頁裡代跑只會壞掉；
    開一個真的終端機讓使用者照著做，完成後回網頁按「重新偵測」最實在。
    """
    import subprocess
    cli = _find_claude_cli()
    if not cli:
        return {"ok": False, "error": "找不到 Claude Code 執行檔",
                "hint": "請改用 API Key 或本地模型路線。"}
    try:
        flags = {}
        if os.name == "nt":
            flags["creationflags"] = getattr(subprocess, "CREATE_NEW_CONSOLE", 0)
        subprocess.Popen([cli, "auth", "login"], cwd=str(Path(cli).parent),
                         env=_cli_env(), **flags)
    except Exception as e:
        return {"ok": False, "error": "無法啟動登入流程：" + str(e), "hint": ""}
    return {"ok": True, "hint": "已開啟登入視窗。照著上面的指示完成登入後，回來按「重新偵測」。"}


def probe_local():
    """掃常見的本地推論埠，回報哪個活著、上面有哪些模型。"""
    out = []
    for name, base in LOCAL_CANDIDATES:
        try:
            r = requests.get(base + "/models", timeout=2)
            if r.ok:
                data = r.json()
                models = [m.get("id") for m in (data.get("data") or []) if m.get("id")]
                out.append({"name": name, "base_url": base, "alive": True,
                            "models": models[:40]})
        except Exception:
            continue
    return out


def test_connection(config, secrets):
    """真的送一次極短請求，確認這條路走得通。不猜，實測。"""
    messages = [{"role": "user", "content": "回覆兩個字：可用"}]
    tiny = dict(config)
    tiny["max_tokens"] = 32
    got, err, hint = "", "", ""
    for ev in stream(tiny, secrets, "你是連線測試回聲器，只回覆使用者要求的字。", messages):
        if ev.get("t"):
            got += ev["t"]
        if ev.get("error"):
            err = ev["error"]
            hint = ev.get("hint") or hint
        if ev.get("end"):
            break
        if len(got) > 200:
            break
    if err:
        return {"ok": False, "error": err, "hint": hint}
    if not got.strip():
        return {"ok": False, "error": "AI 沒有回應內容",
                "hint": "模型可能不支援串流，或本地模型還在載入中。"}
    return {"ok": True, "sample": got.strip()[:80]}
