# -*- coding: utf-8 -*-
"""XS 工坊 XS Studio — 引擎核心套件（無 Flask 依賴）。

模組分工：
    config      設定／金鑰讀寫、首次啟動預設值
    knowledge   xs-skill 知識庫索引與段落檢索（取代 Claude Code 的 Grep）
    prompt      system prompt 組裝、[LOOKUP] 二段檢索協定
    llm         四後端（claude_sdk / anthropic_api / openrouter / local）＋ dispatcher
"""

__all__ = ["config", "knowledge", "prompt", "llm"]
