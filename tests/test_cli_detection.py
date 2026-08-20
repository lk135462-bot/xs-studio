# -*- coding: utf-8 -*-
"""claude 執行檔的挑選順序。

這條有專門的測試，是因為它壞掉時**不會有人發現**：
開發機上裝的是舊版 SDK（0.2.93）還吃 .cmd，一切正常；
使用者拿到的包裡是新版（0.2.142+），它會拒絕執行 .bat/.cmd——
「Windows runs .bat/.cmd files via cmd.exe, which can execute commands injected
through CLI arguments」——於是每一次對話都直接失敗。

規則：原生 claude.exe → SDK 內附的 claude.exe → 真的沒有了才輪到 .cmd。

跑法：python tests/test_cli_detection.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from xs import llm            # noqa: E402


class _Fake:
    """把三種來源換成可控的假值，測純粹的優先順序。"""

    def __init__(self, native="", bundled="", which=None):
        self.native, self.bundled, self.which = native, bundled, which or {}

    def __enter__(self):
        import os
        import shutil
        import tempfile
        self._saved = (llm._native_claude_exe, llm._bundled_claude_cli,
                       shutil.which, getattr(llm._find_claude_cli, "_cached", "unset"),
                       os.environ.get("APPDATA"))
        llm._native_claude_exe = lambda: self.native
        llm._bundled_claude_cli = lambda: self.bundled
        shutil.which = lambda name, *a, **k: self.which.get(name)
        # 最後一順位會去 %APPDATA%\npm 撈實體檔案；指到空目錄才測得準，
        # 否則這台機器上真的有一支 npm 裝的 claude.cmd，測試會被現實汙染
        os.environ["APPDATA"] = tempfile.mkdtemp(prefix="xs_test_appdata_")
        if hasattr(llm._find_claude_cli, "_cached"):
            del llm._find_claude_cli._cached
        return self

    def __exit__(self, *exc):
        import os
        import shutil
        (llm._native_claude_exe, llm._bundled_claude_cli, shutil.which,
         cached, appdata) = self._saved
        if appdata is None:
            os.environ.pop("APPDATA", None)
        else:
            os.environ["APPDATA"] = appdata
        if cached == "unset":
            if hasattr(llm._find_claude_cli, "_cached"):
                del llm._find_claude_cli._cached
        else:
            llm._find_claude_cli._cached = cached


def test_native_exe_wins():
    with _Fake(native=r"C:\native\claude.exe", bundled=r"C:\pkg\claude.exe",
               which={"claude.cmd": r"C:\npm\claude.cmd"}):
        assert llm._find_claude_cli() == r"C:\native\claude.exe"


def test_bundled_exe_beats_cmd():
    """關鍵案例：使用者用 npm 裝過 Claude Code，但那是 .cmd。

    不能因為「使用者自己裝了」就優先用它——新版 SDK 根本不會執行 .cmd。
    """
    with _Fake(native="", bundled=r"C:\pkg\claude.exe",
               which={"claude.cmd": r"C:\npm\claude.cmd"}):
        got = llm._find_claude_cli()
    assert got == r"C:\pkg\claude.exe", "挑到了 .cmd（%s），新版 SDK 會拒跑" % got
    assert not got.lower().endswith(".cmd")


def test_cmd_only_as_last_resort():
    """兩支 exe 都沒有時才用 .cmd——總比什麼都找不到好（probe/login 這條路吃得下）。"""
    with _Fake(native="", bundled="", which={"claude.cmd": r"C:\npm\claude.cmd"}):
        assert llm._find_claude_cli() == r"C:\npm\claude.cmd"


def test_nothing_found_returns_empty():
    with _Fake(native="", bundled="", which={}):
        assert llm._find_claude_cli() == ""


def test_real_machine_never_hands_cmd_to_sdk():
    """在這台機器上實跑：只要內附 exe 存在，就不該挑到 .cmd。"""
    if hasattr(llm._find_claude_cli, "_cached"):
        del llm._find_claude_cli._cached
    try:
        got = llm._find_claude_cli()
    finally:
        if hasattr(llm._find_claude_cli, "_cached"):
            del llm._find_claude_cli._cached
    if llm._bundled_claude_cli() or llm._native_claude_exe():
        assert not got.lower().endswith(".cmd"), "挑到 .cmd：%s" % got


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
