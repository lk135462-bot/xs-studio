# XQ 官方選股腳本範例庫

共 324 個選股腳本範例。

---

## 腳本檔案: 選股/00.語法範例/_基本範例.xs

```xs
{@type:filter}
// 選股範例程式
//

// 使用GetField來取得欄位的數值。請按F7或從「編輯」|「插入欄位」選項內啟動插入欄位的畫面。
// GetField函數的第一個參數是欄位名稱，例如 "每股稅後淨利(元)"，
// GetField函數的第二個參數是欄位的期別，例如 "Q"代表季資料，"M"代表月資料,"Y"代表年資料。
//
Value1 = GetField("每股稅後淨利(元)","Q");

// 如果GetField函數的第二個參數省略的話，則系統會根據執行這個腳本時所設定的頻率來決定
// 資料的期別。請務必注意引用腳本時必須設定正確的頻率，否則可能會遇到執行錯誤的情形。
//
Value2 = GetField("每股稅後淨利(元)");

// 可以使用任何XSScript的語法來做運算，如果股票符合預期的話請設定Ret = 1，以下面一行為例
// 這個腳本會選到最新一年每股稅後淨利 > 5元的股票
//
Ret = GetField("每股稅後淨利(元)","Y") > 5;

// ＊＊　在這個目錄內有更多的程式範本可以參考　＊＊
//
```

---


---

## 腳本檔案: 選股/00.語法範例/EPS連續N季成長.xs

```xs
{@type:filter}
input:N(4); SetInputName(1, "期別");
 
SetTotalBar(3); 

if TrueAll(GetField("EPS","Q") > GetField("EPS","Q")[1],N) then ret=1; 

SetOutputName1("EPS(元)(季)"); 
OutputField1(GetField("EPS","Q"));
```

---


---

## 腳本檔案: 選股/00.語法範例/EPS連續N季衰退.xs

```xs
{@type:filter}
input:N(4); SetInputName(1, "期別");
 
SetTotalBar(3); 

if TrueAll(GetField("EPS","Q") < GetField("EPS","Q")[1],N) then ret=1; 

SetOutputName1("EPS(元)(季)"); 
OutputField1(GetField("EPS","Q"));
```

---


---

## 腳本檔案: 選股/00.語法範例/EPS連續N季都大於X元.xs

```xs
{@type:filter}
input:N(4); setinputname(1, "期別");
input:X(1); setinputname(2, "元"); 

SetTotalBar(3); 

if TrueAll(GetField("EPS", "Q") > X,N) then ret=1; 

SetOutputName1("EPS(元)(季)"); 
OutputField1(GetField("EPS", "Q"));
```

---


---

## 腳本檔案: 選股/00.語法範例/EPS連續N季都小於X元.xs

```xs
{@type:filter}
input:N(4); setinputname(1, "期別");
input:X(0); setinputname(2, "元"); 

SetTotalBar(3); 

if TrueAll(GetField("EPS", "Q") < X,N) then ret=1; 

SetOutputName1("EPS(元)(季)"); 
OutputField1(GetField("EPS", "Q"));
```

---


---

## 腳本檔案: 選股/00.語法範例/EPS連續N年都大於X元.xs

```xs
{@type:filter}
input:N(4); setinputname(1, "期別");
input:X(1); setinputname(2, "元"); 

SetTotalBar(3); 

if TrueAll(GetField("EPS", "Y") > X,N) then ret=1; 

SetOutputName1("EPS(元)(年)"); 
OutputField1(GetField("EPS", "Y"));
```

---


---

## 腳本檔案: 選股/00.語法範例/EPS連續N年都小於X元.xs

```xs
{@type:filter}
input:N(4); setinputname(1, "期別");
input:X(0); setinputname(2, "元"); 

SetTotalBar(3); 

if TrueAll(GetField("EPS", "Y") < X,N) then ret=1; 

SetOutputName1("EPS(元)(年)"); 
OutputField1(GetField("EPS", "Y"));
```

---


---

## 腳本檔案: 選股/00.語法範例/N期股價趨勢向上.xs

```xs
{@type:filter}
input: Period(10); SetInputName(1, "期別");

settotalbar(3);

Condition1 = rateofchange(close, period) >= Period;
Condition2 = close > close[Period/2];
Condition3 = close > average(close, period);

ret = condition1 and condition2 and condition3;
```

---


---

## 腳本檔案: 選股/00.語法範例/N期股價趨勢向下.xs

```xs
{@type:filter}
input: Period(10); SetInputName(1, "期別");

settotalbar(3);

Condition1 = rateofchange(close, period) <= -1 * Period;
Condition2 = close < close[Period/2];
Condition3 = close < average(close, period);

ret = condition1 and condition2 and condition3;
```

---


---

## 腳本檔案: 選股/00.語法範例/收盤價近N期漲幅大於X%以上.xs

```xs
{@type:filter}
input:N(10);	SetInputName(1, "期別");
input:X(5); 	SetInputName(2, "漲幅%");

SetTotalBar(3); 

Value1 = RateOfChange(GetField("收盤價"),N);
if Value1 > X then ret=1;
 
SetOutputName1("近期漲幅%"); 
OutputField1(Value1);
```

---


---

## 腳本檔案: 選股/00.語法範例/收盤價近N期跌幅大於X%以上.xs

```xs
{@type:filter}
input:N(10);	SetInputName(1, "期別");
input:X(5); 	SetInputName(2, "跌幅%");

SetTotalBar(3); 

Value1 = RateOfChange(GetField("收盤價"),N);
if Value1 < -1 * X then ret=1;
 
SetOutputName1("近期跌幅%"); 
OutputField1(Value1);
```

---


---

## 腳本檔案: 選股/00.語法範例/最近4季EPS合計大於X元.xs

```xs
{@type:filter}
input:X(5); SetInputName(1, "元");

variable: N(4);

SetTotalBar(3); 

Value1 = Summation(GetField("EPS","Q"),N);
if Value1 > X then ret=1; 

SetOutputName1("EPS合計"); 
OutputField1(Value1);
```

---


---

## 腳本檔案: 選股/00.語法範例/最近4季EPS合計小於X元.xs

```xs
{@type:filter}
input:X(0); SetInputName(1, "元");

variable: N(4);

SetTotalBar(3); 

Value1 = Summation(GetField("EPS","Q"),N);
if Value1 < X then ret=1; 

SetOutputName1("EPS合計"); 
OutputField1(Value1);
```

---


---

## 腳本檔案: 選股/00.語法範例/月營收創N期新低.xs

```xs
{@type:filter}
input:N(13); setinputname(1, "期別"); 

SetTotalBar(3); 

if GetField("月營收", "M") <= Lowest(GetField("月營收", "M"),N) then ret=1; 

SetOutputName1("月營收"); 
OutputField1(GetField("月營收", "M"));
```

---


---

## 腳本檔案: 選股/00.語法範例/月營收創N期新高.xs

```xs
{@type:filter}
input:N(13); setinputname(1, "期別"); 

SetTotalBar(3); 

if GetField("月營收", "M") >= Highest(GetField("月營收", "M"),N) then ret=1; 

SetOutputName1("月營收"); 
OutputField1(GetField("月營收", "M"));
```

---


---

## 腳本檔案: 選股/00.語法範例/本益比小於X倍.xs

```xs
{@type:filter}
Input: X(10); SetInputName(1, "本益比(倍)");

settotalbar(3);

Value1 = GetField("本益比", "D");
if Value1 < X then Ret = 1;

SetOutputName1("本益比(倍)");
outputfield1(Value1);
```

---


---

## 腳本檔案: 選股/00.語法範例/股價大於近N期平均.xs

```xs
{@type:filter}
input:N(5); setinputname(1, "期別"); 

SetTotalBar(3);

Value1 = Average(GetField("Close"),N);
if GetField("Close") > Average(GetField("Close"),N) then ret=1; 

SetOutputName1("均價");
outputfield1(Value1);
```

---


---

## 腳本檔案: 選股/00.語法範例/股價小於近N期平均.xs

```xs
{@type:filter}
input:N(5); setinputname(1, "期別"); 

SetTotalBar(3);

Value1 = Average(GetField("Close"),N);
if GetField("Close") < Value1 then ret=1; 

SetOutputName1("均價");
outputfield1(Value1);
```

---


---

## 腳本檔案: 選股/00.語法範例/週轉率大於X%.xs

```xs
{@type:filter}
Input: X(5); SetInputName(1, "週轉率%");

settotalbar(3);

Value1 = GetField("週轉率","D");
if Value1 > X then Ret = 1;

SetOutputName1("週轉率%");
outputfield1(Value1);
```

---


---

## 腳本檔案: 選股/01.常用過濾條件/股本篩選.xs

```xs
{@type:filter}
input:MinCapital(10);
input:MaxCapital(50); 

SetInputName(1, "最小股本(億)");
SetInputName(2, "最大股本(億)");

SetTotalBar(3);

Value1 = GetField("最新股本");

// 介於兩者之間
Ret = Value1 >= MinCapital and Value1 <= MaxCapital;
```

---


---

## 腳本檔案: 選股/01.常用過濾條件/股票名稱不含F股.xs

```xs
{@type:filter}
variable:sn("");
sn=symbolname;
if instr(sn,"F")=0
and instr(sn,"Y")=0 then ret=1;
outputfield(1,sn,0,"symbolname");
```

---


---

## 腳本檔案: 選股/01.常用過濾條件/過濾低價股票.xs

```xs
{@type:filter}
input:PriceLimit(5);

SetInputName(1, "最小股價");

SetTotalBar(3);

Ret = close > PriceLimit;
```

---


---

## 腳本檔案: 選股/01.常用過濾條件/過濾低成交量股票.xs

```xs
{@type:filter}
input:Length(5);
input:VolumeLimit(500);
 
SetInputName(1, "均量天期");
SetInputName(2, "最小均量");

SetTotalBar(3);

Value1 = Average(volume, Length);
Ret = Value1 > VolumeLimit;

SetOutputName1("成交均量");
OutputField1(Value1);
```

---


---

## 腳本檔案: 選股/01.常用過濾條件/過濾冷門股票.xs

```xs
{@type:filter}
input:PriceLimit(5),Length(5), VolumeLimit(500);

SetInputName(1, "最小股價");
SetInputName(2, "均量天期");
SetInputName(3, "最小均量");

SetTotalBar(3);

Value1 = Average(volume,Length);
if close > PriceLimit and Value1 > VolumeLimit Then
ret = 1;
```

---


---

## 腳本檔案: 選股/01.常用過濾條件/過濾小型股票.xs

```xs
{@type:filter}
input:MinCapital(10);	// 股本(億)

SetInputName(1, "最小股本(億)");

SetTotalBar(3);

Ret = GetField("最新股本") > MinCapital;
```

---


---

## 腳本檔案: 選股/01.常用過濾條件/過濾沒賺錢的股票.xs

```xs
{@type:filter}
// 過去四季每股盈餘加總必須 > 0
//
SetTotalbar(3);

Value1 = summation(GetField("EPS","Q"), 4);
Ret = Value1 > 0;
```

---


---

## 腳本檔案: 選股/02.基本技術指標/BBand出現買進訊號.xs

```xs
{@type:filter}
input:length(20);
variable:up1(0),down1(0),mid1(0),bbandwidth(0);
up1 = bollingerband(Close, Length, 1);
down1 = bollingerband(Close, Length, -1 );
mid1 = (up1 + down1) / 2;

bbandwidth = 100 * (up1 - down1) / mid1;
if bbandwidth crosses above 5 and close > up1 and close> up1[1]
and average(close,20)>average(close,20)[1]
then ret=1;
```

---


---

## 腳本檔案: 選股/02.基本技術指標/CCI超買.xs

```xs
{@type:filter}
// CCI超買
//
Input: Length(14), AvgLength(9), OverBought(100);
Variable: cciValue(0), cciMAValue(0);

SetTotalBar(maxlist(AvgLength + Length + 1,6) + 3);

SetInputName(1, "期數");
SetInputName(2, "平滑期數");
SetInputName(3, "超買值");

cciValue = CommodityChannel(Length);
cciMAValue = Average(cciValue, AvgLength);

Condition1 = cciMAValue Crosses Over OverBought;
If condition1 then ret = 1;

SetOutputName1("CCI");
OutputField1(cciValue);
```

---


---

## 腳本檔案: 選股/02.基本技術指標/CCI超賣.xs

```xs
{@type:filter}
// CCI超賣
//
Input: Length(14), AvgLength(9), OverSold(-100);
Variable: cciValue(0), cciMAValue(0);

SetTotalBar(maxlist(AvgLength + Length + 1,6) + 3);

SetInputName(1, "期數");
SetInputName(2, "平滑期數");
SetInputName(3, "超賣值");

cciValue = CommodityChannel(Length);
cciMAValue = Average(cciValue, AvgLength);

Condition1 = cciMAValue Crosses Below OverSold;
If condition1 then ret = 1;

SetOutputName1("CCI");
OutputField1(cciValue);
```

---


---

## 腳本檔案: 選股/02.基本技術指標/KD死亡交叉.xs

```xs
{@type:filter}
// KD指標, K值由上往下穿越D值
//
input: Length(9), RSVt(3), Kt(3);
variable: rsv(0), k(0), _d(0);

SetTotalBar(maxlist(Length,6) * 3);

SetInputName(1, "天數");
SetInputName(2, "RSVt權數");
SetInputName(3, "Kt權數");

Stochastic(Length, RSVt, Kt, rsv, k, _d);

Ret = k crosses below _d;
```

---


---

## 腳本檔案: 選股/02.基本技術指標/KD黃金交叉.xs

```xs
{@type:filter}
// KD指標, K值由下往上穿越D值
//
input: Length(9), RSVt(3), Kt(3);
variable: rsv(0), k(0), _d(0);

SetTotalBar(maxlist(Length,6) * 3);

SetInputName(1, "天數");
SetInputName(2, "RSVt權數");
SetInputName(3, "Kt權數");

Stochastic(Length, RSVt, Kt, rsv, k, _d);

Ret = k crosses above _d;
```

---


---

## 腳本檔案: 選股/02.基本技術指標/MACD死亡交叉.xs

```xs
{@type:filter}
// MACD 死亡交叉 (dif向下穿越macd)
//
input: FastLength(12), SlowLength(26), MACDLength(9);
variable: difValue(0), macdValue(0), oscValue(0);

SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 4);

SetInputName(1, "DIF短期期數");
SetInputName(2, "DIF長期期數");
SetInputName(3, "MACD期數");

MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);

Ret = difValue Crosses Below macdValue;
```

---


---

## 腳本檔案: 選股/02.基本技術指標/MACD黃金交叉.xs

```xs
{@type:filter}
// MACD 黃金交叉 (dif向上穿越macd)
//
input: FastLength(12), SlowLength(26), MACDLength(9);
variable: difValue(0), macdValue(0), oscValue(0);

SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 4);

SetInputName(1, "DIF短期期數");
SetInputName(2, "DIF長期期數");
SetInputName(3, "MACD期數");

MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);

Ret = difValue Crosses Above macdValue;
```

---


---

## 腳本檔案: 選股/02.基本技術指標/MTM穿越0.xs

```xs
{@type:filter}
// MTM往上穿越0軸
//
Input: Length(10);

SetInputName(1, "期數");

settotalbar(maxlist(Length,6));

Ret = Momentum(Close, Length) Crosses Above 0;
```

---


---

## 腳本檔案: 選股/02.基本技術指標/MTM跌破0.xs

```xs
{@type:filter}
// MTM往下跌破0軸
//
Input: Length(10);

SetInputName(1, "期數");

settotalbar(maxlist(Length,6));

Ret = Momentum(Close, Length) Crosses Below 0;
```

---


---

## 腳本檔案: 選股/02.基本技術指標/RSI低檔背離.xs

```xs
{@type:filter}
// RSI由下往上, 與價格趨勢背離
Input: RSILength(6, "期數"), Threshold(20, "低檔值"), Region(5, "日期區間");
variable: rsiValue(0);

settotalbar(RSILength * 9);
setbackBar(RSILength);

RSIValue = RSI(Close, RSILength);
If RSIValue Crosses Above Threshold and
   RSIValue = Highest(RSIValue, Region) and
   LinearRegSlope(close,Region) < 0 then
   Ret = 1;
   
outputfield1(RSIValue,"RSI");
```

---


---

## 腳本檔案: 選股/02.基本技術指標/RSI死亡交叉.xs

```xs
{@type:filter}
// RSI短天期往下穿越長天期
//
input: ShortLength(6), LongLength(12);

settotalbar(maxlist(ShortLength,LongLength,6) * 9);

SetInputName(1, "短期期數");
SetInputName(2, "長期期數");

Ret = RSI(Close, ShortLength) Crosses Below RSI(Close, LongLength);
```

---


---

## 腳本檔案: 選股/02.基本技術指標/RSI高檔背離.xs

```xs
{@type:filter}
// RSI由高檔區往下, 與價格趨勢背離
Input: RSILength(6, "期數"), Threshold(80, "高檔值"), Region(5, "日期區間");
variable: rsiValue(0);

settotalbar(RSILength * 9);
setbackBar(RSILength);

RSIValue = RSI(Close, RSILength);
If RSIValue Crosses Below Threshold and
   RSIValue = Lowest(RSIValue, Region) and 
   LinearRegSlope(close,Region) > 0 then
  Ret = 1;

outputfield1(RSIValue,"RSI");
```

---


---

## 腳本檔案: 選股/02.基本技術指標/RSI黃金交叉.xs

```xs
{@type:filter}
// RSI短天期往上穿越長天期
//
input: ShortLength(6), LongLength(12);

settotalbar(maxlist(ShortLength,LongLength,6) * 9);

SetInputName(1, "短期期數");
SetInputName(2, "長期期數");

Ret = RSI(Close, ShortLength) Crosses Above RSI(Close, LongLength);
```

---


---

## 腳本檔案: 選股/02.基本技術指標/均線多頭排列.xs

```xs
{@type:filter}
input:Leng1(5),Leng2(20),Leng3(60);

variable: ma1(0), ma2(0), ma3(0);

SetInputName(1,"短均線");
SetInputName(2,"中均線");
SetInputName(3,"長均線");

settotalbar(3);

ma1 = average(close, Leng1);
ma2 = average(close, Leng2);
ma3 = average(close, Leng3);

condition1 = close > ma1;
condition2 = ma1 > ma2;
condition3 = ma2 > ma3;

if condition1 and condition2 and condition3 then 
ret = 1;

SetOutputName1("短均線");   
OutputField1(ma1);
SetOutputName2("中均線");   
OutputField2(ma2);
SetOutputName3("長均線");   
OutputField3(ma3);
```

---


---

## 腳本檔案: 選股/02.基本技術指標/均線空頭排列.xs

```xs
{@type:filter}
input:Leng1(5),Leng2(20),Leng3(60);

variable: ma1(0), ma2(0), ma3(0);

SetInputName(1,"短均線");
SetInputName(2,"中均線");
SetInputName(3,"長均線");

settotalbar(3);

ma1 = average(close, Leng1);
ma2 = average(close, Leng2);
ma3 = average(close, Leng3);

condition1 = close < ma1;
condition2 = ma1 < ma2;
condition3 = ma2 < ma3;

if condition1 and condition2 and condition3 then 
ret = 1;

SetOutputName1("短均線");   
OutputField1(ma1);
SetOutputName2("中均線");   
OutputField2(ma2);
SetOutputName3("長均線");   
OutputField3(ma3);
```

---


---

## 腳本檔案: 選股/02.基本技術指標/布林通道超買.xs

```xs
{@type:filter}
// 布林通道超買訊號
//
Input: Length(20), UpperBand(2);

SetInputName(1, "期數");
SetInputName(2, "通道上緣");

settotalbar(3);

Ret = High >= bollingerband(Close, Length, UpperBand);
```

---


---

## 腳本檔案: 選股/02.基本技術指標/布林通道超賣.xs

```xs
{@type:filter}
// 布林通道超賣訊號
//
Input: Length(20), LowerBand(2);

SetInputName(1, "期數");
SetInputName(2, "通道下緣");

settotalbar(3);

Ret = Low <= bollingerband(Close, Length, -1 * LowerBand);
```

---


---

## 腳本檔案: 選股/02.基本技術指標/帶量突破均線.xs

```xs
{@type:filter}
// 帶量突破均線
//
input: Length(10), VolFactor(2);

SetInputName(1, "期數");
SetInputName(2, "成交量放大倍數");

settotalbar(3);

if close > Average(close, Length) and  close[1] <  Average(close, Length) and
   volume > Average(volume[1], Length) * VolFactor 
then ret=1;
```

---


---

## 腳本檔案: 選股/02.基本技術指標/成交量放大.xs

```xs
{@type:filter}
input: Length(5), VolFactor(2);

SetInputName(1, "均量區間");
SetInputName(2, "放大倍數");

settotalbar(3);

Ret = Volume > Average(Volume[1], Length) * VolFactor;
```

---


---

## 腳本檔案: 選股/02.基本技術指標/短期均線穿越長期均線.xs

```xs
{@type:filter}
input: Shortlength(5); setinputname(1,"短期均線期數");
input: Longlength(20); setinputname(2,"長期均線期數");

settotalbar(3);

If Average(Close,Shortlength) crosses over Average(Close,Longlength) then Ret=1;
```

---


---

## 腳本檔案: 選股/02.基本技術指標/短期均線跌破長期均線.xs

```xs
{@type:filter}
input: Shortlength(5); setinputname(1,"短期均線期數");
input: Longlength(20); setinputname(2,"長期均線期數");

settotalbar(3);

If Average(Close,Shortlength) crosses under Average(Close,Longlength) then Ret=1;
```

---


---

## 腳本檔案: 選股/02.基本技術指標/跌破糾結均線.xs

```xs
{@type:filter}
setbarfreq("AD");

input: shortlength(5); setinputname(1,"短期均線期數");
input: midlength(10); setinputname(2,"中期均線期數");
input: Longlength(20); setinputname(3,"長期均線期數");
input: Percent(5);  setinputname(4,"均線糾結區間%");
input: XLen(20);  setinputname(5,"均線糾結期數");

input: Volpercent(25);  setinputname(6,"放量幅度%");//帶量突破的量是超過最長期的均量多少%
variable: shortaverage(0);
variable: midaverage(0);
variable: Longaverage(0);
variable: AvgHLp(0),AvgH(0),AvgL(0);

shortaverage = average(close,shortlength);
midaverage = average(close,midlength);
Longaverage = average(close,Longlength);
	
AvgH = maxlist(shortaverage,midaverage,Longaverage);
AvgL = minlist(shortaverage,midaverage,Longaverage);

if AvgL > 0 then AvgHLp = 100*AvgH/AvgL -100;

condition1 = trueAll(AvgHLp < Percent,XLen);
condition2 = V >  average(V[1],XLen)*(1+Volpercent/100) ;
condition3 = average(Volume[1], 5) >= 2000;
condition4 = C < AvgL *(0.98) and L < lowest(L[1],XLen);

ret = condition1 and condition2 and condition3 and condition4;

outputfield(1,AvgH,2,"均線上緣", order := -1);
outputfield(2,AvgL,2,"均線下緣");
```

---


---

## 腳本檔案: 選股/02.基本技術指標/週KD低檔黃金交叉.xs

```xs
{@type:filter}
// KD指標, K值由下往上穿越D值
//
input: Length(9), RSVt(3), Kt(3);
variable: rsv(0), k(0), _d(0);

SetInputName(1, "天數");
SetInputName(2, "RSVt權數");
SetInputName(3, "Kt權數");

Stochastic(Length, RSVt, Kt, rsv, k, _d);

Ret = k crosses above _d and k<30;
```

---


---

## 腳本檔案: 選股/02.基本技術指標/週線月線黃金交叉且站穩.xs

```xs
{@type:filter}
setbarfreq("AD");

value1=average(close,5);
value2=average(close,20);
if value1[3] crosses over value2[3]
and trueall(close>close[1]and close>value1,5)
then ret=1 ;

outputfield(1,value1,2,"週線", order := -1);
outputfield(2,value2,2,"月線");
```

---


---

## 腳本檔案: 選股/03.進階技術分析/KD與均線同步出現買進訊號.xs

```xs
{@type:filter}
input: Length(60, "均線期間");

variable:rsv1(0),k1(0),d1(0);

stochastic(9,3,3,rsv1,k1,d1);

// K線黃金交叉
condition1 = k1 crosses over d1;

condition2 = close crosses over average(close,Length) or close[1] crosses over average(close[1],Length);

// 確認有一定的成交量
condition3 = average(volume,20) > 1000;

ret = condition1 and condition2 and condition3;

outputfield(1,average(close,Length),2,"60日均線", order := -1);
```

---


---

## 腳本檔案: 選股/03.進階技術分析/K棒突破布林值上緣.xs

```xs
{@type:filter}
Input: 
	Length(20, "期數"), 
	UpperBand(2, "通道上緣");

settotalbar(3);

Ret = close >= bollingerband(Close, Length, UpperBand);
```

---


---

## 腳本檔案: 選股/03.進階技術分析/RSI黃金交叉且股價非盤整.xs

```xs
{@type:filter}
input:n1(6); 	setinputname(1,"RSI短期天數");
input:n2(12);	setinputname(2,"RSI長期天數");
input:n3(4);	setinputname(3,"盤整期間創新高次數");


settotalbar(maxlist(n1,n2,6) * 9);

value2 = highdays(n2);

if rsi(close,n1) crosses over rsi(close,n2) and
   rsi(close,n1) < 50 and
   value2 >= n3
then ret=1;
```

---


---

## 腳本檔案: 選股/03.進階技術分析/佔大盤成交量比開始上昇.xs

```xs
{@type:filter}
value1=GetField("佔全市場成交量比","D");

SetTotalBar(5);

if value1[4]=lowest(value1,5) and 
   value1=highest(value1,5) and 
   close crosses above average(close,5)
then ret=1;

SetOutputName1("佔全市場成交量比(%)");
OutputField1(value1);
```

---


---

## 腳本檔案: 選股/03.進階技術分析/冷門股出量.xs

```xs
{@type:filter}
input:limit1(700);		setinputname(1,"均量上限");
input:limit2(1000);		setinputname(2,"突破量");

SetTotalBar(3);

value1 = average(volume,5);
 
if value1 < limit1 and volume > limit2 and High > close[1] and volume > volume[1]
then ret=1;
```

---


---

## 腳本檔案: 選股/03.進階技術分析/外盤成交變多.xs

```xs
{@type:filter}
input:shortPeriod(5);		setinputname(1,"短期平均");
input:midPeriod(12);		setinputname(2,"長期平均");
input:minVolume(2000);		setinputname(3,"成交量門檻");

variable:
	sVolume(0),
	bVolume(0),
	ratio(0),
	ratioAvgShort(0),
	ratioAvgLong(0);

SetTotalBar(MaxList(shortPeriod, midPeriod) + 3);
	
sVolume = GetField("內盤量", "D");//內盤量
bVolume = GetField("外盤量", "D"); //外盤量
if sVolume + bVolume <> 0 then
	ratio = bVolume / (sVolume + bVolume) * 100
else
	ratio = 50;
	
ratioAvgShort = average(ratio,shortPeriod);
ratioAvgLong = average(ratio,midPeriod);

if 
	volume > minVolume and 
	ratioAvgShort < 40 and 
	ratioAvgLong < 40 and 
	absvalue(ratioAvgShort-ratioAvgLong) < 10 and 
	ratioAvgShort crosses above ratioAvgLong
then 
	ret=1;
```

---


---

## 腳本檔案: 選股/03.進階技術分析/多指標都出現買進訊號.xs

```xs
{@type:filter}
settotalbar(120);

//=========計算RSI======================
Input:rsilength(6);		Setinputname(1,"設定RSI計算天期");
input:rsilimit(50);		Setinputname(2,"設定RSI要突破的限制");

Value1=rsi(close,rsilength);//計算RSI的值

//==========計算威廉指標==================
input: rLength(3);		SetInputName(3, "設定威廉指標天期");
input: rLimit(-50);		SetInputName(4, "設定威廉指標的限制");

value2 = PercentR(rLength) - 100;

//============計算DMI=======================
input: dmiLength(10);	setinputname(5,"設定DMI天期");
variable: pdi_value(0), ndi_value(0), adx_value(0);
DirectionMovement(dmiLength, pdi_value, ndi_value, adx_value);
value4=pdi_value;

//============純粹只是想確認本週股價都沒有跌破前週低==============
condition1 = GetField("Low", "W") > GetField("Low", "W")[1];

//============ XQ: tt指標==========================================
input: Length(10);		SetInputName(6, "設定tt指標計算期數");

variable: kk(0), qu(0), qd(0), qf(0), tt(0);

qf = 0;
qu = 0;
qd = 0;

for kk = 1 to length
  begin
	if close[(kk - 1)] > close[kk] then
		qu = qu + Volume[(kk - 1)]
	else
	  begin
		if close[(kk - 1)] < close[kk] then
			qd = qd + Volume[(kk - 1)]
		else { close[(kk - 1)] = close[kk] }
			qf = qf + Volume[(kk - 1)];
	  end;
  end;

if (qd + qf/2) <> 0 then
	tt = 100 * (qu + qf/2) /(qd + qf/2)
else
	tt = 1000;

value5=tt;

//==================設定警示條件====================================
if value1 > rsilimit 
and value2 > rLimit
and condition1 = true
and value4 > 0
and value5 > 800 
then ret=1;
```

---


---

## 腳本檔案: 選股/03.進階技術分析/多空分數翻昇.xs

```xs
{@type:filter}
// 計算技術指標分數序列, 判斷指標分數是否翻轉
//
settotalbar(168);

value1 = techscore();
value2 = average(value1, 10);
if value2 crosses above 5 then ret = 1;
```

---


---

## 腳本檔案: 選股/03.進階技術分析/多空分數轉空.xs

```xs
{@type:filter}
// 計算技術指標分數序列, 判斷指標分數是否翻轉
//
settotalbar(168);

value1 = techscore();
value2 = average(value1, 10);
if value2 crosses under 10 then ret = 1;
```

---


---

## 腳本檔案: 選股/03.進階技術分析/天量後價量未再創新高.xs

```xs
{@type:filter}
input:XLength(60); 	setinputname(1,"長期大量計算期數");
input:Length(3); 	setinputname(2,"超過n日價量未再創新高");

variable: PriceHighBar(0),VolumeHighBar(0);

settotalbar(3);

VolumeHighBar = highestbar(volume, XLength);
PriceHighBar = highestbar(high, Length);

// 近日內成交量創新高, 可是價格沒有創新高
//
if VolumeHighBar > 0 and 
   VolumeHighBar <= Length and
   PriceHighBar = VolumeHighBar then
ret = 1;
```

---


---

## 腳本檔案: 選股/03.進階技術分析/布林帶寬大於N%.xs

```xs
{@type:filter}
input: 
	Length(20, "天數"), 
	UpperBand(2, "上"), 
	LowerBand(2, "下"),
	BBW(80,"N");
	
variable: 
	bbandwidth(0);

bbandwidth = bollingerbandwidth(Close, Length, UpperBand, LowerBand);

if bbandwidth >= BBW then ret=1;

outputfield(1,bbandwidth,2,"布林帶寬");
```

---


---

## 腳本檔案: 選股/03.進階技術分析/布林帶寬小於N%.xs

```xs
{@type:filter}
input: 
	Length(20, "天數"), 
	UpperBand(2, "上"), 
	LowerBand(2, "下"),
	BBW(20,"N");
	
variable: 
	bbandwidth(0);

bbandwidth = bollingerbandwidth(Close, Length, UpperBand, LowerBand);

if bbandwidth <= BBW then ret=1;

outputfield(1,bbandwidth,2,"布林帶寬");
```

---


---

## 腳本檔案: 選股/03.進階技術分析/帶量突破均線後未拉回.xs

```xs
{@type:filter}
input:day(5);		setinputname(1,"幾天內未站回");
input:length(10);	setinputname(2,"移動平均線期別");
input:percent(20);	setinputname(3,"突破當日成交量超過均量多少%");

SetTotalBar(3);

value1=average(close,length);
value2=average(volume,length);

if close[day-1] crosses over average(close[day-1], length) and
   volume[day-1] > average(volume[day-1], length) * (1+percent/100) and
   volume > 1000
then
  begin
	variable: keyprice(0);
	
	keyprice = average(close[day-1], length);
	if trueall(close > keyprice, day-1) then ret = 1;
  end;
```

---


---

## 腳本檔案: 選股/03.進階技術分析/底部越來越高且資金流入的蓄勢股.xs

```xs
{@type:filter}
input:r1(7);		setinputname(1,"近來漲幅上限%");

SetTotalBar(8);

value1 = RateOfChange(close, 12);
value2 = lowest(low,3);
value3 = lowest(low,8);
value4 = lowest(low,13);

condition1=false;
condition2=false;

if 
	value1 < r1 and
	value2 > value3 and 
	value3 > value4 and
	close = highest(close,13)
then 
	condition1=true;

Value5=average(GetField("佔全市場成交量比","D"),13);

if linearregslope(Value5,5) > 0
then condition2=true;

if condition1 and condition2
then ret=1;
```

---


---

## 腳本檔案: 選股/03.進階技術分析/波動幅度開始變大.xs

```xs
{@type:filter}
input: Length(20);		SetInputName(1, "計算區間");
input: VolLimit(1000); SetInputName(2, "成交量限制");

value1 = truerange();
value2 = highest(value1,Length);

SetTotalBar(Length + 3);

if 
	value1 > value2[1] and 
	value1 > value1[1] and 
	close * 1.01 > high and 
	close > close[1] and 
	volume > VolLimit
then ret=1;
```

---


---

## 腳本檔案: 選股/03.進階技術分析/盤整後跌破.xs

```xs
{@type:filter}
input:length(20); 	setinputname(1, "計算期間");
input:percent(7); 	setinputname(2, "設定盤整區間%");

SetTotalBar(3);

value1 = highest(high[1],length);
value2 = lowest(low[1],length);

if 
	close crosses under value2 and 
	value1 < value2 *( 1 + percent * 0.01) //最近幾根bar的收盤價高點與低點差不到N%
then ret=1;
```

---


---

## 腳本檔案: 選股/03.進階技術分析/突破糾結均線.xs

```xs
{@type:filter}
input: shortlength(5); 	setinputname(1,"短期均線期數");
input: midlength(10); 	setinputname(2,"中期均線期數");
input: Longlength(20); 	setinputname(3,"長期均線期數");
input: Percent(2);  	setinputname(4,"均線糾結區間%");
input: Volpercent(25);  setinputname(5,"放量幅度%");//帶量突破的量是超過最長期的均量多少%
input: VolLimit(2000); 	setinputname(6,"最小成交量");

variable: shortaverage(0);
variable: midaverage(0);
variable: Longaverage(0);
variable: maxaverage(0);


shortaverage = average(close,shortlength);
midaverage = average(close,midlength);
Longaverage = average(close,Longlength);
maxaverage = maxlist(shortaverage,midaverage,Longaverage);

SetTotalBar(8);

if 
	volume > average(volume,Longlength) * (1 + volpercent * 0.01) and 
	volume > VolLimit and
    Close crosses over maxaverage 
then
  begin
	value1= absvalue(shortaverage -midaverage);
	value2= absvalue(midaverage -Longaverage);
	value3= absvalue(Longaverage -shortaverage);
	if maxlist(value1,value2,value3)*100 < Percent*Close then  ret=1;
  end;
```

---


---

## 腳本檔案: 選股/03.進階技術分析/築底指標出現買進訊號.xs

```xs
{@type:filter}
input: period(125);		setinputname(1, "計算區間長度");
input: length1(5);		setinputname(2, "短天期");
input: length2(20);		setinputname(3, "長天期");

variable:zd(0),zdma1(0),zdma2(0);

SetTotalBar(Period + 8);

zd = countif(close>=close[1],period) / countif(close<close[1],period);
zdma1 = average(zd,length1);
zdma2 = average(zd,length2);

if zdma1<1 and zdma2<1 and zdma1 crosses above zdma2
then ret=1;
```

---


---

## 腳本檔案: 選股/03.進階技術分析/股價下跌而外盤量佔比上升.xs

```xs
{@type:filter}
input:period(20);		setinputname(1,"計算天期");

settotalbar(period * 2 + 3);

value1 = GetField("外盤量");//日的外盤量
if volume <> 0 then 
	value2 = value1 / volume
else
	value2 = 0;

value3 = average(value2, period);
if linearregslope(value3,period) > 0 and
   linearregslope(close,period) < 0 and 
   volume > 1000
then ret=1;
```

---


---

## 腳本檔案: 選股/03.進階技術分析/股價蠢蠢欲動.xs

```xs
{@type:filter}
SetTotalBar(23);

value1=truerange();
value2=highest(value1,20);

if value1 > value2[1] and 
   value1 > value1[1] and 
   close*1.01 > high and 
   close > close[1]
then ret=1;
```

---


---

## 腳本檔案: 選股/03.進階技術分析/股價跌破走跌後的高壓電線.xs

```xs
{@type:filter}
SetTotalBar(8);

value1 = (average(close,30) + average(close,72)) / 2;	//地心引力線
value2 = value1*1.2;//高壓電線
value3 = linearregslope(value2,5);

if absvalue(value3) <= 0.1 and close crosses under value1
then ret=1;
```

---


---

## 腳本檔案: 選股/03.進階技術分析/趨勢成形.xs

```xs
{@type:filter}
// ADX趨勢成形
//
input: Length(14), Threshold(25);

variable: pdi_value(0), ndi_value(0), adx_value(0);

SetTotalBar(Length*11);

SetInputName(1, "期數");
SetInputName(2, "穿越值");

DirectionMovement(Length, pdi_value, ndi_value, adx_value);

if adx_value Crosses Above Threshold and close=high
then ret=1;
```

---


---

## 腳本檔案: 選股/03.進階技術分析/跌破均線後站不回.xs

```xs
{@type:filter}
input:day(3);			setinputname(1,"幾天內未站回");
input:length(20);		setinputname(2,"移動平均線期別");

settotalbar(length + 3);

if close[day-1] crosses under average(close[day-1], length) then
  begin
	variable: keyprice(0);
	
	keyprice = average(close[day-1], length);
	if trueall(close < keyprice, day-1) then ret = 1;
  end;
```

---


---

## 腳本檔案: 選股/03.進階技術分析/雙KD向上.xs

```xs
{@type:filter}
setbarfreq("AD");

input: Length_D(9, "日KD期間");
input: Length_W(5, "周KD期間");

variable:rsv_d(0),kk_d(0),dd_d(0);
variable:rsv_w(0),kk_w(0),dd_w(0);

stochastic(Length_D, 3, 3, rsv_d, kk_d, dd_d);
xf_stochastic("W", Length_W, 3, 3, rsv_w, kk_w, dd_w);

condition1 = kk_d crosses above dd_d;		// 日KD crosses over
condition2 = xf_crossover("W", kk_w, dd_w);	// 周KD crosses over
condition3 = average(volume[1], 5) >= 1000;

condition4 = kk_d[1] <= 30;							// 日K 低檔
condition5 = xf_getvalue("W", kk_w, 1) <= 50;		// 周K 低檔

ret = condition1 and condition2 and condition3 and condition4 and condition5;

outputfield(1,kk_d,2,"日K值");
outputfield(2,kk_w,2,"週K值", order := -1);
```

---


---

## 腳本檔案: 選股/04.價量選股/M日內連續N日上漲.xs

```xs
{@type:filter}
input:day(11);
input:m1(3);
setinputname(1,"計算天期");
setinputname(2,"連續上漲天數");

variable:x(0),count(0);
count=0;
for x=0 to day-m1 
begin
if close[x]>close[x+1]
and close[x+1]>close[x+2]
and close[x+2]>close[x+3]
then count=count+1;
end;
if count>=1
then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/N年來漲了M倍的公司.xs

```xs
{@type:filter}
input:y1(10,"計算的年數");
input:ratio(800,"上漲的倍數%");

value1=rateofchange(GetField("收盤價","AM"),y1*12);

if value1>=ratio
then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/五日週轉率大於二十日週轉率.xs

```xs
{@type:filter}
if turnoverrate(5)>turnoverrate(20)
then ret=1;
outputfield(1,turnoverrate(5),1,"5日平均週轉率");
outputfield(2,turnoverrate(20),1,"20日平均週轉率");
```

---


---

## 腳本檔案: 選股/04.價量選股/今收破昨高.xs

```xs
{@type:filter}
if close>=high[1]
then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/修正式價量指標黃金交叉.xs

```xs
{@type:filter}
setbarfreq("AD");

input:day(10, "移動平均線天數");

variable:tvp(0),mpc(0);
mpc=(open+high+low+close)/4;

if mpc[1]<>0
then tvp=tvp[1]+(mpc-mpc[1])/mpc[1]*volume
else tvp=tvp[1];

value1=average(tvp,day);
If tvp crosses over value1 and volume>1000
and tvp>value1*1.05
then ret=1;

outputfield(1,average(c,day),2,"10日線", order := -1);
```

---


---

## 腳本檔案: 選股/04.價量選股/價量同步創N期新高.xs

```xs
{@type:filter}
input:period(100,"計算天數");

value1=highest(high,period);
value2=highest(volume,period);
if high=value1 and volume=value2
then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/創最低總市值.xs

```xs
{@type:filter}
input:period(36,"計算的月份數");
setbarfreq("M");

if GetField("總市值","M")=lowest(GetField("總市值","M"),period)
then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/創百日來新高但距離低點不太遠.xs

```xs
{@type:filter}
//說明：今天的收盤價創百日來的收盤價新高，但是收盤價距離低點不太遠

input:day(100);			setinputname(1,"計算區間");
input:percents(14);		setinputname(2,"距離區間最低點漲幅");

SetTotalBar(3);

value1 = lowest(close, day);
if close=highest(close,day) and value1 * (1 + percents/100) >= close
then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/區間內股價創新高天數達一定水準.xs

```xs
{@type:filter}
input:period(10,"計算區間");
input:lowlimit(3,"附合條件的最低次數");
if countif(high=highest(high,20),period)>=lowlimit
then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/多日價量背離後跌破.xs

```xs
{@type:filter}
setbarfreq("AD");

input:Length(5, "計算期數");
input:times(3, "價量背離次數");
input:Dist(20, "距離");

variable:count(0),KPrice(0),hDate(0);

count = CountIf(close > close[1] and volume < volume[1], Length);

if count > times then  begin
  hDate=Date;
  Kprice = lowest(l,length);
end;

Condition1 = Close crosses below Kprice;
Condition2 = DateDiff(Date,hdate) < Dist;
Ret = Condition1 And Condition2;

outputfield(1,Kprice,2,"關卡價", order := -1);
```

---


---

## 腳本檔案: 選股/04.價量選股/多次到底而跌破.xs

```xs
{@type:filter}
setbarfreq("AD");

input:HitTimes(3,"設定觸底次數");
input:RangeRatio(1,"設定底部區範圍寬度%");
input:Length(20,"計算期數");

variable: theLow(0); 
variable: LowUpperBound(0); 
variable: TouchRangeTimes(0);

//找到過去期間的最低點
theLow = lowest(low[1],Length); 

// 設為瓶頸區間上界
LowUpperBound = theLow *(100+RangeRatio)/100; 

//期間中進入瓶頸區間的低點次數,每根K棒要歸0
TouchRangeTimes = CountIF(Low[1] < LowUpperBound, Length);
 
Condition1 = TouchRangeTimes >= HitTimes;
Condition2 = close < theLow;
Condition3 = Average(Volume, 5) >= 1000;
 
Ret = Condition1 And Condition2 And Condition3;

outputfield(1, theLow, 2, "區間低點", order := -1);
```

---


---

## 腳本檔案: 選股/04.價量選股/多頭轉強.xs

```xs
{@type:filter}
setbarfreq("AD");

input:length(10, "天期");
variable: sumUp(0), sumDown(0), up(0), down(0),RS(0);

if CurrentBar = 1 then  begin
    sumUp = Average(maxlist(close - close[1], 0), length);
    sumDown = Average(maxlist(close[1] - close, 0), length);
end else begin
	up = maxlist(close - close[1], 0);
	down = maxlist(close[1] - close, 0);
    sumUp = sumUp[1] + (up - sumUp[1]) / length;
	sumDown = sumDown[1] + (down - sumDown[1]) / length;
end;

if sumdown<>0
then rs=sumup/sumdown;

if rs crosses over 4
and close<close[3]*1.06
//最近3日漲幅小於6%
and Average(Volume[1], 100) >= 500
//成交量判斷
then ret=1;

outputfield(1, nthlowest(1,low[1],length), 2, "區間低點", order := -1);
```

---


---

## 腳本檔案: 選股/04.價量選股/大漲股.xs

```xs
{@type:filter}
condition1=false;
condition2=false;
condition3=false;
//先把簡單的價量條件全部放在condition1
if highest(high,3)<lowest(low,3)*1.15
//區間震盪小於15%
and close>5 
//股價大於5元
and close<200
//股價小於5元
and volume>300
//當日成交量大於300張
and high=highest(high,2)
//創兩日來新高
and close>close[1]*1.02
//最近一日上漲超過2%
then condition1=true;

//用condition2來處理月線斜率大於0.4
value1=average(close,20);
//先算出月線
value2=linearregslope(value1,10);
//算出季線這十天的斜率
if value2>0.4 then condition2=true;
//月線斜率要大於0.4

//處理布林帶寬
input:length(20,"計算天期");
input:width(35,"帶寬%");
variable:up1(0),down1(0),mid1(0),bbandwidth(0);
up1 = bollingerband(Close, Length, 1);
down1 = bollingerband(Close, Length, -1 );
mid1 = (up1 + down1) / 2;

bbandwidth = 100 * (up1 - down1) / mid1;
if bbandwidth <width
then condition3=true;

ret=condition1 and condition2 and condition3;
```

---


---

## 腳本檔案: 選股/04.價量選股/大跌後的急拉.xs

```xs
{@type:filter}
setbarfreq("AD");

value1=barslast(close>=close[1]*1.07);
if value1[1]>50
//超過50天沒有單日上漲超過7%
and value1=0
//今天上漲超過7%
and average(volume,100)>500
and volume>1000
and close[1]*1.25<close[30]
//過去三十天跌幅超過25%
then ret=1;

outputfield(1,lowest(L,50),2,"前波低點", order := -1);
```

---


---

## 腳本檔案: 選股/04.價量選股/底部愈墊愈高且資金流入的蓄勢股.xs

```xs
{@type:filter}
input:r1(7,"近來漲幅上限%");

value1 = RateOfChange(close, 12);
value2 = lowest(low,3);
value3 = lowest(low,8);
value4 = lowest(low,13);

condition1=false;
condition2=false;

if 
	value1 < r1 and
	value2 > value3 and 
	value3 > value4 and
	close = highest(close,13)
then 
	condition1=true;

Value5=average(GetField("佔全市場成交量比","D"),13);

if linearregslope(Value5,5) > 0
then condition2=true;

if condition1 and condition2
then ret=1;

outputfield(1,value2,2,"前波低點", order := -1);
```

---


---

## 腳本檔案: 選股/04.價量選股/收盤價創N日來新高.xs

```xs
{@type:filter}
input:period(100,"計算天數");
if close=highest(close,period)
then ret=1;
value2=GetField("總市值","D");
outputfield(1,value2,0,"總市值");
```

---


---

## 腳本檔案: 選股/04.價量選股/收盤價收N日來新低.xs

```xs
{@type:filter}
input:period(100);
setinputname(1,"計算天數");
value1=LOWEST(LOW,period);

if LOW=value1 
then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/昨天成交量不到2000張今天已超過2000張.xs

```xs
{@type:filter}
if volume[1]<2000
and volume>2000
and close=highest(close,20)
then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/曾經一個月漲超過兩成的股票.xs

```xs
{@type:filter}
setbarfreq("M");
settotalbar(12);

if close>close[1]*1.2 then 
begin
	ret=1;
	outputfield(1,intportion(date*0.01),0,"上漲的月份");
end;
```

---


---

## 腳本檔案: 選股/04.價量選股/最近N日漲跌幅小於M%.xs

```xs
{@type:filter}
input:period(10,"計算區間");
input:ratio(10,"最低漲跌幅");

value1 = rateofchange(close,period-1);
if value1 < ratio then ret=1;

outputfield(1,value1,1,"區間漲跌幅");
```

---


---

## 腳本檔案: 選股/04.價量選股/有一定成交值且過去三日漲幅小.xs

```xs
{@type:filter}
input:b1(1.5,"三日漲幅上限");
if volume*close>=30000
and close<=close[2]*(1+b1/100)
then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/波動幅度開始變大且往上攻.xs

```xs
{@type:filter}
SetBarFreq("AD");

input: Length(20, "計算區間");
input: VolLimit(1000, "成交量限制");

value1 = truerange();
value2 = highest(value1,Length);

SetTotalBar(Length + 3);

if 
	value1 > value2[1] and 
	value1 > value1[1] and 
	close * 1.01 > high and 
	close > close[1] and 
	volume > VolLimit
then ret=1;

outputfield(1,close[1],2,"前波低點", order := -1);
```

---


---

## 腳本檔案: 選股/04.價量選股/波段漲幅不大，近N日有過漲停的.xs

```xs
{@type:filter}
input:day(10,"計算區間");
value1=GetField("漲停價","D");
if trueany(close=value1,day)
//近十日有一天漲停
and close<close[30]*1.2
//近三十日漲幅不到兩成

then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/漲勢加速.xs

```xs
{@type:filter}
setbarfreq("AD");
 
variable:aspeed(0),dspeed(0),a1(0),d1(0),p1(0),ap1(0);
if close>close[1] then aspeed=(close-close[1])/close*100
else aspeed=0;
if close<close[1] then dspeed=(close[1]-close)/close*100
else dspeed=0;

a1=average(aspeed,5);
d1=average(dspeed,5);

p1=a1-d1;
ap1=average(p1,9);

if p1 crosses over ap1
and rsi(close,6)<=75
and close*1.3<close[30]

then ret=1;

outputfield(1, nthlowest(1,low[1],9), 2, "近期低點", order := -1);
```

---


---

## 腳本檔案: 選股/04.價量選股/漲勢成形.xs

```xs
{@type:filter}
Value1=linearregslope(close,3);
value2=linearregslope(close,5);
value3=linearregslope(close,20);

settotalbar(23);

if 
	value1 > value2 and 
	value2 > value3 and 
	value1 > value1[1] and 
	value1[1] > value1[2] and 
	value1 > 0.3 and 
	value3[2] < 0.1 and 
	value3 > 0
then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/漲勢變強.xs

```xs
{@type:filter}
input: Length(100);		setinputname(1,"計算期數");
input: RRatio(100);		setinputname(2,"盤漲最大漲幅%");

settotalbar(3);

variable: Scores(0);

if Close > Open and Close > Close[2]*1.07  {紅棒且累計三天漲幅大於7%}
   and Close < Close[Length]*(1+RRatio/100)  {累計漲幅不超過%}
then 
  begin
	scores = countif(close > close[1], length);
	If scores >= Length / 2 then ret=1;
  end;
```

---


---

## 腳本檔案: 選股/04.價量選股/漲多後跌破頭部.xs

```xs
{@type:filter}
input:ratio(50);
input:period(100);
setinputname(1,"波段漲幅");
condition1=false;
value1=highestbar(close,period);//波段最高價距今幾根bar
value2=lowest(close[1],value1);
if value1>5 and close>close[100]*(1+ratio/100)
and close crosses under value2
then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/炒高後無量反轉下跌.xs

```xs
{@type:filter}
setbarfreq("AD");

input: Periods(150,"計算期數");
input: Ratio(20,"期間漲幅%");

if close < close[4]
and close*1.1>highest(close,periods)
//離最高不到一成
and close >= close[Periods] *(1 + Ratio*0.01)
//過去半年漲幅超過五成
and average(volume[1],5)*1.5 < average(volume[1],20)
//最近幾天成交量大幅縮小
then ret=1;

outputfield(1,highest(close,periods),2,"波段高點", order := -1);
```

---


---

## 腳本檔案: 選股/04.價量選股/無量變有量.xs

```xs
{@type:filter}
input:v1(1000,"前一期成交量");
input:v2(1000,"最新期成交量");
if trueall(volume[1]<=v1,10) and volume>v2 
then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/特定日期迄今漲跌幅超過一定幅度.xs

```xs
{@type:filter}
input:startdate(20160203);
input:ratio(15,"漲幅下限");

value1=getbaroffset(startdate);
value2=rateofchange(close,value1);

if value2>ratio
then ret=1;

outputfield(1,value2,1,"區間漲跌幅");
outputfield(2,GetField("股價淨值比","D"),2,"股價淨值比");
outputfield(3,GetField("月營收年增率","M"),2,"月營收年增率");
outputfield(4,GetField("本益比","D"),1,"本益比");
```

---


---

## 腳本檔案: 選股/04.價量選股/盤整N日後突破.xs

```xs
{@type:filter}
input:period(20,"盤整的天數");
input:ratio(5,"盤整的最大波動範圍");

if highest(close,period)[1]<lowest(close,period)[1]*(1+ratio/100)
and close > highest(close,period)[1]
and volume >average(volume,period)
and volume>2000
then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/站在五十二週高點之上.xs

```xs
{@type:filter}
value1=GetField("最高價","w");
value2=highest(value1[1],52);
if close>value2 then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/總市值跌到歷年低點.xs

```xs
{@type:filter}
setbarfreq("Y");
settotalbar(8);

value1=GetField("總市值","Y");
value2=lowest(value1,8);
if value1<value2*1.1
then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/股價超過N日未再破底.xs

```xs
{@type:filter}
input:period(30);
input:day(10);
setinputname(1,"計算期間");
setinputname(2,"未破底天數");
value1=lowestbar(low,period);
if value1>day
then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/行業轉強個股也轉強.xs

```xs
{@type:filter}
input:period(20,"計算區間");
setbarfreq("D");
settotalbar(20);

value1=GetField("同業股價指標","D");
value2=GetField("佔全市場成交量比","D");

if value1=highest(value1,period)
and value2=highest(value2,period)
then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/跌到52週低點之下.xs

```xs
{@type:filter}
setbarfreq("W");

if close<lowest(low[1],52) then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/週線二連紅.xs

```xs
{@type:filter}
SetBarFreq("AW");

if rateofchange(close,2)[1]>0 and rateofchange(close,2)[2]>0
and close<close[2]*1.07
and close[10]>close*1.2
then ret=1;

outputfield(1,close[2],2,"前波低點", order := -1);
```

---


---

## 腳本檔案: 選股/04.價量選股/過去M日有N日HHLL.xs

```xs
{@type:filter}
input:days(5,"計算天期");
input:occurrence(2, "發生次數");

condition1= high>high[1] and low>low[1] ;
value1=countif(condition1,days);
if value1>=occurrence then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/過去N日價穩量縮.xs

```xs
{@type:filter}
input:days(10,"計算期間");
input:vhilimit(1000,"量的上限");
input:philimit(5,"價格波動上限");
setbarfreq("D");
settotalbar(days);

value1=highest(high,days);
value2=lowest(low,days);
value3=(value1-value2)/value2*100;
if trueall(volume<vhilimit,days)
and trueall(value3<philimit,days)
then ret=1;
```

---


---

## 腳本檔案: 選股/04.價量選股/量價背離.xs

```xs
{@type:filter}
input:length(10);		setinputname(1,"計算區間");

settotalbar(length + 3);

value1 = average(close,length);
value2 = average(volume,length);
value3 = linearregslope(value1,length);
value4 = linearregslope(value2,length);

if value2 > 1000 and value3 < 0 and value4 > 0
then ret=1;
```

---


---

## 腳本檔案: 選股/05.型態選股/三次到頂而破.xs

```xs
{@type:filter}
input: BoxRangePercents(7); setinputname(1,"定義整理區間幅度");
input: HighAreaPercents(1.5); setinputname(2,"定義區間高檔範圍");
variable: BoxHigh(0);

variable:period(10),MaxPeriod(40);

period = 10;
while period < Maxperiod and
	highest(high[1],period) < lowest(low[1],period) *(1+BoxRangePercents/100)
begin period +=1; end;

if period < MaxPeriod then
begin
	BoxHigh = highest(High[1],period); {區間高點}

	if Close > BoxHigh   and  {突破整理區間高點}
	   NthHighest(3,High[1],period) > BoxHigh*(1-HighAreaPercents/100)
	   {昨天以前第3個高點也在高檔區間,即曾經攻高3次}
	   then ret=1;
end;
```

---


---

## 腳本檔案: 選股/05.型態選股/上昇旗形.xs

```xs
{@type:filter}
setbarfreq("AD");

input:period(20,"計算區間");

value2=nthhighest(1,high[1],period);//最高價
value3=nthhighest(2,high[1],period);//第二高價
value4=nthhighest(3,high[1],period);//第三高價
value5=nthhighestbar(1,high[1],period);//最高價距今幾根bar
value6=nthhighestbar(2,high[1],period);//第二高價距今幾根bar
value7=nthhighestbar(3,high[1],period);//第三高價距今幾根bar

condition1=false;
condition2=false;

if value6-value5>3 and value7-value6>3
then condition1=true;//三個高點沒有連在一起，且是愈來愈高

if maxlist(value2,value3,value4)<minlist(value2,value3,value4)*1.07
then condition2=true;//三個高點沒有差多少

 
if condition1 and condition2  
and close crosses over value2
and close[period]*1.05<value2
then ret=1;

outputfield(1, value2, 2, "前波高點", order := -1);
```

---


---

## 腳本檔案: 選股/05.型態選股/下跌後的吊人線.xs

```xs
{@type:filter}
setbarfreq("AD");

condition1=false;
condition2=false;
condition3=false;

if high<= maxlist(open, close)*1.01	
//狀況1:小紅小黑且上影線很小
then condition1=true;

if (close-low)> absvalue(open-close)*2 and (close-low)>close*0.02
//狀況2:下影線為實體兩倍以上
then condition2=true;

if highest(high,30)>close[1]*1.4
//狀況3:近30日來最高點到昨天跌幅超過40%
then condition3=true;
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3

THEN	RET=1;	

outputfield(1,high,2,"K棒高點", order := -1);
```

---


---

## 腳本檔案: 選股/05.型態選股/下降趨勢改變.xs

```xs
{@type:filter}
input:Length(20); 		setinputname(1,"下降趨勢計算期數");
input:VolLimit(1000);	setinputname(2,"突破量");

variable: kk(0);

settotalbar(maxlist(length, 5) + 3);

If CurrentBar = 1 then
	kk = 0
else
	kk = kk[1] + (close - close[1])/close[1] * Volume;

value1 = linearregslope(kk, Length);
value2 = linearregslope(kk, 5);

IF value1 < 0 and value2 > 0 AND VOLUME > VolLimit then ret=1;
```

---


---

## 腳本檔案: 選股/05.型態選股/下降趨勢明確.xs

```xs
{@type:filter}
input:Length(20,"期間");   //"計算期間"
settotalbar(20);

LinearReg(close, Length, 0, value1, value2, value3, value4);
//做收盤價20天線性回歸
{value1:斜率,value4:預期值}

value5=rsquare(close,value4,20);
//算收盤價與線性回歸值的R平方

if value1<0 and value5>0.2
then ret=1;
```

---


---

## 腳本檔案: 選股/05.型態選股/做M頭的股票.xs

```xs
{@type:filter}
input:day(60,"計算區間");//設定計算區間
input:GP(30,"波段漲幅下限");//設定波段漲幅下限，單位是%
input:pc(2,"M頭兩高點價差上限");//設定M頭兩高點價差上限，單位是%
input:rg(30,"波段低點到高點的最少天數");//波段低點到高點的最少天數
input:bc(4,"M谷底距離頭部最低跌幅");//M谷底距離頭部最低跌幅，單位是%

value1=highest(high,day);//找出波段最高點
value2=lowest(low,day);//找出波段最低點
value3=nthhighest(2,high,day);//波段第二高點
value4=nthhighestbar(1,high,day);//最高價在距今第幾根bar
value5=nthlowestbar(1,low,day);//最低價在距今第幾根bar
value6=nthhighestbar(2,high,day);//第二價在距今第幾根bar
value7=lowest(low,maxlist(value4,value6));//從第一個M頭以來的最低點
value8=nthlowestbar(1,low,maxlist(value4,value6));//谷底距今第幾根bar
condition1=false;
condition2=false;
condition3=false;
condition4=false;

if value1>value2*(1+gp/100) then condition1=true;//波段漲幅超過30%
if value5>maxlist(value4,value6)+rg then condition2=true;//低點在圖左邊
if value1<=value3*(1+pc/100) then condition3=true;//兩個高點之間的價差不大
if value8>minlist(value4,value6) and value8<minlist(value4,value6)
then condition4=true;//谷底在兩頭之間

if condition1 and condition2 and condition3 and condition4  
then ret=1;
```

---


---

## 腳本檔案: 選股/05.型態選股/在上昇趨勢中的股票.xs

```xs
{@type:filter}
input:Length(20,"期間");   //"計算期間"
settotalbar(20);

LinearReg(close, Length, 0, value1, value2, value3, value4);
//做收盤價20天線性回歸
{value1:斜率,value4:預期值}

value5=rsquare(close,value4,20);
//算收盤價與線性回歸值的R平方

if value1>0 and value5>0.2
then ret=1;
```

---


---

## 腳本檔案: 選股/05.型態選股/平台整理後突破.xs

```xs
{@type:filter}
setbarfreq("AD");

input:Period(20, "平台區間");
input:ratio(10, "整理幅度(%)");
input:ratio1(3,"各高點(低點)間的差異幅度");

variable:h1(0),h2(0),L1(0),L2(0);

h1=nthhighest(1,high[1],period);
h2=nthhighest(4,high[1],period);
l1=nthlowest(1,low[1],period);
l2=nthlowest(4,low[1],period);

if (h1-l1)/l1<=ratio/100
  and (h1-h2)/h2<=ratio1/100
  and (l2-l1)/l1<=ratio1/100
  and close crosses over h1
  and close[period+30]*1.1<h1
  and volume> average(volume,period)
then ret=1;

outputfield(1, h1, 2, "區間高點", order := -1);
```

---


---

## 腳本檔案: 選股/05.型態選股/平台整理後跌破.xs

```xs
{@type:filter}
setbarfreq("AD");

input:Period(15, "平台區間");
input:ratio(7, "整理幅度(%)");
input:ratio1(2,"各高點(低點)間的差異幅度");

variable:h1(0),h2(0),L1(0),L2(0);

h1=nthhighest(1,high[1],period);
h2=nthhighest(4,high[1],period);
l1=nthlowest(1,low[1],period);
l2=nthlowest(4,low[1],period);
 
if (h1-l1)/l1<=ratio/100
and (h1-h2)/h2<=ratio1/100
and (l2-l1)/l1<=ratio1/100
and close crosses below l1
and close[period+30]>l1*1.1
then ret=1;

outputfield(1, l1, 2, "區間低點", order := -1);
```

---


---

## 腳本檔案: 選股/05.型態選股/突破下降旗型.xs

```xs
{@type:filter}
input: Length(100);		Setinputname(1, "區間");
input: UpRatio(2);		SetInputName(2, "當日上漲幅度%");
input: VolLimit(300);	SetInputName(3, "當日成交量下限");

variable: hDate(date),day(0),KeyPrice(0),HighPrice(0);

settotalbar(Length + 3);

if high = highest(high,Length) then hDate = date;

day = datediff(date,hdate);

if day =0 and day[1] > 0 then KeyPrice = Close;

if day >0 and day[1] = 0 then HighPrice = High;

if KeyPrice > 0 and HighPrice > 0 and day > 2 and day <= Length / 2 and 
	Close > Open * (1 + 0.01 * UpRatio) and 
	Close >= highest(High,3) and
	volume > VolLimit and 
	Close > KeyPrice and 
	Close < HighPrice  
then ret=1;
```

---


---

## 腳本檔案: 選股/05.型態選股/突破整理格局.xs

```xs
{@type:filter}
input:limit1(7);		setinputname(1,"定義整理的區間幅度");
input:limit2(2);		setinputname(2,"定義三個頂點間的差距");
input:rangemax(30);		setinputname(3,"整理區間最長日期限制");
input:vollimit(500);	setinputname(4,"突破時成交量最小值");

variable: period(0);

SetTotalBar(rangemax + 3);

period = 5;
repeat
 begin
	value1=simplehighest(high[1],period);
	value2=simplelowest(low[1],period);
	period=period+1;
 end;	
until period >= rangemax or (value1 > value2 * (1 + limit1/100));

if period < rangemax
then
  begin
	value3=nthhighest(1, high[1], period);
	value4=nthhighest(3, high[1], period);

	if value3 <= value4 * (1 + limit2/100) and 
	   close crosses over value3 and
	   volume > vollimit
	then ret=1;
  end;
```

---


---

## 腳本檔案: 選股/05.型態選股/突破箱型.xs

```xs
{@type:filter}
input:period(20);
input:rangeratio(10);
variable:h1(0),h2(0),l1(0),l2(0),hd1(0),hd2(0),ld1(0),ld2(0);
h1=nthhighest(1,high,period);
h2=nthhighest(2,high,period);
l1=nthlowest(1,low,period);
l2=nthlowest(2,low,period);
hd1=nthhighestbar(1,high,period);
hd2=nthhighestbar(2,high,period);
ld1=nthlowestbar(1,low,period);
ld2=nthlowestbar(2,low,period);
if absvalue(hd1[1]-hd2[1])>=4 and absvalue(ld1[1]-ld2[1])>=4
and h1[1]-h2[1]<=h1[1]*0.02
and l2[1]-l1[1]<=l1[1]*0.02
and h1[1]<=l1[1]*(1+rangeratio/100)
then begin
if close crosses over h1[1]
and volume >=average(volume,period)*1.3
then ret=1;
end;
```

---


---

## 腳本檔案: 選股/05.型態選股/突破繼續型態.xs

```xs
{@type:filter}
setbarfreq("AD");

variable:iHigh(0); iHigh=maxlist(iHigh,H);
variable:iLow(100000); iLow=minlist(iLow,L);
variable:hitlow(0),hitlowdate(0);
//觸低次觸與最後一次觸低日期
if iLow = Low then begin
	hitlow+=1;
	hitlowdate =date;
end;

if DateAdd(hitlowdate,"M",2) < Date and//如果自觸低點那天1個月後都沒有再觸低
iHigh/iLow < 1.3 and //波動在三成以內
iHigh = High
//來到設定日期以來最高點
then ret =1;

outputfield(1, highest(high[1],100), 2, "前波高點", order := -1);
```

---


---

## 腳本檔案: 選股/05.型態選股/突破股票箱.xs

```xs
{@type:filter}
input:length(12);		setinputname(1, "股票箱區間長度");
input:boxrange(10);		setinputname(2, "箱區高低範圍(%)");
	
settotalbar(3);	
	
value1=NthHighest(1,high,length);
value3=nthhighest(3,high,length);
value4=Nthlowest(1,low,length);
value5=nthlowest(3,low,length);

if 
  value1[1] <= 1.03 * value3[1] and 
  value5[1] <= 1.03 * value4[1] and 
  value1[1] <= (1 + 0.01 * boxrange) * value4[1] and 
  close > value1[1]
then ret=1;
```

---


---

## 腳本檔案: 選股/05.型態選股/跌勢後的內困三日翻紅.xs

```xs
{@type:filter}
setbarfreq("AD");

If close[4]=lowest(close,20)
and close[4]*1.2<=close[24]
and open[3]>close[3]*0.01
And close[2]>open[2]*0.01
And close[1]>open[1]*0.01
And close>high[4]
and volume>average(volume,5)
and average(volume,100)>=1000

Then
ret=1;

outputfield(1,close[4],2,"前波低點", order := -1);
```

---


---

## 腳本檔案: 選股/05.型態選股/近期漲幅不大.xs

```xs
{@type:filter}
input:period(20,"計算區間");
input:ratio(7,"最低漲跌幅");

if close[period-1]<>0
and (close/close[period-1]-1)*100<ratio
then ret=1;

outputfield(1,GetField("法說會日期"),0,"法說會日期", order := -1);
```

---


---

## 腳本檔案: 選股/05.型態選股/長時間未破底後創新高.xs

```xs
{@type:filter}
setbarfreq("AD");

input:period(90,"未破底區間");
input:percent(25,"盤整區間漲幅上限");

condition1=false;
condition2=false;
value1=lowest(low,period);
if value1=low[period-1]
then condition1=true;

if highest(high[1],period)<=value1*(1+percent/100)
then condition2=true;

if condition1 and condition2 and close crosses over highest(close[1],period)
then ret=1;

outputfield(1,value1,2,"前波低點", order := -1);
```

---


---

## 腳本檔案: 選股/05.型態選股/長紅.xs

```xs
{@type:filter}
if close>=open*1.035
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/N日以來投信曾大買過.xs

```xs
{@type:filter}
input:period(250,"計算期間");
input:days(5,"計算買進的天數");
input:amount(3000,"大買的最低張數");
setbarfreq("D");
settotalbar(period+days);

value1=GetField("投信買張");
value2=summation(value1,days);
if countif(value2>=amount,period)>=1
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/N日內三大法人曾同步買超.xs

```xs
{@type:filter}
input:days(20,"計算天期");
setbarfreq("D");
settotalbar(days+1);

value1=GetField("外資買賣超","D");
value2=GetField("投信買賣超","D");
value3=GetField("自營商自行買賣買賣超","D");
condition1=value1>0 and value2>0 and value3>0;
if barslast(condition1)<days
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/不明買盤介入.xs

```xs
{@type:filter}
input:period(5);	setinputname(1,"均線期間");
input:ratio(30);	setinputname(2,"不明買盤比重%");

settotalbar(period + 7);

value1=GetField("法人買張","D");
value2=GetField("資券互抵張數","D");
value3=GetField("散戶買張","D");
value4=volume - value1 - value2 - value3;
value5=value4*100/volume;	// 不明買盤的比重
value6=average(value5,period);

if value6 crosses over ratio
then ret=1;

SetOutputName1("不明買盤比重(%)");
OutputField1(value5);
```

---


---

## 腳本檔案: 選股/06.籌碼選股/主力偷偷調節後下殺.xs

```xs
{@type:filter}
setbarfreq("AD");

input:period(10,"籌碼計算天期");
 
Value1=GetField("分公司買進家數","D");
value2=GetField("分公司賣出家數","D");
value3=(value1-value2);
//買進家數減去賣出家數，代表籌碼發散的情況
value4=average(close,5);
//計算發散程度的五日移動平均
 
if period<>0 then begin
	if countif(value3>10, period)/period >0.6
	//區間裡超過六成以上的日子主力都是站在出貨那一邊
	and linearregslope(value4,5)>0
	//發散程度之五日移動平均線短期趨勢是向上
	then ret=1;
end;

outputfield(1, countif(value3>10, period), 0, "出貨天數", order := 1);
```

---


---

## 腳本檔案: 選股/06.籌碼選股/主力公司派可能出貨中.xs

```xs
{@type:filter}
input:Period(5);	setinputname(1,"近期偏弱期間");
input:Rate1(1000);	setinputname(2,"法人及散戶合計賣出上限");
input:Rate2(5000);	setinputname(3,"成交量下限");
input:Ratio(1); 	setinputname(4,"接近低點幅度");

SetTotalBar(3);
 
if Close < Close[Period] and  {近期股價累計為下跌}
   Close < Lowest(Low,Period)* (1+Ratio/100) and {接近期間低點}
   Average(Volume,Period) > Rate2    {偏弱期間均量大於成交量下限}
then 
  begin  
	value1= GetField("法人持股","D") - GetField("法人持股","D")[Period]; {期間法人累計買賣超}
	value2= GetField("融資餘額張數","D") - GetField("融資餘額張數","D")[Period] ; {期間融資累計增減}
	value3= GetField("融券餘額張數","D") - GetField("融券餘額張數","D")[Period];{期間融券累計增減}
 
	if value1 + value2 -value3 >  Rate1 * -1 then ret=1;
  end;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/主力慢慢收集籌碼後攻堅.xs

```xs
{@type:filter}
setbarfreq("AD");

input:period(10,"籌碼計算天期");
 
Value1=GetField("分公司買進家數","D");
value2=GetField("分公司賣出家數","D");
value3=(value2-value1);
//賣出的家數比買進家數多的部份
value4=average(close,5);

if period<>0 then begin
   if countif(value3>30, period)/period >0.7
   then ret=1;
end;

outputfield(1, countif(value3>30, period), 0, "進貨天數", order := 1);
```

---


---

## 腳本檔案: 選股/06.籌碼選股/主力發動股.xs

```xs
{@type:filter}
//成交量 連續 3 日遞減
//股價 > 20日均線 10%

if volume<volume[1] 
and volume[1]<volume[2]
and close>average(close,20)*1.1
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/主力買超超過門檻.xs

```xs
{@type:filter}
input: Length(5); 	setinputname(1,"計算天數");
input: limit1(20);	setinputname(2,"買超佔成交量比例");

variable: r1(0), volTotal(0),ratio(0);

SetTotalBar(3);

r1 = summation(GetField("主力買賣超張數"), Length);
volTotal = summation(Volume, Length);

if voltotal<>0 then 
  begin
	ratio = r1 / voltotal * 100;
    if ratio >= limit1 and average(volume,20) > 500 then ret=1;
	
	setoutputname1("主力買賣超比重(%)");
	outputfield1(ratio);
  end;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/主力長期收集.xs

```xs
{@type:filter}
input:period(60,"計算區間");
setbarfreq("D");
settotalbar(period);

value1=GetField("分公司買進家數","D");
value2=GetField("分公司賣出家數","D");
condition1=false;
if countif(value1<value2,period)>period/2
then condition1=true;

if condition1
and close>open*1.035
and GetField("主力買賣超張數","D")>0
and summation(GetField("主力買賣超張數","D"),5)>0
and summation(GetField("主力買賣超張數","D"),20)>0
and summation(GetField("主力買賣超張數","D"),60)>0
and summation(GetField("主力買賣超張數","D"),120)>0
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/主流股蓄勢待發.xs

```xs
{@type:filter}
input:days(10);
input: FastLength(12, "DIF短期期數"), SlowLength(26, "DIF長期期數"), MACDLength(9, "MACD期數");
variable: difValue(0), macdValue(0), oscValue(0),Kprice(0);

settotalbar(100);
MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);
if absvalue((average(close,20)-close)/close)*100<2
and absvalue((average(close,60)-close)/close)*100<2
and close=highest(close,days)
and macdvalue>macdvalue[1]
and macdvalue>0
and difvalue>0
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/交易家數暴增.xs

```xs
{@type:filter}
value1=GetField("分公司交易家數","D");
value2=highest(GetField("分公司交易家數","D")[1],20);
if value1-value2>150
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/借券增.xs

```xs
{@type:filter}
input:lowlimit(200,"借券增加張數");
input:days(3,"計算天數");
setbarfreq("D");
settotalbar(3);

value1=GetField("借券賣出餘額張數","D")-GetField("借券賣出餘額張數","D")[days];//借券賣出餘額張數增加數
if value1>=lowlimit
then ret=1;

outputfield(1,value1,"借券賣出餘額張數增加數");
```

---


---

## 腳本檔案: 選股/06.籌碼選股/借券賣出餘額張數大減.xs

```xs
{@type:filter}
input: amount(1000);		setinputname(1, "減少張數");

SetTotalBar(3);

value1 = GetField("借券賣出餘額張數");
if value1[1] - value1 > amount
then ret=1;

setoutputname1("借券賣出減少張數");
outputfield1(value1[1] - value1);
```

---


---

## 腳本檔案: 選股/06.籌碼選股/再跌就有斷頭賣壓的股票.xs

```xs
{@type:filter}
setbarfreq("AD");

input:period(30, "波段天期");

value2=nthhighestbar(1,close,period);//波段高點在第幾根Bar
if GetField("融資餘額張數","D")>average(volume,5)
//融資餘額大於五日均量
and GetField("融資餘額張數","D")[value2]>10000
//融資餘額大於一萬張
and GetField("融資餘額張數","D")[value2]>10000
//最高點時融資餘額也大於一萬張
and close*1.2<=close[value2]//波段跌幅超過兩成
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/券增價漲.xs

```xs
{@type:filter}
input: Length(10); setinputname(1,"近期天數");
input: UpRatio(3.5); setinputname(2, "上漲幅度(%)");

settotalbar(3);

if RateOfChange(Close, 1) >= UpRatio and
	Getfield("融券餘額張數") > 0 and
	Getfield("融券餘額張數") = highest(Getfield("融券餘額張數"), Length)  
then ret=1;

SetOutputName1("融券餘額張數");
OutputField1(Getfield("融券餘額張數"));
```

---


---

## 腳本檔案: 選股/06.籌碼選股/券補力道超過一定值.xs

```xs
{@type:filter}
value1=GetField("融券餘額張數","D");
input:lowlimit(100,"券補力道下限");
if value1/average(volume,5)*100>lowlimit
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/千張大戶增加而散戶減少.xs

```xs
{@type:filter}
setbarfreq("W");
settotalbar(3);

condition1 = GetField("大戶持股人數","W",param:=1000)>GetField("大戶持股人數","W",param:=1000)[1];
condition2 = GetField("散戶持股人數","W",param:=400)<GetField("散戶持股人數","W",param:=400)[1];

if condition1 and condition2 then ret=1;

outputfield(1,GetField("大戶持股人數","W",param:=1000),0,"本週大戶人數");
outputfield(2,GetField("大戶持股人數","W",param:=1000)[1],0,"上週大戶人數");
outputfield(3,GetField("大戶持股人數","W",param:=1000)-GetField("大戶持股人數","W",param:=1000)[1],0,"大戶增加數");
outputfield(4,GetField("散戶持股人數","W",param:=400),0,"本週散戶人數");
outputfield(5,GetField("散戶持股人數","W",param:=400)[1],0,"上週散戶人數");
outputfield(6,GetField("散戶持股人數","W",param:=400)-GetField("散戶持股人數","W",param:=400)[1],0,"散戶減少數");
```

---


---

## 腳本檔案: 選股/06.籌碼選股/千張大戶增持.xs

```xs
{@type:filter}
input: ratio(10, "增加比例%");

setbarfreq("W");
settotalbar(3);

if GetField("大戶持股比例","W",param:=1000) > (GetField("大戶持股比例","W",param:=1000)[1] * (1 + ratio/100)) then ret=1;

outputfield(1, GetField("大戶持股比例","W",param:=1000), 2, "大戶比例");
outputfield(2, GetField("大戶持股比例","W",param:=1000)[1], 2, "大戶比例[1]");
```

---


---

## 腳本檔案: 選股/06.籌碼選股/千張大戶減少而散戶增加.xs

```xs
{@type:filter}
setbarfreq("W");
settotalbar(3);

condition1 = GetField("大戶持股人數","W",param:=1000)<GetField("大戶持股人數","W",param:=1000)[1];
condition2 = GetField("散戶持股人數","W",param:=400)>GetField("散戶持股人數","W",param:=400)[1];

if condition1 and condition2 then ret=1;

outputfield(1,GetField("大戶持股人數","W",param:=1000),0,"本週大戶人數");
outputfield(2,GetField("大戶持股人數","W",param:=1000)[1],0,"上週大戶人數");
outputfield(3,GetField("大戶持股人數","W",param:=1000)-GetField("大戶持股人數","W",param:=1000)[1],0,"大戶減少數");
outputfield(4,GetField("散戶持股人數","W",param:=400),0,"本週散戶人數");
outputfield(5,GetField("散戶持股人數","W",param:=400)[1],0,"上週散戶人數");
outputfield(6,GetField("散戶持股人數","W",param:=400)-GetField("散戶持股人數","W",param:=400)[1],0,"散戶增加數");
```

---


---

## 腳本檔案: 選股/06.籌碼選股/增資股即將出籠.xs

```xs
{@type:filter}
setbarfreq("AD");

value1=GetField("現增新股上市日");
value2=GetField("現增比率");//每千股可認股數
value3=GetField("現增價格");
value4=GetField("融券餘額張數","D");
value5=GetField("普通股股本","Q");//單位:億

if value1>date and datediff(value1,date)<10//增資股快上市了
and value5*10000*value2/1000>2000//增資張數大於5000張
and value4[30]>value4-1000//近一個月融券增加沒有超過1000張
and value3*1.1<close//股價仍比現增價格高超過一成
then ret=1;

outputfield(1,value1,0,"新股上市日", order := -1);
outputfield(2,value2,2,"現增比率");
outputfield(3,close-value3,2,"現增價差");
```

---


---

## 腳本檔案: 選股/06.籌碼選股/外資完全不碰的股票有人在收籌碼.xs

```xs
{@type:filter}
input: period(5);				setinputname(1, "計算期間");
input: investorLimit(2000);		setinputname(2, "外資持股上限");
input: ratio(50);				setinputname(3, "主力買張比重(%)");
input: volLimit(500);			setinputname(4, "成交均量下限");

SetTotalBar(3);

// 主力買張比重
value1 = summation(GetField("主力買張","D"), period);
value2 = summation(volume, period);
value3 = value1 / value2 * 100;

if GetField("外資持股","D") < investorLimit and value3 > ratio and value2 > volLimit * period  
then ret=1;

SetOutputName1("主力買張比重(%)");
OutputField1(value3);
```

---


---

## 腳本檔案: 選股/06.籌碼選股/外資拉抬.xs

```xs
{@type:filter}
input: Length(10); setinputname(1,"計算天數");
input: UpRatio(3.5); setinputname(2, "上漲幅度(%)");
input: VolumeRatio(5); setinputname(3, "買超佔比例(%)");

variable: SumForce(0);
variable: SumTotalVolume(0);

settotalbar(3);

if RateOfChange(Close, 1) >= UpRatio then
begin
	SumTotalVolume = Summation(volume, Length);
	SumForce = Summation(GetField("外資買賣超"), Length);
	if SumForce > SumTotalVolume * VolumeRatio / 100 then ret =1;
end;

SetOutputName1("外資累計買超張數");
OutputField1(SumForce);
```

---


---

## 腳本檔案: 選股/06.籌碼選股/外資由空翻多.xs

```xs
{@type:filter}
setbarfreq("D");
settotalbar(3);

if summation(GetField("外資買賣超","D"),20)<0
and trueall(GetField("外資買賣超","D")>200,3)
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/外資買超後隔天會漲的機率很高的股票.xs

```xs
{@type:filter}
input:n(500,"樣本數");
settotalbar(n);
value1=GetField("外資買賣超","D");
variable:x1(0),y(0),c1(0),c2(0),c3(0);
if value1[1]>200 
then begin
x1=1;
c1=c1+1;
//外資買超的次數
end
else x1=0;

if close>open
then begin
y=1;
c2=c2+1;
//上漲的次數
end
else y=0;

if value1[1]>200
and close>open
then c3=c3+1;
//上漲且外資買超的次數

value2=c1/n; //外資買超的機率
value3=c2/n; //上漲的機率
value4=c3/c2;//收紅且外資買超的機率
value5=value4*value3/value2;
if countif(value1[1]>200,n)>20
then ret=1;
outputfield(1,value5*100,0,"外資前一日買超隔天收高的機率");
outputfield(2,c1,0,"上漲次數");
outputfield(3,c2,"外資買超次數");
outputfield(4,c3,0,"上漲且外資買超");
```

---


---

## 腳本檔案: 選股/06.籌碼選股/大跌後法人散戶清浮額.xs

```xs
{@type:filter}
input:period(10);	setinputname(1,"計算跌幅區間");
input:percent1(10);	setinputname(2,"區間最小跌幅");

settotalbar(3);

value1=GetField("法人買賣超張數");
value2=GetField("融資增減張數");

if close[period-1] >= close*(1+percent1/100) and 
   value1 < 0 and 
   value2 < 0 and 
   close > close[1]
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/官股買超比重.xs

```xs
{@type:filter}
input: lowlimit(30, "官股買超比重(%)");

value1 = getfield("官股券商買賣超張數", "D");
if value1 > 0 then begin
	value2 = value1 * 100 / volume;
	if value2 >= lowlimit then ret=1;
end;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/投信從空手到開始佈局.xs

```xs
{@type:filter}
input: r1(500);		setinputname(1,"先前買超上限張數");
input: r2(5000);	setinputname(2,"近一日買超金額下限(萬元)");
input: length(20);	setinputname(3,"投信布局天數");

setTotalBar(3);

if trueall(GetField("投信買賣超","D")[1] < r1, length) and 
   GetField("投信買賣超","D") * close > r2 * 10
then ret=1;

SetOutputName1("投信買賣超(張)");
OutputField1(GetField("投信買賣超","D"));
```

---


---

## 腳本檔案: 選股/06.籌碼選股/投信拉抬.xs

```xs
{@type:filter}
input: Length(10); setinputname(1,"計算天數");
input: UpRatio(3.5); setinputname(2, "上漲幅度(%)");
input: VolumeRatio(5); setinputname(3, "買超佔比例(%)");

variable: SumForce(0);
variable: SumTotalVolume(0);

settotalbar(3);

if RateOfChange(Close, 1) >= UpRatio then
begin
	SumTotalVolume = Summation(volume, Length);
	SumForce = Summation(GetField("投信買賣超"), Length);
	if SumForce > SumTotalVolume * VolumeRatio / 100 then ret =1;
end;

SetOutputName1("投信累計買超張數");
OutputField1(SumForce);
```

---


---

## 腳本檔案: 選股/06.籌碼選股/投信持股從無到有.xs

```xs
{@type:filter}
input: v1(2000);	setinputname(1, "投信估計持股上限(張)");
input: v2(300);		setinputname(2, "近一日買賣超(張)");

value1=GetField("投信持股","D");
value2=GetField("投信買賣超","D");

if value1 < v1 and value2 > v2
then ret=1;

SetOutputName1("投信買賣超(張)");
OutputField1(value2);
```

---


---

## 腳本檔案: 選股/06.籌碼選股/投信掃貨.xs

```xs
{@type:filter}
input: pastDays(5); 		setinputname(1,"計算天數");
input: _BuyRatio(10); 		setinputname(2,"買超佔比例(%)");

variable: SumForce(0);
variable: SumTotalVolume(0);

SetTotalBar(3);

SumForce = Summation(GetField("投信買賣超"), pastDays);
sumTotalVolume = Summation(Volume, pastDays);
value1 = SumForce / SumTotalVolume * 100;
if value1 > _BuyRatio then ret =1;

SetOutputName1("買超佔比例(%)");
OutputField1(value1);
```

---


---

## 腳本檔案: 選股/06.籌碼選股/投信爭買的小型成長股.xs

```xs
{@type:filter}
input: miniratio(10); 	setinputname(1,"投信買進佔今日總量%");
input: lv(5000); 		setinputname(2,"投信持股張數上限");
input: holdratio(10); 	setinputname(3,"投信持股比例上限%");

SetTotalBar(3);

value1=GetField("投信買張");			//投信買張
value2=GetField("投信持股");			//投信持股
value3=GetField("投信持股比例");		//投信持股比例 

if  
   value1 > volume * miniratio*0.01 and //買進張數/成交量 >= minratio
   value2 < lv and 						//原來庫存低
   value3 < holdratio and 				//原來庫存低
   GetField("公司類別","M") = "小型股" 	//小型股
then ret=1;

SetOutputName1("投信買張");
OutputField1(value1);
```

---


---

## 腳本檔案: 選股/06.籌碼選股/投信第一天大買進.xs

```xs
{@type:filter}
value1=GetField("最新股本");//單位:億
value2=GetField("投信買張","D");
value3=value2*close/10;  //單位:萬}

 
 
condition1=value3>200 and value1<80;
 
condition2=filter(condition1,5);

if condition2 
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/散戶買進比例上揚.xs

```xs
{@type:filter}
Input: r1(50);	setinputname(1, "散戶買進比例下限(%)");
Input: r2(500);	setinputname(2, "五日均量下限(張)");

SetTotalBar(28);

value1=GetField("散戶買張");
value2=value1/volume*100;		// 散戶買張比例
value3=average(value2,5);		// 短期散戶比例
value4=average(value2,20);		// 長期散戶比例

if value2 > r1 and
   value3 crosses above value4 and
   average(volume,5) > r2
then ret=1;

SetOutputName1("散戶買進比例(%)");
OutputField1(value2);
```

---


---

## 腳本檔案: 選股/06.籌碼選股/斷頭後的止跌.xs

```xs
{@type:filter}

input:Length(4); setinputname(1,"計算區間");
input:DVOL(3000); setinputname(2,"區間融資減少張數");
input:R1(30);	 setinputname(3,"區間跌幅(%)");	

SetTotalBar(3);

if Close > Close[1] and 
   RateOfChange(Close, Length) < -1 * R1 and
   GetField("融資餘額張數")[Length] - GetField("融資餘額張數") > DVOL 
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/法人主力敢買又敢拉的股票.xs

```xs
{@type:filter}
value1=GetField("法人買賣超張數");
value2=GetField("主力買賣超張數");
value3=value1+value2;
value4=GetField("內外盤比","D");//外盤量/內盤量*100

condition1=false;
condition2=false;
condition3=false;

if countif(value3>300,5)>=4 or countif(value3>300,4)>=3
then condition1=true; 

if value3>volume*0.3 and value4>50
then condition2=true;

if high<=close*1.02
then condition3=true;

if condition1 and condition2 and condition3
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/法人大出籌碼.xs

```xs
{@type:filter}
input:r1(45);
setinputname(1,"法人賣出佔成交量比例下限%");
value1=GetField("外資賣張","D");
value2=GetField("投信賣張","D");
value3=GetField("自營商賣張","D");
if volume<>0 then 
value4=(value1+value2+value3)/volume;
if value4*100>r1
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/法人大買而股價尚未發動.xs

```xs
{@type:filter}
input:day(10);			setinputname(1,"連續買超天數");
input:amount(100);		setinputname(2,"每日至少買超張數(張)");
input:percent1(3);		setinputname(3,"漲幅上限(%)");

SetTotalBar(3);

if trueall(GetField("法人買賣超張數") > amount, day) and 
   RateOfChange(Close, day) < percent1
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/法人淨買超比例高.xs

```xs
{@type:filter}
input:ratio(30);		setinputname(1,"比例下限(%)");
input:period(3);		setinputname(2,"計算區間");
input:volLimit(1000);	setinputname(3,"成交量下限(張)");

settotalbar(3);

value1 = Summation(Volume - GetField("資券互抵張數"), period);
value2 = Summation(GetField("法人買賣超張數"), period);
value3 = value2 / value1 * 100;

if value3 > ratio and volume > volLimit then
ret = 1;

SetOutputName1("近日法人淨買超比例(%)");
OutputField1(value3);
```

---


---

## 腳本檔案: 選股/06.籌碼選股/法人買超.xs

```xs
{@type:filter}
input: Length(10); setinputname(1,"計算天數");
input: UpRatio(3.5); setinputname(2, "上漲幅度(%)");
input: VolumeRatio(5); setinputname(3, "買超佔比例(%)");

variable: SumForce(0);
variable: SumTotalVolume(0);

settotalbar(3);

if RateOfChange(Close, 1) >= UpRatio then
begin
	SumTotalVolume = Summation(volume, Length);
	SumForce = Summation(GetField("法人買賣超張數"), Length);
	if SumForce > SumTotalVolume * VolumeRatio / 100 then ret =1;
end;

SetOutputName1("三大法人累計買超張數");
OutputField1(SumForce);
```

---


---

## 腳本檔案: 選股/06.籌碼選股/法人買超減融資佔成交量比重增加.xs

```xs
{@type:filter}
input: r1(15);				setinputname(1,"籌碼收集比例(%)");
input: volLimit(1000);		setinputname(2,"成交量下限(張)");

settotalbar(3);

value1 = (GetField("法人買賣超張數") - GetField("融資買進張數")) / Volume * 100;

if value1 > r1 and volume > volLimit then
ret = 1;

setoutputname1("法人籌碼收集比例(%)");
outputfield1(value1);
```

---


---

## 腳本檔案: 選股/06.籌碼選股/法人買進佔成交量超過25%.xs

```xs
{@type:filter}
input:r1(45);
setinputname(1,"法人買進佔成交量比例下限%");
value1=GetField("外資買張","D");
value2=GetField("投信買張","D");
value3=GetField("自營商買張","D");
if volume<>0 then 
value4=(value1+value2+value3)/volume;
if value4*100>r1
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/法人逢低買超破億元.xs

```xs
{@type:filter}
input:day(5,"計算期別");
input:lowlimit(1,"單位:億元");
setbarfreq("D");
settotalbar(day);

value1=GetField("法人買賣超張數","D");
value2=summation(value1,day);
value3=value1*value2/10000;

if value3>=1 
and close*1.1<close[30]
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/法人連續買進達一定標準.xs

```xs
{@type:filter}
input:day(5);			setinputname(1,"計算天數");
input:ratio1(40);		setinputname(2,"法人買進張數比例下限(%)");
input:times(2);			setinputname(3,"達標天數");
input:volLimit(500);	setinputname(4,"最小成交均量");

SetTotalBar(day + 3);

value1 = (GetField("外資買張") + GetField("投信買張"))/Volume * 100;
value2 = countif(value1 > ratio1, day);
if value2 >= times and average(volume, day) > volLimit then
ret = 1;

SetOutputName1("近日法人買進比例(%)");
OutputField1(value1);
```

---


---

## 腳本檔案: 選股/06.籌碼選股/流通在外股數不多.xs

```xs
{@type:filter}
value1=GetField("最新股本");//單位:億
value2=GetField("董監持股佔股本比例","D");
value3=GetField("法人持股比例","D");
if value1*(1-value2/100-value3/100)<50
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/籌碼安定比率.xs

```xs
{@type:filter}
input:r1(60);	setinputname(1,"投信外資及董監合計持股比例下限(%)");

SetTotalBar(3);

value1=GetField("投信持股比例","D");
value2=GetField("外資持股比例","D");
value3=GetField("董監持股佔股本比例","D");
value4=value1+value2+value3;

if value4 > r1
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/籌碼從散戶手裡被收集.xs

```xs
{@type:filter}
input:ratio(200);		setinputname(1,"控盤者買張除以散戶買張的比例(%)");
input:volLimit(2000);	setinputname(2,"成交量下限(張)");

settotalbar(3);

value1=GetField("控盤者買張");
value2=GetField("散戶買張");
value3=value1/value2 * 100;

if volume > volLimit and value3 > ratio and value3[1] > ratio
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/籌碼被發散.xs

```xs
{@type:filter}
setbarfreq("AD");

input:period(10, "天期");

value1=GetField("分公司賣出家數");
value2=GetField("分公司買進家數");

if linearregslope(value1,period)<0
//賣出的家數愈來愈少
and linearregslope(value2,period)>0
//買進的家數愈來愈多 
and value2>300
and close>close[period]*1.05
//但這段期間股價在漲
and close>close[1]*1.025
//今天又漲超過2.5%
then ret=1;

outputfield(1,value2,0,"買進家數", order := 1);
outputfield(2,value1,0,"賣出家數");
```

---


---

## 腳本檔案: 選股/06.籌碼選股/籌碼集中度超過兩成的股票.xs

```xs
{@type:filter}
input:day(10,"天數");
input:ratio(20,"最低百分比");
setbarfreq("D");
settotalbar(day+3);

value1=GetField("主力買賣超張數","D");

if volume<>0 then 
	value2=summation(value1,day)/summation(volume,day)*100;
if value2>=ratio then 
	ret=1;
	
outputfield(1,value2,0,"籌碼集中度");
```

---


---

## 腳本檔案: 選股/06.籌碼選股/股價突破外資成本線.xs

```xs
{@type:filter}
Input: period(20, "期間(天)");
variable: avg_b(0);
setbarfreq("D");
settotalbar(period+7);

if GetField("Volume") > 0 then 
	Value5 = GetField("外資買張")*GetField("成交金額")*100000/GetField("Volume")
else
	Value5 = 0;

Value1 = summation(Value5, period);
Value2 = summation(GetField("外資買張"), period);
 
if Value2 > 0 then avg_b = Value1 / Value2;
if close cross over avg_b then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/股價突破投信成本線.xs

```xs
{@type:filter}
Input: period(20, "期間(天)");

variable: avg_b(0);

settotalbar(period + 5);

if GetField("Volume") > 0 then 
	Value5 = GetField("投信買張")*GetField("成交金額(元)")/(GetField("Volume")*1000)	 
else 
	Value5 = 0;

Value1 = summation(Value5, period);
Value2 = summation(GetField("投信買張"), period);
  
if Value2 > 0 and Value2 <> Value2[1] then avg_b = Value1 / Value2;

if close cross over avg_b then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/自營商拉抬.xs

```xs
{@type:filter}
// 
//
input: Length(10); setinputname(1,"計算天數");
input: UpRatio(3.5); setinputname(2, "上漲幅度(%)");
input: VolumeRatio(5); setinputname(3, "買超佔比例(%)");

variable: SumForce(0);
variable: SumTotalVolume(0);

settotalbar(3);

if RateOfChange(Close, 1) >= UpRatio then
begin
	SumTotalVolume = Summation(volume, Length);
	SumForce = Summation(GetField("自營商買賣超"), Length);
	if SumForce > SumTotalVolume * VolumeRatio / 100 then ret =1;
end;

SetOutputName1("自營商累計買超張數");
OutputField1(SumForce);
```

---


---

## 腳本檔案: 選股/06.籌碼選股/融資大減後轉強.xs

```xs
{@type:filter}
input: period(80);		setinputname(1, "計算區間");
input: v1(3000);		setinputname(2, "融資減少張數");

SetTotalBar(3);

value1 = highestbar(close,period);
value2 = GetField("融資餘額張數")[value1] - GetField("融資餘額張數");

if  value2 > v1 and 
	trueall(close > close[1],3)
then ret=1;

SetOutputName1("融資減少張數");
OutputField1(value2);
```

---


---

## 腳本檔案: 選股/06.籌碼選股/融資追捧.xs

```xs
{@type:filter}
input: Length(10); setinputname(1,"近期天數");
input: UpRatio(3.5); setinputname(2, "上漲幅度(%)");

settotalbar(3);

if RateOfChange(Close, 1) >= UpRatio and
	Getfield("融資餘額張數") > 0 and
	Getfield("融資餘額張數") = highest(Getfield("融資餘額張數"), Length)  
then ret=1;

SetOutputName1("融資餘額張數");
OutputField1(Getfield("融資餘額張數"));
```

---


---

## 腳本檔案: 選股/06.籌碼選股/近N日主力合計買超大於M張.xs

```xs
{@type:filter}
value1=GetField("主力買賣超張數","D");
input:days(5,"計算天期");
input:lowmit(200,"買超最低張數");
if summation(value1,days)>=lowmit
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/連續兩日籌碼在收集.xs

```xs
{@type:filter}
value1=GetField("分公司買進家數","D");
value2=GetField("分公司賣出家數","D");
value3=value2-value1;
if trueall(value3>30,2)
then ret=1;
```

---


---

## 腳本檔案: 選股/06.籌碼選股/連續大戶進散戶出.xs

```xs
{@type:filter}
input: periods(3, "連續期別");

setbarfreq("W");
settotalbar(periods+2);

condition1 = trueall(getfield("大戶持股比例", "W", param:=1000) > getfield("大戶持股比例", "W", param:=1000)[1], periods);
condition2 = trueall(getfield("散戶持股比例", "W", param:=400) < getfield("散戶持股比例", "W", param:=400)[1], periods);

ret= condition1 and condition2;

outputfield(1, getfield("大戶持股比例", "W", param:=1000), 2, "大戶比例");
outputfield(2, getfield("散戶持股比例", "W", param:=400), 2, "散戶比例");
```

---


---

## 腳本檔案: 選股/06.籌碼選股/集保張數減少中.xs

```xs
{@type:filter}
input: n(3);			setinputname(1, "計算期間(週)");
input: Amount(1000);	setinputname(2, "減少張數(張)");

SetTotalBar(3);

// 單位=萬張
Value1 = (GetField("集保張數","W")[n] - GetField("集保張數","W")) * 10000;
if Value1 > Amount then
ret = 1;

setoutputname1("減少張數(張)");
OutputField1(Value1);
```

---


---

## 腳本檔案: 選股/07.月營收選股/可預期的營收成長股.xs

```xs
{@type:filter}
// 找出過去幾年這個月的營收都會成長的股票
//
input: years(3, "過去N年");
input: growrate(10, "YOY成長%");

variable: mm(0);
variable: count(0);
variable: idx(0);

settotalbar(1);

// 最新一期營收月份
//
mm = Month(getfielddate("月營收", "M"));

// 下一期營收月份
mm = mm + 1;
if mm > 12 then mm = 1;

while count < years begin
	if Month(getfielddate("月營收", "M")[idx]) = mm then begin
		// 看同月份的營收YOY是否符合標準, 不符合的話就不用再找了
		if getfield("月營收年增率", "M")[idx] < growrate then return;
		count = count + 1;
	end;
	idx = idx + 1;	
end;

ret = 1;
```

---


---

## 腳本檔案: 選股/07.月營收選股/旺季不旺.xs

```xs
{@type:filter}
input:r1(5,"過去幾年月營收單月成長幅度下限%");
setbarfreq("M");
settotalbar(3);

value1=GetField("月營收月增率","M");
value2=GetField("月營收月增率","M")[12];
value3=GetField("月營收月增率","M")[24];
value4=GetField("月營收月增率","M")[36];

value5=(value2+value3+value4)/3;

if value2 > r1 and value3 > r1 and value4 > r1 and value1 < value5
then ret=1;
```

---


---

## 腳本檔案: 選股/07.月營收選股/最近三個月營收明顯成長.xs

```xs
{@type:filter}
settotalbar(3);
value1=GetField("月營收月增率","M");
value2=GetField("月營收年增率","M");
condition1=false;
condition2=false;

if average(value1,3)>10 and average(value2,3)>10
and value1>value1[1]
and value2>value2[1] 
then condition1=true;

if trueall(value1>5 and value2>5,3)
then condition2=true;
if condition1 and condition2 then ret=1;

outputfield(1,value1,1,"月營收月增率");
outputfield(2,value1[1],1,"上個月營收月增率");
outputfield(3,value2,1,"月營收年增率");
outputfield(4,value2[1],1,"上個月營收年增率");
```

---


---

## 腳本檔案: 選股/07.月營收選股/月營收YOYN月移動平均大於X.xs

```xs
{@type:filter}
input:lowlimit(10,"年增率下限");
input:period(12,"移動平均線的期別");

if average(GetField("月營收年增率","M"),period) >= lowlimit
then ret=1;
```

---


---

## 腳本檔案: 選股/07.月營收選股/月營收出現死亡交叉.xs

```xs
{@type:filter}
input:shortterm(4);
input:longterm(12);
setinputname(1,"短期均線");
setinputname(2,"長期均線");

if average(GetField("月營收","M"),shortterm)*1.1
< average(GetField("月營收","M"),longterm)
then ret=1;
```

---


---

## 腳本檔案: 選股/07.月營收選股/月營收創新低.xs

```xs
{@type:filter}
input:period(36, "期別");
settotalbar(period + 5);

value1=GetField("月營收","M");
value2=lowest(GetField("月營收","M"),period);

if value1=value2
and value1[1]=value2[1]
then ret=1;

outputfield(1, value1,2,"月營收(億)", order := 1);
```

---


---

## 腳本檔案: 選股/07.月營收選股/月營收創新高股價離高點有些距離.xs

```xs
{@type:filter}
value1=highest(getfield("月營收","M"),48);
value2=highest(GetField("總市值","D"),500);

if getfield("月營收","M")=value1
and value2>GetField("總市值","D")*1.2
then ret=1;
```

---


---

## 腳本檔案: 選股/07.月營收選股/月營收大成長的公司.xs

```xs
{@type:filter}
input:lowlimit(20);//單位:%
variable:FEPS(0);
setinputname(1,"成長百分比");

value1=GetField("月營收","M");//億
value2=GetField("營業利益率","Q");
value3=value1*12*value2/100;
value4=GetField("最新股本");//億
FEPS=value3/value4*10;
if feps<>0 then value5=close/feps;
condition1 = value5<12 and value5>0;
value6=GetField("月營收月增率","M");
value7=GetField("月營收年增率","M");
condition2 = value6>=lowlimit and value7>=lowlimit and value6[1]>0;
if condition1 and condition2 then ret=1;
setoutputname1("用月營收預估的本業EPS");
outputfield1(FEPS);
setoutputname2("用月營收預估的本益比");
outputfield2(value5);
```

---


---

## 腳本檔案: 選股/07.月營收選股/月營收年增率移動平均黃金交叉.xs

```xs
{@type:filter}
value1=GetField("月營收年增率","M");

if average(value1,4) crosses over average(value1,12)
and value1 > 0
then ret=1;

outputfield(1,value1,2,"月營收年增率%", order := 1);
```

---


---

## 腳本檔案: 選股/07.月營收選股/月營收成長動能加快.xs

```xs
{@type:filter}
setbarfreq("M");

value1=average(GetField("月營收年增率","M"),3);
//月營收年增率三個月平均
value2=average(GetField("月營收年增率","M"),12);
//月營收年增率十二個月平均
if value1 crosses over value2
//黃金交叉
and value1>5
and value1-value2>5
and value2>=1
then ret=1;
outputfield(1,value1,0,"3個月平均");
outputfield(2,value2,0,"12個月平均");
outputfield(3,(close-close[1])/close[1]*100,1,"本月漲跌幅");
```

---


---

## 腳本檔案: 選股/07.月營收選股/營收再起飛.xs

```xs
{@type:filter}
//input:TXT("僅適用月線"); setinputname(1,"使用限制");
setbarfreq("M");

If barfreq <> "M" then raiseruntimeerror("頻率設定有誤");

settotalbar(23);

value1=GetField("月營收年增率","M");
value2=average(GetField("月營收年增率","M"), 3);
value3=linearregslope(value2,20);
value4=linearregslope(value2,5);

if value3 < 0 and value4 crosses above 0
then ret=1;
```

---


---

## 腳本檔案: 選股/07.月營收選股/營收年增率由負轉正，且至少連續3個月.xs

```xs
{@type:filter}
value1=GetField("月營收年增率","M");
input:period(3);
if trueall(value1>0,period) and value1[3]<0
then ret=1;
```

---


---

## 腳本檔案: 選股/07.月營收選股/營收月增率優於平均.xs

```xs
{@type:filter}
value1=GetField("月營收月增率","M");
value2=average(GetField("月營收月增率","M"),36);
if value1>10
and value1>value2*1.3
then ret=1;
```

---


---

## 腳本檔案: 選股/07.月營收選股/營收月增率比歷年突出.xs

```xs
{@type:filter}
input:r1(5);		setinputname(1,"月營收月增幅與過往三年的數字增加百分比(%)");
//input:TXT("僅適用月線"); setinputname(2,"使用限制");
setbarfreq("M");

If barfreq <> "M" then raiseruntimeerror("頻率設定有誤");

value1 = GetField("月營收月增率","M");
value2 = average(GetField("月營收月增率","M"),3);
value3 = average(GetField("月營收月增率","M")[12],3);
value4 = average(GetField("月營收月增率","M")[24],3);
value5 = average(GetField("月營收月增率","M")[36],3);

value6 = (value3 + value4 + value5) / 3;
if (value2 - value6) > r1 then
ret = 1;

SetOutputName1("近3月月營收增幅平均");
OutputField1(value2);
```

---


---

## 腳本檔案: 選股/07.月營收選股/營收高於預期.xs

```xs
{@type:filter}
input: r1(10);		setinputname(1, "月營收年增率增加幅度下限(%)");
//input:TXT("僅適用月線"); setinputname(2,"使用限制");
setbarfreq("M");

If barfreq <> "M" then raiseruntimeerror("頻率設定有誤");

settotalbar(3);

value1=GetField("月營收年增率","M");
value2=average(GetField("月營收年增率","M")[1],3);
if value1-value2 > r1
then ret=1;

setoutputname1("月營收年增率(%)");
outputfield1(value1);
```

---


---

## 腳本檔案: 選股/07.月營收選股/營運趨緩.xs

```xs
{@type:filter}
input: months(24);	setinputname(1, "月營收計算期間(月)");
input: quarters(16);setinputname(2, "營業毛利率計算期間(季)");

settotalbar(3);

value1=GetField("月營收年增率","M");
value2=GetField("營業毛利率","Q");
if value1 = lowest(GetField("月營收年增率","M"), months) and
   value2 = lowest(GetField("營業毛利率","Q"), quarters) then
ret = 1;
```

---


---

## 腳本檔案: 選股/07.月營收選股/累計月營收年增率連續N月成長.xs

```xs
{@type:filter}
input:period(6,"計算區間");
settotalbar(period+1);
value1=GetField("累計營收年增率","M");
if trueall(value1>value1[1],period)
then ret=1;
```

---


---

## 腳本檔案: 選股/07.月營收選股/累計營收年增率黃金交叉.xs

```xs
{@type:filter}
value1=GetField("累計營收年增率","M");
input: r1(3),r2(12);
setinputname(1,"短天期");
setinputname(2,"長天期");
if average(value1,r1) crosses over average(value1,r2)+5
and value1>10
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/N年平均盈餘本益比.xs

```xs
{@type:filter}
input:r1(10);		setinputname(1,"本益比上限");
input:years(8);		setinputname(2,"計算期間(年)");

settotalbar(3);

value1=GetField("最新股本");			//單位=億元
value2=GetField("本期稅後淨利","Y");	//單位=百萬元
value3=average(GetField("本期稅後淨利","Y"), years);	//稅後淨利平均
value4=value3/(value1*10);				//每股盈餘
value6=GetField("收盤價","D");

if value4 > 0 then
begin
	value5 = GetField("收盤價","D") / value4;
	if value5 < r1 then ret = 1;
	
	SetOutputName1("平均盈餘本益比");
	OutputField1(value5);
end;
```

---


---

## 腳本檔案: 選股/08.財報選股/N年累計營業利益市值比.xs

```xs
{@type:filter}
input:r1(50);		setinputname(1,"累計營業利益佔總市值比例(%)");
input:years(10);		setinputname(2,"計算期間(年)");

settotalbar(3);

value1=GetField("總市值","D");		//單位億
value2=summation(GetField("營業利益","y"),years);
value3=value2/value1;				//單位=百分比

if value3 < r1
then ret=1;

setoutputname1("累計營業利益佔市值比例(%)");
outputfield1(value3);
```

---


---

## 腳本檔案: 選股/08.財報選股/PB來到近年來低點.xs

```xs
{@type:filter}
input:r1(10);	setinputname(1,"PB距離N個月來低點只剩N%");
input:r2(60);	setinputname(2,"N個月以來");
//input:TXT("僅適用月資料"); setinputname(3,"使用限制");
setbarfreq("M");

if barfreq <> "M" then raiseruntimeerror("頻率錯誤");

settotalbar(3);

value1=GetField("股價淨值比","M");
value2=lowest(GetField("股價淨值比","M"),r2);
value3=average(GetField("股價淨值比","M"),r2);

if value1 < value3 and value1 < value2*(1+r1/100)
then ret=1;

setoutputname1("股價淨值比");
outputfield1(value1);
```

---


---

## 腳本檔案: 選股/08.財報選股/PEG指標.xs

```xs
{@type:filter}
input:r1(1);	setinputname(1,"PEG上限");

settotalbar(3);

// PEG指標
//
value1 = GetField("本益比","D");
value2 = GetField("月營收年增率","M"); 
if value1 > 0 and value2 > 0 and value1 / value2 < r1 then
ret=1;

SetOutputName1("PEG指標");
OutputField1(value1 / value2);
```

---


---

## 腳本檔案: 選股/08.財報選股/ROE漸入佳境.xs

```xs
{@type:filter}
value1=GetField("股東權益報酬率","Q");
if GetField("股東權益報酬率","Q")>GetField("股東權益報酬率","Q")[1]
and GetField("股東權益報酬率","Q")>GetField("股東權益報酬率","Q")[4]
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/上一季本業賺錢.xs

```xs
{@type:filter}
value1=GetField("營業利益率","Q");
if value1>0
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/上市股可以發行權證的流動性條件.xs

```xs
{@type:filter}
{
	1. 市值超過100億元
	
	2. (a or b)
		a. 最近3個月成交股數佔已發行股份總額比例達20%以上。
		b. 最近三個月月平均成交股數達1億股以上。

	3. 最近期經會計師查核或核閱之財務報告無虧損
}

settotalbar(3);

// 近三個月成交股數佔以發行股份比例
//
Value1 = Summation(GetField("成交量", "M"), 3) * 100 / (GetField("發行張數","D") * 10000);

// 最近三個月月平均成交股數
//
Value2 = Average(GetField("成交量", "M"), 3) * 1000;

if GetField("總市值","D") >= 100 and 
   (Value1 >= 20 or Value2 >= 10000000) and 
   GetField("每股稅後淨利(元)","Q") > 0 
then 
Ret = 1;
```

---


---

## 腳本檔案: 選股/08.財報選股/上櫃股可以發行權證的流動性條件.xs

```xs
{@type:filter}
{
	1. 市值超過40億元
	
	2. (a or b)
		a. 最近3個月成交股數佔已發行股份總額比例達10%以上。
		b. 最近三個月月平均成交股數達3000萬股以上。

	3. 最近期經會計師查核或核閱之財務報告無虧損
}

settotalbar(3);

// 近三個月成交股數佔以發行股份比例
//
Value1 = Summation(GetField("成交量", "M"), 3) * 100 / (GetField("發行張數","D") * 10000);

// 最近三個月月平均成交股數
//
Value2 = Average(GetField("成交量", "M"), 3) * 1000;

if GetField("總市值","D") >= 40 and 
   (Value1 > 10 or Value2 > 3000000) and 
   GetField("每股稅後淨利(元)","Q") > 0 
then 
Ret = 1;
```

---


---

## 腳本檔案: 選股/08.財報選股/五年內有至少三年營收成長.xs

```xs
{@type:filter}
value1=GetField("營業收入淨額","Y");
value2=value1-value1[1];
if countif(value2>0,5)>=3
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/企業價值除以自由現金流的倍數低於一水準.xs

```xs
{@type:filter}
input: t1(4,"倍數");
setbarfreq("Q");
settotalbar(4);

value1=GetField("企業價值","Q");//單位百萬
value2=GetField("來自營運之現金流量","Q");//單位百萬
value3=GetField("資本支出金額","Q");//單位百萬
value4=GetField("所得稅費用","Q");//單位百萬
value5=GetField("利息支出","Q");//單位百萬
value6=value2-value3-value4-value5;
//自由現金流量 = 營運現金流量 - 資本支出 - 利息 - 稅金
value7=summation(value6,4);
//最近四期現金流量

if value1<t1*value7 then ret=1;
outputfield(1,value1,0,"企業價值");
outputfield(2,value7,0,"近四季自由現金流合計");
```

---


---

## 腳本檔案: 選股/08.財報選股/低修正型股價淨值比.xs

```xs
{@type:filter}
input:r1(1);		setinputname(1,"股價淨值比上限");

SetTotalBar(3);

value1 = average(GetField("營業利益成長率", "Y"), 6);		// 近六年平均營業利益成長率
value2 = GetField("每股淨值(元)","Q") * (1 + value1/100);	// 修正後每股淨值
value3 = close / value2;									// 修正後股價淨值比

if 0 < value3 and value3 < r1
then ret=1;

SetOutputName1("修正後股價淨值比");
OutputField1(value3);
```

---


---

## 腳本檔案: 選股/08.財報選股/公司官僚化.xs

```xs
{@type:filter}
// 連續4期[管理費用/營業收入淨額的比例]成長
//
//input:TXT("僅適用季資料"); setinputname(1,"使用限制");
setbarfreq("Q");

if barfreq <> "Q" then raiseruntimeerror("頻率錯誤");

settotalbar(3);

Ret = TrueAll(
	GetField("管理費用","Q")/GetField("營業收入淨額","Q") > 
	GetField("管理費用","Q")[1]/GetField("營業收入淨額","Q")[1], 4);
```

---


---

## 腳本檔案: 選股/08.財報選股/公司連續N年獲利大於X億.xs

```xs
{@type:filter}
input:lowlimit(1,",金額下單位億元");
input:period(10,"連續年度數");
value1=GetField("本期稅後淨利","Y");//單位百萬
if trueall(value1>lowlimit*100,period) 
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/利息支出佔股本比例.xs

```xs
{@type:filter}
input:r1(5);	setinputname(1,"利息支出佔股本比例(%)");

settotalbar(3);

value1=GetField("最新股本");		//單位億
value2=GetField("利息支出","Y");	//單位百萬

value3=value2/(value1*100) * 100;

if value3 > r1
then ret=1;

SetOutputName1("利息支出佔股本比例(%)");
OutputField1(value3);
```

---


---

## 腳本檔案: 選股/08.財報選股/即將董監改選.xs

```xs
{@type:filter}
input: day(180);		setinputname(1, "距離董監改選日期(天)");

settotalbar(3);

// 董監每三年得改選一次
//
variable: lastdate(0), diff(0), years_3(0);

lastdate = GetField("董監事就任日期");
diff = datediff(currentdate, lastdate);
years_3 = 365*3;

OutputField(1,lastdate,"董監事就任日期");
OutputField(2,diff,"改選天數");

ret = diff < years_3 and diff > years_3 - day;
```

---


---

## 腳本檔案: 選股/08.財報選股/可能由虧轉盈.xs

```xs
{@type:filter}
// 計算最新一期月營收的日期(mm=月份)
//
variable: mm(0);
mm = datevalue(getfielddate("月營收","M"),"M");

setbarfreq("M");

// 預估最新一季的季營收(單位=億)
//
if mm=1 or mm=4 or mm=7 or mm=10
then value1=GetField("月營收","M") * 3;
if mm=2 or mm=5 or mm=8 or mm=11
then value1=GetField("月營收","M") * 2 + GetField("月營收","M")[1];
if mm=3 or mm=6 or mm=9 or mm=12
then value1=GetField("月營收","M")+GetField("月營收","M")[1]+GetField("月營收","M")[2];

// 預估獲利(單位=百萬) = 季營收 * 毛利率 - 營業費用
//
value2 = value1 * GetField("營業毛利率","Q") - GetField("營業費用","Q");

if GetField("營業利益","Q")<0
and value2>0 
then ret=1;

outputfield(1,value2 / 100,2,"預估單季本業獲利(億)");
outputfield(2,GetField("營業利益","Q"),0,"最近一季營業利益");
```

---


---

## 腳本檔案: 選股/08.財報選股/固定資產佔股本比率低於N%.xs

```xs
{@type:filter}
input:r1(10,"固定資產佔股本比例(單位%)");

value1=GetField("最新股本");//單位億
value2=GetField("固定資產","Q");
value3=value2/(value1*100);

if value3<r1/100
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/季營收連N季YOY正成長.xs

```xs
{@type:filter}
input:n(12,"期數(單位:季)");
setbarfreq("Q");
settotalbar(n+4);

value1=GetField("營業收入淨額","Q");//單位:百萬
if trueall(value1>value1[4],n)
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/市值研發費用比.xs

```xs
{@type:filter}
input:n(5);						setinputname(1,"研發費用市值比");

settotalbar(3);

value1=GetField("總市值");				// 單位=億
value2=GetField("研發費用","Y");		// 單位=百萬
value3=value2 / value1;					// % 
if value3 > n
then ret=1;

SetOutputName1("研發費用市值比");
OutputField1(value3);
```

---


---

## 腳本檔案: 選股/08.財報選股/帳上現金少.xs

```xs
{@type:filter}
input:r1(50);	setinputname(1,"帳上現金(單位:百萬元)");

settotalbar(3);

value1=GetField("現金及約當現金","Q");
if value1 < r1
then ret=1;

SetOutputName1("帳上現金(百萬)");
OutputField1(value1);
```

---


---

## 腳本檔案: 選股/08.財報選股/年營收成長率超過一定比例.xs

```xs
{@type:filter}
setbarfreq("Y");
settotalbar(5);

value1=GetField("營收成長率","Y");
value2=average(value1,5);
if trueall(value1>0,5) and value2>=25
then ret=1;

OutputField(1,value1,"年度營收成長率");
OutputField(2,value2,"五年平均營收成長率");
```

---


---

## 腳本檔案: 選股/08.財報選股/最新一季可能虧錢的公司.xs

```xs
{@type:filter}
setbarfreq("M");

value1=GetField("月營收","M");//單位:億
value2=value1[2]+value1[3]+value1[4];
value3=GetField("營業毛利率","Q");
value4=GetField("營業費用","Q");//單位:百萬

if value2*value3/100-value4/100<0  
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/最近五年ROE平均高於某值.xs

```xs
{@type:filter}
input:r1(15,"平均報酬率");

if average(GetField("股東權益報酬率","Y"),5)>r1
then ret=1;

outputfield(1,GetField("股東權益報酬率","Y"),1,"最近一年");
outputfield(2,GetField("股東權益報酬率","Y")[1],1,"前一年");
outputfield(3,GetField("股東權益報酬率","Y")[2],1,"前兩年");
outputfield(4,GetField("股東權益報酬率","Y")[3],1,"前三年");
outputfield(5,GetField("股東權益報酬率","Y")[4],1,"前四年");
outputfield(6,average(GetField("股東權益報酬率","Y"),5),1,"平均");
```

---


---

## 腳本檔案: 選股/08.財報選股/最近幾季存貨增加的比營收還快.xs

```xs
{@type:filter}
input:r1(4 ,"存貨比營收成長率大的連續季數");
setbarfreq("Q");
settotalbar(r1+2);

value1=GetField("營業收入淨額","Q");
value2=GetField("存貨","Q");

value3=rateofchange(value1,1);
value4=rateofchange(value2,1);
value5=value4-value3;

if trueall(value5>0,r1)
and trueall(value5-value5[1]>0,r1)
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/本業可能轉虧為盈.xs

```xs
{@type:filter}

SetTotalbar(3);

// 計算最新一期月營收的日期(mm=月份)
//
variable: mm(0);
mm = datevalue(getfielddate("月營收","M"),"M");

// 預估最新一季的季營收(單位=億)
//
if mm=1 or mm=4 or mm=7 or mm=10
then value1=GetField("月營收","M") * 3;
if mm=2 or mm=5 or mm=8 or mm=11
then value1=GetField("月營收","M") * 2 + GetField("月營收","M")[1];
if mm=3 or mm=6 or mm=9 or mm=12
then value1=GetField("月營收","M")+GetField("月營收","M")[1]+GetField("月營收","M")[2];

// 預估獲利(單位=百萬) = 季營收 * 毛利率 - 營業費用
//
value2 = value1 * GetField("營業毛利率","Q") - GetField("營業費用","Q");

if value2 > 0 and GetField("營業利益","Q") < 0 then
ret = 1;

SetOutputName1("預估單季營收(億)");
OutputField1(value1);

SetOutputName2("預估單季本業獲利(億)");
OutputField2(value2 / 100);
```

---


---

## 腳本檔案: 選股/08.財報選股/本業推估本益比低於N.xs

```xs
{@type:filter}
input:epsl(15,"預估本益比上限");

value3= summation(GetField("營業利益","Q"),4); //單位百萬;
value4= GetField("最新股本");//單位億;
value5= value3/(value4*10);//每股預估EPS
if value5>0 and close/value5<=epsl
then ret=1;

outputfield(1,close/value5,1,"預估本益比", order := 1);
```

---


---

## 腳本檔案: 選股/08.財報選股/本業獲利佔八成以上.xs

```xs
{@type:filter}
value1=GetField("營業利益","Q");//單位百萬
value2=GetField("稅前淨利","Q");//單位百萬
if value2>0
then begin
if value1/value2*100>80
then ret=1;
end;
```

---


---

## 腳本檔案: 選股/08.財報選股/每年本業都獲利且趨勢向上.xs

```xs
{@type:filter}
input:lm(200,"年營業利益下限");
settotalbar(5);

value1=GetField("營業利益","Y");//百萬
if trueall(value1>lm,5)
//週去五年都賺超過一億
and linearregslope(value1,5)>0
//五年的營業利益趨勢往上
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/每股來自營運現金流量.xs

```xs
{@type:filter}
input:r1(25);	setinputname(1,"來自營運的現金流量佔股本比率下限%");

settotalbar(3);

value1=GetField("最新股本");				// 單位=億
value2=GetField("來自營運之現金流量","Q");	// 單位=百萬
value3=value2/value1;						// 單位=%

if value3 > r1
then ret=1;

setoutputname1("來自營運的現金流量佔股本比率(%)");
outputfield1(value3);
```

---


---

## 腳本檔案: 選股/08.財報選股/毛利沒掉營收成長費用減少.xs

```xs
{@type:filter}
input:ratio(10,"毛利率單季衰退幅度上限");
input:period1(10,"計算的期間，單位是季");
input:period2(5,"計算的季別");
input:count(2,"符合條件之最低次數");
setbarfreq("Q");
settotalbar(maxlist(period1,period2)+1);

value1=GetField("營業毛利率","Q");
value2=GetField("營業收入淨額","Q");//單位百萬
value3=GetField("營業費用","Q");//單位百萬

if trueall(value1>value1[1]*(1-ratio/100),period1)
and countif(value2>value2[1]and value3<value3[1],period2)>=count
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/毛利率上昇月營收成長.xs

```xs
{@type:filter}
value1=GetField("月營收月增率","M");
value2=GetField("營業毛利率","Q");
if value1>value1[1]
and value2>value2[1]
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/毛利率沒掉的兇.xs

```xs
{@type:filter}
input:ratio(10,"毛利率單季衰退幅度上限");
input:period(10,"計算的期間，單位是季");

value1=GetField("營業毛利率","Q");
if trueall(value1>value1[1]*(1-ratio/100),period)
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/法定盈餘公積已提足，配股能力提昇.xs

```xs
{@type:filter}
value1=GetField("法定盈餘公積","Q");	//百萬

value2=GetField("最新股本");			//億

value3=GetField("本期稅後淨利","Q");	//百萬

// 稅後淨利 + 法定盈餘公積 > 股本
//
if value1 + value3 > value2*100
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/流動資產市值比.xs

```xs
{@type:filter}
input:r1(12);			setinputname(1,"流動資產市值比下限%");

settotalbar(3);

value1=GetField("流動資產","Q");	// 單位=百萬
value2=GetField("總市值","D");		// 單位=億
value3=value1/value2;				// 單位=%
if value3 < r1
then ret=1;

setoutputname1("流動資產市值比%");
outputfield1(value3);
```

---


---

## 腳本檔案: 選股/08.財報選股/流動資產減負債超過市值N成.xs

```xs
{@type:filter}
input:ratio(80,"佔總市值百分比%");
if (GetField("流動資產","Q")-GetField("負債總額","Q"))*100>GetField("總市值","D")*ratio/100
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/流動資產減負債超過總市值N成.xs

```xs
{@type:filter}
input:ratio(80,"比率下限");

value1=GetField("流動資產","Q");//單位百萬
value2=GetField("負債總額","Q");//單位百萬
value3=GetField("總市值","D");//單位億

if (value1-value2)>=value3*ratio
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/淡季不淡.xs

```xs
{@type:filter}
input:r1(5);	setinputname(1,"過去幾年月營收單月衰退幅度下限(%)");
input:r2(0);	setinputname(2,"最近一個月營收月增率下限(%)");
//input:TXT("僅適用月線"); setinputname(3,"使用限制");
setbarfreq("M");

If barfreq <> "M" then raiseruntimeerror("頻率設定有誤");

settotalbar(3);

value1=GetField("月營收月增率","M");
value2=GetField("月營收月增率","M")[12];
value3=GetField("月營收月增率","M")[24];
value4=GetField("月營收月增率","M")[36];

if value2 < -r1 and value3 < -r1 and value4 < -r1 and value1 > r2
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/營收上昇費用降低.xs

```xs
{@type:filter}
input:period(5,"計算的季別");
input:count(2,"符合條件之最低次數");
setbarfreq("Q");
settotalbar(period+1);

value1=GetField("營業收入淨額","Q");//單位百萬
value2=GetField("營業費用","Q");//單位百萬

if countif(value1>value1[1] and value2<value2[1],period)>=count
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/營收市值比位於歷史低檔.xs

```xs
{@type:filter}
input:period(60,"計算月數");
input:ratio(10,"距離低點幅度");
setbarfreq("M");
settotalbar(period);

value1=GetField("總市值","M");//單位:億元
value2=GetField("月營收","M");//單位:億元
if value2<>0 then 
	value3=value1/value2
else
	value3=0;

if value3<lowest(value3,period)*(1+ratio/100)
//總市值營收比值距離過去一段時間最低點沒有差多遠
and value3>0
then ret=1;
outputfield(1,value3,2,"總市值/月營收");
outputfield(2,lowest(value3,period),2,"期間最低值");
outputfield(3,value3/lowest(value3,period),2,"兩者的比率");
```

---


---

## 腳本檔案: 選股/08.財報選股/營業利益均線向上.xs

```xs
{@type:filter}
setbarfreq("Q");
settotalbar(10);
value1=GetField("營業利益","Q");
if linearregslope(average(value1,5),5)>0
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/營業利益率不曾大幅下滑.xs

```xs
{@type:filter}
input:r1(5, "營業利益率QOQ最大衰退幅度");
input:p1(5, "計算的季期數");

SetTotalBar(p1 + 4);
value1=GetField("營業利益率","Q");
if trueall(value1*(1+r1/100)>value1[1],p1)
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/營業外收入愈來愈高.xs

```xs
{@type:filter}
settotalbar(3);

if trueall(GetField("營業外收入合計","Y") > GetField("營業外收入合計","Y")[1], 3) 
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/營益率由負轉正且持續上揚.xs

```xs
{@type:filter}
settotalbar(3);

if 
	GetField("營業利益率","Q")[2]<0 and 
	GetField("營業利益率","Q")[1]>0 and
	GetField("營業利益率","Q") > GetField("營業利益率","Q")[1] and
	GetField("月營收月增率","M") > 0 and 
	GetField("月營收月增率","M")[1] >0
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/營運現金流大於稅後盈餘.xs

```xs
{@type:filter}
settotalbar(3);

value1=GetField("來自營運之現金流量","Q");
value2=GetField("本期稅後淨利","Q");
if value1 > value2
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/獲利穩定的公司.xs

```xs
{@type:filter}
setbarfreq("Y");
settotalbar(5);
value1=GetField("每股稅後淨利(元)","Y");
if trueall(value1>=2,5)//過去五年每年都賺超過兩元
and highest(value1,5)<lowest(value1,5)*1.5//獲利的高低差距在忍受範圍
then ret=1;
outputfield(1,highest(value1,5),1,"最高EPS");
outputfield(2,lowest(value1,5),1,"最低EPS");
```

---


---

## 腳本檔案: 選股/08.財報選股/獲利追不上固定資本支出.xs

```xs
{@type:filter}
input:r1(3);		setinputname(1,"連續幾年資本支出增加的速度比稅後淨利高");
//input:TXT("僅適用年資料"); setinputname(2,"使用限制");
setbarfreq("Y");

if barfreq <> "Y" then raiseruntimeerror("頻率錯誤");

settotalbar(3);

if trueall(
	GetField("本期稅後淨利","Y") - GetField("本期稅後淨利","Y")[1] <
	GetField("固定資產","Y") - GetField("固定資產","Y")[1],
	r1)
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/現增佔比低.xs

```xs
{@type:filter}
value1=GetField("現金增資佔股本比重","Y");
if value1<20
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/現金不少但股價淨值比低.xs

```xs
{@type:filter}
input:r1(0,"來自營運之現金流量下限");
input:r2(10,"現金及約當現金單位億元");
input:r3(0.8,"股價淨值比上限");

value1=GetField("來自營運之現金流量","Q");
value2=GetField("現金及約當現金","Q");
value3=GetField("股價淨值比","D");

if value1>r1
and value2/100>r2
and value3<r3
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/現金佔總市值比例.xs

```xs
{@type:filter}
input: r1(50);		setinputname(1,"現金佔總市值比例%");

settotalbar(3);

value1=GetField("現金及約當現金","Q");	// 單位=百萬
value2=GetField("總市值","D");			// 單位=億
value3=value1/value2;					// 單位=%

if value3 > r1 then ret=1;

SetoutputName1("現金佔總市值比例%");
OutputField1(value3);
```

---


---

## 腳本檔案: 選股/08.財報選股/現金很多的公司.xs

```xs
{@type:filter}
input: lowlimit(10,"償債後現金及短投最少金額");

value1=GetField("現金及約當現金","Q");//單位百萬
value2=GetField("短期投資","Q");//單位百萬
value3=GetField("短期借款","Q");//單位百萬
value4=(value1+value2-value3)/100;//單位億之現金及短期投資合計金額

if value4>=lowlimit
then ret=1;

outputfield(1,value4,"償債後現金及短投金額(億)");
```

---


---

## 腳本檔案: 選股/08.財報選股/現金總市值比.xs

```xs
{@type:filter}
value1=GetField("現金及約當現金","Q");//單位百萬
value2=GetField("短期投資","Q");//單位百萬
value3=(value1+value2)/100;//單位億之現金及短期投資合計金額
value4=GetField("總市值","D");//單位:億
if value4<>0
then value5=value3/value4;//現金總市值比;
if value5>0.7 and value3>3 //現金總市值比大於0.7且現金及短投合計超過3億
then ret=1;

outputfield(1, value5, 1, "現金總市值比", order := 1);
```

---


---

## 腳本檔案: 選股/08.財報選股/總市值接近歷史低點.xs

```xs
{@type:filter}
input: r1(5);			setinputname(1, "接近低點幅度(%)");
//input:TXT("僅適用月資料"); setinputname(2,"使用限制");
setbarfreq("M");

if barfreq <> "M" then raiseruntimeerror("頻率錯誤");

settotalbar(3);

value1=GetField("總市值","M");
value2=nthlowest(1,GetField("總市值","M"),48);
value3=nthlowest(1,GetField("總市值","M"),24);

if absvalue(value2-value3)*100 / value3 < r1
then 
  begin
	if (value1-value2) * 100 / value2 < r1 and
	   (value1-value3) * 100 / value3 < r1 
	then
		ret=1;
  end;
	
SetOutputName1("最近市值(億)");
OutputField1(value1);
```

---


---

## 腳本檔案: 選股/08.財報選股/考慮成長率的股利回推合理股價.xs

```xs
{@type:filter}
input:r(6,"年預期報酬率單位%");
variable: s1(0);

value1=average(GetField("現金股利","Y"),5);

if lowest(GetField("現金股利","Y")[1],3)>0 then 
	s1=lowest(rateofchange(GetField("現金股利","Y"),1),3);

if value1>1 and r>s1 and s1>0then begin
	value2=value1/(r-s1)*100;
	if close<>0 then 
		value3=(value2-close)/close*100;
	if value3>10
	and GetField("現金股利","Y")>GetField("現金股利","Y")[1]
	then ret=1;
	
	outputfield(1,value1,1,"平均現金股利");
	outputfield(2,s1,1,"近年最低股利成長率");

end;
```

---


---

## 腳本檔案: 選股/08.財報選股/股價低於N年平均股利的N倍.xs

```xs
{@type:filter}
input:N1(5);
input:N2(16);
setinputname(1,"股利平均的年數");
setinputname(2,"股利的倍數");
value1=GetField("股利合計","Y");
value2=average(value1,N1);
if close<value2*N2
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/股息配發率超過一定比率.xs

```xs
{@type:filter}
input:ratio(60,"股息配發率%");
value1=GetField("每股稅後淨利(元)","Y");
value2=GetField("現金股利","Y");
if value1>0
then value3=value2/value1*100;//股息配發率

if trueall(value3>ratio,3) then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/股本膨脹營收獲利跟不上.xs

```xs
{@type:filter}
//input:TXT("僅適用年資料"); setinputname(1,"使用限制");
setbarfreq("Y");

if barfreq <> "Y" then raiseruntimeerror("頻率錯誤");

settotalbar(4);

value1 = RateOfChange(GetField("普通股股本","Y"), 1);
value2 = RateOfChange(GetField("營業收入淨額","Y"), 1);
value3 = GetField("營業利益成長率","Y");

if 
	value1 > value2 and
	value1 > value3 and
	value1[1] > value2[1] and
	value1[1] > value3[1]
then
ret = 1;
```

---


---

## 腳本檔案: 選股/08.財報選股/股東權益報酬率高且穩定.xs

```xs
{@type:filter}
input:years(5);		setinputname(1,"評估期間(年)");
input:r1(15);		setinputname(2,"ROE下限(%)");
input:r2(3);		setinputname(3,"ROE最大差異(%)");
input:fx("資料頻率");	SetInputName(4, "使用限制:請選擇年頻率");

if barfreq <> "Y" then raiseruntimeerror("頻率錯誤");

settotalbar(3);

value1=GetField("股東權益報酬率","Y");

value2=lowest(GetField("股東權益報酬率","Y"), years);
value3=highest(GetField("股東權益報酬率","Y"), years);

if (value3 - value2) < r2 and value2 > r1 
then ret=1;

setoutputname1("ROE(%)");
outputfield1(value1);
```

---


---

## 腳本檔案: 選股/08.財報選股/股魚選股策略.xs

```xs
{@type:filter}
value1=GetField("營業利益","Q");//單位百萬
value2=GetField("稅前淨利","Q");//單位百萬
value3=GetField("來自營運之現金流量","Q");//單位百萬
value4=GetField("資本支出金額","Q");//單位百萬
value5=GetField("利息支出","Q");//單位百萬
value6=GetField("所得稅費用","Q");//單位百萬
condition1=false;
condition2=false;
condition3=false;

if value2>0 then begin
	if value1/value2*100>80
	then condition1=true;  //本業獲利佔八成以上
end;

if value3-value4-value5-value6>0 //自由現金流量大於零
then condition2=true;

value7=GetField("利息保障倍數","Y");
value8=GetField("股東權益報酬率","Y");//單位%
value9=GetField("營業利益率","Q");//單位%
value10=GetField("本益比","D");
value11=GetField("殖利率","D");
value12=GetField("每股淨值(元)","Q");
value13=value12*value8/8;//獲利能力比率

if value7>20 and value8>8 and value9>0 and value10<12 and value11>6 and close<value13
then condition3=true;

if condition1 and condition2 and condition3
then ret=1;

outputfield(1,GetField("股東權益報酬率","Y"),2,"ROE");
outputfield(2,GetField("殖利率","D"),2,"殖利率", order := 1);
```

---


---

## 腳本檔案: 選股/08.財報選股/葛拉罕的選股兩標準.xs

```xs
{@type:filter}
value1=summation(GetField("本期稅後淨利","Q"),4);//單位:百萬
value2=GetField("負債總額","Q");
value3=GetField("資產總額","Q");
value4=GetField("總市值","D");//單位:億

if value4<value1*7/100
and value3>value2*2
then ret=1;

outputfield(1,value1/100,0,"近四季獲利(億)");
outputfield(2,value1/100*7,0,"獲利的七倍(億)");
outputfield(3,value4,0,"總市值");
outputfield(4,value2,0,"負債");
outputfield(5,value3,0,"資產");
```

---


---

## 腳本檔案: 選股/08.財報選股/說好的好業績一直沒有來.xs

```xs
{@type:filter}
input: r1(5);		setinputname(1, "月營收月增率上限(%)");
input: r2(30);		setinputname(2, "預估本益比下限");

settotalbar(3);

value1 = 4 * GetField("每股稅後淨利(元)","Q");	// 預估每股盈餘(年)
if value1 > 0 then
	value2 = close / value1				//本益比
else	
	value2 = 0;	

if value2 > r2 and 
   trueall(GetField("月營收月增率","M") < r1, 3) 
then ret = 1;

setoutputname1("預估每股盈餘(元)");
outputfield1(value1);
```

---


---

## 腳本檔案: 選股/08.財報選股/資產報酬率達到一定的水準且沒有明顯下滑.xs

```xs
{@type:filter}
value1=GetField("資產報酬率","Q");
value2=average(value1,4);
value3=linearregslope(value2,5);
if value3>0
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/近N年EPS成長率平均大於X%.xs

```xs
{@type:filter}
input: N(5), X(10);
setbarfreq("Y");

setinputname(1, "期別");
setinputname(2, "平均EPS成長率(%)");

SetTotalBar(N+3);

Value1 = Average(RateOfChange(GetField("每股稅後淨利(元)","Y"), 1), N);

Ret = Value1 > X;

SetOutputName1("平均EPS成長率(%)");
OutputField1(Value1);
```

---


---

## 腳本檔案: 選股/08.財報選股/近五年至少有一年營業利益超過五億.xs

```xs
{@type:filter}
input:years(5,"期間");
setbarfreq("Y");
settotalbar(5);

value1=GetField("營業利益","Y");//單位: 百萬
if highest(value1,years)>=500
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/近四季EPS合計大於N元.xs

```xs
{@type:filter}
input:n1(3);
setinputname(1,"每股稅後淨利最低標準");
value1=GetField("每股稅後淨利(元)","Q");
value2=summation(value1,4);
if value2>=n1
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/近期有大額資本支出.xs

```xs
{@type:filter}
input:period(20,"計算N季");
input:lm(30,"比均值增加的幅度");
input:cm(500,"單季資本支出金額下限");
settotalbar(period+1);

value1=GetField("資本支出金額","Q");//單位: 百萬
value2=GetField("資本支出營收比","Q");//單位：%
value3=average(value1,period);
value4=average(value2,period);

if value1>cm//資本支出超過一定金額
and value1>value3*(1+lm/100)
and value2>value4*(1+lm/100)
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/過去三年來自營運的現金流量都大於零.xs

```xs
{@type:filter}
value1=GetField("來自營運之現金流量","Y");
if trueall(value1>0,3)
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/預估殖利率高的.xs

```xs
{@type:filter}
value1=GetField("營業利益","Q");//單位:百萬
value2=GetField("月營收","M");//單位:億
value3=GetField("營業利益率","Q");
value4=SUMMATION(GETFIELD("月營收","M"),3);//近三個月營收
value5=value4*value3/100;
//用最近一期營益率去估算的最近一季營業利益
value6=SUMMATION(GetField("營業利益","Q"),3)+value5*100;
//前三季營業利益加上最近一季預估營業利益
value8=GetField("最新股本");//單位億
value9=value6/(value8*100)*10;
//估算出來的EPS

value10=value9/close*100;
//eps/股價*100: 預估殖利率

if value10>10 and value3>0 and close>10
then ret=1;
outputfield(1,value10,1,"殖利率");
outputfield(2,value9,1,"預估EPS");
```

---


---

## 腳本檔案: 選股/08.財報選股/預期報酬率高的公司.xs

```xs
{@type:filter}
input: tp(150,"最低目標預期報酬率");

value1=GetField("累計營收年增率","M");
value2=GetField("月營收","M");//單位:億
value3=GetField("營業毛利率","Q");
value4=GetField("營業費用","Q");//單位百萬
value5=GetField("加權平均股本","Q");//單位億

{用月營收*毛利率-季營業費用/3來當單月本業獲利，
乘12當未來一年的本業獲利除以股本為預估的未來一年EPS}
value6=((value2*value3/100-value4/300)*12/(value5))*10;

//未來一年預估EPS*累計營收年增率為目標價
//但若累計營收年增率不到10就以10倍本益比來算目標價
if value1>10 and value1<20 then value7=value6*value1
else if value1>=20 then value7=value6*20
else value7=value6*10;

//用預估EPS乘上累計營收成長率當成目標價
if close<>0
then value8=((value7-close)/close)*100;

if GetField("月營收月增率","M")<30 and GetField("月營收年增率","M")<50
then begin
	if value8 > tp then ret=1;
	outputfield(1,value8,"預期報酬率");
	outputfield(2,value7,"目標價");
	outputfield(3,value6,"預估EPS");
	outputfield(4,value2,"最近月營收(億)");
	outputfield(5,value3,"毛利率");
	outputfield(6,value4,"季營業費用(百萬)");
	outputfield(7,value5,"加權股本(億)");
end;
```

---


---

## 腳本檔案: 選股/08.財報選股/高F_Score的股票.xs

```xs
{@type:filter}
setbarfreq("Q");
settotalbar(5);

variable:score(0);

value1=GetField("資產報酬率","Q");
value2=GetField("來自營運之現金流量","Q");//單位百萬
value3=GetField("本期稅後淨利","Q");//單位百萬
value5=GetField("負債比率","Q");
value6=GetField("流動比率","Q");
value7=GetField("現金增資佔股本比重","y");
value8=GetField("營業毛利率","Q");
value9=GetField("總資產週轉率(次)","Q");

if date<>date[1] then score=0;
if value1>0 then score=score+1;
if value1-value1[3]>0 then score=score+1;
if value2>0 then score=score+1;
if value3>value2 then score=score+1;
if value5<value5[3] then score=score+1;
if value6>value6[3] then score=score+1;
if value7<=value7[3] then score=score+1;
if value8>value8[3] then score=score+1;
if value9>value9[3] then score=score+1;

if score>=8 
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/高毛利低獲利營收暴衝.xs

```xs
{@type:filter}
input:
	smr(5,"月營收月增率"),
	syr(10,"月營收年增率"),
	gr(45,"營業毛利率"),
	epsy(1,"年EPS"),
	epsq(0.5,"季EPS");

value1=GetField("月營收月增率","M");
value2=GetField("月營收年增率","M");
value3=GetField("營業毛利率","Q");

if value1> smr //月營收月增率大於10%
and value2> syr//月營收年增率大於10%
and value3>= gr//毛利率大於45%
and GetField("每股稅後淨利(元)","Y")<epsy//最近一年稅後EPS小於1
and GetField("每股稅後淨利(元)","Q")<epsq//最近一季稅後EPS小於0.5
and GetField("每股營業額(元)","Y")>10//每股年營收大於10
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/高現金報酬率.xs

```xs
{@type:filter}
input:r1(5);		setinputname(1,"現金報酬率下限(%)");

settotalbar(3);

// 自由現金流
//
value1 = GetField("來自營運之現金流量","Q") - (GetField("固定資產","Q") - GetField("固定資產","Q")[1]);

// 淨利息費用

value2=GetField("利息支出","Q") - GetField("利息收入","Q");				

// 現金報酬率(%)
//
value3 = (value1 + value2) / GetField("企業價值","Q") * 100;

if value3 > r1 then ret = 1;
 
SetOutputName1("現金報酬率(%)");
OutputField1(value3);
```

---


---

## 腳本檔案: 選股/08.財報選股/高現金股利政策且營運仍佳.xs

```xs
{@type:filter}
input:peratio(17,"本益比上限倍數");
input:ratio(60,"現金股利佔股利之比重下限");
input:epsl(2,"預估本益EPS下限");
input:rate1(5,"累計營收成長率下限");
 
value1=GetField("累計營收年增率","M");//單位%
value2=GetField("現金股利佔股利比重","Y");
value3=GetField("營業利益","Q");//單位百萬;
value4=GetField("最新股本");//單位億;
value5=summation(value3,4)/(value4*10);//每股預估EPS

if value1>=rate1 //本業持續成長
and value2>=ratio //主要以現金股利為主
and value5>=EPSl //每股推估本業獲利高
and value5/close<=peratio //本益比低
then ret=1;
```

---


---

## 腳本檔案: 選股/08.財報選股/高護城河.xs

```xs
{@type:filter}
condition1=false;
condition2=false;
condition3=false;

if trueall(GetField("營業毛利率","Y") >=10,5)
then condition1=true;

if trueall(GetField("來自營運之現金流量","Y")>100,5)
then condition2=true;

if trueall(GetField("股東權益報酬率","Y")>20,5)
then condition3=true;

if condition1 and condition2 and condition3
then ret=1;

outputfield(1,GetField("營業毛利率","Y"),2,"營業毛利率%", order := 1);
```

---


---

## 腳本檔案: 選股/08.財報選股/高護城河的公司.xs

```xs
{@type:filter}
condition1=false;
condition2=false;
condition3=false;

//每年毛利率都大於10%
if trueall(GetField("營業毛利率","Y")>=10,4) then condition1=true;

//每年來自營運的現金流量都大於1億
if trueall(GetField("來自營運之現金流量","Y")>100,4) then condition2=true;

//股東權益報酬率大於15%
if trueall(GetField("股東權益報酬率","Y")>15,4) then condition3=true;

if condition1 and condition2 and condition3
then ret=1;
```

---


---

## 腳本檔案: 選股/09.時機操作/即將進入季節性多頭.xs

```xs
{@type:filter}
setbarfreq("AM");
settotalbar(3);

array:m1[7](0);
variable:x(0),count(0),avgup(0);

avgup = 0;

for x=1 to 7 begin
	m1[x]=(close[12*x-1]-close[12*x])/close[12*x];
end;
count=0;
for x=1 to 7 begin
	if m1[x]>0.02 then begin
		count=count+1;
		avgup=avgup+m1[x];
	end;
end;

if count>=6 and close>5 
and average(volume,20)>10000
then ret=1;
```

---


---

## 腳本檔案: 選股/09.時機操作/即將進入季節性空頭.xs

```xs
{@type:filter}
setbarfreq("AM");
settotalbar(3);

array:m1[7](0);
variable:x(0),count(0),avgdn(0);

avgdn=0;

for x=1 to 7 begin
	m1[x]=(close[12*x-1]-close[12*x])/close[12*x];
end;
count=0;
for x=1 to 7 begin
	if m1[x]<-0.02 then begin
		count=count+1;
		avgdn=avgdn+m1[x];
	end;
end;

if count>=6 and close>10
and average(volume,20)>20000
then ret=1;
```

---


---

## 腳本檔案: 選股/09.時機操作/可能有填權行情的股票.xs

```xs
{@type:filter}
value1=GetField("除權日期");
value2=GetField("每股稅後淨利(元)","Y");
if value1>date
and datediff(value1,date)<5
//除權後五天內
and trueall(close<close[1]*1.02,3)
//除權前後未大漲
and value2>=2
//每股稅後淨利大於2元
then ret=1;
outputfield(1,value1,0,"今年度除權日");
```

---


---

## 腳本檔案: 選股/09.時機操作/台幣升值受災股.xs

```xs
{@type:filter}
value1=GetField("每股營業額(元)","Y");
value2=GetField("外銷比率","Y");
if value1>20 and value2>90
//每股營收超過20且外銷比率超過九成
then ret=1;

outputfield(1,value1,0,"每股營收");
outputfield(2,value2,0,"外銷比率");
```

---


---

## 腳本檔案: 選股/09.時機操作/投信可能會作帳的股票.xs

```xs
{@type:filter}
setbarfreq("AD");
settotalbar(50);

input:r1(50,"股本上限單位億");
input:day(30,"天期");
input:r2(15,"區間買超天數");
input:r3(5000,"區間合計買超張數");
input:r4(30,"漲幅上限");

value1=GetField("投信買張","D");
value2=GetField("最新股本");//單位:億

condition1=false;
condition2=false;
condition3=false;

if value2<r1
then condition1=true;//股本小於50億元

value3=countif(value1>50,day);
if value3>=r2
then condition2=true;//近30天裡有超過15天買超

if summation(value1,day)>r3
then condition3=true;//近30天合計買超超過5000張

if condition1 and condition2 and condition3
and close<close[day-1]*(1+r4/100)
then ret=1;

outputfield(1,summation(value1,day),0,"投信累計買進", order := 1);
```

---


---

## 腳本檔案: 選股/09.時機操作/旺季來臨前.xs

```xs
{@type:filter}
settotalbar(40);

variable:W1(0),W2(0),W3(0),F1(0),F2(0),F3(0);

value1=GetField("月營收","M");//單位:億元

W1=(value1[12]+value1[13]+value1[14])/3;
W2=(value1[24]+value1[25]+value1[26])/3;
W3=(value1[36]+value1[37]+value1[38])/3;

F1=(value1[11]+value1[10]+value1[9])/3;
F2=(value1[23]+value1[22]+value1[21])/3;
F3=(value1[35]+value1[34]+value1[33])/3;

if F1>=W1*1.25 and F2>=W2*1.25 and F3>=W3*1.25

then ret=1;
```

---


---

## 腳本檔案: 選股/09.時機操作/長期都填權的股票.xs

```xs
{@type:filter}
input:N(5);

if getfield("除權息日期") = date then
begin
value1 = date;
value2 = c[1];
value3 = currentbar;
end;

if value1 > 0
  AND currentbar - value3 = N - 1
  AND c > value2
then
begin
value4 = date;
value5 = c;
condition1 = true;
end;

if condition1 then ret=1;

outputfield(1,value1,0,"除權息日期");
outputfield(2,value2,2,"除權息前一天收盤");
outputfield(4,value4,0,"N天後日期");
outputfield(5,value5,2,"N天後收盤");
```

---


---

## 腳本檔案: 選股/10.價值投資/PB跌到歷年低點區且低於0.8.xs

```xs
{@type:filter}
value1=GetField("股價淨值比","Y");
value2=lowest(value1,4);
if value1<value2*1.3 and value1<=0.8
then ret=1;

outputfield(1, GetField("股價淨值比","Y"),2, "PB比", order := -1);
```

---


---

## 腳本檔案: 選股/10.價值投資/低PB股的逆襲.xs

```xs
{@type:filter}
if close<15
and H = highest(H,20)
and close<lowest(low,20)*1.07
and highest(h,40)>close*1.1
then ret=1;

outputfield(1, GetField("股價淨值比","D"),2, "PB比", order := 1);
```

---


---

## 腳本檔案: 選股/10.價值投資/低本益比低PB高殖利率.xs

```xs
{@type:filter}
{本益比小於 15 倍 股價淨值比小於 2 倍 殖利率大於 3%}



if GetField("本益比","D") < 10 and
   GetField("股價淨值比","D") <1.5 and
   GetField("殖利率","D") > 3  and
   GetField("營收成長率","Q") >0 
    
    
   then ret=1;
```

---


---

## 腳本檔案: 選股/10.價值投資/低預估本益比攻勢發動.xs

```xs
{@type:filter}
value1=GetField("月營收","M");//單位:億元
value2=GetField("稅後淨利率","Q");
value3=GetField("最新股本");//單位:億元
if value3<>0 then
value6=(value1*value2*12)/(value3*10);//單月營收推估的本業EPS
if value6<>0 then 
value7=close/value6;

value4=GetField("總市值");
value5=average(GetField("總市值"),600);

if value4<value5*0.7
and close=highest(close,10)
then ret=1;

outputfield(1,value7,2,"推估本益比", order := -1);
```

---


---

## 腳本檔案: 選股/10.價值投資/價值雪球股.xs

```xs
{@type:filter}
if GetField("本益比","D") < 15 and
   GetField("股價淨值比","D") <2 and
   GetField("殖利率","D") > 3  and
   GetField("營收成長率","Q") >0 and
   GetField("營業利益","Q") >GetField("營業利益","Q")[1] and
   C > Lowest(L,255) + (highest(h,255)-Lowest(L,255))*0.5
   then ret=1;
   
outputfield(1,GetField("本益比","D"),1,"本益比");
outputfield(2,GetField("股價淨值比","D"),1,"PB比");
outputfield(3,GetField("殖利率","D"),2, "殖利率", order := 1);
```

---


---

## 腳本檔案: 選股/10.價值投資/新一代金牌定存股.xs

```xs
{@type:filter}
input:lowlimit(5,"年度獲利下限(億)");

value1=GetField("本期稅後淨利","Y");//單位:百萬
value2=lowest(value1,5);//五年獲利低點
value3=average(value1,5);//五年來平均獲利
if value1/100> lowlimit//獲利超過年度獲利下限
and value1/100<50//獲利沒有超過五十億元
and value1>value1[1]*0.9
and value1[1]>value1[2]*0.9//年度獲利連續兩年未衰退超過一成
and value2*1.3>value3
//五年來獲利最差的時候比平均值沒有掉超過三成

then ret=1;

outputfield(1, value1/100, 1, "稅後淨利(億)", order := 1);
```

---


---

## 腳本檔案: 選股/10.價值投資/月營收推估出的低本益比股.xs

```xs
{@type:filter}
input:peraito(10,"預估本益比上限");

value1=GetField("月營收","M");//單位:億元
value3=GetField("本期稅後淨利","Q");//單位百萬
value4=GetField("營業利益率","Q");
value5=GetField("最新股本");//單位:億元

condition1=false;
condition2=false;
if value5<>0 then
value6=(value1*value4*12)/(value5*100)*10;//單月營收推估的本業EPS
if value6<>0 then 
value7=close/value6;

if value7<peraito and value7>0 and value3>200
then ret=1;

outputfield(1,value7,0,"推估本益比", order := -1);
outputfield(2,value6,2,"推估EPS");
outputfield(3,value1,2,"月營收");
outputfield(4,value4,2,"營業利益率");
outputfield(5,value5,2,"最新股本");
```

---


---

## 腳本檔案: 選股/10.價值投資/本業推估本益比低於N.xs

```xs
{@type:filter}
input:peuplimit(15,"預估本益比上限");
value3= summation(GetField("營業利益","Q"),4); //單位百萬;
value4= GetField("最新股本");//單位億;
value5= value3/(value4*10);//每股預估EPS
if value5>0 and close/value5<=peuplimit
then ret=1;
```

---


---

## 腳本檔案: 選股/10.價值投資/每股流動資產遠大於股價.xs

```xs
{@type:filter}
input:percent(20);
setinputname(1,"每股易變現資產與股價間的落差比");
value1=GetField("現金及約當現金","Q");//百萬;
value2=GetField("短期投資","Q");//百萬
value3=GetField("應收帳款及票據","Q");//百萬
value4=GetField("長期投資","Q");//百萬
value5=GetField("負債總額","Q");//百萬
value6=GetField("最新股本");//單位: 億
value7=(value1+value2+value3+value4-value5)/(value6*10);
if value7>close*(1+percent/100)
then ret=1;
```

---


---

## 腳本檔案: 選股/10.價值投資/營運現金流量的持續積累.xs

```xs
{@type:filter}
input:ratio(50, "比例");//總市值減去淨值是十年營運現金流的的多少百分比, 單位是%

var: nv(0);
value1=GetField("來自營運之現金流量","q");//單位百萬
value2=GetField("總市值","D");//單位億
value3=summation(value1,8);//最近八季的營運現金流總和
value4=value3*5;//以最近兩年來推未來十年營運現金流總和

nv=GetField("股東權益總額","Q");//單位百萬
if value2*100-nv<value4*ratio/100
then ret=1;

outputfield(1, 100*value2/value4,1, "市值/現金流", order := -1);
```

---


---

## 腳本檔案: 選股/10.價值投資/股價距離合理價值很遠.xs

```xs
{@type:filter}
variable: idx(0), t(0);
input:r1(3, "假設未來十年營業利益年成長率");
input:r2(2, "未來十年平均年利率");
input:r3(100, "未來獲利折現合計淨值與市價比");

// 計算未來10年的營業利益折現值

value1=GetField("營業利益","Y");		//單位:百萬
value2=GetField("最新股本");			//單位:億
value3=GetField("每股淨值(元)","y");

value11 = maxlist(GetField("營業利益","Y"),GetField("營業利益","Y")[1],GetField("營業利益","Y")[2],GetField("營業利益","Y")[3],GetField("營業利益","Y")[4]);
value12 = minlist(GetField("營業利益","Y"),GetField("營業利益","Y")[1],GetField("營業利益","Y")[2],GetField("營業利益","Y")[3],GetField("營業利益","Y")[4]);

if trueall(value1>0,5) and (value11-value12)/value11<0.5 then begin
	t = 0;
	for idx =1 to 10 begin
		t = t + value1 * power(1+r1/100,idx)/power(1+r2/100,idx);
	end;

	// t=百萬,value2=億,換成每股
	value5 = t / value2 / 100;
	value6=close/(value3+value5);

	if value6<r3/100
	then ret=1;
end;

outputfield(1, value5, 2, "估算每股營業利益");
outputfield(2, value6, 1, "市價/淨值比", order := -1);
```

---


---

## 腳本檔案: 選股/10.價值投資/跌不下去的高殖利率股.xs

```xs
{@type:filter}
input:N(20, "天期");
 
condition1 = L = Lowest(L,N);
condition2 = H = Highest(H,N);
 
if condition2
//股價創區間以來高點
and	TrueAll(Condition1=false,N)
//這段區間都未破底
and close<close[N-1]*1.05
and volume>600
//區間股價漲幅不大
then ret=1;

outputfield(1, GetField("股東權益報酬率","Q"),2, "股東權益%", order := 1);
outputfield(2, GetField("現金股利","Y"),2, "現金股利");
```

---


---

## 腳本檔案: 選股/11.選股機器人/上游價格指標趨勢向上.xs

```xs
{@type:filter}
input: Period(20, "天期"); 
Condition1 = rateofchange(GetField("上游股價指標"), period) >= Period; 
Condition2 = GetField("上游股價指標") > GetField("上游股價指標")[Period/2]; 
Condition3 = GetField("上游股價指標") > average(GetField("上游股價指標"), period); 
ret = condition1 and condition2 and condition3; 

outputfield(1,rateofchange(GetField("上游股價指標","D"),period),2,"上游漲幅%", order := 1);
```

---


---

## 腳本檔案: 選股/11.選股機器人/下游價格指標趨勢向上.xs

```xs
{@type:filter}
input: Period(20, "天期"); 
Condition1 = rateofchange(GetField("下游股價指標"), period) >= Period; 
Condition2 = GetField("下游股價指標") > GetField("下游股價指標")[Period/2]; 
Condition3 = GetField("下游股價指標") > average(GetField("下游股價指標"), period); 
ret = condition1 and condition2 and condition3; 

outputfield(1,rateofchange(GetField("下游股價指標","D"),Period),2,"下游漲幅%", order := 1);
```

---


---

## 腳本檔案: 選股/11.選股機器人/中小型股整理結束.xs

```xs
{@type:filter}
setbarfreq("AD");

//盤整後噴出
input: Periods(20,"計算期數");
input: Ratio(3,"近期波動幅度%");
input: Direction(1,"方向:1突破 -1跌破");
 
condition1 = false;

if (highest(high[1],Periods-1) - lowest(low[1],Periods-1))/close[1] <= ratio*0.01 
then condition1=true//近期波動在?%以內
else return;

if condition1 and Direction > 0 and high = highest(high, Periods)
and close>close[1]*1.02
then ret=1;//盤整後往上突破

outputfield(1,highest(high[1],Periods-1),2,"整理區高點", order := -1);
```

---


---

## 腳本檔案: 選股/11.選股機器人/創百日新高但距低點不遠.xs

```xs
{@type:filter}
//說明：今天的收盤價創百日的收盤價新高，但收盤價距離區間低點不遠

input:day(200,"計算區間");
input:day1(20,"短線漲幅計算區間");
input:percents(10,"距離區間最低點漲幅");

value1=lowest(close,day1);
if close=highest(close,day)
and value1*(1+percents/100)>=close
and close >= value1*1.05
and volume >= average(volume[1], 5)

then ret=1;

outputfield(1, value1, 2, "區間低點", order := -1);
```

---


---

## 腳本檔案: 選股/11.選股機器人/可能由盈轉虧.xs

```xs
{@type:filter}
// 計算最新一期月營收的日期(mm=月份)
//
variable: mm(0);
mm = datevalue(getfielddate("月營收","M"),"M");

// 預估最新一季的季營收(單位=億)
//
if mm=1 or mm=4 or mm=7 or mm=10
then value1=GetField("月營收","M") * 3;
if mm=2 or mm=5 or mm=8 or mm=11
then value1=GetField("月營收","M") * 2 + GetField("月營收","M")[1];
if mm=3 or mm=6 or mm=9 or mm=12
then value1=GetField("月營收","M")+GetField("月營收","M")[1]+GetField("月營收","M")[2];

// 預估獲利(單位=百萬) = 季營收 * 毛利率 - 營業費用
//
value2 = value1 * GetField("營業毛利率","Q") - GetField("營業費用","Q");

ret = 1;

outputfield(1,value2 / 100,2,"預估單季本業獲利(億)", order := 1);
```

---


---

## 腳本檔案: 選股/11.選股機器人/可能轉虧為盈.xs

```xs
{@type:filter}
// 計算最新一期月營收的日期(mm=月份)
//
variable: mm(0);
mm = datevalue(getfielddate("月營收","M"),"M");

// 預估最新一季的季營收(單位=億)
//
if mm=1 or mm=4 or mm=7 or mm=10
then value1=GetField("月營收","M") * 3;
if mm=2 or mm=5 or mm=8 or mm=11
then value1=GetField("月營收","M") * 2 + GetField("月營收","M")[1];
if mm=3 or mm=6 or mm=9 or mm=12
then value1=GetField("月營收","M")+GetField("月營收","M")[1]+GetField("月營收","M")[2];

// 預估獲利(單位=百萬) = 季營收 * 毛利率 - 營業費用
//
value2 = value1 * GetField("營業毛利率","Q") - GetField("營業費用","Q");

if value2 > 0 and GetField("營業利益","Q") < 0 then
ret = 1;

outputfield(1,value1,2,"預估單季營收(億)", order := 1);
outputfield(2, value2 / 100,2, "預估單季本業獲利(億)");
```

---


---

## 腳本檔案: 選股/11.選股機器人/外資先前沒買，突然連買三天.xs

```xs
{@type:filter}
setbarfreq("AD");

input: _period(20, "期間");
input: _ratio(5, "買超占成交比重");

condition1 = trueall(GetField("外資買賣超","D")[3]=0, _period);
condition2 = trueall(GetField("外資買賣超","D")*100/volume>=_ratio,3);

if condition1 and condition2 
then ret=1;

value1 = Summation(GetField("外資買賣超","D"), 3) / Summation(Volume, 3) * 100;
outputfield(1,value1,2,"外資買超%", order := 1);
```

---


---

## 腳本檔案: 選股/11.選股機器人/多次到頂而破.xs

```xs
{@type:filter}
setbarfreq("AD");

input:HitTimes(3,"設定觸頂次數");
input:RangeRatio(2,"設定頭部區範圍寬度%");
input:Length(60,"計算期數");

variable: theHigh(0);
variable: HighLowerBound(0);
variable: TouchRangeTimes(0);

//找到過去其間的最高點
theHigh = Highest(High[1],Length);
value1=highestbar(high[1],length);

// 設為瓶頸區間上界
HighLowerBound = theHigh *(100-RangeRatio)/100;

//回算在此區間中 進去瓶頸區的次數
TouchRangeTimes = CountIF(High[1] > HighLowerBound, Length-value1);

Condition1 = TouchRangeTimes >= HitTimes;
Condition2 = close > theHigh;
Condition3 = close[length]*1.2<thehigh;

condition4=false;
if Condition1 and Condition2 and condition3
then condition4=true;

if barslast(condition4=true)=1
then ret=1;

outputfield(1, theHigh, 2, "區間高點", order := -1);
```

---


---

## 腳本檔案: 選股/11.選股機器人/多頭下起漲前的籌碼收集.xs

```xs
{@type:filter}
setbarfreq("AD");

value1=GetField("分公司買進家數");
value2=GetField("分公司賣出家數");
value3=value2-value1;
value4=countif(value3>20,10);
if value4>6 and close[30]>close*1.1
then ret=1;

outputfield(1,value1,0,"買進家數", order := -1);
outputfield(2,value2,0,"賣出家數");
```

---


---

## 腳本檔案: 選股/11.選股機器人/天價上影線賣出訊號.xs

```xs
{@type:filter}
setbarfreq("AD");

variable:Kprice(0);

if H > O*1.03 and C <O and H = highest(H,255) then Kprice = L;

condition1 = c crosses below Kprice;
condition2 = average(volume[1], 5) >= 500;
ret = condition1 and condition2;

outputfield(1,Kprice,2,"關卡價", order := -1);
```

---


---

## 腳本檔案: 選股/11.選股機器人/投信初介入.xs

```xs
{@type:filter}
setbarfreq("AD");

input: day(30, "投信交易期間");

value1 = summation(GetField("投信買賣超")[1], day); 
value2 = summation(volume[2], day);

condition1 = value1 < value2 * 0.02;
//先前投信不怎麼買這檔股票

condition2 = GetField("投信買賣超")>= volume[1] * 0.15;
//投信開始較大買超

condition3 = H > H[1];
//買了股價有往上攻

condition4 = C > C[1];
//今天收盤有往上走

condition5=close<close[10]*1.05;

RET = condition1 and condition2 and condition3 and condition4 and condition5;

outputfield(1,GetField("投信買賣超","D"),0,"投信買超", order := 1);
```

---


---

## 腳本檔案: 選股/11.選股機器人/投信掃貨.xs

```xs
{@type:filter}
input: pastDays(5, "計算天數");
input: _BuyRatio(10, "買超佔比例(%)");

variable: SumForce(0);
variable: SumTotalVolume(0);

SumForce = Summation(GetField("投信買賣超"), pastDays);
sumTotalVolume = Summation(Volume, pastDays);
value1 = SumForce / SumTotalVolume * 100;
if value1 > _BuyRatio then ret =1;

outputfield(1,value1,2,"投信買超%", order := 1);
```

---


---

## 腳本檔案: 選股/11.選股機器人/投信第一天大買.xs

```xs
{@type:filter}
setbarfreq("AD");

input: v1(500, "投信估計持股上限(張)");

value1=GetField("投信持股","D");
value2=GetField("投信買賣超","D");

if value1 < v1 and value2 > VOLUME*0.2
then ret=1;

outputfield(1,GetField("投信買賣超","D"),0,"投信買超", order := 1);
```

---


---

## 腳本檔案: 選股/11.選股機器人/月營收年增率移動平均黃金交叉b.xs

```xs
{@type:filter}
value1=GetField("月營收年增率","M");

if average(value1,4) crosses over average(value1,12)
and value1 > 0
then ret=1;

outputfield(1,value1,2,"月營收年增率%", order := 1);
```

---


---

## 腳本檔案: 選股/11.選股機器人/殺過頭.xs

```xs
{@type:filter}
setbarfreq("AD");

input:day(5,"短期天數");
input:period(20,"波段天數");
input:r1(20,"波段最低跌幅");
input:r2(10,"短期最低跌幅");
input:r3(2,"本日急拉幅度");
input:v1(1000,"成交量下限");

condition1=false;
condition2=false;
condition3=false;
 
if highest(high,period)>=close[1]*(1+r1/100)
then condition1=true;
 
if highest(high,day)>=close[1]*(1+r2/100)
then condition2=true;
 
if close>=close[1]*(1+r3/100) and v1>=1000
then condition3=true;
 
if condition1 and condition2 and condition3
then ret=1;

outputfield(1,lowest(low,period),2,"前波低點", order := -1);
```

---


---

## 腳本檔案: 選股/11.選股機器人/毛利率創一年新高.xs

```xs
{@type:filter}
value1=GetField("營業毛利率","Q");
if value1=highest(value1,12)
then ret=1;
```

---


---

## 腳本檔案: 選股/11.選股機器人/毛利率沒掉的兇.xs

```xs
{@type:filter}
input:ratio(10,"毛利率單季衰退幅度上限");
input:period(10,"計算的期間，單位是季");

value1=GetField("營業毛利率","Q");
if trueall(value1>value1[1]*(1-ratio/100),period)
then ret=1;
```

---


---

## 腳本檔案: 選股/11.選股機器人/烏龜交易法則之買進訊號.xs

```xs
{@type:filter}
setbarfreq("AD");

condition1=false;
condition2=false;
 
if high=highest(high,100)and barslast(high=highest(high,100))[1]>100
then condition1=true; 
//創百日新高且上一次發生時是在100個交易日之前

if average(volume[1], 5) >= 1000
then condition2=true;

//五日移動平均量大於千張
if condition1 and condition2
then ret=1;
 
outputfield(1,highest(high,100),2,"突破高點", order := -1);
```

---


---

## 腳本檔案: 選股/11.選股機器人/烏龜交易法則之賣出訊號.xs

```xs
{@type:filter}
setbarfreq("AD");

condition1=false;
condition2=false;
 
if L=lowest(L,100)and barslast(L=lowest(L,100))[1]>100
then condition1=true; 
//創百日新低且上一次發生時是在100個交易日之前

if average(volume[1], 5) >= 1000
then condition2=true;

//五日移動平均量大於千張
if condition1 and condition2
then ret=1;
 
outputfield(1,lowest(L,100),2,"跌破低點", order := -1);
```

---


---

## 腳本檔案: 選股/11.選股機器人/突破糾結均線.xs

```xs
{@type:filter}
setbarfreq("AD");

input: shortlength(5); setinputname(1,"短期均線期數");
input: midlength(10); setinputname(2,"中期均線期數");
input: Longlength(20); setinputname(3,"長期均線期數");
input: Percent(5);  setinputname(4,"均線糾結區間%");
input: XLen(20);  setinputname(5,"均線糾結期數");

input: Volpercent(25);  setinputname(6,"放量幅度%");//帶量突破的量是超過最長期的均量多少%
variable: shortaverage(0);
variable: midaverage(0);
variable: Longaverage(0);
variable: AvgHLp(0),AvgH(0),AvgL(0);

shortaverage = average(close,shortlength);
midaverage = average(close,midlength);
Longaverage = average(close,Longlength);
		
AvgH = maxlist(shortaverage,midaverage,Longaverage);
AvgL = minlist(shortaverage,midaverage,Longaverage);

if AvgL > 0 then AvgHLp = 100*AvgH/AvgL -100;

condition1 = trueAll(AvgHLp < Percent,XLen);
condition2 = V > average(V[1],XLen)*(1+Volpercent/100) ;
condition3 = C > AvgH *(1.02) and H > highest(H[1],XLen);
condition4 = average(volume[1], 5) >= 1000; 

ret = condition1 and condition2 and condition3 and condition4;

outputfield(1,AvgH,2,"均線上緣", order := -1);
outputfield(2,AvgL,2,"均線下緣");
```

---


---

## 腳本檔案: 選股/11.選股機器人/總市值位於歷史低檔區.xs

```xs
{@type:filter}
setbarfreq("AD");

input:period(1250,"計算天數");
input:ratio(10,"距離低點幅度");

value1=GetField("總市值");
value2=lowest(GetField("總市值"),period);

if value1<value2*(1+ratio/100)
//總市值距離過去一段時間最低點沒有差多遠
then begin

	if close=highest(close,20)
	and close<close[19]*1.07
	and close crosses over average(close,20)
	and close<=15

	then ret=1;

end;

outputfield(1, value1, 2, "總市值(億)", order := -1);
```

---


---

## 腳本檔案: 選股/11.選股機器人/股價領先大盤創新高.xs

```xs
{@type:filter}
input: Length(20, "布林通道天數");
input: BandRange(2, "上下寬度");
variable: up(0);

Condition1 = GetSymbolField("TSE.TW","收盤價","D") > average(GetSymbolField("TSE.TW","收盤價","D"),10);
Condition2 = average(GetSymbolField("TSE.TW","收盤價","D"),5) > average(GetSymbolField("TSE.TW","收盤價","D"),20);

value1=close/GetSymbolField("TSE.TW","收盤價","D");
up = bollingerband(value1, Length, BandRange);
Condition3 = TrueAll(value1 >= up, 3);

// 成交量判斷
Condition99 = Average(Volume[1], 100) >= 1000;

if Condition1 And Condition2 And Condition3 And Condition99 then ret=1;

outputfield(1, rateofchange(c,5), 2, "5日漲幅%", order := 1);
outputfield(2, rateofchange(GetSymbolField("TSE.TW","收盤價","D"),5), 2, "大盤5日漲幅%");
```

---


---

## 腳本檔案: 選股/11.選股機器人/週轉率高點買進.xs

```xs
{@type:filter}
setbarfreq("AD");

value1=GetField("成交金額");
value2=GetField("總成交次數","D");
if value2>0 then value3=value1/value2;

if value3=highest(value3,200)
and close>close[1]*1.025
and close[2]<close[12]*1.05
and volume>2000
then ret=1;

outputfield(1, GetField("週轉率","D"), 2, "週轉率%", order := 1);
```

---


---

## 腳本檔案: 選股/11.選股機器人/除權後的填權行情.xs

```xs
{@type:filter}
if  close[1]*1.1<close[20]
and close>close[1]*1.025
and volume>average(volume,20)
then ret=1;

value1=getbaroffset(dateadd(GetField("除權息日期"),"D",-1));
outputfield(1,close[value1],2,"除權參考價");
outputfield(2,-RateOfChange(c,value1),2,"貼權率%", order := 1);
```
