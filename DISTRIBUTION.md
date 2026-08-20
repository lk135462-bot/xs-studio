# 推廣與環境建置

要讓一個 XQ 用戶真的用上 XS 工坊，他得跨過三道門檻。每一道都會流失人，
所以逐道盤點「現在有多難、我們做了什麼降阻、還剩什麼問題」。

事實類敘述都標了查證日期；未經實測的地方寫明未測，不假裝知道。

---

## 門檻一：打得開嗎（Windows 的阻擋）

**結論：已解決。** 免安裝版在開著 Smart App Control 的機器上實測可正常啟動。
以下記錄怎麼撞牆、怎麼繞過，因為這個坑會反覆出現在任何 Windows 桌面發行上。

### 撞到的牆（2026-08-21 實測，Windows 11 Pro 26200）

PyInstaller 打出來的**未簽章** EXE 被 **Smart App Control 直接封鎖**，
`CreateProcess` 回 `WinError 4551`（應用程式控制原則已封鎖此檔案），連續三次重試皆同。
機器狀態確認：`HKLM\SYSTEM\CurrentControlSet\Control\CI\Policy` 的
`VerifiedAndReputablePolicyState = 1`，SAC 為強制模式。

打包產物本身沒問題——被擋的是 Windows 的執行政策，不是我們的程式。

### 繞過的方式：不要自己產生執行檔

關鍵領悟是「SAC 管的是**可執行映像**，不是程式語言」。
所以問題不在「用不用 Python」，而在**整包裡有沒有一支沒人擔保的 .exe**。

免安裝版因此改成只用「別人已經簽好、而且信譽良好」的執行檔：

| 執行檔 | 簽署者 | 實測狀態 |
|---|---|---|
| `python\python.exe` | CN=Python Software Foundation（DigiCert 簽發） | Valid |
| `claude_agent_sdk\_bundled\claude.exe` | CN=Anthropic, PBC（EV，Private Organization） | Valid |

我們自己只出 `.py` 與 `.bat`——都不是可執行映像，不受該政策管轄。
Python 用官方 **embeddable 版**（python.org 的 zip），解壓即用、不寫登錄檔、不裝進系統。

`build.py portable` 每次打包都會跑一次簽章稽核，把 pip 現場產生的 console-script 殼
（`flask.exe`／`uvicorn.exe` 之類）與 pywin32 的 `Pythonwin.exe`／`pythonservice.exe`
清掉——那些我們一支都不會執行，留著只是白白給 SAC 攔截的理由。
稽核不通過會在打包輸出直接示警，不靠記憶宣稱「應該都簽了」。

### 實測結果

- 免安裝版在 SAC 強制模式的機器上**啟動成功**，首頁 HTTP 200、知識庫 17 檔 2764 筆掛載。
- 走內附 `claude.exe`（模擬「從沒裝過 Claude Code」的使用者）實跑對話成功。
- 完整對話：首字 3.9 秒、全長 29 秒，腳本結構與規範正確。
- 體積：資料夾 380 MB、壓縮檔 **125 MB**。

### 三種發行形態的現況

| 形態 | 使用者要做什麼 | 會被擋嗎 | 體積 | 狀態 |
|---|---|---|---|---|
| **免安裝版**（主力） | 解壓縮、雙擊 | **不會**（已實測） | 125 MB zip | 可以發 |
| 輕量版 | 先裝 Python，再解壓縮雙擊 | 不會 | 0.4 MB zip | 可以發，適合工程背景的人 |
| PyInstaller 版 | 解壓縮、雙擊 | **會**（SAC 封鎖／SmartScreen 警告） | 324 MB | 需簽章憑證才發得出去 |

`build.py exe` 保留給「已經有程式碼簽章憑證」的場景，刻意不列入 `build.py all`。

### 還是想走 PyInstaller／要簽章的話（查證於 2026-08-21）

1. **台灣公司目前不符合 Azure Artifact Signing（原 Trusted Signing）資格。**
   該服務的公開信任憑證開放地區為美國、加拿大、歐盟、英國、澳洲、紐西蘭、日本、
   南韓、新加坡、瑞士、挪威、以色列——**不含台灣**。要簽章得走傳統 CA
   （DigiCert／Sectigo／SSL.com 等）的 OV 或 EV 憑證。

2. **不必為了 SmartScreen 多付 EV 的錢。** 微軟自 2024 年 3 月更新信任根計畫後，
   EV 憑證不再享有 SmartScreen 的即時信任特權；EV 與 OV 現在都是靠下載量累積信譽。
   而且**簽了章也不保證 SAC 立刻放行**——SAC 除了看簽章還看雲端信譽。

3. **若專案改為開源，SignPath Foundation 提供免費的 OV 等級簽章**給符合資格的
   開源專案（需公開原始碼與認可的開源授權，由他們的 HSM 保管金鑰並驗證建置來源）。

4. **SAC 現在可以關了。** 微軟在 2026 年 3 月的 Windows 11 更新中放寬，
   使用者可自行關閉 SAC 而不必重灌系統。但別當主要方案——
   叫人關掉防護來裝你的軟體，信任成本很高。

---

## 門檻二：接得上 AI 嗎

這是原本最容易勸退人的一關——「你要先去申請 API、儲值、貼金鑰」對非工程背景的
交易者是硬門檻。降阻做法：

### 已做的四件事

**1. 內附一份 Claude Code。**
`claude-agent-sdk` 套件裡自帶完整的 Claude Code 執行檔（230 MB，也是安裝包體積的
主要來源）。意思是：**有 Claude 訂閱但從沒裝過 Claude Code 的人，
不必先裝 Node、不必碰終端機**，登入一次就能用。這是體積換來的最大價值，
也是免安裝版能「零安裝上手」的關鍵。

挑哪一支 `claude` 有講究，順序是**原生 `claude.exe` → 內附 `claude.exe` → 最後才是 `.cmd`**。
原因是 `claude-agent-sdk` 自 0.2.142 起**拒絕執行 `.bat`／`.cmd`**
（「Windows runs .bat/.cmd files via cmd.exe, which can execute commands injected
through CLI arguments」，是它刻意的安全設計）。
用 npm 裝 Claude Code 得到的正是 `claude.cmd`——若照直覺「使用者自己裝的優先」，
在裝了新版 SDK 的機器上每一次對話都會直接失敗。
`tests/test_cli_detection.py` 專門鎖住這個順序。

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
| Claude Code 訂閱 | 登入一次（＋可能要裝 Git for Windows） | 低 | **已實測**：測試連線 5 秒、完整腳本 29–30 秒；內附 CLI 路徑亦已實測 |
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
   種子。125 MB 的免安裝版可以直接接上現有發放流程（雲端硬碟連結即可），零額外成本。

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
- [SignPath Software Integrity Platform — 開源專案免費簽章](https://signpath.io/solutions/open-source-community)
- [Windows embeddable package — python.org 下載頁](https://www.python.org/downloads/windows/)
