# XS 工坊 XS Studio

把交易想法講成一支能在 XQ 全球贏家編譯執行的 XScript 腳本。

一個獨立的桌面前台：點開就是對話視窗，用平常講策略的方式描述需求，AI 會查 XQ 官方
手冊與近 400 支官方範例腳本，寫出符合編碼規範的 XS 腳本，一鍵複製或存成 `.xs`。

---

## 三十秒上手

1. 雙擊 **`XS 工坊.exe`**（或輕量版的 `啟動 XS 工坊.bat`）
2. 瀏覽器自動打開，第一次會跳出**連線嚮導**，選一條 AI 路線
3. 開始講你的策略

想放到桌面：跑一次同資料夾裡的 `建立桌面捷徑.bat`。

---

## 四條 AI 連線路線

程式本身不含 AI，要接一個「大腦」。嚮導會自動偵測你這台電腦有什麼可用。

| 路線 | 適合誰 | 要準備什麼 | 花費 |
|---|---|---|---|
| **Claude Code 訂閱**（預設） | 已訂閱 Claude 的人 | 登入一次 Claude 帳號 | 吃訂閱額度，不另外付費 |
| **Anthropic API Key** | 沒訂閱、想最快開始 | 到 console.anthropic.com 申請金鑰並儲值 | 依用量計費 |
| **OpenRouter** | 想換模型或想省錢 | OpenRouter 金鑰 | 依用量計費 |
| **本地模型** | 有顯示卡、在意資料不外流 | Ollama 或 LM Studio 先開著 | 免費 |

金鑰只存在你自己電腦的 `secrets.json`，不會傳給任何第三方——這支程式只對你選的
AI 服務連線，沒有其他外連。

> **Windows 上走 Claude Code 路線的前提**：需要 Git for Windows 或 PowerShell 7
> 其中之一（Claude Code 本身的要求）。嚮導偵測不到會直接告訴你缺什麼、去哪裝。
> 不想裝就走 Anthropic API Key 路線，那條完全不需要。

---

## 寫好之後怎麼放進 XQ

1. 按腳本區塊右上角的**複製**，或**存成 .xs**
2. XQ 全球贏家 →「XScript 編輯器」，貼上
3. 按 **F6** 編譯
4. 編不過就把錯誤訊息整段貼回對話裡，軍師會修
5. 編譯成功後依類型加進指標／雷達／選股中心／自動交易

---

## 知識庫

`knowledge/` 是 XQ 官方 XS 資料整理成的知識庫，程式啟動時自動掛載：

- 編碼規範、函數速查、開發注意事項（每輪對話都在 prompt 裡）
- 900+ 資料欄位、全部內建與系統函數、近 400 支官方範例腳本（依當輪問題檢索）

**回答只以這份知識庫為準**。查不到的東西軍師會直說查不到，不會編一個看起來很像
的函數名給你——XS 是小眾語言，AI 憑印象寫出來的語法多半編譯不過。

想補自己的筆記，直接把 `.md` 檔丟進 `knowledge/`，重開程式就會被索引進去。

---

## 給開發者

```bash
pip install -r requirements.txt
python app.py                     # http://127.0.0.1:5101/

python tests/test_chat_flow.py    # 對話流程（含 [LOOKUP] 二段檢索）
python tests/test_oai_stream.py   # OpenAI 相容串流解析

python build.py lite              # 輕量版 zip
python build.py exe               # 綠色免安裝版
```

程式結構、設計決策與驗收紀錄見 [SPEC.md](SPEC.md)；
對外發行的門檻與策略見 [DISTRIBUTION.md](DISTRIBUTION.md)。
