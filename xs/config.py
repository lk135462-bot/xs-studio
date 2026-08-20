# -*- coding: utf-8 -*-
"""設定與金鑰的讀寫。

刻意把「設定」與「金鑰」分兩個檔：
    config.json   provider / model / 介面偏好 —— 可以安心進 git、可以隨安裝包發出去
    secrets.json  API key —— gitignore，永遠不進版控、不隨安裝包散佈

兩者都用「檔案不存在就當空 dict」的寬容讀法：綠色免安裝版第一次跑起來時
使用者的資料夾裡本來就什麼都沒有，不該因此炸掉。
"""
import json
import os
import tempfile
from pathlib import Path

from .paths import data_dir

APP_DIR = data_dir()
CONFIG_FILE = APP_DIR / "config.json"
SECRETS_FILE = APP_DIR / "secrets.json"

DEFAULT_CONFIG = {
    "provider": "claude_sdk",          # claude_sdk / anthropic_api / openrouter / local
    "model": "",                       # 空＝各 provider 自己的預設
    "temperature": 0.3,                # 寫程式碼，低溫
    "max_tokens": 8000,
    "local_base_url": "http://127.0.0.1:11434/v1",   # Ollama 預設；LM Studio 是 :1234/v1
    "local_model": "",
    "onboarded": False,                # 首次啟動嚮導是否走完
}


def _atomic_write(path: Path, text: str) -> None:
    """同資料夾 temp 檔 + os.replace 原子換檔。

    設定檔被寫壞使用者就進不了介面，而寫入正好撞上關視窗／當機並不罕見。
    temp 檔必須跟目標同一個資料夾，否則跨磁碟時 os.replace 不是原子操作。
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def _read_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def load_config() -> dict:
    """讀設定，缺的欄位用預設值補齊（舊版設定檔升級後不會少欄位）。"""
    cfg = dict(DEFAULT_CONFIG)
    cfg.update(_read_json(CONFIG_FILE))
    return cfg


def save_config(cfg: dict) -> None:
    # 只留認得的鍵，避免前端塞進來的雜訊長期堆積在設定檔裡
    clean = {k: cfg[k] for k in DEFAULT_CONFIG if k in cfg}
    _atomic_write(CONFIG_FILE, json.dumps(clean, ensure_ascii=False, indent=2))


def load_secrets() -> dict:
    return _read_json(SECRETS_FILE)


def save_secrets(secrets: dict) -> None:
    clean = {k: v for k, v in secrets.items() if isinstance(v, str)}
    _atomic_write(SECRETS_FILE, json.dumps(clean, ensure_ascii=False, indent=2))


def mask(key: str) -> str:
    """回給前端顯示用的遮罩：sk-ant-…AbCd。完整金鑰永遠不出後端。"""
    if not key:
        return ""
    return key[:7] + "…" + key[-4:] if len(key) > 14 else "…" + key[-4:]
