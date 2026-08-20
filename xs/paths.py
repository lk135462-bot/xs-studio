# -*- coding: utf-8 -*-
"""路徑解析——原始碼跑法與打包成 EXE 跑法的差別都收在這裡。

打包後有兩個不同的「根」，混用會出兩種 bug：

    data_dir()    使用者看得到、可以動的東西：knowledge/、config.json、secrets.json
                  → 跟 EXE 放在同一層。使用者要能打開資料夾補自己的手冊、
                    也要能直接把整個資料夾複製到隨身碟帶走。

    bundle_dir()  唯讀資源：templates/、static/
                  → PyInstaller 解壓到暫存目錄（sys._MEIPASS），每次執行都不同，
                    寫進去是沒有意義的。

未打包時兩者都是專案根目錄，所以開發跟正式跑起來行為一致。
"""
import sys
from pathlib import Path

_PKG_PARENT = Path(__file__).resolve().parent.parent


def frozen() -> bool:
    return getattr(sys, "frozen", False)


def data_dir() -> Path:
    """使用者資料根：EXE 所在資料夾（未打包時為專案根）。"""
    if frozen():
        return Path(sys.executable).resolve().parent
    return _PKG_PARENT


def bundle_dir() -> Path:
    """唯讀資源根：打包時的解壓目錄（未打包時為專案根）。"""
    meipass = getattr(sys, "_MEIPASS", None)
    return Path(meipass) if meipass else _PKG_PARENT
