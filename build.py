# -*- coding: utf-8 -*-
"""打包分發版。

    python build.py portable  免安裝版：內嵌官方 Python，雙擊即用，不必先裝 Python
    python build.py lite      輕量版（~0.4 MB）：只有原始碼＋知識庫，需使用者自備 Python
    python build.py all       上面兩種
    python build.py exe       PyInstaller 版——**未簽章的話發不出去**，見下

為什麼免安裝版不用 PyInstaller：

  PyInstaller 會產生一支我們自己的 bootloader exe。它未簽章、沒有信譽，
  Windows 11 開著 Smart App Control 的機器會**直接封鎖**（實測 WinError 4551，
  不是跳警告是打不開），其餘機器也至少跳一次 SmartScreen。

  免安裝版改成只用「別人已經簽好且信譽良好」的執行檔——
  python.exe 由 Python Software Foundation 經 DigiCert 簽章、
  claude.exe 由 Anthropic, PBC 以 EV 憑證簽章（實測皆 Valid）。
  我們自己只出 .py 與 .bat，都不是可執行映像，不受該政策管轄。
  使用者體驗一樣是解壓縮、雙擊、就開了。

  `build.py exe` 保留給「已經有程式碼簽章憑證」的情況，所以不列入 all。
  憑證取得途徑見 DISTRIBUTION.md。
"""
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

LF, CRLF = chr(10), chr(13) + chr(10)

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
NAME = "XS 工坊"

# 輕量版要帶的東西。secrets.json / config.json 絕不進包——那是本機個人資料。
LITE_FILES = ["app.py", "requirements.txt", "README.md", "啟動 XS 工坊.bat",
              "sitecustomize.py"]
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
SHORTCUT_BAT_PORTABLE = SHORTCUT_BAT_LITE

# 免安裝版的啟動器：直接用包內那份 Python，不碰使用者系統上的任何東西
PORTABLE_BAT = """@echo off
chcp 65001 >nul
cd /d "%~dp0"
title XS 工坊 XS Studio

echo ============================================================
echo   XS 工坊 XS Studio
echo   啟動中，稍候會自動開啟瀏覽器…
echo.
echo   ※ 保持此視窗開啟＝運行中；關掉這個視窗就結束。
echo ============================================================
echo.

if not exist "%~dp0python.exe" (
    echo [錯誤] 找不到程式檔案。
    echo.
    echo   最常見的原因：你是在「壓縮檔裡面」直接點的。
    echo   請先把壓縮檔解壓縮出來，再打開解壓縮後的資料夾點一次。
    echo.
    pause
    exit /b 1
)

"%~dp0python.exe" "%~dp0app.py"

echo.
echo XS 工坊已結束。按任意鍵關閉視窗。
pause >nul
"""


def _write_readme(src: Path, dst: Path):
    """使用說明用 CRLF ＋ BOM 寫出去。

    使用者多半是用記事本打開它。沒有 BOM 中文會變亂碼，沒有 CRLF 整份會擠成一行——
    兩個都是「第一眼就毀掉信任」的那種問題。
    """
    text = src.read_text(encoding="utf-8").replace(CRLF, LF).replace(LF, CRLF)
    dst.write_bytes(text.encode("utf-8-sig"))


def _write_bat(path: Path, text: str):
    """批次檔一律寫成 CRLF。

    Windows 的 cmd.exe 解析 .bat 需要 CRLF；只有 LF 會讓它把第一行讀壞、
    整支檔案跑不起來（實測第一行會變成 '???echo'）。Python 預設寫 LF，
    所以這裡要明講。
    """
    normalized = text.replace(CRLF, LF).replace(LF, CRLF)
    path.write_bytes(normalized.encode("utf-8"))


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
    _write_bat(stage / "建立桌面捷徑.bat", SHORTCUT_BAT_LITE)
    _write_readme(ROOT / "使用說明.txt", stage / "使用說明.txt")

    out = DIST / ("%s-輕量版.zip" % NAME)
    _zip(stage, out, NAME)
    print("  產出：%s（%.1f MB）" % (out, _mb(out)))
    print("  給使用者：解壓縮 → 雙擊「啟動 XS 工坊.bat」（需先裝 Python）")
    return out


def build_portable():
    """免安裝版：內嵌 Python 官方 embeddable 版，整包沒有任何未簽章執行檔。

    這是 PyInstaller 那條路撞牆之後找到的正解。差別在「誰的執行檔」：

        PyInstaller  產生一支我們自己的 bootloader exe——未簽章、沒有信譽，
                     Windows 11 開著 Smart App Control 的機器直接封鎖（WinError 4551）。
        本方案       只用別人已經簽好、且信譽良好的執行檔：
                     python.exe 由 Python Software Foundation 經 DigiCert 簽章，
                     claude.exe 由 Anthropic, PBC 以 EV 憑證簽章（實測皆 Valid）。

    **啟動點是那支已簽章的 exe 本身，不是 .bat。** 這一點是必要的，不是講究：
    從網路下載的檔案會被蓋上 Mark of the Web，實測帶著這個標記的
    .bat／.cmd／.lnk 在開啟 Smart App Control 的機器上**一律被封鎖**，
    而已簽章的 python.exe 照常執行。所以把 python.exe 複製一份改名成
    「XS 工坊.exe」（改名不影響簽章），搭配同名的 ._pth 與 sitecustomize.py
    做到雙擊即開——使用者不必知道「右鍵→內容→解除封鎖」這種事。

    Python 執行期直接攤平在資料夾根目錄（不放 python/ 子目錄），
    因為那支 exe 必須跟 python311.dll 同層才找得到它。攤平出來的雜項檔案
    會設成隱藏屬性，使用者打開資料夾只會看到啟動器與知識庫。
    """
    print("\n-- 免安裝版（內嵌 Python）----------------------")
    out_dir = DIST / ("%s-免安裝" % NAME)
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    # 1) 取得官方 embeddable 版。版本鎖成建置機的版本，wheel 的 ABI 才對得上。
    ver = "%d.%d.%d" % sys.version_info[:3]
    tag = "cp%d%d" % sys.version_info[:2]
    cache = DIST / ("_cache/python-%s-embed-amd64.zip" % ver)
    if not cache.exists():
        cache.parent.mkdir(parents=True, exist_ok=True)
        url = ("https://www.python.org/ftp/python/%s/python-%s-embed-amd64.zip"
               % (ver, ver))
        print("  下載 %s" % url)
        import urllib.request
        urllib.request.urlretrieve(url, cache)
    # 攤平在根目錄：啟動器 exe 必須與 python311.dll 同層
    py_dir = out_dir
    with zipfile.ZipFile(cache) as z:
        z.extractall(py_dir)
    print("  內嵌 Python %s" % ver)

    # 2) embeddable 版預設不吃 site-packages，要把它打開，否則裝好的套件 import 不到
    pth = next(py_dir.glob("python*._pth"))
    pth.write_text("python%d%d.zip\n.\nLib\\site-packages\nimport site\n"
                   % sys.version_info[:2], encoding="ascii")

    # 3) 相依裝進去。用 --target 而不是 venv：embeddable 版沒有 venv 模組。
    site_dir = py_dir / "Lib" / "site-packages"
    print("  安裝相依套件…")
    r = subprocess.run([sys.executable, "-m", "pip", "install",
                        "--disable-pip-version-check", "-q",
                        "--target", str(site_dir),
                        "--only-binary", ":all:",
                        "--python-version", ver, "--implementation", "cp",
                        "--abi", tag, "--platform", "win_amd64",
                        "-r", "requirements.txt"], cwd=str(ROOT))
    if r.returncode != 0:
        sys.exit("相依套件安裝失敗")

    # 3b) 清掉 site-packages 裡所有「未簽章」的 .exe。
    #     整包唯一會被執行的是 python.exe（我們的啟動器）與 claude.exe（SDK 呼叫），
    #     兩者都有有效簽章。其餘的（pip 產生的 flask.exe/uvicorn.exe 殼、
    #     pywin32 的 Pythonwin.exe/pythonservice.exe）我們一支都不跑，
    #     留著只會讓整包不再是「零未簽章執行檔」，白白給 SAC 攔截的理由。
    shims = site_dir / "bin"
    if shims.is_dir():
        shutil.rmtree(shims)
    removed = 0
    for path, _status in _audit_signatures(site_dir):
        if path.is_file():
            path.unlink()
            removed += 1
    if removed:
        print("  移除 %d 支未簽章且用不到的執行檔" % removed)
    # 順手清掉測試與快取，這些不該進發行包
    for junk in list(site_dir.rglob("__pycache__")) + list(site_dir.rglob("tests")):
        if junk.is_dir():
            shutil.rmtree(junk, ignore_errors=True)

    # 4) 應用程式本體
    for name in LITE_FILES:
        if name.endswith(".bat"):
            continue                      # 免安裝版有自己的啟動器，不用輕量版那支
        src = ROOT / name
        if src.exists():
            shutil.copy2(src, out_dir / name)
    for name in LITE_DIRS:
        shutil.copytree(ROOT / name, out_dir / name,
                        ignore=shutil.ignore_patterns(*LITE_EXCLUDE, "*.pyc"))

    _write_readme(ROOT / "使用說明.txt", out_dir / "使用說明.txt")

    # 5) 啟動器：把已簽章的 python.exe 複製一份改名。
    #    改名不影響 Authenticode（簽的是內容不是檔名，已驗），
    #    但 Python 會改去找「跟執行檔同名」的 ._pth，所以那份要一起產。
    launcher = out_dir / ("%s.exe" % NAME)
    shutil.copy2(out_dir / "python.exe", launcher)
    (out_dir / ("%s._pth" % NAME)).write_text(
        LF.join(["python%d%d.zip" % sys.version_info[:2], ".",
                 "Lib\\site-packages", "import site", ""]), encoding="ascii")

    # 備援啟動器：萬一哪台機器的 exe 啟動器出狀況，還有一條路可以走。
    # 它從網路下載後可能被 Mark of the Web 擋，所以只是備援不是主力。
    _write_bat(out_dir / "備援啟動（若主程式打不開再用）.bat", PORTABLE_BAT)

    # 註：執行期雜項的「隱藏」不在這裡做——zip 格式不保留 Windows 隱藏屬性，
    #     解壓縮出來還是會全部露出來（實測 47 個可見項目）。
    #     改由 app.py 的 _tidy_folder() 在首次啟動時整理。

    unsigned = _audit_signatures(out_dir)
    print("  資料夾：%s（%.0f MB）" % (out_dir, _mb(out_dir)))
    if unsigned:
        print("  [警告] 仍有未簽章執行檔，SAC 可能攔截：")
        for path, status in unsigned[:10]:
            print("         %s -> %s" % (path.relative_to(out_dir), status))
    else:
        print("  [OK] 包內所有 .exe 皆為有效簽章，不會被 Smart App Control 封鎖。")

    out_zip = DIST / ("%s-免安裝版.zip" % NAME)
    print("  壓縮中…")
    _zip(out_dir, out_zip, NAME)
    print("  產出：%s（%.0f MB）" % (out_zip, _mb(out_zip)))
    print("  給使用者：解壓縮 → 雙擊「%s.exe」（不必先裝任何東西）" % NAME)
    return out_dir


def _audit_signatures(root: Path):
    """清點 root 底下每一支 .exe 的簽章，回傳 [(Path, 狀態), …]，只含非 Valid 的。

    這個檢查是本方案的核心保證，所以每次打包都跑一遍，不靠記憶宣稱「應該都簽了」。

    路徑用「索引」對回，不讓 PowerShell 把路徑吐回來——它的 stdout 走的是主控台
    編碼（本機 cp950），中文資料夾名一往返就變亂碼，Path 再也對不上實體檔案。
    踩過一次：清理程式因此一支都沒刪掉，卻不會報錯。
    """
    exes = sorted(root.rglob("*.exe"))
    if not exes:
        return []
    # 路徑清單走 UTF-8 暫存檔進去，回來只帶「第幾支 + 狀態」
    import tempfile
    fd, listfile = tempfile.mkstemp(suffix=".txt")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write("\n".join(str(p) for p in exes))
    script = (
        "$ErrorActionPreference='Stop';"
        "$paths=[IO.File]::ReadAllLines('%s',[Text.Encoding]::UTF8);"
        "for($i=0;$i -lt $paths.Count;$i++){"
        "  $s=Get-AuthenticodeSignature -LiteralPath $paths[$i];"
        "  if($s.Status -ne 'Valid'){Write-Output ($i.ToString()+'|'+$s.Status)}}"
        % listfile.replace("'", "''"))
    try:
        r = subprocess.run(["powershell", "-NoProfile", "-Command", script],
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=600)
    finally:
        try:
            os.unlink(listfile)
        except OSError:
            pass
    out = []
    for line in (r.stdout or "").splitlines():
        if "|" not in line:
            continue
        idx, _, status = line.strip().partition("|")
        if idx.isdigit() and int(idx) < len(exes):
            out.append((exes[int(idx)], status))
    return out


def build_exe():
    print("\n-- PyInstaller 版（需簽章才發得出去）------------")
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
    _write_bat(out_dir / "建立桌面捷徑.bat", SHORTCUT_BAT)
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
    if target not in ("lite", "portable", "exe", "all"):
        sys.exit(__doc__)
    if target in ("lite", "all"):
        build_lite()
    if target in ("portable", "all"):
        build_portable()
    if target == "exe":
        # 刻意不進 all：未簽章的 PyInstaller 產物發不出去，要用得先有憑證
        build_exe()
    print("\n完成。")


if __name__ == "__main__":
    main()
