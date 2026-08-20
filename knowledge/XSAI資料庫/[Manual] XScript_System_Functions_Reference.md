---
title: XS完整手冊 - 系統函數
category: 系統函數
tags: [XS語法, 系統函數, DaysToExpiration, PSY, xf_MACD, LastDayOfMonth, OHLCPeriodsAgo, TrueLow, WMA, MTM, VR, CCI, KeltnerMA, Covariance, BSDelta, KeltnerUB, GetBarOffsetForYears, VariancePS, MACD, NthDayofMonth, DwLimit, ArrayLinearRegSlope, formatMQY, Stochastic, CloseD, MoM, K_Value, TrueRange, ArrayXDaySeries, DaysToExpirationTF, calcvwapdistribution, xf_CrossOver, BollingerBand, xf_GetDTValue, CloseW, OpenD, NthHighest, AvgDeviation, TRIX, xfMin_PercentR, SimpleLowestBar, UpTrend, SwingLow, DiffBidAskVolumeLxL, Average, Angle, ADI, CloseH, DirectionMovement, NthLowestBar, xf_GetValue, xfMin_GetDTValue, EMP, xfMin_CrossOver, AR, XAverage, LowD, ATR, FastHighestBar, NthExtremesArray, DateTime, ArraySeries, HL_Osc, MI, RSI, MO, NthLowestArray, IVolatility, xf_DirectionMovement, DMO, LowDays, BSVega, VA, HighD, ACC, CountIf, HighH, SummationIf, DPO, TrueHigh, VPT, xf_Stochastic, HighDays, LowestBar, xfmin_MTM, OpenM, EMA, xfMin_RSI, TimeSeriesForecast, xfMin_CrossUnder, LinearRegAngle, xf_GetBoolean, MTM_MA, DiffUpDownVolume, SimpleHighestBar, FastLowest, WAD, UpShadow, NDaysAngle, TrueAny, BiasDiff, LowY, HVolatility, CoefficientR, FastLowestBar, Momentum, GetLastTradeDate, xfMin_GetBoolean, IsXOrder, HighM, CommodityChannel, SwingLowBar, xfMin_XAverage, ArrayMASeries, DiffBidAskVolumeXL, CrossUnder, ReadTicks, QoQ, AverageIF, NthHighestBar, Bias, LinearReg, BSTheta, Q指標, xf_GetCurrentBar, DownTrend, TypicalPrice, CrossOver, Range, angleprice, TurnOverRate, KeltnerLB, OpenW, KST確認指標, RC, TrueCount, ERC, xf_EMA, IFF, HighW, HighestBar, Filter, NORMSDIST, ADO, SwingHighBar, NthHighestArray, HighY, SimpleLowest, LowM, OpenY, xf_WeightedClose, PercentR, TechScore, LowestArray, DIF, CountIfARow, HighQ, xf_XAverage, LinearRegSlope, TSEMFI, xfMin_GetValue, xfMin_GetCurrentBar, NthLowest, TrueAll, VHF, LowH, HighestArray, CloseY, BR, xfMin_WeightedClose, BSPrice, PercentB, Extremes, VVA, xfMin_EMA, CloseQ, CloseM, xfMin_Stochastic, VAO, YoY, Summation, SwingHigh, IsXLOrder, Correlation, BSGamma, RSquare, xf_CrossUnder, RateOfChange, ExtremesArray, LowW, xf_PercentR, UpLimit, D_Value, SAR, TSELSindex, BollingerBandWidth, AvgPrice, BarsLast, KO成交量擺盪指標, StandardDev, xf_RSI, FastHighest, WeightedClose, SimpleHighest, OpenQ, EnterMarketCloseTime, NthExtremes, blackscholesmodel, MAM, RSV, LowQ, xfMin_DirectionMovement, Lowest, DiffTradeVolumeAtAskBid, Highest, xfMin_MACD, MA_Osc, OpenH]
last_updated: 2026-01-08
total_functions: 216
---

# 系統函數 (完整收錄)

> 本文件收錄了 [系統函數] 下的所有子分類與函數說明，共 216 筆。
> 包含子分類：DaysToExpiration, PSY, xf_MACD, LastDayOfMonth, OHLCPeriodsAgo, TrueLow, WMA, MTM, VR, CCI, KeltnerMA, Covariance, BSDelta, KeltnerUB, GetBarOffsetForYears, VariancePS, MACD, NthDayofMonth, DwLimit, ArrayLinearRegSlope, formatMQY, Stochastic, CloseD, MoM, K_Value, TrueRange, ArrayXDaySeries, DaysToExpirationTF, calcvwapdistribution, xf_CrossOver, BollingerBand, xf_GetDTValue, CloseW, OpenD, NthHighest, AvgDeviation, TRIX, xfMin_PercentR, SimpleLowestBar, UpTrend, SwingLow, DiffBidAskVolumeLxL, Average, Angle, ADI, CloseH, DirectionMovement, NthLowestBar, xf_GetValue, xfMin_GetDTValue, EMP, xfMin_CrossOver, AR, XAverage, LowD, ATR, FastHighestBar, NthExtremesArray, DateTime, ArraySeries, HL_Osc, MI, RSI, MO, NthLowestArray, IVolatility, xf_DirectionMovement, DMO, LowDays, BSVega, VA, HighD, ACC, CountIf, HighH, SummationIf, DPO, TrueHigh, VPT, xf_Stochastic, HighDays, LowestBar, xfmin_MTM, OpenM, EMA, xfMin_RSI, TimeSeriesForecast, xfMin_CrossUnder, LinearRegAngle, xf_GetBoolean, MTM_MA, DiffUpDownVolume, SimpleHighestBar, FastLowest, WAD, UpShadow, NDaysAngle, TrueAny, BiasDiff, LowY, HVolatility, CoefficientR, FastLowestBar, Momentum, GetLastTradeDate, xfMin_GetBoolean, IsXOrder, HighM, CommodityChannel, SwingLowBar, xfMin_XAverage, ArrayMASeries, DiffBidAskVolumeXL, CrossUnder, ReadTicks, QoQ, AverageIF, NthHighestBar, Bias, LinearReg, BSTheta, Q指標, xf_GetCurrentBar, DownTrend, TypicalPrice, CrossOver, Range, angleprice, TurnOverRate, KeltnerLB, OpenW, KST確認指標, RC, TrueCount, ERC, xf_EMA, IFF, HighW, HighestBar, Filter, NORMSDIST, ADO, SwingHighBar, NthHighestArray, HighY, SimpleLowest, LowM, OpenY, xf_WeightedClose, PercentR, TechScore, LowestArray, DIF, CountIfARow, HighQ, xf_XAverage, LinearRegSlope, TSEMFI, xfMin_GetValue, xfMin_GetCurrentBar, NthLowest, TrueAll, VHF, LowH, HighestArray, CloseY, BR, xfMin_WeightedClose, BSPrice, PercentB, Extremes, VVA, xfMin_EMA, CloseQ, CloseM, xfMin_Stochastic, VAO, YoY, Summation, SwingHigh, IsXLOrder, Correlation, BSGamma, RSquare, xf_CrossUnder, RateOfChange, ExtremesArray, LowW, xf_PercentR, UpLimit, D_Value, SAR, TSELSindex, BollingerBandWidth, AvgPrice, BarsLast, KO成交量擺盪指標, StandardDev, xf_RSI, FastHighest, WeightedClose, SimpleHighest, OpenQ, EnterMarketCloseTime, NthExtremes, blackscholesmodel, MAM, RSV, LowQ, xfMin_DirectionMovement, Lowest, DiffTradeVolumeAtAskBid, Highest, xfMin_MACD, MA_Osc, OpenH

---


## ArrayLinearRegSlope
--- 

### ArrayLinearRegSlope
#### ArrayLinearRegSlope – （系統函數） <kbd>Array函數</kbd>

##### 語法
> 利用陣列來計算的線性迴歸的斜率。  
> **回傳陣列=ArrayLinearRegSlope(陣列,期數)**  
> 傳入二個參數:  
> - 第一個參數是陣列。  
> - 第二個參數是期數。  

---

##### 說明
利用最小平方法計算線性迴歸的斜率。

___


## ArrayMASeries
--- 

### ArrayMASeries
#### ArrayMASeries – （系統函數） <kbd>Array函數</kbd>

##### 語法
> 將均線數值序列轉成陣列。  
> **回傳陣列=ArrayMASeries(數列,數列期數,陣列)**  
> 傳入三個參數:  
> - 第一個參數是數列。  
> - 第二個參數是數列期數。  
> - 第三個參數是陣列。  

---

##### 說明
將某個數值序列的均線轉成陣列型態。

___


## ArraySeries
--- 

### ArraySeries
#### ArraySeries – （系統函數） <kbd>Array函數</kbd>

##### 語法
> 將數值序列轉成陣列。  
> **回傳陣列=ArraySeries(數列,數列期數,陣列)**  
> 傳入三個參數:  
> - 第一個參數是數列。  
> - 第二個參數是數列期數。  
> - 第三個參數是陣列。  

---

##### 說明
將某個數值序列轉成陣列型態。

___


## ArrayXDaySeries
--- 

### ArrayXDaySeries
#### ArrayXDaySeries – （系統函數） <kbd>Array函數</kbd>

##### 語法
> 以陣列儲存跨頻率的序列值。  
> **回傳陣列=ArrayXDaySeries(序列,最大引用筆數,陣列)**  
> 傳入三個參數:  
> - 第一個參數是序列。  
> - 第二個參數是最大引用筆數。  
> - 第三個參數是陣列。  

---

##### 說明
以Array儲存跨頻率的序列值，傳入一個序列。

範例：
        
```pascal
Array: CloseArray[](0);
ArrayXDaySeries(GetField("收盤價","D"),SBB_length,_DayValue);
```

___


## calcvwapdistribution
--- 

### calcvwapdistribution
#### calcvwapdistribution – （系統函數） <kbd>交易相關</kbd>

##### 語法
> 計算過去N日的VWAP分佈。  
> calcvwapdistribution(計算天數，開始時間，結束時間，一個array)  

---

##### 說明
計算過去N日的VWAP分佈

請傳入

- 計算天數
- 開始時間, 例如091000
- 結束時間, 例如095900 (請注意請以1分K的Time為基準)
- 一個array, 用來儲存上述指定區間內每分鐘的累積成交量分佈%, 
  - CalcVWAPDistribution會自動設定array的大小,
  - array[1]是從開始時間後第1分鐘的累計成交量%, array[2]是從開始時間到後第2分鐘的累計成交量%, etc.
  - 請注意這是一個累積的數值, 例如array[1] = 2.5, array[2] = 5.4, array[3] = 7.0, ... array[最後一個]=100.0,

___


## EnterMarketCloseTime
--- 

### EnterMarketCloseTime
#### EnterMarketCloseTime – （系統函數） <kbd>交易相關</kbd>

##### 語法
> **回傳布林值。**  
> 判斷是否已經進入收盤階段：用來判斷不再進場 or 平倉當日部位。  
> 使用時須傳入N，代表在最後可以送單前N分鐘就認定進入收盤階段，  
> **例如如果傳1，而且是台股的話, 那在13:24:00就會回傳True，代表已經進入收盤階段。**  
> ※請注意：這個函數只支援台股, 以及台灣期貨市場內的常用商品, 也不考慮部分外匯期貨 or 其他市場期貨, 例如東証指。  

---

##### 說明
可至 XQ 系統的 XScrip 編輯器，開啟「系統-交易相關」資料夾底下的 EnterMarketCloseTime 函數腳本，查看詳細函數語法撰寫邏輯。

___


## ReferralCode
--- 

### ReferralCode
#### ReferralCode – （系統函數） <kbd>達人鎖碼／權限</kbd>

##### 語法
> **布林值 = ReferralCode("優惠碼")**  
> 判斷目前執行腳本的帳號是否已綁定指定的優惠碼。  
> 已綁定回傳 `True`、未綁定回傳 `False`。  

---

##### 說明
ReferralCode 函數用於「達人鎖碼」—— 達人把策略 / 指標上架時，可用此函數限制只有綁定特定優惠碼的用戶才能執行腳本，未綁碼者直接中斷、看不到腳本內容。

- 優惠碼字串需帶 `@` 前綴（例：`@MOFI`），整串當參數傳入。
- 標準用法搭配 `RaiseRunTimeError`，放在腳本最前面（頻率防呆之後、實際運算之前），未綁碼就提早中斷以保護內容。
- 四大類腳本（指標／選股／警示／交易）皆適用。

範例:

```pascal
// 未綁定優惠碼 @MOFI 的用戶 → 直接中斷
If ReferralCode("@MOFI") = false then
    RaiseRunTimeError("請綁定優惠碼 @MOFI 解鎖");
```

___


## AvgPrice
--- 

### AvgPrice
#### AvgPrice – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得利用K棒的開高低收所計算出的平均價格。  
> **回傳數值=AvgPrice**  
> ---  
> ※請注意：AvgPrice 與 getfield("AvgPrice") 是不同的數值，  
> getfield("AvgPrice") 是今日的平均成交價，也就是「當日每筆的成交金額加總／當日成交量」  

---

##### 說明
計算公式：

平均價格 = (當期開盤價 + 當期最高價 + 當期最低價 + 當期收盤價)/4

範例：

```pascal
plot1(avgprice);    //繪製當天平均價格的連線
plot2(avgprice[1]); //繪製前一天平均價格的連線
```

___


## CloseD
--- 

### CloseD
#### CloseD – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得日線的收盤價。  
> 僅限使用於日線以下之頻率。  
> **回傳數值=CloseD(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於日線時，用CloseD可以找到某期的日收盤價。

範例：

```pascal
plot1(CloseD(0)); //繪製當日收盤價的連線
plot2(CloseD(1)); //繪製前一日收盤價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## CloseH
--- 

### CloseH
#### CloseH – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得半年線的收盤價。  
> 僅限使用於半年線以下之頻率。  
> **數值=CloseH(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於半年線時，用CloseH可以找到某期的半年收盤價。

範例：

```pascal
plot1(CloseH(0)); //繪製當期半年線收盤價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## CloseM
--- 

### CloseM
#### CloseM – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得月線的收盤價。  
> 僅限使用於月線以下之頻率。  
> **回傳數值=CloseM(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於月線時，用CloseM可以找到某期的月收盤價。

範例：

```pascal
plot1(CloseM(0)); //繪製當月收盤價的連線
plot2(CloseM(1)); //繪製前一月收盤價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## CloseQ
--- 

### CloseQ
#### CloseQ – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得季線的收盤價。  
> 僅限使用於季線以下之頻率。  
> **回傳數值=CloseQ(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於季線時，用CloseQ可以找到某期的季收盤價。

範例：

```pascal
plot1(CloseQ(0)); //繪製當季收盤價的連線
plot2(CloseQ(1)); //繪製前一季收盤價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## CloseW
--- 

### CloseW
#### CloseW – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得週線的收盤價。  
> 僅限使用於週線以下之頻率。  
> **回傳數值=CloseW(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於週線時，用CloseW可以找到某期的週收盤價。

範例：

```pascal
plot1(CloseW(0)); //繪製當週收盤價的連線
plot2(CloseW(1)); //繪製前一週收盤價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## CloseY
--- 

### CloseY
#### CloseY – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得年線的收盤價。  
> 僅限使用於年線以下之頻率。  
> **回傳數值=CloseY(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於年線時，用CloseY可以找到某期的年收盤價。

範例：

```pascal
plot1(CloseY(0)); //繪製當年收盤價的連線
plot2(CloseY(1)); //繪製前一年收盤價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## FastHighest
--- 

### FastHighest
#### FastHighest – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 計算序列資料的最大值。  
> **回傳數值=FastHighest(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的極大值。

FastHighest函數為[Highest](api.aspx?a=highest&b=sys)函數的快速計算版本。

在運算極值的時候，會用 For 迴圈往前抓到極值紀錄後，之後執行腳本就會用當下的序列資料與紀錄極值相比，若大於紀錄極值則更新輸出極值與輸出極值的相對K棒位置。因為不會每根 K 棒都用 For 迴圈往前抓極值，所以腳本運行會更加快速。

範例：

```pascal
plot1(FastHighest(high,5));    //繪製5期最高價的最大值的連線
```

___


## FastLowest
--- 

### FastLowest
#### FastLowest – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 計算序列資料的最小值。  
> **回傳數值=FastLowest(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的極小值。

FastLowest函數為[Lowest](api.aspx?a=lowest&b=sys)函數的快速計算版本。

在運算極值的時候，會用 For 迴圈往前抓到極值紀錄後，之後執行腳本就會用當下的序列資料與紀錄極值相比，若大於紀錄極值則更新輸出極值與輸出極值的相對K棒位置。因為不會每根 K 棒都用 For 迴圈往前抓極值，所以腳本運行會更加快速。

範例：

```pascal
plot1(FastLowest(low,5));    //繪製5期最低價的最小值的連線
```

___


## HighD
--- 

### HighD
#### HighD – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得日線的最高價。  
> 僅限使用於日線以下之頻率。  
> **回傳數值=HighD(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於日線時，用HighD可以找到某期的日最高價。

範例：

```pascal
plot1(HighD(0)); //繪製當日最高價的連線
plot2(HighD(1)); //繪製前一日最高價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## Highest
--- 

### Highest
#### Highest – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 計算序列資料的最大值。  
> **回傳數值=Highest(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的極大值。

Highest函數與[FastHighest](api.aspx?a=FastHighest&b=sys)函數的運算方式一致，都是用 [Extremes](api.aspx?a=Extremes&b=sys) 函數抓極大值。

範例：

```pascal
plot1(Highest(high,5));    //繪製5期最高價的最大值的連線
```

___


## HighH
--- 

### HighH
#### HighH – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得半年線的最高價。  
> 僅限使用於半年線以下之頻率。  
> **回傳數值=HighH(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於半年線時，用HighH可以找到某期的半年最高價。

範例：

```pascal
plot1(HighH(0)); //繪製當期半年線最高價的連線
```

___


## HighM
--- 

### HighM
#### HighM – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得月線的最高價。  
> 僅限使用於月線以下之頻率。  
> **回傳數值=HighM(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於月線時，用HighM可以找到某期的月最高價。

範例：

```pascal
plot1(HighM(0)); //繪製當月最高價的連線
plot2(HighM(1)); //繪製前一月最高價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## HighQ
--- 

### HighQ
#### HighQ – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得季線的最高價。  
> 僅限使用於季線以下之頻率。  
> **回傳數值=HighQ(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於季線時，用HighQ可以找到某期的季最高價。

範例：

```pascal
plot1(HighQ(0)); //繪製當季最高價的連線
plot2(HighQ(1)); //繪製前一季最高價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## HighW
--- 

### HighW
#### HighW – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得週線的最高價。  
> 僅限使用於週線以下之頻率。  
> **回傳數值=HighW(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於週線時，用HighW可以找到某期的週最高價。

範例：

```pascal
plot1(HighW(0)); //繪製當週最高價的連線
plot2(HighW(1)); //繪製前一週最高價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## HighY
--- 

### HighY
#### HighY – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得年線的最高價。  
> 僅限使用於年線以下之頻率。  
> **回傳數值=HighY(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於年線時，用HighY可以找到某期的年最高價。

範例：

```pascal
plot1(HighY(0)); //繪製當年最高價的連線
plot2(HighY(1)); //繪製前一年最高價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## LowD
--- 

### LowD
#### LowD – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得日線的最低價。  
> 僅限使用於日線以下之頻率。  
> **回傳數值=LowD(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於日線時，用LowD可以找到某期的日最低價。

範例：

```pascal
plot1(LowD(0)); //繪製當日最低價的連線
plot2(LowD(1)); //繪製前一日最低價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## Lowest
--- 

### Lowest
#### Lowest – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 計算序列資料的最小值。  
> **回傳數值=Lowest(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的極小值。

Lowest函數與[FastLowest](api.aspx?a=FastLowest&b=sys)函數的運算方式一致，都是用 [Extremes](api.aspx?a=Extremes&b=sys) 函數抓極小值。

範例：

```pascal
plot1(Lowest(low,5));    //繪製5期最低價的最小值的連線
```

___


## LowH
--- 

### LowH
#### LowH – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得半年線的最低價。  
> 僅限使用於半年線以下之頻率。  
> **回傳數值=LowH(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於半年線時，用LowH可以找到某期的半年最低價。

範例：

```pascal
plot1(LowH(0)); //繪製當期半年線最低價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## LowM
--- 

### LowM
#### LowM – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得月線的最低價。  
> 僅限使用於月線以下之頻率。  
> **回傳數值=LowM(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於月線時，用LowM可以找到某期的月最低價。

範例：

```pascal
plot1(LowM(0)); //繪製當月最低價的連線
plot2(LowM(1)); //繪製前一月最低價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## LowQ
--- 

### LowQ
#### LowQ – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得季線的最低價。  
> 僅限使用於季線以下之頻率。  
> **回傳數值=LowQ(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於季線時，用LowQ可以找到某期的季最低價。

範例：

```pascal
plot1(LowQ(0)); //繪製當季最低價的連線
plot2(LowQ(1)); //繪製前一季最低價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## LowW
--- 

### LowW
#### LowW – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得週線的最低價。  
> 僅限使用於週線以下之頻率。  
> **回傳數值=LowW(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於週線時，用LowW可以找到某期的週最低價。

範例：

```pascal
plot1(LowW(0)); //繪製當週最低價的連線
plot2(LowW(1)); //繪製前一週最低價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## LowY
--- 

### LowY
#### LowY – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得年線的最低價。  
> 僅限使用於年線以下之頻率。  
> **回傳數值=LowY(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於年線時，用LowY可以找到某期的年最低價。

範例：

```pascal
plot1(LowY(0)); //繪製當年最低價的連線
plot2(LowY(1)); //繪製前一年最低價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## OpenD
--- 

### OpenD
#### OpenD – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得日線的開盤價。  
> 僅限使用於日線以下之頻率。  
> **回傳數值=OpenD(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於日線時，用OpenD可以找到某期的日開盤價。

範例：

```pascal
plot1(OpenD(0)); //繪製當日開盤價的連線
plot2(OpenD(1)); //繪製前一日開盤價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## OpenH
--- 

### OpenH
#### OpenH – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得半年線的開盤價。  
> 僅限使用於半年線以下之頻率。  
> **回傳數值=OpenH(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於半年線時，用OpenH可以找到某期的半年開盤價。

範例：

```pascal
plot1(OpenH(0)); //繪製當期半年線開盤價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## OpenM
--- 

### OpenM
#### OpenM – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得月線的開盤價。  
> 僅限使用於月線以下之頻率。  
> **回傳數值=OpenM(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於月線時，用OpenM可以找到某期的月開盤價。

範例：

```pascal
plot1(OpenM(0)); //繪製當月開盤價的連線
plot2(OpenM(1)); //繪製前一月開盤價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## OpenQ
--- 

### OpenQ
#### OpenQ – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得季線的開盤價。  
> 僅限使用於季線以下之頻率。  
> **回傳數值=OpenQ(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於季線時，用OpenQ可以找到某期的季開盤價。

範例：

```pascal
plot1(OpenQ(0)); //繪製當季開盤價的連線
plot2(OpenQ(1)); //繪製前一季開盤價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## OpenW
--- 

### OpenW
#### OpenW – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得週線的開盤價。  
> 僅限使用於週線以下之頻率。  
> **回傳數值=OpenW(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於週線時，用OpenW可以找到某期的週開盤價。

範例：

```pascal
plot1(OpenW(0)); //繪製當週開盤價的連線
plot2(OpenW(1)); //繪製前一週開盤價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## OpenY
--- 

### OpenY
#### OpenY – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得年線的開盤價。  
> 僅限使用於年線以下之頻率。  
> **回傳數值=OpenY(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

##### 說明
當使用頻率小於年線時，用OpenY可以找到某期的年開盤價。

範例：

```pascal
plot1(OpenY(0)); //繪製當年開盤價的連線
plot2(OpenY(1)); //繪製前一年開盤價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)

___


## TrueHigh
--- 

### TrueHigh
#### TrueHigh – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得價格真實區間(TrueRange)的高點。  
> **回傳數值=TrueHigh**  

---

##### 說明
計算方法為比較當根K棒的高點與前根K棒的收盤價，取數值較大者。

範例：

```pascal
plot1(TrueHigh);    //繪製當期真實區間高點的連線
plot2(TrueHigh[1]); //繪製前一期真實區間高點的連線
```

請參考 [TrueLow函數](api.aspx?a=truelow&b=sys)以及[TrueRange函數](api.aspx?a=truerange&b=sys)。

___


## TrueLow
--- 

### TrueLow
#### TrueLow – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 取得價格真實區間(TrueRange)的低點。  
> **回傳數值=TrueLow**  

---

##### 說明
計算方法為比較當根K棒的低點與前根K棒的收盤價，取數值較小者。

範例：

```pascal
plot1(TrueLow);    //繪製當期真實區間低點的連線
plot2(TrueLow[1]); //繪製前一期真實區間低點的連線
```

請參考 [TrueHigh函數](api.aspx?a=truehigh&b=sys)以及[TrueRange函數](api.aspx?a=truerange&b=sys)。

___


## TypicalPrice
--- 

### TypicalPrice
#### TypicalPrice – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 傳回技術分析的典型價。  
> **回傳數值=TypicalPrice**  

---

##### 說明
計算公式：

典型價 = (當期最高價 + 當期最低價 + 當期收盤價)/3

範例：

```pascal
plot1(TypicalPrice);    //繪製當期典型價的連線
plot2(TypicalPrice[1]); //繪製前一期典型價的連線
```

___


## WeightedClose
--- 

### WeightedClose
#### WeightedClose – （系統函數） <kbd>價格取得</kbd>

##### 語法
> 計算技術分析的加權平均收盤價。  
> **回傳數值=WeightedClose**  

---

##### 說明
加權平均價給予收盤價較大的權重，著名的MACD指標即是利用加權平均價做計算。

計算公式：

WeightedClose = (當期最高價 + 當期最低價 + 2*當期收盤價)/4

範例：

```pascal
plot1(WeightedClose);    //繪製當期加權平均收盤價的連線
plot2(WeightedClose[1]); //繪製前一期加權平均收盤價的連線
```

___


## Extremes
--- 

### Extremes
#### Extremes – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算序列資料的極大值或極小值。  
> 以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的極值。  
> **回傳數值=Extremes(數列,期數,要計算極大值或極小值,輸出極值,輸出極值K棒相對位置)**  
> 傳入五個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  
> - 第三個參數是要計算極大值或極小值；1為極大值、-1為極小值。  
> **- 第四個參數為傳址參數，會回傳計算完的極值。**  
> **- 第五個參數是傳址參數，會回傳極值K棒相對於當期K棒的期數。**  

---

##### 說明
計算成功時回傳值為1，結果會回傳在第4、5個參數。

範例：

```pascal
value1 = extremes(high,5,1,value2,value3); //計算5期最高價的極大值
plot1(value2);                             //繪製5期最高價的極大值的連線
```

___


## ExtremesArray
--- 

### ExtremesArray
#### ExtremesArray – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算陣列資料的極大值或極小值。  
> **回傳數值=ExtremesArray(陣列,陣列大小,要計算極大值或極小值,輸出極值,輸出極值的陣列索引值)**  
> 傳入五個參數:  
> - 第一個參數是要計算的陣列。  
> - 第二個參數是陣列大小。  
> - 第三個參數是要計算極大值或極小值；1為極大值、-1為極小值。  
> **- 第四個參數為傳址參數，會回傳計算完的極值。**  
> **- 第五個參數是傳址參數，會回傳極值的陣列索引值。**  

---

##### 說明
計算成功時回傳值為1，結果會回傳在第4、5個參數。

範例：

```pascal
Array: arrA[5](0); // 宣告arrA是一個有5個元素的陣列，初始值都是0

arrA[1] = 0;  arrA[2] = 10; arrA[3] = 20; arrA[4] = 30; arrA[5] = 40;

value1 = extremesarray(arrA,5,-1,value2,value3); //計算陣列arrA的極小值
plot1(value2);                                   //繪製陣列arrA的極小值的連線
```

___


## FastHighestBar
--- 

### FastHighestBar
#### FastHighestBar – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算序列資料的最大值的相對位置。  
> **回傳數值=FastHighestBar(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的極大值的相對位置。
如果有同樣兩個以上的極大值，則傳回離現在最近的那個。

FastHighestBar函數為[HighestBar](api.aspx?a=HighestBar&b=sys)函數的快速計算版本。

在運算極值的時候，會用 For 迴圈往前抓到極值紀錄後，之後執行腳本就會用當下的序列資料與紀錄極值相比，若大於紀錄極值則更新輸出極值與輸出極值的相對K棒位置。因為不會每根 K 棒都用 For 迴圈往前抓極值，所以腳本運行會更加快速。

範例：

```pascal
plot1(FastHighestBar(high,5));    //繪製近5期最高的最高價相對位置的連線
```

___


## FastLowestBar
--- 

### FastLowestBar
#### FastLowestBar – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算序列資料的最小值的相對位置。  
> **回傳數值=FastLowestBar(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的極小值的相對位置。
如果有同樣兩個以上的極小值，則傳回離現在最近的那個。

FastLowestBar函數為[LowestBar](api.aspx?a=LowestBar&b=sys)函數的快速計算版本。

在運算極值的時候，會用 For 迴圈往前抓到極值紀錄後，之後執行腳本就會用當下的序列資料與紀錄極值相比，若大於紀錄極值則更新輸出極值與輸出極值的相對K棒位置。因為不會每根 K 棒都用 For 迴圈往前抓極值，所以腳本運行會更加快速。

範例：

```pascal
plot1(FastLowestBar(low,5));    //繪製近5期最低的最低價相對位置的連線
```

___


## HighDays
--- 

### HighDays
#### HighDays – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算指定期間內創新高的次數。  
> **回傳數值=HighDays(期數)**  
> 傳入一個參數:  
> - 第一個參數是期數。期數含當期，最小值為1。  

---

##### 說明
範例：

```pascal
plot1(HighDays(10)); //繪製近10期創新高次數的連線
```

請參考[LowDays函數](api.aspx?a=lowdays&b=sys)。

___


## HighestArray
--- 

### HighestArray
#### HighestArray – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算陣列資料的最大值。  
> **回傳數值=HighestArray(陣列,陣列大小)**  
> 傳入二個參數:  
> - 第一個參數是要計算的陣列。  
> - 第二個參數是陣列大小。  

---

##### 說明
範例：

```pascal
Array: arrA[5](0); // 宣告arrA是一個有5個元素的陣列，初始值都是0

arrA[1] = 0;  arrA[2] = 10; arrA[3] = 20; arrA[4] = 30; arrA[5] = 40;

value1 = HighestArray(arrA,5); //計算陣列arrA的極大值
plot1(value1);                 //繪製陣列arrA的極大值的連線
```

___


## HighestBar
--- 

### HighestBar
#### HighestBar – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算序列資料的最大值的相對位置。  
> **回傳數值=HighestBar(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的極大值的相對位置。
如果有同樣兩個以上的極大值，則傳回離現在最近的那個。

範例：

```pascal
plot1(HighestBar(high,5));    //繪製近5期最高的最高價相對位置的連線
```

___


## LowDays
--- 

### LowDays
#### LowDays – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算指定期間內創新低的次數。  
> **回傳數值=LowDays(期數)**  
> 傳入一個參數:  
> - 第一個參數是期數。期數含當期，最小值為1。  

---

##### 說明
範例：

```pascal
plot1(LowDays(10)); //繪製近10期創新低次數的連線
```

請參考[HighDays函數](api.aspx?a=highdays&b=sys)。

___


## LowestArray
--- 

### LowestArray
#### LowestArray – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算陣列資料的最小值。  
> **回傳數值=LowestArray(陣列,陣列大小)**  
> 傳入二個參數:  
> - 第一個參數是要計算的陣列。  
> - 第二個參數是陣列大小。  

---

##### 說明
範例：

```pascal
Array: arrA[5](0); // 宣告arrA是一個有5個元素的陣列，初始值都是0

arrA[1] = 0;  arrA[2] = 10; arrA[3] = 20; arrA[4] = 30; arrA[5] = 40;

value1 = LowestArray(arrA,5);  //計算陣列arrA的極小值
plot1(value1);                 //繪製陣列arrA的極小值的連線
```

___


## LowestBar
--- 

### LowestBar
#### LowestBar – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算序列資料的最小值的相對位置。  
> **回傳數值=LowestBar(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的極小值的相對位置。
如果有同樣兩個以上的極小值，則傳回離現在最近的那個。

範例：

```pascal
plot1(LowestBar(low,5));    //繪製近5期最低的最低價相對位置的連線
```

___


## MoM
--- 

### MoM
#### MoM – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算序列資料的月變化率(換算成百分比)  
> 限用於月頻率資料。  
> **回傳數值=MoM(數列)**  

---

##### 說明
範例：

```pascal
plot1(MoM(close));    //繪製收盤價的月變化率連線
```

___


## NthExtremes
--- 

### NthExtremes
#### NthExtremes – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算序列資料的第N個極大值或極小值。  
> **回傳數值=NthExtremes(數列,期數,第幾個極值,要計算極大值或極小值,輸出極值,輸出極值K棒相對位置)**  
> 傳入六個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  
> - 第三個參數是要計算極值的序號。  
> - 第四個參數是要計算極大值或極小值；1為極大值、-1為極小值。  
> **- 第五個參數為傳址參數，會回傳計算完的極值。**  
> **- 第六個參數是傳址參數，會回傳極值K棒相對於當期K棒的期數。**  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的第N個極值。

計算成功時回傳值為1，結果會回傳在第5、6個參數。

範例：

```pascal
value1 = nthextremes(high,10,2,1,value2,value3); //計算10期內第二個最高價
plot1(value2);                                   //繪製10期內第二個最高價的連線
```

___


## NthExtremesArray
--- 

### NthExtremesArray
#### NthExtremesArray – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算陣列資料的第N個極大值或極小值。  
> **回傳數值=ExtremesArray(陣列,陣列大小,第幾個極值,要計算極大值或極小值,輸出極值,輸出極值的陣列索引值)**  
> 傳入六個參數:  
> - 第一個參數是要計算的陣列。  
> - 第二個參數是陣列大小。  
> - 第三個參數是要計算極值的序號。  
> - 第四個參數是要計算極大值或極小值；1為極大值、-1為極小值。  
> **- 第五個參數為傳址參數，會回傳計算完的極值。**  
> **- 第六個參數是傳址參數，會回傳極值的陣列索引值。**  

---

##### 說明
計算成功時回傳值為1，結果會回傳在第5、6個參數。

範例：

```pascal
Array: arrA[5](0); // 宣告arrA是一個有5個元素的陣列，初始值都是0

arrA[1] = 0;  arrA[2] = 10; arrA[3] = 20; arrA[4] = 30; arrA[5] = 40;

value1 = NthExtremesArray(arrA,5,3,-1,value2,value3); //計算陣列arrA的第三個極小值
plot1(value2);                                   //繪製陣列arrA的第三個極小值的連線
```

___


## NthHighest
--- 

### NthHighest
#### NthHighest – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算序列資料的第N個極大值。  
> **回傳數值=NthHighest(第幾個極大值,數列,期數)**  
> 傳入三個參數:  
> - 第一個參數是要計算極大值的序號。  
> - 第二個參數是數列，通常是開高低收的價格數列。  
> - 第三個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的第N個極大值。

範例：

```pascal
value1 = NthHighest(2,high,5); //計算近5期次高的最高價
plot1(value1);                 //繪製近5期次高的最高價的連線
```

___


## NthHighestArray
--- 

### NthHighestArray
#### NthHighestArray – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算陣列資料的第N個極大值。  
> **回傳數值=NthHighestArray(陣列,陣列大小,第幾個極大值)**  
> 傳入三個參數:  
> - 第一個參數是要計算的陣列。  
> - 第二個參數是陣列大小。  
> - 第三個參數是要計算極大值的序號。  

---

##### 說明
範例：

```pascal
Array: arrA[5](0); // 宣告arrA是一個有5個元素的陣列，初始值都是0

arrA[1] = 0;  arrA[2] = 10; arrA[3] = 20; arrA[4] = 30; arrA[5] = 40;

value1 = NthHighestArray(arrA,5,3); //計算陣列arrA的第三個極大值
plot1(value1);                      //繪製陣列arrA的第三個極大值的連線
```

___


## NthHighestBar
--- 

### NthHighestBar
#### NthHighestBar – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算序列資料的第N個極大值距當期K棒的相對位置。  
> **回傳數值=NthHighestBar(第幾個極大值,數列,期數)**  
> 傳入三個參數:  
> - 第一個參數是要計算極大值的序號。  
> - 第二個參數是數列，通常是開高低收的價格數列。  
> - 第三個參數是期數。  

---

##### 說明
範例：

```pascal
value1 = NthHighestBar(2,high,5); //計算近5期次高的最高價的相對位置
plot1(value1);                    //繪製近5期次高的最高價相對位置的連線
```

___


## NthLowest
--- 

### NthLowest
#### NthLowest – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算序列資料的第N個極小值。  
> **回傳數值=NthLowest(第幾個極小值,數列,期數)**  
> 傳入三個參數:  
> - 第一個參數是要計算極小值的序號。  
> - 第二個參數是數列，通常是開高低收的價格數列。  
> - 第三個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的第N個極小值。

範例：

```pascal
value1 = NthLowest(2,low,5); //計算近5期次低的最低價
plot1(value1);               //繪製近5期次低的最低價的連線
```

___


## NthLowestArray
--- 

### NthLowestArray
#### NthLowestArray – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算陣列資料的第N個極小值。  
> **回傳數值=NthLowestArray(陣列,陣列大小,第幾個極小值)**  
> 傳入三個參數:  
> - 第一個參數是要計算的陣列。  
> - 第二個參數是陣列大小。  
> - 第三個參數是要計算極小值的序號。  

---

##### 說明
範例：

```pascal
Array: arrA[5](0); // 宣告arrA是一個有5個元素的陣列，初始值都是0

arrA[1] = 0;  arrA[2] = 10; arrA[3] = 20; arrA[4] = 30; arrA[5] = 40;

value1 = NthLowestArray(arrA,5,3); //計算陣列arrA的第三個極小值
plot1(value1);                      //繪製陣列arrA的第三個極小值的連線
```

___


## NthLowestBar
--- 

### NthLowestBar
#### NthLowestBar – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算序列資料的第N個極小值距當期K棒的相對位置。  
> **回傳數值=NthLowestBar(第幾個極小值,數列,期數)**  
> 傳入三個參數:  
> - 第一個參數是要計算極小值的序號。  
> - 第二個參數是數列，通常是開高低收的價格數列。  
> - 第三個參數是期數。  

---

##### 說明
範例：

```pascal
value1 = NthLowestBar(2,low,5); //計算近5期次低的最低價的相對位置
plot1(value1);                  //繪製近5期次低的最低價相對位置的連線
```

___


## OHLCPeriodsAgo
--- 

### OHLCPeriodsAgo
#### OHLCPeriodsAgo – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算指定頻率K棒的開盤價，最高價，最低價，收盤價。  
> 僅能取得目前計算數列較高頻率之K棒資料  
> **回傳數值=OHLCPeriodsAgo(頻率,K棒相對位置,輸出之開盤價,輸出之最高價,輸出之最低價,輸出之收盤價,)**  
> 傳入六個參數:  
> - 第一個參數是頻率，1:日線、2:週線、3:月線、3.25:季、3.5 半年、4:年線  
> - 第二個參數是K棒相對位置，和序列引用定義相同，0表當期、1表前一期...依此類推。  
> **- 第三個參數為傳址參數，會回傳指定頻率的開盤價。**  
> **- 第四個參數為傳址參數，會回傳指定頻率的最高價。**  
> **- 第五個參數為傳址參數，會回傳指定頻率的最低價。**  
> **- 第六個參數為傳址參數，會回傳指定頻率的收盤價。**  

---

##### 說明
取得特定頻率、特定K棒的開盤價、最高價、最低價和收盤價

計算成功時回傳值為1，結果會回傳在第3~6個參數。

範例：

```pascal
value1 = OHLCPeriodsAgo(2,1,value2,value3,value4,value5); //計算前期週線的開高低收價
plot1(value4);                                            //繪製前期週線最低價的連線
```

___


## QoQ
--- 

### QoQ
#### QoQ – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算序列資料的季變化率(換算成百分比)  
> 限用於季頻率資料。  
> **回傳數值=QoQ(數列)**  

---

##### 說明
範例：

```pascal
plot1(QoQ(close));    //繪製收盤價的季變化率連線
```

___


## ReadTicks
--- 

### ReadTicks
#### ReadTicks – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 讀取自上次腳本執行後到目前為止的所有 Tick 成交資料  
> **本次執行更新的資料筆數 = ReadTicks ( 輸出儲存Tick資料的二維陣列, 輸出最後一筆讀到的Tick序號 ) ;**  
>   
> 回測在1分鐘頻率時，不支援模擬逐筆洗價  

---

##### 說明
請先參考 [台股逐筆撮合的連續成交Tick序列](https://www.xq.com.tw/lesson/xspractice/%e5%8f%b0%e8%82%a1%e9%80%90%e7%ad%86%e6%92%ae%e5%90%88%e7%9a%84%e7%a9%bf%e5%83%b9tick/) ，關於腳本洗價方式與MultiTick的概念。

###### **參數設定說明**

**輸出儲存Tick資料的二維陣列**
```pascal
array: tick_array[100, 11](0);
```

必須先宣告一個2維陣列來儲存Tick資料。

第一維(列)是每次洗價的最大讀取筆數；第二維(行)用來儲存每一筆的成交相關資料，必須 >= 11


**輸出腳本執行完畢的最後一筆Tick序號（`Seqno`）**
```pascal

var: intrabarpersist readtick_cookie(0);
```
必須先宣告一個`intrabarpersist`的變數，給 **ReadTicks** 內部使用。


######  **參數輸出內容說明**

####### **tick_array**

當 **ReadTicks** 執行完畢後，`tick_array`的每一列代表一筆成交紀錄（或是合併後的 MultiTick），每一行 (column) 包含該筆紀錄的不同欄位資訊。

- 每一列成交紀錄

	回傳的 Tick 資料是倒序的，`tick_array[1, ...]`是離當下最近的那筆成交，`tick_array[2, ...]`是前一筆，依此類推。

- 每一行欄位資訊
	
	```pascal
	tick_array[..., 1] = Date
	tick_array[..., 2] = Time（MultiTick 合併後，此為序列的統一時間）
	tick_array[..., 3] = Close（若是 MultiTick，則為序列中最後一筆的成交價）
	tick_array[..., 4] = Volume（若是 MultiTick，則為序列中最後一筆的成交量。若需總量請參考欄位10）
	tick_array[..., 5] = 內外盤標記（1: 外盤；-1: 內盤；0: 無法區分）
	tick_array[..., 6] = Tick序號 （若是 MultiTick，則為序列中最後一筆的序號）
	tick_array[..., 7] = 成交方式註記（-1: 集合競價；0: 逐筆撮合下的單筆成交；>0: 逐筆撮合下的 MultiTick，數值代表此序列包含的 Tick 筆數）
	tick_array[..., 8] = 起始Offset（若是MultiTick，為第一筆與最新一筆Tick的相對位置）
	tick_array[..., 9] = 結束Offset（若是MultiTick，為最後一筆與最新一筆Tick的相對位置。若是單筆成交，此值與欄位 8 相同）
	tick_array[..., 10] = 成交量加總（該筆成交的總量。若是 MultiTick，此為序列中所有 Tick 的成交量總和）
	tick_array[..., 11] = 成交值加總（ 該筆成交的總金額(元)。若是 MultiTick，此為序列中所有 Tick 的成交值總和）
	```
- 請注意

	- 不完整序列
	
		若在兩次執行之間，系統只收到了 MultiTick 的一部分，**ReadTicks** 會暫不處理，並將`readtick_cookie`停在序列開始前的位置，待下次收到完整序列時再一併回傳。

	- `ReadTicks`不會在每次執行前清空`tick_array`

		它只會從第一列開始覆寫資料。若前一次呼叫回傳了 20 筆資料，而本次只回傳 10 筆，則陣列的第 11 至 20 列將會保留舊的資料。因此，務必使用`ReadTicks`的回傳值來控制迴圈的範圍，避免讀取到過時的資訊。

###### **ReadTicks的回傳值**

ReadTicks本身可以用一個變數來存取它的輸出值，代表本次執行在`tick_array`內更新的資料筆數 (即實際填入的行數)

___


## SimpleHighest
--- 

### SimpleHighest
#### SimpleHighest – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算序列資料的最大值。  
> **回傳數值=SimpleHighest(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的極大值。

每次呼叫SimpleHighest時，腳本都會依照指定期別，往前抓取期別內的每一筆資料來計算。

系統另外提供[Highest](api.aspx?a=highest&b=sys)函數，也可以用來計算過去期數的最大值，兩者的差異請參考Highest函數的說明。

範例：

```pascal
plot1(SimpleHighest(high,5));    //繪製5期最高價的最大值的連線
```

___


## SimpleLowest
--- 

### SimpleLowest
#### SimpleLowest – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算序列資料的最小值。  
> **回傳數值=SimpleLowest(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的極小值。

每次呼叫SimpleLowest時，腳本都會依照指定期別，往前抓取期別內的每一筆資料來計算。

系統另外提供[Lowest](api.aspx?a=lowest&b=sys)函數，也可以用來計算過去期數的最大值，兩者的差異請參考Lowest函數的說明。

範例：

```pascal
plot1(SimpleLowest(low,5));    //繪製5期最低價的最小值的連線
```

___


## YoY
--- 

### YoY
#### YoY – （系統函數） <kbd>價格計算</kbd>

##### 語法
> 計算序列資料的年變化率(換算成百分比)  
> 限用於年頻率資料。  
> **回傳數值=YoY(數列)**  

---

##### 說明
範例：

```pascal
plot1(YoY(close));    //繪製收盤價的年變化率連線
```

___


## Average
--- 

### Average
#### Average – （系統函數） <kbd>價格關係</kbd>

##### 語法
> 計算序列資料的移動平均。  
> **回傳數值=Average(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
計算序列資料的移動平均。

以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的序列平均值。


範例：

```pascal
value1 = Average(Close,5); //計算5期收盤價的移動平均
```

___


## AvgDeviation
--- 

### AvgDeviation
#### AvgDeviation – （系統函數） <kbd>價格關係</kbd>

##### 語法
> 計算序列資料的平均差。  
> **回傳數值=AvgDeviation(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的平均差。

範例：

```pascal
value1 = AvgDeviation(Close,5); //計算5期收盤價的平均差
```

___


## DwLimit
--- 

### DwLimit
#### DwLimit – （系統函數） <kbd>價格關係</kbd>

##### 語法
> 依傳入之參考價計算跌停價。  
> **回傳數值=DwLimit(參考價)**  

---

##### 說明
範例：

```pascal
value1 = DwLimit(CloseD(1)); //計算當期之跌停價
```

___


## EMA
--- 

### EMA
#### EMA – （系統函數） <kbd>價格關係</kbd>

##### 語法
> 計算序列資料的XQ指數移動平均。  
> **回傳數值=EMA(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的XQ指數移動平均值。

XQ指數移動平均和一般指數移動平均（XAverage）的計算差異在於最前面幾期（小於平均期數）時的計算公式不同。

當K棒編號 ≦ 期數時：

當期均價 = (當期價格 + (前期均價*(K棒編號-1)))/K棒編號  (換句話說，當期均價 = 這幾期的算數平均)

當K棒編號 > 期數時：

當期均價 = (2/(n+1))*當期價格 + (n-1)/(n+1)*前期均價

範例：

```pascal
value1 = EMA(Close,5); //計算5期收盤價的XQ EMA
```

___


## Range
--- 

### Range
#### Range – （系統函數） <kbd>價格關係</kbd>

##### 語法
> 傳回當根K棒的高低價差。  
> **回傳數值=Range**  

---

##### 說明
計算公式：

Range = (當期最高價 - 當期最低價)

範例：

```pascal
plot1(Range);    //繪製當期K棒高低價差的連線
plot2(Range[1]); //繪製前一期K棒高低價差的連線
```

___


## RateOfChange
--- 

### RateOfChange
#### RateOfChange – （系統函數） <kbd>價格關係</kbd>

##### 語法
> 計算序列資料的變化率。  
> **回傳數值=RateOfChange(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
以前N根K棒資料為基準點，計算至當根K棒的的數值變化率。

計算公式：

RateOfChange = ( 當期價格 ／ N期前價格 - 1 ) * 100

範例：

```pascal
value1 = RateOfChange(Close,5); //計算5期收盤價的變化率
```

___


## SimpleHighestBar
--- 

### SimpleHighestBar
#### SimpleHighestBar – （系統函數） <kbd>價格關係</kbd>

##### 語法
> 取得區間內數列最大值的K棒位置。  
> **回傳數值=SimpleHighestBar(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
取得區間內數列最大值的K棒位置。
可以使用這個函數來取得欄位區間內新高的位置。

___


## SimpleLowestBar
--- 

### SimpleLowestBar
#### SimpleLowestBar – （系統函數） <kbd>價格關係</kbd>

##### 語法
> 取得區間內數列最小值的K棒位置。  
> **回傳數值=SimpleLowestBar(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
取得區間內數列最小值的K棒位置。
可以使用這個函數來取得欄位區間內新低的位置。

___


## Summation
--- 

### Summation
#### Summation – （系統函數） <kbd>價格關係</kbd>

##### 語法
> 計算序列資料的總和。  
> **回傳數值=Summation(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的數值總和。

範例：

```pascal
value1 = Summation(Close,5); //計算5期收盤價的總和
```

___


## TrueRange
--- 

### TrueRange
#### TrueRange – （系統函數） <kbd>價格關係</kbd>

##### 語法
> 傳回當根K棒的真實區間。  
> **回傳數值=TrueRange**  

---

##### 說明
真實區間是韋爾達（J. W. Wilder）於1978年發表於New Concepts in Technical Trading Systems中測量價格波動性的方法。

根據韋爾達的定義，真實區間為下列三項中的最大值：

- 當期最高價至最低價的幅度。
- 當期最低價與前期收盤價的幅度。
- 當期最高價至前期收盤價的幅度。

範例：

```pascal
plot1(TrueRange);    //繪製當期K棒真實區間的連線
plot2(TrueRange[1]); //繪製前一期K棒真實區間的連線
```

___


## UpLimit
--- 

### UpLimit
#### UpLimit – （系統函數） <kbd>價格關係</kbd>

##### 語法
> 依傳入之參考價計算漲停價。  
> **回傳數值=UpLimit(參考價)**  

---

##### 說明
範例：

```pascal
value1 = UpLimit(CloseD(1)); //計算當期之漲停價
```

___


## WMA
--- 

### WMA
#### WMA – （系統函數） <kbd>價格關係</kbd>

##### 語法
> 計算序列資料的加權移動平均。  
> **回傳數值=WMA(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的加權移動平均值。

計算公式：

WMAt=(Pt * n + Pt-1 * (n-1) + Pt-2 * (n-2) + ... + Pt-n+1) / (n + (n-1) + (n-2) + ... + 1)

範例：

```pascal
value1 = WMA(Close,5); //計算5期收盤價的加權移動平均
```

___


## XAverage
--- 

### XAverage
#### XAverage – （系統函數） <kbd>價格關係</kbd>

##### 語法
> 計算序列資料的指數移動平均。  
> **回傳數值=XAverage(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的指數移動平均值。

計算公式：

當期均價 = (2/(n+1))*當期價格 + (n-1)/(n+1)*前期均價

範例：

```pascal
value1 = XAverage(Close,5); //計算5期收盤價的指數移動平均
```

___


## ACC
--- 

### ACC
#### ACC – （系統函數） <kbd>技術指標</kbd>

##### 語法
> ACC加速量指標(Acceleration)。用來觀察行情價格變化的加速度幅度。  
> **回傳數值=ACC(期數)**  

---

##### 說明
ACC是將MTM運動量指標再做一次動量運算的指標。

範例：
```pascal
value1 = ACC(10);       //計算收盤價10期的加速量指標
plot1(value1, "ACC");   
```

___


## ADI
--- 

### ADI
#### ADI – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算累積分配指標值。  
> **回傳數值=ADI**  

---

##### 說明
ADI指標的原文是Accumulation Distribution Index，按原文直譯的名稱是「累積分配指標」，其實它真正的意思是「漲跌力道聚散指標」，Accumulation指的是上漲力道在累積，而Distribution指的是上漲力道在消散之意，所以是「聚散指標」。

當日價格上漲時，表示上升力道戰勝，將此上升力道累積起來。

若當日是下跌，便從上升累積力道中減去下降的力道。

範例：

```pascal
value1 = ADI;           //計算累積分配指標
plot1(value1, "A/DI");   
```

___


## ADO
--- 

### ADO
#### ADO – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算聚散擺盪指標值。  
> **回傳數值=ADO**  

---

##### 說明
ADO指標的原文是Accumulation／Distribution Oscillator，直譯為「聚散擺盪」指標。

計算公式如下：
 
ADO＝( BP + SP ) ／ ( 2 * ( 最高價 － 最低價 ) ) * 100

其中

- BP = 最高價－開盤價
- SP = 收盤盤－最低價　

範例：

```pascal
value1 = ADO;              //計算聚散擺盪指標
plot1(value1, "A/D-Osc");   
```

___


## AR
--- 

### AR
#### AR – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算人氣指標值，買賣氣勢強度的測試指標，觀察開盤後對股價的現實反應。  
> **回傳數值=AR(期數)**  

---

##### 說明
AR值高時，代表行情很活潑，當AR值介於0.25至1.85(25%至185%)間時，屬於盤整行情。
AR值低時，表示人氣不足。

計算公式如下：
 
AR ＝ (今日最高價－今日開盤價) N日內總合 ／ (今日開盤價－今日最低價) N日內總合
 
範例：

```pascal
value1 = AR(26);       //計算26期的AR指標
plot1(value1, "AR");   
```

___


## ATR
--- 

### ATR
#### ATR – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算平均真實區間指標值。  
> **回傳數值=ATR(期數)**  

---

##### 說明
平均真實區間是真實區間（True Range）的平均。

真實區間是韋爾達（J. W. Wilder）於1978年發表於New Concepts in Technical Trading Systems中測量價格波動性的方法。

根據韋爾達的定義，真實區間為下列三項中的最大值：
- 當期最高價至最低價的幅度。
- 當期最低價與前期收盤價的幅度。
- 當期最高價至前期收盤價的幅度。

範例：

```pascal
value1 = ATR(14);       //計算14期的ATR指標
plot1(value1, "ATR");   
```

___


## Bias
--- 

### Bias
#### Bias – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算一段時間內的收盤價與均線的乖離程度。  
> **回傳數值=Bias(期數)**  

---

##### 說明
以百分比幅度值表示移動平均線到底離股票價位有多遠。如果我們把移動平均線值當成是市場的平均買入成本的話，則乖離率可以想像成是目前市場上平均的獲利率。

另外，乖離率用來觀察均線回歸的現象。當乖離率來到歷史的極大值或極小值附近時，可能會是趨勢的反轉點。

範例：

```pascal
value1 = Bias(5);       //計算5期的乖離率
plot1(value1, "Bias");   
```

___


## BiasDiff
--- 

### BiasDiff
#### BiasDiff – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算長短期乖離率的差值。  
> **回傳數值=BiasDiff(短期期數,長期期數)**  
> 傳入二個參數:  
> - 第一個參數是較短的期數。  
> - 第二個參數是較長的期數。  

---

##### 說明
除了價格數列和均線間會出現均線回歸的現象外，長短期的均線也會反復出現發散、收斂的循環現象。乖離率差是用來觀察長短期均線相對關係。

範例：

```pascal
value1 = BiasDiff(3,6);       //計算3期與6期的乖離率差
plot1(value1, "BiasDiff");   
```

___


## BollingerBand
--- 

### BollingerBand
#### BollingerBand – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算包寧傑通道線。  
> **回傳數值=BollingerBand(數列,期數,標準差倍數)**  
> 傳入三個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是計算均線的期數。  
> - 第三個參數是決定通道寬度的標準差倍數，輸入正值時為計算上通道，輸入負值時為計算下通道。  

---

##### 說明
包寧傑通道為John Bollinger在1980年代發明的指標。以價格均線為中心點，往上N個標準差為通道上限（壓力線）；往下減去N個標準差，為通道下限（支撐線）。

範例：

```pascal
value1 = BollingerBand(Close,20,2);       //計算20期、2個標準差寬的包寧傑通道上限
plot1(value1, "BollingerUpperBand");   
```

___


## BR
--- 

### BR
#### BR – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算意願指標值，用來觀察開盤前對股價的預期心理。  
> **回傳數值=BR(期數)**  

---

##### 說明
BR買賣意願指標是一種被用來配合[AR](api.aspx?a=AR&b=sys)買賣人氣指標作分析的技術指標。它的公式推算原理方式也相當的類似於AR指標，利用統計某一段時日內，前一日收盤價位分別與當日最高價及當日最低價位二者的差距和的比值，以此來作為該段期間內，買賣行情雙方力道強弱的參考指標。

計算公式：
 
BR ＝ (今日最高價－昨日收盤價) N日內總合 ／ (昨日收盤價－今日最低價)絕對值的N日內總合

範例：

```pascal
value1 = BR(26);       //計算26期的BR指標
plot1(value1, "BR");   
```

___


## CCI
--- 

### CCI
#### CCI – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算CCI技術指標值。  
> **回傳數值=CCI(期數)**  

---

##### 說明
CCI順勢指標為Donald Lambert在1980年代發明的指標。CCI大多時間會落在+100到-100之間，主要的功能在於針對商品本身所具有的週期循環特性，來尋找出行情的高低價位區來。

若CCI值從一高點急速往下降時，可視為是賣出的訊號；同理若CCI值從一低點快速往上升時，可視之為買進的訊號。

範例：

```pascal
value1 = CCI(14);       //計算14期的CCI
plot1(value1, "CCI");   
```

註：CCI函數和[CommodityChannel](api.aspx?a=CommodityChannel&b=sys)函數相同。

___


## CommodityChannel
--- 

### CommodityChannel
#### CommodityChannel – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算CCI技術指標值。  
> **回傳數值=CommodityChannel(期數)**  

---

##### 說明
CCI順勢指標為Donald Lambert在1980年代發明的指標。CCI大多時間會落在+100到-100之間，主要的功能在於針對商品本身所具有的週期循環特性，來尋找出行情的高低價位區來。

若CCI值從一高點急速往下降時，可視為是賣出的訊號；同理若CCI值從一低點快速往上升時，可視之為買進的訊號。

範例：

```pascal
value1 = CommodityChannel(14);       //計算14期的CCI
plot1(value1, "CCI");   
```

註：CommodityChannel函數和[CCI](api.aspx?a=CCI&b=sys)函數相同。

___


## D_Value
--- 

### D_Value
#### D_Value – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算KD指標中的D值。  
> **回傳數值=D_Value(資料期數,D值平滑期數)**  
> 傳入二個參數:  
> - 第一個參數是資料期數，指定計算的區間長度。  
> - 第二個參數是D值平滑期數，指定計算D值所用的平滑期數。  

---

##### 說明
KD指標為美國交易員George Lane所創，原名為Stochastic Oscillator。 
D_Value即隨機指標中的慢速線（%D）。

範例：

```pascal
value1 = D_Value(9,3);       //計算KD指標中的D值
plot1(value1, "D");
```

___


## DIF
--- 

### DIF
#### DIF – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算MACD中的DIF值。  
> **回傳數值=DIF(短期數,長期數)**  
> 傳入二個參數:  
> - 第一個參數是計算快速線（短期）的期數。  
> - 第二個參數是計算慢速線（長期）的期數。  

---

##### 說明
MACD是由Gerald Appel於1970年代所發明的指標。利用二條快速與慢速指數移動平均線的收斂或發散來判斷價格走勢。

DIF是快速線與慢速線的差值。

範例：

```pascal
value1 = DIF(12,26);       //計算MACD中的DIF值
plot1(value1, "DIF");
```

___


## DirectionMovement
--- 

### DirectionMovement
#### DirectionMovement – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算DMI指標。  
> **回傳數值=DirectionMovement(期數,輸出+DI值,輸出-DI值,輸出ADX值)**  
> 傳入四個參數:  
> - 第一個參數是計算期數。  
> - 第二個參數是輸出計算完的+DI值。  
> - 第三個參數是輸出計算完的-DI值。  
> - 第四個參數是輸出計算完的ADX值。  

---

##### 說明
DMI趨向指標是威爾德（Wilder）所發明。主要的用途在於作趨勢成立的判斷，因此是屬於較為長期交易的技術指標。

DMI指標包含了+DI、-DI及ADX三個數值。DirectionMovement函數回傳1時，代表計算成功。+DI、-DI及ADX的值是回傳在第2、3、4個參數。

範例：

```pascal
value1 = DirectionMovement(14,value2,value3,value4);       //計算14期的DMI指標
plot1(value2, "+DI");
plot2(value3, "-DI");
plot3(value4, "ADX");
```

___


## DMO
--- 

### DMO
#### DMO – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算DMO指標。  
> **回傳數值=DMO(期數)**  

---

##### 說明
DMO指標（Directional Movement Oscillator）是利用DMI趨向指標指標中的正負DI線計算，以此二條線的差值做為新的指標線。

範例：

```pascal
value1 = DMO(14);       //計算14期的DMO指標
plot1(value1, "DMO");
```

___


## DPO
--- 

### DPO
#### DPO – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算DPO指標。  
> **回傳數值=DPO(期數)**  

---

##### 說明
非趨勢價格擺盪指標（Detrended Price Oscillator）是Walt Bressert所發明的指標。他研究商品的循環後發現，一個長期波動中包含了多個短期波動。因此，觀察短期波動的變化規律，可以估計長期波動高低點出現的時機。例如：二個短期循環底部，形成一個長期循環底部。因此，DPO指標刻意忽略較長期的波動，一方面可以減少週期干擾的混淆，也可以凸顯個別週期的波動。

範例：

```pascal
value1 = DPO(10);       //計算10期的DPO指標
plot1(value1, "DPO");
```

___


## EMP
--- 

### EMP
#### EMP – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算Empty Line指標值  
> **回傳數值=EMP**  

---

##### 說明
Empty Line是移動平均線的一種變化，它的數值的計算方式是用3期、6期、12期與24期的移動平均線值取平均後產生的。

計算公式：

EMP = （3期收盤價平均 + 6期收盤價平均 + 12期收盤價平均 + 24期收盤價平均）／4

範例：

```pascal
value1 = EMP;       //計算EMP指標
plot1(value1, "EMP");
```

___


## ERC
--- 

### ERC
#### ERC – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算價格變動率的指數移動平均。  
> **回傳數值=ERC(資料期數,平滑期數)**  
> 傳入二個參數:  
> - 第一個參數是計算RC的資料期數。  
> - 第二個參數是計算ERC的平滑期數。  

---

##### 說明
計算當期對N期前的變動幅度，再對此數值取指數移動平均。

範例：

```pascal
value1 = ERC(12,12);       //計算12期的ERC指標
plot1(value1, "ERC");   
```

___


## HL_Osc
--- 

### HL_Osc
#### HL_Osc – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算HL-Osc指標。  
> **回傳數值=HL_Osc**  

---

##### 說明
高低價擺盪指標（High Low Oscillator）是以當日高點至昨收這段價差佔真實區間的比例來判斷強弱勢。

範例：

```pascal
value1 = HL_Osc;       //計算HL-Osc指標
plot1(value1, "HL-Osc");
```

___


## K_Value
--- 

### K_Value
#### K_Value – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算KD指標中的K值。  
> **回傳數值=K_Value(資料期數,K值平滑期數)**  
> 傳入二個參數:  
> - 第一個參數是資料期數，指定計算的區間長度。  
> - 第二個參數是K值平滑期數，指定計算K值所用的平滑期數。  

---

##### 說明
KD指標為美國交易員George Lane所創，原名為Stochastic Oscillator。 
K_Value即隨機指標中的快速線（%K）。


範例：

```pascal
value1 = K_Value(9,3);       //計算KD指標中的K值
plot1(value1, "K");
```

___


## KeltnerLB
--- 

### KeltnerLB
#### KeltnerLB – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算肯特納通道的下通道線（支撐線）。  
> **回傳數值=KeltnerLB(通道倍數)**  

---

##### 說明
肯特納通道是原始概念是由Chester W. Keltner於1960年代所發明。但現在較常用的版本是由Linda Bradford Raschke於1980年代所出的修正版本。

原始版本的肯特納通道是以10期的典型價移動平均線為中心線，然後以10期的當日高低價差平均為通道寬度。

新版的肯特納通道是以20期的收盤價指數移動平均線為中心線，然後以2.5倍的20期真實範圍平均做通道寬度。我們提供的是較新版本的肯特納通道。


範例：

```pascal
value1 = KeltnerLB(2.5);       //計算肯特納通道的下通道線
plot1(value1, "KeltnerLowerBand");
```

___


## KeltnerMA
--- 

### KeltnerMA
#### KeltnerMA – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算肯特納通道的中心線。  
> **回傳數值=KeltnerMA(期數)**  

---

##### 說明
肯特納通道是原始概念是由Chester W. Keltner於1960年代所發明。但現在較常用的版本是由Linda Bradford Raschke於1980年代所出的修正版本。

原始版本的肯特納通道是以10期的典型價移動平均線為中心線，然後以10期的當日高低價差平均為通道寬度。

新版的肯特納通道是以20期的收盤價指數移動平均線為中心線，然後以2.5倍的20期真實範圍平均做通道寬度。我們提供的是較新版本的肯特納通道。


範例：

```pascal
value1 = KeltnerMA(20);       //計算肯特納通道的中心線
plot1(value1, "KeltnerMid");
```

___


## KeltnerUB
--- 

### KeltnerUB
#### KeltnerUB – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算肯特納通道的上通道線（壓力線）。  
> **回傳數值=KeltnerUB(通道倍數)**  

---

##### 說明
肯特納通道是原始概念是由Chester W. Keltner於1960年代所發明。但現在較常用的版本是由Linda Bradford Raschke於1980年代所出的修正版本。

原始版本的肯特納通道是以10期的典型價移動平均線為中心線，然後以10期的當日高低價差平均為通道寬度。

新版的肯特納通道是以20期的收盤價指數移動平均線為中心線，然後以2.5倍的20期真實範圍平均做通道寬度。我們提供的是較新版本的肯特納通道。

範例：

```pascal
value1 = KeltnerUB(2.5);       //計算肯特納通道的上通道線
plot1(value1, "KeltnerUpperBand");
```

___


## KO成交量擺盪指標
--- 

### KO成交量擺盪指標
#### KO成交量擺盪指標 – （系統函數） <kbd>技術指標</kbd>

##### 語法

> 計算KO成交量擺盪值。  
> **回傳數值=callfunction("KO成交量擺盪指標",短期數,長期數,雜訊平滑期數);**  
> 傳入三個參數:  
> - 第一個參數是短期數，計算短期KO成交量的簡單移動平均。  
> - 第二個參數是長期數，計算長期KO成交量的簡單移動平均。  

---

##### 說明

範例：

```pascal
value1 =callfunction("KO成交量擺盪指標", Length1, Length2); 
```

___


## KST確認指標
--- 

### KST確認指標
#### KST確認指標 – （系統函數） <kbd>技術指標</kbd>

##### 語法

> 計算KST確認指標值。  
> **回傳數值=callfunction("KST確認指標");**  

---

##### 說明

詳細說明請參考[交易的點點滴滴](https://xstrader.net/KST確認指標/)。

範例：

```pascal
value1=callfunction("KST確認指標");
```

___


## MA_Osc
--- 

### MA_Osc
#### MA_Osc – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算移動平均線擺盪指標。  
> **回傳數值=MA_Osc(短期數,長期數)**  
> 傳入二個參數:  
> - 第一個參數是計算快速線（短期）的期數。  
> - 第二個參數是計算慢速線（長期）的期數。  

---

##### 說明
MA_Osc是計算二條不同期數的簡單移動平均線差值而得。

範例：

```pascal
value1 = MA_Osc(5,10);       //計算MA-Osc
plot1(value1, "MA_Osc");
```

___


## MACD
--- 

### MACD
#### MACD – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算MACD指標值。  
> **回傳數值=MACD(數列,短期數,長期數,MACD平滑期數,輸出DIF值,輸出MACD值,輸出OSC值)**  
> 傳入七個參數:  
> - 第一個參數是數列，MACD通常是以加權平均收盤價（WeightedClose）來計算。  
> - 第二個參數是計算快速線（短期）的期數。  
> - 第三個參數是計算慢速線（長期）的期數。  
> - 第四個參數是計算MACD使用之平滑期數。  
> - 第五個參數是輸出計算完的DIF值。  
> - 第六個參數是輸出計算完的MACD值。  
> - 第七個參數是輸出計算完的OSC值。  

---

##### 說明
MACD是由Gerald Appel於1970年代所發明的指標。利用二條快速與慢速指數移動平均線的收斂或發散來判斷價格走勢。

MACD指標包含了DIF、MACD及OSC三個數值。MACD函數回傳1時，代表計算成功。DIF、MACD及OSC的值是回傳在第5、6、7個參數。

範例：

```pascal
value1 = MACD(WeightedClose,12,26,9,value2,value3,value4);       //計算MACD
plot1(value2, "DIF");
plot2(value3, "MACD");
plot3(value4, "OSC");   
```

___


## MAM
--- 

### MAM
#### MAM – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算MAM指標。  
> **回傳數值=MAM(移動平均期數,動量期數)**  
> 傳入二個參數:  
> - 第一個參數是用來計算移動平均的期數。  
> - 第二個參數是用來計算動量的期數。  

---

##### 說明
移動平均動量指標（Moving Average Momentum）的用法、概念和Momentum相同，但計算方式改為計算移動平均的動量。

計算公式：當期移動平均值，減去n期前的移動平均值。

範例：

```pascal
value1 = MAM(10,10);       //計算MAM指標
plot1(value1, "MAM");   
```

___


## MI
--- 

### MI
#### MI – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算質量指標。  
> **回傳數值=MI(期數1,期數2)**  
> 傳入二個參數:  
> - 第一個參數是計算指數移動平均的期數。  
> - 第二個參數是計算總和的期數。  

---

##### 說明
MI指標（Mass Index）是由Donald Dorsey所發明。質量指標是觀察高低價範圍的變化，試圖找出趨勢的反轉點。

計算公式： 

EMA1 = (最高價－最低價)的9日EMA
EMA2 = EMA1 的9日EMA
MI = ( EMA1 ／ EMA2 ) 的N2日簡單加總

範例：

```pascal
value1 = MI(9,25);       //計算收盤價10期的質量指標
plot1(value1, "MI");   
```

___


## MO
--- 

### MO
#### MO – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算收盤價變動的百分比。  
> **回傳數值=MO(期數)**  

---

##### 說明
動量震盪指標（Momentum Oscillator）和MTM相類似，都是測量收盤價的變動量。

差別在於MTM指標是計算變動絕對值，而MO為變動的百分比來衡量變動量。

計算公式：

MO = ( 當期收盤價 ／ 前N期收盤價 ) * 100

範例：

```pascal
value1 = MO(10);       //計算收盤價10期的運動量指標
plot1(value1, "MO");   
```

___


## Momentum
--- 

### Momentum
#### Momentum – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算數列指定期間的變動量。  
> **回傳數值=Momentum(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
計算目前K棒與N根K棒之前的差值。

計算公式：

Momentum = 當期價格 - 前N期價格

範例：

```pascal
value1 = Momentum(Close,10);       //計算收盤價10期的運動量指標
plot1(value1, "MTM");   
```

___


## MTM
--- 

### MTM
#### MTM – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算收盤價的變動量。  
> **回傳數值=MTM(期數)**  

---

##### 說明
以收盤價計算目前K棒與N根K棒之前的差值。

計算公式：

MTM = 當期收盤價 - 前N期收盤價

範例：

```pascal
value1 = MTM(10);       //計算收盤價10期的運動量指標
plot1(value1, "MTM");   
```

與[Momentum函數](api.aspx?a=momentum&b=sys)相同。

___


## MTM_MA
--- 

### MTM_MA
#### MTM_MA – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 平均運動量指標，計算運動量指標的簡單移動平均。  
> **回傳數值=MTM_MA(期數)**  

---

##### 說明
計算公式：

MTM_MA = （當期收盤價 - 前N期收盤價）的N期平均

範例：

```pascal
value1 = MTM_MA(10);       //計算收盤價10期的平均運動量指標
plot1(value1, "MTM_MA");   
```

___


## PercentR
--- 

### PercentR
#### PercentR – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算威廉指標（或稱百分比R、%R）。  
> **回傳數值=PercentR(期數)**  

---

##### 說明
由Larry Williams所提出，將當前收盤價在指定期間內的區間最高價與最低價之間位置，以百分比表示。

範例：

```pascal
value1 = PercentR(12) - 100;       //計算12期的威廉指標
plot1(value1, "%R");   
```

___


## PSY
--- 

### PSY
#### PSY – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 人氣指標心理線。  
> **回傳數值=PSY(期數)**  

---

##### 說明
計算特定期間內，行情上漲期數的比例。

計算公式：

PSY = 100 * 上漲次數／總次數

範例：

```pascal
value1 = PSY(12);       //計算12期的心理線指標
plot1(value1, "PSY");   
```

___


## Q指標
--- 

### Q指標
#### Q指標 – （系統函數） <kbd>技術指標</kbd>

##### 語法

> 計算技術分析的Q值。  
> **回傳數值=callfunction("Q指標",期數,平滑期數,雜訊平滑期數);**  
> 傳入三個參數:  
> - 第一個參數是期數，指定要計算累積價格變化的區間。  
> - 第二個參數是平滑期數，計算累積價格變化的簡單移動平均。  
> - 第三個參數是雜訊平滑期數，計算雜訊的簡單移動平均。  

---

##### 說明

詳細說明請參考[交易的點點滴滴](https://xstrader.net/自訂指標的撰寫技巧以q指標為例/)。

___


## RC
--- 

### RC
#### RC – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算價格變動率。  
> **回傳數值=RC(期數)**  

---

##### 說明
計算當期對N期前的變動幅度。

計算公式：

RC = （當期收盤價／前N期收盤價）／前N期收盤價

範例：

```pascal
value1 = RC(12);       //計算12期的RC指標
plot1(value1, "RC");   
```

___


## RSI
--- 

### RSI
#### RSI – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算相對強弱指標數值。  
> **回傳數值=RSI(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
RSI是相對強弱指標（Relative Strength Index）用於衡量一個資產的過去價格變動，並評估其是否處於超買或超賣的狀態。

RSI的計算基於資產的價格變動幅度，通常在一段時間內（例如14個交易日）內進行計算。指標的值位於0到100之間，通常被分成以下幾個區域：

- 80以上：表示該資產可能處於超買狀態，可能會有回調或調整的風險。

- 20以下：表示該資產可能處於超賣狀態，可能會有反彈或上漲的機會。

投資者可以利用RSI指標來識別潛在的轉折點，例如在RSI進入超買或超賣區域時，可能預示著價格反轉的機會。

範例：

```pascal
value1 = RSI(Close,6);       //計算6期的RSI指標
plot1(value1, "RSI");   
```

___


## RSV
--- 

### RSV
#### RSV – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 未成熟隨機值  
> **回傳數值=RSV(期數)**  

---

##### 說明
計算收盤價在指定期間內的區間最高價與最低價之間位置，以百分比表示。後續可用來計算KD指標的K值與D值。

計算公式：

RSV=(收盤價－n日之最低價)／(n日內最高價－n日最低價)＊100

範例：

```pascal
value1 = RSV(9);       //計算9期的RSV指標
plot1(value1, "RSV");   
```

___


## SAR
--- 

### SAR
#### SAR – （系統函數） <kbd>技術指標</kbd>

##### 語法
> SAR停損點轉向指標，或稱為拋物線型指標，為一種設定停損點相當有效力的指標。  
> **回傳數值=SAR(加速因子初始值,加速因子遞增值,加速因子最大值)**  
> 傳入三個參數:  
> - 第一個參數是加速因子初始值。  
> - 第二個參數是加速因子遞增值。  
> - 第三個參數是加速因子最大值。  

---

##### 說明
由威爾德（Wilder）發明的停損點轉向操作系統（SAR, Stop And Reverse）或者稱之為拋物線型指標（Parabolic Time/Price），是一種隨著時間的延續，用類似於拋物曲線的追趕方式，來追趕價位行情，以便設定出買賣操作時的停損點反轉值，使得一旦行情觸及停損反轉時，可以依照訊號進行買賣的動作。

範例：

```pascal
value1 = SAR(0.02, 0.02, 0.2);       //計算SAR指標
plot1(value1, "SAR");   
```

___


## Stochastic
--- 

### Stochastic
#### Stochastic – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算KD指標。  
> **回傳數值=Stochastic(資料期數,K值平滑期數,D值平滑期數,輸出RSV值,輸出K值,輸出D值)**  
> 傳入六個參數:  
>   
> - 第一個參數是資料期數，指定計算的區間長度。  
> - 第二個參數是K值平滑期數，指定計算K值所用的平滑期數。  
> - 第三個參數是D值平滑期數，指定計算D值所用的平滑期數。  
> **- 第四個參數是輸出RSV值，回傳計算完的RSV值。**  
> **- 第五個參數是輸出K值，回傳計算完的K值。**  
> **- 第六個參數是輸出D值，回傳計算完的D值。**  

---

##### 說明
KD指標為美國交易員George Lane所創，原名為Stochastic Oscillator。 

Stochastic函數可計算KD指標的RSV、K及D三個數值。Stochastic函數回傳1時，代表計算成功。RSV、K及D的值是回傳在第4、5、6個參數。

範例：

```pascal
value1 = Stochastic(9,3,3,value2,value3,value4);       //計算KD指標
plot1(value3, "K");
plot2(value4, "D");     
```

___


## TechScore
--- 

### TechScore
#### TechScore – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算多空判斷分數。  
> **回傳數值=TechScore**  

---

##### 說明
利用多種指標計算多空分數，綜合研判後續走勢。使用的指標包括：Arron指標、隨機漫步指標、順勢指標、CMO錢德動量擺動指標、RSI、MACD、MTM、KD、DMI、AR、ACC、TRIX、SAR及均線計14種。

多空判斷分數會介於0~14之間，12以上是超買區、3以下是超賣區。

範例：

```pascal
value1 = TechScore;       //計算多空判斷分數
plot1(value1, "多空指標");
```

___


## TRIX
--- 

### TRIX
#### TRIX – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 三重指數平滑移動平均指標。  
> **回傳數值=TRIX(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
TRIX是在1980年代由Jack Hutson所發明的指標。TRIX指的是對股價X取TRIPLE （三次） 平滑的意思。將數值計算三次指數移動平均（EMA，也就是MACD式平滑法）之後的數列，再計算其變動率而得。

範例：

```pascal
value1 = TRIX(Close, 9);       //計算9期TRIX指標
plot1(value1, "TRIX");
```

___


## VA
--- 

### VA
#### VA – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算成交量累散佈指標。  
> **回傳數值=VA**  

---

##### 說明
VA指標的原文是Volume Accumulation／Distribution指標，原文的意思直譯的話，稱為「成交量累積散佈」指標。它的公式與修正OBV公式完全相同，沒有兩樣。

VA屬於累積型的指標，指標值會因計算的起始點不同而有所差異。

範例：

```pascal
value1 = VA;       //計算成交量累散佈指標
plot1(value1, "VA");
```

___


## VAO
--- 

### VAO
#### VAO – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算成交量累散佈擺盪指標。  
> **回傳數值=VAO**  

---

##### 說明
VAO指標的原文是Volume Accumulation／Distribution Oscillator指標，按照原文的意思直譯為「成交量累積散佈擺盪」指標。累積指的自然是籌碼集中累積到少數人手上的現象，而散佈自然是指籌碼散佈分散到多數人手上的現象。這個指標與VA指標（即修正OBV指標）幾乎雷同，唯一的差別是VA指標要逐日累加，VAO不累加而已。

範例：

```pascal
value1 = VAO;       //計算成交量累散佈擺盪指標
plot1(value1, "VAO");
```

___


## VHF
--- 

### VHF
#### VHF – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算垂直水平過濾指標。  
> **回傳數值=VHF(期數)**  

---

##### 說明
本指標由亞當．懷特（Adam White）所發明，用來確定價格的變動是處於水平變動（區間橫向整理期），或是垂直變動（固定趨勢的大幅漲跌期）的階段。然後投資人可依此選用趨勢指標或震盪指標，來決定買賣的時機。

範例：

```pascal
value1 = VHF(42);       //計算42期的VHF指標
plot1(value1, "VHF");   
```

___


## VPT
--- 

### VPT
#### VPT – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算量價趨勢指標。  
> **回傳數值=VPT**  

---

##### 說明
VPT（Volume Price Trend）量價趨勢指標，或被稱為PVT指標，也是一種類似於OBV的技術指標。而它所累算的是價格漲跌幅與成交量的乘積。


範例：

```pascal
value1 = VPT;       //計算量價趨勢指標
plot1(value1, "VPT");
```

___


## VR
--- 

### VR
#### VR – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算成交量比率指標。  
> **回傳數值=VR(期數)**  

---

##### 說明
VR(Volume Ratio)中文譯為「容量比率」，或者又稱為「成交量比率指標」。其計算方式為針對特定期間內，累加上漲日的成交量作為分子，以及累加下跌日的成交量作為分母，然後將此兩數相除即得。

VR指標的設計原意，是要利用量價關係的基本原理，來作為研判股價的可能變動方向。

如果VR公式中的分子與分母大小相同，則VR的數值會剛好等於100，表示計算期間內的上漲成交量等於下跌成交量。當VR大於100，表示上漲成交量大於下跌成交量；而VR小於100，則表示上漲成交量小於下跌成交量。

不過，由於在股巿中，股價上漲時成交量的擴增比較沒有上限，可以擴增到數倍（甚或數十倍）之多；而股價下跌時成交量的下降反而比較有限，頂多只降個幾十個百分點（最多不會超過100%）。所以VR指標不會出現剛好以100為中心，上下波動幅度相同的情況。而是VR的高點會明顯大於100很多，低點則小於100的程度不大。

範例：

```pascal
value1 = VR(26);       //計算26期的VR指標
plot1(value1, "VR");   
```

___


## VVA
--- 

### VVA
#### VVA – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算VVA指標。  
> **回傳數值=VVA**  

---

##### 說明
OBV的變形累算方法，除了VA成交量累散佈指標以外，還有另外一種的變化方式，即VVA指標(Variable Volume Accumulation/Distribution)。

VVA屬於累積型的指標，指標值會因計算的起始點不同而有所差異。

範例：

```pascal
value1 = VVA;       //計算VVA指標
plot1(value1, "VVA");
```

___


## WAD
--- 

### WAD
#### WAD – （系統函數） <kbd>技術指標</kbd>

##### 語法
> 計算威廉多空力度線(Williams Accumulation/Distribution)。  
> **回傳數值=WAD**  

---

##### 說明
由Larry Williams所發明的指標，屬於累積型的指標，指標值會因計算的起始點不同而有所差異。

範例：

```pascal
value1 = WAD;              //計算威廉多空力度線
plot1(value1, "WA/D");   
```

___


## AverageIF
--- 

### AverageIF
#### AverageIF – （系統函數） <kbd>日期相關</kbd>

##### 語法
> 計算符合條件的數值平均。  
> **回傳數值=AverageIF(條件數列,資料數列,期數)**  
> 傳入三個參數:  
> - 第一個參數是條件數列，當條件值為True時，才會納入計算平均。  
> - 第二個參數是資料數列，通常是開高低收的價格數列。  
> - 第三個參數是期數。  

---

##### 說明
範例：

```pascal
value1 = averageif(open>close[1],rateofchange(close,1),5); //計算開高時漲跌幅5期平均
```

___


## CountIf
--- 

### CountIf
#### CountIf – （系統函數） <kbd>日期相關</kbd>

##### 語法
> 計算符合條件的次數。  
> **回傳數值=CountIf(條件數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是條件數列，當條件值為True時，才會納入計算。  
> - 第二個參數是期數。  

---

##### 說明
CountIF會計算特定期間內符合某些條件的次數。

範例：

```pascal
value1 = CountIf(open>close[1],5); //計算過去5天開高的次數
```

___


## CountIfARow
--- 

### CountIfARow
#### CountIfARow – （系統函數） <kbd>日期相關</kbd>

##### 語法
> 計算符合條件連續符合的次數。  
> **回傳數值=CountIfARow(條件數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是條件數列。  
> - 第二個參數是期數。  

---

##### 說明
以最新的資料為基準，往前計算連續符合條件的次數。

範例：

```pascal
value1 = CountIfARow(close>close[1],5); //計算過去5天連續收紅的次數
```

註：CountIfARow函數和[TrueCount](api.aspx?a=TrueCount&b=sys)函數相同。

___


## CrossOver
--- 

### CrossOver
#### CrossOver – （系統函數） <kbd>日期相關</kbd>

##### 語法
> 判斷數列一是否由下往上穿越數列二，又稱黃金交叉。  
> **回傳布林值=CrossOver(數列一,數列二)**  
> 傳入二個參數:  
> - 第一個參數是數列一。  
> - 第二個參數是數列二。  

---

##### 說明
如果出現黃金交叉傳回True，其他狀況傳回False。

範例：

```pascal
condition1 = CrossOver(Average(close,5),Average(close,10)); //判斷5期均線和10期均線是否黃金交叉
```

___


## CrossUnder
--- 

### CrossUnder
#### CrossUnder – （系統函數） <kbd>日期相關</kbd>

##### 語法
> 判斷數列一是否由上往下穿越數列二，又稱死亡交叉。  
> **回傳布林值=CrossUnder(數列一,數列二)**  
> 傳入二個參數:  
> - 第一個參數是數列一。  
> - 第二個參數是數列二。  

---

##### 說明
如果出現死亡交叉傳回True，其他狀況傳回False。

範例：

```pascal
condition1 = CrossUnder(Average(close,5),Average(close,10)); //判斷5期均線和10期均線是否死亡交叉
```

___


## DateTime
--- 

### DateTime
#### DateTime – （系統函數） <kbd>日期相關</kbd>

##### 語法
> 資料的日期與時間，格式為14碼的數字。  
> **當日期為西元2015年6月30日，且時間為12點30分00秒時，回傳值為20150630123000。**  

---

##### 說明


___


## Filter
--- 

### Filter
#### Filter – （系統函數） <kbd>日期相關</kbd>

##### 語法
> 過濾指定期數內重複出現的警示。  
> **回傳布林值=Filter(條件布林值,過濾期數)**  
> 傳入二個參數:  
> - 第一個參數是代表被過濾條件是否成立的布林值。  
> - 第二個參數是要過濾重複出現警示的期數。  

---

##### 說明
當條件成立後，過濾在指定期數內重複出現的警示。例如：當股價第一次創20日新高時，未來5天再創20日新高就不再警示。

回傳TRUE，表示過濾後仍然成立的條件，意即原始條件為TRUE且距離原始條件成立的期數大於過濾期數。
回傳FALSE，表示過濾後不成立的條件，意即原始條件為FALSE，或是距離原始條件成立的期數小於等於過濾期數。

範例：

```pascal
//警示腳本
condition1 = high = highest(high,20);       //判斷今高是否為20期之高點
condition2 = filter(condition1,5);       //過濾未來5期內重複的創新高警示
if condition2 then ret = 1;       
```

___


## GetBarOffsetForYears
--- 

### GetBarOffsetForYears
#### GetBarOffsetForYears – （系統函數） <kbd>日期相關</kbd>

##### 語法
> 依年份取得相對K棒位置。  
> **回傳數值=GetBarOffsetForYears(數值)**  

---

##### 說明
依傳入的年份計算相對K棒的位置。
當回傳值為0時，表示傳入年份 ≧K棒根數。

___


## IFF
--- 

### IFF
#### IFF – （系統函數） <kbd>日期相關</kbd>

##### 語法
> **依條件成立狀況回傳對應的值。**  
> **回傳數值=IFF(條件,條件成立時的回傳值,條件不成立時的回傳值)**  
> 傳入三個參數:  
> - 第一個參數是條件。  
> **- 第二個參數是條件成立時的回傳值。**  
> **- 第三個參數是條件不成立時的回傳值。**  

---

##### 說明
把IF/Else的邏輯判斷用函數的形式來表示。

範例：

```pascal
value1 = IFF(Close>Close[1],1,0); //當上漲時value1為1，其他狀況時value1為0
```

___


## SummationIf
--- 

### SummationIf
#### SummationIf – （系統函數） <kbd>日期相關</kbd>

##### 語法
> 計算符合條件的數值總和。  
> **回傳數值=SummationIf(條件數列,資料數列,期數)**  
> 傳入三個參數:  
> - 第一個參數是條件數列，當條件值為True時，才會納入計算總和。  
> - 第二個參數是資料數列，通常是開高低收的價格數列。  
> - 第三個參數是期數。  

---

##### 說明
當某期資料符合某項判斷準則時，才將該期資料計入加總。

範例：

```pascal
value1 = SummationIf(open>close[1],rateofchange(close,1),5); //計算近5期開高時的漲跌幅總和
```

___


## TrueAll
--- 

### TrueAll
#### TrueAll – （系統函數） <kbd>日期相關</kbd>

##### 語法
> 判斷條件數列在指定期數內是否同時成立。  
> **回傳布林值=TrueAll(條件數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是條件數列。  
> - 第二個參數是期數。  

---

##### 說明
當期間內所有條件皆成立時，回傳True；其他狀況則回傳False

範例：

```pascal
condition1 = TrueAll(Close>Close[1],3); //判斷K棒是否連續三期上漲
```

___


## TrueAny
--- 

### TrueAny
#### TrueAny – （系統函數） <kbd>日期相關</kbd>

##### 語法
> 判斷條件數列在指定期數內是否有任何一筆成立。  
> **回傳布林值=TrueAny(條件數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是條件數列。  
> - 第二個參數是期數。  

---

##### 說明
當期間內有一筆以上條件成立時，回傳True；其他狀況則回傳False

範例：

```pascal
condition1 = TrueAny(Close>Close[1],3); //判斷最近三期是否有任一期K棒上漲
```

___


## TrueCount
--- 

### TrueCount
#### TrueCount – （系統函數） <kbd>日期相關</kbd>

##### 語法
> 計算符合條件連續符合的次數。  
> **回傳數值=TrueCount(條件數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是條件數列。  
> - 第二個參數是期數。  

---

##### 說明
以最新的資料為基準，往前計算連續符合條件的次數。

範例：

```pascal
value1 = TrueCount(close>close[1],5); //計算過去5天連續收紅的次數
```

註：TrueCount函數和[CountIfARow](api.aspx?a=CountIfARow&b=sys)函數相同。

___


## CoefficientR
--- 

### CoefficientR
#### CoefficientR – （系統函數） <kbd>期權相關</kbd>

##### 語法
> 計算兩個數列的Pearson積差相關係數。  
> **回傳數值=CoefficientR(數列一,數列二,期數)**  
> 傳入三個參數:  
> - 第一個參數是第一個數列，通常是開高低收的價格數列。  
> - 第二個參數是第二個數列，通常是開高低收的價格數列。  
> - 第三個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的相關係數。

回傳數值會介於-1到1之間。如果無法計算，會傳回-2。

範例：

```pascal
value1 = GetField("外資買賣超金額");
value2 = rateofchange(close,1);          //計算當日漲跌幅
value3 = coefficientr(value1,value2,20); //計算外資買賣超金額與大盤漲跌幅的相關係數
plot1(value3);
```

___


## Correlation
--- 

### Correlation
#### Correlation – （系統函數） <kbd>期權相關</kbd>

##### 語法
> 計算兩個數列的相關係數。  
> **回傳數值=Correlation(數列一,數列二,期數)**  
> 傳入三個參數:  
> - 第一個參數是第一個數列，通常是開高低收的價格數列。  
> - 第二個參數是第二個數列，通常是開高低收的價格數列。  
> - 第三個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的相關係數。

回傳數值會介於-1到1之間。如果無法計算，會傳回-2。

範例：

```pascal
value1 = GetField("外資買賣超金額");
value2 = rateofchange(close,1);          //計算當日漲跌幅
value3 = Correlation(value1,value2,20); //計算外資買賣超金額與大盤漲跌幅的相關係數
plot1(value3);
```

___


## Covariance
--- 

### Covariance
#### Covariance – （系統函數） <kbd>期權相關</kbd>

##### 語法
> 計算兩個數列的共變異數。  
> **回傳數值=Covariance(數列一,數列二,期數)**  
> 傳入三個參數:  
> - 第一個參數是第一個數列，通常是開高低收的價格數列。  
> - 第二個參數是第二個數列，通常是開高低收的價格數列。  
> - 第三個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的共變異數。

範例：

```pascal
value1 = GetField("外資買賣超金額");
value2 = rateofchange(close,1);        //計算當日漲跌幅
value3 = Covariance(value1,value2,20); //計算外資買賣超金額與大盤漲跌幅的共變異數
plot1(value3);
```

___


## RSquare
--- 

### RSquare
#### RSquare – （系統函數） <kbd>期權相關</kbd>

##### 語法
> 計算兩個數列的R平方值。  
> **回傳數值=RSquare(數列一,數列二,期數)**  
> 傳入三個參數:  
> - 第一個參數是第一個數列，通常是開高低收的價格數列。  
> - 第二個參數是第二個數列，通常是開高低收的價格數列。  
> - 第三個參數是期數。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的R平方值。

範例：

```pascal
value1 = GetField("外資買賣超金額");
value2 = rateofchange(close,1);          //計算當日漲跌幅
value3 = RSquare(value1,value2,20); //計算外資買賣超金額與大盤漲跌幅的R平方值
plot1(value3);
```

___


## StandardDev
--- 

### StandardDev
#### StandardDev – （系統函數） <kbd>期權相關</kbd>

##### 語法
> 計算數列的標準差。  
> **回傳數值=StandardDev(數列,期數,母體或樣本)**  
> 傳入三個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  
> - 第三個參數是指定計算是母體標準差(1)或樣本標準差(2)。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的標準差。

提供母體（Population）或樣本（Sample）二種計算方式。

範例：

```pascal
value1 = StandardDev(close,20,2); //計算收盤價的標準差
plot1(value1);
```

___


## VariancePS
--- 

### VariancePS
#### VariancePS – （系統函數） <kbd>期權相關</kbd>

##### 語法
> 計算數列的變異數。  
> **回傳數值=VariancePS(數列,期數,母體或樣本)**  
> 傳入三個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  
> - 第三個參數是指定計算是母體變異數(1)或樣本變異數(2)。  

---

##### 說明
以最新一筆資料為基準點，輸入要計算的期數，然後計算過去期數的變異數。

提供母體（Population）或樣本（Sample）二種計算方式。

範例：

```pascal
value1 = VariancePS(close,20,2); //計算收盤價的變異數
plot1(value1);
```

___


## Angle
--- 

### Angle
#### Angle – （系統函數） <kbd>統計分析</kbd>

##### 語法
> 計算任意二個日期的走勢角度。  
> **回傳數值=Angle(日期1,日期2)**  
> 傳入二個參數:  
> - 第一個參數是日期1。  
> - 第二個參數是日期2，需大於日期1。  

---

##### 說明
任意二個日期間的價格角度可以代表趨勢的強度。我們利用第一個日期的開盤價及第二個日期的收盤價計算整段走勢的角度。

當回傳數值大於0時，代表趨勢向上；當回傳數值小於0時，代表趨勢向下。

範例：

```pascal
value1 = Angle(date[3],date); //計算近四期走勢的角度
```

___


## LinearReg
--- 

### LinearReg
#### LinearReg – （系統函數） <kbd>統計分析</kbd>

##### 語法
> 計算線性迴歸的斜率與角度，以及預測資料投影點的位置。  
> **回傳數值=LinearReg(數列,期數,預測值的相對K棒位置,輸出斜率,輸出弧度,輸出X軸截距,輸出預測值)**  
> 傳入七個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  
> - 第三個參數是預測值的相對K棒位置，和序列引用定義相同，0表當期、1表前一期、-1表後一期。  
> - 第四個參數是輸出計算完的線性回歸線斜率。  
> - 第五個參數是輸出計算完的線性回歸線弧度。  
> - 第六個參數是輸出計算完的線性回歸線X軸截距。  
> - 第七個參數是輸出計算完的線性回歸線預測值。  

---

##### 說明
LinearReg函數回傳1時，代表計算成功。斜率、弧度、X軸截距及預測值是回傳在第4、5、6、7個參數。

範例：

```pascal
value1 = linearreg(close,20,-1,value2,value3,value4,value5); //計算收盤價20期的線性迴歸
plot1(value5);                                               //繪製明天的收盤價線性迴歸預測值連線
```

___


## LinearRegAngle
--- 

### LinearRegAngle
#### LinearRegAngle – （系統函數） <kbd>統計分析</kbd>

##### 語法
> 計算線性迴歸的弧度。  
> **回傳數值=LinearRegAngle(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
利用最小平方法計算線性回歸的角度。

範例：

```pascal
value1 = LinearRegAngle(close,20); //計算收盤價20期的線性迴歸線角度
```

___


## LinearRegSlope
--- 

### LinearRegSlope
#### LinearRegSlope – （系統函數） <kbd>統計分析</kbd>

##### 語法
> 計算線性迴歸的斜率。  
> **回傳數值=LinearRegSlope(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
利用最小平方法計算線性回歸的斜率。

範例：

```pascal
value1 = LinearRegSlope(close,20); //計算收盤價20期的線性迴歸線斜率
```

___


## SwingHigh
--- 

### SwingHigh
#### SwingHigh – （系統函數） <kbd>統計分析</kbd>

##### 語法
> 計算數列最近N個的轉折高點數值。  
> **回傳數值=SwingHigh(數列,期數,左肩期數,右肩期數,第幾個高點)**  
> 傳入五個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是要尋找轉折點的樣本期數。  
> - 第三個參數是高點左側要有幾筆較低的數值。  
> - 第四個參數是高點右側要有幾筆較低的數值。  
> - 第五個參數是第幾個高點，依圖表由右往左(時間新到舊)，1為最近一次的高點、2為第二近的高點。  

---

##### 說明
若某一筆資料的左右二側數值在指定的期數內都比該筆資料低的話，則定義為轉折高點。

當無法找到對應的轉折高點時，回傳值為-1。

範例：

```pascal
value1 = SwingHigh(High,20,3,3,2); //找出過去20期內，第2個轉折高點
```

___


## SwingHighBar
--- 

### SwingHighBar
#### SwingHighBar – （系統函數） <kbd>統計分析</kbd>

##### 語法
> 計算數列最近N個的轉折高點的相對位置。  
> **回傳數值=SwingHighBar(數列,期數,左肩期數,右肩期數,第幾個高點)**  
> 傳入五個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是要尋找轉折點的樣本期數。  
> - 第三個參數是高點左側要有幾筆較低的數值。  
> - 第四個參數是高點右側要有幾筆較低的數值。  
> - 第五個參數是第幾個高點，依圖表由右往左(時間新到舊)，1為最近一次的高點、2為第二近的高點。  

---

##### 說明
若某一筆資料的左右二側數值在指定的期數內都比該筆資料低的話，則定義為轉折高點。

當無法找到對應的轉折高點時，回傳值為-1。

範例：

```pascal
value1 = SwingHighBar(High,20,3,3,2); //找出過去20期內，第2個轉折高點的相對位置
```

___


## SwingLow
--- 

### SwingLow
#### SwingLow – （系統函數） <kbd>統計分析</kbd>

##### 語法
> 計算數列最近N個的轉折低點數值。  
> **回傳數值=SwingLow(數列,期數,左肩期數,右肩期數,第幾個低點)**  
> 傳入五個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是要尋找轉折點的樣本期數。  
> - 第三個參數是高點左側要有幾筆較高的數值。  
> - 第四個參數是高點右側要有幾筆較高的數值。  
> - 第五個參數是第幾個低點，依圖表由右往左(時間新到舊)，1為最近一次的低點、2為第二近的低點。  

---

##### 說明
若某一筆資料的左右二側數值在指定的期數內都比該筆資料高的話，則定義為轉折低點。

當無法找到對應的轉折低點時，回傳值為-1。

範例：

```pascal
value1 = SwingLow(Low,20,3,3,1); //找出過去20期內，第1個轉折低點
```

___


## SwingLowBar
--- 

### SwingLowBar
#### SwingLowBar – （系統函數） <kbd>統計分析</kbd>

##### 語法
> 計算數列最近N個的轉折低點的相對位置。  
> **回傳數值=SwingLowBar(數列,期數,左肩期數,右肩期數,第幾個低點)**  
> 傳入五個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是要尋找轉折點的樣本期數。  
> - 第三個參數是高點左側要有幾筆較高的數值。  
> - 第四個參數是高點右側要有幾筆較高的數值。  
> - 第五個參數是第幾個低點，依圖表由右往左(時間新到舊)，1為最近一次的低點、2為第二近的低點。  

---

##### 說明
若某一筆資料的左右二側數值在指定的期數內都比該筆資料高的話，則定義為轉折低點。

當無法找到對應的轉折低點時，回傳值為-1。

範例：

```pascal
value1 = SwingLowBar(Low,20,3,3,1); //找出過去20期內，第1個轉折低點的相對位置
```

___


## TimeSeriesForecast
--- 

### TimeSeriesForecast
#### TimeSeriesForecast – （系統函數） <kbd>統計分析</kbd>

##### 語法
> 計算線性迴歸預測資料投影點的位置。  
> **回傳數值=TimeSeriesForecast(數列,期數,預測值的相對K棒位置)**  
> 傳入三個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  
> - 第三個參數是預測值的相對K棒位置，和序列引用定義相同，0表當期、1表前一期、-1表後一期。  

---

##### 說明
利用最小平方法計算線性回歸的預測值。

範例：

```pascal
value1 = TimeSeriesForecast(close,20,-1); //計算收盤價20期的線性迴歸
plot1(value1);                            //繪製明天的收盤價線性迴歸預測值連線
```

___


## TSELSindex
--- 

### TSELSindex
#### TSELSindex – （系統函數） <kbd>統計分析</kbd>

##### 語法
> 利用外資買賣超金額計算大盤的多空狀態。  
> **回傳數值=TSELSindex(期數,標準)**  
> 傳入二個參數:  
> - 第一個參數是期數，指定要計算的區間。  
> - 第二個參數是標準，要買超至少幾日才算多頭。  

---

##### 說明
詳細說明請參考[交易的點點滴滴](https://xstrader.net/打造自己的大盤多空函數/)。

___


## TSEMFI
--- 

### TSEMFI
#### TSEMFI – （系統函數） <kbd>統計分析</kbd>

##### 語法
> 利用大盤的資金流向指標來判斷多空方向  
> **回傳數值 = TSEMFI**  
> **如果是多頭，回傳1，如果是空頭，回傳0**  

---

##### 說明


___


## UpShadow
--- 

### UpShadow
#### UpShadow – （系統函數） <kbd>統計分析</kbd>

##### 語法
> **回傳目前K棒上影線佔整根K棒的比例。**  
> **回傳數值=UpShadow**  

---

##### 說明
範例：

```pascal
value1 =UpShadow; //計算當期K棒之上影線佔整根K棒比例
value2 =UpShadow[1]; //計算前一期K棒之上影線佔整根K棒比例
```

___


## angleprice
--- 

### angleprice
#### angleprice – （系統函數） <kbd>趨勢分析</kbd>

##### 語法
> 傳回「N期至今的角度的趨勢線價格」  
> **回傳數值=Angleprice(期數,角度)**  
> 傳入二個參數:  
> - 第一個參數是期數。  
> - 第二個參數是角度。  

---

##### 說明
用前N期到現在的角度，運算出趨勢線的價格。

範例：

```pascal
value1 = angleprice(5,0);
plot1(value1); //Value1為前五期的開盤價，因為第二個參數是0度，所以會等於前五期的開盤價。
```

更多的資訊，請參考[常用語法匯總](https://www.xq.com.tw/xstrader/%E5%B8%B8%E7%94%A8%E7%9A%84%E8%AA%9E%E6%B3%95%E5%8C%AF%E7%B8%BD/)

___


## BarsLast
--- 

### BarsLast
#### BarsLast – （系統函數） <kbd>趨勢分析</kbd>

##### 語法
> 取得上一次條件成立到當前的K棒數  
> **回傳數值=BarsLast(條件數列)**  

---

##### 說明
計算目前K棒與上次條件成立K棒的期數差。例如，上次KD黃金交叉是幾天前。

回傳值為0表示條件成立當期，回傳值為1表示前1期條件成立，依此類推。

範例：

```pascal
value1 = average(C,5);
value2 = average(C,20);
value3 = barslast(value1 cross over value2);       //計算上次5日均線和20日均線黃金交叉的期數差
value4 = low[value3];       //取得上次均線黃金交叉時的最低價做為支撐價
plot1(value4);       //繪製支撐價的連線
```

___


## DaysToExpiration
--- 

### DaysToExpiration
#### DaysToExpiration – （系統函數） <kbd>趨勢分析</kbd>

##### 語法
> 計算台股指數類期貨商品的到期天數。  
> **回傳數值=DaysToExpiration(商品月份,商品年份)**  
> 傳入二個參數:  
> - 第一個參數是商品月份。  
> - 第二個參數是商品年份。  

---

##### 說明
台股指數類期貨商品的到期日期為該月的第三個星期三。此函數會計算特定合約距當期K棒的天數。

回傳值為1，表示當天為結算日。回傳值小於1，表示該合約已到期。

範例：

```pascal
value1 = DaysToExpiration(month(date),year(date));
if value1 <= 1 then begin
	value2 = dateadd(date,"M",1);
	value2 = encodedate(year(value2),month(value2),1);
	value1 = DaysToExpiration(month(value2),year(value2));
end;
plot1(value1); //繪製最新的台股指數類期貨到期天數的連線
```

注意，此函數並無調整因放假而導致的到期日異動。

___


## DownTrend
--- 

### DownTrend
#### DownTrend – （系統函數） <kbd>趨勢分析</kbd>

##### 語法
> 判斷某個序列是否趨勢向下。  
> **回傳布林值=DownTrend(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，可以是GetField("欄位名稱")。  
> - 第二個參數是期數。  

---

##### 說明
計算序列資料是否趨勢向下。回傳布林值。
若為趨勢向上，則回傳「True」
若不為趨勢向上，則回傳「False」

___


## formatMQY
--- 

### formatMQY
#### formatMQY – （系統函數） <kbd>趨勢分析</kbd>

##### 語法
> 依目前資料頻率取得代表日期字串。  
> **回傳字串=formatMQY(參考日期)**  
> 傳入一個參數:  
> - 第一個參數是日期，格式為YYYYMMDD的數值。  

---

##### 說明
formatMQY回傳的字串為：
- 當頻率為年時，回傳格式為YYYY的字串；例如：2015。
- 當頻率為季時，回傳格式為YYYYQQ的字串；例如：2015Q1。
- 當頻率為月時，回傳格式為YYYYMM的字串；例如：201501。
- 當其他頻率時，回傳格式為YYYYMMDD的字串；例如：20150103。

範例：

```pascal
var: string1("");
string1 = formatMQY(date); //將日期轉換為MQY格式的字串
print(date," ",string1); 
```

___


## GetLastTradeDate
--- 

### GetLastTradeDate
#### GetLastTradeDate – （系統函數） <kbd>趨勢分析</kbd>

##### 語法
> 取得台股指數類期貨商品的到期日期（該月第三個星期三）。  
> **回傳數值=GetLastTradeDate(商品月份,商品年份)**  
> 傳入二個參數:  
> - 第一個參數是商品月份。  
> - 第二個參數是商品年份。  

---

##### 說明
依台灣期貨交易所規定台股指數類期貨商品的到期日期為該月的第三個星期三。

函數回傳值的格式為8碼數字: **YYYYMMDD**。


範例：

```pascal
value1 = GetLastTradeDate(7,2015); //取得台股指數類期貨2015年7月合約的到期日
```

注意，此函數並無調整因放假而導致的到期日異動。

___


## LastDayOfMonth
--- 

### LastDayOfMonth
#### LastDayOfMonth – （系統函數） <kbd>趨勢分析</kbd>

##### 語法
> 取得指定月份的天數。  
> **回傳數值=LastDayOfMonth(月份)**  
> 傳入一個參數:  
> - 第一個參數是月份，1為1月、2為2月...依此類推。  

---

##### 說明
傳回指定月份的天數。

例如：一月有31天、二月只有28天、四月有30天。

範例：

```pascal
value1 = LastDayOfMonth(month(date)); //取得當月的天數
```

___


## NDaysAngle
--- 

### NDaysAngle
#### NDaysAngle – （系統函數） <kbd>趨勢分析</kbd>

##### 語法
> 計算股價N期走勢的角度  
> **回傳數值=NDaysAngle(期數)**  

---

##### 說明
計算股價N期走勢的角度。回傳數值。
若為上漲趨勢，則回傳「0 ~ 90」度
若為下跌趨勢，則回傳「0 ~ -90」度

範例：
input:_Length(10,"期數");        //計算10期走勢的角度
plot1(NDaysAngle(_Length),"走勢角度");

___


## NthDayofMonth
--- 

### NthDayofMonth
#### NthDayofMonth – （系統函數） <kbd>趨勢分析</kbd>

##### 語法
> 取得指定日期後第N個星期幾的日期。  
> **回傳數值=NthDayOfMonth(參考日期,第幾個,星期幾)**  
> 傳入三個參數:  
> - 第一個參數是日期，格式為YYYYMMDD的數值。  
> - 第二個參數是第幾個，可以是正數(表示往後找), 也可以是負數(表示往前找)。  
> - 第三個參數是星期幾：0為星期日，1為星期一，2為星期二，3為星期三，4為星期四，5為星期五，6為星期六  

---

##### 說明
NthDayOfMonth回傳的數值是YYYYMMDD的日期格式。

範例：

```pascal
value1 = NthDayOfMonth(date,3,1)); //取得未來第3個星期一的日期
```

___


## UpTrend
--- 

### UpTrend
#### UpTrend – （系統函數） <kbd>趨勢分析</kbd>

##### 語法
> 判斷某個數列是否趨勢向上。  
> **回傳布林值=UpTrend(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，可以是GetField("欄位名稱")。  
> - 第二個參數是期數。  

---

##### 說明
計算序列資料是否趨勢向上。回傳布林值。
若為趨勢向上，則回傳「True」
若不為趨勢向上，則回傳「False」

___


## BollingerBandWidth
--- 

### BollingerBandWidth
#### BollingerBandWidth – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算布林帶寬度指標（Bandwidth，BW）。  
> **回傳數值=BollingerBandWidth(數列,期數,上通道寬度的標準差倍數,下通道寬度的標準差倍數)**  
> 傳入四個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是計算均線的期數。  
> - 第三個參數是決定上通道寬度的標準差倍數。  
> - 第四個參數是決定下通道寬度的標準差倍數。  

---

##### 說明
布林帶寬度指標（Bandwidth，BW），是由布林帶中軌及上、下軌衍生出的指標，利用股價波動範圍以判斷趨勢的強度與轉折；計算公式通常為：布林帶寬度指標值 = （布林帶上軌值 - 布林帶下軌值）÷ 布林帶中軌值。

範例：

```pascal
value1 = BollingerBandWidth(Close,20,2,2);	//計算20期、上下通道寬度的標準差倍數為2
plot1(value1, "BollingerBandWidth");
```

___


## PercentB
--- 

### PercentB
#### PercentB – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算%b指標（Percent b，PB）。  
> **回傳數值=PercentB(數列,期數,上通道寬度的標準差倍數,下通道寬度的標準差倍數)**  
> 傳入四個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是計算均線的期數。  
> - 第三個參數是決定上通道寬度的標準差倍數。  
> - 第四個參數是決定下通道寬度的標準差倍數。  

---

##### 說明
%b指標（Percent b，PB），是從布林值演化過來的，了解%B指標前，建議熟悉布林通道(BollingerBand)；%b指標以數值形式呈現收盤價在布林帶中的位置，計算公式通常為：%b 值 = （收盤價 - 布林帶下軌值） ÷ （布林帶上軌值 - 布林帶下軌值）。

範例：

```pascal
value1 = PercentB(Close,20,2,2);	//計算20期、上下通道寬度的標準差倍數為2
plot1(value1, "%b指標");
```

___


## TurnOverRate
--- 

### TurnOverRate
#### TurnOverRate – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算股票周轉率（或稱換手率）。  
> **回傳數值=TurnOverRate(期數)**  

---

##### 說明
股票周轉率是在一段時間內的股票交易數量與股票發行總數之比。當週轉率高時，代表股票在投資人之間轉換頻率過高，也表示市場的流動性高；週轉率高也可能是因為市場中充斥太多投機者搶短線所造成的。

範例：

```pascal
value1 = TurnOverRate(10);	//計算10期的周轉率
plot1(value1, "周轉率"); 
```

___


## xf_CrossOver
--- 

### xf_CrossOver
#### xf_CrossOver – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 判斷指定頻率的數列一是否由下往上穿越數列二，又稱黃金交叉。  
> **回傳布林值=xf_CrossOver(頻率,數列一,數列二)**  
> 傳入三個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是目標頻率的數列一。  
> - 第三個參數是目標頻率的數列二。  

---

##### 說明
如果出現黃金交叉傳回True，其他狀況傳回False。

範例：

```pascal
condition1 = xf_CrossOver("W",Average(GetField("收盤價","W"),5),Average(GetField("收盤價","W") ,10)); //判斷週線5期均線和10期均線是否黃金交叉
```

___


## xf_CrossUnder
--- 

### xf_CrossUnder
#### xf_CrossUnder – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 判斷指定頻率的數列一是否由上往下穿越數列二，又稱死亡交叉。  
> **回傳布林值=xf_CrossUnder(頻率,數列一,數列二)**  
> 傳入三個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是目標頻率的數列一。  
> - 第三個參數是目標頻率的數列二。  

---

##### 說明
如果出現死亡交叉傳回True，其他狀況傳回False。

範例：

```pascal
condition1 = xf_CrossUnder("W",Average(GetField("close","W"),5),Average(GetField("close","W") ,10) ); //判斷週線5期均線和10期均線是否死亡交叉
```

___


## xf_DirectionMovement
--- 

### xf_DirectionMovement
#### xf_DirectionMovement – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算跨頻率DMI指標。  
> **回傳數值=xf_DirectionMovement(頻率,期數,輸出+DI值,輸出-DI值,輸出ADX值)**  
> 傳入五個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是計算期數。  
> - 第三個參數是輸出計算完的+DI值。  
> - 第四個參數是輸出計算完的-DI值。  
> - 第五個參數是輸出計算完的ADX值。  

---

##### 說明
xf_DirectionMovement是[DirectionMovement](api.aspx?a=DirectionMovement&b=sys) 函數的跨頻率版本，增加了指定頻率的參數，可以計算指定頻率的DMI值。

範例：

```pascal
value1 = xf_DirectionMovement("W",14,value2,value3,value4);       //計算14期的週DMI指標
plot1(value2, "週+DI");
plot2(value3, "週-DI");
plot3(value4, "週ADX");
```

___


## xf_EMA
--- 

### xf_EMA
#### xf_EMA – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算指定頻率的XQ指數移動平均。  
> **回傳數值=xf_EMA(頻率,數列,期數)**  
> 傳入三個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是目標頻率的數列，通常是開高低收的價格數列。  
> - 第三個參數是期數。  

---

##### 說明
xf_EMA是[EMA](api.aspx?a=EMA&b=sys)函數的跨頻率版本，增加了指定頻率的參數，可以計算指定頻率的EMA值。

範例：

```pascal
value1 = xf_EMA("W", Close,5); //計算週線5期收盤價的XQ EMA
```

___


## xf_GetBoolean
--- 

### xf_GetBoolean
#### xf_GetBoolean – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 引用指定頻率的數值。  
> **回傳數值=xf_GetBoolean(頻率,數列,期別)**  
> 傳入三個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是目標頻率的布林數列。  
> - 第三個參數是期別，相對目前而言要往前的筆數。  

---

##### 說明
在同一個頻率時，我們可以直接利用**變數[3]**取得前3期的變數值。當資料頻率不同時（跨頻率），我們就需要使用xf_GetValue或xf_GetBoolean來取得之前的變數值。若變數是數值時，要用xf_GetValue；若變數是布林值時，要用xf_GetBoolean。

```pascal
input:Length_W(9,"跨頻率週期數");
variable:rsv_w(0),kk_w(0),dd_w(0);
xf_stochastic("W", Length_W, 3, 3, rsv_w, kk_w, dd_w);
condition1 = xf_GetBoolean("W",xf_crossover("W", kk_w, dd_w),1);	//在日線抓周KD黃金交叉
```

相關函數：[xf_GetValue](api.aspx?a=xf_GetValue&b=sys)。

___


## xf_GetCurrentBar
--- 

### xf_GetCurrentBar
#### xf_GetCurrentBar – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 傳回指定頻率的K棒編號。  
> **K棒編號 =  xf_GetCurrentBar(頻率)**  
> 傳入一個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"D", "W", "M", "AD", "AW", "AM"。  

---

##### 說明
傳回指定頻率的K棒序列編號，由1開始，第一筆K棒編號為1，第二筆K棒編號為2，依序遞增。

可以使用這個函數來判斷目前腳本執行的時機點

```pascal
value1 = xf_GetCurrentBar(FreqType);

if Length + 1 = 0 then Factor = 1 else Factor = 2 / (Length + 1);

if value1 = 1 then
    xf_XAverage = Series
else
    xf_XAverage = lastXAverage + Factor * (Series - lastXAverage);
```

上述範例利用xf_GetCurrentBar來判斷目前是否是第一筆K棒。如果是的話則回傳xf_XAverage的初始數值。

___


## xf_GetDTValue
--- 

### xf_GetDTValue
#### xf_GetDTValue – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算指定頻率的序列值。  
> **回傳數值=xf_GetDTValue(頻率,日期)**  
> 傳入二個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是日期。  

---

##### 說明
經由傳入的日期判斷指定頻率的期別是否有異動

```pascal
value1 = xf_getdtvalue("W",date);
if value1 <> value1[1] then plot1(1) else plot1(0);
```

上述範例利用xf_GetDTValue來判斷目前是否為新的一週。如果是的話則在圖表上顯示為1。

___


## xf_GetValue
--- 

### xf_GetValue
#### xf_GetValue – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 引用指定頻率的數值。  
> **回傳數值=xf_GetValue(頻率,數列,期別)**  
> 傳入三個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是目標頻率的數列。  
> - 第三個參數是期別，相對目前而言要往前的筆數。  

---

##### 說明
在同一個頻率時，我們可以直接利用**變數[3]**取得前3期的變數值。當資料頻率不同時（跨頻率），我們就需要使用xf_GetValue或xf_GetBoolean來取得之前的變數值。若變數是數值時，要用xf_GetValue；若變數是布林值時，要用xf_GetBoolean。

```pascal
value1 = xf_WeightedClose("W");            //計算週線的加權平均價
value2 = xf_GetValue("W",value1,1);        //取得上一週的加權平均價
plot1(value2);
plot2(value1[1]);                        //可以比較一下和value2的差異
```

相關函數：[xf_GetBoolean](api.aspx?a=xf_GetBoolean&b=sys)。

___


## xf_MACD
--- 

### xf_MACD
#### xf_MACD – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算指定頻率的MACD指標值。  
> **回傳數值=xf_MACD(頻率,數列,短期數,長期數,MACD平滑期數,輸出DIF值,輸出MACD值,輸出OSC值)**  
> 傳入八個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是目標頻率的數列，MACD通常是以加權平均收盤價（WeightedClose）來計算。  
> - 第三個參數是計算快速線（短期）的期數。  
> - 第四個參數是計算慢速線（長期）的期數。  
> - 第五個參數是計算MACD使用之平滑期數。  
> - 第六個參數是輸出計算完的DIF值。  
> - 第七個參數是輸出計算完的MACD值。  
> - 第八個參數是輸出計算完的OSC值。  

---

##### 說明
xf_MACD是[MACD](api.aspx?a=MACD&b=sys) 函數的跨頻率版本，增加了指定頻率的參數，可以計算指定頻率的MACD值。

範例：

```pascal
value1 = xf_MACD("W",xf_weightedclose("W"),12,26,9,value2,value3,value4);       //計算週線MACD
plot1(value2, "週DIF");
plot2(value3, "週MACD");
plot3(value4, "週OSC");   
```

___


## xf_PercentR
--- 

### xf_PercentR
#### xf_PercentR – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算指定頻率的威廉指標值。  
> **回傳數值=xf_PercentR(頻率,期數)**  
> 傳入二個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是計算威廉指標的期數。  

---

##### 說明
xf_PercentR是[PercentR](api.aspx?a=PercentR&b=sys) 函數的跨頻率版本，增加了指定頻率的參數，可以計算指定頻率的PercentR值。

範例：

```pascal
value1 = xf_PercentR("W", 14) - 100;       //計算週線威廉指標
Plot1(value1, "週威廉指標");
```

___


## xf_RSI
--- 

### xf_RSI
#### xf_RSI – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算指定頻率的相對強弱指標數值。  
> **回傳數值=xf_RSI(頻率,數列,期數)**  
> 傳入三個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是目標頻率的數列，通常是開高低收的價格數列。  
> - 第三個參數是期數。  

---

##### 說明
xf_RSI是[RSI](api.aspx?a=RSI&b=sys) 函數的跨頻率版本，增加了指定頻率的參數，可以計算指定頻率的RSI值。

範例：

```pascal
value1 = xf_RSI("W",GetField("Close","W"),6);       //計算6期的週RSI指標
plot1(value1, "週RSI");   
```

___


## xf_Stochastic
--- 

### xf_Stochastic
#### xf_Stochastic – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算指定頻率的KD指標。  
> **回傳數值=xf_Stochastic(頻率,資料期數,K值平滑期數,D值平滑期數,輸出RSV值,輸出K值,輸出D值)**  
> 傳入八個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是資料期數，指定計算的區間長度。  
> - 第三個參數是K值平滑期數，指定計算K值所用的平滑期數。  
> - 第四個參數是D值平滑期數，指定計算D值所用的平滑期數。  
> **- 第五個參數是輸出RSV值，回傳計算完的RSV值。**  
> **- 第六個參數是輸出K值，回傳計算完的K值。**  
> **- 第七個參數是輸出D值，回傳計算完的D值。**  

---

##### 說明
xf_Stochastic是[Stochastic](api.aspx?a=Stochastic&b=sys) 函數的跨頻率版本，增加了指定頻率的參數，可以計算指定頻率的Stochastic值。

範例：

```pascal
value1 = xf_Stochastic("W",9,3,3,value2,value3,value4);       //計算週KD指標
plot1(value3, "週K");
plot2(value4, "週D");     
```

___


## xf_WeightedClose
--- 

### xf_WeightedClose
#### xf_WeightedClose – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算指定頻率的加權平均收盤價。  
> **回傳數值=xf_WeightedClose(頻率)**  
> 傳入一個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"D", "W", "M", "AD", "AW", "AM"。  

---

##### 說明
xf_WeightedClose是[WeightedClose](api.aspx?a=WeightedClose&b=sys) 函數的跨頻率版本，增加了指定頻率的參數，可以計算指定頻率的WeightedClose值。

範例：

```pascal
plot1(xf_WeightedClose("W"));    //繪製週線加權平均收盤價的連線
```

___


## xf_XAverage
--- 

### xf_XAverage
#### xf_XAverage – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算指定頻率的指數移動平均。  
> **回傳數值=xf_XAverage(頻率,數列,期數)**  
> 傳入三個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是目標頻率的數列，通常是開高低收的價格數列。  
> - 第三個參數是期數。  

---

##### 說明
xf_XAverage是[XAverage](api.aspx?a=XAverage&b=sys) 函數的跨頻率版本，增加了指定頻率的參數，可以計算指定頻率的XAverage值。

範例：

```pascal
value1 = xf_XAverage("W",GetField("Close","W"),5); //計算週線5期收盤價的指數移動平均
```

___


## xfMin_CrossOver
--- 

### xfMin_CrossOver
#### xfMin_CrossOver – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 判斷指定頻率的數列一是否由下往上穿越數列二，又稱黃金交叉。  
> **回傳布林值=xfMin_CrossOver(頻率,數列一,數列二)**  
> 傳入三個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"1","5","10","15","30","60","D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是目標頻率的數列一。  
> - 第三個參數是目標頻率的數列二。  
> 備註：商品類型僅支援台股與台期權。不支援XS選股、XS選股自訂排行與XS選股回測。  

---

##### 說明
如果出現黃金交叉傳回True，其他狀況傳回False。

範例：

```pascal
condition1 = xfMin_CrossOver("30",Average(GetField("收盤價","30"),5),Average(GetField("收盤價","30") ,10)); //判斷30分鐘線5期均線和10期均線是否黃金交叉
```

___


## xfMin_CrossUnder
--- 

### xfMin_CrossUnder
#### xfMin_CrossUnder – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 判斷指定頻率的數列一是否由上往下穿越數列二，又稱死亡交叉。  
> **回傳布林值=xfMin_CrossUnder(頻率,數列一,數列二)**  
> 傳入三個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"1","5","10","15","30","60","D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是目標頻率的數列一。  
> - 第三個參數是目標頻率的數列二。  
> 備註：商品類型僅支援台股與台期權。不支援XS選股、XS選股自訂排行與XS選股回測。  

---

##### 說明
如果出現死亡交叉傳回True，其他狀況傳回False。

範例：

```pascal
condition1 = xfMin_CrossUnder("30",Average(GetField("close","30"),5),Average(GetField("close","30") ,10) ); //判斷30分鐘線5期均線和10期均線是否死亡交叉
```

___


## xfMin_DirectionMovement
--- 

### xfMin_DirectionMovement
#### xfMin_DirectionMovement – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算跨頻率DMI指標。  
> **回傳數值=xfMin_DirectionMovement(頻率,期數,輸出+DI值,輸出-DI值,輸出ADX值)**  
> 傳入五個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"1","5","10","15","30","60","D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是計算期數。  
> - 第三個參數是輸出計算完的+DI值。  
> - 第四個參數是輸出計算完的-DI值。  
> - 第五個參數是輸出計算完的ADX值。  
> 備註：商品類型僅支援台股與台期權。不支援XS選股、XS選股自訂排行與XS選股回測。  

---

##### 說明
xfMin_DirectionMovement是[xf_DirectionMovement](api.aspx?a=xf_DirectionMovement&b=sys) 函數的跨頻率加強版本，增加了指定分鐘頻率的參數，可以計算指定分鐘頻率的DMI值。

範例：

```pascal
value1 = xfMin_DirectionMovement("30",14,value2,value3,value4);       //計算14期的30分鐘線DMI指標
plot1(value2, "30分+DI");
plot2(value3, "30分週-DI");
plot3(value4, "30分ADX");
```

___


## xfMin_EMA
--- 

### xfMin_EMA
#### xfMin_EMA – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算指定頻率的XQ指數移動平均。  
> **回傳數值=xfMin_EMA(頻率,數列,期數)**  
> 傳入三個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"1","5","10","15","30","60","D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是目標頻率的數列，通常是開高低收的價格數列。  
> - 第三個參數是期數。  
> 備註：商品類型僅支援台股與台期權。不支援XS選股、XS選股自訂排行與XS選股回測。  

---

##### 說明
xfMin_EMA是[xf_EMA](api.aspx?a=xf_EMA&b=sys)函數的跨頻率加強版本，增加了指定分鐘頻率的參數，可以計算指定分鐘頻率的EMA值。

範例：

```pascal
value1 = xfMin_EMA("30", GetField("Close", "30"),5); //計算30分鐘線5期收盤價的XQ EMA
```

___


## xfMin_GetBoolean
--- 

### xfMin_GetBoolean
#### xfMin_GetBoolean – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 引用指定頻率的數值。  
> **回傳數值=xfMin_GetBoolean(頻率,數列,期別)**  
> 傳入三個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"1","5","10","15","30","60","D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是布林數列。  
> - 第三個參數是期別，相對目前而言要往前的筆數。  
> 備註：商品類型僅支援台股與台期權。不支援XS選股、XS選股自訂排行與XS選股回測。  

---

##### 說明
在同一個頻率時，我們可以直接利用**變數[3]**取得前3期的變數值。當資料頻率不同時（跨頻率），我們就需要使用xfMin_GetValue或xfMin_GetBoolean來取得之前的變數值。若變數是數值時，要用xfMin_GetValue；若變數是布林值時，要用xfMin_GetBoolean。支援跨分鐘頻率。

```pascal
input:Length_Min(9,"跨分鐘頻率期數");
variable:rsv_w(0),kk_w(0),dd_w(0);
xfMin_stochastic("30", Length_Min, 3, 3, rsv_w, kk_w, dd_w);
condition1 = xfMin_GetBoolean("30",xfMin_crossover("30", kk_w, dd_w),1);	//在15分鐘線抓30分鐘線KD黃金交叉
```

相關函數：[xfMin_GetValue](api.aspx?a=xfMin_GetValue&b=sys)。

___


## xfMin_GetCurrentBar
--- 

### xfMin_GetCurrentBar
#### xfMin_GetCurrentBar – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 傳回指定頻率的K棒編號。  
> **K棒編號 = xfMin_GetCurrentBar(頻率)**  
> 傳入一個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"1","5","10","15","30","60","D", "W", "M", "AD", "AW", "AM"。  
> 備註：商品類型僅支援台股與台期權。不支援XS選股、XS選股自訂排行與XS選股回測。  

---

##### 說明
傳回指定頻率（支援分鐘）的K棒序列編號，由1開始，第一筆K棒編號為1，第二筆K棒編號為2，依序遞增。

可以使用這個函數來判斷目前腳本執行的時機點

```pascal
value1 = xfMin_GetCurrentBar(FreqType);

if Length + 1 = 0 then Factor = 1 else Factor = 2 / (Length + 1);

if value1 = 1 then
    xfMin_XAverage = Series
else
    xfMin_XAverage = lastXAverage + Factor * (Series - lastXAverage);
```

上述範例利用xfMin_GetCurrentBar來判斷目前是否是第一筆K棒。如果是的話則回傳xfMin_XAverage的初始數值。

___


## xfMin_GetDTValue
--- 

### xfMin_GetDTValue
#### xfMin_GetDTValue – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算指定頻率的序列值。  
> **回傳數值=xfMin_GetDTValue(頻率,日期)**  
> 傳入二個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"1","5","10","15","30","60","D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是日期。  
> 備註：商品類型僅支援台股與台期權。不支援XS選股、XS選股自訂排行與XS選股回測。  

---

##### 說明
經由傳入的日期判斷指定頻率的期別是否有異動，支援指定分鐘頻率。

```pascal
value1 = xfMin_getdtvalue("30",date);
if value1 <> value1[1] then plot1(1) else plot1(0);
```

上述範例利用xfMin_GetDTValue來判斷目前是否為新的30分鐘。如果是的話則在圖表上顯示為1。

___


## xfMin_GetValue
--- 

### xfMin_GetValue
#### xfMin_GetValue – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 引用指定頻率的數值。  
> **回傳數值=xfMin_GetValue(頻率,數列,期別)**  
> 傳入三個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"1","5","10","15","30","60","D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是目標頻率的數列。  
> - 第三個參數是期別，相對目前而言要往前的筆數。  
> 備註：商品類型僅支援台股與台期權。不支援XS選股、XS選股自訂排行與XS選股回測。  

---

##### 說明
在同一個頻率時，我們可以直接利用**變數[3]**取得前3期的變數值。當資料頻率不同時（跨頻率），我們就需要使用xfMin_GetValue或xfMin_GetBoolean來取得之前的變數值。若變數是數值時，要用xfMin_GetValue；若變數是布林值時，要用xfMin_GetBoolean。支援跨分鐘頻率。

```pascal
value1 = xfMin_WeightedClose("30");            //計算30分鐘線的加權平均價
value2 = xfMin_GetValue("30",value1,1);        //取得上一期30分鐘線的加權平均價
plot1(value2);
plot2(value1[1]);                        //可以比較一下和value2的差異
```

相關函數：[xfMin_GetBoolean](api.aspx?a=xfMin_GetBoolean&b=sys)。

___


## xfMin_MACD
--- 

### xfMin_MACD
#### xfMin_MACD – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算指定頻率的MACD指標值。  
> **回傳數值=xfMin_MACD(頻率,數列,短期數,長期數,MACD平滑期數,輸出DIF值,輸出MACD值,輸出OSC值)**  
> 傳入八個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"1","5","10","15","30","60","D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是目標頻率的數列，MACD通常是以加權平均收盤價（WeightedClose）來計算。  
> - 第三個參數是計算快速線（短期）的期數。  
> - 第四個參數是計算慢速線（長期）的期數。  
> - 第五個參數是計算MACD使用之平滑期數。  
> - 第六個參數是輸出計算完的DIF值。  
> - 第七個參數是輸出計算完的MACD值。  
> - 第八個參數是輸出計算完的OSC值。  
> 備註：商品類型僅支援台股與台期權。不支援XS選股、XS選股自訂排行與XS選股回測。  

---

##### 說明
xfMin_MACD是[xf_MACD](api.aspx?a=xf_MACD&b=sys) 函數的跨頻率加強版本，增加了指定分鐘頻率的參數，可以計算指定分鐘頻率的MACD值。

範例：

```pascal
value1 = xfMin_MACD("30",xfMin_weightedclose("30"),12,26,9,value2,value3,value4);    //計算30分鐘線MACD
plot1(value2, "30分鐘DIF");
plot2(value3, "30分鐘MACD");
plot3(value4, "30分鐘OSC");   
```

___


## xfmin_MTM
--- 

### xfmin_MTM
#### xfmin_MTM – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算指定頻率的威廉指標值。  
> **回傳數值=xfMin_MTM(頻率,期數)**  
> 傳入二個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"1","5","10","15","30","60","D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是計算MTM指標的期數。  
> 備註：商品類型僅支援台股與台期權。不支援XS選股、XS選股自訂排行與XS選股回測。  

---

##### 說明
xfMin_MTM是[MTM](api.aspx?a=MTM&b=sys) 函數的跨頻率版本，增加了指定頻率的參數，可以計算指定頻率的MTM值。

範例：

```pascal
value1 = xfMin_MTM("5", 10);       //value1 = 五分鐘MTM
Plot1(value1, "5分鐘MTM");
```

___


## xfMin_PercentR
--- 

### xfMin_PercentR
#### xfMin_PercentR – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算指定頻率的威廉指標值。  
> **回傳數值=xfMin_PercentR(頻率,期數)**  
> 傳入二個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"1","5","10","15","30","60","D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是計算威廉指標的期數。  
> 備註：商品類型僅支援台股與台期權。不支援XS選股、XS選股自訂排行與XS選股回測。  

---

##### 說明
xfMin_PercentR是[xf_PercentR](api.aspx?a=xf_PercentR&b=sys) 函數的跨頻率加強版本，增加了指定分鐘頻率的參數，可以計算指定分鐘頻率的PercentR值。

範例：

```pascal
value1 = xfMin_PercentR("30", 14) - 100;       //計算30分鐘線威廉指標
Plot1(value1, "30分鐘威廉指標");
```

___


## xfMin_RSI
--- 

### xfMin_RSI
#### xfMin_RSI – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算指定頻率的相對強弱指標數值。  
> **回傳數值=xfMin_RSI(頻率,數列,期數)**  
> 傳入三個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"1","5","10","15","30","60","D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是目標頻率的數列，通常是開高低收的價格數列。  
> - 第三個參數是期數。  
> 備註：商品類型僅支援台股與台期權。不支援XS選股、XS選股自訂排行與XS選股回測。  

---

##### 說明
xfMin_RSI是[xf_RSI](api.aspx?a=xf_RSI&b=sys) 函數的跨頻率加強版本，增加了指定分鐘頻率的參數，可以計算指定分鐘頻率的RSI值。

範例：

```pascal
value1 = xfMin_RSI("30",GetField("Close","30"),6);       //計算6期的30分鐘線RSI指標
plot1(value1, "30分RSI");   
```

___


## xfMin_Stochastic
--- 

### xfMin_Stochastic
#### xfMin_Stochastic – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算指定頻率的KD指標。  
> **回傳數值=xfMin_Stochastic(頻率,資料期數,K值平滑期數,D值平滑期數,輸出RSV值,輸出K值,輸出D值)**  
> 傳入八個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"1","5","10","15","30","60","D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是資料期數，指定計算的區間長度。  
> - 第三個參數是K值平滑期數，指定計算K值所用的平滑期數。  
> - 第四個參數是D值平滑期數，指定計算D值所用的平滑期數。  
> **- 第五個參數是輸出RSV值，回傳計算完的RSV值。**  
> **- 第六個參數是輸出K值，回傳計算完的K值。**  
> **- 第七個參數是輸出D值，回傳計算完的D值。**  
> 備註：商品類型僅支援台股與台期權。不支援XS選股、XS選股自訂排行與XS選股回測。  

---

##### 說明
xfMin_Stochastic是[xf_Stochastic](api.aspx?a=xf_Stochastic&b=sys) 函數的跨頻率加強版本，增加了指定分鐘頻率的參數，可以計算指定分鐘頻率的Stochastic值。

範例：

```pascal
value1 = xfMin_Stochastic("30",9,3,3,value2,value3,value4);       //計算30分鐘線KD指標
plot1(value3, "30分K");
plot2(value4, "30分D");     
```

___


## xfMin_WeightedClose
--- 

### xfMin_WeightedClose
#### xfMin_WeightedClose – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算指定頻率的加權平均收盤價。  
> **回傳數值=xfMin_WeightedClose(頻率)**  
> 傳入一個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"1","5","10","15","30","60","D", "W", "M", "AD", "AW", "AM"。  
> 備註：商品類型僅支援台股與台期權。不支援XS選股、XS選股自訂排行與XS選股回測。  

---

##### 說明
xfMin_WeightedClose是[xf_WeightedClose](api.aspx?a=xf_WeightedClose&b=sys) 函數的跨頻率加強版本，增加了指定分鐘頻率的參數，可以計算指定分鐘頻率的WeightedClose值。

範例：

```pascal
plot1(xfMin_WeightedClose("30"));    //繪製30分鐘線加權平均收盤價的連線
```

___


## xfMin_XAverage
--- 

### xfMin_XAverage
#### xfMin_XAverage – （系統函數） <kbd>跨頻率</kbd>

##### 語法
> 計算指定頻率的指數移動平均。  
> **回傳數值=xfMin_Xaverage(頻率,數列,期數)**  
> 傳入三個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"1","5","10","15","30","60","D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是目標頻率的數列，通常是開高低收的價格數列。  
> - 第三個參數是期數。  
> 備註：商品類型僅支援台股與台期權。不支援XS選股、XS選股自訂排行與XS選股回測。  

---

##### 說明
xfMin_XAverage是[xf_XAverage](api.aspx?a=xf_XAverage&b=sys) 函數的跨頻率加強版本，增加了指定分鐘頻率的參數，可以計算指定分鐘頻率的XAverage值。

範例：

```pascal
value1 = xfMin_XAverage("30",GetField("Close","30"),5); //計算30分鐘線5期收盤價的指數移動平均
```

___


## blackscholesmodel
--- 

### blackscholesmodel
#### blackscholesmodel – （系統函數） <kbd>邏輯判斷</kbd>

##### 語法
> 利用BlackScholes選擇權評價模型計算理論價及Greeks  
> **回傳數值=BlackScholesModel (買賣權,標的價格,履約價,到期天數,無風險利率,持有成本,波動率,輸出理論價,輸出Delta,輸出Gamma,輸出Vega,輸出Theta,輸出Rho)**  
> 傳入十三個參數:  
> - 第一個參數是買賣權，C表買權、P表賣權。  
> - 第二個參數是標的價格。  
> - 第三個參數是履約價。  
> - 第四個參數是到期天數。  
> - 第五個參數是無風險利率，百分比值。若無風險利率為2%，請輸入2。  
> - 第六個參數是持有成本，百分比值。若持有成本為1%，請輸入1。  
> - 第七個參數是波動率，百分比值。若持有成本為30%，請輸入30。  
> **- 第八個參數為傳址參數，會回傳計算完的選擇權理論價。**  
> **- 第九個參數為傳址參數，會回傳計算完的選擇權Delta。**  
> **- 第十個參數為傳址參數，會回傳計算完的選擇權Gamma。**  
> **- 第十一個參數為傳址參數，會回傳計算完的選擇權Vega。**  
> **- 第十二個參數為傳址參數，會回傳計算完的選擇權Theta。**  
> **- 第十三個參數為傳址參數，會回傳計算完的選擇權Rho。**  

---

##### 說明
BS選擇權定價模型為諾貝爾經濟學獎得主Robert Merton和Myron Scholes於1973所發表。依據下列六個參數決定選擇權的理論價：標的價格、履約價、到期天數、無風險利率、持有成本、波動率。其中只有履約價和到期天數是由合約所規定，其餘參數皆會隨市場狀況而變動。


持有成本會因標的商品的不同而異：
- 股票選擇權的持有成本為無風險利率（r）-股票殖利率
- 期貨選擇權的持有成本為0
- 外匯選擇權的持有成本為無風險利率（r）-外國無風險利率


這個函數可以依照使用者傳入的參數，計算選擇權的理論價、Delta、Gamma、Vega、Theta及Rho。


範例：

```pascal
value1 = BlackScholesModel("C",8800,9000,20,2,0,25,value2,value3,value4,value5,value6,value7);       //計算波動率25%、20天後到期之台指選擇權9000的Call在指數為8800點的理論價
plot1(value2, "理論價");   
plot2(value3, "Delta");   
plot3(value4, "Gamma");   
plot4(value5, "Vega");   
plot5(value6, "Theta");   
plot6(value7, "Rho");   
```

___


## BSDelta
--- 

### BSDelta
#### BSDelta – （系統函數） <kbd>邏輯判斷</kbd>

##### 語法
> 以BlackScholes模型計算選擇權Delta  
> **回傳數值=BSDelta(買賣權,標的價格,履約價,到期天數,無風險利率,持有成本,波動率)**  
> 傳入七個參數:  
> - 第一個參數是買賣權，C表買權、P表賣權。  
> - 第二個參數是標的價格。  
> - 第三個參數是履約價。  
> - 第四個參數是到期天數。  
> - 第五個參數是無風險利率，百分比值。若無風險利率為2%，請輸入2。  
> - 第六個參數是持有成本，百分比值。若持有成本為1%，請輸入1。  
> - 第七個參數是波動率，百分比值。若持有成本為30%，請輸入30。  

---

##### 說明
BS選擇權定價模型為諾貝爾經濟學獎得主Robert Merton和Myron Scholes於1973所發表。依據下列六個參數決定選擇權的理論價：標的價格、履約價、到期天數、無風險利率、持有成本、波動率。其中只有履約價和到期天數是由合約所規定，其餘參數皆會隨市場狀況而變動。

範例：

```pascal
value1 = BSDelta("C",8800,9000,20,2,0,25);       //計算波動率25%、20天後到期之台指選擇權9000的Call在指數為8800點的Delta值
plot1(value1, "Delta"); 
```

註：更多參數說明請參考[BlackScholes公式](api.aspx?a=BlackScholesModel&b=sys)。

___


## BSGamma
--- 

### BSGamma
#### BSGamma – （系統函數） <kbd>邏輯判斷</kbd>

##### 語法
> 以BlackScholes模型計算選擇權Gamma  
> **回傳數值=BSGamma(買賣權,標的價格,履約價,到期天數,無風險利率,持有成本,波動率)**  
> 傳入七個參數:  
> - 第一個參數是買賣權，C表買權、P表賣權。  
> - 第二個參數是標的價格。  
> - 第三個參數是履約價。  
> - 第四個參數是到期天數。  
> - 第五個參數是無風險利率，百分比值。若無風險利率為2%，請輸入2。  
> - 第六個參數是持有成本，百分比值。若持有成本為1%，請輸入1。  
> - 第七個參數是波動率，百分比值。若持有成本為30%，請輸入30。  

---

##### 說明
Gamma為選擇權敏感度分析的參數之一，用來衡量Delta相對於標的價格變動的敏感度。


函數回傳值為標的價格每變動1％，選擇權Delta變化的百分比。Gamma永遠為正值，選擇權在價平時Gamma值最大。例如，假設選擇權的Delta為0.56、Gamma為0.0015，則表示只要標的價格上漲1點，Delta會由0.56增加至0.5615（0.56+1*0.0015=0.5615）


範例：

```pascal
value1 = BSGamma("C",8800,9000,20,2,0,25);       //計算波動率25%、20天後到期之台指選擇權9000的Call在指數為8800點的Gamma值
plot1(value1, "Gamma");   
```

註：更多參數說明請參考[BlackScholes公式](api.aspx?a=BlackScholesModel&b=sys)。

___


## BSPrice
--- 

### BSPrice
#### BSPrice – （系統函數） <kbd>邏輯判斷</kbd>

##### 語法
> 以BlackScholes模型計算選擇權理論價  
> **回傳數值=BSPrice(買賣權,標的價格,履約價,到期天數,無風險利率,持有成本,波動率)**  
> 傳入七個參數:  
> - 第一個參數是買賣權，C表買權、P表賣權。  
> - 第二個參數是標的價格。  
> - 第三個參數是履約價。  
> - 第四個參數是到期天數。  
> - 第五個參數是無風險利率，百分比值。若無風險利率為2%，請輸入2。  
> - 第六個參數是持有成本，百分比值。若持有成本為1%，請輸入1。  
> - 第七個參數是波動率，百分比值。若持有成本為30%，請輸入30。  

---

##### 說明
BS選擇權定價模型為諾貝爾經濟學獎得主Robert Merton和Myron Scholes於1973所發表。依據下列六個參數決定選擇權的理論價：標的價格、履約價、到期天數、無風險利率、持有成本、波動率。其中只有履約價和到期天數是由合約所規定，其餘參數皆會隨市場狀況而變動。

範例：

```pascal
value1 = BSPrice("C",8800,9000,20,2,0,25);       //計算波動率25%、20天後到期之台指選擇權9000的Call在指數為8800點的理論價
plot1(value1, "理論價");   
```

註：更多參數說明請參考[BlackScholes公式](api.aspx?a=BlackScholesModel&b=sys)。

___


## BSTheta
--- 

### BSTheta
#### BSTheta – （系統函數） <kbd>邏輯判斷</kbd>

##### 語法
> 以BlackScholes模型計算選擇權Theta  
> **回傳數值=BSTheta(買賣權,標的價格,履約價,到期天數,無風險利率,持有成本,波動率)**  
> 傳入七個參數:  
> - 第一個參數是買賣權，C表買權、P表賣權。  
> - 第二個參數是標的價格。  
> - 第三個參數是履約價。  
> - 第四個參數是到期天數。  
> - 第五個參數是無風險利率，百分比值。若無風險利率為2%，請輸入2。  
> - 第六個參數是持有成本，百分比值。若持有成本為1%，請輸入1。  
> - 第七個參數是波動率，百分比值。若持有成本為30%，請輸入30。  

---

##### 說明
Theta為選擇權敏感度分析的參數之一，用來衡量時間變化對選擇權價格的影響。


函數回傳值為選擇權剩餘天數每減少一天，選擇權理論價的變化。Theta永遠為負值，表示選擇權的時間價值隨著到期日的接近而消失。如果選擇權的Theta為-2，在所有條件維持不變的情況下，明日選擇權的理論價會由今天的70下降為68（70-1*2=68）。


範例：

```pascal
value1 = BSTheta("C",8800,9000,20,2,0,25);       //計算波動率25%、20天後到期之台指選擇權9000的Call在指數為8800點的Theta值
plot1(value1, "Theta");   
```

註：更多參數說明請參考[BlackScholes公式](api.aspx?a=BlackScholesModel&b=sys)。

___


## BSVega
--- 

### BSVega
#### BSVega – （系統函數） <kbd>邏輯判斷</kbd>

##### 語法
> 以BlackScholes模型計算選擇權Vega  
> **回傳數值=BSVega(買賣權,標的價格,履約價,到期天數,無風險利率,持有成本,波動率)**  
> 傳入七個參數:  
> - 第一個參數是買賣權，C表買權、P表賣權。  
> - 第二個參數是標的價格。  
> - 第三個參數是履約價。  
> - 第四個參數是到期天數。  
> - 第五個參數是無風險利率，百分比值。若無風險利率為2%，請輸入2。  
> - 第六個參數是持有成本，百分比值。若持有成本為1%，請輸入1。  
> - 第七個參數是波動率，百分比值。若持有成本為30%，請輸入30。  

---

##### 說明
BS選擇權定價模型為諾貝爾經濟學獎得主Robert Merton和Myron Scholes於1973所發表。依據下列六個參數決定選擇權的理論價：標的價格、履約價、到期天數、無風險利率、持有成本、波動率。其中只有履約價和到期天數是由合約所規定，其餘參數皆會隨市場狀況而變動。

範例：

```pascal
value1 = BSPrice("C",8800,9000,20,2,0,25);       //計算波動率25%、20天後到期之台指選擇權9000的Call在指數為8800點的理論價
plot1(value1, "理論價");   
```

註：更多參數說明請參考[BlackScholes公式](api.aspx?a=BlackScholesModel&b=sys)。

___


## DaysToExpirationTF
--- 

### DaysToExpirationTF
#### DaysToExpirationTF – （系統函數） <kbd>邏輯判斷</kbd>

##### 語法
> 自動計算台股指數類期貨、選擇權商品的到期天數。  
> **回傳數值=DaysToExpirationTF**  

---

##### 說明
自動依目前執行的商品計算對應的到期天數。支援週選擇權。


回傳值為1，表示當天為結算日。回傳值小於1，表示該合約已到期。


範例：

```pascal
value1 = DaysToExpirationTF;
plot1(value1); //繪製最新的台股指數類期貨到期天數的連線
```

注意，此函數並無調整因放假而導致的到期日異動。

___


## HVolatility
--- 

### HVolatility
#### HVolatility – （系統函數） <kbd>邏輯判斷</kbd>

##### 語法
> 計算序列資料的波動率。  
> **回傳數值=HVolatility(數列,期數)**  
> 傳入二個參數:  
> - 第一個參數是數列，通常是開高低收的價格數列。  
> - 第二個參數是期數。  

---

##### 說明
歷史波動率代表的是價格過往的波動性高低。波動率是影響選擇權價格的重要因子，而歷史波動率會是一個很好的參考。


範例：

```pascal
value1 = HVolatility(Close,20);       //計算20天的歷史波動率
plot1(value1,"20天歷史波動率");   
```

___


## IsXLOrder
--- 

### IsXLOrder
#### IsXLOrder – （系統函數） <kbd>邏輯判斷</kbd>

##### 語法
> 判斷成交金額是否是特大單。  
> **回傳布林值=IsXLOrder**  

---

##### 說明
級距表請參考：
[台股逐筆功能行情端相關異動](https://www.xq.com.tw/%e5%8f%b0%e8%82%a1%e9%80%90%e7%ad%86%e5%8a%9f%e8%83%bd%e8%a1%8c%e6%83%85%e7%ab%af%e7%9b%b8%e9%97%9c%e7%95%b0%e5%8b%95/)

___


## IsXOrder
--- 

### IsXOrder
#### IsXOrder – （系統函數） <kbd>邏輯判斷</kbd>

##### 語法
> **回傳目前的成交金額是否是大單(大單+特大單)。**  
> **回傳布林值=IsXOrder**  

---

##### 說明
級距表請參考：
[台股逐筆功能行情端相關異動](https://www.xq.com.tw/%e5%8f%b0%e8%82%a1%e9%80%90%e7%ad%86%e5%8a%9f%e8%83%bd%e8%a1%8c%e6%83%85%e7%ab%af%e7%9b%b8%e9%97%9c%e7%95%b0%e5%8b%95/)

___


## IVolatility
--- 

### IVolatility
#### IVolatility – （系統函數） <kbd>邏輯判斷</kbd>

##### 語法
> 計算選擇權的隱含波動率  
> **回傳數值=IVolatility(買賣權,標的價格,履約價,到期天數,無風險利率,持有成本,選擇權現價)**  
> 傳入七個參數:  
> - 第一個參數是買賣權，C表買權、P表賣權。  
> - 第二個參數是標的價格。  
> - 第三個參數是履約價。  
> - 第四個參數是到期天數。  
> - 第五個參數是無風險利率，百分比值。若無風險利率為2%，請輸入2。  
> - 第六個參數是持有成本，百分比值。若持有成本為1%，請輸入1。  
> - 第七個參數是選擇權現價。  

---

##### 說明
隱含波動率是經由選擇權市場價格反推而得的波動率。隱含波動率的水準顯示了選擇權價格的高低（貴或便宜），也代表了市場參與者對未來的預期。通常會搭配歷史波動率來判斷市場是否出現狂熱或恐慌的狀況。


範例：

```pascal
value1 = IVolatility("C",8800,9000,20,2,0,40);       //計算8800買權的隱含波動率
plot1(value1,"隱含波動率");   
```

___


## NORMSDIST
--- 

### NORMSDIST
#### NORMSDIST – （系統函數） <kbd>邏輯判斷</kbd>

##### 語法
> 計算數值的標準常態累加分配函數。  
> **回傳數值=NORMSDIST(數值)**  
> 傳入一個參數:  
> - 第一個參數是數值。  

---

##### 說明
計算在平均值為0、標準差為1的標準常態分配下，數值小於傳入值的累計機率。


本函數利用多項式計算近似值，精確度到小數點以下六位。


範例：

```pascal
value1 = NORMSDIST(1.33);       //1.33的標準常態累加分配函數
plot1(value1);   
```

___


## DiffBidAskVolumeLxL
--- 

### DiffBidAskVolumeLxL
#### DiffBidAskVolumeLxL – （系統函數） <kbd>量能相關</kbd>

##### 語法
> 傳回「近15分鐘大戶買賣超」的數值  
> **回傳數值 = DiffBidAskVolumeLxL**  
> 僅支援1分鐘頻率與台股商品。  

---

##### 說明
DiffBidAskVolumeLxL為近15分鐘大戶買賣超的函數，
該函數運算出來的數值，與XS指標的「流動大戶買賣力」指標相同。

___


## DiffBidAskVolumeXL
--- 

### DiffBidAskVolumeXL
#### DiffBidAskVolumeXL – （系統函數） <kbd>量能相關</kbd>

##### 語法
> 傳回「近15分鐘特大單買賣超」的張數  
> **回傳數值 = DiffBidAskVolumeXL**  
> 僅支援1分鐘頻率與台股商品。  

---

##### 說明
DiffBidAskVolumeXL為近15分鐘特大單買賣超張數的函數。

範例：
```pascal
value1 = DiffBidAskVolumeXL;
plot1(value1); //value1為近15分鐘特大單買賣超張數
```

___


## DiffTradeVolumeAtAskBid
--- 

### DiffTradeVolumeAtAskBid
#### DiffTradeVolumeAtAskBid – （系統函數） <kbd>量能相關</kbd>

##### 語法
> 傳回「分時買賣力」的數值  
> **回傳數值 = DiffTradeVolumeAtAskBid**  
> 僅支援分鐘與日頻率（含還原）  
> 支援台股與期權商品。  

---

##### 說明
DiffTradeVolumeAtAskBid為分時買賣力的函數，
該函數運算出來的數值，與XS指標的「分時買賣力」指標相同。

___


## DiffUpDownVolume
--- 

### DiffUpDownVolume
#### DiffUpDownVolume – （系統函數） <kbd>量能相關</kbd>

##### 語法
> 傳回「分時漲跌成交量」的數值  
> **回傳數值 = DiffUpDownVolume**  
> 僅支援分鐘與日頻率（含還原）  
> 支援台股與期權商品。  

---

##### 說明
DiffUpDownVolume為分時漲跌成交量的函數，
該函數運算出來的數值，與XS指標的「分時漲跌成交量」指標相同。

___
