# xscript 程式交易語法規格書

本文件整合了 xscript 的指標繪圖、選股排行與自動交易系統的詳細語法規格與邏輯。

## 1. 指標繪圖 (Indicator & Plotting) [Source: _2025_指標語法.docx]

本章節定義如何在技術分析圖表上繪製線條、K棒、填色及文字。

### 1.1 設定繪圖樣式 (SetPlotStyle)
[cite_start]**定義：** 用於設定繪圖序列的屬性。建議在腳本開頭呼叫，設定預設值（Compile-time 處理）[cite: 103, 106]。

**完整語法：**
```xscript
SetPlotStyle(
    序列編號,
    [cite_start]name := "序列名稱",             // [cite: 410]
    plotType := pt.line | pt.segment | pt.bar | pt.shape | pt.fill | pt.k, // [cite: 411]
    lineStyle := ls.solid | ls.dash | ls.dot | ls.dashdot | ls.dashdotdot, // [cite: 412]
    lineWidth := 1 | 2 | 3 | 4 | 5 | 6 | 7, // [cite: 413]
    lineColor := lc.solid | lc.zero | lc.updown, // 指定線條顏色邏輯 (單色/正負/漲跌) [cite: 414]
    barStyle := bs.solid | bs.frame | bs.zero | bs.updown, // [cite: 415]
    shapeType := shape.icon | shape.emoji, // [cite: 416]
    shapeName := icon.abc | emoji.abc,     // [cite: 417]
    size := size.S | size.M | size.L,      // [cite: 418]
    location := loc.price | loc.top | loc.bottom | loc.aboveBar | loc.belowBar, // [cite: 419]
    textColor := tc.default | tc.solid | tc.zero | tc.updown, // 文字欄位顏色樣式 
    alignType := align.left | align.right | align.center,     // 文字對齊方式 [cite: 423]
    color := Color.Red | RGB(r,g,b),      // 主顏色 [cite: 425]
    color2 := Color.Red | RGB(r,g,b),     // 副顏色 (雙色設定用) [cite: 426]
    color3 := Color.Red | RGB(r,g,b),     // K線陰線實體顏色 [cite: 350, 427]
    color4 := Color.Red | RGB(r,g,b),     // K線陰線外框顏色 [cite: 351, 428]
    valueFormat := vf.none | vf.auto | vf.full | vf.percent | vf.wy | vf.wz | vf.qz | vf.kmb, // [cite: 430]
    valueDP := dp.auto | 0 | 1 | 2 | 3 | 4, // 小數點位數 [cite: 431]
    axis := 1 | 2 | ..,                    // 指定座標軸編號 [cite: 432]
    visible := 1 | 0,                      // 預設是否顯示 [cite: 433]
    visibility_quickedit := 1,             // 是否提供介面快速切換顯示 [cite: 434]
    editable := 1 | 0,                     // 0=關閉 UI 設定 (強制依腳本) 
    kfill := 1 | 0,                        // 陽線是否填滿 [cite: 436]
    kfill2 := 1 | 0                        // 陰線是否填滿 [cite: 437]
);
```

**詳細參數列表 (Parameter Dictionary)：**
- **name (string):** 序列名稱，顯示於圖表標題。
- **plotType:** 繪圖類型。
    - pt.line: 線條 (預設)。
    - pt.bar: 柱狀圖。
    - pt.shape: 點 (搭配 shapeType 使用)。
    - pt.segment: 線段。
    - pt.fill: (2025/01/02 新增) 填色區域 。
    - pt.k: (2025/01/02 新增) K線樣式 。
- **lineColor:** 線條顏色邏輯。
    - lc.solid: 單色。
    - lc.updown: (2025 新增) 漲紅跌綠雙色線條 。
- **color / color2:**
    - 一般模式：color 為主顏色，color2 為副顏色。
    - K線模式 (pt.k)：color=陽線實體，color2=陽線外框 。
- **color3 / color4:** (2025/01/02 新增)
    - K線模式專用：color3=陰線實體，color4=陰線外框 。
- **kfill / kfill2:** (2025/01/02 新增)
    - kfill: 陽線是否填滿 (1=填滿, 0=空心)。
    - kfill2: 陰線是否填滿 (1=填滿, 0=空心) 。
- **valueFormat:** 數值顯示格式。
    - vf.wy: 萬/億單位。
    - vf.percent: 百分比。
    - vf.full: 完整數值 。
- **editable:** (2025 新增) UI 設定鎖定。
    - 1: 開放使用者調整 (預設)。
    - 0: 關閉 UI 設定，強制依照腳本樣式顯示 。

**重要功能說明：**
- **K線樣式 (pt.k)：**支援自訂陽線/陰線的實體與外框顏色 (color~color4) 及填滿狀態 (kfill, kfill2) 。
- **雙色線條：**lineColor:=lc.updown 可繪製漲紅跌綠的線條 。
- **UI 鎖定：**若 editable:=0，使用者無法在介面上修改此指標樣式，保證顯示與腳本設計一致 。

### 1.2 輸出數值與標籤 (Plot & Label)
- **Plot(序列, 數值):** 每根 Bar 傳入數值。請勿在此設定樣式，樣式應由 SetPlotStyle 處理 。
- **SetPlotLabel(序列, label, ...):** 設定動態標題與數值格式。
    - 語法：SetPlotLabel(序列, "標題", valueFormat:=..., valueDP:=...) 。
- **SetPlotColor(序列, color):** 依條件動態改變某根 Bar 的顏色。
    - 注意：系統會在 Compile-time 收集所有出現過的顏色，並在 UI 提供調整介面 。
- **PlotText(序列, "字串"):** 輸出文字類型欄位 。

### 1.3 繪圖工具 (Tool Syntax)
此類語法用於在圖表特定座標繪製物件，非連續指標 。
- **Tool_Line:** 繪製趨勢線。
    - 語法：Tool_Line(x1, y1, x2, y2, color:=..., width:=..., style:=..., extend:=extend.none|extend.left|extend.right|extend.both) 。
- **Tool_Text:** 繪製文字與圖示。
    - 語法：Tool_Text(x, y, text:="...", location:=..., textAlign:=..., shapeType:=..., shapeName:=...) 。

##　2. 選股排行 (Ranking Syntax) [Source: _2024_排行語法.docx]
本章節定義如何在選股腳本中進行跨商品的排序與統計。

### 2.1 排行物件定義 (Rank Object)
必須在 Top-level 定義 rank 物件，系統會先執行此區塊統計所有商品後，才執行主選股邏輯 。

**語法：**
```xscript
rank 物件名稱 [asc | desc] begin
    // 支援變數宣告與計算
    retval = [排序數值]; // [cite: 663]
end;
```

**排行屬性 (Attributes)：** 透過 物件名稱.屬性 存取統計結果：
- pos: 排名 (1 為第一名) 。
- range: 排行百分比 (pos / count * 100) 。
- pr: 百分位排名 (Percentile Rank) 。
- count: 參與排行的商品總數 。
- value: 該商品的原始數值 (retval) 。
- avgvalue: 所有商品數值的平均值 。
- medvalue: 所有商品數值的中位數 。
- stdvaluep: 所有商品數值的母體標準差 。
- minvalue / .maxvalue: 所有商品中的最小/最大值 。
- Q1 / .Q3: 第 25% 與 75% 分位數值 (用於離群值判斷) 。
- isvalid: 布林值，代表該商品是否有效參與排行 。

### 2.2 離群值排除 (Outlier Removal)
在 rank 區塊內使用，直接將異常值排除於排行之外 。

**語法：**
```xscript
SetRemoveOutlier("zscore", value:=3); // 排除標準差 > 3 的數值 [cite: 911]
// 或
SetRemoveOutlier("IQR", value:=1.5);  // 排除超過 1.5 倍 IQR 的數值 [cite: 912]
```

## 3. 自動交易 (Auto-Trading Syntax) [Source: 2021交易語法_20210728.docx]
本章節定義自動交易的指令、邏輯與安控機制。

### 3.1 核心交易指令
透過調整「目標部位 (Position)」來觸發交易 。

**語法：**
- SetPosition(部位, [價格], label:="..."): 設定目標部位至指定數量。
- Buy(數量, [價格], label:="..."): 多頭加碼 (若有空單會先平倉)。
- Sell(數量, [價格], label:="..."): 多頭減碼 (不會翻空，最小為 0)。
- Short(數量, [價格], label:="..."): 空頭加碼 (若有多單會先平倉)。
- Cover(數量, [價格], label:="..."): 空頭減碼 (不會翻多，最大為 0)。

**重要邏輯：**
- **優先順序：** 每次洗價只執行**第一個**被呼叫的交易指令 。
- **虛擬委託：** 系統比較 Position (目標) 與 Filled (實際)，產生虛擬委託，底層再依庫存狀況拆解為實際委託 (如現股賣出+現先賣) 。
- **價格處理：**
    - MARKET: 市價單 。
    - AddSpread(Price, Offset, limit:=True): 計算滑價。limit (2025/09/19新增) 控制是否受漲跌停限制 。

### 3.2 交易安控機制 (Risk Control)
包含策略層級與帳號層級的安控 。
- **單一商品/策略整體最大部位：** 檢查部位絕對值 。
- **每日最多進場次數：** 翻轉部位或從 0 進場才算一次 。
- **每分鐘最多交易次數 (2024/11/29新增)：** 避免高頻訊號，超過次數會擋下委託 。
- **期貨每日進場金額上限 (2024/11/22新增)：** 計算期貨原始保證金累積值 。
- **金額上限邏輯：** 分為「預估額度」(下單前計算) 與「實際額度」(成交/刪改後更新) 。

### 3.3 回測設定 (Backtesting)
- **模擬逐筆洗價：** 決定是否在每根 K 棒內多次洗價 (模擬 Tick 行為) 。
- **每日部位歸零：** 每日收盤強制平倉 。
- **交易費用：** 可設定股票 (%) 與期貨 (元/口) 費用 。

### 3.4 交易歷程函數
- FilledRecordCount, FilledRecordPrice(N), FilledRecordQty(N) 。
- FilledAvgPrice(): 取得目前未平倉部位的平均成本 (採先進先出計算) 。