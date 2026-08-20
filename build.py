# -*- coding: utf-8 -*-
"""打包分發版。

    python build.py lite     輕量版（~3 MB）：原始碼＋知識庫＋啟動 bat，需使用者自備 Python
    python build.py exe      綠色免安裝版（~324 MB）：內含 Python 與 Claude Code，雙擊即用
    python build.py all      兩種都出

兩種並存是有理由的，不是猶豫不決：

  輕量版今天就能發。它跑的是使用者自己那份 python.exe（微軟認得的簽章），
  不會被 SmartScreen 或 Smart App Control 攔下來。代價是要先裝 Python。

  綠色版體驗最好、也是要推廣的目標形態，但**未簽章的執行檔在 Windows 11
  開啟 Smart App Control 的機器上會被直接封鎖**（WinError 4551），
  一般機器則至少跳一次 SmartScreen 警告。要真正對外推，需要程式碼簽章憑證。
  詳見 DISTRIBUTION.md。
"""
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
NAME = "XS 工坊"

# 輕量版要帶的東西。secrets.json / config.json 絕不進包——那是本機個人資料。
LITE_FILES = ["app.py", "requirements.txt", "README.md", "啟動 XS 工坊.bat"]
LITE_DIRS = ["xs", "templates", "static", "knowledge"]
LITE_EXCLUDE = {"__pycache__", ".pytest_cache"}

SHORTCUT_BAT = """@echo off
chcp 65001 >nul
set "TARGET=%~dp0XS 工坊.exe"
set "LNK=%USERPROFILE%\\Desktop\\XS 工坊.lnk"
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$s=(New-Object -COM WScript.Shell).CreateShortcut('%LNK%');" ^
  "$s.TargetPath='%TARGET%';" ^
  "$s.WorkingDirectory='%~dp0';" ^
  "$s.Description='XS 工坊 — XQ 腳本軍師';" ^
  "$s.Save()"
if exist "%LNK%" (
    echo 桌面捷徑建立完成，回到桌面點「XS 工坊」就能開。
) else (
    echo 建立失敗。你也可以直接把「XS 工坊.exe」拖到桌面建立捷徑。
)
pause
"""

SHORTCUT_BAT_LITE = SHORTCUT_BAT.replace("XS 工坊.exe", "啟動 XS 工坊.bat")


def _mb(path: Path) -> float:
    if path.is_file():
        return path.stat().st_size / 1048576
    return sum(f.stat().st_size for f in path.rglob("*") if f.is_file()) / 1048576


def _zip(src_dir: Path, out_zip: Path, arc_root: str):
    out_zip.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for f in sorted(src_dir.rglob("*")):
            if f.is_file():
                z.write(f, str(Path(arc_root) / f.relative_to(src_dir)))


def build_lite():
    print("\n-- 輕量版 --------------------------------------")
    stage = DIST / "_lite" / NAME
    if stage.parent.exists():
        shutil.rmtree(stage.parent)
    stage.mkdir(parents=True)

    for name in LITE_FILES:
        src = ROOT / name
        if src.exists():
            shutil.copy2(src, stage / name)
    for name in LITE_DIRS:
        shutil.copytree(ROOT / name, stage / name,
                        ignore=shutil.ignore_patterns(*LITE_EXCLUDE, "*.pyc"))
    (stage / "建立桌面捷徑.bat").write_text(SHORTCUT_BAT_LITE, encoding="utf-8")

    out = DIST / ("%s-輕量版.zip" % NAME)
    _zip(stage, out, NAME)
    print("  產出：%s（%.1f MB）" % (out, _mb(out)))
    print("  給使用者：解壓縮 → 雙擊「啟動 XS 工坊.bat」（需先裝 Python）")
    return out


def build_exe():
    print("\n-- 綠色免安裝版 --------------------------------")
    out_dir = DIST / NAME
    for stale in (ROOT / "build", out_dir):
        if stale.exists():
            shutil.rmtree(stale)

    cmd = [sys.executable, "-m", "PyInstaller", "--noconfirm", "--clean",
           "--name", NAME, "--onedir",
           "--console",                      # 關掉視窗＝關掉程式，跟萬界一致的心智模型
           "--add-data", "templates;templates",
           "--add-data", "static;static",
           # SDK 有一批執行期才 import 的東西，靜態分析會漏；內附的 claude.exe 也靠這個帶進來
           "--collect-all", "claude_agent_sdk",
           "--hidden-import", "xs.paths",
           "app.py"]
    print("  >", " ".join(cmd))
    if subprocess.run(cmd, cwd=str(ROOT)).returncode != 0:
        sys.exit("PyInstaller 失敗")

    # 知識庫刻意不進 --add-data：要留在 EXE 旁邊，使用者看得到、也能補自己的手冊
    shutil.copytree(ROOT / "knowledge", out_dir / "knowledge")
    (out_dir / "建立桌面捷徑.bat").write_text(SHORTCUT_BAT, encoding="utf-8")
    for doc in ("README.md",):
        if (ROOT / doc).exists():
            shutil.copy2(ROOT / doc, out_dir / doc)

    print("  產出：%s（%.0f MB）" % (out_dir, _mb(out_dir)))
    print("  [警告] 未簽章：Smart App Control 開啟的機器會直接封鎖，"
          "其餘機器會跳 SmartScreen 警告。")
    print("         對外推廣前請先取得程式碼簽章憑證，見 DISTRIBUTION.md。")
    return out_dir


def main():
    target = (sys.argv[1] if len(sys.argv) > 1 else "all").lower()
    if target not in ("lite", "exe", "all"):
        sys.exit(__doc__)
    if target in ("lite", "all"):
        build_lite()
    if target in ("exe", "all"):
        build_exe()
    print("\n完成。")


if __name__ == "__main__":
    main()
