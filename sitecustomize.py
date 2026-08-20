# -*- coding: utf-8 -*-
"""讓免安裝版的「XS 工坊.exe」被雙擊時自動啟動，不必經過 .bat。

## 為什麼要繞這一圈

從網路下載的檔案，Windows 會蓋上 Mark of the Web。實測（2026-08-21，
Windows 11 開啟 Smart App Control）：帶著這個標記的 `.bat`／`.cmd`／`.lnk`
**一律被封鎖**，錯誤訊息是「應用程式控制原則已封鎖此檔案」——不是跳警告，是打不開。
而**已簽章的 `python.exe` 即使帶著同一個標記也照常執行**。

所以啟動點必須是那支已簽章的執行檔本身。做法：
    XS 工坊.exe      python.exe 的副本（改名不影響 Authenticode 簽章，已驗）
    XS 工坊._pth     只有這支 exe 會讀，內容開啟 import site
    sitecustomize.py 這支檔案——site 模組啟動時會自動 import 它（Python 官方機制）

使用者因此不必知道「右鍵→內容→解除封鎖」這種事。

## 為什麼判斷條件寫得這麼嚴

這支檔案會在**任何**用到這份 Python 的情境被載入。只有「使用者雙擊那支啟動器」
才該自動開 app，其餘一律放行，否則以後有人拿這份 Python 做別的事會被攔胡。
"""
import os
import sys

_LAUNCHER = "XS 工坊"


def _should_autostart():
    # argv == [''] 才是「雙擊、完全沒帶任何參數」的長相。
    # 用 len(argv) <= 1 判斷會誤傷 `python -c "..."`——那時 argv 是 ['-c']。
    if sys.argv != [""]:
        return False
    exe = os.path.splitext(os.path.basename(sys.executable))[0]
    return exe == _LAUNCHER


def _run():
    here = os.path.dirname(os.path.abspath(sys.executable))
    app = os.path.join(here, "app.py")
    if not os.path.exists(app):
        return None                      # 不是完整的安裝包，交給正常流程去報錯

    import runpy
    sys.argv = [app]
    try:
        runpy.run_path(app, run_name="__main__")
        return 0
    except SystemExit as e:
        return e.code if isinstance(e.code, int) else 0
    except BaseException:
        import traceback
        traceback.print_exc()
        print()
        print("XS 工坊啟動失敗了。上面那整段訊息就是原因，請整段回報給我們。")
        try:
            input("按 Enter 關閉視窗…")   # 不停住的話視窗會一閃就消失，什麼也看不到
        except Exception:
            pass
        return 1


if _should_autostart():
    _code = _run()
    if _code is not None:
        for _s in (sys.stdout, sys.stderr):
            try:
                _s.flush()
            except Exception:
                pass
        # 這裡不能 raise SystemExit：現在還在 site 初始化階段，
        # 丟例外會變成「Fatal Python error: init_import_site」。直接結束進程。
        os._exit(_code)
