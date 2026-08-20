# XS 語法開發：核心函數與注意事項補充大全

這是一份為 XS 開發者彙整的核心函數指南與注意事項大全，涵蓋了偵錯匯出、資料範圍控制、群體運算、選股排行以及逐筆大單解析等五大核心主題。

---

## 一、 print 指令與資料匯出實務

print 是 XS 語法中解決「變數不如預期」與「資料對位錯誤」的終極救星，除了除錯外，還能作為強大的自訂資料庫匯出工具。

### 函數寫法範例

基礎語法與字串格式化

```xs
// 印出字串與數值，搭配字串轉換函數與加號組裝
print(
    "日期: " + datetostring(date),
    "代碼: " + symbol,
    "收盤價: " + numtostr(close, 2)
);
```

高階應用：指定輸出路徑與動態檔名

可以利用 file() 函數與動態標籤（如 [symbol]、[scriptname] 等）來自動分類建檔：

```xs
// 依商品代碼自動分類建檔，例如：2330.tw.log
print(file("c:\print\[symbol].log"), "date:", date, "大戶買超:", value1);

// 將所有股票的數據集中匯出到同一個檔案 (類似 csv 概念)
print(file("c:\print\all_stocks_report.log"), "[symbol]", date, close, value1);
```

### 開發注意事項

1. 交易腳本強制規定：如果在「自動交易腳本（trading）」當中使用 print，必須強制指定檔案路徑（搭配 file 函數），否則系統無法正常印出數值。
2. 回測效能影響：
   - 策略雷達與選股中心回測時，必須手動勾選「啟動腳本內 print 指令」才能產出數據。
   - 極度拖慢速度：印出大量資料會大幅拖慢雲端伺服器的回測速度。建議只在小範圍抓漏時開啟，正式跑長天期回測前務必將 print 註解掉（加上 //）。

---

## 二、 資料範圍控制：settotalbar 與 setbackbar

這兩個函數用於控制腳本執行時的歷史 K 棒資料準備量，直接影響指標計算的正確性與跨頻率運算的效能。

### 函數寫法範例

**settotalbar (設定資料讀取總筆數)**

用來設定腳本執行時系統需準備的歷史 K 棒總數（不含當日即時洗價 K 棒）。

```xs
// 警示腳本預設只有 200 筆，若要計算 240 日均線必須強制加大讀取筆數
settotalbar(300);
value1 = average(close, 240);
```

**setbackbar (設定最大引用筆數 / 跨頻率優化)**

當腳本引用的歷史期數極深，或進行跨頻率運算時，預先告訴系統準備歷史緩衝區，能極大幅度減少系統不必要的運算。

```xs
// 在 5 分鐘頻率腳本中，計算日線的 20 日均線
input: _davglength(20, "日均線期數");

// 效能優化寫法：直接宣告需要引用 20 筆的「日」資料
setbackbar(_davglength, "d");

// 主頻率(5分k)只要極少 K 棒即可成功執行
value1 = average(getfield("close", "d"), _davglength);
```

### 開發注意事項

1. 預設值差異：若未寫入 settotalbar，系統會依腳本類型給予預設值：指標腳本為「全部歷史長度」、警示腳本為「200筆」、選股腳本為「10筆」。
2. 效能拿捏：settotalbar 設太大會明顯拖慢策略啟動與洗價速度（影響 for 迴圈總次數）；而在跨頻率抓取長天期資料時，強烈建議使用 setbackbar(期數, "頻率") 來取代放大 settotalbar，讀取速度會大幅提升。

---

## 三、 商品清單 (group) 應用

當策略從單一商品擴展到「一籃子商品」（如計算族群總營收、抓取個股所有權證），就必須使用商品清單。

### 函數寫法範例

```xs
// 宣告清單變數
group: _symbolgroup();
var: _sum(0), _i(0);

// 自動取得台灣50的成分股
_symbolgroup = getsymbolgroup("tse50.sj", "成分股");
value1 = groupsize(_symbolgroup); // 防呆：取得成分股總檔數

// 針對清單執行迴圈運算前，務必先確認清單內有商品
if value1 > 0 then begin
    for _i = 1 to value1 begin
        // 檢查該商品是否有"月營收"欄位，再進行跨商品取值
        if checksymbolfield(_symbolgroup[_i], "月營收", "m") then begin
            _sum += getsymbolfield(_symbolgroup[_i], "月營收", "m");
        end;
    end;
end;
```

### 開發注意事項

1. 索引值規定：清單內容的索引值從 1 開始，不可使用 0。若在腳本中直接印出 group 變數 (未加索引)，會導致「索引值超出範圍」的錯誤。
2. 唯讀屬性：清單是唯讀的 (read-only)，只能讀取代號，嚴禁在腳本內修改（如 `_symbolgroup = "2330.tw"` 會編譯失敗）。
3. 容量上限：一個 group 清單最多只能容納 3000 個商品。
4. 執行時機：處理清單的程序發生在「洗價之前」，系統會先建立好清單才開始執行歷史 K 棒的運算。
5. **getsymbolfield 參數限制**：`getsymbolfield` 的第一參數只接受字串常數、input 或 group 元素，**不接受 var 字串變數**。必須直接寫 `getsymbolfield(_symbolgroup[_i], "欄位")`，不可先存入 var 再傳入。

---

## 四、 rank 排行運算 (選股專用)

rank 是一個獨立的運算區塊，用於選股範圍內所有商品的橫向（cross-sectional）排名，能將策略從「絕對數值」昇華到「相對強弱」判斷。

### 函數寫法範例

```xs
// 1. 在最外層宣告排行物件 (預設由大到小排序)
rank _myrank begin
    // 必須在區塊內獨立宣告與抓取變數
    value1 = getfield("外資持股比例", "d");
    value2 = value1 - value1[1]; // 與昨日相比的差值
    retval = value2; // 指定以此數值作為排行依據
end;

// 2. 主邏輯：只挑選排名前 10 名的股票
if _myrank.pos <= 10 then ret = 1;

// 3. 輸出屬性供介面查看
outputfield(1, _myrank.value, 2, "外資持股增加比例");
outputfield(2, _myrank.pos, 0, "外資買超排名");
```

### 開發注意事項（四大鐵律）

1. **僅限選股**：此功能僅限「選股腳本」使用，指標、警示、交易皆不支援。
2. **必須放在最外層 (top level)**：rank 宣告絕對不可以被包在 if ... then 判斷式或 for 迴圈裡面。
3. **獨立變數空間 (scope 隔離)**：無法讀取腳本外部的 input 參數或自訂變數，所有需要的變數必須在 rank 區塊內重新抓取或運算。
4. **屬性呼叫格式**：呼叫如 `.pos` (名次)、`.value` (數值)、`.range` (百分比) 等屬性時，小數點前後不可以有空白。名稱不可與外部變數重複。

---

## 五、 tick 逐筆撮合與大單解析

在逐筆撮合時代，解析單筆明細需要克服「快市漏接」與「連續成交拆單」兩大問題。強烈建議使用高階函數 readticks。

### 函數寫法範例

readticks 函數能一次讀回上次洗價到目前的所有 tick，並自動將「連續成交序列」合併成一筆，存入二維陣列中。

```xs
// 宣告儲存 tick 資料的二維陣列
array: _tick_array[100, 12](0);

// 宣告紀錄讀取位置的持續性變數 (極重要)
var: intrabarpersist _readtick_cookie(0);
var: _idx(0), _row_count(0);

// 讀取從上次洗價到現在的連續合併 tick 資料
_row_count = readticks(_tick_array, _readtick_cookie);

for _idx = 1 to _row_count begin
    // 陣列[_idx, 5]: 1 代表外盤；陣列[_idx, 10]: 連續成交總量
    if _tick_array[_idx, 5] = 1 and _tick_array[_idx, 10] >= 100 then begin
        ret = 1; // 發現外盤連續成交大於 100 張的大單
        break;
    end;
end;
```

### 開發注意事項

1. **tick 欄位 vs 報價欄位**：tick (`getfield("close", "tick")`) 能保證與當下 K 棒完全對齊；而報價欄位 (`q_last`) 是系統當下的最新行情，在快市中可能與洗價 K 棒不一致。
2. **禁止變數儲存前期調用**：跨頻率抓 tick 時，請直接寫 `getfield("欄位", "tick")`，絕對不要先存入變數 value1 再呼叫 `value1[1]`，這會發生嚴重的對位問題抓錯資料。
3. **環境設定與效能**：
   - 加入雷達時，務必在執行頻率設定處勾選「逐筆洗價」。
   - 歷史回測 tick 資料運算極度耗時且龐大，建議先用「極短的時間區間」進行測試。

---

## 六、 函數參數型別陷阱（實戰踩坑）

XS 對函數參數的型別檢查很嚴，以下兩個是實戰編譯失敗的高頻雷點（2026-07 RRG 選股腳本踩過）。

### iff 的值參數只吃 Numeric，不能塞 true/false

`iff(條件, A, B)` 的 A、B **必須是數值（Numeric）**，塞布林字面值 `true` / `false` 會編譯錯：「函數 IFF：第 2 個參數應該是 Numeric」。

要產生布林開關，直接用**比較運算式**（它本身就回傳 TrueFalse）：

```xs
// 錯誤：iff 值參數塞 true/false
// _adj = iff(_mode = 1, true, false);   // 編譯錯：第 2 參數應為 Numeric

// 正確：比較運算式本身即回傳 TrueFalse
_adj = (_mode = 1);
```

### adjusted 參數只吃「字面常數」，不吃變數

`getfield` / `getsymbolfield` 的 `adjusted:=` 參數**只接受字面常數 `true` / `false`**，傳變數會編譯錯：「第 N 個參數應該是 TrueFalse」——**即使那個變數確實是布林型別也一樣**。

要用參數切換「還原值／原始值」，必須用 `if` 分兩塊、各自把 `adjusted` 寫死：

```xs
// 錯誤：adjusted 傳變數（即使 _adj 是布林也不行）
// _adj = (_mode = 1);
// value1 = getfield("收盤價", "D", adjusted:=_adj);   // 編譯錯：第 3 參數應為 TrueFalse

// 正確：if 分兩塊，adjusted 寫死字面常數
if _mode = 1 then
    value1 = getfield("收盤價", "D", adjusted:=true, default:=0)
else
    value1 = getfield("收盤價", "D", adjusted:=false, default:=0);
```

> 同理 `getsymbolfield(..., adjusted:=true/false, ...)` 也只吃字面常數。若還有多個商品分支（例如多個基準）× 還原/原始，就用外層 `if _adjust` 包住整組分支，內層各基準的 `adjusted` 全部寫死，避免任何變數傳入。
