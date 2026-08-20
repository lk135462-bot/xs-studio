# -*- coding: utf-8 -*-
"""OpenAI 相容串流的解析測試（OpenRouter 與本地模型共用同一段程式）。

用一個假的本機端點跑真的 HTTP，驗證三件事：
    R1  逐塊 SSE 能正確拼回完整內容
    R2  非 2xx 回應要變成看得懂的錯誤訊息，不是丟出 traceback
    R3  /models 探測能列出模型清單（連線嚮導的自動偵測靠它）

不打真的 OpenRouter：那要金鑰、要花錢，而且別人服務掛掉會讓我們的測試變紅燈。

跑法：python tests/test_oai_stream.py
"""
import json
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from xs import llm            # noqa: E402

CHUNKS = ["讓我", "查一下", "手冊。\n```xs\n", "value1 = close;\n", "```"]
EXPECTED = "".join(CHUNKS)

_mode = {"fail": False}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass                      # 測試輸出保持乾淨

    def do_GET(self):
        if self.path.endswith("/models"):
            self._json({"data": [{"id": "qwen2.5-coder:14b"}, {"id": "llama3.1:8b"}]})
        else:
            self.send_error(404)

    def do_POST(self):
        length = int(self.headers.get("Content-Length") or 0)
        body = json.loads(self.rfile.read(length) or b"{}")
        if _mode["fail"]:
            self._json({"error": {"message": "no credit"}}, code=402)
            return
        # 回話裡要看得到 system 有被送過去，否則等於知識庫沒進 prompt
        assert body["messages"][0]["role"] == "system", "system prompt 沒送出去"
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.end_headers()
        for c in CHUNKS:
            payload = {"choices": [{"delta": {"content": c}}]}
            self.wfile.write(b"data: " + json.dumps(payload).encode() + b"\n\n")
            self.wfile.flush()
        self.wfile.write(b"data: [DONE]\n\n")
        self.wfile.flush()

    def _json(self, obj, code=200):
        raw = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)


def _serve():
    srv = HTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, "http://127.0.0.1:%d/v1" % srv.server_address[1]


SRV, BASE = _serve()
CFG = {"provider": "local", "local_base_url": BASE, "local_model": "test-model",
       "max_tokens": 500, "temperature": 0.3}


def _collect(cfg):
    text, err = "", None
    for ev in llm.stream(cfg, {}, "你是測試用的 system prompt。",
                         [{"role": "user", "content": "hi"}]):
        if ev.get("t"):
            text += ev["t"]
        if ev.get("error"):
            err = ev
    return text, err


def test_stream_reassembles_content():
    _mode["fail"] = False
    text, err = _collect(CFG)
    assert err is None, err
    assert text == EXPECTED, repr(text)


def test_http_error_becomes_readable_message():
    _mode["fail"] = True
    try:
        text, err = _collect(CFG)
    finally:
        _mode["fail"] = False
    assert err is not None, "402 沒有變成錯誤事件"
    assert "本地模型" in err["error"] and "402" in err["error"], err


def test_unreachable_endpoint_has_hint():
    """服務沒開的情況——要給白話建議，不是丟 ConnectionError。"""
    cfg = dict(CFG, local_base_url="http://127.0.0.1:1/v1")
    text, err = _collect(cfg)
    assert err and err.get("hint"), err
    assert "Ollama" in err["hint"] or "網路" in err["hint"], err


def test_probe_lists_models():
    llm.LOCAL_CANDIDATES.append(("測試端點", BASE))
    try:
        found = [s for s in llm.probe_local() if s["base_url"] == BASE]
    finally:
        llm.LOCAL_CANDIDATES.pop()
    assert found, "偵測不到測試端點"
    assert "qwen2.5-coder:14b" in found[0]["models"], found[0]


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
