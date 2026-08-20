# -*- coding: utf-8 -*-
"""對話流程的伺服器側測試——用可控替身取代真實 AI。

真實模型回什麼是機率性的，不能拿來斷言失敗路徑。這裡把 llm.stream 換掉，
腳本化地重現四種情況，確認伺服器的扣字／放行／重查邏輯每次都對：

    R1  一般回答          原樣逐字送出，一個字都不能少
    R2  [LOOKUP] 開頭     扣住不送、觸發重查、丟掉半截輸出，只送第二輪的答案
    R3  以 [ 開頭但不是    誤判成 LOOKUP 就會吃掉開頭，必須完整送出
    R4  超過上限的重查     不能無限迴圈，第二次之後強制作答

跑法：python -m pytest tests/ -q   （或直接 python tests/test_chat_flow.py）
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import app as server            # noqa: E402
from xs import llm              # noqa: E402


def _chunks(text, size=7):
    """把腳本化回應切成小塊，模擬逐字串流——扣字邏輯的邊界都在切塊處。"""
    for i in range(0, len(text), size):
        yield {"t": text[i:i + size]}
    yield {"end": True}


def _fake(replies):
    """依呼叫次數依序吐出 replies 裡的回應。"""
    calls = {"n": 0}

    def _stream(config, secrets, system, messages):
        i = min(calls["n"], len(replies) - 1)
        calls["n"] += 1
        yield from _chunks(replies[i])

    _stream.calls = calls
    return _stream


def _run(replies, message="測試"):
    original = llm.stream
    fake = _fake(replies)
    llm.stream = fake
    try:
        client = server.app.test_client()
        resp = client.post("/api/chat", json={"message": message, "history": []})
        events = []
        for raw in resp.get_data(as_text=True).split("\n\n"):
            raw = raw.strip()
            if raw.startswith("data:"):
                events.append(json.loads(raw[5:].strip()))
        text = "".join(e.get("t", "") for e in events)
        return text, events, fake.calls["n"]
    finally:
        llm.stream = original


def test_plain_answer_passes_through():
    body = "這是一段普通回答。\n```xs\nvalue1 = close;\n```\n結束。"
    text, events, calls = _run([body])
    assert text == body, "一般回答被改動了：%r" % text
    assert calls == 1
    assert any(e.get("end") for e in events)


def test_lookup_triggers_second_round():
    text, events, calls = _run([
        "[LOOKUP]setposition, 停損[/LOOKUP]",
        "查過手冊了，答案是這樣。",
    ])
    assert calls == 2, "沒有觸發重查，calls=%d" % calls
    assert text == "查過手冊了，答案是這樣。", "第一輪的 LOOKUP 漏出去了：%r" % text
    lookups = [e["lookup"] for e in events if "lookup" in e]
    assert lookups == ["setposition, 停損"], lookups
    rounds = [e["round"] for e in events if "cite" in e]
    assert rounds == [0, 1], rounds


def test_bracket_start_is_not_swallowed():
    """以 [ 開頭但不是 LOOKUP——扣字邏輯不能把它吃掉。"""
    body = "[注意] 這不是查詢指令，是正常內容，必須完整出現。"
    text, events, calls = _run([body])
    assert text == body, "開頭被吃掉了：%r" % text
    assert calls == 1


def test_lookup_rounds_are_capped():
    """模型每輪都喊查詢時，不能無限迴圈，也不能把標記秀給使用者看。"""
    text, events, calls = _run(["[LOOKUP]一直查[/LOOKUP]"] * 6)
    assert calls <= server.promptmod.MAX_LOOKUP_ROUNDS + 1, "重查沒有上限，calls=%d" % calls
    assert "[LOOKUP]" not in text, "查詢標記漏到畫面上：%r" % text
    assert any(e.get("end") for e in events)


def test_exhausted_round_keeps_the_real_answer():
    """次數用完那輪若同時帶了查詢標記與答案，標記剝掉、答案要留。"""
    text, _, _ = _run([
        "[LOOKUP]第一次[/LOOKUP]",
        "[LOOKUP]第二次[/LOOKUP]",
        "[LOOKUP]還想查[/LOOKUP]這是我盡力寫出的答案。",
    ])
    assert "[LOOKUP]" not in text, repr(text)
    assert "這是我盡力寫出的答案。" in text, repr(text)


def test_error_reaches_client_with_hint():
    def _boom(config, secrets, system, messages):
        yield {"error": "測試用錯誤", "hint": "這是白話建議"}
        yield {"end": True}

    original = llm.stream
    llm.stream = _boom
    try:
        client = server.app.test_client()
        resp = client.post("/api/chat", json={"message": "x", "history": []})
        events = [json.loads(r.strip()[5:].strip())
                  for r in resp.get_data(as_text=True).split("\n\n")
                  if r.strip().startswith("data:")]
    finally:
        llm.stream = original
    err = [e for e in events if e.get("error")]
    assert err and err[0]["hint"] == "這是白話建議", events


def test_short_answer_below_hold_threshold():
    """短到沒觸發放行門檻的回應，收尾時要補吐出來，不能吞掉。"""
    text, _, _ = _run(["好。"])
    assert text == "好。", repr(text)


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
