# 推廣與環境建置

要讓一個 XQ 用戶真的用上 XS 工坊，他得跨過三道門檻。每一道都會流失人，
所以逐道盤點「現在有多難、我們做了什麼降阻、還剩什麼問題」。

事實類敘述都標了查證日期；未經實測的地方寫明未測，不假裝知道。

---

## 門檻一：打得開嗎（Windows 的阻擋）

### 實測現況（2026-08-21，Windows 11 Pro 26200）

PyInstaller 打出來的**未簽章** EXE，在本機被 **Smart App Control 直接封鎖**，
`CreateProcess` 回 `WinError 4551`（應用程式控制原則已封鎖此檔案），連續三次重試皆同。
確認機器狀態：`HKLM\SYSTEM\CurrentControlSet\Control\CI\Policy` 的
`VerifiedAndReputablePolicyState = 1`，即 SAC 為強制模式。

這不是打包做錯了。打包產物本身已驗證正確（模擬 frozen 狀態實跑，頁面 200、
靜態檔 200、知識庫讀到 EXE 旁那份），被擋的是 Windows 的執行政策。

### 這影響多少人

SAC 只在**乾淨安裝**的 Windows 11 上預設開啟，升級上來的機器預設關閉。
所以會是一部分人踩到、不是全部。但踩到的人是**直接打不開**，不是跳警告——
最糟的一種流失。沒踩到 SAC 的人也至少會遇到一次 SmartScreen「Windows 已保護您的電腦」
的藍色警告視窗，要點「其他資訊 → 仍要執行」才能開。

### 三個選項

| 選項 | 阻力 | 成本 | 適用時機 |
|---|---|---|---|
| **A. 輕量 zip ＋ bat**（已做） | 要先裝 Python，但**完全不會被擋** | 0 | 現在就能發，種子用戶／內部先跑 |
| **B. 買程式碼簽章憑證，簽 EXE** | 簽完仍需累積下載量建立信譽，前期還是可能跳警告 | 憑證年費 | 要對外大規模推的必經之路 |
| **C. 走 XQ 官方既有安裝／更新通道** | 對使用者阻力最低 | 內部協調 | 若這支要變成 XQ 官方功能 |

輕量版跑的是使用者自己那份 `python.exe`——微軟認得的簽章，SAC 與 SmartScreen 都不攔。
這是它今天就能發的原因，也是為什麼 `build.py` 保留兩種產出而不是只做 EXE。

### 關於憑證，兩件查證過的事（2026-08-21）

1. **台灣公司目前不符合 Azure Artifact Signing（原 Trusted Signing）資格。**
   微軟該服務的公開信任憑證開放地區為美國、加拿大、歐盟、英國、澳洲、紐西蘭、
   日本、南韓、新加坡、瑞士、挪威、以色列——**不含台灣**。
   所以 XQ 要簽章，得走傳統 CA（DigiCert／Sectigo／SSL.com 等）的 OV 或 EV 憑證。

2. **不必為了 SmartScreen 多付 EV 的錢。**
   微軟自 2024 年 3 月更新信任根計畫後，EV 憑證不再享有 SmartScreen 的即時信任特權；
   EV 與 OV 現在都是靠下載量累積信譽。EV 仍有其他價值（硬體金鑰保管、驗證層級），
   但「買 EV 就不會跳警告」已經不成立。OV 憑證足夠，價差可以省。

   另外要有心理準備：**簽了章也不保證 SAC 立刻放行**——SAC 除了看簽章還看雲端信譽，
   新發布的簽章程式初期仍可能被擋，要靠安裝量累積。

3. **SAC 現在可以關了。** 微軟在 2026 年 3 月的 Windows 11 更新中放寬，
   使用者可以自行關閉 SAC 而不必重灌系統（在此之前關掉就回不去）。
   這讓「請使用者暫時關閉 SAC」從不可行變成可行的最後手段，但仍不該當成主要方案——
   叫人關掉防護來裝你的軟體，信任成本很高。

### 建議

**現在**：輕量版對種子用戶與課程學員發，同時把 EXE 版給願意點「仍要執行」的人。
**接下來**：若確定要對外推，先取得 OV 程式碼簽章憑證並把簽章步驟接進 `build.py`；
若這支要掛 XQ 品牌，優先走選項 C，一次解決信譽問題。

---

## 門檻二：接得上 AI 嗎

這是原本最容易勸退人的一關——「你要先去申請 API、儲值、貼金鑰」對非工程背景的
交易者是硬門檻。降阻做法：

### 已做的四件事

**1. 內附一份 Claude Code。**
`claude-agent-sdk` 套件裡自帶完整的 Claude Code 執行檔（230 MB，也是 EXE 版體積的
主要來源）。程式會優先用使用者自己裝的版本，沒有才用內附這份。
意思是：**有 Claude 訂閱但從沒裝過 Claude Code 的人，不必先裝 Node、不必碰終端機**，
登入一次就能用。這是 EXE 版體積換來的最大價值。

**2. 一鍵登入。**
嚮導的「登入 Claude 帳號」會另開終端機跑 `claude auth login`，使用者照著點瀏覽器
完成即可，回來按「重新偵測」。登入狀態由 `claude auth status` 實際查詢，
會顯示「已登入 someone@example.com（max 訂閱）」——不是猜的。

**3. 缺什麼講什麼。**
Claude Code 在 Windows 需要 **Git for Windows 或 PowerShell 7** 其中之一
（已實測確認：兩者皆無時 CLI 直接拒絕啟動）。嚮導偵測不到會明講缺哪個、附下載連結，
並提示「不想裝就走 Anthropic API Key 路線，那條完全不需要」。
以前這種問題會變成「測試連線一直失敗，不知道為什麼」。

**4. 測試連線是真的送一次請求。**
不是 ping、不是檢查金鑰格式，是實際跑一次極短對話並把 AI 的回覆秀出來。
使用者看到「連線成功，AI 回覆：『可用』」才算數。

### 四條路線的實際阻力

| 路線 | 使用者要做的事 | 阻力 | 驗證狀態 |
|---|---|---|---|
| Claude Code 訂閱 | 登入一次（＋可能要裝 Git for Windows） | 低 | **已實測**：測試連線 5 秒、完整腳本 30 秒 |
| Anthropic API Key | 申請帳號、儲值、貼金鑰 | 中 | 程式已實作，**未用真實金鑰實測** |
| OpenRouter | 同上 | 中 | 同上；共用的串流解析已用假端點驗過 |
| 本地模型 | 先裝 Ollama／LM Studio 並下載模型 | 高（但完全免費） | 偵測與串流已用假端點驗過 |

> 本地模型那條要誠實提醒使用者：小模型不熟 XS 語法，寫出來常編譯不過。
> 介面上已經寫了「挑 14B 以上、擅長程式的模型會好很多」。

---

## 門檻三：第一支腳本寫得出來嗎

裝好、接上了，如果第一次對話沒得到能用的東西，人就不會有第二次。

### 已做的降阻

- **起手式**：側欄五個可直接點的真實範例，涵蓋選股／警示／指標／自動交易／改腳本
  五種類型，點了就填進輸入框。不必自己想第一句話怎麼講。
- **不無謂盤問**：prompt 明確要求「使用者講得夠清楚就直接動手，不要為了湊問題把人
  擋在門外」。真的缺關鍵資訊才問，而且一次問完。
- **交付到位**：每支腳本附「複製 / 存成 .xs」按鈕與匯入 XQ 的步驟（含按 F6 編譯）。
- **編譯失敗有下一步**：明白告訴使用者「編不過就把錯誤訊息整段貼回來」，
  迭代模式會做外科手術式最小修改，不整支重寫。
- **不編造**：查不到就說查不到。對這個族群來說，一個看起來很像但編譯不過的函數名，
  比誠實說「查不到」傷害大得多——他們沒有能力分辨。

### 還沒做、值得做的

- **範例腳本畫廊**：把知識庫裡近 400 支官方範例做成可瀏覽的頁面，讓人「先看到成品
  再開口」。素材已經在 `knowledge/` 裡，只差一個列表頁。
- **對話存檔**：目前重開就沒了。使用者調了半天的腳本會想留著。
- **一鍵回報**：編譯錯誤訊息若能一鍵貼回，比叫人自己複製更順。

---

## 擴散的槓桿在哪

三道門檻是「不流失」，要主動擴散還需要讓人願意講出去。三個現成的槓桿：

1. **課程夾帶**：「老墨的 AI 交易室」已經在發 `/xs` 安裝包了，學員名單就是最精準的
   種子。輕量版可以直接接上現有發放流程，零額外成本。

2. **成品自帶傳播**：使用者存下來的 `.xs` 檔會在社群裡互相傳。
   腳本開頭的說明區可以帶一行來源註記——這是最自然的口碑管道，
   不必做任何推廣動作。（目前未做，一行 prompt 就能加。）

3. **知識庫可擴充**：`knowledge/` 丟 `.md` 進去就會被索引。
   這讓進階用戶能把自己的筆記變成軍師的知識，也讓 XQ 之後補官方文件不必改程式。
   願意投入的人會變成留下來的人。

---

## 資料來源

- [Windows 11 Smart App Control explained — Computerworld](https://www.computerworld.com/article/4043925/windows-11-smart-app-control-explained.html)
- [Microsoft confirms you can soon disable Smart App Control without reinstalling Windows 11](https://www.windowslatest.com/2025/12/16/microsoft-confirms-you-can-soon-disable-smart-app-control-without-reinstalling-windows-11/)
- [SmartScreen reputation for Windows app developers — Microsoft Learn](https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/smartscreen-reputation)
- [Code signing options for Windows app developers — Microsoft Learn](https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/code-signing-options)
- [Which Code Signing Certificate do I Need? EV or OV? — SSL.com](https://www.ssl.com/faqs/which-code-signing-certificate-do-i-need-ev-ov/)
- [Trusted signing for other countries — Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/2243504/trusted-signing-for-other-countries)
- [Quickstart: Set up Artifact Signing — Microsoft Learn](https://learn.microsoft.com/en-us/azure/artifact-signing/quickstart)
