# XS 工坊 XS Studio — 規格

立案日期：2026-08-21

## 目標

讓 XQ 全球贏家的使用者有一個**獨立、快速、點開就能用**的視窗，用講話的方式把交易
情境變成一支能編譯執行的 XScript 腳本，不必先變成工程師、也不必先學會怎麼用
Claude Code。

參照對象是萬界 OmniWorld 與 SillyTavern 的形態：本機伺服器 ＋ 瀏覽器介面 ＋
一個桌面捷徑。

## 範疇

**做**
- 本機 Flask 伺服器（127.0.0.1:5101，被占用會自動往上找）＋ 瀏覽器對話介面
- 自動掛載 `knowledge/` 的 XS 知識庫，並在伺服器側做段落檢索
- 四種 AI 後端可切換，附首次啟動的連線嚮導與實際連線測試
- 兩種分發形態：綠色免安裝 EXE、輕量 zip

**不做**
- 不直接操作 XQ 全球贏家（那是 `xq-desktop-operator` Skill 的守備範圍）
- 不做雲端帳號、不做多人協作、不收任何資料回傳
- 不編譯 XS（編譯是 XQ 端的事；編譯錯誤由使用者貼回來，走迭代模式修）

## 輸入

| 來源 | 內容 |
|---|---|
| `knowledge/` | xs-skill 知識庫（17 份 md，2.4 MB）。原始來源 `xs-skill.zip`，zip 內檔名為 cp950，解壓時已轉碼 |
| `config.json` | provider／model／本地端點。首次啟動由嚮導寫入 |
| `secrets.json` | API 金鑰。gitignore，永不進版控與安裝包 |
| 使用者輸入 | 自然語言的策略描述，或貼上既有 XS 腳本要求修改 |

## 輸出

- 對話介面裡的完整 XS 腳本（```xs 圍籬），可一鍵複製或存成 `.xs`（UTF-8 with BOM）
- 每輪附「參考了知識庫哪幾筆」的引用清單
- 匯入 XQ 的步驟指引

## 架構

```
app.py            Flask 路由、SSE 串流、[LOOKUP] 二段檢索的伺服器側流程控制
xs/paths.py       原始碼跑法 vs 打包跑法的路徑解析（data_dir / bundle_dir）
xs/config.py      設定與金鑰讀寫（原子寫入）
xs/knowledge.py   知識庫索引與檢索（取代 Claude Code 的 Grep）
xs/prompt.py      system prompt 組裝、[LOOKUP] 協定
xs/llm.py         四後端 ＋ dispatcher ＋ 連線偵測（改編自萬界 omni/llm.py）
templates/ static/  前端（零外部相依，離線可跑）
```

### 關鍵設計決策

**檢索做在伺服器側，不靠模型的工具能力。**
原版 `/xs` skill 跑在 Claude Code 裡，用 Read／Grep 翻手冊。本前台要能接 API key、
OpenRouter、本地模型——那些後端沒有檔案工具。所以由伺服器先撈好段落塞進 prompt，
四種後端才會有一致的品質。

**知識庫分兩層。** 全部 2.4 MB 塞進 prompt 既貴又稀釋重點：
- 常駐層（23K 字）：編碼規範＋函數速查＋開發注意事項，每輪都在，放 system 最前段吃前綴快取
- 檢索層：依當輪問題撈，預算 45K 字、限 8 筆、同一來源最多 3 筆

**限制同一來源筆數是必要的。** 範例腳本又短又多，純比分數會讓五筆全是範例，
把「這個欄位到底叫什麼名字」的手冊條目擠掉——而那正是最容易寫錯的地方。

**`[LOOKUP]` 二段檢索補回 grep 能力。** 模型判斷手邊節錄不足時，只回一行
`[LOOKUP]關鍵字[/LOOKUP]`，伺服器據此重撈再問一次，上限兩次。
伺服器會扣住回應開頭直到確認不是查詢指令才放行，使用者看不到這個內部往返，
只看到「軍師正在翻手冊…」。

**中文檢索用 n-gram，不引入斷詞套件。** 綠色免安裝包要維持零額外相依。
2764 筆記錄線性掃描實測 7–24 ms，沒有引入索引結構的必要。

## 驗收

| 項目 | 方式 | 結果 |
|---|---|---|
| 知識庫索引 | `tests` 外的實跑：17 檔、2764 筆、建索引 23 ms | 通過 |
| 檢索品質 | 五個代表性問題，逐筆檢查撈到的來源是否對題 | 通過（欄位／函數／範例三類都撈得到） |
| 端到端對話 | 走正式 `/api/chat` ＋ Claude Code SDK 實跑「月營收年增率連續三個月成長」 | 通過：首字 5.3 s、全長 29.6 s、腳本符合四大區塊與 `default:=0`／中括號取前期兩條鐵則 |
| `[LOOKUP]` 流程 | `tests/test_chat_flow.py`，7 項（含扣字邊界、次數上限、標記外洩） | 全過 |
| OpenAI 相容串流 | `tests/test_oai_stream.py`，4 項（假端點跑真 HTTP） | 全過 |
| 連線偵測 | `/api/probe` 實跑 `claude auth status` | 通過：回報已登入帳號與訂閱等級 |
| 介面 | Playwright 桌面 1440／手機 420 截圖 ＋ console 錯誤檢查 | 通過（0 錯誤；修掉 4 項視覺缺陷，見 WORKLOG） |
| 打包產物 | 模擬 frozen 狀態實跑 dist 內容 | 通過：頁面 200、靜態檔 200、知識庫讀到 EXE 旁那份 |
| EXE 啟動 | 雙擊 | **未完成驗收**——本機 Smart App Control 封鎖未簽章執行檔（WinError 4551），見 DISTRIBUTION.md |

**未驗證項目（誠實記錄）**：Anthropic API 與 OpenRouter 兩條路線的實際線上呼叫
未測（手上無金鑰）。兩者共用的串流解析與錯誤處理已用假端點驗過，
但真實服務的回應細節（模型名稱、錯誤碼語意）尚未對照。

## 邊界

- 只監聽 127.0.0.1，不對外開放；沒有驗證機制，因為預設沒有第二個使用者
- 不碰使用者的 XQ 安裝、不寫入 XQ 目錄
- 金鑰不進版控、不進安裝包、不回傳；前端只拿得到遮罩值
- 對話歷史只保留最近 12 輪送進 prompt，避免無限膨脹
- SDK 路線關閉所有工具（`disallowed_tools=["*"]`、`setting_sources=[]`），
  不讀使用者的 `~/.claude` 設定，避免與他們自己的 Claude Code 互相污染

## 相關

- 知識庫原始來源：`xs-skill.zip`（老墨的 AI 交易室 `/xs` 安裝包）
- XS 語法本身的權威：`xq-trade-ai` Skill
- 要在真的 XQ 上點擊操作：`xq-desktop-operator` Skill
- LLM 層改編自：`D:/Workspace/projects/omniworld/omni/llm.py`
