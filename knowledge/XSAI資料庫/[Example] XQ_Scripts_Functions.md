# XQ 官方函數腳本範例庫

共 224 個函數腳本範例。

---

## 腳本檔案: 函數/Array函數/ArrayLinearRegSlope.xs

```xs
{@type:function}
{
	傳入Array來計算LinearRegression的Slope
	最新一期的資料放在ThePriceArray[1]
}

Input: ThePriceArray[DataLength](NumericArray);
Input: Length(numericsimple, "統計天期");

if DataLength < Length then RaiseRunTimeError("Array的長度不能小於Length");

variable: SumX(0), //和
      SumX2(0), //平方和
      SumY(0),
      SumXY(0);

SumX = Length * (Length+1)/2;
SumX2 = Length * (Length+1)*(2*Length+1)/6;


variable: Xi(0);

SumXY=0; SumY=0;
for Xi = 1 to Length
Begin
   SumXY += Xi* ThePriceArray[Length-Xi+1];
   SumY  += ThePriceArray[Length-Xi+1];
End;

retval = IFF((Length*SumX2 - Square(SumX)) <> 0,
             (Length*SumXY - SumX*SumY) / (Length*SumX2 - Square(SumX)),
			 0);
```

---


---

## 腳本檔案: 函數/Array函數/ArrayMASeries.xs

```xs
{@type:function}
{
	把某個數值序列的MA轉成Array
	
	範例:
	
	Array: MAArray[](0);
	
	ArrayMASeries(Close, 10, MAArray);
	
    // Array_GetMaxIndex(MAArray) = 10	
	// MAArray[1] = MA(Close, 10), 
	// MAArray[2] = MA(Close[1], 10),
	// MAArray[3] = MA(Close[2], 10),
	// ...
}

input: TheSeries(numericseries, "序列");
input: MALength(numericsimple, "MA天期");
Input: TargetArray[X](NumericArrayRef);

Array_SetMaxIndex(TargetArray, MALength);

var: acc(0), idx(0);
acc = 0;

for idx = 0 to MALength-1 begin
	acc = acc + TheSeries[idx];
end;

for idx = 0 to MALength-1 begin
	TargetArray[idx+1] = acc / MALength;
	acc = acc - TheSeries[idx];
	acc = acc + TheSeries[MALength + idx];
end;
```

---


---

## 腳本檔案: 函數/Array函數/ArraySeries.xs

```xs
{@type:function}
{
	把某個數值序列轉成Array
	

	範例:
	
	Array: CloseArray[](0);
	
	ArraySeries(Close, 10, CloseArray);
	
    // Array_GetMaxIndex(CloseArray) = 10	
	// CloseArray[1] = Close, CloseArray[2] = Close[1], CloseArray[3] = Close[2], ..
}

input: TheSeries(numericseries, "序列");
input: Length(numericsimple, "序列長度");
Input: TargetArray[X](NumericArrayRef);

Array_SetMaxIndex(TargetArray, Length);

Var: idx(0);
for idx = 0 to Length - 1 begin
	TargetArray[idx+1] = TheSeries[idx];
end;
```

---


---

## 腳本檔案: 函數/Array函數/ArrayXDaySeries.xs

```xs
{@type:function}
{
	以Array儲存跨頻率的序列值，傳入一個序列
	

	範例:
	
	Array: CloseArray[](0);
	
	ArrayXDaySeries(GetField("收盤價","D"),SBB_length,_DayValue);
}

Input: TheSeries(numericseries, "序列");
Input: SBB_length(NumericSimple, "SetBackBar的筆數");
Input: TargetArray[X](NumericArrayRef);
Var: idx(0),_length(0),_xf_CurrentBar(0);
_length = GetBarBack("D");
_xf_CurrentBar = xf_GetCurrentBar("D");

if _length < SBB_length then raiseRunTimeError("新上市櫃商品資料引用筆數不足，所以不允計算");

if currentBar = 1 then begin
	Array_SetMaxIndex(TargetArray, _length);
	for idx = 0 to _length - 1 begin
		TargetArray[idx + 1] = TheSeries[idx];
	end;
end else begin
	if _xf_CurrentBar > _xf_CurrentBar[1] then begin
		Array_Copy(TargetArray, 1, TargetArray, 2, _length - 1);
	end;
	TargetArray[1] = TheSeries[0];
end;
```

---


---

## 腳本檔案: 函數/交易相關/CalcVWAPDistribution.xs

```xs
{@type:function}
{
	計算過去N日的VWAP分佈
	
	請傳入
	
	- 計算天數
	- 開始時間, 例如091000
	- 結束時間, 例如095900 (請注意請以1分K的Time為基準)
	- 一個array, 用來儲存上述指定區間內每分鐘的累積成交量分佈%, 
	  - CalcVWAPDistribution會自動設定array的大小,
	  - array[1]是從開始時間後第1分鐘的累計成交量%, array[2]是從開始時間到後第2分鐘的累計成交量%, etc.
	  - 請注意這是一個累積的數值, 例如array[1] = 2.5, array[2] = 5.4, array[3] = 7.0, ... array[最後一個]=100.0,	  
}

input: totaldays(numericsimple, "計算天數");
input: start_hhmmss(numericsimple, "開始時間, 例如091000");
input: end_hhmmss(numericsimple, "結束時間, 例如095900");
input: dist_array[X](numericarrayref, "回傳成交量分佈%");

var: total_minutes(0);
array: day_dist[](0);		{ 儲存每一日的成交量分佈% }

{ 請注意: 不支援跨日的計算 }

if start_hhmmss >= end_hhmmss then raiseruntimeerror("開始時間必須小於結束時間");

total_minutes = TimeDiff(end_hhmmss, start_hhmmss, "M") + 1;	{ 頭尾都算 }

Array_SetMaxIndex(day_dist, total_minutes);
Array_SetMaxIndex(dist_array, total_minutes);

var: lastdate(0);
lastdate = GetFieldDate("Date", "1");	// 目前1分鐘K棒的TDate

var: idx(0), days(0);
var: idx_daystart(0), idx_dayend(0);

Array_SetValRange(dist_array, 0, total_minutes, 0);

{ 先找到昨日的最後一筆, 從這裡開始統計N日的資料 }
idx = 1;
while GetFieldDate("Date", "1")[idx] = lastdate begin
	idx = idx + 1;
end;

days = 0;
while days < totaldays begin
	lastdate = GetFieldDate("Date", "1")[idx];	
	idx_daystart = -1; 
	idx_dayend = -1;
	while GetFieldDate("Date", "1")[idx] = lastdate begin
		if GetField("Time", "1")[idx] = end_hhmmss then idx_dayend = idx;
		if GetField("Time", "1")[idx] = start_hhmmss then idx_daystart = idx;	
		idx = idx + 1;
	end;
	if idx_daystart = -1 or idx_dayend = -1 then raiseruntimeerror("Internal error");

	{print(
		"days=", numtostr(days, 0), 
		"date=", formatdate("yyyy/MM/dd", lastdate), 
		"idx_daystart=", numtostr(idx_daystart, 0), 
		"idx_dayend=", numtostr(idx_dayend, 0),
		""
	);}

	{ 收集從idx_start到idx_end之間的成交量分佈 }
	
	var: totalvolume(0), jdx(0);
	
	totalvolume = 0;
	day_dist[0] = 0;
	for jdx = idx_daystart downto idx_dayend begin
		{ 每一筆 = 前一筆的累積 + 這一分K的成交量 }
		day_dist[idx_daystart - jdx + 1] = GetField("Volume", "1")[jdx] + day_dist[idx_daystart - jdx];

		{print(
			"Index=", numtostr(idx_daystart - jdx + 1, 0),
			"day_dist[]=", numtostr(day_dist[idx_daystart - jdx + 1], 0),
			"Date=", FormatDate("yyyy/MM/dd", GetField("Date", "1")[jdx]),
			"Time=", FormatTime("HH:mm", GetField("Time", "1")[jdx]),
			"Vol=", numtostr(GetField("Volume", "1")[jdx], 0),
			""
		);}
		
	end;	
		
	for jdx = idx_daystart downto idx_dayend begin
		{ 換算成累積到目前為止的成交量% }
		day_dist[idx_daystart - jdx + 1] = day_dist[idx_daystart - jdx + 1] * 100 / day_dist[idx_daystart - idx_dayend + 1];
		
		{ 累積到 dist_array }
		dist_array[idx_daystart - jdx + 1] = dist_array[idx_daystart - jdx + 1] + day_dist[idx_daystart - jdx + 1];
		
		{print(
			"Index=", numtostr(idx_daystart - jdx + 1, 0),
			"day_dist[]=", numtostr(day_dist[idx_daystart - jdx + 1], 2),
			"dist_array[]=", numtostr(dist_array[idx_daystart - jdx + 1], 2),
			""
		);}
	end;
	
	days = days + 1;
end;	

{ 回傳dist_array = 近N日的平均值 }
for jdx = 1 to total_minutes begin
	dist_array[jdx] = dist_array[jdx] / totaldays;
end;
```

---


---

## 腳本檔案: 函數/交易相關/EnterMarketCloseTime.xs

```xs
{@type:function_bool}
{
	判斷是否已經進入收盤階段: 用來判斷不再進場 or 平倉當日部位
	
	使用時須傳入N, 代表在最後可以送單前N分鐘就認定進入收盤階段, 
	例如如果傳1, 而且是台股的話, 那在13:24:00就會回傳True, 代表已經進入收盤階段


	請注意: 這個函數只支援台股, 以及台灣期貨市場內的常用商品, 也不考慮部分外匯期貨 or 其他市場期貨, 例如東証指
}

input: exit_period(numericsimple, "收盤前N分鐘");

var: market_close_time(0);		{ 市場收盤時間 }
var: market_lasttrade_time(0);	{ 最後可交易時間 }

if symbolexchange = "TW" then begin
	market_close_time = 134000;		{ 往後延長一點, 處理Tick可能延後收到的情形 }
	market_lasttrade_time = 132500;
end else if symbolexchange = "TF" then begin
	if daystoexpirationtf = 0 then begin
		market_lasttrade_time = 133000;
		market_close_time = 134000;	{ 往後延長一點, 處理Tick可能延後收到的情形 }
	end else begin	
		market_lasttrade_time = 134500;
		market_close_time = 135000; { 往後延長一點, 處理Tick可能延後收到的情形 }
	end;	
end else
	raiseruntimeerror("不支援此商品");

{ 往前推算N分鐘 }
market_lasttrade_time = TimeAdd(market_lasttrade_time, "M", -1 * exit_period);

if CurrentTime >= market_lasttrade_time and CurrentTime <= market_close_time then retval = true else retval = false;
```

---


---

## 腳本檔案: 函數/價格取得/AvgPrice.xs

```xs
{@type:function}
SetBarMode(1);

AvgPrice = (Open + High + Low + Close) /4;
```

---


---

## 腳本檔案: 函數/價格取得/CloseD.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

CloseD = GetField("Close","D")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/CloseH.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

CloseH = GetField("Close","H")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/CloseM.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

CloseM = GetField("Close","M")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/CloseQ.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

CloseQ = GetField("Close","Q")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/CloseW.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

CloseW = GetField("Close","W")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/CloseY.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

CloseY = GetField("Close","Y")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/FastHighest.xs

```xs
{@type:function}
SetBarMode(1);

input: thePrice(numericseries),Length(numericsimple);

variable: _Output(0);

Extremes(thePrice, Length, 1, _Output, value2);

FastHighest = _Output;
```

---


---

## 腳本檔案: 函數/價格取得/FastLowest.xs

```xs
{@type:function}
SetBarMode(1);

input: thePrice(numericseries), Length(numericsimple);
variable: _Output(0);

Extremes(thePrice, Length, -1, _Output, value2);

FastLowest = _Output;
```

---


---

## 腳本檔案: 函數/價格取得/HighD.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

HighD = GetField("High","D")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/Highest.xs

```xs
{@type:function}
SetBarMode(1);

input: thePrice(numericseries),Length(numericsimple);

variable: _Output(0);

Extremes(thePrice, Length, 1, _Output, value2);

Highest = _Output;
```

---


---

## 腳本檔案: 函數/價格取得/HighH.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

HighH = GetField("High","H")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/HighM.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

HighM = GetField("High","M")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/HighQ.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

HighQ = GetField("High","Q")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/HighW.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

HighW = GetField("High","W")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/HighY.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

HighY = GetField("High","Y")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/LowD.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

LowD = GetField("Low","D")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/Lowest.xs

```xs
{@type:function}
SetBarMode(1);

input: thePrice(numericseries), Length(numericsimple);

variable: _Output(0);

Extremes(thePrice, Length, -1, _Output, value2);

Lowest = _Output;
```

---


---

## 腳本檔案: 函數/價格取得/LowH.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

LowH = GetField("Low","H")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/LowM.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

LowM = GetField("Low","M")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/LowQ.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

LowQ = GetField("Low","Q")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/LowW.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

LowW = GetField("Low","W")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/LowY.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

LowY = GetField("Low","Y")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/OpenD.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

OpenD = GetField("Open","D")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/OpenH.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

OpenH = GetField("Open","H")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/OpenM.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

OpenM = GetField("Open","M")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/OpenQ.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

OpenQ = GetField("Open","Q")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/OpenW.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

OpenW = GetField("Open","W")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/OpenY.xs

```xs
{@type:function}
SetBarMode(1);

input: PeriodsAgo(numericsimple);

OpenY = GetField("Open","Y")[PeriodsAgo];
```

---


---

## 腳本檔案: 函數/價格取得/TrueHigh.xs

```xs
{@type:function}
SetBarMode(1);

if Close[1] > High then TrueHigh = Close[1]
else TrueHigh = High;
```

---


---

## 腳本檔案: 函數/價格取得/TrueLow.xs

```xs
{@type:function}
SetBarMode(1);

if Close[1] < Low then TrueLow = Close[1]
else TrueLow = Low;
```

---


---

## 腳本檔案: 函數/價格取得/TypicalPrice.xs

```xs
{@type:function}
SetBarMode(1);

TypicalPrice = (High + Low + Close) /3;
```

---


---

## 腳本檔案: 函數/價格取得/WeightedClose.xs

```xs
{@type:function}
SetBarMode(1);

WeightedClose = (2 * Close + High + Low) / 4;
```

---


---

## 腳本檔案: 函數/價格計算/Average.xs

```xs
{@type:function}
SetBarMode(1);

input:thePrice(numericseries); //"價格序列"
input:Length(numericsimple);   //"計算期間"
 
if  Length > 0 then
	Average = Summation(thePrice, Length) / Length
else  
	Average =0;
```

---


---

## 腳本檔案: 函數/價格計算/AvgDeviation.xs

```xs
{@type:function}
SetBarMode(1);

input:thePrice(numericseries); //"價格序列"
input:Length(numericsimple);   //"計算期間"

variable:	truesum(0),
			averageprice(0),
			counter(0);
truesum = 0;
averageprice = Average(thePrice,Length);

for counter = 0 to Length - 1  begin
	truesum = truesum + AbsValue(thePrice[counter] - averageprice);
end;

AvgDeviation = truesum / Length;
```

---


---

## 腳本檔案: 函數/價格計算/DwLimit.xs

```xs
{@type:function}
SetBarMode(1);

input:refPrice(numericsimple);
variable:obup1(0),obdw1(0),STOCKUP(0),STOCKDW(0);

if date < 20150601 then begin
	obup1= refPrice*1.07;
	obdw1= refPrice*0.93;
end else begin
	obup1= refPrice*1.1;
	obdw1= refPrice*0.9;
end;

if (obup1<10 and obdw1<10) then begin
	STOCKUP = ((floor((floor(obup1*100)*100)))/100)/100;
	STOCKDW = ((floor((ceiling(obdw1*100)*100)))/100)/100;
end else if (obup1>=10 and obdw1<10) then begin
	STOCKUP = ((floor(((floor(obup1/0.05)*0.05)*100)*100))/100)/100;
	STOCKDW = ((floor((ceiling(obdw1*100)*100)))/100)/100;
end else if (obup1>=10 and obdw1>=10 and obup1<50 and obdw1<50) then begin
	STOCKUP = ((floor(((floor(obup1/0.05)*0.05)*100)*100))/100)/100;
	STOCKDW = ((floor(((ceiling(obdw1/0.05)*0.05)*100)*100))/100)/100;
end else if (obup1>=50 and obdw1<50 ) then begin
	STOCKUP = ((floor(((floor(obup1/0.1)*0.1)*100)*100))/100)/100;
	STOCKDW = (ceiling(obdw1/0.05)*0.05);
end else if (obup1>=50 and obdw1>=50 and obup1<100 and obdw1<100) then begin
	STOCKUP = ((floor(((floor(obup1/0.1)*0.1)*100)*100))/100)/100;
	STOCKDW = ((floor(((ceiling(obdw1/0.1)*0.1)*100)*100))/100)/100;
end else if (obup1>=100 and obdw1<100 ) then begin
	STOCKUP = ((floor(((floor(obup1/0.5)*0.5)*100)*100))/100)/100;
	STOCKDW = ((floor(((ceiling(obdw1/0.1)*0.1)*100)*100))/100)/100;
end else if (obup1>=100 and obdw1>=100 and obup1<500 and obdw1<500) then begin
	STOCKUP = ((floor(((floor(obup1/0.5)*0.5)*100)*100))/100)/100;
	STOCKDW = ((floor(((ceiling(obdw1/0.5)*0.5)*100)*100))/100)/100;
end else if (obup1>=500 and obdw1<500) then begin
	STOCKUP = ((floor(((floor(obup1/0.5)*0.5)*100)*100))/100)/100;
	STOCKDW = ((floor(((ceiling(obdw1/0.1)*0.1)*100)*100))/100)/100;
end else if (obup1>=500 and obdw1>=500 and obup1<1000 and obdw1<1000) then begin
	STOCKUP = ((floor(((floor(obup1/ 1)* 1)*100)*100))/100)/100;
	STOCKDW = ((floor(((ceiling(obdw1/ 1)* 1)*100)*100))/100)/100;
end else if (obup1>=1000 and obdw1<1000) then begin
	STOCKUP = ((floor(((floor(obup1/5)*5)*100)*100))/100)/100;
	STOCKDW = ((floor(((ceiling(obdw1/ 1)* 1)*100)*100))/100)/100;
end else if (obup1>=1000 and obdw1>=1000) then begin
	STOCKUP = ((floor(((floor(obup1/5)*5)*100)*100))/100)/100;
	STOCKDW = ((floor(((ceiling(obdw1/5)*5)*100)*100))/100)/100;
end;

DwLimit = STOCKDW;
```

---


---

## 腳本檔案: 函數/價格計算/EMA.xs

```xs
{@type:function}
SetBarMode(2);

input:thePrice(numericseries); //"價格序列"
input:Length(Numeric);   //"計算期間"

variable:  Factor(0);

if length + 1 = 0 then Factor = 1 else Factor = 2 / (Length + 1);

if CurrentBar = 1 then
	EMA = thePrice
else if CurrentBar <= Length then
    EMA = (thePrice + (EMA[1]*(CurrentBar-1)))/CurrentBar	
else
	EMA = EMA[1] + Factor * (thePrice - EMA[1]);
```

---


---

## 腳本檔案: 函數/價格計算/Range.xs

```xs
{@type:function}
SetBarMode(1);

Range = High - Low;
```

---


---

## 腳本檔案: 函數/價格計算/RateOfChange.xs

```xs
{@type:function}
SetBarMode(1);

input:thePrice(numericseries); //"價格序列"
input:Length(numericsimple);   //"計算期間"


if thePrice[Length] <> 0 then RateOfChange = (thePrice / absvalue(thePrice[Length]) - sign(thePrice[Length])) * 100
else RateOfChange = 0;
```

---


---

## 腳本檔案: 函數/價格計算/ReadTicks.xs

```xs
{@type:function}
{
    讀取從上次洗價到這次洗價之間的Tick資料

    - 可以指定最大的讀取筆數(如果兩次洗價之間的資料量超過這個限制的話, 則只回傳最新的資料)
    - 自動合併台股逐筆撮合的MultiTick(連續成交序列)
        - 所謂MultiTick, 指的是在台股逐筆撮合時, 一筆買單(賣單)同時產生了多筆不同價格的成交的情形,
        - 當發生這種情形時, 交易所會把每一個價格的成交資料分別傳送, 可是ReadTicks會把這些成交紀錄合併統計, 
		  方便使用者計算這個大單的總量,
        - 關於MultiTick, 請參考 https://bit.ly/3uZtwbG 內的更多說明

    呼叫方式:

    var: intrabarpersist readtick_cookie(0);// ReadTicks內部使用, 每次呼叫時請照實傳入
    array: tick_array[100, 11](0);          // 需要宣告一個2維陣列來儲存Tick資料
                                            // 陣列的第一維是最大讀取筆數,
                                            // 陣列的第二維是每一筆的欄位數, 請傳入11

    var: idx(0);
    value1 = ReadTicks(tick_array, readtick_cookie);
    for idx = 1 to value1 begin
        // 依序處理回傳的每一筆Tick
        // 每一筆Tick共有11個欄位, 分別是 tick_array[idx, 1], tick_array[idx, 2], .. tick_array[idx, 11]
        // 請參考底下說明
    end;

    回傳結果說明:

    - value1會是tick_array內所讀到的筆數, 如果上次洗價到這次洗價之間實際成交筆數超過tick_array宣告的大小的話, 則只會回傳最新的前N筆資料

    - tick_array[1, ..]是洗價當時最新的一筆, tick_array[2, ..]是前一筆, tick_array[value1, ..]是回傳的最後一筆

    舉例:

    如果目前已經收到了#1, #2, #3, #4 這四筆ticks, 而#3跟#4是屬於同一組MultiTick, 那麼呼叫ReadTicks時, 會回傳3筆紀錄,
    第一筆紀錄(tick_array[1,..])是#3跟#4合併的結果, 第二筆紀錄(tick_array[2,..])是#2的資料,第三筆紀錄(tick_array[3,..])是#1的資料

    - value1有可能是0, 表示到目前為止還沒有收到一筆完整的Tick. 這種情形可能會發生在系統收到了MultiTick的資料, 可是最後一筆MultiTick的資料還沒有收到.
      因為ReadTicks會把完整的MultiTick合併成一筆回傳給你, 所以此時value1會先回0. 等到下一次收到最後一筆MultiTick時就會把完整的MultiTick資料回傳給用戶.


    每一筆資料會有11個欄位, 以下分別說明

    - tick_array[n, 1] = Date (成交日期, 格式為yyyyHHmm)

    - tick_array[n, 2] = Time (成交時間, 格式為HHmmss)
        - 如果是MultiTick的話, 每一筆的Time都是一樣的(同時間成交)

    - tick_array[n, 3] = Close (成交價),
        - 如果是MultiTick的話, 回的是MultiTick序列最後一筆的成交價, 如果是買盤的話, 會是價格最高的那一筆, 如果是賣盤的話, 會是價格最低的那一筆

    - tick_array[n, 4] = Volume (成交量),
        - 如果是MultiTick的話, 回的是MultiTick序列最後一筆的成交量, 如果想要得到整組MultiTick的成交量(加總)的話, 請讀取tick_array[n, 10]

    - tick_array[n, 5] = BidAskFlag (內外盤標記, 1=外盤, -1=內盤, 0=不分),

    - tick_array[n, 6] = SeqNo (Tick序號, 每日的第一筆從1開始編制, 越來越大)
        - 如果是MultiTick的話, 回的是MultiTick序列最後一筆的Tick序號

    - tick_array[n, 7] = 成交方式註記
        - 如果不是台股的話, 這個欄位都會回-1
        - 如果是台股的話, 則依照這一筆成交資料的撮合方式來決定. 如果這一筆是集合競價的話, 回傳-1. 
		  依照目前台股的撮合規則, 每一日的開盤, 收盤, 都是集合競價, 如果商品被處置(分盤交易), 每一筆資料也是集合競價, 
		  如果商品委託價格發生很大的異動時, 交易所可能也會暫緩撮合, 此時也是集合競價.
        - 當這一筆資料被標示成集合競價時, 代表的是, 這一筆資料的價格/數量, 可能是很多個人委託單的合併, 所以XQ統計大單時, 會略過這些資料,
        - 如果是台股, 而且不是集合競價的話(也就是逐筆撮合), 那則依照這一筆是單筆成交, 還是連續成交序列(MultiTick)來判斷,
        - 如果是單筆成交的話, 回傳0, 如果是連續成交序列的話, 則回傳連續成交序列的筆數

    - tick_array[n, 8] (請看底下說明)
    - tick_array[n, 9] (請看底下說明)

    - tick_array[n, 10] = 成交量加總
        - 如果不是MultiTick的話, tick_array[n, 10]的數值跟tick_array[n, 4]是一樣的
        - 如果是MultiTick的話, tick_array[n, 10]的數值是這一組MultiTick每一筆成交量的加總

    - tick_array[n, 11] = 成交值加總(股票適用)
        - 如果不是MultiTick的話, tick_array[n, 11]是這一筆成交資料的成交值(元)
        - 如果是MultiTick的話, tick_array[n, 10]的數值是這一組MultiTick每一筆成交值的加總

    應用方式:

    value1 = ReadTicks(tick_array, readtick_cookie);
    for idx = 1 to value1 begin
        if tick_array[idx, 7] = -1 then begin
            // 集合撮合: 不判斷這一筆是否是大單
        end else begin
            // 逐筆撮合: 可以用tick_array[10]跟tick_array[11]來判斷這一筆資料的成交量/成交金額
            //
            if tick_array[idx, 10] >= 400 then ret=1;           // 400張的大單
            if tick_array[idx, 11] >= 100*10000 then ret=1;     // 100萬的大單
        end;
    end;

    - tick_array[n, 8] = 這一筆資料與目前系統最新一筆Tick的資料間隔(offset)
        - 如果這是MultiTick的話, 則[n, 8]回傳的是MultiTick序列內「第一筆資料」與目前系統最新一筆tick的offset,
        - 如果這不是MultiTick的話, 則[n, 8]回傳的是這一筆資料與目前系統最新一筆tick的offset,
        - 這個欄位的主要目的, 是讓使用者如果想要讀取MultiTick內「每一筆成交紀錄」時可以使用, 請參考底下的範例

    - tick_array[n, 9] = 這一筆資料與目前系統最新一筆Tick的資料間隔(offset)
        - 如果這是MultiTick的話, 則[n, 9]回傳的是MultiTick序列內「最後一筆資料」與目前系統最新一筆tick的offset,
        - 如果這不是MultiTick的話, 則[n, 9]回傳的是這一筆資料與目前系統最新一筆tick的offset,

    應用方式:

    value1 = ReadTicks(tick_array, readtick_cookie);
    for idx = 1 to value1 begin
        if tick_array[idx, 7] > 0 then begin
            // 這是一個MultiTick
            // 以下的寫法是從第一筆scan到最後一筆, 如果是買盤的話, 則價格由低到高, 如果是賣盤的話, 則價格由高到低
            //
            for j = tick_array[_i, 8] downto tick_array[_i, 9] begin
                value11 = GetField("Close", "Tick")[j];     // MultiTick: 其中一筆成交價
                value12 = GetField("Volume", "Tick")[j];    // MultiTick: 其中一筆成交量
            end;
        end;
    end;
}

input: tick_array[X,Y](NumericArray);	{ 參數1: 傳入要儲存tick資料的array }
input: readtick_cookie(NumericRef);		{ 參數2: Cookie: 儲存最後一次**處理**完畢的Tick編號 }

if Y < 10 then raiseruntimeerror("tick_array的第二維至少要 >= 10");

var: _cur_tickseq(0), _row(0), _i(0);
var: _last_multitick_start(0);
var: _lotsize(-1);

_cur_tickseq = GetField("SeqNo", "Tick");

if readtick_cookie > _cur_tickseq then
	readtick_cookie = 0;

if _lotsize < 0 then begin
	if symbolType = 2 then 
		_lotsize = GetSymbolInfo("交易單位") 
	else 
		_lotsize = 1;
end;

// 從上次到目前的資料範圍: readtick_cookie+1 .. _cur_tickseq
//
_i = _cur_tickseq; 	
_row = 1;
_last_multitick_start = 0;
while _i > readtick_cookie and _row <= X begin

	value1 = GetField("Date", "Tick")[_cur_tickseq - _i];
	value2 = GetField("Time", "Tick")[_cur_tickseq - _i];
	value3 = GetField("Close", "Tick")[_cur_tickseq - _i];
	value4 = GetField("Volume", "Tick")[_cur_tickseq - _i];
	value5 = GetField("BidAskFlag", "Tick")[_cur_tickseq - _i];
	value6 = GetField("SeqNo", "Tick")[_cur_tickseq - _i];
	value7 = GetField("TickGroup", "Tick")[_cur_tickseq - _i];
	
	if value7 = 0 or value7 = -1 then begin
		// 不是MultiTick
		//
		tick_array[_row, 1] = value1;		// Date
		tick_array[_row, 2] = value2;		// Time
		tick_array[_row, 3] = value3;		// Close
		tick_array[_row, 4] = value4;		// Volume
		tick_array[_row, 5] = value5;		// BidAskFlag
		tick_array[_row, 6] = value6;		// SeqNo
		
		if Y = 10 then
			tick_array[_row, 7] = 0			// (舊版邏輯) 不是MultiTick: 回0  
		else
			tick_array[_row, 7] = value7;	// (新版邏輯) 不是MultiTick: 回這一筆的TickGroup
				
		tick_array[_row, 8] = _cur_tickseq - value6;	// 這一筆的offset			
		tick_array[_row, 9] = _cur_tickseq - value6;	// 這一筆的offset
		tick_array[_row, 10] = value4;		// Volume
		
		if Y > 10 then
			tick_array[_row, 11] = value3 * value4 * _lotsize;	// (新版邏輯) 成交金額
				
		_row = _row + 1;
		_i = _i - 1;			
		
	end else begin
		// 這是MultiTick
		//
		// value7的內容應該是1, 2, 2, 3 (從舊到新)
		//
		var: _total_v(0), _total_pv(0), _count(0);
		var: _complete(false);
		
		_complete = false;
		_count = 1;
		_i = _i - 1;
		_total_v = value4;
		_total_pv = value3 * value4 * _lotsize;

		if value7 = 1 then begin
			_complete = true;
		end else begin
			while not _complete and _i > readtick_cookie begin
				value33 = GetField("Close", "Tick")[_cur_tickseq - _i];
				value44 = GetField("Volume", "Tick")[_cur_tickseq - _i];
				value66 = GetField("SeqNo", "Tick")[_cur_tickseq - _i];
				value77 = GetField("TickGroup", "Tick")[_cur_tickseq - _i];
				
				_total_v = _total_v + value44;
				_total_pv = _total_pv + value33 * value44 * _lotsize;
			
				_i = _i - 1;
				_count = _count + 1;
				
				if value77 = 1 then _complete = true;
			end;
		end;
		
		// 三種情形
		//	case#1: _complete 而且 value7(最新一筆的標記) =3 => 我們讀到了一個完整的multitick序列
		//	case#2: _complete 可是 value7不是3 
		//		=> 這個表示我們收到了一個multitick序列的開頭, 可是結尾還沒有收到
		//		case#2a	=> 如果這種情形發生在最新的資料端, 那我們可以等待下一次洗價時再來處理
		//				Example: 0, 0, 0, 1 (2, 3 is coming)
		//		case#2b	=> 如果這種情形發生在最新的資料端, 那我們可以等待下一次洗價時再來處理
		//				Example: 0, 0, 0, 1, 2, 2 (3 is coming)
		//		case#2c	=> 可是如果這種情形是發生在中間的話, 那就是資料有問題了, 例如
		//				Example: 0, 0, 0, 1 (where is 3 ?) 0, 0
		//	case#3: not _complete => 這個表示這一整批資料的第一筆竟然不是multitick序列的開頭, 可能有人傳錯 readtick_cookie了 ?
		//				Example: (where is 1 ?) 2, 2, 2, 3
		//
		// 如果是 case#2a的話, 目前收到的multitick資料就先不處理, 等下一次呼叫時再來處理
		// 其餘情形我們就組一筆MultiTick的資料
		//
		if _complete and value7 <> 3 and _row = 1 then begin
			// 紀錄這一批multitick的第一筆, 當成下一次的開始
			//
			_last_multitick_start = _i;
		
		end else begin
			tick_array[_row, 1] = value1;		// Date
			tick_array[_row, 2] = value2;		// Time
			tick_array[_row, 3] = value3;		// Close = MultiTick最後一筆的價格
			tick_array[_row, 4] = value4;		// Volume
			tick_array[_row, 5] = value5;		// BidAskFlag
			tick_array[_row, 6] = value6;		// SeqNo
			tick_array[_row, 7] = _count;		// MultiTick的筆數
			tick_array[_row, 8] = _cur_tickseq - value66; // MultiTick 第一筆的位置
			tick_array[_row, 9] = _cur_tickseq - value6;  // MultiTick 最後一筆的位置
			tick_array[_row, 10] = _total_v;	// MultiTick的總成交量

			if Y > 10 then
				tick_array[_row, 11] = _total_pv;	// (新版邏輯) 成交金額(MultiTick加總)
			
			_row = _row + 1;
		end;
	
	end;
end;


if _last_multitick_start <> 0 then begin
	readtick_cookie = _last_multitick_start;	
end else begin
	readtick_cookie = _cur_tickseq;
end;

retval = _row - 1;		// 回傳的筆數
```

---


---

## 腳本檔案: 函數/價格計算/Summation.xs

```xs
{@type:function}
SetBarMode(1);

input:thePrice(numericseries); //"價格序列"
input:Length(numericsimple);   //"計算期間"

variable:Sum(0),SumLength(0);
Sum=0;

for SumLength = 0 to Length - 1
begin 
    Sum = Sum + thePrice[SumLength];
end;

Summation = Sum;
```

---


---

## 腳本檔案: 函數/價格計算/TrueRange.xs

```xs
{@type:function}
SetBarMode(1);

TrueRange = TrueHigh - TrueLow;
```

---


---

## 腳本檔案: 函數/價格計算/UpLimit.xs

```xs
{@type:function}
SetBarMode(1);

input:refPrice(numericsimple);
variable:obup1(0),obdw1(0),STOCKUP(0),STOCKDW(0);

if date < 20150601 then begin
	obup1= refPrice*1.07;
	obdw1= refPrice*0.93;
end else begin
	obup1= refPrice*1.1;
	obdw1= refPrice*0.9;
end;

if (obup1<10 and obdw1<10) then begin
	STOCKUP = ((floor((floor(obup1*100)*100)))/100)/100;
	STOCKDW = ((floor((ceiling(obdw1*100)*100)))/100)/100;
end else if (obup1>=10 and obdw1<10) then begin
	STOCKUP = ((floor(((floor(obup1/0.05)*0.05)*100)*100))/100)/100;
	STOCKDW = ((floor((ceiling(obdw1*100)*100)))/100)/100;
end else if (obup1>=10 and obdw1>=10 and obup1<50 and obdw1<50) then begin
	STOCKUP = ((floor(((floor(obup1/0.05)*0.05)*100)*100))/100)/100;
	STOCKDW = ((floor(((ceiling(obdw1/0.05)*0.05)*100)*100))/100)/100;
end else if (obup1>=50 and obdw1<50 ) then begin
	STOCKUP = ((floor(((floor(obup1/0.1)*0.1)*100)*100))/100)/100;
	STOCKDW = (ceiling(obdw1/0.05)*0.05);
end else if (obup1>=50 and obdw1>=50 and obup1<100 and obdw1<100) then begin
	STOCKUP = ((floor(((floor(obup1/0.1)*0.1)*100)*100))/100)/100;
	STOCKDW = ((floor(((ceiling(obdw1/0.1)*0.1)*100)*100))/100)/100;
end else if (obup1>=100 and obdw1<100 ) then begin
	STOCKUP = ((floor(((floor(obup1/0.5)*0.5)*100)*100))/100)/100;
	STOCKDW = ((floor(((ceiling(obdw1/0.1)*0.1)*100)*100))/100)/100;
end else if (obup1>=100 and obdw1>=100 and obup1<500 and obdw1<500) then begin
	STOCKUP = ((floor(((floor(obup1/0.5)*0.5)*100)*100))/100)/100;
	STOCKDW = ((floor(((ceiling(obdw1/0.5)*0.5)*100)*100))/100)/100;
end else if (obup1>=500 and obdw1<500) then begin
	STOCKUP = ((floor(((floor(obup1/0.5)*0.5)*100)*100))/100)/100;
	STOCKDW = ((floor(((ceiling(obdw1/0.1)*0.1)*100)*100))/100)/100;
end else if (obup1>=500 and obdw1>=500 and obup1<1000 and obdw1<1000) then begin
	STOCKUP = ((floor(((floor(obup1/ 1)* 1)*100)*100))/100)/100;
	STOCKDW = ((floor(((ceiling(obdw1/ 1)* 1)*100)*100))/100)/100;
end else if (obup1>=1000 and obdw1<1000) then begin
	STOCKUP = ((floor(((floor(obup1/5)*5)*100)*100))/100)/100;
	STOCKDW = ((floor(((ceiling(obdw1/ 1)* 1)*100)*100))/100)/100;
end else if (obup1>=1000 and obdw1>=1000) then begin
	STOCKUP = ((floor(((floor(obup1/5)*5)*100)*100))/100)/100;
	STOCKDW = ((floor(((ceiling(obdw1/5)*5)*100)*100))/100)/100;
end;

UpLimit = STOCKUP;
```

---


---

## 腳本檔案: 函數/價格計算/WMA.xs

```xs
{@type:function}
SetBarMode(1);

input:thePrice(numericseries); //"價格序列"
input:Length(Numeric);   //"計算期間"

variable:  Factor(0);

if Factor = 0 then Factor = 0.5 * Length * (Length+1);

if CurrentBar < Length then
	WMA = thePrice
else begin
	WMA = Length * thePrice;
	for value1 = 1 to Length - 1
		WMA += thePrice[value1] * (Length - value1);	
    WMA = WMA/Factor;
end;
```

---


---

## 腳本檔案: 函數/價格計算/XAverage.xs

```xs
{@type:function}
SetBarMode(2);

input:thePrice(numericseries); //"價格序列"
input:Length(Numeric);   //"計算期間"

variable:  Factor(0);

if length + 1 = 0 then Factor = 1 else Factor = 2 / (Length + 1);

if CurrentBar = 1 then
	XAverage = thePrice
else
	XAverage = XAverage[1] + Factor * (thePrice - XAverage[1]);
```

---


---

## 腳本檔案: 函數/價格關係/Extremes.xs

```xs
{@type:function}
SetBarMode(2);

input:  
	SourceSeries(numericseries), 	//來源數列
	Length(numericsimple), 			//計算期間
    DscAsc(numericsimple), 			//極大值(1)或極小值(-1)
	refExtremeValue(numericref), 	//輸出極值
	refExtremeBar(numericref);		//輸出極值K棒相對位置
	
var:
	exLength(0),
	exCalcBar(0),
	calcInterval(0);

if 1 > Length then 
begin
  refExtremeValue = 0 ;
  refExtremeBar = -1 ;
  extremes = -1 ;
  return;
end;

if Length < exLength or currentbar = 1 or value2 >= Length - 1 then //強制進行重算的case
begin
	value1 = SourceSeries;
	value2 = 0;
	for value3 = 1 to Length - 1
	begin
		if DscAsc * SourceSeries[value3] > DscAsc * value1 then
		begin
			value1 = SourceSeries[value3];
			value2 = value3;	
		end;
	end;
end else if Length > exLength and Length - exLength = currentBar - exCalcBar then //判斷計算長度是否和K棒同步長大，若是，只需要計算差額。
begin
	calcInterval = Length - exLength;
	for value3 = calcInterval - 1 to 0
	begin
		if DscAsc * SourceSeries[value3] >= DscAsc * value1 then
		begin
			value1 = SourceSeries[value3];
			value2 = value3;	
		end	else
			value2 = value2 + 1;
	end;	
end else 
begin
	if DscAsc * SourceSeries >= DscAsc * value1 then begin
		value1 = SourceSeries;
		value2 = 0;	
	end	else
		value2 = value2 + 1;
end;

exLength = Length;
exCalcBar = currentBar;
refExtremeValue = value1;
refExtremeBar = value2;
extremes = 1;
```

---


---

## 腳本檔案: 函數/價格關係/ExtremesArray.xs

```xs
{@type:function}
SetBarMode(1);

input:
	SourceArray[MaxSize](numericarray), 	//來源陣列
	Size(numericsimple), 					//來源陣列大小
    DscAsc(numericsimple), 					//極大值(1)或極小值(-1)
	refExtremeValue(numericref), 			//輸出極值
	refExtremeIndex(numericref);			//輸出極值陣列索引值

variable:  	price(0),
			_bar(0),
			counter(0);

if  Size < 1 or Size > MaxSize then
begin
  refExtremeValue = 0 ;
  refExtremeIndex = -1 ;
  ExtremesArray = -1 ;
  return;
end;


price = SourceArray[1];
_bar = 1;

for counter = 2 to Size 
  begin
	if (DscAsc=1 and SourceArray[counter]>price) then
	  begin
		price = SourceArray[counter];
		_bar = counter;
	  end
	else if (DscAsc=-1 and SourceArray[counter]<price) then
	  begin	
		price = SourceArray[counter];
		_bar = counter;
	  end;
  end;

refExtremeValue = price;
refExtremeIndex = _bar;

ExtremesArray = 1;
```

---


---

## 腳本檔案: 函數/價格關係/FastHighestBar.xs

```xs
{@type:function}
SetBarMode(1);

input:thePrice(numericseries); //"價格序列"
input:Length(numericsimple);   //"計算期間"

variable: _Output(0);

Extremes(ThePrice, Length, 1, value1, _Output);

FastHighestBar = _Output;
```

---


---

## 腳本檔案: 函數/價格關係/FastLowestBar.xs

```xs
{@type:function}
SetBarMode(1);

input:thePrice(numericseries); //"價格序列"
input:Length(numericsimple);   //"計算期間"

variable: _Output(0);

Extremes(ThePrice, Length, -1, value1, _Output);

FastLowestbar = _Output;
```

---


---

## 腳本檔案: 函數/價格關係/HighDays.xs

```xs
{@type:function}
SetBarMode(1);

// 計算過去幾筆資料內創新高的次數
//
input: length(numeric);		// 計算天期(含當根bar)

variable: tt(0);　　
variable: ix(0); 
variable: currentHigh(0);

tt=0;
currentHigh = high[length-1];

for ix = length-2 downto 0 
begin 
	if ( high[ix] > currentHigh ) then
	begin
		tt+=1;　　
		currentHigh = high[ix];
	end; 
end;

HighDays=tt;
```

---


---

## 腳本檔案: 函數/價格關係/HighestArray.xs

```xs
{@type:function}
SetBarMode(1);

input:  thePriceArray[MaxSize](NumericArray),ArraySize(numericsimple);
variable: _Output(0);

ExtremesArray(thePriceArray, ArraySize, 1, _Output, value2);

HighestArray = _Output;
```

---


---

## 腳本檔案: 函數/價格關係/HighestBar.xs

```xs
{@type:function}
SetBarMode(1);

input:thePrice(numericseries); //"價格序列"
input:Length(numericsimple);   //"計算期間"

variable: _Output(0);

Extremes(ThePrice, Length, 1, value1, _Output);

HighestBar = _Output;
```

---


---

## 腳本檔案: 函數/價格關係/LowDays.xs

```xs
{@type:function}
SetBarMode(1);

// 計算過去幾筆資料內創新低的次數
//
input: length(numeric);		// 計算天期(含當根bar)

variable: tt(0);　　
variable: ix(0); 
variable: currentlow(0);

tt=0;
currentlow = low[length-1];

for ix = length-2 downto 0 
begin 
	if ( low[ix] < currentlow ) then
	begin
		tt+=1;　　
		currentlow = low[ix];
	end; 
end;

LowDays=tt;
```

---


---

## 腳本檔案: 函數/價格關係/LowestArray.xs

```xs
{@type:function}
SetBarMode(1);

input:  thePriceArray[MaxSize](NumericArray),ArraySize(numericsimple);
variable: _Output(0);

ExtremesArray(thePriceArray, ArraySize, -1, _Output, value2);
LowestArray = _Output;
```

---


---

## 腳本檔案: 函數/價格關係/LowestBar.xs

```xs
{@type:function}
SetBarMode(1);

input:thePrice(numericseries); //"價格序列"
input:Length(numericsimple);   //"計算期間"

variable: _Output(0);

Extremes(ThePrice, Length, -1, value1, _Output);

Lowestbar = _Output;
```

---


---

## 腳本檔案: 函數/價格關係/MoM.xs

```xs
{@type:function}
SetBarMode(1);

input:MomVal(numericseries);

if barfreq <> "M" and barfreq <> "AM" then
	raiseruntimeerror("僅支援月頻率")
else
	MOM = (MomVal/MomVal[1]-1)*100;
```

---


---

## 腳本檔案: 函數/價格關係/NthExtremes.xs

```xs
{@type:function}
SetBarMode(1);

input:  
	SourceSeries(numericseries), 	//來源數列
	Length(numericsimple), 			//計算期間
    N(numericsimple),               //極值順序
    DscAsc(numericsimple), 			//極大值(1)或極小值(-1)
	refExtremeValue(numericref), 	//輸出極值
	refExtremeBar(numericref);		//輸出極值K棒相對位置
	

array: nthA[500](0),nthB[500](0);
variable:x(0),y(0),temp(0);


if N>Length or Length>500 then
begin
    refExtremeValue = 0;
    refExtremeBar = -1;
    NthExtremes = -1;
end
else
begin
    for x = 0 to Length -1
    begin
        nthA[x] = SourceSeries[x];
        nthB[x] = x ;
    end;
	
    for x = 0 to Length -2
	begin
		for y = x + 1 to Length -1
		begin
			if ((DscAsc=1 and nthA[x] < nthA[y])or
				(DscAsc=-1 and nthA[x] > nthA[y])) then
			begin	
				temp = nthA[ y ];
                nthA[ y ] = nthA[ x ];
                nthA[ x ] = temp;
				temp = nthB[ y ];
                nthB[ y ] = nthB[ x ];
                nthB[ x ] = temp;
			end;
		end;
	end;
    refExtremeValue = 	nthA[ N-1 ];
    refExtremeBar	= 	nthB[ N-1 ] + ExecOffset;
    NthExtremes = 1;

end;
```

---


---

## 腳本檔案: 函數/價格關係/NthExtremesArray.xs

```xs
{@type:function}
SetBarMode(1);

input:
	SourceArray[MaxSize](numericarray), 	//來源陣列
	Size(numericsimple), 					//來源陣列大小
	N(numericsimple),                       //極值順序
    DscAsc(numericsimple), 					//極大值(1)或極小值(-1)
	refExtremeValue(numericref), 			//輸出極值
	refExtremeIndex(numericref);			//輸出極值陣列索引值

array: ntharrayA[200](0),ntharrayB[200](0);
variable: x(0),y(0),temp(0);
variable: startIndex(0),endIndex(0),NIndex(0);

if N > Size or Size > MinList(MaxSize+1,200) then
begin 
	refExtremeValue = 0;
	refExtremeIndex = -1;
	NthExtremesarray = -1;
end
else 
begin
	if Size = MaxSize+1 then begin
		startIndex = 0;
		endIndex = MaxSize;
		NIndex = N - 1;
	end else begin
		startIndex = 1;
		endIndex = Size;
		NIndex = N;
	end;

	for x = startIndex to endIndex
	begin
		ntharrayA[x] = SourceArray[x];
		ntharrayB[x] = x;
	end;
	for x = startIndex to endIndex - 1
	begin
		for y = x + 1 to endIndex
		begin
			if((DscAsc = 1 and ntharrayA[x] < ntharrayA[y] )or
				(DscAsc = -1 and ntharrayA[x] > ntharrayA[y])) then
			begin
				temp = ntharrayA[x];
				ntharrayA[x] = ntharrayA[y];
				ntharrayA[y] = temp;
				
				temp = ntharrayB[x];
				ntharrayB[x] = ntharrayB[y];
				ntharrayB[y] = temp;
			end;
		end;
	end;
	refExtremeValue = ntharrayA[NIndex];
	refExtremeIndex = ntharrayB[NIndex];
	NthExtremesarray = 1;
end;
```

---


---

## 腳本檔案: 函數/價格關係/NthHighest.xs

```xs
{@type:function}
SetBarMode(1);

input: N (numericsimple), thePrice(numericseries), Length(numericsimple);
variable: _Output(0);

NthExtremes(thePrice, Length, N, 1, _Output, value2);

NthHighest = _Output;
```

---


---

## 腳本檔案: 函數/價格關係/NthHighestArray.xs

```xs
{@type:function}
SetBarMode(1);

input:  thePriceArray[MaxSize](NumericArray), Size(numericsimple), N (numericsimple);
variable: _Output(0);

NthExtremesArray(thePriceArray, Size, N, 1, _Output, value2);

NthHighestArray = _Output;
```

---


---

## 腳本檔案: 函數/價格關係/NthHighestBar.xs

```xs
{@type:function}
SetBarMode(1);

input: N (numericsimple), thePrice(numericseries), Length(numericsimple);
variable: _Output(0);

NthExtremes(thePrice, Length, N, 1, value1, _Output);

NthHighestBar = _Output;
```

---


---

## 腳本檔案: 函數/價格關係/NthLowest.xs

```xs
{@type:function}
SetBarMode(1);

input: N (numericsimple), thePrice(numericseries), Length(numericsimple);
variable: _Output(0);

NthExtremes(thePrice, Length, N, -1, _Output, value2);

NthLowest = _Output;
```

---


---

## 腳本檔案: 函數/價格關係/NthLowestArray.xs

```xs
{@type:function}
SetBarMode(1);

input:  thePriceArray[MaxSize](NumericArrayRef), Size(numericsimple), N (numericsimple);                
variable: _Output(0);

NthExtremesArray( thePriceArray, Size, N, -1, _Output, value2) ;

NthLowestArray = _Output ;
```

---


---

## 腳本檔案: 函數/價格關係/NthLowestBar.xs

```xs
{@type:function}
SetBarMode(1);

input: N (numericsimple), thePrice(numericseries), Length(numericsimple);
variable: _Output(0);

NthExtremes(thePrice, Length, N, -1, value1, _Output);

NthLowestBar = _Output;
```

---


---

## 腳本檔案: 函數/價格關係/OHLCPeriodsAgo.xs

```xs
{@type:function}
SetBarMode(2);

input:  
	FreqType(numericsimple), 	//指定K棒頻率，1:日線、2:週線、3:月線、3.25:季、3.5 半年、4:年線
	FreqAgo(numericsimple), 	//指定K棒位置
	refFreqOpen(numericref), 	//輸出K棒開盤價
	refFreqHigh(numericref),	//輸出K棒最高價
	refFreqLow(numericref), 	//輸出K棒最低價
	refFreqClose(numericref);	//輸出K棒收盤價
variable:
	varBarFreqInt(-1),
	varBarIndex(-1);
array:
	arrayO[200](-1),
	arrayH[200](-1),
	arrayL[200](-1),
	arrayC[200](-1);

switch (barfreq)
begin
	case "Tick":
		varBarFreqInt = 0;
	case "Min","Hour":
		varBarFreqInt = 1;
	case "D","AD":
		varBarFreqInt = 2;
	case "W","AW":
		varBarFreqInt = 3;
	case "M","AM","Q","H","Y":
		varBarFreqInt = 4;
	default:
		varBarFreqInt = -1;
end;

if  FreqAgo > 200 or FreqAgo < 0 or varBarFreqInt = -1 or varBarFreqInt > FreqType + 1 then return;

switch (FreqType)
begin
	case 2:
		condition1 = WeekofYear(Date) <> WeekofYear(Date[1]) ;
		if WeekofYear(Date[1]) =53 and  DayofWeek(Date)> DayofWeek(Date[1]) then condition1= false;
  	case 3:
		condition1 = Month(Date) <> Month(Date[1]);
	case 3.25:
	    condition1 = Mod(Month(Date),3)=1 and Mod(Month(Date[1]),3)=0 ;
	case 3.5:
	    condition1 = Mod(Month(Date),6)=1 and Mod(Month(Date[1]),6)=0 ;
	case 4:
		condition1 = Year(Date) <> Year(Date[1]);
	default:
		condition1 = Date <> Date[1];
end;

condition1 = CurrentBar = 1 or condition1;
if condition1 then
begin
	varBarIndex = varBarIndex - 1;
	if varBarIndex < 0 then varBarIndex = FreqAgo;	
	arrayO[varBarIndex] = Open;
	arrayH[varBarIndex] = High;
	arrayL[varBarIndex] = Low;
	arrayC[varBarIndex] = Close;
end
else
begin
	arrayC[varBarIndex] = Close;
	if High > arrayH[varBarIndex] then
		arrayH[varBarIndex] = High;
	if Low < arrayL[varBarIndex] then
		arrayL[varBarIndex] = Low;
end;

refFreqOpen = arrayO[Mod( varBarIndex + FreqAgo, FreqAgo + 1) ];
refFreqHigh = arrayH[Mod( varBarIndex + FreqAgo, FreqAgo + 1) ];
refFreqLow = arrayL[Mod( varBarIndex + FreqAgo, FreqAgo + 1) ];
refFreqClose = arrayC[Mod( varBarIndex + FreqAgo, FreqAgo + 1) ];
OHLCPeriodsAgo = 1;
```

---


---

## 腳本檔案: 函數/價格關係/QoQ.xs

```xs
{@type:function}
SetBarMode(1);

input:QoQVal(numericseries);

if barfreq <> "Q" then
	raiseruntimeerror("僅支援季頻率")
else
	QoQ = 100*(QoQVal/QoQVal[1]-1);
```

---


---

## 腳本檔案: 函數/價格關係/SimpleHighest.xs

```xs
{@type:function}
SetBarMode(1);

input: thePrice(numericseries),Length(numericsimple);

variable: highValue(0);
variable: i(0);

highValue = thePrice[0];
for i = 1 to Length-1
begin
  if thePrice[i] > highValue then
    highValue = thePrice[i];
end;

SimpleHighest = highValue;
```

---


---

## 腳本檔案: 函數/價格關係/SimpleHighestBar.xs

```xs
{@type:function}
SetBarMode(1);

input: thePrice(numericseries),Length(numericsimple);

variable: highValue(0);
variable: i(0);
variable: barOffset(0);

highValue = thePrice[0];
barOffset = 0;
for i = 1 to Length-1
begin
  if thePrice[i] > highValue then begin
    highValue = thePrice[i];
	barOffset = i;
  end;	
end;

SimpleHighestBar = barOffset;
```

---


---

## 腳本檔案: 函數/價格關係/SimpleLowest.xs

```xs
{@type:function}
SetBarMode(1);

input: thePrice(numericseries),Length(numericsimple);

variable: lowValue(0);
variable: i(0);

lowValue = thePrice[0];
for i = 1 to Length-1
begin
  if thePrice[i] < lowValue then
    lowValue = thePrice[i];
end;

SimpleLowest = lowValue;
```

---


---

## 腳本檔案: 函數/價格關係/SimpleLowestBar.xs

```xs
{@type:function}
SetBarMode(1);

input: thePrice(numericseries),Length(numericsimple);

variable: lowValue(0);
variable: i(0);
variable: barOffset(0);

lowValue = thePrice[0];
barOffset = 0;
for i = 1 to Length-1
begin
  if thePrice[i] < lowValue then begin
    lowValue = thePrice[i];
	barOffset = i;
  end;	
end;

SimpleLowestBar = barOffset;
```

---


---

## 腳本檔案: 函數/價格關係/YoY.xs

```xs
{@type:function}
SetBarMode(1);

input:YoYVal(numericseries);

switch(barfreq)
begin
	Case "M","AM":
		YoY = RateOfChange(YoYVal,12);
	Case "Q":
		YoY = RateOfChange(YoYVal,4);
	Case "Y":
		YoY = RateOfChange(YoYVal,1);
	default:
		raiseruntimeerror("僅支援月、季、年頻率");
end;
```

---


---

## 腳本檔案: 函數/技術指標/ACC.xs

```xs
{@type:function}
SetBarMode(1);

{
ACC加速量指標(Acceleration)，用來觀察行情價格變化的加速度幅度，
是MOM運動量指標的再一次計算，使用收盤價，並以相同期間長度計算
Length: 計算期數
}

input: Length(numeric);

value1 = Momentum(Close, Length);
value2 = Momentum(value1, Length);

ACC =value2;
```

---


---

## 腳本檔案: 函數/技術指標/ADI.xs

```xs
{@type:function}
SetBarMode(2);

{
輸出ADI指標值:
當日價格是漲時，表示上升力道戰勝，將此力道累積起來。
若當日是下跌，便從上升累積力道中減去下降的力道。
}
variable: ADIt(0);

if Close > Close[1] then
	ADIt = ADIt[1] + (Close - minlist(low, close[1]))
else
  begin
	if Close < Close[1] then
		ADIt = ADIt[1] - (maxlist(high, close[1]) - close)
	else
		ADIt = ADIt[1];
  end;

ADI =ADIt;
```

---


---

## 腳本檔案: 函數/技術指標/ADO.xs

```xs
{@type:function}
SetBarMode(1);

{
Accumulation／Distribution Oscillator，「聚散擺盪」指標。
傳回ADO值
}

variable: bp(0), sp(0), adot(0);

bp = High - Open;
sp = Close - Low;
if High <> low then
	adot = (bp + sp)/(2*(High - Low))*100
else
	adot = 50;

ADO =adot;
```

---


---

## 腳本檔案: 函數/技術指標/AR.xs

```xs
{@type:function}
SetBarMode(2);

{
買賣氣勢強度的測試指標。
AR值高時，代表行情很活潑，當AR值介於0.25~1.85間時，屬於盤整行情。AR值低時，表示人氣不足
Length: 計算期數
}
input: Length(numeric);
variable: sum(0), art(0);

sum = Summation((Open - Low), Length);
if sum <> 0 then
	art = 100 * Summation((High - Open), length) / sum
else
	art = art[1];

AR = art;
```

---


---

## 腳本檔案: 函數/技術指標/ATR.xs

```xs
{@type:function}
SetBarMode(1);

{
傳回平均真實區間
Length: 計算期數
}
input: Length(numeric);
ATR = Average(TrueRange, Length);
```

---


---

## 腳本檔案: 函數/技術指標/Bias.xs

```xs
{@type:function}
SetBarMode(1);

// Bias function (for 乖離率相關指標)
//
input: length(numericsimple);

value1 = Average(close, length);
if value1 <> 0 then
	Bias = ((close / absValue(value1)) - sign(value1)) * 100
else begin
	if close > 0 then 
		Bias = 999
	else if close < 0 then
		Bias = -999
	else
		Bias = 0;
end;
```

---


---

## 腳本檔案: 函數/技術指標/BiasDiff.xs

```xs
{@type:function}
SetBarMode(1);

{
Bias function (計算乖離率差值)
輸入兩個期間數值,計算並輸出此兩期間的乖離率差
Length1: 短期期數
Length2: 長期期數
}
input: length1(numericsimple),length2(numericsimple);

BiasDiff  = Bias(Length1) - Bias(Length2);
```

---


---

## 腳本檔案: 函數/技術指標/BollingerBand.xs

```xs
{@type:function}
SetBarMode(1);

// BollingerBand function
//
Input: price(numericseries), length(numericsimple), _band(numericsimple);

BollingerBand = Average(price, length) + _band * StandardDev(price, length, 1);
```

---


---

## 腳本檔案: 函數/技術指標/BollingerBandWidth.xs

```xs
{@type:function}
// BollingerBand Width function
//

input: 
	Price(numericseries, "數列"),
	Length(numericsimple, "天數"), 
	UpperBand(numericsimple, "上"), 
	LowerBand(numericsimple, "下");
	
variable: 
	up(0), down(0), mid(0), bbandwidth(0);

up = bollingerband(Price, Length, UpperBand);
down = bollingerband(Price, Length, -1 * LowerBand);
mid = (up + down) / 2;

if mid <> 0 then 
	bollingerbandwidth = 100 * (up - down) / mid
else
	bollingerbandwidth = 0;
```

---


---

## 腳本檔案: 函數/技術指標/BR.xs

```xs
{@type:function}
SetBarMode(2);

{
BR買賣願指標:買賣行情雙方力道強弱的參考指標
當BR指標值介於70~50時，行情為處盤整狀態。
若BR值超過300，表行情處相對高價，應小心回檔。
若BR值低於50，表行情處於相對低價，應注意價位的反彈。
Length: 計算期數
}
input: Length(numeric);
variable: sum(0), brt(0);

sum= Summation((Close[1] - Low), length);
if sum <> 0 then
	brt = 100 * Summation((High - Close[1]), length) / sum
else
	brt = brt[1];

BR  = brt;
```

---


---

## 腳本檔案: 函數/技術指標/CCI.xs

```xs
{@type:function}
SetBarMode(1);

{
Length : CCI指標計算期間
}
input: Length(numeric);
cci = CommodityChannel(Length);
```

---


---

## 腳本檔案: 函數/技術指標/CommodityChannel.xs

```xs
{@type:function}
SetBarMode(2);

// CommodityChannel function (for CCI指標)
//
input: length(numericsimple);                                                 
variable: avgtp(0);
variable: idx(0);
variable: sumDist(0);

avgtp = average(High + Low + Close, length);

sumDist = 0;
for idx = 0 to length - 1 
begin
	sumDist = sumDist + AbsValue(avgtp[idx] - (High + Low + Close)[idx]); 
end ;
sumDist = sumDist / length;

if sumDist <> 0 then
  CommodityChannel = (High + Low + Close - avgtp) / (0.015 * sumDist)
else
  CommodityChannel = 0;
```

---


---

## 腳本檔案: 函數/技術指標/CV.xs

```xs
{@type:function}
SetBarMode(2);

If CurrentBar = 1 then
	CV = Close * Volume
else	
	CV = CV[1] + (Close - Close[1]) * Volume;
```

---


---

## 腳本檔案: 函數/技術指標/D_Value.xs

```xs
{@type:function}
SetBarMode(1);

{
XQ: KD指標中的D值
Length:計算期數
Kt:Kt權數
}
input: Length(numeric), Kt(numeric);
variable:_rsv(0), _k(0), _d(0);

Stochastic(Length, Kt, Kt, _rsv, _k, _d);

D_value = _d;
```

---


---

## 腳本檔案: 函數/技術指標/DIF.xs

```xs
{@type:function}
SetBarMode(1);

{
傳回XQ: MACD指標中DIF值
FastLength: 短期期數
SlowLength: 長期期數
}
input: FastLength(numeric), SlowLength(numeric);
variable: price(0);

price = WeightedClose();

DIF = XAverage(price, FastLength) - XAverage(price, SlowLength);
```

---


---

## 腳本檔案: 函數/技術指標/DirectionMovement.xs

```xs
{@type:function}
SetBarMode(2);

// DirectionMovement function (for DMI相關指標)
//	Input: length
//	Return: pdi_value(+di), ndi_value(-di), adx_value(adx)
//
input: 
	length(numericsimple),
	pdi_value(numericref),
	ndi_value(numericref),
	adx_value(numericref);
	
variable:
	padm(0), nadm(0), radx(0),
	atr(0), pdm(0), ndm(0), tr(0),
	dValue0(0), dValue1(0), dx(0),
	idx(0);

if currentbar = 1 then
 begin
	padm = close / 10000;
	nadm = padm;
	atr = padm * 5;
	radx = 20;
 end
else
 begin
	pdm = maxlist(High - High[1], 0);
	ndm = maxlist(Low[1] - Low, 0);

	if pdm < ndm then
		pdm = 0
	else 
	  begin
		if pdm > ndm then
			ndm = 0
		else
		  begin
			pdm = 0;
			ndm = 0;
		  end;		
	  end;

	if Close[1] > High then
		tr = Close[1] - Low
	else	
	  begin
		if Close[1] < Low then
			tr = High - Close[1]
		else	
			tr = High - Low;
	  end;

	padm = padm[1] + (pdm - padm[1]) / length;
	nadm = nadm[1] + (ndm - nadm[1]) / length;
	atr = atr[1] + (tr - atr[1]) / length;
	
	if atr <> 0 then begin
		dValue0 = 100 * padm / atr;
		dValue1 = 100 * nadm / atr;
	end;
	
	if dValue0 + dValue1 <> 0 then
		dx = AbsValue(100 * (dValue0 - dValue1) / (dValue0 + dValue1));

	radx = radx[1] + (dx - radx[1]) / length;
 end;

pdi_value = dValue0;
ndi_value = dValue1;
adx_value = radx;
```

---


---

## 腳本檔案: 函數/技術指標/DMO.xs

```xs
{@type:function}
SetBarMode(1);

{
DMO指標(Directional Movement Oscillator)以
DMI趨向指標指標中正負DI值，將此二條線合併而成的一條指標線。
Length: 計算期數
}

input: Length(numeric);
variable: pdi_value(0), ndi_value(0), adx_value(0);

DirectionMovement(Length, pdi_value, ndi_value, adx_value);

DMO =(pdi_value - ndi_value);
```

---


---

## 腳本檔案: 函數/技術指標/DPO.xs

```xs
{@type:function}
SetBarMode(1);

{
XQ: DPO指標
Detrended Price Oscillator，「非趨勢價格擺盪」指標
Length: 計算期數
}

input: Length(numeric);

DPO = Close - Average(Close, Length)[(Length /2) + 1];
```

---


---

## 腳本檔案: 函數/技術指標/EMP.xs

```xs
{@type:function}
SetBarMode(1);

EMP= (AVERAGE(C,3)+AVERAGE(C,6)+AVERAGE(C,12)+AVERAGE(C,24))/4;
```

---


---

## 腳本檔案: 函數/技術指標/ERC.xs

```xs
{@type:function}
SetBarMode(1);

{
RC指標變動率的移動平均值(ERC)
Length: 計算期數
EMALength: 平滑期數
}
input: Length(numeric), EMALength(numeric);

if Close[Length] > 0 then
  value1 = (Close - Close[Length]) / Close[Length];

ERC = XAverage(value1, EMALength);
```

---


---

## 腳本檔案: 函數/技術指標/HL_Osc.xs

```xs
{@type:function}
SetBarMode(1);

{
 XQ: HL-Osc 指標
}
variable: hlot(0);

if TrueRange <> 0 then
	hlot = 100 * (H - C[1]) / TrueRange
else
	hlot = 0;

hl_osc = hlot;
```

---


---

## 腳本檔案: 函數/技術指標/K_Value.xs

```xs
{@type:function}
SetBarMode(1);

{
XQ: KD指標中的K值
Length:計算期數
RSVt:RSVt權數
}
input: Length(numeric), RSVt(numeric);
variable: _rsv(0), _k(0),_d(0);

Stochastic(Length, RSVt, RSVt, _rsv, _k, _d);

k_value = _k;
```

---


---

## 腳本檔案: 函數/技術指標/KeltnerLB.xs

```xs
{@type:function}
SetBarMode(1);

input:Para(NumericSimple);

//Keltner Channels 的繪製，是以一條指數移動平均線為中間， 然後在上下兩邊依據所謂的"平均真實範圍值"來繪出軌道的範圍來。

KeltnerLB = KeltnerMA(20) - ATR(20) * Para;
```

---


---

## 腳本檔案: 函數/技術指標/KeltnerMA.xs

```xs
{@type:function}
SetBarMode(1);

input:n(NumericSimple);

//Keltner Channels 的繪製，是以一條指數移動平均線為中間， 然後在上下兩邊依據所謂的"平均真實範圍值"來繪出軌道的範圍來。

KeltnerMA = XAverage(close, n);
```

---


---

## 腳本檔案: 函數/技術指標/KeltnerUB.xs

```xs
{@type:function}
SetBarMode(1);

input:Para(NumericSimple);

//Keltner Channels 的繪製，是以一條指數移動平均線為中間， 然後在上下兩邊依據所謂的"平均真實範圍值"來繪出軌道的範圍來。

KeltnerUB = KeltnerMA(20) + ATR(20) * Para;
```

---


---

## 腳本檔案: 函數/技術指標/KO成交量擺盪指標.xs

```xs
{@type:function}
SetBarMode(2);

Input: Length1(numericsimple, "短天期");
Input: Length2(numericsimple, "長天期");

variable: kovolume(0), tp(0), ko(0), koaverage(0);   

tp = typicalprice;   

if tp >= tp[1] then   
	kovolume = volume   
else    
	kovolume = -volume;
  
ko = average(kovolume, Length1) - average(kovolume, Length2);

ret = ko;
```

---


---

## 腳本檔案: 函數/技術指標/KST確認指標.xs

```xs
{@type:function}
SetBarMode(1);

value1=average(rateofchange(close,12),10);
value2=average(rateofchange(close,20),10);
value3=average(rateofchange(close,30),8);
value4=average(rateofchange(close,40),15);

ret = value1+value2*2+value3*3+value4*4;
```

---


---

## 腳本檔案: 函數/技術指標/MA_Osc.xs

```xs
{@type:function}
SetBarMode(1);

{
 XQ: MA-Osc :移動平均線擺盪指標。將兩條不同天期的簡單移動平均線相減即得
 Length1:第1條平均線期數
 Length2:第2條平均線期數
}
input: Length1(numeric), Length2(numeric);

value1 = Average(close, Length1);
value2 = Average(close, Length2);
value3 = (value1 - value2);

ma_osc = value3;
```

---


---

## 腳本檔案: 函數/技術指標/MACD.xs

```xs
{@type:function}
SetBarMode(1);

// MACD function
//	Input: Price序列, FastLength, SlowLength, MACDLength
//  Output: DifValue, MACDValue, OscValue
// 
Input: Price(numericseries), FastLength(numericsimple), SlowLength(numericsimple), MACDLength(numericsimple);
Input: DifValue(numericref), MACDValue(numericref), OscValue(numericref);

DifValue = XAverage(price, FastLength) - XAverage(price, SlowLength);
MACDValue = XAverage(DifValue, MACDLength) ;
OscValue = DifValue - MACDValue;
```

---


---

## 腳本檔案: 函數/技術指標/MAM.xs

```xs
{@type:function}
SetBarMode(2);

{
 XQ: MAM指標 :當日所計算出移動平均值減去n日前的移動平均值
 Length:計算平均期數
 Distance:相隔期間
}
Input: Length(numeric), Distance(numeric);

Value1 = Average(Close, Length);
Value2 = Average(Close, Length)[Distance];

MAM = Value1 - Value2;
```

---


---

## 腳本檔案: 函數/技術指標/MI.xs

```xs
{@type:function}
SetBarMode(1);

{
XQ: MI 質量指標
Length:計算EMA期數
SumLength:計算總和期數
}
input: Length(numeric), SumLength(numeric);
variable: ema1(0), ema2(0), divSeries(0), mit(0);


ema1 = XAverage(High - Low, length);
ema2 = XAverage(ema1, length);

if ema2 <> 0 then
	divSeries = ema1 / ema2
else
	divSeries = 0;

if CurrentBar >= sumLength then
	mit = Summation(divSeries, sumLength)
else
	mit = 0;

MI =mit;
```

---


---

## 腳本檔案: 函數/技術指標/MO.xs

```xs
{@type:function}
SetBarMode(2);

{
MO運動量震盪指標(Momentum Oscillator)可以說是
MOM運動量指標的另一種的表現方式，
它把原先以絕對數值展現的MOM指標，改成以相對的數值來展現
Length: 計算期數
}

input: Length(numeric);

 if  Close[Length] > 0  then
        mo = 100 * Close / Close[Length]
	else
	    mo=0;
```

---


---

## 腳本檔案: 函數/技術指標/Momentum.xs

```xs
{@type:function}
SetBarMode(2);

// Momentum function
//
input: price(numericseries), length(numericsimple);

Momentum = price - price[length];
```

---


---

## 腳本檔案: 函數/技術指標/MTM.xs

```xs
{@type:function}
SetBarMode(1);

{
以收盤價計算的運動量指標
Length: 計算期數
}
input: Length(numeric);

MTM = Momentum(Close, Length);
```

---


---

## 腳本檔案: 函數/技術指標/MTM_MA.xs

```xs
{@type:function}
SetBarMode(2);

{
對收盤價的運動量指標取再次平均價
Length: 計算期數
}
input: Length(numeric);

value1 = Momentum(Close, Length);
if CurrentBar >= Length then
	Value2 = Average(Value1, Length)
else
	Value2 = Value1;

mtm_ma = value2;
```

---


---

## 腳本檔案: 函數/技術指標/PercentB.xs

```xs
{@type:function}
// %b from BollingerBand function
//

input: 
	Price(numericseries, "數列"),
	Length(numericsimple, "天數"), 
	UpperBand(numericsimple, "上"), 
	LowerBand(numericsimple, "下");

variable: up(0), down(0), mid(0);

up = bollingerband(Price, Length, UpperBand);
down = bollingerband(Price, Length, -1 * LowerBand);

if up - down <> 0 then 
	percentb = 100 * (Price - down) / (up - down) 
else 
	percentb = 0;
```

---


---

## 腳本檔案: 函數/技術指標/PercentR.xs

```xs
{@type:function}
SetBarMode(1);

// PercentR function (for 威廉指標)
//
input: Length(numericsimple);
variable: variableA(0), variableB(0);

variableA = Highest(High, Length);
variableB = variableA - Lowest(Low, Length);

if variableB <> 0 then  
	PercentR = 100 - ((variableA - Close) / variableB) * 100
else 
	PercentR = 0;
```

---


---

## 腳本檔案: 函數/技術指標/PSY.xs

```xs
{@type:function}
SetBarMode(1);

{
XQ心理線:人氣指標心理線，計算特定期間內，行情上漲期數的比例
Length: 計算期數
}
input: Length(numeric);

PSY = 100 * CountIf(Close > Close[1], Length) / Length;
```

---


---

## 腳本檔案: 函數/技術指標/PVC.xs

```xs
{@type:function}
SetBarMode(1);

Input: Length(numericsimple, "天數");

value1 = Average(Volume, Length);
if value1 <> 0 then
	PVC = 100 * (Volume - value1) / value1
else
	PVC = 0;
```

---


---

## 腳本檔案: 函數/技術指標/Q指標.xs

```xs
{@type:function}
SetBarMode(2);

input:t1(numericsimple,"天期");
input:t2(numericsimple,"平均天期");
input:t3(numericsimple,"雜訊平滑天期");
variable:Qindicator(0);

value1=close-close[1];			//價格變化
value2=summation(value1,t1);	//累積價格變化
value3=average(value2,t2);
value4=absvalue(value2-value3);	//雜訊
value5=average(value4,t3);		//把雜訊移動平均


if value5 = 0 then 
	Qindicator = 0
else
	Qindicator = value3 / value5*5;

ret = Qindicator;
```

---


---

## 腳本檔案: 函數/技術指標/RC.xs

```xs
{@type:function}
SetBarMode(2);

{
RC指標變動率
Length: 計算期數
}
input: Length(numeric);

if  Close[Length] > 0 then
 RC = (Close - Close[Length]) / Close[Length]
else
 RC=0;
```

---


---

## 腳本檔案: 函數/技術指標/RSI.xs

```xs
{@type:function}
SetBarMode(2);

// RSI function (for RSI指標)
//
input: price(numericseries), length(numericsimple);                                             

variable: sumUp(0), sumDown(0), up(0), down(0);

if CurrentBar = 1 then
  begin
	sumUp = Average(maxlist(price - price[1], 0), length); 
	sumDown = Average(maxlist(price[1] - price, 0), length); 
  end
else
  begin
	up = maxlist(price - price[1], 0);
	down = maxlist(price[1] - price, 0);
	
	sumUp = sumUp[1] + (up - sumUp[1]) / length;
	sumDown = sumDown[1] + (down - sumDown[1]) / length;
  end;

if sumUp + sumDown = 0 then
	RSI = 0
else
	RSI = 100 * sumUp / (sumUp + sumDown);
```

---


---

## 腳本檔案: 函數/技術指標/RSV.xs

```xs
{@type:function}
SetBarMode(1);

{
XQ: RSV指標 Raw Stochastic Value
Length: 計算期數
}
input: Length(numeric);
variable: RSVt(3), Kt(3), rsvx(0), k(0), _d(0);

Stochastic(Length, RSVt, Kt, rsvx, k, _d);

RSV =rsvx;
```

---


---

## 腳本檔案: 函數/技術指標/SAR.xs

```xs
{@type:function}
SetBarMode(2);

// SAR function (for SAR指標)
//
Input: AFInitial(numericsimple);
Input: AFIncrement(numericsimple);
Input: AFMax(numericsimple);

variable:
	presar(0), ep(0), upTrend(false), af(0);
	
if CurrentBar = 1 then
  begin
	if Close > Close[1] then	// 上漲
	  begin
		upTrend = true;
		sar = Low[1];
		ep = High[1];
	  end	
	else						// 下跌
	  begin
		upTrend = false;
		sar = High[1];
		ep = Low[1];
	  end;	

	af = AFInitial;
	presar = sar;
  end
else
  begin  
	sar = presar + af * (ep - presar);
	presar = sar;
	if upTrend = true then
	  begin
		if High > ep then		// 繼續破high
		  begin
			ep = High;
			af = minlist(af + AFIncrement, AFMax);
		  end;
		
		if sar >= Low then		// 反轉
		  begin
			presar = ep;
			ep = Low;
			af = AFInitial;
			sar = presar;
			upTrend = false;
		  end;	
	  end
	else
	  begin
		if Low < ep then		// 繼續破low
		  begin
			ep = Low;
			af = minlist(af + AFIncrement, AFMax);
		  end;

		if sar <= High then		// 反轉
		  begin
			presar = ep;
			ep = High;
			af = AFInitial;
			sar = presar;
			upTrend = true;
		  end;	
	  end;
  end;
```

---


---

## 腳本檔案: 函數/技術指標/Stochastic.xs

```xs
{@type:function}
SetBarMode(2);

// Stochastic function (for KD/RSV相關指標)
//
// Input: length, rsvt, kt
// Return: rsv_value, k_value, d_value
//
input:
	length(numericsimple), rsvt(numericsimple), kt(numericsimple),
	rsv(numericref), k(numericref), d(numericref);

variable:
	maxHigh(0), minLow(0);

maxHigh = Highest(high, length);
minLow = Lowest(low, length);

if maxHigh <> minLow then
	rsv = 100 * (close - minLow) / (maxHigh - minLow)
else
	rsv = 50;

if currentbar = 1 then
  begin
	k = 50;
	d = 50;
  end
else
  begin
	k = (k[1] * (rsvt - 1) + rsv) / rsvt;
	d = (d[1] * (kt - 1) + k) / kt;
  end;  

stochastic = 1;
```

---


---

## 腳本檔案: 函數/技術指標/TechScore.xs

```xs
{@type:function}
SetBarMode(2);

// 利用多種指標, 計算多空分數
//
variable: count(0);

// 每次計算都要reset
count = 0;

//------------------ Arron指標 -------------------//
variable: arron_up(0),arron_down(0),arron_oscillator(0);//arron oscillator
arron_up=(25-nthhighestbar(1,high,25))/25*100;
arron_down=(25-nthlowestbar(1,low,25))/25*100;
arron_oscillator=arron_up-arron_down;
if arron_up > arron_down and arron_up > 70 and arron_oscillator > 50
then count=count+1;

//------------------ 隨機漫步指標 ---------------//
variable: RWIH(0),RWIL(0);
value1 = standarddev(close,10,1);
value2 = average(truerange,10);
if value1 <> 0 and value2 <> 0 then
begin
  RWIH=(high-low[9])/value2*value1;
  RWIL=(high[9]-low)/value2*value1;
end;
  
if RWIH > RWIL
then count=count+1;

//------------------ 順勢指標 -------------------//
variable:bp1(0),abp1(0);
if truerange <> 0 then  
	bp1=(close-close[1])/truerange*100;//順勢指標

abp1=average(bp1,10);
if abp1 > 0
then count=count+1;

//---------- CMO錢德動量擺動指標 ----------------//
variable:SU(0),SD(0),CMO1(0), SUSUM(0), SDSUM(0);

if close >= close[1] then 
	SU=CLOSE-CLOSE[1]
else
	SU=0;

if close < close[1] then 
	SD=CLOSE[1]-CLOSE
else
	SD=0;

SUSUM = summation(SU,9);
SDSUM = summation(sd,9);
if (SUSUM+SDSUM) <> 0 then 
	cmo1=(SUSUM-SDSUM)/(SUSUM+SDSUM)*100;

if linearregslope(cmo1,5) > 0
then count=count+1;

//------------------ RSI指標 -------------------//
variable: rsiShort(0), rsiLong(0);
rsiShort=rsi(close,5);
rsiLong=rsi(close,10);
if rsiShort > rsiLong and rsiShort < 90
then count=count+1;

//----------------- MACD指標 -------------------//
variable: Dif_val(0), MACD_val(0), Osc_val(0);  
MACD(Close, 12, 26, 9, Dif_val, MACD_val, Osc_val); 
if osc_val > 0
then count=count+1;

//----------------- MTM指標 -------------------//
if mtm(10) > 0
then count=count+1;

//----------------- KD指標 --------------------//
variable:rsv1(0),k1(0),d1(0);
stochastic(9,3,3,rsv1,k1,d1);
if k1 > d1 and k1 < 80
then count=count+1;

//----------------- DMI指標 -------------------//
variable:pdi_value(0),ndi_value(0),adx_value(0);
DirectionMovement(14,pdi_value,ndi_value,adx_value);
if pdi_value > ndi_value 
then count=count+1; 

//----------------- AR指標 -------------------//
variable: arValue(0);
arValue = ar(26);
if linearregslope(arValue,5) > 0
then count=count+1;

//----------------- ACC指標 -----------------//
if acc(10) > 0
then count=count+1;

//----------------- TRIX指標 ----------------//
if trix(close,9) > trix(close,15)
then count=count+1;

//----------------- SAR指標 ----------------//
if close > SAR(0.02, 0.02, 0.2)
then count=count+1;

//----------------- 均線指標 ----------------//
if average(close,5) > average(close,12)
then count=count+1;

// Return value
//
ret = count;
```

---


---

## 腳本檔案: 函數/技術指標/TRIX.xs

```xs
{@type:function}
SetBarMode(2);

// TRIX function (for TRIX指標)
//
Input: price(numericseries), length(numericsimple);

value1 = XAverage(price, length);
value2 = XAverage(value1, length);
value3 = XAverage(value2, length);
	
if CurrentBar = 1 then
	TRIX = 0
else
begin
    if value3[1] <> 0 then
        TRIX = (value3 - value3[1]) / value3[1]
    else
        TRIX = 0;
end;
```

---


---

## 腳本檔案: 函數/技術指標/TurnOverRate.xs

```xs
{@type:function}
input:period(numericsimple);
value1=GetField("股本(億)","D")*10000;
value2=average(volume,period);
if value1<>0
then value3=value2/value1*100;
turnoverrate=value3;
```

---


---

## 腳本檔案: 函數/技術指標/VA.xs

```xs
{@type:function}
SetBarMode(2);

VA = VA[1] + VAO;
```

---


---

## 腳本檔案: 函數/技術指標/VAO.xs

```xs
{@type:function}
SetBarMode(1);

variable: support(0), resist(0), hlDiff(0);
 
support = (Close - Low);
resist = (High - Close);
hlDiff = (High - Low);

if hlDiff = 0 then
	VAO = 0
else
	VAO = (support - resist) / hlDiff * v;
```

---


---

## 腳本檔案: 函數/技術指標/VHF.xs

```xs
{@type:function}
SetBarMode(2);

{
XQ: VHF指標
Length: 計算期數
}
input: Length(numeric);
Variable: hp(0), lp(0), numerator(0), denominator(0), VHFt(0);

hp = highest(Close, Length);
lp = lowest(Close, Length);

numerator = hp - lp;
denominator = Summation(absvalue((Close - Close[1])), Length);

if denominator <> 0 then
	VHFt = numerator / denominator
else
	VHFt = 0;

VHF = VHFt;
```

---


---

## 腳本檔案: 函數/技術指標/VPT.xs

```xs
{@type:function}
SetBarMode(2);

// XQ: PVT指標
//

If CurrentBar = 1 then
	VPT = 0
else	
	VPT = VPT[1] + (close - close[1])/close[1] * Volume;
```

---


---

## 腳本檔案: 函數/技術指標/VR.xs

```xs
{@type:function}
SetBarMode(2);

input:Length(numericsimple);
setinputname(1,"天數");
variable:UPV(0),DNV(0),NCV(0);
{
VR容量比率	
	UPV=N日內上漲天數的成交量總合
	DNV=N日內下跌天數的成交量總合
	NCV=N日內持平天數的成交量總合
}

UPV = SummationIf((C > C[1]), volume, Length);  
DNV = SummationIf((C < C[1]), volume, Length);  
NCV = SummationIf((C = C[1]), volume, Length);  

VR = iff(DNV + NCV/2=0,VR[1],100 * (UPV + NCV/2)/(DNV + NCV/2));
```

---


---

## 腳本檔案: 函數/技術指標/VVA.xs

```xs
{@type:function}
SetBarMode(2);

// XQ: VVA指標
//

if High <> Low then
	Value1 = (Close - Open)/(High - Low) * Volume
else
	Value1 = 0;

If CurrentBar = 1 then
	VVA = Value1
else	
	VVA = Value1 + VVA[1];
```

---


---

## 腳本檔案: 函數/技術指標/WAD.xs

```xs
{@type:function}
SetBarMode(2);

{
XQ: WA/D 指標
}

variable: wadt(0), adt(0);

if CurrentBar = 1 then
	wadt = 0
else
  begin
	if close = close[1] then
		adt = 0
	else
	  begin
		if close < close[1] then
			adt = close - TrueHigh
		else
			adt = close - TrueLow;
	  end;

	wadt = adt + wadt[1];
  end;

WAD = wadt;
```

---


---

## 腳本檔案: 函數/排行/乖離率排行榜.xs

```xs
{@type:function}
SetBarMode(1);

// 這是一個自訂排行條件的範例
// 示範如何針對內建函數的回傳值進行排序
// 使用者可以自行替換成需要使用的函數
//
// Length是期數
//

input:
	Length(5, numericsimple, "計算期間");

retval = bias(Length);
```

---


---

## 腳本檔案: 函數/排行/外資連續買超排行榜.xs

```xs
{@type:function}
SetBarMode(1);

// 這是一個自訂排行條件的範例
// 示範如何依外資連續N期買超的張數進行排序
// 使用者可以自行替換成需要使用的欄位
//
// Length是期數
//

input:
	Length(10, numericsimple, "計算期間");

if TrueAll(GetField("外資買賣超") > 0, Length) Then
   retval = Summation(GetField("外資買賣超"), Length)
Else
   return;

{ 
//如果要排序投信連續買超，可以改用"投信買賣超"的欄位:
if TrueAll(GetField("投信買賣超") > 0, Length) Then
   retval = Summation(GetField("投信買賣超"), Length)
Else
   return;

//如果要排序自營商連續買超，可以改用"自營商買賣超"的欄位:
if TrueAll(GetField("自營商買賣超") > 0, Length) Then
   retval = Summation(GetField("自營商買賣超"), Length)
Else
   return;
   
//可以依需要自行更換欄位
}
```

---


---

## 腳本檔案: 函數/排行/收盤價排行榜.xs

```xs
{@type:function}
SetBarMode(1);

// 這是一個自訂排行條件的範例
// 示範如何針對特定欄位的數值進行排序
// 使用者可以自行替換成需要使用的欄位
//
//

retval = GetField("收盤價");

{
//同理，當日漲跌幅的排行榜就會是：
retval = GetField("漲跌幅");
}
```

---


---

## 腳本檔案: 函數/排行/收盤均價排行榜.xs

```xs
{@type:function}
SetBarMode(1);

// 這是一個自訂排行條件的範例
// 示範如何針對特定欄位的N期平均進行排序
// 使用者可以自行替換成需要使用的欄位
//
// Length是期數

input:
	Length(3, numericsimple, "計算期間");

retval = Average(GetField("收盤價"),Length);

{
//如果想做均量的排行榜，只需要更換欄位為成交量：
retval = Average(GetField("成交量"),Length);
}
```

---


---

## 腳本檔案: 函數/排行/漲幅排行榜.xs

```xs
{@type:function}
SetBarMode(1);

// 這是一個自訂排行條件的範例
// 示範如何針對特定欄位的N期增幅進行排序
// 使用者可以自行替換成需要使用的欄位
//
// Length是期數

input:
	Length(20, numericsimple, "計算期間");
 
retval = rateofchange(GetField("收盤價"),Length);
```

---


---

## 腳本檔案: 函數/排行/跌幅排行榜.xs

```xs
{@type:function}
SetBarMode(1);

// 這是一個自訂排行條件的範例
// 示範如何針對特定欄位的N期減幅進行排序
// 使用者可以自行替換成需要使用的欄位
//
// Length是期數

input:
	Length(20, numericsimple, "計算期間");
 
retval = -rateofchange(GetField("收盤價"),Length);
```

---


---

## 腳本檔案: 函數/日期相關/BarsLast.xs

```xs
{@type:function}
SetBarMode(2);

input:  pX(TrueFalseSeries);

if pX then value1 = currentbar;

BarsLast = currentbar - value1;
```

---


---

## 腳本檔案: 函數/日期相關/DateTime.xs

```xs
{@type:function}
setbarmode(1);
datetime = date*1000000 + time;
```

---


---

## 腳本檔案: 函數/日期相關/DaysToExpiration.xs

```xs
{@type:function}
SetBarMode(1);

// 傳入到期月份/年份, 回傳資料日期與到期日之間還差幾日
// 範例: Value1 = DaysToExpiration(4, 2013)
//
input:  
	_ExpiredM(numericsimple),
    _ExpiredY(numericsimple);

variable:
	lastTradeDate(0);
	
lastTradeDate = GetLastTradeDate(_ExpiredM, _ExpiredY);
DaysToExpiration = DateDiff(lastTradeDate, Date) + 1;
```

---


---

## 腳本檔案: 函數/日期相關/FormatMQY.xs

```xs
{@type:function_string}
SetBarMode(1);

input:Date1(numericsimple);

value1 = ceiling(month(Date1)/3);
switch (Barfreq) Begin
	case "M","AM":
		formatMQY = Formatdate("yyyyMM",Date1);
	case "Q" :
		formatMQY = Formatdate("yyyy",Date1) + "Q" + numtostr(value1,0);
	case "Y" :
		formatMQY = Formatdate("yyyy",Date1);
	default:
		formatMQY = Formatdate("yyyyMMdd",Date1);
end;
```

---


---

## 腳本檔案: 函數/日期相關/GetBarOffsetForYears.xs

```xs
{@type:function}
{
	計算BarOffset for N years
	
	return 0 if out-of-range
}

input: years(numericsimple, "N年");

value1 = DateAdd(Date, "Y", -1 * years);
retval = GetBarOffset(value1);
```

---


---

## 腳本檔案: 函數/日期相關/GetLastTradeDate.xs

```xs
{@type:function}
SetBarMode(1);

// 傳入到期月份/年份, 回傳台灣期交所指數期貨的到期日
// (不考慮國定假日等特殊事件)
//
input:  
	_ExpiredM(numericsimple),
    _ExpiredY(numericsimple);

GetLastTradeDate = NthDayofMonth(EncodeDate(_ExpiredY,_ExpiredM,1),3,3);
```

---


---

## 腳本檔案: 函數/日期相關/LastDayOfMonth.xs

```xs
{@type:function}
SetBarMode(1);

input: SelectedMonth(numericsimple);

value1 = dateadd(EncodeDate(year(date),SelectedMonth,1),"M",1);
value2 = dateadd(value1,"D",-DayOfMonth(value1));
retval = DayOfMonth(value2);
```

---


---

## 腳本檔案: 函數/日期相關/NthDayOfMonth.xs

```xs
{@type:function}
SetBarMode(1);

// 計算自某一天起算的第N個星期序數的日期
//
input: StartDate(numericsimple), Nth(numericsimple), TargetDay(numericsimple);

variable: OddDaysOfWeek(0);

OddDaysOfWeek = TargetDay - DayOfWeek(StartDate);

If OddDaysOfWeek > 0 Then
	NthDayofMonth = dateadd(startdate,"D", iff(Nth >= 0,(Nth - 1 ),Nth) * 7 + OddDaysOfWeek)
Else if OddDaysOfWeek < 0 Then
	NthDayofMonth = dateadd(startdate,"D", iff(Nth >= 0,Nth,(Nth + 1)) * 7 + OddDaysOfWeek)
Else
	NthDayofMonth = dateadd(startdate,"D", iff(Nth >= 0,Nth - 1, Nth + 1) * 7);
```

---


---

## 腳本檔案: 函數/期權相關/BlackScholesModel.xs

```xs
{@type:function}
SetBarMode(1);

input:
	iCallPutFlag(stringsimple),	 	//C表買權、P表賣權
    iSpotPrice(numericsimple),		//標的價格
	iStrikePrice(numericsimple),	//履約價
	iDtoM(numericsimple),			//到期天數
	iRate100(numericsimple),		//無風險利率
	iB100(numericsimple),			//持有成本
									//股票選擇權 b=r-殖利率
									//期貨選擇權 b=0
									//外匯選擇權 b=r-外國無風險利率
	iVolity100(numericsimple),		//波動率
	oOptPriceValue(numericref), 	//選擇權理論價
	oDelta(numericref), 			//Delta
	oGamma(numericref), 			//Gamma
	oVega(numericref), 				//Vega
	oTheta(numericref), 			//Theta
	oRho(numericref);				//Rho

variable:
	optiontype(iff(upperstr(iCallPutFlag)="P",-1,1)),
	d1(0),d2(0),nd1(0),nd2(0),nd1_prob(0),iRate(0),iB(0),iVolity(0),
	ty(0.002739726027),
	t(iDtoM*ty);

	optiontype = iff(upperstr(iCallPutFlag)="P",-1,1);
	t = iDtoM*ty;
	
	iRate = iRate100*0.01;
	iB = iB100*0.01;
	iVolity = iff(iVolity100=0,0.00000001,iVolity100*0.01);
	t = iDtoM*ty;

    If t > 0 Then
	begin
	
        d1 = (Log(iSpotPrice / iStrikePrice) + (iB + square(iVolity) * 0.5) * t) / (iVolity * SquareRoot(t));
		d2 = d1 - iVolity * SquareRoot(t);
        Nd1 = NormSDist(d1 * optiontype);
        Nd2 = NormSDist(d2 * optiontype);
        Nd1_Prob = ExpValue( -Square(d1) * 0.5 ) * 0.398942280407;

		oOptPriceValue = (iSpotPrice * ExpValue((iB - iRate) * t) * Nd1 - iStrikePrice * ExpValue(-iRate * t) * Nd2) * optiontype;
		oDelta = ExpValue((iB - iRate) * t) * Nd1 * optiontype;
		oGamma = ExpValue((iB - iRate) * t) * Nd1_Prob / (iSpotPrice * iVolity * SquareRoot(t));
		oVega = iSpotPrice * ExpValue((iB - iRate) * t) * SquareRoot(t) * Nd1_Prob * 0.01;		
		oTheta = (-iSpotPrice * ExpValue((iB - iRate) * t) * Nd1_Prob * iVolity / (2 * SquareRoot(t)) - optiontype * ((iB - iRate) * iSpotPrice * ExpValue((iB - iRate) * t) * Nd1 + iRate * iStrikePrice * ExpValue(-iRate * t) * Nd2)) * ty;
		oRho = iff(iB <> 0, (t * iStrikePrice * ExpValue(-iRate * t) * Nd2) * optiontype * 0.0001, -t * oOptPriceValue * 0.0001);
		
	end else begin
		oOptPriceValue=maxlist((iSpotPrice - iStrikePrice) * optiontype, 0);
		oDelta=iff(iSpotPrice > iStrikePrice,0.5 * (1 + optiontype),
				iff(iSpotPrice < iStrikePrice,0.5 * (1 + optiontype),
				0.5 * optiontype));
		oGamma=iff(iSpotPrice <> iStrikePrice,0,1);
		oVega=0;
		oTheta=0;
		oRho=0;
    end;


blackscholesmodel = 1;
```

---


---

## 腳本檔案: 函數/期權相關/BSDelta.xs

```xs
{@type:function}
SetBarMode(1);

input:
	iCallPutFlag(stringsimple),	 	//C表買權、P表賣權
    iSpotPrice(numericsimple),		//標的價格
	iStrikePrice(numericsimple),	//履約價
	iDtoM(numericsimple),			//到期天數
	iRate100(numericsimple),		//無風險利率
	iB100(numericsimple),			//持有成本
									//股票選擇權 b=r-殖利率
									//期貨選擇權 b=0
									//外匯選擇權 b=r-外國無風險利率
	iVolity100(numericsimple);		//波動率
	
variable: _Output(0);

blackscholesmodel(iCallPutFlag,iSpotPrice,iStrikePrice,iDtoM,iRate100,iB100,iVolity100,
value1,_Output,value3,value4,value5,value6);

BSDelta = _Output;
```

---


---

## 腳本檔案: 函數/期權相關/BSGamma.xs

```xs
{@type:function}
SetBarMode(1);

input:
	iCallPutFlag(stringsimple),	 	//C表買權、P表賣權
    iSpotPrice(numericsimple),		//標的價格
	iStrikePrice(numericsimple),	//履約價
	iDtoM(numericsimple),			//到期天數
	iRate100(numericsimple),		//無風險利率
	iB100(numericsimple),			//持有成本
									//股票選擇權 b=r-殖利率
									//期貨選擇權 b=0
									//外匯選擇權 b=r-外國無風險利率
	iVolity100(numericsimple);		//波動率
	
variable: _Output(0);

blackscholesmodel(iCallPutFlag,iSpotPrice,iStrikePrice,iDtoM,iRate100,iB100,iVolity100,
value1,value2,_Output,value4,value5,value6);

BSGamma = _Output;
```

---


---

## 腳本檔案: 函數/期權相關/BSPrice.xs

```xs
{@type:function}
SetBarMode(1);

input:
	iCallPutFlag(stringsimple),	 	//C表買權、P表賣權
    iSpotPrice(numericsimple),		//標的價格
	iStrikePrice(numericsimple),	//履約價
	iDtoM(numericsimple),			//到期天數
	iRate100(numericsimple),		//無風險利率
	iB100(numericsimple),			//持有成本
									//股票選擇權 b=r-殖利率
									//期貨選擇權 b=0
									//外匯選擇權 b=r-外國無風險利率
	iVolity100(numericsimple);		//波動率
	
variable: _Output(0);

blackscholesmodel(iCallPutFlag,iSpotPrice,iStrikePrice,iDtoM,iRate100,iB100,iVolity100,
_Output,value2,value3,value4,value5,value6);

BSPrice = _Output;
```

---


---

## 腳本檔案: 函數/期權相關/BSTheta.xs

```xs
{@type:function}
SetBarMode(1);

input:
	iCallPutFlag(stringsimple),	 	//C表買權、P表賣權
    iSpotPrice(numericsimple),		//標的價格
	iStrikePrice(numericsimple),	//履約價
	iDtoM(numericsimple),			//到期天數
	iRate100(numericsimple),		//無風險利率
	iB100(numericsimple),			//持有成本
									//股票選擇權 b=r-殖利率
									//期貨選擇權 b=0
									//外匯選擇權 b=r-外國無風險利率
	iVolity100(numericsimple);		//波動率
	
variable: _Output(0);

blackscholesmodel(iCallPutFlag,iSpotPrice,iStrikePrice,iDtoM,iRate100,iB100,iVolity100,
value1,value2,value3,value4,_Output,value6);

BSTheta = _Output;
```

---


---

## 腳本檔案: 函數/期權相關/BSVega.xs

```xs
{@type:function}
SetBarMode(1);

input:
	iCallPutFlag(stringsimple),	 	//C表買權、P表賣權
    iSpotPrice(numericsimple),		//標的價格
	iStrikePrice(numericsimple),	//履約價
	iDtoM(numericsimple),			//到期天數
	iRate100(numericsimple),		//無風險利率
	iB100(numericsimple),			//持有成本
									//股票選擇權 b=r-殖利率
									//期貨選擇權 b=0
									//外匯選擇權 b=r-外國無風險利率
	iVolity100(numericsimple);		//波動率
	
variable: _Output(0);

blackscholesmodel(iCallPutFlag,iSpotPrice,iStrikePrice,iDtoM,iRate100,iB100,iVolity100,
value1,value2,value3,_Output,value5,value6);

BSVega = _Output;
```

---


---

## 腳本檔案: 函數/期權相關/DaysToExpirationTF.xs

```xs
{@type:function}
SetBarMode(1);

variable:string1(""),string2(""),string3("");
variable:strike(0),cpflag(""),ww(0),mm(0),yy(0);

if instr(symbol,".TF") = 0 then 
	raiseruntimeerror("僅支援台股期貨及選擇權")
else
	string1 = leftstr(symbol,strlen(symbol) - 3);

if leftstr(string1,1) = "F" or midstr(string1,3,1) = "O" then
begin
	yy = year(date);
	if leftstr(string1,1) = "F" then
		mm = strtonum(midstr(string1,5,2))
	else
		mm = strtonum(midstr(string1,4,2));
	if mm = 0 then begin
		mm = month(date);
		value1 = 0;
		while (value1 < strtonum(rightstr(string1,1)))
		begin
			daystoexpirationtf = daystoexpiration(mm,yy);
			if (daystoexpirationtf > 0) then value1 = value1 + 1;
			value99 = DateAdd(encodedate(yy,mm,1),"M",1);
			mm = month(value99);
			yy = year(value99);
		end;
		return;
	end;
	daystoexpirationtf = daystoexpiration(mm,yy);
	return;
end else if leftstr(string1,2) = "TX" then
begin 
	value99 = NthDayofMonth(date,1,3);
	daystoexpirationtf = DateDiff(value99, Date) + 1;
	return;
end;

daystoexpirationtf = -1;
```

---


---

## 腳本檔案: 函數/期權相關/HVolatility.xs

```xs
{@type:function}
SetBarMode(1);

input: 
	thePrice(numericseries),
	Length(numericsimple);

variable: 
	vTradingDays(SquareRoot(260));                                                  

vTradingDays = SquareRoot(260);
                                                                                
if thePrice[1] = 0 then 
	value1 = 0
else 
	value1 = Log(thePrice / thePrice[1]);

HVolatility = 100 * vTradingDays * StandardDev(value1, Length, 0) ;
```

---


---

## 腳本檔案: 函數/期權相關/IVolatility.xs

```xs
{@type:function}
SetBarMode(1);

input: 
	iCallPutFlag(stringsimple),	 	//C表買權、P表賣權
    iSpotPrice(numericsimple),		//標的價格
	iStrikePrice(numericsimple),	//履約價
	iDtoM(numericsimple),			//到期天數
	iRate100(numericsimple),		//無風險利率
	iB100(numericsimple),			//持有成本
									//股票選擇權 b=r-殖利率
									//期貨選擇權 b=0
									//外匯選擇權 b=r-外國無風險利率
	iPrice(numericsimple);			//選擇權現價

variable: 
	var1( 0 ), 
	var2( 0 ), 
	var3( 0 ), 
	var4( 0 ) ;

condition1 = iDtoM > 0 and iStrikePrice > 0 and iSpotPrice > 0 ;
if condition1 then
	begin
	var1 = 100 ;
	var2 = bsprice(iCallPutFlag, iSpotPrice, iStrikePrice, iDtoM, iRate100, iB100, var1);
	while var2 < iPrice and var1 <= 900
		begin
		var1 = var1 + 100 ;
		var2 = bsprice(iCallPutFlag, iSpotPrice, iStrikePrice, iDtoM, iRate100, iB100, var1);
		end ;
	if var2 < iPrice then
		ivolatility= 999
	else
		begin
		var3 = 1 ;
		var4 = 100 ;
		while AbsValue( var2 - iPrice ) >= .005 and var3 < 11
			                                                                     
			                             
			begin
			var4 = var4 * .5 ;
			if var2 > iPrice then
				var1 = var1 - var4
			else if var2 < iPrice then
				var1 = var1 + var4 ;
			var2 = bsprice(iCallPutFlag, iSpotPrice, iStrikePrice, iDtoM, iRate100, iB100, var1);
			var3 = var3 + 1 ;
			end ;
		ivolatility= var1 ;
		end ;
	end
else
	ivolatility= 0 ;
```

---


---

## 腳本檔案: 函數/期權相關/NormSDist.xs

```xs
{@type:function}
SetBarMode(1);

//利用多項式計算近似值，精確度到小數點以下六位。

input: 
	zvalue(numericsimple);

variable: 
	a1(0.31938153),
    a2(-0.356563782),
    a3(1.781477937),
    a4(-1.821255978),
    a5(1.330274429),
	sqrtof2pi(2.506628275),
    gamma(0.2316419);
	
	
value1 = 1 / ( 1 + gamma * AbsValue( zvalue ) ) ;
value2 = ExpValue( -Square( zvalue ) * .5 ) / sqrtof2pi ;
value3 = 1 - value2 * ( ( ( ( ( a5 * value1 + a4 ) * value1 + a3 ) * value1 + a2 ) * value1 + a1 ) 
 * value1 ) ;

if zvalue < 0 then 
	NormSDist = 1 - value3
else
	NormSDist = value3;
```

---


---

## 腳本檔案: 函數/統計分析/CoefficientR.xs

```xs
{@type:function}
SetBarMode(1);

input:Indep(numericseries);{說明:獨立的K棒值}
input:Dep(numericseries);{說明:不獨立的K棒值}
input:Length(numericsimple);{說明:過去N期}

{
	                 Sum((Xi-Xb)*(Yi-Yb))
 r = --------------------------------------------------
	 Sqrt(Sum((Xi-Xb)(Xi-Xb)) * Sum((Yi-Yb)*(Yi-Yb)))
	
}

variable:
	idx(0), Xb(0), Yb(0), sumXiXb(0), sumYiYb(0), sumCovar(0);

	CoefficientR = 0;
	if Length <= 0 Then Return;
	
	Xb = average(Indep, Length);
	Yb = average(Dep, Length);
	
	sumXiXb = 0;
	sumYiYb = 0;
	sumCovar = 0;
	
	for idx = 0 to Length - 1 
	  begin
		sumXiXb = sumXiXb + (Indep[idx] - Xb) * (Indep[idx] - Xb);
		sumYiYb = sumYiYb + (Dep[idx] - Yb) * (Dep[idx] - Yb);
		sumCovar = sumCovar + (Indep[idx] - Xb) * (Dep[idx] - Yb);
	  end;
	
	if sumXiXb <> 0 and sumYiYb <> 0 then
	  begin
		Value1 = sumCovar / squareroot(sumXiXb * sumYiYb);
		if -1 <= Value1 and Value1 <= 1 then
			CoefficientR = Value1;
	  end;
```

---


---

## 腳本檔案: 函數/統計分析/Correlation.xs

```xs
{@type:function}
SetBarMode(1);

input:Indep(numericseries);{說明:獨立的K棒值}
input:Dep(numericseries);{說明:不獨立的K棒值}
input:Length(numericsimple);{說明:過去N期}

Correlation = -2;
if Length <= 0 then return;

Value1 = CountIf(Indep > Indep[1] and Dep > Dep[1], Length); 
value2 = CountIf(Indep < Indep[1] and Dep < Dep[1], Length);
value3 = CountIf(Indep = Indep[1] and Dep = Dep[1], Length);

Correlation = (Value1-value2)/(Value1+value2+value3);
```

---


---

## 腳本檔案: 函數/統計分析/Covariance.xs

```xs
{@type:function}
SetBarMode(1);

input: DepValue(numericseries),
       IndepVal(numericseries),
       Length(numericsimple);

variable:
		Xb(0), Yb(0), idx(0), sum(0);

{
	Covar(x,y) = Sum((Xi-Xb)*(Yi-Yb)) / N
}

If Length <> 0 Then
Begin
    Xb = Average(IndepVal, Length);
    Yb = Average(DepValue, Length);

	sum = 0;
    For idx = 0 To Length - 1
      Begin
      	 sum = sum + (IndepVal[idx] - Xb) * (DepValue[idx] - Yb);
      End;

    Covariance = sum / Length;
End;
```

---


---

## 腳本檔案: 函數/統計分析/RSquare.xs

```xs
{@type:function}
SetBarMode(1);

input: Indep(numericseries), Dep(numericseries), Length(numericsimple);

RSquare = Square(CoefficientR(Indep, Dep, Length));
```

---


---

## 腳本檔案: 函數/統計分析/StandardDev.xs

```xs
{@type:function}
SetBarMode(1);

input:  thePrice(numericseries), Length(numericsimple), DataType(numericsimple);

Value1 = VariancePS(thePrice, Length, DataType);
if Value1 > 0 then 
	StandardDev = SquareRoot(Value1)
else 
	StandardDev = 0;
```

---


---

## 腳本檔案: 函數/統計分析/VariancePS.xs

```xs
{@type:function}
SetBarMode(1);

input:  thePrice(numericseries), Length(numericsimple), DataType(numericsimple);

variable:  Period(0), sum(0), avg(0);

VariancePS = 0;
Period = Iff(DataType = 1, Length, Length - 1);
if Period > 0 then
begin  
	avg = Average(thePrice, Length);
	sum = 0;
	for Value1 = 0 to Length - 1
	begin
		sum = sum + Square(thePrice[Value1] - avg);
	end;
	VariancePS = sum / Period;
end;
```

---


---

## 腳本檔案: 函數/趨勢分析/Angle.xs

```xs
{@type:function}
SetBarMode(1);

input:Date1(numeric),Date2(numeric);

variable:Date1Bar(0),Date2Bar(0),Date1Price(0),Date2Price(0),_Slope(0);

Date1Bar = getbaroffset(date1); Date1Price =Open[Date1Bar];
Date2Bar = getbaroffset(date2); Date2Price =Close[Date2Bar];


if Date1Bar > Date2Bar then 
   _Slope = (Date2Price/Date1Price-1)*100 / (Date1Bar-Date2Bar);


Angle = arcTangent(_Slope);
```

---


---

## 腳本檔案: 函數/趨勢分析/Angleprice.xs

```xs
{@type:function}
input:Date1(numeric),ang(numeric);

variable:Date1Price(0);
 
Date1Price =Open[Date1];

value1=tan(ang);
value2=date1price*(1+value1*date1/100);
angleprice=value2;
```

---


---

## 腳本檔案: 函數/趨勢分析/DownTrend.xs

```xs
{@type:function_bool}
{
	判斷某個序列是否趨勢朝下
	
	注意事項:
	
	- 判斷N日趨勢會判斷均線的趨勢, 所以資料必須要有Length*2以上
	- 每次計算時會讀取近Length*2筆計算, 為了效能起見, 僅需在最新筆呼叫此函數即可

	範例:
	
	SetBackBar(2 * Length);			// 需有2倍的資料筆數	
	SetTotalBar(2);					// 
	if CurrentBar <> GetTotalBar() then return;
	ret = DownTrend(Close, Length);		
}
input: TheSeries(numericseries, "序列");
input: Length(numericsimple, "天期");

{
	底下是目前選股系統腳本使用的計算邏輯

	Condition1 = rateofchange(TheSeries, Length) <= Length; 
	Condition2 = TheSeries < TheSeries[Length/2]; 
	Condition3 = TheSeries < average(TheSeries, Length); 
	Condition4 = TheSeries <= TheSeries[1];

	retval = condition1 and condition2 and condition3 and condition4; 
}

Array: TheSeriesArray[](0);
Array: LongMA[](0);			// 儲存長MA (MA(Length))
Array: ShortMA[](0);		// 儲存短MA (MA(Length/2))

ArraySeries(TheSeries, Length, TheSeriesArray);

// Value1 = Average(TheSeries, Length);
// Value2 = Average(TheSeries, Length/2);

Var: ShortLength(Ceiling(Length/2));
ArrayMASeries(TheSeries, Length, LongMA);
ArrayMASeries(TheSeries, ShortLength, ShortMA);

if Length >= 10 then begin
	retval = 
		ShortMA[1] <= LongMA[1] and // Value2 <= Value1 and
		ArrayLinearRegSlope(LongMA, Length) < 0 and //LinearRegSlope(Value1, Length) < 0 and 
		ArrayLinearRegSlope(ShortMA, ShortLength) < 0 and //LinearRegSlope(Value2, Length/2) < 0 and
		LongMA[1] <= LongMA[2] and // Value1 <= Value1[1] and
		ShortMA[1] <= ShortMA[2] and // Value2 <= Value2[1] and
		TheSeriesArray[1] <= TheSeriesArray[2]; // TheSeries <= TheSeries[1];		
end else begin
	retval = 
		ArrayLinearRegSlope(LongMA, Length) < 0 and //LinearRegSlope(Value1, Length) < 0 and 
		LongMA[1] <= LongMA[2] and // Value1 <= Value1[1] and
		TheSeriesArray[1] <= TheSeriesArray[2]; // TheSeries <= TheSeries[1];		
end;
```

---


---

## 腳本檔案: 函數/趨勢分析/LinearReg.xs

```xs
{@type:function}
SetBarMode(1);

input:thePrice(numericseries);	{資料序列} 
input:Length(numericsimple); 	{資料長度}
input:target(numericsimple); 	{預期日期位置:0表示現在,-1表示未來一天,1表示過去一天}
input:_slope(numericref); 		{回傳:斜率}
input:_angle(numericref);		{回傳:弧度} 
input:intercept(numericref);	{回傳:X軸切點} 
input:forecast(numericref); 	{回傳:target日後預期值}

variable: SumX((Length* (Length+1))/2), //和
      sumX2(Length*(Length+1)*(2*Length+1)/6 ), //平方和
      sumY(0),
      SumXY(0),
      t_slope(0),
      tIntercept(0);
	
sumX2 = Length*(Length+1)*(2*Length+1)/6;
SumX = (Length* (Length+1))/2;

LinearReg = -1;
if Length < 1 then return;

variable: Xi(0);

SumXY=0; SumY =0;
for Xi = 1 to Length
Begin
   SumXY += Xi* thePrice[ Length -Xi];
   SumY  += thePrice[ Length -Xi];
End;

t_slope = IFF((Length*SumX2 -Square(SumX))<>0,
             ( Length *SumXY -SumX *SumY) / (Length*SumX2 -Square(SumX)),
			 0);
tIntercept = (SumY - t_slope*SumX)/Length;

_slope =t_slope;
_angle = arctangent(t_slope);
intercept =tIntercept;
forecast = intercept + _slope * (Length - target + ExecOffset);

LinearReg = 1;
```

---


---

## 腳本檔案: 函數/趨勢分析/LinearRegAngle.xs

```xs
{@type:function}
SetBarMode(1);

input:thePrice(numericseries); //"價格序列"
input:Length(numericsimple);   //"計算期間"

variable: _Output(0);

LinearReg(thePrice, Length, 0, value1, _Output, value3, value4);

LinearRegAngle = _Output;
```

---


---

## 腳本檔案: 函數/趨勢分析/LinearRegSlope.xs

```xs
{@type:function}
SetBarMode(1);

input:thePrice(numericseries); //"價格序列"
input:Length(numericsimple);   //"計算期間"

variable: _Output(0);

LinearReg(thePrice, Length, 0, _Output, value2, value3, value4);

LinearRegSlope = _Output;
```

---


---

## 腳本檔案: 函數/趨勢分析/NDaysAngle.xs

```xs
{@type:function}
{
	計算股價N日走勢的角度

	上漲趨勢回傳值 = 0 ~ 90
	下跌趨勢回傳值 = 0 ~ -90
}

input: Length(numericsimple, "天期");

{
                      | y=<Close/Close[N]-1>
					  |
	------------------+ y=0
	
	- Y軸的數值, 是Close/Close[N]-1, 
	- 第一筆的數值是0, 如果上漲50%, 則數值 = 0.5, 如果上漲100%, 則數值=1
	
	- consider: X邊如果是N, Y邊如果是0.5(上漲50%), 那算出來的斜率 x 2N之後, 表示這是一個x=1/y=1的三角形, 角度=45度角

	上漲跟下跌的差異
	
	- 上漲100%, 例如4元漲到8元 => y = 1
	- 下跌50%, 例如8元跌到4元 => y = -0.5

}

array: thePriceArray[](0);
var: idx(0);

var: angle45(0), factor45(0);

// 定義N日上漲 x% = 45度
//
if Length <= 5 then angle45 = 30
else if Length <= 10 then angle45 = 50
else if Length <= 20 then angle45 = 75
else if Length <= 60 then angle45 = 100
else if Length <= 120 then angle45 = 150
else angle45 = 200;

// 底邊 = Length
// 高度 = 上漲%
//
factor45 = Length / (0.01 * angle45);

Array_SetMaxIndex(thePriceArray, Length);
for idx = 1 to Length begin
	thePriceArray[idx] = (Close[idx-1] / Close[Length-1] - 1) * factor45;
end;

value1 = ArrayLinearRegSlope(thePriceArray, Length);
value2 = arctangent(value1);

// 因為下跌最多就是100%, 所以算出來最多角度=-45度, 所以下跌角度會 x 2, 希望上漲角度/下跌角度可以在同一個scale內
//
if value2 < 0 then value2 = value2 * 2;
retval = value2;
```

---


---

## 腳本檔案: 函數/趨勢分析/SwingHigh.xs

```xs
{@type:function}
SetBarMode(2);

input: Price(numericseries), Length(numericsimple), LeftStrength(numericsimple), RightStrength(numericsimple), occur(numericsimple);
//價格序列、時間長度、左區間、右區間、第幾個峰值

variable: now(0), tmpnow(0), cnt(0), success(0);

now = Rightstrength;
cnt = 0;

while cnt < occur and now < Length
begin
	success = 1;
	tmpnow = now+1;
	while success = 1 and tmpnow-now <= LeftStrength
	begin
		if Price[now] < Price[tmpnow] then
			success = 0
		else tmpnow = tmpnow+1;
	end;
	
	tmpnow = now-1;
	while success = 1 and now-tmpnow <= RightStrength
	begin
		if Price[now] <= Price[tmpnow] then
			success = 0
		else tmpnow = tmpnow-1;
	end;
	
	if success = 1 then
		cnt = cnt+1;
	now = now+1;
end;

if cnt < occur then
	SwingHigh = -1
else
	swingHigh = Price[now-1];
```

---


---

## 腳本檔案: 函數/趨勢分析/SwingHighBar.xs

```xs
{@type:function}
SetBarMode(2);

input: 
Price(numericseries), 
Length(numericsimple), 
LeftStrength(numericsimple), 
RightStrength(numericsimple), 
occur(numericsimple);
//價格序列、時間長度、左區間、右區間、第幾個峰值

variable: now(0), tmpnow(0), cnt(0), success(false);

now = Rightstrength;
cnt = 0;

while cnt < occur and now < Length
begin
	success = true;
	tmpnow = now+1;
	while success = true and tmpnow-now <= LeftStrength
	begin
		if Price[now] < Price[tmpnow] then
			success = false
		else tmpnow = tmpnow+1;
	end;
	
	tmpnow = now-1;
	while success = true and now-tmpnow <= RightStrength
	begin
		if Price[now] <= Price[tmpnow] then
			success = false
		else tmpnow = tmpnow-1;
	end;
	
	if success = true then
		cnt = cnt+1;
		
	now = now+1;
end;

if cnt < occur then
	swingHighBar  = -1
else
	swingHighBar  = now-1;
```

---


---

## 腳本檔案: 函數/趨勢分析/SwingLow.xs

```xs
{@type:function}
SetBarMode(2);

input: Price(numericseries), Length(numericsimple), LeftStrength(numericsimple), RightStrength(numericsimple), occur(numericsimple);
//價格序列、時間長度、左區間、右區間、第幾個峰值

variable: now(0), tmpnow(0), cnt(0), success(0);

now = Rightstrength;
cnt = 0;

while cnt < occur and now < Length
begin
	success = 1;
	tmpnow = now+1;
	while success = 1 and tmpnow-now <= LeftStrength
	begin
		if Price[now] > Price[tmpnow] then
			success = 0
		else tmpnow = tmpnow+1;
	end;
	
	tmpnow = now-1;
	while success = 1 and now-tmpnow <= RightStrength
	begin
		if Price[now] >= Price[tmpnow] then
			success = 0
		else tmpnow = tmpnow-1;
	end;
	
	if success = 1 then
		cnt = cnt+1;
	now = now+1;
end;

if cnt < occur then
	SwingLow = -1
else
	swingLow = Price[now-1];
```

---


---

## 腳本檔案: 函數/趨勢分析/SwingLowBar.xs

```xs
{@type:function}
SetBarMode(2);

input: Price(numericseries), Length(numericsimple), LeftStrength(numericsimple), RightStrength(numericsimple), occur(numericsimple);
//價格序列、時間長度、左區間、右區間、第幾個峰值

variable: now(0), tmpnow(0), cnt(0), success(0);

now = Rightstrength;
cnt = 0;

while cnt < occur and now < Length
begin
	success = 1;
	tmpnow = now+1;
	while success = 1 and tmpnow-now <= LeftStrength
	begin
		if Price[now] > Price[tmpnow] then
			success = 0
		else tmpnow = tmpnow+1;
	end;
	
	tmpnow = now-1;
	while success = 1 and now-tmpnow <= RightStrength
	begin
		if Price[now] >= Price[tmpnow] then
			success = 0
		else tmpnow = tmpnow-1;
	end;
	
	if success = 1 then
		cnt = cnt+1;
	now = now+1;
end;

if cnt < occur then
	SwingLowBar = -1
else
	SwingLowBar = now-1;
```

---


---

## 腳本檔案: 函數/趨勢分析/TimeSeriesForecast.xs

```xs
{@type:function}
SetBarMode(1);

input: thePrice(numericseries), Length(numericsimple), TgtBar(numericsimple);
variable: _Output(0);

LinearReg(thePrice, Length, TgtBar, value1, value2, value3, _Output);

TimeSeriesForecast = _Output;
```

---


---

## 腳本檔案: 函數/趨勢分析/TSELSindex.xs

```xs
{@type:function}
{
函數說明
https://www.xq.com.tw/xstrader/打造自己的大盤多空函數/
}

SetBarMode(1);

input:Length(numeric);
input:LowLimit(numeric);
 
if countif(GetSymbolField("tse.tw","外資買賣超金額","D") > 0,Length) >= LowLimit
and GetSymbolField("tse.tw","外資買賣超金額","D") > 0 then
	value1 = 1
else
	value1 = 0;

tselsindex = value1;
```

---


---

## 腳本檔案: 函數/趨勢分析/TSEMFI.xs

```xs
{@type:function}
SetBarMode(2);

variable: tp(0), tv(0), utv(0), dtv(0), pmf(0), nmf(0), mfivalue(0);

tp = (getsymbolfield("TSE.TW","最高價")+getsymbolfield("TSE.TW","最低價")+getsymbolfield("TSE.TW","收盤價")) /3;
tv = tp * getsymbolfield("TSE.TW","成交量");

if tp > tp[1] then begin
	utv = tv;
	dtv = 0;
end else begin
	utv = 0;
	dtv = tv;
end;

pmf = Average(utv, MinList(CurrentBar, 6));
nmf = Average(dtv, MinList(CurrentBar, 6));

if CurrentBar < 6 or (pmf + nmf) = 0 then
	mfivalue = 50
else 
	mfivalue = 100 * pmf /(pmf + nmf);

if mfivalue > 50 then
	tsemfi = 1
else
	tsemfi = 0;
```

---


---

## 腳本檔案: 函數/趨勢分析/UpShadow.xs

```xs
{@type:function}
//上影線佔實體比例
SetBarMode(1);

if range = 0 then
	upshadow = 0
else 
	upshadow = (high - maxlist(open,close)) / range;
```

---


---

## 腳本檔案: 函數/趨勢分析/UpTrend.xs

```xs
{@type:function_bool}
{
	判斷某個序列是否趨勢朝上
	
	注意事項:
	
	- 判斷N日趨勢會判斷均線的趨勢, 所以資料必須要有Length*2以上
	- 每次計算時會讀取近Length*2筆計算, 為了效能起見, 僅需在最新筆呼叫此函數即可

	範例:
	
	SetBackBar(2 * Length);			// 需有2倍的資料筆數	
	SetTotalBar(2);					// 
	if CurrentBar <> GetTotalBar() then return;
	ret = UpTrend(Close, Length);	
}

input: TheSeries(numericseries, "序列");
input: Length(numericsimple, "天期");

{
	底下是目前選股系統腳本使用的計算邏輯

	Condition1 = rateofchange(TheSeries, Length) >= Length; 
	Condition2 = TheSeries > TheSeries[Length/2]; 
	Condition3 = TheSeries > average(TheSeries, Length); 
	Condition4 = TheSeries >= TheSeries[1];

	retval = condition1 and condition2 and condition3 and condition4; 	
}

Array: TheSeriesArray[](0);
Array: LongMA[](0);			// 儲存長MA (MA(Length))
Array: ShortMA[](0);		// 儲存短MA (MA(Length/2))

ArraySeries(TheSeries, Length, TheSeriesArray);

// Value1 = Average(TheSeries, Length);
// Value2 = Average(TheSeries, Length/2);

Var: ShortLength(Ceiling(Length/2));
ArrayMASeries(TheSeries, Length, LongMA);
ArrayMASeries(TheSeries, ShortLength, ShortMA);

if Length >= 10 then begin
	retval = 
		ShortMA[1] >= LongMA[1] and // Value2 >= Value1 and
		ArrayLinearRegSlope(LongMA, Length) > 0 and //LinearRegSlope(Value1, Length) > 0 and 
		ArrayLinearRegSlope(ShortMA, ShortLength) > 0 and //LinearRegSlope(Value2, Length/2) > 0 and
		LongMA[1] >= LongMA[2] and // Value1 >= Value1[1] and
		ShortMA[1] >= ShortMA[2] and // Value2 >= Value2[1] and
		TheSeriesArray[1] >= TheSeriesArray[2]; // TheSeries >= TheSeries[1];
end else begin
	retval = 
		ArrayLinearRegSlope(LongMA, Length) > 0 and //LinearRegSlope(Value1, Length) > 0 and 
		LongMA[1] >= LongMA[2] and // Value1 >= Value1[1] and
		TheSeriesArray[1] >= TheSeriesArray[2]; // TheSeries >= TheSeries[1];
end;
```

---


---

## 腳本檔案: 函數/跨頻率/xf_CrossOver.xs

```xs
{@type:function_bool}
SetBarMode(1);

// 傳入兩個序列(跟目前的頻率不同), 判斷是否crossover
//
// FreqType是傳入序列的資料期別, 支援"D", "W", "M"
// SeriesA, SeriesB是傳入的序列
//
input:
	FreqType(string), 
	SeriesA(numericseries),
	SeriesB(numericseries);
 
variable:
	valA(0), valB(0), posA(0), posB(0);
 
posA = 0;
posB = 0;
valA = xf_getvalue(FreqType, SeriesA, posA);
valB = xf_getvalue(FreqType, SeriesB, posB);
if valA <= valB then
begin
	xf_CrossOver = false;
	return;
end; 

variable: idx(0);
for idx = 1 to 6
begin
	posA = posA + 1;
	posB = posB + 1;
	valA = xf_getvalue(FreqType, SeriesA, posA);
	valB = xf_getvalue(FreqType, SeriesB, posB);
	if valA < valB then
	begin
		xf_CrossOver = true;
		return;
	end
	else
	begin
		if valA > valB then
		begin
			xf_CrossOver = false;
			return;
		end;
	end; 
end;
xf_CrossOver = false;
```

---


---

## 腳本檔案: 函數/跨頻率/xf_CrossUnder.xs

```xs
{@type:function_bool}
SetBarMode(1);

// 傳入兩個序列(跟目前的頻率不同), 判斷是否crossunder
//
// FreqType是傳入序列的資料期別, 支援"D", "W", "M"
// SeriesA, SeriesB是傳入的序列
//
input:
	FreqType(string), 
	SeriesA(numericseries),
	SeriesB(numericseries);
 
variable:
	valA(0), valB(0), posA(0), posB(0);
 
posA = 0;
posB = 0;
valA = xf_getvalue(FreqType, SeriesA, posA);
valB = xf_getvalue(FreqType, SeriesB, posB);

if valA >= valB then
begin
	xf_CrossUnder = false;
	return;
end; 

variable: idx(0);
for idx = 1 to 6
begin
	posA = posA + 1;
	posB = posB + 1;
	valA = xf_getvalue(FreqType, SeriesA, posA);
	valB = xf_getvalue(FreqType, SeriesB, posB);
	if valA > valB then
	begin
		xf_CrossUnder = true;
		return;
	end
	else
	begin
		if valA < valB then
		begin
			xf_CrossUnder = false;
			return;
		end;
	end; 
end;
xf_CrossUnder = false;
```

---


---

## 腳本檔案: 函數/跨頻率/xf_DirectionMovement.xs

```xs
{@type:function}
SetBarMode(2);

// 跨頻率DirectionMovement function (for DMI相關指標)
//
// FreqType是預期要比對的期別, 支援"D", "W", "M"
// 輸入: FreqType, Length
// Return: pdi_value(+di), ndi_value(-di), adx_value(adx)
//
input: 
	FreqType(string),		//引用頻率
	length(numericsimple),	//計算期間
	pdi_value(numericref),	//回傳+DI
	ndi_value(numericref),	//回傳-DI
	adx_value(numericref);	//回傳ADX
	
variable:
	padm(0), nadm(0), radx(0),
	LastPAdm(0), LastNAdm(0), LastRAdx(0), LastATR(0),
	atr(0), pdm(0), ndm(0), tr(0),
	dValue0(0), dValue1(0), dx(0),
	changeHigh(0),changeLow(0),closePeriod(0),
	idx(0);

//跨頻率會用到的前期值需要手動記錄
condition1 = xf_getdtvalue(FreqType, getFieldDate("Date")) <> xf_getdtvalue(FreqType, getFieldDate("Date")[1]);
if condition1 then
begin
	LastPAdm = padm[1];
	LastNAdm = nadm[1];
	LastRAdx = radx[1];
	LastATR = atr[1];
end;

//取得跨頻率會用到的變數值
switch (FreqType)
begin
	case "D":
		if GetField("Close", "D")[1] > GetField("High", "D") then
			tr = GetField("Close", "D")[1] - GetField("Low", "D")
		else if GetField("Close", "D")[1] < GetField("Low", "D") then
			tr = GetField("High", "D") - GetField("Close", "D")[1]
		else
			tr = GetField("High", "D") - GetField("Low", "D");
		changeHigh = GetField("High", "D") - GetField("High", "D")[1];
		changeLow = GetField("Low", "D")[1] - GetField("Low", "D");
		closePeriod = GetField("Close", "D");

	case "W":
		if GetField("Close", "W")[1] > GetField("High", "W") then
			tr = GetField("Close", "W")[1] - GetField("Low", "W")
		else if GetField("Close", "W")[1] < GetField("Low", "W") then
			tr = GetField("High", "W") - GetField("Close", "W")[1]
		else
			tr = GetField("High", "W") - GetField("Low", "W");
		changeHigh = GetField("High", "W") - GetField("High", "W")[1];
		changeLow = GetField("Low", "W")[1] - GetField("Low", "W");
		closePeriod = GetField("Close", "W");

	case "M":
		if GetField("Close", "M")[1] > GetField("High", "M") then
			tr = GetField("Close", "M")[1] - GetField("Low", "M")
		else if GetField("Close", "M")[1] < GetField("Low", "M") then
			tr = GetField("High", "M") - GetField("Close", "M")[1]
		else
			tr = GetField("High", "M") - GetField("Low", "M");
		changeHigh = GetField("High", "M") - GetField("High", "M")[1];
		changeLow = GetField("Low", "M")[1] - GetField("Low", "M");
		closePeriod = GetField("Close", "M");

	case "AD":
		if GetField("Close", "AD")[1] > GetField("High", "AD") then
			tr = GetField("Close", "AD")[1] - GetField("Low", "AD")
		else if GetField("Close", "AD")[1] < GetField("Low", "AD") then
			tr = GetField("High", "AD") - GetField("Close", "AD")[1]
		else
			tr = GetField("High", "AD") - GetField("Low", "AD");
		changeHigh = GetField("High", "AD") - GetField("High", "AD")[1];
		changeLow = GetField("Low", "AD")[1] - GetField("Low", "AD");
		closePeriod = GetField("Close", "AD");

	case "AW":
		if GetField("Close", "AW")[1] > GetField("High", "AW") then
			tr = GetField("Close", "AW")[1] - GetField("Low", "AW")
		else if GetField("Close", "AW")[1] < GetField("Low", "AW") then
			tr = GetField("High", "AW") - GetField("Close", "AW")[1]
		else
			tr = GetField("High", "AW") - GetField("Low", "AW");
		changeHigh = GetField("High", "AW") - GetField("High", "AW")[1];
		changeLow = GetField("Low", "AW")[1] - GetField("Low", "AW");
		closePeriod = GetField("Close", "AW");

	case "AM":
		if GetField("Close", "AM")[1] > GetField("High", "AM") then
			tr = GetField("Close", "AM")[1] - GetField("Low", "AM")
		else if GetField("Close", "AM")[1] < GetField("Low", "AM") then
			tr = GetField("High", "AM") - GetField("Close", "AM")[1]
		else
			tr = GetField("High", "AM") - GetField("Low", "AM");
		changeHigh = GetField("High", "AM") - GetField("High", "AM")[1];
		changeLow = GetField("Low", "AM")[1] - GetField("Low", "AM");
		closePeriod = GetField("Close", "AM");

	default:
		if Close[1] > High then
			tr = Close[1] - Low
		else if Close[1] < Low then
			tr = High - Close[1]
		else
			tr = High - Low;
		changeHigh = High - High[1];
		changeLow = Low[1] - Low;
		closePeriod = Close;
end;

//原始的技術指標計算
value1 = xf_GetCurrentBar(FreqType);

if value1 = 1 then
 begin
	padm = closePeriod / 10000;
	nadm = padm;
	atr = padm * 5;
	radx = 20;
 end
else
 begin
	pdm = maxlist(changeHigh, 0);
	ndm = maxlist(changeLow, 0);

	if pdm < ndm then
		pdm = 0
	else 
	  begin
		if pdm > ndm then
			ndm = 0
		else
		  begin
			pdm = 0;
			ndm = 0;
		  end;		
	  end;
	
	padm = LastPAdm + (pdm - LastPAdm) / length;
	nadm = LastNAdm + (ndm - LastNAdm) / length;
	atr = LastATR + (tr - LastATR) / length;
	
	if atr <> 0 then begin
		dValue0 = 100 * padm / atr;
		dValue1 = 100 * nadm / atr;
	end;
	
	if dValue0 + dValue1 <> 0 then
		dx = AbsValue(100 * (dValue0 - dValue1) / (dValue0 + dValue1));

	radx = LastRAdx + (dx - LastRAdx) / length;
 end;

pdi_value = dValue0;
ndi_value = dValue1;
adx_value = radx;
xf_directionmovement = 1;
```

---


---

## 腳本檔案: 函數/跨頻率/xf_EMA.xs

```xs
{@type:function}
SetBarMode(2);

// 跨頻率EMA
//
// FreqType是預期要比對的期別, 支援"D", "W", "M"
// 輸入: FreqType, Series, Length
//
input:
	FreqType(string),		//引用頻率
	Series(numericseries),	//價格序列
	Length(numericsimple);	//計算期間
 
variable:
	Factor(0), lastEMA(0);

 
condition1 = xf_getdtvalue(FreqType, getFieldDate("Date")) <> xf_getdtvalue(FreqType, getFieldDate("Date")[1]);
if condition1 then
	lastEMA = xf_EMA[1];

value1 = xf_GetCurrentBar(FreqType);

if Length + 1 = 0 then Factor = 1 else Factor = 2 / (Length + 1);

if value1 = 1 then
	xf_EMA = Series
else if value1 <= Length then
    xf_EMA = (Series + (lastEMA * (value1 - 1)))/value1	
else
	xf_EMA = lastEMA + Factor * (Series - lastEMA);
```

---


---

## 腳本檔案: 函數/跨頻率/xf_GetBoolean.xs

```xs
{@type:function_bool}
SetBarMode(1);

// 傳入一個序列(跟目前的頻率不同), 取得這個序列以此頻率的第幾筆
//
// FreqType是傳入序列的資料期別, 支援"D", "W", "M"
// TFSeries是傳入的布林序列
// poi是要取得的位置
// 
input:
	FreqType(string), 
	TFSeries(truefalseseries),
	poi(numeric);
 
variable: _pos(0);
  
_pos = poi; 
if _pos <= 0 then
	xf_GetBoolean = TFSeries[0]
else
begin
	variable: idx(0), dt(0), dt2(0);
	idx = 0;
	while _pos > 0 and idx < currentbar-1
	begin
		dt = xf_getdtvalue(FreqType, getFieldDate("Date")[idx]);
		dt2 = xf_getdtvalue(FreqType, getFieldDate("Date")[idx+1]);
		if dt <> dt2 then _pos = _pos - 1; 
		idx = idx + 1;
	end;
	xf_GetBoolean = TFSeries[idx];
end;
```

---


---

## 腳本檔案: 函數/跨頻率/xf_GetCurrentBar.xs

```xs
{@type:function}
SetBarMode(2);

// 取得指定頻率的K棒編號（CurrentBar）
//
// FreqType是預期要引用的頻率, 支援"D", "W", "M"
// 輸入: FreqType
//
input:
	FreqType(string);		//引用頻率

condition1 = xf_getdtvalue(FreqType, getFieldDate("Date")) <> xf_getdtvalue(FreqType, getFieldDate("Date")[1]);
if currentbar = 1 then 
	xf_GetCurrentBar = 1
else if condition1 then
	xf_GetCurrentBar = xf_GetCurrentBar[1] + 1
else
	xf_GetCurrentBar = xf_GetCurrentBar[1];
```

---


---

## 腳本檔案: 函數/跨頻率/xf_GetDTValue.xs

```xs
{@type:function}
SetBarMode(1);

// 回傳某個日期的'normalized' value
// 用這個value來比對是否已經跨期
//
// FreqType是預期要比對的期別, 支援"D", "W", "M"
// dtValue 是目前資料序列上面的Date
//
input:
	FreqType(string), 
	dtValue(numeric);
 
switch (FreqType)
begin
	case "D" , "AD":
		xf_GetDTValue = dtValue;
	  
	case "W" , "AW":
		// 年度 * 100 + 周別, e.g. 201001, 表示是2010年的第一週
		// 
		xf_GetDTValue = Year(dtValue) * 100 + WeekofYear(dtValue);
		
		// 每年的第一週需要判斷是否和去年的最後一週重疊
		// 
		if mod(dtValue, 10000) <= 104 and WeekofYear(DateAdd(dtValue,"D", 1-DayofWeek(dtValue))) = 53 then 
			xf_GetDTValue = round(dtValue / 10000 - 1, 0) * 100 + 53;
	 
	case "M" , "AM":
		// 年度 * 100 + 月別, e.g. 201001, 表示是2010年的第一個月
		//
		xf_GetDTValue = Year(dtValue) * 100 + Month(dtValue);
	 
	default:
		xf_GetDTValue = dtValue;
end;
```

---


---

## 腳本檔案: 函數/跨頻率/xf_GetValue.xs

```xs
{@type:function}
SetBarMode(1);

// 傳入一個序列(跟目前的頻率不同), 取得這個序列以此頻率的第幾筆
//
// FreqType是傳入序列的資料期別, 支援"D", "W", "M"
// PriceSeries是傳入的序列
// poi是要取得的位置
// 
input:
	FreqType(string), 
	PriceSeries(numericseries),
	poi(numeric);
 
variable: _pos(0);
  
_pos = poi; 
if _pos <= 0 then
	xf_GetValue = PriceSeries[0]
else
begin
	variable: idx(0), dt(0), dt2(0);
	idx = 0;
	while _pos > 0 and idx < currentbar-1
	begin
		dt = xf_getdtvalue(FreqType, getfieldDate("Date")[idx]);
		dt2 = xf_getdtvalue(FreqType, getfieldDate("Date")[idx+1]);
		if dt <> dt2 then _pos = _pos - 1; 
		idx = idx + 1;
	end;
	xf_GetValue = PriceSeries[idx];
end;
```

---


---

## 腳本檔案: 函數/跨頻率/xf_MACD.xs

```xs
{@type:function}
SetBarMode(1);

// 跨頻率MACD函數
//
// FreqType是預期要引用的頻率, 支援"D", "W", "M"
// 輸入: FreqType, FastLength, SlowLength, MACDLength;
// 輸出: DifValue, MACDValue, OscValue;

input:
	FreqType(string),		//引用頻率
	Price(numericseries), 	
	FastLength(numericsimple), SlowLength(numericsimple), MACDLength(numericsimple),
	DifValue(numericref), MACDValue(numericref), OscValue(numericref);

DifValue = xf_XAverage(FreqType, Price, FastLength) - xf_XAverage(FreqType, Price, SlowLength);
MACDValue = xf_XAverage(FreqType, DifValue, MACDLength);
OscValue = DifValue - MACDValue;

xf_MACD = 1;
```

---


---

## 腳本檔案: 函數/跨頻率/xf_PercentR.xs

```xs
{@type:function}
SetBarMode(1);

// 跨頻率PercentR函數(for 威廉指標)
//
// FreqType是預期要引用的頻率, 支援"D", "W", "M"
// 輸入: FreqType, SeriesH, SeriesL, SeriesC, Length, rsvt, kt
// 輸出: rsv_value, k_value, d_value
//
input:
	FreqType(string), 
	Length(numericsimple);
 
variable:
	maxHigh(0), minLow(0),variableA(0),variableB(0),closePeriod(0);

switch (upperstr(FreqType))
begin
	case "D":
		maxHigh = highest(GetField("High", "D"),Length);
		minLow = lowest(GetField("Low", "D"),Length);
		closePeriod = GetField("Close", "D");

	case "W":
		maxHigh = highest(GetField("High", "W"),Length);
		minLow = lowest(GetField("Low", "W"),Length);
		closePeriod = GetField("Close", "W");

	case "M":
		maxHigh = highest(GetField("High", "M"),Length);
		minLow = lowest(GetField("Low", "M"),Length);
		closePeriod = GetField("Close", "M");

	case "AD":
		maxHigh = highest(GetField("High", "AD"),Length);
		minLow = lowest(GetField("Low", "AD"),Length);
		closePeriod = GetField("Close", "AD");

	case "AW":
		maxHigh = highest(GetField("High", "AW"),Length);
		minLow = lowest(GetField("Low", "AW"),Length);
		closePeriod = GetField("Close", "AW");

	case "AM":
		maxHigh = highest(GetField("High", "AM"),Length);
		minLow = lowest(GetField("Low", "AM"),Length);
		closePeriod = GetField("Close", "AM");

	default:
		maxHigh = highest(High,Length);
		minLow = lowest(Low,Length);
		closePeriod = Close;
end;

variableB = maxHigh - minLow;

if variableB <> 0 then  
	xf_PercentR = 100 - ((maxHigh - closePeriod) / variableB) * 100
else 
	xf_PercentR = 0;
```

---


---

## 腳本檔案: 函數/跨頻率/xf_RSI.xs

```xs
{@type:function}
SetBarMode(2);

// 跨頻率RSI函數
//
// FreqType是預期要引用的頻率, 支援"D", "W", "M"
// 輸入: FreqType, Series, Length
//
input:
	FreqType(string),		//引用頻率
	Series(numericseries),	//價格序列
	Length(numericsimple);	//計算期間

variable: 
	SumUp(0), SumDown(0), 
	LastSumUp(0), LastSumDown(0),LastRefSeries(Series), 
	up(0), down(0),
	closePeriod(0);

condition1 = xf_getdtvalue(FreqType, getFieldDate("Date")) <> xf_getdtvalue(FreqType, getFieldDate("Date")[1]);
if condition1 then
begin
	LastSumUp = SumUp[1];
	LastSumDown = SumDown[1];
	LastRefSeries = Series[1];
end;

if xf_GetCurrentBar(FreqType) = 1 then
  begin
	SumUp = Average(maxlist(Series - LastRefSeries, 0), Length); 
	SumDown = Average(maxlist(LastRefSeries - Series, 0), Length); 
  end
else
  begin
	up = maxlist(Series - LastRefSeries, 0);
	down = maxlist(LastRefSeries - Series, 0);
	
	SumUp = LastSumUp + (up - LastSumUp) / Length;
	SumDown = LastSumDown + (down - LastSumDown) / Length;
  end;

if SumUp + SumDown = 0 then
	xf_RSI = 0
else
	xf_RSI = 100 * SumUp / (SumUp + SumDown);
```

---


---

## 腳本檔案: 函數/跨頻率/xf_Stochastic.xs

```xs
{@type:function}
SetBarMode(2);

// 跨頻率Stochastic函數(for KD/RSV相關指標)
//
// FreqType是預期要引用的頻率, 支援"D", "W", "M"
// 輸入: FreqType, SeriesH, SeriesL, SeriesC, Length, rsvt, kt
// 輸出: rsv_value, k_value, d_value
//
input:
	FreqType(string), 
	Length(numericsimple), rsvt(numericsimple), kt(numericsimple),
	rsv(numericref), k(numericref), d(numericref);
 
variable:
	maxHigh(0), minLow(0),lastK(50),lastD(50),closePeriod(0);
 
condition1 = xf_getdtvalue(FreqType, getFieldDate("Date")) <> xf_getdtvalue(FreqType, getFieldDate("Date")[1]);
if condition1 then
begin
	lastK = k[1];
	lastD = d[1];
end;

switch (FreqType)
begin
	case "D":
		maxHigh = highest(GetField("High", "D"),Length);
		minLow = lowest(GetField("Low", "D"),Length);
		closePeriod = GetField("Close", "D");

	case "W":
		maxHigh = highest(GetField("High", "W"),Length);
		minLow = lowest(GetField("Low", "W"),Length);
		closePeriod = GetField("Close", "W");

	case "M":
		maxHigh = highest(GetField("High", "M"),Length);
		minLow = lowest(GetField("Low", "M"),Length);
		closePeriod = GetField("Close", "M");

	case "AD":
		maxHigh = highest(GetField("High", "AD"),Length);
		minLow = lowest(GetField("Low", "AD"),Length);
		closePeriod = GetField("Close", "AD");

	case "AW":
		maxHigh = highest(GetField("High", "AW"),Length);
		minLow = lowest(GetField("Low", "AW"),Length);
		closePeriod = GetField("Close", "AW");

	case "AM":
		maxHigh = highest(GetField("High", "AM"),Length);
		minLow = lowest(GetField("Low", "AM"),Length);
		closePeriod = GetField("Close", "AM");

	default:
		maxHigh = highest(High,Length);
		minLow = lowest(Low,Length);
		closePeriod = Close;
end;

if maxHigh <> minLow then
	rsv = 100 * (closePeriod - minLow) / (maxHigh - minLow)
else
	rsv = 50;
 
if currentbar = 1 then
begin
	k = 50;
	d = 50;
end
else
begin
	k = (lastK * (rsvt - 1) + rsv) / rsvt;
	d = (lastD * (kt - 1) + k) / kt;
end; 
 
xf_Stochastic = 1;
```

---


---

## 腳本檔案: 函數/跨頻率/xf_WeightedClose.xs

```xs
{@type:function}
SetBarMode(1);

// 跨頻率WeightedClose函數
//
// FreqType是預期要引用的頻率, 支援"D", "W", "M"
//
input:
	FreqType(string);

switch (upperstr(FreqType))
begin
	case "D":
		xf_WeightedClose = (2 * GetField("Close", "D") + GetField("High", "D") + GetField("Low", "D")) / 4;

	case "W":
		xf_WeightedClose = (2 * GetField("Close", "W") + GetField("High", "W") + GetField("Low", "W")) / 4;

	case "M":
		xf_WeightedClose = (2 * GetField("Close", "M") + GetField("High", "M") + GetField("Low", "M")) / 4;

	case "AD":
		xf_WeightedClose = (2 * GetField("Close", "AD") + GetField("High", "AD") + GetField("Low", "AD")) / 4;

	case "AW":
		xf_WeightedClose = (2 * GetField("Close", "AW") + GetField("High", "AW") + GetField("Low", "AW")) / 4;

	case "AM":
		xf_WeightedClose = (2 * GetField("Close", "AM") + GetField("High", "AM") + GetField("Low", "AM")) / 4;

	default:
		xf_WeightedClose = (2 * Close + High + Low) / 4;
end;
```

---


---

## 腳本檔案: 函數/跨頻率/xf_XAverage.xs

```xs
{@type:function}
SetBarMode(2);

// 跨頻率XAverage
//
// FreqType是預期要比對的期別, 支援"D", "W", "M"
// 輸入: FreqType, Series, Length
//
input:
	FreqType(string),		//引用頻率
	Series(numericseries),	//價格序列
	Length(numericsimple);	//計算期間
 
variable:
	Factor(0), lastXAverage(0);

 
condition1 = xf_getdtvalue(FreqType, getFieldDate("Date")) <> xf_getdtvalue(FreqType, getFieldDate("Date")[1]);
if condition1 then
	lastXAverage = xf_XAverage[1];

value1 = xf_GetCurrentBar(FreqType);

if Length + 1 = 0 then Factor = 1 else Factor = 2 / (Length + 1);

if value1 = 1 then
	xf_XAverage = Series
else
	xf_XAverage = lastXAverage + Factor * (Series - lastXAverage);
```

---


---

## 腳本檔案: 函數/跨頻率/xfMin_CrossOver.xs

```xs
{@type:function_bool}
SetBarMode(1);

// 傳入兩個序列(跟目前的頻率不同), 判斷是否crossover
//
// FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
// SeriesA, SeriesB是傳入的序列
// 不支援XS選股、XS選股自訂排行與XS選股回測。
//
input:
	FreqType(string), 
	SeriesA(numericseries),
	SeriesB(numericseries);
 
variable:
	valA(0), valB(0), posA(0), posB(0);

if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");

posA = 0;
posB = 0;
valA = xfMin_getvalue(FreqType, SeriesA, posA);
valB = xfMin_getvalue(FreqType, SeriesB, posB);
if valA <= valB then
begin
	xfMin_CrossOver = false;
	return;
end; 

variable: idx(0);
for idx = 1 to 6
begin
	posA = posA + 1;
	posB = posB + 1;
	valA = xfMin_getvalue(FreqType, SeriesA, posA);
	valB = xfMin_getvalue(FreqType, SeriesB, posB);
	if valA < valB then
	begin
		xfMin_CrossOver = true;
		return;
	end
	else
	begin
		if valA > valB then
		begin
			xfMin_CrossOver = false;
			return;
		end;
	end; 
end;
xfMin_CrossOver = false;
```

---


---

## 腳本檔案: 函數/跨頻率/xfMin_CrossUnder.xs

```xs
{@type:function_bool}
SetBarMode(1);

// 傳入兩個序列(跟目前的頻率不同), 判斷是否crossunder
//
// FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
// SeriesA, SeriesB是傳入的序列
// 不支援XS選股、XS選股自訂排行與XS選股回測。
//
input:
	FreqType(string), 
	SeriesA(numericseries),
	SeriesB(numericseries);

variable:
	valA(0), valB(0), posA(0), posB(0);

if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");
 
posA = 0;
posB = 0;
valA = xfMin_getvalue(FreqType, SeriesA, posA);
valB = xfMin_getvalue(FreqType, SeriesB, posB);

if valA >= valB then
begin
	xfMin_CrossUnder = false;
	return;
end; 

variable: idx(0);
for idx = 1 to 6
begin
	posA = posA + 1;
	posB = posB + 1;
	valA = xfMin_getvalue(FreqType, SeriesA, posA);
	valB = xfMin_getvalue(FreqType, SeriesB, posB);
	if valA > valB then
	begin
		xfMin_CrossUnder = true;
		return;
	end
	else
	begin
		if valA < valB then
		begin
			xfMin_CrossUnder = false;
			return;
		end;
	end; 
end;
xfMin_CrossUnder = false;
```

---


---

## 腳本檔案: 函數/跨頻率/xfMin_DirectionMovement.xs

```xs
{@type:function}
SetBarMode(2);

// 跨頻率DirectionMovement function (for DMI相關指標)
//
// FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
// 輸入: FreqType, Length
// Return: pdi_value(+di), ndi_value(-di), adx_value(adx)
// 不支援XS選股、XS選股自訂排行與XS選股回測。
//
input: 
	FreqType(string),		//引用頻率
	length(numericsimple),	//計算期間
	pdi_value(numericref),	//回傳+DI
	ndi_value(numericref),	//回傳-DI
	adx_value(numericref);	//回傳ADX
	
variable:
	padm(0), nadm(0), radx(0),
	LastPAdm(0), LastNAdm(0), LastRAdx(0), LastATR(0),
	atr(0), pdm(0), ndm(0), tr(0),
	dValue0(0), dValue1(0), dx(0),
	changeHigh(0),changeLow(0),closePeriod(0),
	idx(0);

if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");

//跨頻率會用到的前期值需要手動記錄
if FreqType="D" or FreqType="AD" or FreqType="W" or FreqType="AW" or FreqType="M" or FreqType="AM" then 
	condition1 = xfMin_getdtvalue(FreqType, GetFielddate("Date")) <> xfMin_getdtvalue(FreqType, GetFielddate("Date")[1])
else 
	condition1 = xfMin_getdtvalue(FreqType, datetime) <> xfMin_getdtvalue(FreqType, datetime[1]);
if condition1 then
begin
	LastPAdm = padm[1];
	LastNAdm = nadm[1];
	LastRAdx = radx[1];
	LastATR = atr[1];
end;

//取得跨頻率會用到的變數值
switch (FreqType)
begin
	case  "1":
		if GetField("Close", "1")[1] > GetField("High", "1") then
			tr = GetField("Close", "1")[1] - GetField("Low", "1")
		else if GetField("Close", "1")[1] < GetField("Low", "1") then
			tr = GetField("High", "1") - GetField("Close", "1")[1]
		else
			tr = GetField("High", "1") - GetField("Low", "1");
		changeHigh = GetField("High", "1") - GetField("High", "1")[1];
		changeLow = GetField("Low", "1")[1] - GetField("Low", "1");
		closePeriod = GetField("Close", "1");
	
	case  "2":
		if GetField("Close", "2")[1] > GetField("High", "2") then
			tr = GetField("Close", "2")[1] - GetField("Low", "2")
		else if GetField("Close", "2")[1] < GetField("Low", "2") then
			tr = GetField("High", "2") - GetField("Close", "2")[1]
		else
			tr = GetField("High", "2") - GetField("Low", "2");
		changeHigh = GetField("High", "2") - GetField("High", "2")[1];
		changeLow = GetField("Low", "2")[1] - GetField("Low", "2");
		closePeriod = GetField("Close", "2");
	
	case  "3":
		if GetField("Close", "3")[1] > GetField("High", "3") then
			tr = GetField("Close", "3")[1] - GetField("Low", "3")
		else if GetField("Close", "3")[1] < GetField("Low", "3") then
			tr = GetField("High", "3") - GetField("Close", "3")[1]
		else
			tr = GetField("High", "3") - GetField("Low", "3");
		changeHigh = GetField("High", "3") - GetField("High", "3")[1];
		changeLow = GetField("Low", "3")[1] - GetField("Low", "3");
		closePeriod = GetField("Close", "3");

	case  "5":
		if GetField("Close", "5")[1] > GetField("High", "5") then
			tr = GetField("Close", "5")[1] - GetField("Low", "5")
		else if GetField("Close", "5")[1] < GetField("Low", "5") then
			tr = GetField("High", "5") - GetField("Close", "5")[1]
		else
			tr = GetField("High", "5") - GetField("Low", "5");
		changeHigh = GetField("High", "5") - GetField("High", "5")[1];
		changeLow = GetField("Low", "5")[1] - GetField("Low", "5");
		closePeriod = GetField("Close", "5");

	case "10":
		if GetField("Close", "10")[1] > GetField("High", "10") then
			tr = GetField("Close", "10")[1] - GetField("Low", "10")
		else if GetField("Close", "10")[1] < GetField("Low", "10") then
			tr = GetField("High", "10") - GetField("Close", "10")[1]
		else
			tr = GetField("High", "10") - GetField("Low", "10");
		changeHigh = GetField("High", "10") - GetField("High", "10")[1];
		changeLow = GetField("Low", "10")[1] - GetField("Low", "10");
		closePeriod = GetField("Close", "10");

	case "15":
		if GetField("Close", "15")[1] > GetField("High", "15") then
			tr = GetField("Close", "15")[1] - GetField("Low", "15")
		else if GetField("Close", "15")[1] < GetField("Low", "15") then
			tr = GetField("High", "15") - GetField("Close", "15")[1]
		else
			tr = GetField("High", "15") - GetField("Low", "15");
		changeHigh = GetField("High", "15") - GetField("High", "15")[1];
		changeLow = GetField("Low", "15")[1] - GetField("Low", "15");
		closePeriod = GetField("Close", "15");
		
	case "30":
		if GetField("Close", "30")[1] > GetField("High", "30") then
			tr = GetField("Close", "30")[1] - GetField("Low", "30")
		else if GetField("Close", "30")[1] < GetField("Low", "30") then
			tr = GetField("High", "30") - GetField("Close", "30")[1]
		else
			tr = GetField("High", "30") - GetField("Low", "30");
		changeHigh = GetField("High", "30") - GetField("High", "30")[1];
		changeLow = GetField("Low", "30")[1] - GetField("Low", "30");
		closePeriod = GetField("Close", "30");

	case "60":
		if GetField("Close", "60")[1] > GetField("High", "60") then
			tr = GetField("Close", "60")[1] - GetField("Low", "60")
		else if GetField("Close", "60")[1] < GetField("Low", "60") then
			tr = GetField("High", "60") - GetField("Close", "60")[1]
		else
			tr = GetField("High", "60") - GetField("Low", "60");
		changeHigh = GetField("High", "60") - GetField("High", "60")[1];
		changeLow = GetField("Low", "60")[1] - GetField("Low", "60");
		closePeriod = GetField("Close", "60");

	case "D":
		if GetField("Close", "D")[1] > GetField("High", "D") then
			tr = GetField("Close", "D")[1] - GetField("Low", "D")
		else if GetField("Close", "D")[1] < GetField("Low", "D") then
			tr = GetField("High", "D") - GetField("Close", "D")[1]
		else
			tr = GetField("High", "D") - GetField("Low", "D");
		changeHigh = GetField("High", "D") - GetField("High", "D")[1];
		changeLow = GetField("Low", "D")[1] - GetField("Low", "D");
		closePeriod = GetField("Close", "D");

	case "W":
		if GetField("Close", "W")[1] > GetField("High", "W") then
			tr = GetField("Close", "W")[1] - GetField("Low", "W")
		else if GetField("Close", "W")[1] < GetField("Low", "W") then
			tr = GetField("High", "W") - GetField("Close", "W")[1]
		else
			tr = GetField("High", "W") - GetField("Low", "W");
		changeHigh = GetField("High", "W") - GetField("High", "W")[1];
		changeLow = GetField("Low", "W")[1] - GetField("Low", "W");
		closePeriod = GetField("Close", "W");

	case "M":
		if GetField("Close", "M")[1] > GetField("High", "M") then
			tr = GetField("Close", "M")[1] - GetField("Low", "M")
		else if GetField("Close", "M")[1] < GetField("Low", "M") then
			tr = GetField("High", "M") - GetField("Close", "M")[1]
		else
			tr = GetField("High", "M") - GetField("Low", "M");
		changeHigh = GetField("High", "M") - GetField("High", "M")[1];
		changeLow = GetField("Low", "M")[1] - GetField("Low", "M");
		closePeriod = GetField("Close", "M");

	case "AD":
		if GetField("Close", "AD")[1] > GetField("High", "AD") then
			tr = GetField("Close", "AD")[1] - GetField("Low", "AD")
		else if GetField("Close", "AD")[1] < GetField("Low", "AD") then
			tr = GetField("High", "AD") - GetField("Close", "AD")[1]
		else
			tr = GetField("High", "AD") - GetField("Low", "AD");
		changeHigh = GetField("High", "AD") - GetField("High", "AD")[1];
		changeLow = GetField("Low", "AD")[1] - GetField("Low", "AD");
		closePeriod = GetField("Close", "AD");

	case "AW":
		if GetField("Close", "AW")[1] > GetField("High", "AW") then
			tr = GetField("Close", "AW")[1] - GetField("Low", "AW")
		else if GetField("Close", "AW")[1] < GetField("Low", "AW") then
			tr = GetField("High", "AW") - GetField("Close", "AW")[1]
		else
			tr = GetField("High", "AW") - GetField("Low", "AW");
		changeHigh = GetField("High", "AW") - GetField("High", "AW")[1];
		changeLow = GetField("Low", "AW")[1] - GetField("Low", "AW");
		closePeriod = GetField("Close", "AW");

	case "AM":
		if GetField("Close", "AM")[1] > GetField("High", "AM") then
			tr = GetField("Close", "AM")[1] - GetField("Low", "AM")
		else if GetField("Close", "AM")[1] < GetField("Low", "AM") then
			tr = GetField("High", "AM") - GetField("Close", "AM")[1]
		else
			tr = GetField("High", "AM") - GetField("Low", "AM");
		changeHigh = GetField("High", "AM") - GetField("High", "AM")[1];
		changeLow = GetField("Low", "AM")[1] - GetField("Low", "AM");
		closePeriod = GetField("Close", "AM");

	default:
		if Close[1] > High then
			tr = Close[1] - Low
		else if Close[1] < Low then
			tr = High - Close[1]
		else
			tr = High - Low;
		changeHigh = High - High[1];
		changeLow = Low[1] - Low;
		closePeriod = Close;
end;

//原始的技術指標計算
value1 = xfMin_GetCurrentBar(FreqType);

if value1 = 1 then
 begin
	padm = closePeriod / 10000;
	nadm = padm;
	atr = padm * 5;
	radx = 20;
 end
else
 begin
	pdm = maxlist(changeHigh, 0);
	ndm = maxlist(changeLow, 0);

	if pdm < ndm then
		pdm = 0
	else 
	  begin
		if pdm > ndm then
			ndm = 0
		else
		  begin
			pdm = 0;
			ndm = 0;
		  end;		
	  end;
	
	padm = LastPAdm + (pdm - LastPAdm) / length;
	nadm = LastNAdm + (ndm - LastNAdm) / length;
	atr = LastATR + (tr - LastATR) / length;
	
	if atr <> 0 then begin
		dValue0 = 100 * padm / atr;
		dValue1 = 100 * nadm / atr;
	end;
	
	if dValue0 + dValue1 <> 0 then
		dx = AbsValue(100 * (dValue0 - dValue1) / (dValue0 + dValue1));

	radx = LastRAdx + (dx - LastRAdx) / length;
 end;

pdi_value = dValue0;
ndi_value = dValue1;
adx_value = radx;
xfMin_directionmovement = 1;
```

---


---

## 腳本檔案: 函數/跨頻率/xfMin_EMA.xs

```xs
{@type:function}
SetBarMode(2);

// 跨頻率EMA
//
// FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
// 輸入: FreqType, Series, Length
// 不支援XS選股、XS選股自訂排行與XS選股回測。
//
input:
	FreqType(string),		//引用頻率
	Series(numericseries),	//價格序列
	Length(numericsimple);	//計算期間
 
variable:
	Factor(0), lastEMA(0);

if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");

if FreqType="D" or FreqType="AD" or FreqType="W" or FreqType="AW" or FreqType="M" or FreqType="AM" then 
	condition1 = xfMin_getdtvalue(FreqType, getfieldDate("Date")) <> xfMin_getdtvalue(FreqType, getfieldDate("Date")[1])
else 
	condition1 = xfMin_getdtvalue(FreqType, datetime) <> xfMin_getdtvalue(FreqType, datetime[1]);
if condition1 then
	lastEMA = xfMin_EMA[1];

value1 = xfMin_GetCurrentBar(FreqType);

if Length + 1 = 0 then Factor = 1 else Factor = 2 / (Length + 1);

if value1 = 1 then
	xfMin_EMA = Series
else if value1 <= Length then
    xfMin_EMA = (Series + (lastEMA * (value1 - 1)))/value1	
else
	xfMin_EMA = lastEMA + Factor * (Series - lastEMA);
```

---


---

## 腳本檔案: 函數/跨頻率/xfMin_GetBoolean.xs

```xs
{@type:function_bool}
SetBarMode(1);

// 傳入一個序列(跟目前的頻率不同), 取得這個序列以此頻率的第幾筆
//
// FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
// TFSeries是傳入的布林序列
// poi是要取得的位置
// 不支援XS選股、XS選股自訂排行與XS選股回測。
// 
input:
	FreqType(string), 
	TFSeries(truefalseseries),
	poi(numeric);
 
variable: _pos(0);

if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");

_pos = poi; 
if _pos <= 0 then
	xfMin_GetBoolean = TFSeries[0]
else
begin
	variable: idx(0), dt(0), dt2(0);
	idx = 0;
	while _pos > 0 and idx < currentbar-1
	begin
		switch (FreqType)
		begin
			case "1","2","3","5","10","15","30","60":
				dt = xfMin_getdtvalue(FreqType, datetime[idx]);
				dt2 = xfMin_getdtvalue(FreqType, datetime[idx+1]);
				if dt <> dt2 then _pos = _pos - 1; 
				idx = idx + 1;			  		 
			default:
				dt = xfMin_getdtvalue(FreqType, getfieldDate("Date")[idx]);
				dt2 = xfMin_getdtvalue(FreqType, getfieldDate("Date")[idx+1]);
				if dt <> dt2 then _pos = _pos - 1; 
				idx = idx + 1;
		end;
	end;
	xfMin_GetBoolean = TFSeries[idx];
end;
```

---


---

## 腳本檔案: 函數/跨頻率/xfMin_GetCurrentBar.xs

```xs
{@type:function}
SetBarMode(2);

// 取得指定頻率的K棒編號（CurrentBar）
//
// FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
// 輸入: FreqType
// 不支援XS選股、XS選股自訂排行與XS選股回測。
//
input:
	FreqType(string);		//引用頻率

if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");

if FreqType="D" or FreqType="AD" or FreqType="W" or FreqType="AW" or FreqType="M" or FreqType="AM" then 
	condition1 = xfMin_getdtvalue(FreqType, getfieldDate("Date")) <> xfMin_getdtvalue(FreqType, getfieldDate("Date")[1])
else 
	condition1 = xfMin_getdtvalue(FreqType, datetime) <> xfMin_getdtvalue(FreqType, datetime[1]);	
if currentbar = 1 then 
	xfMin_GetCurrentBar = 1
else if condition1 then
	xfMin_GetCurrentBar = xfMin_GetCurrentBar[1] + 1
else
	xfMin_GetCurrentBar = xfMin_GetCurrentBar[1];
```

---


---

## 腳本檔案: 函數/跨頻率/xfMin_GetDTValue.xs

```xs
{@type:function}
SetBarMode(1);

// 回傳某個日期的'normalized' value
// 用這個value來比對是否已經跨期
//
// FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
// dtValue 是目前資料序列上面的Date
// 不支援XS選股、XS選股自訂排行與XS選股回測。
//
input:
	FreqType(string), 
	dtValue(numeric);

if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");

switch (FreqType)
begin
	case "1","2","3","5","10","15","30","60":
		// 回傳分鐘線的日期時間YYYYMMDDhhmmss。例如：2018/9/10 12:03:59的五分線會回傳20180910120000
		if symbolExchange="TF" then begin
			if dtValue < 19870106000000 then begin
				xfMin_GetDTValue = dtValue;
				return;
			end;
			value1 = strtonum(FreqType);
			value2 = strtonum(rightstr(numtostr(dtValue,0),6));
			if value2>=084500 and value2<150000 then value20=084500
			else if value2 >=150000 then value20=150000
			else value20=000000;
			value21= timediff(value2,value20,"M");
			value3 = IntPortion(value21 / value1) * value1;
			value31= timeadd(value20,"M",value3);
			xfMin_GetDTValue = dtValue - value2 + value31;
		end 
		else begin
			if dtValue < 19870106000000 then begin
				xfMin_GetDTValue = dtValue;
				return;
			end;
			value1 = strtonum(FreqType);
			value2 = strtonum(rightstr(numtostr(dtValue,0),6));
			value3 = IntPortion(minute(value2) / value1) * value1;
			xfMin_GetDTValue = dtValue - value2 + EncodeTime(hour(value2), value3, 0);	
		end;
		
	case "D" , "AD":
		// 回傳YYYYMMDD
		xfMin_GetDTValue = dtValue;
	  
	case "W" , "AW":
		// 年度 * 100 + 周別, e.g. 201001, 表示是2010年的第一週
		xfMin_GetDTValue = Year(dtValue) * 100 + WeekofYear(dtValue);
		
		// 每年的第一週需要判斷是否和去年的最後一週重疊 
		if WeekofYear(DateAdd(dtValue,"D", 1-DayofWeek(dtValue))) = 53 then 
			xfMin_GetDTValue = Year(DateAdd(dtValue,"D", 1-DayofWeek(dtValue))) * 100 + WeekofYear(DateAdd(dtValue,"D", 1-DayofWeek(dtValue)));
	 
	case "M" , "AM":
		// 年度 * 100 + 月別, e.g. 201001, 表示是2010年的第一個月
		xfMin_GetDTValue = Year(dtValue) * 100 + Month(dtValue);
	 
	default:
		xfMin_GetDTValue = dtValue;
end;
```

---


---

## 腳本檔案: 函數/跨頻率/xfMin_GetValue.xs

```xs
{@type:function}
SetBarMode(1);

// 傳入一個序列(跟目前的頻率不同), 取得這個序列以此頻率的第幾筆
//
// FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
// PriceSeries是傳入的序列
// poi是要取得的位置
// 不支援XS選股、XS選股自訂排行與XS選股回測。
// 
input:
	FreqType(string), 
	PriceSeries(numericseries),
	poi(numeric);
 
variable: _pos(0);

if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");

_pos = poi; 
if _pos <= 0 then
	xfMin_GetValue = PriceSeries[0]
else
begin
	variable: idx(0), dt(0), dt2(0);
	idx = 0;
	while _pos > 0 and idx < currentbar-1
	begin
		switch (FreqType)
		begin
			case "1","2","3","5","10","15","30","60":
				dt = xfMin_getdtvalue(FreqType, datetime[idx]);
				dt2 = xfMin_getdtvalue(FreqType, datetime[idx+1]);
				if dt <> dt2 then _pos = _pos - 1; 
				idx = idx + 1;			  		 
			default:
				dt = xfMin_getdtvalue(FreqType, getfieldDate("Date")[idx]);
				dt2 = xfMin_getdtvalue(FreqType, getfieldDate("Date")[idx+1]);
				if dt <> dt2 then _pos = _pos - 1; 
				idx = idx + 1;
		end;
	end;
	xfMin_GetValue = PriceSeries[idx];
end;
```

---


---

## 腳本檔案: 函數/跨頻率/xfMin_MACD.xs

```xs
{@type:function}
SetBarMode(1);

// 跨頻率MACD函數
//
// FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
// 輸入: FreqType, FastLength, SlowLength, MACDLength;
// 輸出: DifValue, MACDValue, OscValue;
// 不支援XS選股、XS選股自訂排行與XS選股回測。

if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");

input:
	FreqType(string),		//引用頻率
	Price(numericseries), 	
	FastLength(numericsimple), SlowLength(numericsimple), MACDLength(numericsimple),
	DifValue(numericref), MACDValue(numericref), OscValue(numericref);

DifValue = xfMin_XAverage(FreqType, Price, FastLength) - xfMin_XAverage(FreqType, Price, SlowLength);
MACDValue = xfMin_XAverage(FreqType, DifValue, MACDLength);
OscValue = DifValue - MACDValue;

xfMin_macd = 1;
```

---


---

## 腳本檔案: 函數/跨頻率/xfmin_MTM.xs

```xs
{@type:function}
SetBarMode(1);

// 跨頻率MTM函數(for MTM指標)
//
// FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
// 輸入: FreqType, Series, Length
//
input:
	FreqType(string),		//引用頻率
	Length(numericsimple);	//計算期間
	
if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");
 
switch (FreqType)
begin
	case  "1":
		xfMin_MTM = GetField("收盤價", "1") - GetField("收盤價", "1")[length];

	case  "2":
		xfMin_MTM = GetField("收盤價", "2") - GetField("收盤價", "2")[length];
		
	case  "3":
		xfMin_MTM = GetField("收盤價", "3") - GetField("收盤價", "3")[length];
	
	case  "5":
		xfMin_MTM = GetField("收盤價", "5") - GetField("收盤價", "5")[length];
	
	case "10":
		xfMin_MTM = GetField("收盤價", "10") - GetField("收盤價", "10")[length];
	
	case "15":
		xfMin_MTM = GetField("收盤價", "15") - GetField("收盤價", "15")[length];
	
	case "30":
		xfMin_MTM = GetField("收盤價", "30") - GetField("收盤價", "30")[length];
	
	case "60":
		xfMin_MTM = GetField("收盤價", "60") - GetField("收盤價", "60")[length];

	case "D":
		xfMin_MTM = GetField("收盤價", "D") - GetField("收盤價", "D")[length];

	case "W":
		xfMin_MTM = GetField("收盤價", "W") - GetField("收盤價", "W")[length];

	case "M":
		xfMin_MTM = GetField("收盤價", "M") - GetField("收盤價", "M")[length];

	case "AD":
		xfMin_MTM = GetField("收盤價", "AD") - GetField("收盤價", "AD")[length];

	case "AW":
		xfMin_MTM = GetField("收盤價", "AW") - GetField("收盤價", "AW")[length];

	case "AM":
		xfMin_MTM = GetField("收盤價", "AM") - GetField("收盤價", "AM")[length];

	default:
		xfMin_MTM = close - close[length];
end;
```

---


---

## 腳本檔案: 函數/跨頻率/xfMin_PercentR.xs

```xs
{@type:function}
SetBarMode(1);

// 跨頻率PercentR函數(for 威廉指標)
//
// FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
// 輸入: FreqType, SeriesH, SeriesL, SeriesC, Length, rsvt, kt
// 輸出: rsv_value, k_value, d_value
// 不支援XS選股、XS選股自訂排行與XS選股回測。
//
input:
	FreqType(string), 
	Length(numericsimple);
 
variable:
	maxHigh(0), minLow(0),variableA(0),variableB(0),closePeriod(0);

if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");

switch (upperstr(FreqType))
begin
	case  "1":
		maxHigh = simplehighest(GetField("High", "1"),Length);
		minLow = simplelowest(GetField("Low", "1"),Length);
		closePeriod = GetField("Close", "1");	
		
	case  "2":
		maxHigh = simplehighest(GetField("High", "2"),Length);
		minLow = simplelowest(GetField("Low", "2"),Length);
		closePeriod = GetField("Close", "2");	
		
	case  "3":
		maxHigh = simplehighest(GetField("High", "3"),Length);
		minLow = simplelowest(GetField("Low", "3"),Length);
		closePeriod = GetField("Close", "3");	

	case  "5":
		maxHigh = simplehighest(GetField("High", "5"),Length);
		minLow = simplelowest(GetField("Low", "5"),Length);
		closePeriod = GetField("Close", "5");
		
	case "10":
		maxHigh = simplehighest(GetField("High", "10"),Length);
		minLow = simplelowest(GetField("Low", "10"),Length);
		closePeriod = GetField("Close", "10");
	
	case "15":
		maxHigh = simplehighest(GetField("High", "15"),Length);
		minLow = simplelowest(GetField("Low", "15"),Length);
		closePeriod = GetField("Close", "15");
	
	case "30":
		maxHigh = simplehighest(GetField("High", "30"),Length);
		minLow = simplelowest(GetField("Low", "30"),Length);
		closePeriod = GetField("Close", "30");
	
	case "60":
		maxHigh = simplehighest(GetField("High", "60"),Length);
		minLow = simplelowest(GetField("Low", "60"),Length);
		closePeriod = GetField("Close", "60");

	case "D":
		maxHigh = simplehighest(GetField("High", "D"),Length);
		minLow = simplelowest(GetField("Low", "D"),Length);
		closePeriod = GetField("Close", "D");

	case "W":
		maxHigh = simplehighest(GetField("High", "W"),Length);
		minLow = simplelowest(GetField("Low", "W"),Length);
		closePeriod = GetField("Close", "W");

	case "M":
		maxHigh = simplehighest(GetField("High", "M"),Length);
		minLow = simplelowest(GetField("Low", "M"),Length);
		closePeriod = GetField("Close", "M");

	case "AD":
		maxHigh = simplehighest(GetField("High", "AD"),Length);
		minLow = simplelowest(GetField("Low", "AD"),Length);
		closePeriod = GetField("Close", "AD");

	case "AW":
		maxHigh = simplehighest(GetField("High", "AW"),Length);
		minLow = simplelowest(GetField("Low", "AW"),Length);
		closePeriod = GetField("Close", "AW");

	case "AM":
		maxHigh = simplehighest(GetField("High", "AM"),Length);
		minLow = simplelowest(GetField("Low", "AM"),Length);
		closePeriod = GetField("Close", "AM");

	default:
		maxHigh = simplehighest(High,Length);
		minLow = simplelowest(Low,Length);
		closePeriod = Close;
end;

variableB = maxHigh - minLow;

if variableB <> 0 then  
	xfMin_PercentR = 100 - ((maxHigh - closePeriod) / variableB) * 100
else 
	xfMin_PercentR = 0;
```

---


---

## 腳本檔案: 函數/跨頻率/xfMin_RSI.xs

```xs
{@type:function}
SetBarMode(2);

// 跨頻率RSI函數
//
// FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
// 輸入: FreqType, Series, Length
// 不支援XS選股、XS選股自訂排行與XS選股回測。
//
input:
	FreqType(string),		//引用頻率
	Series(numericseries),	//價格序列
	Length(numericsimple);	//計算期間

variable: 
	SumUp(0), SumDown(0), 
	LastSumUp(0), LastSumDown(0),LastRefSeries(Series), 
	up(0), down(0),
	closePeriod(0);
	
if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");

if FreqType="D" or FreqType="AD" or FreqType="W" or FreqType="AW" or FreqType="M" or FreqType="AM" then 
	condition1 = xfMin_getdtvalue(FreqType, getfieldDate("Date")) <> xfMin_getdtvalue(FreqType, getfieldDate("Date")[1])
else 
	condition1 = xfMin_getdtvalue(FreqType, datetime) <> xfMin_getdtvalue(FreqType, datetime[1]);	
if condition1 then
begin
	LastSumUp = SumUp[1];
	LastSumDown = SumDown[1];
	LastRefSeries = Series[1];
end;

if xfMin_GetCurrentBar(FreqType) = 1 then
  begin
	SumUp = Average(maxlist(Series - LastRefSeries, 0), Length); 
	SumDown = Average(maxlist(LastRefSeries - Series, 0), Length); 
  end
else
  begin
	up = maxlist(Series - LastRefSeries, 0);
	down = maxlist(LastRefSeries - Series, 0);
	
	SumUp = LastSumUp + (up - LastSumUp) / Length;
	SumDown = LastSumDown + (down - LastSumDown) / Length;
  end;

if SumUp + SumDown = 0 then
	xfMin_RSI = 0
else
	xfMin_RSI = 100 * SumUp / (SumUp + SumDown);
```

---


---

## 腳本檔案: 函數/跨頻率/xfMin_Stochastic.xs

```xs
{@type:function}
SetBarMode(2);

// 跨頻率Stochastic函數(for KD/RSV相關指標)
//
// FreqType是預期要比對的期別, 支援 "1", "2", "3", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
// 輸入: FreqType, SeriesH, SeriesL, SeriesC, Length, rsvt, kt
// 輸出: rsv_value, k_value, d_value
// 不支援XS選股、XS選股自訂排行與XS選股回測。
//
input:
	FreqType(string), 
	Length(numericsimple), rsvt(numericsimple), kt(numericsimple),
	rsv(numericref), k(numericref), d(numericref);
 
variable:
	maxHigh(0), minLow(0),lastK(50),lastD(50),closePeriod(0);

if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");
 
if FreqType="D" or FreqType="AD" or FreqType="W" or FreqType="AW" or FreqType="M" or FreqType="AM" then 
	condition1 = xfMin_getdtvalue(FreqType, getfieldDate("Date")) <> xfMin_getdtvalue(FreqType, getfieldDate("Date")[1])
else 
	condition1 = xfMin_getdtvalue(FreqType, datetime) <> xfMin_getdtvalue(FreqType, datetime[1]);	
	
if condition1 then
begin
	lastK = k[1];
	lastD = d[1];
end;

switch (FreqType)
begin
	case  "1":
		maxHigh = simplehighest(GetField("High", "1"),Length);
		minLow = simplelowest(GetField("Low", "1"),Length);
		closePeriod = GetField("Close", "1");
		
	case  "2":
		maxHigh = simplehighest(GetField("High", "2"),Length);
		minLow = simplelowest(GetField("Low", "2"),Length);
		closePeriod = GetField("Close", "2");
	
	case  "3":
		maxHigh = simplehighest(GetField("High", "3"),Length);
		minLow = simplelowest(GetField("Low", "3"),Length);
		closePeriod = GetField("Close", "3");
	
	case  "5":
		maxHigh = simplehighest(GetField("High", "5"),Length);
		minLow = simplelowest(GetField("Low", "5"),Length);
		closePeriod = GetField("Close", "5");
		
	case "10":
		maxHigh = simplehighest(GetField("High", "10"),Length);
		minLow = simplelowest(GetField("Low", "10"),Length);
		closePeriod = GetField("Close", "10");
	
	case "15":
		maxHigh = simplehighest(GetField("High", "15"),Length);
		minLow = simplelowest(GetField("Low", "15"),Length);
		closePeriod = GetField("Close", "15");
	
	case "30":
		maxHigh = simplehighest(GetField("High", "30"),Length);
		minLow = simplelowest(GetField("Low", "30"),Length);
		closePeriod = GetField("Close", "30");
	
	case "60":
		maxHigh = simplehighest(GetField("High", "60"),Length);
		minLow = simplelowest(GetField("Low", "60"),Length);
		closePeriod = GetField("Close", "60");

	case "D":
		maxHigh = simplehighest(GetField("High", "D"),Length);
		minLow = simplelowest(GetField("Low", "D"),Length);
		closePeriod = GetField("Close", "D");

	case "W":
		maxHigh = simplehighest(GetField("High", "W"),Length);
		minLow = simplelowest(GetField("Low", "W"),Length);
		closePeriod = GetField("Close", "W");

	case "M":
		maxHigh = simplehighest(GetField("High", "M"),Length);
		minLow = simplelowest(GetField("Low", "M"),Length);
		closePeriod = GetField("Close", "M");

	case "AD":
		maxHigh = simplehighest(GetField("High", "AD"),Length);
		minLow = simplelowest(GetField("Low", "AD"),Length);
		closePeriod = GetField("Close", "AD");

	case "AW":
		maxHigh = simplehighest(GetField("High", "AW"),Length);
		minLow = simplelowest(GetField("Low", "AW"),Length);
		closePeriod = GetField("Close", "AW");

	case "AM":
		maxHigh = simplehighest(GetField("High", "AM"),Length);
		minLow = simplelowest(GetField("Low", "AM"),Length);
		closePeriod = GetField("Close", "AM");

	default:
		maxHigh = simplehighest(High,Length);
		minLow = simplelowest(Low,Length);
		closePeriod = Close;
end;

if maxHigh <> minLow then
	rsv = 100 * (closePeriod - minLow) / (maxHigh - minLow)
else
	rsv = 50;
 
if currentbar = 1 then
begin
	k = 50;
	d = 50;
end
else
begin
	k = (lastK * (rsvt - 1) + rsv) / rsvt;
	d = (lastD * (kt - 1) + k) / kt;
end; 
 
xfMin_Stochastic = 1;
```

---


---

## 腳本檔案: 函數/跨頻率/xfMin_WeightedClose.xs

```xs
{@type:function}
SetBarMode(1);

// 跨頻率WeightedClose函數
//
// FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
// 不支援XS選股、XS選股自訂排行與XS選股回測。
//
input:
	FreqType(string);

if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");

switch (UpperStr(FreqType))
begin
	case  "1":
		xfMin_WeightedClose = (2 * GetField("Close", "1") + GetField("High", "1") + GetField("Low", "1")) / 4;

	case  "2":
		xfMin_WeightedClose = (2 * GetField("Close", "2") + GetField("High", "2") + GetField("Low", "2")) / 4;
		
	case  "3":
		xfMin_WeightedClose = (2 * GetField("Close", "3") + GetField("High", "3") + GetField("Low", "3")) / 4;
		
	case  "5":
		xfMin_WeightedClose = (2 * GetField("Close", "5") + GetField("High", "5") + GetField("Low", "5")) / 4;	
	
	case "10":
		xfMin_WeightedClose = (2 * GetField("Close", "10") + GetField("High", "10") + GetField("Low", "10")) / 4;	
	
	case "15":
		xfMin_WeightedClose = (2 * GetField("Close", "15") + GetField("High", "15") + GetField("Low", "15")) / 4;	
	
	case "30":
		xfMin_WeightedClose = (2 * GetField("Close", "30") + GetField("High", "30") + GetField("Low", "30")) / 4;	
	
	case "60":
		xfMin_WeightedClose = (2 * GetField("Close", "60") + GetField("High", "60") + GetField("Low", "60")) / 4;

	case "D":
		xfMin_WeightedClose = (2 * GetField("Close", "D") + GetField("High", "D") + GetField("Low", "D")) / 4;

	case "W":
		xfMin_WeightedClose = (2 * GetField("Close", "W") + GetField("High", "W") + GetField("Low", "W")) / 4;

	case "M":
		xfMin_WeightedClose = (2 * GetField("Close", "M") + GetField("High", "M") + GetField("Low", "M")) / 4;

	case "AD":
		xfMin_WeightedClose = (2 * GetField("Close", "AD") + GetField("High", "AD") + GetField("Low", "AD")) / 4;

	case "AW":
		xfMin_WeightedClose = (2 * GetField("Close", "AW") + GetField("High", "AW") + GetField("Low", "AW")) / 4;

	case "AM":
		xfMin_WeightedClose = (2 * GetField("Close", "AM") + GetField("High", "AM") + GetField("Low", "AM")) / 4;

	default:
		xfMin_WeightedClose = (2 * Close + High + Low) / 4;
end;
```

---


---

## 腳本檔案: 函數/跨頻率/xfMin_XAverage.xs

```xs
{@type:function}
SetBarMode(2);

// 跨頻率XAverage
//
// FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
// 輸入: FreqType, Series, Length
// 不支援XS選股、XS選股自訂排行與XS選股回測。
//
input:
	FreqType(string),		//引用頻率
	Series(numericseries),	//價格序列
	Length(numericsimple);	//計算期間
 
variable:
	Factor(0), lastXAverage(0);

if getinfo("Instance")=3 and getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");

if FreqType="D" or FreqType="AD" or FreqType="W" or FreqType="AW" or FreqType="M" or FreqType="AM" then 
	condition1 = xfMin_getdtvalue(FreqType, getfieldDate("Date")) <> xfMin_getdtvalue(FreqType, getfieldDate("Date")[1])
else 
	condition1 = xfMin_getdtvalue(FreqType, datetime) <> xfMin_getdtvalue(FreqType, datetime[1]);

if condition1 then
	lastXAverage = xfMin_XAverage[1];

value1 = xfMin_GetCurrentBar(FreqType);

if Length + 1 = 0 then Factor = 1 else Factor = 2 / (Length + 1);

if value1 = 1 then
	xfMin_XAverage = Series
else
	xfMin_XAverage = lastXAverage + Factor * (Series - lastXAverage);
```

---


---

## 腳本檔案: 函數/邏輯判斷/AverageIF.xs

```xs
{@type:function}
SetBarMode(1);

input: TrueAndFalse(truefalseseries),
       thePrice(numericseries),
	   Length(numericsimple);

variable: variableA(0);
variable:Sum(0);
variableA = 0;
Sum = 0;
for Value1 = 0 to Length - 1
begin
    if TrueAndFalse[Value1] then 
	begin 
		variableA = variableA + 1;
		Sum = Sum + thePrice[Value1];		
	end;	
end;

if variableA > 0 then
  AverageIf = Sum/variableA
else 
  AverageIf = 0;
```

---


---

## 腳本檔案: 函數/邏輯判斷/CountIF.xs

```xs
{@type:function}
SetBarMode(1);

input:TrueAndFalse(truefalseseries),Length(numericsimple);

variable: variableA(0);

variableA = 0;

for Value1 = 0 to Length - 1
begin
	if TrueAndFalse[Value1] then 	
		variableA = variableA + 1;
end;

CountIf = variableA;
```

---


---

## 腳本檔案: 函數/邏輯判斷/CountIfARow.xs

```xs
{@type:function}
SetBarMode(1);

input:TrueAndFalse(truefalseseries),Length(numericsimple);

CountIfARow = truecount(TrueAndFalse,Length);
```

---


---

## 腳本檔案: 函數/邏輯判斷/CrossOver.xs

```xs
{@type:function_bool}
SetBarMode(1);

input:
	SeriesA(numericseries),
	SeriesB(numericseries);
 
variable:
	valA(0), valB(0), posA(0), posB(0), idx(0);

CrossOver  = false;
posA = 0;
posB = 0;
valA = SeriesA[posA];
valB = SeriesB[posB];

if valA <= valB then 
	CrossOver = false
else begin
	for idx = 1 to minlist(6, currentbar)
	begin
		posA = posA + 1;
		posB = posB + 1;
		valA = SeriesA[posA];
		valB = SeriesB[posB];
		if valA < valB then
		begin
			CrossOver = true;
			break;
		end
		else
		begin
			if valA > valB then
			begin
				CrossOver = false;
				break;
			end;
		end; 
	end;
end;
```

---


---

## 腳本檔案: 函數/邏輯判斷/CrossUnder.xs

```xs
{@type:function_bool}
SetBarMode(1);

input:
	SeriesA(numericseries),
	SeriesB(numericseries);
 
variable:
	valA(0), valB(0), posA(0), posB(0), idx(0);

CrossUnder  = false;
posA = 0;
posB = 0;
valA = SeriesA[posA];
valB = SeriesB[posB];

if valA >= valB then 
	CrossUnder = false
else begin
	for idx = 1 to minlist(6, currentbar)
	begin
		posA = posA + 1;
		posB = posB + 1;
		valA = SeriesA[posA];
		valB = SeriesB[posB];
		if valA > valB then
		begin
			CrossUnder = true;
			break;
		end
		else
		begin
			if valA < valB then
			begin
				CrossUnder = false;
				break;
			end;
		end; 
	end;
end;
```

---


---

## 腳本檔案: 函數/邏輯判斷/Filter.xs

```xs
{@type:function_bool}
SetBarMode(2);

input:  pX(TrueFalseSimple), pLength(NumericSimple);
variable: vCounter(0);

If pX Then begin
	If vCounter < pLength Then begin
			vCounter = vCounter + 1;
			Filter = False;
	end Else begin
			vCounter = 0;
			Filter = True;
	End;
end Else begin
	vCounter = vCounter + 1;
	Filter = False;
End;
```

---


---

## 腳本檔案: 函數/邏輯判斷/IFF.xs

```xs
{@type:function}
SetBarMode(1);

input: Logicoperator(truefalsesimple),
       TrueReturnV(numericsimple),
       FalseReturnV(numericsimple);

if Logicoperator then IFF = TrueReturnV
else IFF = FalseReturnV;
```

---


---

## 腳本檔案: 函數/邏輯判斷/IsXLOrder.xs

```xs
{@type:function_bool}
{
	判斷成交金額是否是特大單
	
	級距表請參考:
	
	https://www.xq.com.tw/%e5%8f%b0%e8%82%a1%e9%80%90%e7%ad%86%e5%8a%9f%e8%83%bd%e8%a1%8c%e6%83%85%e7%ab%af%e7%9b%b8%e9%97%9c%e7%95%b0%e5%8b%95/	
}


input: pv(numericsimple, "成交金額");

var: intraBarPersist _open_price(0);
var: intraBarPersist _threshold(0);
var: intraBarPersist _last_date(0);

if _last_date <> Date then begin
	_last_date = Date;
	_open_price = GetField("Open", "D");
	if _open_price < 30 then 
		_threshold = 800000
	else if _open_price < 50 then 
		_threshold = 1000000
	else if _open_price < 100 then 
		_threshold = 1200000
	else if _open_price < 200 then 
		_threshold = 2000000
	else if _open_price < 500 then 
		_threshold = 4000000
	else
		_threshold = 4000000;
end;

if pv > _threshold then retval = true else retval = false;
```

---


---

## 腳本檔案: 函數/邏輯判斷/IsXOrder.xs

```xs
{@type:function_bool}
{
	判斷成交金額是否是大單(大單+特大單)
	
	級距表請參考:
	
	https://www.xq.com.tw/%e5%8f%b0%e8%82%a1%e9%80%90%e7%ad%86%e5%8a%9f%e8%83%bd%e8%a1%8c%e6%83%85%e7%ab%af%e7%9b%b8%e9%97%9c%e7%95%b0%e5%8b%95/	
}


input: pv(numericsimple, "成交金額");

var: intraBarPersist _open_price(0);
var: intraBarPersist _threshold(0);
var: intraBarPersist _last_date(0);

if _last_date <> Date then begin
	_last_date = Date;
	_open_price = GetField("Open", "D");
	if _open_price < 30 then 
		_threshold = 400000
	else if _open_price < 50 then 
		_threshold = 500000
	else if _open_price < 100 then 
		_threshold = 700000
	else if _open_price < 200 then 
		_threshold = 1200000
	else if _open_price < 500 then 
		_threshold = 2000000
	else
		_threshold = 2500000;
end;

if pv > _threshold then retval = true else retval = false;
```

---


---

## 腳本檔案: 函數/邏輯判斷/SummationIF.xs

```xs
{@type:function}
SetBarMode(1);

input: TrueAndFalse(truefalseseries), thePrice(numericseries), Length(numericsimple);
variable: _Output(0);

_Output = 0;

for Value1 = 0 to Length - 1
begin
    if TrueAndFalse[Value1] then _Output = _Output + thePrice[Value1];
end;

SummationIf = _Output;
```

---


---

## 腳本檔案: 函數/邏輯判斷/TrueAll.xs

```xs
{@type:function_bool}
SetBarMode(1);

input:TrueAndFalse(truefalseseries), Length(numericsimple);

TrueAll = True;

for Value1 = 0 to Length - 1
begin
    if TrueAndFalse[Value1] = False then
    begin
        TrueAll = False;
        break;
    end;
end;
```

---


---

## 腳本檔案: 函數/邏輯判斷/TrueAny.xs

```xs
{@type:function_bool}
SetBarMode(1);

input:TrueAndFalse(truefalseseries), Length(numericsimple);

TrueAny = False;

for Value1 = 0 to Length - 1
begin
    if TrueAndFalse[Value1] then
    begin
        TrueAny = True;
        break;
    end;
end;
```

---


---

## 腳本檔案: 函數/邏輯判斷/TrueCount.xs

```xs
{@type:function}
SetBarMode(1);

input:TrueAndFalse(truefalseseries), Length(numericsimple);

value2 = 0;

for Value1 = 0 to Length - 1
begin
    if TrueAndFalse[Value1] = true then
        value2 = value2 +1
    else
     begin
        break;
     end;
end;
TrueCount = value2;
```

---


---

## 腳本檔案: 函數/量能相關/DiffBidAskVolumeLxL.xs

```xs
{@type:function}
{
	DiffBidAskVolumeLxL為近15分鐘大戶買賣超的函數，
	該函數運算出來的數值，與XS指標的「流動大戶買賣力」指標相同。
}

array:_ArrayLarge[15](0),_ArraySmall[15](0);
var:_Count(0);
if barfreq <> "Min" or barinterval <> 1 then 
	raiseruntimeerror("僅支援 1 分鐘頻率");
//初始化
if getfieldDate("Date") <> getfieldDate("Date")[1] then begin
	_Count = 0;
	Array_SetValRange(_ArrayLarge, 1, 15, 0);
	Array_SetValRange(_ArraySmall, 1, 15, 0);
	value3 = 0;
	value99 = 0;
end else begin
	_Count += 1;
end;
value99 = mod(_count,15) + 1;
_ArrayLarge[value99] = GetField("買進大單量", "1") + GetField("買進特大單量", "1");
_ArraySmall[value99] = GetField("賣出大單量", "1") + GetField("賣出特大單量", "1");
value1 = Array_Sum(_ArrayLarge, 1, 15);
value2 = Array_Sum(_ArraySmall, 1, 15);
DiffBidAskVolumeLxL = value1 - value2;
```

---


---

## 腳本檔案: 函數/量能相關/DiffBidAskVolumeXL.xs

```xs
{@type:function}
{
	DiffBidAskVolumeXL為近15分鐘特大單買賣超的函數。
	計算方式為「近15分鐘累計的買進特大單量－賣出特大單量」
}

array:_ArrayLarge[15](0),_ArraySmall[15](0);
var:_Count(0);
if barfreq <> "Min" or barinterval <> 1 then 
	raiseruntimeerror("僅支援 1 分鐘頻率");
//初始化
if getfieldDate("Date") <> getfieldDate("Date")[1] then begin
	_Count = 0;
	Array_SetValRange(_ArrayLarge, 1, 15, 0);
	Array_SetValRange(_ArraySmall, 1, 15, 0);
	value3 = 0;
	value99 = 0;
end else begin
	_Count += 1;
end;
value99 = mod(_count,15) + 1;
_ArrayLarge[value99] = GetField("買進特大單量", "1");
_ArraySmall[value99] = GetField("賣出特大單量", "1");
value1 = Array_Sum(_ArrayLarge, 1, 15);
value2 = Array_Sum(_ArraySmall, 1, 15);
DiffBidAskVolumeXL = value1 - value2;
```

---


---

## 腳本檔案: 函數/量能相關/DiffTradeVolumeAtAskBid.xs

```xs
{@type:function}
{
	DiffTradeVolumeAtAskBid為分時買賣力的函數，
	該函數運算出來的數值，與XS指標的「分時買賣力」指標相同。
}

value1 = GetField("外盤量");
value2 = GetField("內盤量");
DiffTradeVolumeAtAskBid = value1 - value2;
```

---


---

## 腳本檔案: 函數/量能相關/DiffUpDownVolume.xs

```xs
{@type:function}
{
	DiffUpDownVolume為分時漲跌成交量的函數，
	該函數運算出來的數值，與XS指標的「分時漲跌成交量」指標相同。
}

DiffUpDownVolume = GetField("上漲量") - GetField("下跌量");
```

---
