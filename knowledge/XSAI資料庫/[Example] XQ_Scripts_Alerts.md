# XQ 官方警示腳本範例庫

共 359 個警示腳本範例。

---

## 腳本檔案: 警示/!語法範例/1.基本語法.xs

```xs
{@type:sensor}
//基本語法共有以下幾個元素
//1.宣告參數
//2.宣告變數
//3.引用時間序列的回傳值﹙包括開高低收成交量等﹚
//4.運用函數
//5.條件判斷：例如使用cross over這樣的關係因子
//6.設定警示條件：if.. then ret=1;
//在這邊我們用一個警示來示範這幾個基本語法的使用方式。

//=================範例：平均漲跌幅變大========================================
//1.宣告參數：利用input宣告輸入的參數。
//宣告後的參數，可以直接在警示中進場數值的調整，而不需要調整腳本內容
input:shortlength(5),longlength(20);
//參數的名稱，可以用setinputname來指定中文的說明
//指定後再設定警示參數時，就可以直接看到中文，而非參數英文名稱
//我們在這邊故意只指定第一個參數的中文名，讓大家看看效果
setinputname(1,"短天期");

//2.宣告變數，利用variable
//這是宣告一個變數叫xi，其初始值為0
variable:xi(0);
variable:yi(0);

//3.引用時間序列的回傳值﹙包括開高低收成交量等﹚
//系統也提供value1~value99共99個不必宣告就可直接用的變數名稱
value1=close-close[1];//close[1]代表前一天收盤價

//4.運用函數
//透過absvalue這個函數取close-close[1]的絕對值
value2=absvalue(value1); 
//指定變數值的計算公式，計算漲跌幅
yi=value2/close; 
//透過average這個函數計算數列的平均值
value3=average(yi,longlength);//計算長期平均漲跌幅
value4=average(yi,shortlength);//計算短期平均漲跌幅

//5.條件判斷：例如使用cross over這樣的關係因子
//6.設定警示條件：if.. then ret=1;
//最後設定警示條件，當短期平均漲跌幅與長期平均漲跌幅黃金交叉時，觸發警示
if value4 crosses over value3
then ret=1;
```

---


---

## 腳本檔案: 警示/!語法範例/2.getfield.xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 警示/!語法範例/3.getquote.xs

```xs
{@type:sensor}
//第三個範例，我們示範如何利用盤中即時數據﹙委買、委賣、內盤量、外盤量等等﹚來製作警示
//使用者可以透過"getquote"來取得這些數據
//只要在編輯器上打getquote就可以直接挑選所提供的欄位

//=====================範例：外盤漲停=======================================

//4.運用函數
//利用getfield取得買進價、賣出價及漲停價
value1=GetQuote("Ask");//賣出價
value2=GetQuote("DailyUplimit");//漲停價
value3=GetQuote("Bid");//買進價
//可以用q_來取代GetQuote完成快速引用

//6.設定警示條件：if.. then ret=1;
//賣出價=漲停價  且買進價跟賣出價相差不超過0.5%
if value1=value2 and value1/value2<=1.005
then ret=1;
```

---


---

## 腳本檔案: 警示/!語法範例/4.if..then..else.xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 警示/!語法範例/5.if..begin..end..then.xs

```xs
{@type:sensor}
//當我們的條件需要多行敘述才能完成時，
//可以用begin..end來標示。

//=====================範例：累積漲幅達X%並且今日跳空開高超過Y%=======================================

//例如若要找出前N日漲幅超過X%且今天跳空開高超過Y%的股票

//1.宣告參數：利用input宣告輸入的參數。
input:N(3);//前N日
input:X(10);//前n日漲幅%
input:_Y(4);//缺口大小%

if open>high[1] then //跳空開高
//用begin來呈現if 之後要執行的不只一件的事情
begin
value1=(1-close[1]/close[N])*100;//計算前N天的漲幅 
value2=(open-high[1])/close*100;//計算跳空缺口的大小
end;
//最後用end來宣告if之後要執行程式的結束

//6.設定警示條件：if.. then ret=1;
if value1>=X and value2>=_Y
then ret=1;
```

---


---

## 腳本檔案: 警示/!語法範例/6.condition條件的交集.xs

```xs
{@type:sensor}
//就像value1~value99是系統內建變數，其回傳值是一個數值
//condition1~condition99是系統內建回傳true或false邏輯值的變數名稱
//於是我們在口語上的如果~而且~就通知我，這樣的語法很容易用這個方式來撰寫

//========範例：融資餘額前十天大減超過2000張且減幅超過兩成===================
//1.宣告參數：利用input宣告輸入的參數。
input: range1(2000);
input: percent(0.2);

condition1=false;//將condition1設成false狀態，一旦符合條件才轉成true

//4.運用函數
//利用getfield取得外資買賣超資料
value1=getfield("融資餘額張數")[1];
value2=getfield("融資餘額張數")[10];


if value2-value1>range1 and (value2-value1)/value2>percent//計算融資增減張數
then condition1=true;//融資餘額前十天大減超過2000張且減幅超過兩成

//6.設定警示條件：if.. then ret=1;
//多重條件交易才觸發警示
if condition1 and average(close,20)/close[1]>1.05 and q_ask>open//近20天跌幅超過5%且現在外盤超過開盤價
then ret=1;
```

---


---

## 腳本檔案: 警示/!語法範例/7.0date(日期)的用法.xs

```xs
{@type:sensor}
//系統用date來表示每根bar的日期，其回傳值為yyyymmdd，例如2013年3月20日為20130320

//=========================範例：大單買進========================

//1.宣告參數：利用input宣告輸入的參數。
input: atVolume(100); //最少要求的量
input: LaTime(10); //至少要有幾次

//2.宣告變數，利用variable
value1=GetField("內外盤","Tick");//內外盤標記  內盤為-1 外盤為1

variable: Xtime(0);//計數器
variable: intrabarpersist XDate(0);

//3.引用時間序列的回傳值﹙包括開高低收成交量等﹚
//日期函數應用
if Date > XDate then Xtime =0; //開盤那根要歸0次數
XDate = Date;

if q_tickvolume > atVolume and value1>0 then  Xtime=Xtime+1; //外盤且單量夠大就加1次

//6.設定警示條件：if.. then ret=1;
if Xtime > LaTime  then ret=1;
```

---


---

## 腳本檔案: 警示/!語法範例/7.1time(時間)的用法.xs

```xs
{@type:sensor}
//系統用time來代表時間，顯示格式為hhmmss

//===========範例：開盤前三根K線都是陽線======================

//3.引用時間序列的回傳值﹙包括開高低收成交量等﹚
//時間函數應用
if time=091500 //時間是九點十五分

and close>close[1]     and close>open      
and close[1]>close[2]  and close[1]>open[1]
and close[2]>close[3]  and close[2]>open[2]

then ret=1;
```

---


---

## 腳本檔案: 警示/!語法範例/8.0常用函數.xs

```xs
{@type:sensor}
//函數是用來協助語法快速運算的功能

//===========範例：均線糾結======================

//1.宣告參數：利用input宣告輸入的參數。
input:shortLen(5),midLen(10),longLen(20),percent(0.02);

//4.運用函數
//透過average這個函數計算數列的平均值
value1=average(close,shortLen);//短期移動平均
value2=average(close,midLen);//中期移動平均
value3=average(close,longLen);//長期移動平均
value4=value1-value2;
value5=value2-value3;
value6=value1-value3;

//6.設定警示條件：if.. then ret=1;
if absvalue(value4)/close<percent 
and absvalue(value5)/close<percent 
and absvalue(value6)/close<percent
and close crosses above maxlist(value1,value2,value3)
then ret=1;
```

---


---

## 腳本檔案: 警示/!語法範例/9.0for(迴圈)的用法.xs

```xs
{@type:sensor}
//迴圈是用來重複執行多次相同的敘述句

//==============================範例：開盤五分鐘創三次新高======================

variable: n(0);
variable: count(0);

if  Barinterval=1 and barfreq ="Min" then Begin  //適用於1分鐘線
//執行迴圈，檢查過去五分鐘高點過前高的次數
if time = 90500 then begin
	for n=1 to 5 begin//以下的陳述(到end;為止)，n=1執行一次，n=2執行一次，一直到n=5
		if high[n]>high[n-1]
		then count=count+1;
	end;
end;
//設定警示條件：if.. then ret=1;
if count>=3
then ret=1;
end;
```

---


---

## 腳本檔案: 警示/!語法範例/9.1switch...case.xs

```xs
{@type:sensor}
//透過switch..case的語法，可以在一個變數的數值不一樣時，往不同的流程進行
//例如要計算外資過去十天買超超過七天時，可以運用以下的語法來寫腳本 

//==============================範例：外資近日買超天數比例======================

//1.宣告參數：利用input宣告輸入的參數。
input:day(10);//過去幾天 
input:ratio(0.7);//外資買超的天數佔多少比例

//2.宣告變數，利用variable
value1=GetField("Fdifference");//外資買賣超
variable:count(0);
variable:xi(0);

for xi= 1 to day
begin
	//============================================
	switch(value1[xi])
	begin
		case >0:
			count=count+1;
		case <0:
			count=count;
		case 0:
			count=count;
	end;//所有case都表達完之後，最後必須加end;來表示各種數值選項已結束
	//============================================
end;

//6.設定警示條件：if.. then ret=1;
if day<>0 and count/day>=ratio
then ret=1;
```

---


---

## 腳本檔案: 警示/!語法範例/9.2while(一直算到條件不符合).xs

```xs
{@type:sensor}
//還有另一種迴圈是while，會一直執行到條件不符合
//請小心不要造成無法跳出的無窮迴圈

//==============================範例：開盤五分鐘創三次新高﹙改用while迴圈﹚======================

variable: n(0);
variable: count(0);
if  Barinterval=1 and barfreq ="Min" then Begin  //適用於1分鐘線
//執行迴圈，檢查過去五分鐘高點過前高的次數
if time = 90500 then begin
	n = 1;
	while n <= 5 begin//以下的陳述(到end;為止)，n=1執行一次，n=2執行一次，一直到n=5
		if high[n]>high[n-1]
		then count=count+1;
		n = n + 1;
	end;
end;

//設定警示條件：if.. then ret=1;
if count>=3
then ret=1;
end;
```

---


---

## 腳本檔案: 警示/!語法範例/陣列例子.xs

```xs
{@type:sensor}
//陣列可以用來存放多個相同屬性的變數值，而不需重複宣告

//2.宣告變數，利用variable
variable: i(0); //用來做迴圈的
//宣告陣列，名稱ValueArray，內含100個元素，索引值從0到99，初始值為0
array:ValueArray[99](0);

//利用迴圈將陣列的每個元素填入對應的值，
//例如：把過去1~99的High指到ValueArray裡
//使得 ValueArray[1] =High[1] ,ValueArray[2] =High[2],
//     ValueArray[3] =High[3] ... ValueArray[99] =High[99]
for  i = 1 to 99
begin
	ValueArray[i] = High[i] ;
end;

//陣列可以透過內建函數做運算
//如果要全部加總
value1 = Array_Sum(ValueArray,1,99);
//或是從第 7個加到第20個
value1 = Array_Sum(ValueArray,7,20);

//6.設定警示條件：if.. then ret=1;
if value1 >= close * 14
then ret=1;
```

---


---

## 腳本檔案: 警示/1.籌碼監控/主力切入見真章.xs

```xs
{@type:sensor}
input: pastDays(3); setinputname(1,"近期天數");
input: UpRatio(3.5); setinputname(2, "上漲幅度(%)");
input: _buyAmount(3000); setinputname(3,"累積金額(萬)");
input:TXT("僅適用日線"); setinputname(4,"使用限制");

variable: SumForce(0);
variable:intrabarpersist tickcounter(0);

settotalbar(pastdays + 3);

if BarFreq <> "D" then return;

if   close > close[1]*(1 + UpRatio/100) then
begin
	// 過去N日 主力買賣超的成交金額的總和
    //	
    SumForce = Summation((AvgPrice * GetField("主力買賣超張數")/10)[1], pastDays);

	if SumForce > _buyAmount  then ret =1;
end;
```

---


---

## 腳本檔案: 警示/1.籌碼監控/主力認賠再追賣.xs

```xs
{@type:sensor}
input:TXT("僅適用日線"); setinputname(1,"使用限制");

variable: pastDays(10);

settotalbar(15);

if BarFreq <> "D" then return;
 
if close < lowest(low[1] ,pastDays) and
   volume > volume[1]*0.5 and
   GetField("主力買賣超張數")[1] < average(volume[1],pastDays)/-7 and
   Summation(GetField("主力買賣超張數")[2],pastDays) > Average(volume[2],pastDays)/7
 then ret =1;
```

---


---

## 腳本檔案: 警示/1.籌碼監控/券增價漲再推升.xs

```xs
{@type:sensor}
input: pastDays(10); setinputname(1,"近期天數");
input: UpRatio(3.5); setinputname(2, "上漲幅度(%)");
input:TXT("僅適用日線"); setinputname(3,"使用限制");

settotalbar(pastdays + 3);

if BarFreq <> "D" then return;

if  close > high[1] and close > close[1]*(1 + UpRatio/100) and
	Getfield("融券餘額張數")[1] = highest(Getfield("融券餘額張數")[1] ,pastDays)  
then ret=1;
```

---


---

## 腳本檔案: 警示/1.籌碼監控/外資增持收新高.xs

```xs
{@type:sensor}
input: pastDays(3); setinputname(1,"近期天數");
input: _buyAmount(3000); setinputname(2,"累積金額(萬)");
input:TXT("僅適用日線"); setinputname(3,"使用限制");

variable: SumForce(0);

settotalbar(pastdays + 3);

if BarFreq <> "D" then return;

if close > highest(high[1],pastDays) then 
begin
	// 過去N日外資買超金額
    //	
    SumForce = Summation((AvgPrice * GetField("外資買賣超")/10)[1], pastDays);

	if SumForce > _buyAmount   then ret =1;
end;
```

---


---

## 腳本檔案: 警示/1.籌碼監控/外資拉抬上攻.xs

```xs
{@type:sensor}
input: pastDays(3); setinputname(1,"計算天數");
input: _BuyRatio(25); setinputname(2,"買超佔比例(%)");
input:TXT("僅適用日線"); setinputname(3,"使用限制");

variable: SumForce(0);
variable: SumTotalVolume(0);

settotalbar(pastdays + 3);

if BarFreq <> "D" then return;

if Close > High[1] then
begin
	SumTotalVolume = Summation(volume[1], pastDays);
	SumForce = Summation(GetField("外資買賣超")[1], pastDays);

	if SumForce > SumTotalVolume * _BuyRatio / 100 then ret =1;
end;
```

---


---

## 腳本檔案: 警示/1.籌碼監控/外資換手再創高.xs

```xs
{@type:sensor}
Input: Percent(30); SetInputName(1, "外資換手比重(%)");
input:TXT("僅適用日線"); setinputname(2,"使用限制");

variable:FB(0);	FB=GetField("外資買張")[1];
variable:FS(0); FS=GetField("外資賣張")[1];	

settotalbar(5);

if BarFreq <> "D" then return;

if close > high[1] and FB-FS > 0 and (FB+FS) > 2 * volume[1] * Percent / 100  then ret=1;
```

---


---

## 腳本檔案: 警示/1.籌碼監控/實戶潛進終抬頭.xs

```xs
{@type:sensor}
input: pastDays(3); setinputname(1,"計算天數");
input: _BuyRatio(20); setinputname(2,"買超佔比例(%)");
input: length(20); setinputname(3, "整理期間");
input:TXT("僅適用日線"); setinputname(4,"使用限制");

variable: MonthLine(0); //現在的整理期間位置
variable: SumForce(0);
variable: SumTotalVolume(0);
variable: counter(0);

settotalbar(pastdays + 3);

MonthLine = average(close[1],length);

if BarFreq <> "D" then return;

if Close crosses over MonthLine then
begin
  
    counter = summationif(close[1] < MonthLine, 1, pastDays);
    
	if counter  = pastDays then 
	begin
	// 最近一段時間在月線底下的吃貨量
     	SumForce = summationif(close[1] < MonthLine, GetField("實戶買賣超張數")[1], pastDays);
    	SumTotalVolume = Summationif(close[1] < MonthLine, Volume[1], pastDays);
	if SumForce > SumTotalVolume * _BuyRatio / 100  then ret =1;
	end;
end;
```

---


---

## 腳本檔案: 警示/1.籌碼監控/投信加持卻遇襲.xs

```xs
{@type:sensor}
Input: pastDays(5); setinputname(1, "計算天數");
Input: _buyAmount(1000); setinputname(2, "買超張數");
input:TXT("僅適用日線"); setinputname(3,"使用限制");

variable: SumForce(0);

settotalbar(pastdays + 3);

if BarFreq <> "D" then return;

if close < lowest(low[1], pastdays) then
begin
	sumForce = Summation(GetField("投信買賣超")[1], pastDays);
	if sumForce > _buyAmount then ret=1;

end;
```

---


---

## 腳本檔案: 警示/1.籌碼監控/投信存股連拉升.xs

```xs
{@type:sensor}
input: HoldRatio(50); setinputname(1,"投信持股比例下限(%)");
input: Length(25); setinputname(2, "持股檢查區間");
input:TXT("僅適用日線"); setinputname(3,"使用限制");

settotalbar(Length + 3);

if BarFreq <> "D" then return;

if  GetField("投信持股比例")[1]> holdratio and
    GetField("投信持股比例")[1]=highest(GetField("投信持股比例")[1], Length) and
    close > close[1] and close[1] > close[2] and close[2] > close[3]
    
    then ret =1;
```

---


---

## 腳本檔案: 警示/1.籌碼監控/投信拉抬上攻.xs

```xs
{@type:sensor}
input: pastDays(3); setinputname(1,"計算天數");
input: _BuyRatio(25); setinputname(2,"買超佔比例(%)");
input:TXT("僅適用日線"); setinputname(3,"使用限制");

variable: SumForce(0);
variable: SumTotalVolume(0);

settotalbar(pastDays + 3);

if BarFreq <> "D" then return;

if Close > High[1] then
begin
	SumForce = Summation(GetField("投信買賣超")[1], pastDays);
	sumTotalVolume = Summation(Volume[1], pastDays);

	if SumForce > SumTotalVolume * _BuyRatio/100 then ret =1;

end;
```

---


---

## 腳本檔案: 警示/1.籌碼監控/散戶下車股價漲.xs

```xs
{@type:sensor}
input:TXT("僅適用日線"); setinputname(1,"使用限制");

settotalbar(3);

if BarFreq <> "D" then return;

if close > high[1] and 
	GetField("散戶買賣超張數")[1] < volume[1] * -0.1  then ret=1;
```

---


---

## 腳本檔案: 警示/1.籌碼監控/散戶撿到出貨後創低.xs

```xs
{@type:sensor}
input: ChangeKshares(1000); setinputname(1,"主力出貨張數");
input:TXT("僅適用日線"); setinputname(2,"使用限制");

settotalbar(3);

if BarFreq <> "D" then return;

if close < low[1] and
	GetField("主力買賣超張數")[1] < ChangeKshares*-1 and 
	GetField("散戶買賣超張數")[1] > ChangeKshares
then ret=1;
```

---


---

## 腳本檔案: 警示/1.籌碼監控/法人主攻漲升.xs

```xs
{@type:sensor}
input: pastDays(3); setinputname(1,"計算天數");
input: _BuyRatio(25); setinputname(2,"買超佔比例(%)");
input:TXT("僅適用日線"); setinputname(3,"使用限制");

variable: SumForce(0);
variable: SumTotalVolume(0);

settotalbar(pastDays + 3);

if BarFreq <> "D" then return;

if Close > High[1] and close[1] > close[2] then
begin
	SumForce = Summation(
		(GetField("外資買賣超")+GetField("自營商買賣超")+GetField("投信買賣超"))[1], 
		pastDays);
	SumTotalVolume = Summation(Volume[1], pastDays);

	if SumForce > SumTotalVolume * _BuyRatio / 100  then ret =1;
end;
```

---


---

## 腳本檔案: 警示/1.籌碼監控/自營商增持收新高.xs

```xs
{@type:sensor}
input: pastDays(3); setinputname(1,"近期天數");
input: _buyAmount(3000); setinputname(2,"累積金額(萬)");
input:TXT("僅適用日線"); setinputname(3,"使用限制");

variable: SumForce(0);

if BarFreq <> "D" then return;

if close > highest(high[1],pastDays) then 
begin
	SumForce = Summation((AvgPrice * GetField("自營商買賣超")/10)[1], pastDays);

	if SumForce > _buyAmount   then ret =1;
end;
```

---


---

## 腳本檔案: 警示/1.籌碼監控/自營商拉抬上攻.xs

```xs
{@type:sensor}
input: pastDays(3); setinputname(1,"計算天數");
input: _BuyRatio(25); setinputname(2,"買超佔比例(%)");
input:TXT("僅適用日線"); setinputname(3,"使用限制");

variable: SumForce(0);
variable: SumTotalVolume(0);

settotalbar(pastDays + 3);

if BarFreq <> "D" then return;

if Close > High[1] then
begin
	SumForce = Summation(GetField("自營商買賣超")[1], pastDays);
	SumTotalVolume = Summation(Volume[1], pastDays);

	if SumForce > SumTotalVolume * _BuyRatio / 100 then ret =1;
end;
```

---


---

## 腳本檔案: 警示/1.籌碼監控/融資追捧戰新高.xs

```xs
{@type:sensor}
input: pastDays(10); setinputname(1,"計算天數");
input:TXT("僅適用日線"); setinputname(2,"使用限制");

settotalbar(pastDays + 3);

if BarFreq <> "D" then return;

if Getfield("融資餘額張數")[1] = highest(Getfield("融資餘額張數")[1] ,pastDays) and
   close >= highest(high[1],pastDays)  
then ret=1;
```

---


---

## 腳本檔案: 警示/1.籌碼監控/連日外盤攻擊創新高.xs

```xs
{@type:sensor}
input:TXT("僅適用日線"); setinputname(1,"使用限制");

settotalbar(3);

if BarFreq <> "D" then return;

if Close > maxlist(high[1],high[2]) and GetField("內盤量","D")>0 and GetField("外盤量") > GetField("內盤量","D") * 1.2  then
begin
	if TrueAll(Getfield("外盤量")[1] > 1.1 * Getfield("內盤量")[1], 3) then ret=1;
end;
```

---


---

## 腳本檔案: 警示/2.市場常用語/N期內創新高次數.xs

```xs
{@type:sensor}
input:Length(10); setinputname(1,"N期內");
input:mNewHighTimes(3); setinputname(2,"創M次以上新高");
 
variable: la(Length-1); //日數與參數調整
variable: QHigh(0); Qhigh=high[la]; //含當根K棒 最左邊第一筆資料起算
variable: _outputdays(0);　　_outputdays=0; //每跟K要歸0
variable: i(0); //迴圈用數

settotalbar(Length + 3);
 
for i = 1 to la begin  
     if ( high[la-i]  > QHigh ) then
      begin
        _outputdays+=1;　　
      　QHigh = high[la-i];
     end; 
end;

if high = QHigh and _outputdays >= mNewHighTimes then ret=1;
```

---


---

## 腳本檔案: 警示/2.市場常用語/N期內破底次數.xs

```xs
{@type:sensor}
input:Length(10); setinputname(1,"n期內");
input:mNewLowTimes(3); setinputname(2,"創幾次以上新低");
 
variable: la(Length-1); //日數與參數調整
variable: QLow(0); QLow=Low[la]; //含當根K棒 最左邊第一筆資料起算
variable: _outputdays(0);　　_outputdays=0; //每跟K要歸0
variable: i(0); //迴圈用數

settotalbar(Length + 3);
 
for i = 1 to la begin  
     if ( Low[la-i]  < QLow ) then
      begin
        _outputdays+=1;　　
      　QLow = Low[la-i];
     end; 
end;

if Low = QLow and _outputdays >= mNewLowTimes then ret=1;
```

---


---

## 腳本檔案: 警示/2.市場常用語/今日多方表態.xs

```xs
{@type:sensor}

{三次到頂而破}
variable:CaliPrice(0),peakIndex(0),MaxPeak(0);
Array:peakDate[50](0),peakPrice[50](0),LongTrendPercent[50](0);
CaliPrice = (High[0]+Low[0]+Close[0])/3;

if CaliPrice[2] = MaxList(CaliPrice ,CaliPrice[1],CaliPrice[2],CaliPrice[3],CaliPrice[4]) and High[2] > CaliPrice[4]*1.02 and High[2] > CaliPrice[0]*1.02  then begin
	peakDate[peakIndex] = Date[2];peakPrice[peakIndex] = High[2];
	if peakIndex = 0 then LongTrendPercent[peakIndex]  = ( High[2]/ Close[2+20]-1)*100;
	if peakIndex > 0 and DateDiff(date,peakDate[peakIndex-1]) >5 then LongTrendPercent[peakIndex]  = ( High[2]/ Close[2+20]-1)*100;
	peakIndex+=1;
end;

if Date=CurrentDate  and Close > Open then begin

  if peakIndex >2 and Absvalue(peakPrice[peakIndex-1]/ peakPrice[peakIndex-2]-1 )< 0.01 and DateDiff(Date, peakDate[peakIndex-1])>20 then condition1 =true ;
  if  condition1  and  Close*1.065   >  highest(high[1],100) and
    minlist(low[100],low[99],low[98],low[97],low[96]) = Lowest(Low,100) and
    peakIndex >3 and LongTrendPercent[peakIndex-2] >20 and 
    Absvalue( peakPrice[peakIndex-1]/ peakPrice[peakIndex-2]-1 )< 0.01 and 
    DateDiff( peakDate[peakIndex-2] ,peakDate[peakIndex-3]) > 20 and 
    DateDiff( peakDate[peakIndex-1] ,peakDate[peakIndex-2]) > 5 and 
    Date < DateAdd(peakDate[peakIndex-1],"D",20)  
    then begin
    MaxPeak =MaxList(peakPrice[peakIndex-1],peakPrice[peakIndex-2]);
    if  Close > MaxPeak*1.005  and C>O then ret=1; 
    end;
end;

{激烈波動}
if Date =currentdate then  begin
	variable:STDEV(standarddev(volume[1],19,1)*3);
	if C>O and Volume*GetField("均價") > 30000{仟元} and  Close > High*0.99 and high = highest(high,20) and highest(high[1],19)/lowest(Low[1],19) - 1 <0.065 and 
	   TrueAll(ABSValue(high[1]/low[1]-1)<0.04,15) and  Volume > average(Volume[1],19)+STDEV then ret=1;   
end;

{波段初漲}
variable:hHigh(0),pC(0),iHigh(0),iLow(10000),iDate(0),eLow(10000);
if DateDiff(currentdate,date) < 93 then begin 	
    eLow = minlist(low,elow);
	if DateDiff(currentdate,date) >=90 then begin iHigh =high; iDate= Date; value1=open; end;
	hHigh = maxlist(high,hHigh); 
	if eLow = Low then hHigh = low;
	if hHigh > iHigh  then begin
	if C>O and iHigh<> iLow and close> eLow*1.08 and DateDiff(Date,iDate)> 30 and v>500 then  ret=1;
	iHigh =hHigh;iLOw = hHigh;iDate =Date;
	end else iLow =minlist(Low,iLow);
end;

{突破均線極度糾結}
variable:VSTDEV(1000000),PSTDEV(1000),AVG1(0),AVG2(0),AVG3(0),AVG4(0);
 AVG1 = average(close,5);AVG2 = average(close,10);AVG3 = average(close,20);AVG4 = average(close,60);
 if Date = currentdate then   begin
   VSTDEV=standarddev(volume[1],19,1)*3;
   PSTDEV=standarddev(H[1]-L[1],19,1)*3;
   if volume < average(Volume[1],19)+VSTDEV  or (C-O)/(H-L) < 0.7 then return;
   if C>O and Close  > maxlist(AVG1,AVG2,AVG3,AVG4)  and C > L +PSTDEV and  TrueAll( H[1]/L[1]-1 < 0.07,20) and 
       TrueAll(maxlist(AVG1,AVG2,AVG3,AVG4)/Maxlist( Minlist(AVG1,AVG2,AVG3,AVG4),0.01)-1 < 0.035,20) then ret=1;
 end;
```

---


---

## 腳本檔案: 警示/2.市場常用語/今日資券籌碼分析.xs

```xs
{@type:sensor}
variable:i(1);
if Currenttime > 220000  or Currenttime < 083000 then i=0; 

settotalbar(3);

if GetField("成交金額")[i]>10000000 and GetField("融資使用率")[i+1] > 0 and
   (GetField("融資使用率")[i]/GetField("融資使用率")[i+1]-1)*100 * (C[i]/C[i+1]-1)*100 >40
then ret=1;

if  C[i] > C[i+2]*1.1 and (GetField("融券增減張數")[i]*C[i])> 10000 then ret=1;
```

---


---

## 腳本檔案: 警示/2.市場常用語/分鐘暴量n%.xs

```xs
{@type:sensor}
input:percent(100);  setinputname(1,"量增比例%");
input:Length(200);  setinputname(2,"均量期數");
input:XLimit(True);  setinputname(3,"限制最低觸發門檻");
input:atVolume(500);  setinputname(4,"最低觸發張數");
input:TXT("建議使用分鐘線"); setinputname(5,"使用說明");

variable: AvgVolume(0);

settotalbar(Length + 3);

AvgVolume=Average(volume,Length);
if XLimit then 
begin
  if Volume > atVolume  and  volume > AvgVolume *(1+ percent/100)  then ret=1;
end
else
begin
  if Volume > Volume[1]  and  volume > AvgVolume *(1+ percent/100)  then ret=1;
end;
```

---


---

## 腳本檔案: 警示/2.市場常用語/外盤漲停.xs

```xs
{@type:sensor}
settotalbar(3);
if GetField("漲停價", "D") = q_Ask and close <> GetField("漲停價", "D") then ret=1;
```

---


---

## 腳本檔案: 警示/2.市場常用語/多次觸底而破 .xs

```xs
{@type:sensor}
input:HitTimes(3);    setinputname(1,"設定觸底次數");
input:RangeRatio(1);  setinputname(2,"設定底部區範圍寬度%");
input:Length(20);     setinputname(3,"計算期數");

settotalbar(Length + 3);
 
variable: theLow(0); theLow = lowest(low[1],Length);  //找到過去期間的最低點
variable: LowUpperBound(0);  LowUpperBound = theLow *(100+RangeRatio)/100;  // 設為瓶頸區間上界
variable: TouchRangeTimes(0); TouchRangeTimes=0;  //期間中進入瓶頸區間的低點次數,每根K棒要歸0
variable: ix(0);
 
for ix = length-1  downto 1 
begin
      if Low[ix] < LowUpperBound  then TouchRangeTimes +=1;  //回算在此區間中 進去瓶頸區的次數
end;
 
if  TouchRangeTimes >= HitTimes   and  (q_bid <theLow  or  close < theLow)  then ret=1;
```

---


---

## 腳本檔案: 警示/2.市場常用語/大單敲進.xs

```xs
{@type:sensor}
input: atVolume(100); setinputname(1,"大單門檻");
input: LaTime(10); setinputname(2,"大單筆數");
input:TXT("須逐筆洗價"); setinputname(3,"使用限制");

settotalbar(3);

variable: intrabarpersist Xtime(0);//計數器
variable: intrabarpersist Volumestamp(0);
variable: intrabarpersist XDate(0);

Volumestamp =GetField("Volume", "D");

if Date > XDate or Volumestamp = Volumestamp[1]  then Xtime =0; //開盤那根要歸0次數
XDate = Date;

if GetField("Volume", "Tick") > atVolume and GetField("內外盤","Tick")=1 then  Xtime+=1; //量夠大就加1次

if Xtime > LaTime  then 
begin
	ret=1; 
	Xtime=0;
end;
```

---


---

## 腳本檔案: 警示/2.市場常用語/急拉.xs

```xs
{@type:sensor}
input:P1(1.5); setinputname(1,"急拉幅度%");

settotalbar(3);

IF close > close[1]*(1+P1/100)  and close=high and volume>volume[1]
then ret=1;
```

---


---

## 腳本檔案: 警示/2.市場常用語/急殺.xs

```xs
{@type:sensor}
input:P1(1.5); setinputname(1,"急殺幅度%");

settotalbar(3);

IF close < close[1]*(1-P1/100)  and close=Low and volume>volume[1]
then ret=1;
```

---


---

## 腳本檔案: 警示/2.市場常用語/拉尾盤.xs

```xs
{@type:sensor}
input:Ratio(1); setinputname(1,"拉尾盤幅度%");
input:tTime(130000); setinputname(2,"尾盤切算時間%");
input:TXT("限用5分鐘以下"); setinputname(3,"使用限制");
if barfreq <> "Min" or barinterval > 5 then return;

settotalbar(3);

variable:fPrice(0); if date<>date[1] then fPrice=0;

if time < tTime then fPrice = Close else
if Close > fPrice*(1+Ratio/100) and time >= tTime and fPrice>0 
then RET=1;
```

---


---

## 腳本檔案: 警示/2.市場常用語/殺尾盤.xs

```xs
{@type:sensor}
input:TXT("限用10分鐘以下"); setinputname(1,"使用限制");

settotalbar(3);

variable:KeyPrice(0);

if Date> date[1] then KeyPrice = 0;		// 換日的話則重新定義KeyPrice
if time>132000 and KeyPrice = 0 then KeyPrice =close;

if KeyPrice > 0 and close <= KeyPrice *0.99//時間超過13:20分且十分鐘跌幅超過1%
then ret=1;
```

---


---

## 腳本檔案: 警示/2.市場常用語/當日上漲n%.xs

```xs
{@type:sensor}
input:percent(1.5); setinputname(1,"當日上漲幅度%");

settotalbar(3);

variable:WorkTrue(true);

if  WorkTrue and  currenttime <= TimeAdd(time,"M",1) and 
    Close > GetField("RefPrice", "D") * (1+ Percent/100) then 
begin
Ret=1;
WorkTrue =false;
end;

if WorkTrue =false and Close < GetField("RefPrice", "D") * (1+ Percent/100) then WorkTrue =true;
```

---


---

## 腳本檔案: 警示/2.市場常用語/盤中多方警示.xs

```xs
{@type:sensor}
settotalbar(20);

array:intrabarpersist Trigger[20](True);

Array: intrabarpersist MK[330,6](0),intrabarpersist MD[7](1); {Time,Open,High,Low,Close,Volume}
variable:intrabarpersist BI(1),OT(090000){開盤時間},MF{KBbar頻率}(1);
if CurrentTime < TimeAdd(OT,"M",BI*MF) then 
begin  
MD[2]=MaxList(MD[2],C); MD[3]=MinList(MD[3],C);MD[4]=C; MD[7]+=q_TickVolume;
if BI =1 then  begin MD[1]=GetField("Open", "D");MD[2]=GetField("High", "D");MD[3]=GetField("Low", "D") ;end;
end else begin
MK[BI,0]=TimeAdd(OT,"M",BI-1);MK[BI,1]=MD[1];MK[BI,2]=MD[2];MK[BI,3]= MD[3];MK[BI,4]= MD[4];MK[BI,5]=GetField("Volume", "D")-q_TickVolume-MD[5];            
BI+=1; MD[1]=C;MD[2]=C;MD[3]=C;MD[4]=C; MD[5]=GetField("Volume", "D")-q_TickVolume; MD[7]=q_TickVolume;
end;

array:intrabarpersist Q1[100,3](90000),intrabarpersist Q2[10,3](90000),intrabarpersist QI[5,5](0); QI[1,4] = 99; QI[2,4] = 9; 
variable:QD(1);
for QD = 1 to 2
begin
if QI[QD,1] < QI[QD,4] then QI[QD,1]+=1 else QI[QD,1]=0; 
if QI[QD,1] =0 then QI[QD,2]=QI[QD,4] else QI[QD,2]=QI[QD,2]-1; 
if QI[QD,1] =QI[QD,4] then QI[QD,3]=0 else QI[QD,3]=QI[QD,1]+1;
end;
Q1[QI[1,1],0] = currenttime;Q1[QI[1,1],1] = Close;Q1[QI[1,1],2] = q_TickVolume;     
Q2[QI[2,1],0] = currenttime;Q2[QI[2,1],1] = Close;Q2[QI[2,1],2] = q_TickVolume;     


{=============}
variable:TA1(-1),TA2(-1),AVGX(10000);
if Date = currentdate then begin
if TA1 = -1  then TA1 = Countif( GetField("融資增減張數")[1]<0,10);
variable: forceratio(0);
if V[1] > 0 then forceratio = GetField("主力買賣超張數")[1]/V[1] else forceratio = forceratio[1];
if TA2 = -1 then TA2 = Summation(forceratio,10);
if AVGX =10000 then AVGX = Average(Close,5);{五日}
end;
{=============}

{開盤處理融資追繳後的反彈}
if Trigger[19] then  if currenttime < 093000 and Close > Low *1.02 and Close > Open and  V > V[1]*0.6 and  TA1=10{融資增減張數之減少天數}
and Low = Lowest(Low,20) and Low < Highest(high,20)*0.7 then  begin ret=1; trigger[19]=false; end;
if h > highest(h[1],8) and v < highest(v[1],18)*BI/135 then return; 
{過濾} 
if Close = GetField("漲停價", "D") or Close < highest(high,10)*0.95 or GetField("均價")*GetField("Volume", "D") < 10000{仟元}   
   or Close < GetField("Volume", "D")*0.985 or Date <currentdate 
   or Close > AVGX*1.25 or Close > C[5]*1.25   then return;

{1.1分鐘線爆量上漲}
if Trigger[1] then  if MD[7] > (V[1]+V)/(270+BI)*3 and Close > MD[1]*1.01  then begin ret=1; trigger[1]=false; end;
{2.5分鐘線3連陽}
if Trigger[2] then  if BI >= 15 and MK[BI,4]> MK[BI-4,1] and MK[BI-5,4]> MK[BI-9,1] and MK[BI-10,4] > MK[BI-14,1] then begin ret=1; trigger[2]=false; end;
{3.連日盤整後急拉}
if Trigger[3] then  if Close > Q2[QI[2,3],1]*1.015 and TimeDiff(currenttime, Q2[QI[2,3],0],"M") <5 and TrueAll(absvalue(high[1]/low[1]-1) < 0.03,10) then begin ret=1; trigger[3]=false; end;
{4.主動性買盤大增} variable: AvgOutSideVol(averageIF( close > close[1] ,volume,15));
if Trigger[4] then if GetField("外盤量", "D") > AvgOutSideVol*1.5 then begin ret=1; trigger[4]=false; end;
{5.多頭波動表態}   variable:STDEV(standarddev(High[1]-Low[1],15,1)*3);
if Trigger[5] then if q_PriceChangeRatio >3{%} and Volume*GetField("均價") > 30000{仟元} and  High > Low + average(High[1]-Low[1],15)+STDEV then begin ret=1; trigger[5]=false; end;
{6.多方放量待起漲} variable:VSTDEV(standarddev(volume,15,1)*3);
if Trigger[6] then if q_PriceChangeRatio>2{%} and  volume > average(volume[1],15)+3*VSTDEV and close > highest(high[1],15)*0.965 then begin ret=1; trigger[6]=false; end;
{7.連日強攻再滾量攻高}
if Trigger[7] then  if BI>3 and  Close > High[1] and (MK[BI,5]+MK[BI-1,5]+MK[BI-2,5])*GetField("均價") > 10000{仟元} and CountIF(high>high[1],10) > 7 then begin ret=1; trigger[7]=false; end;
{8.10個1分鐘階梯連漲} variable:Steps(true); 
if Trigger[8] then if BI>10 then begin for QD=0 to 9   begin    Steps  = Steps and (MK[BI-QD,4]>MK[BI-1-QD,4]); end;  if Steps then begin ret=1; trigger[8]=false; end; ;end;  
{9.多方人氣急增}
if Trigger[9] then if BI>4  and q_PriceChangeRatio > 2{%} and MK[BI,4]> MK[BI-1,1]  and MK[BI-1,4]> MK[BI-3,1]  and (TimeDiff( currenttime, Q1[QI[1,3],0],"S")- TimeDiff(currenttime, Q2[QI[2,3],0],"S"))/90 > TimeDiff(currenttime, Q2[QI[2,3],0],"S")*3/10 then begin ret=1; trigger[9]=false; end;
{10.主力決心作價}
if Trigger[10] then if  V*GetField("均價")> 30000{仟元} and TA2{"主力買賣超張數"} > 0.33 and high= Highest(High,10) then  begin ret=1; trigger[10]=false; end;
{11.開盤快速急攻}
if Trigger[11] then if CurrentTime < 091500  and q_PriceChangeRatio >2{%} and Volume*GetField("均價") > 30000{仟元}  and high =Highest(High,15)  and  High > Low[1] + average(High[1]-Low[1],15)+STDEV then begin ret=1; trigger[11]=false; end;
{12.2%門前急拉} 
if Trigger[12] then if Q2[QI[2,1],1] < GetField("RefPrice", "D") *1.02 and close >= GetField("RefPrice", "D") *1.02 and  Close * q_TickVolume >500{仟元} and  Close > Q2[QI[2,3],1]*1.01  and   timediff(Currenttime,Q2[QI[2,3],0],"M")< 3{分鐘}  then begin ret=1; trigger[12]=false; end;    {3分鐘內快速拉升}
{13.下殺後反彈過今高}
if Trigger[13] then if Close > GetField("RefPrice", "D") and Close > GetField("Open", "D") and  Close = GetField("Volume", "D") and  Close >= GetField("Low", "D")*1.02 then begin ret=1; trigger[13]=false; end;
{14.帶量衝新高}
if Trigger[14] then if Close = GetField("Volume", "D") and Close > highest(H[1],20)  and Close*q_TickVolume > 3000  then begin ret=1; trigger[14]=false; end;
{15.開盤15分鐘一路向上不回頭} variable:Counter(0);
if Trigger[15] then  If BI =15 then  for QD =0 to 13  if MK[BI-QD,4] > MK[BI-1-QD,4] then Counter+=1;  if Counter > 12 then begin ret=1; trigger[15]=false; end;
```

---


---

## 腳本檔案: 警示/2.市場常用語/突破上切線.xs

```xs
{@type:sensor}
input:Length(20); setinputname(1,"上切計算期數");
input:Rate(50); setinputname(2,"陡增率");

settotalbar(Length + 3);

variable: Factor(0);

Factor = 100/Close[Length];

if close > open and close > highest(high[1],Length) and 
   (linearregslope(high*Factor,3) -linearregslope(high*Factor,Length))>Rate*0.01 
then ret=1;
```

---


---

## 腳本檔案: 警示/2.市場常用語/翻紅.xs

```xs
{@type:sensor}
settotalbar(7);
if close crosses over close[1]
then ret=1;
```

---


---

## 腳本檔案: 警示/2.市場常用語/翻黑.xs

```xs
{@type:sensor}
settotalbar(7);
if close crosses under close[1]
then ret=1;
```

---


---

## 腳本檔案: 警示/2.市場常用語/資減券增.xs

```xs
{@type:sensor}
input:x1(300);setinputname(1,"融資減少張");
input:x2(200);setinputname(2,"融券增加張");
input:x3(10); setinputname(3,"全計佔成交量比例%");
input: Type(1); setinputname(4,"最新資料：0=今日、1=昨日");
input: TXT1("僅適用日線"); setinputname(5,"使用限制");
input: TXT2("盤中無當日資券資料"); setinputname(6,"建議使用單次洗價模式");

settotalbar(3);

value1=GetField("融資增減張數")[Type];//融資增減張數
value2=GetField("融券增減張數")[Type];//融券增減張數

 if value1 <-x1 and 
    value2 > x2 and 
    (value2-value1)/volume[Type]>x3/100
 then ret=1;
```

---


---

## 腳本檔案: 警示/2.市場常用語/近日多方火力集中.xs

```xs
{@type:sensor}
settotalbar(10);

variable:CDay(3);
variable:i(1),XData(0),XDataAmount(0),XAmount(0),XV(0),XPrice(0),Trigger(False);

if Currenttime > 170000  or Currenttime < 083000 then i=0; 
Trigger=False;
XAmount =Summation(GetField("成交金額")[i],CDay);XV = Summation(V[i],CDay);XPrice = XAmount/XV/1000;
XDataAmount = Summation(GetField("主力買賣超張數")[i],CDay)/XV; if XDataAmount>0.2 and trueall( XDataAmount[1]<0.1,5) then Trigger=true;
XDataAmount = Summation(GetField("實戶買賣超張數")[i],CDay)/XV; if XDataAmount>0.25 and trueall( XDataAmount[1]<0.1,5) then Trigger=true;
XDataAmount = Summation(GetField("控盤者買賣超張數")[i],CDay)/XV; if XDataAmount>0.25 and trueall( XDataAmount[1]<0.1,5) then Trigger=true;
if C[i]> XPrice and  V>300 and Trigger then ret=1;


variable:iHigh(0),iDate(0);
if high > iHigh then begin iHigh= high;iDate= Date; end;
if DateDiff(Date,iDate) >30  and C > iHigh *0.935 and C<iHigh and
   (Summation(GetField("外資買賣超")[i]*XPrice,CDay) > 30000 or
    Summation(GetField("投信買賣超")[i]*XPrice,CDay) > 30000 or
	Summation(GetField("自營商買賣超")[i]*XPrice,CDay) > 30000)
then ret=1;
```

---


---

## 腳本檔案: 警示/2.市場常用語/連日量縮下跌.xs

```xs
{@type:sensor}
input:percent(4);setinputname(1,"累計下跌幅度%"); 
input:ratio(20); setinputname(2,"量縮幅度%"); 
input:Length(3);setinputname(3,"持續期數");

settotalbar(Length + 3);

if close[Length-1]  > Close * (1+percent/100) and 
   volume[Length-1] > Volume* (1+ratio/100) and 
   TrueAll(Close < Close[1] ,Length-1) 
then ret=1;
```

---


---

## 腳本檔案: 警示/2.市場常用語/開低走高.xs

```xs
{@type:sensor}
input:OpenGap(1); setinputname(1,"開低幅度%");
input:uppercent(1);setinputname(2,"從最低點反彈上揚幅度%");

settotalbar(3);

if  GetField("Low", "D") = GetField("Open", "D") and
    GetField("Open", "D") < GetField("RefPrice", "D") * (1- OpenGap/100) and
    q_Last	> GetField("Low", "D") * (1+uppercent/100)
then ret=1;
```

---


---

## 腳本檔案: 警示/2.市場常用語/開高走低.xs

```xs
{@type:sensor}
input:OpenGap(1); setinputname(1,"開高幅度%");
input:Downpercent(1);setinputname(2,"從最高點回檔下跌幅度%");

settotalbar(3);

if  GetField("High", "D") = GetField("Open", "D") and
    GetField("Open", "D") > GetField("RefPrice", "D") * (1+ OpenGap/100) and
    Close < GetField("High", "D") * (1 - Downpercent/100)
then ret=1;
```

---


---

## 腳本檔案: 警示/2.市場常用語/高點回檔n%.xs

```xs
{@type:sensor}
input:Length(20);  setinputname(1,"尋找高點期數");
input:percent(7); setinputname(2,"自高點回檔幅度%");

settotalbar(Length + 3);

if close < highest(high,Length)*(1- percent/100) then Ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/DMI賣出訊號.xs

```xs
{@type:sensor}
input:Length(14); setinputname(1,"計算期數");
variable: pdi(0), ndi(0), adx_value(0);

settotalbar(maxlist(Length,6) * 13 + 8);

DirectionMovement(Length, pdi, ndi, adx_value);

if pdi<pdi[1] and ndi>ndi[1] and ndi crosses over pdi
then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/KD高檔死亡交叉.xs

```xs
{@type:sensor}
input: Length(9), RSVt(3), Kt(3), HighBound(75);

SetTotalBar(maxlist(Length,6) * 3 + 8);

SetInputName(1, "計算期數");
SetInputName(2, "RSVt權數");
SetInputName(3, "Kt權數");
setInputName(4, "高檔區");

variable: rsv(0), k(0), _d(0);

Stochastic(Length, RSVt, Kt, rsv, k, _d);

if k>HighBound and k crosses under _d
then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/MACD出現賣出訊號.xs

```xs
{@type:sensor}
input: FastLength(12), SlowLength(26), MACDLength(9);

SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 3 + 8);

SetInputName(1, "DIF短期期數");
SetInputName(2, "DIF長期期數");
SetInputName(3, "MACD天數");

variable: difValue(0), macdValue(0), oscValue(0);

MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);

Ret = oscValue Crosses Below 0;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/MTM轉負.xs

```xs
{@type:sensor}
input: Length(10); SetInputName(1, "期數");

settotalbar(maxlist(Length,6) + 8);

if momentum(close,Length) crosses under 0 then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/OBV退潮.xs

```xs
{@type:sensor}
input:Length(15); setinputname(1,"計算期數");
variable: OBVolume(0);

settotalbar(10);

value1 = close-close[1];

if close<> close[1] then 
   OBVolume +=  Volume*(value1)/absvalue(value1);

 if close<highest(high,Length) and
    OBVolume[2]=highest(OBVolume,Length) and 
	OBVolume=lowest(OBVolume,3)
 then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/RSI高檔死亡交叉.xs

```xs
{@type:sensor}
input: Length1(6); SetInputName(1, "短期期數");
input: Length2(12); SetInputName(2, "長期期數");
input: HighBound(75); SetInputName(3, "高檔區");

settotalbar(maxlist(Length1,Length2,6) * 8 + 8);

value1=RSI(close,Length1);
value2=RSI(close,Length2);

if value1 crosses under value2 and value1>HighBound
then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/一舉跌破多根均線.xs

```xs
{@type:sensor}
input: shortlength(5); setinputname(1,"短期均線期數");
input: midlength(10);  setinputname(2,"中期均線期數");
input: Longlength(20); setinputname(3,"長期均線期數");

setbarback(maxlist(shortlength,midlength,Longlength,6)+8);

variable: shortaverage(0);
variable: midaverage(0);
variable: Longaverage(0);


shortaverage = Average(close,shortlength);
midaverage = Average(close,midlength) ;
Longaverage = Average(close,Longlength); 

if close  crosses under  shortaverage and 
   close  crosses under  midaverage and 
   close  crosses under  Longaverage 
then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/一黑破n紅.xs

```xs
{@type:sensor}
input:Length(3); setinputname(1,"計算期數");

settotalbar(Length + 3);

if high=highest(high[1],Length) and close<lowest(low[1],Length) 
then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/三長上影線.xs

```xs
{@type:sensor}
input: Percent(1.5); setinputname(1,"上影線佔股價絕對百分比");

settotalbar(5);

condition1 = (high- maxlist(open,close)) > absvalue(open-close)*3; 
condition2 = high > maxlist(open, close) * (100 + Percent)/100;

if trueall( condition1 and condition2, 3) then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/主力出貨 .xs

```xs
{@type:sensor}
input:RatioThre(1.5); setinputname(1,"下跌量上漲量比");

settotalbar(8);

variable: upvolume(0);//累計上漲量
variable: downvolume(0);//累計下跌量
variable: uprange(0);//累計上漲值
variable: downrange(0);//累計下跌值
variable: DUratio(0);//下跌量上漲量比
if date[1] <> date then 
begin 
      downvolume  =0; upvolume =0;
	  uprange =0; downrange=0;
      if close > open then  
	    begin 
	      upvolume = volume; 
		  uprange = close -open;   
		end
      else 
	  if close < open then  
		begin 
		  downvolume = volume;  
		  downrange = open -close; 
		end
	  else 
	  if close < close[1] then  
	    begin 
		  downvolume = volume;  
		  downrange = close[1] -close; 
	    end
	  else 
	  if close > close[1] then  
	    begin 
		  upvolume = volume; 
		  uprange = close -close[1]; 
	    end;
end;//如果前一個跟Bar跟目前的bar日期不同 今天第一根起算

if date[1] = date then  //還在同一天
begin 
      if close > close[1] then  
	    begin 
	      upvolume += volume; 
		  uprange += close -close[1];   
		end
      else 
	  if close < close[1] then  
	    begin 
		  downvolume += volume;  
		  downrange += close[1] -close; 
	    end;
 if upvolume > 0 then DUratio = downvolume/upvolume else DUratio=1;
end;

if DUratio crosses over RatioThre and uprange crosses under downrange then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/主力賣超.xs

```xs
{@type:sensor}
input:PastDays(3); setinputname(1,"計算天數");
input:summ(2000);setinputname(2,"合計賣超張數門檻");
input:TXT("僅適用日線"); setinputname(3,"使用限制");

settotalbar(PastDays + 3);

if Barfreq = "D" and close< close[1] and
   summation(GetField("LeaderDifference")[1],PastDays) <= summ*-1 then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/乖離過大.xs

```xs
{@type:sensor}
input:Length(200); setinputname(1,"計算期數");
input:Ratio(70); setinputname(2,"正向乖離門檻%");

settotalbar(Length + 3);

if close/average(close,Length)>= 1+Ratio/100
then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/分鐘線九連黑.xs

```xs
{@type:sensor}
Input: Length(9); SetInputName(1, "連續筆數");

settotalbar(Length + 3);

if Barfreq ="Min" then 
   if trueall(close < open,Length) then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/多日價量背離.xs

```xs
{@type:sensor}
input:Length(5); setinputname(1,"計算期數");
input:times(3);setinputname(2,"價量背離次數");
input:TXT("建議使用日線"); setinputname(3,"使用說明");

variable:count(0);

settotalbar(Length + 3);

count = CountIf(close > close[1] and volume < volume[1], Length);

if count > times then 
ret = 1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/大黑棒.xs

```xs
{@type:sensor}
input:Percent(4); setinputname(1,"實體K棒為股價絕對百分比");

settotalbar(3);

if open/close >= 1 + Percent/100  //實體(開盤-收盤)
then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/天價留上影線後未開高.xs

```xs
{@type:sensor}
input:Length(20); setinputname(1,"設定波段天數");
input:P1(2); setinputname(2,"設定高檔壓回百分比");
input:P2(0.5); setinputname(3,"當日開高基準百分比");
input:P3(0.5); setinputname(4,"上影線佔價格幅度%");
input:TXT("建議使用日線"); setinputname(5,"使用說明");

settotalbar(3);
setbarback(Length);

if  open - close[1] <P2/100*close[1]  and
    high[1]=highest(high,Length)  and 
	(high[1]-close[1])>= P1/100 *close[1] and
	high[1] > maxlist(open[1], close[1]) *(1+P3/100)
then  ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/天量後價量未再創新高.xs

```xs
{@type:sensor}
input:XLength(60); setinputname(1,"長期大量計算期數");
input:Length(3); setinputname(2,"自高點回檔天數");
input:TXT("建議使用日線"); setinputname(3,"使用說明");

variable: PriceHighBar(0),VolumeHighBar(0);

settotalbar(XLength + 3);

extremes(high,Length,1,value1,PriceHighBar);
extremes(volume,XLength,1,value1,VolumeHighBar);

if (PriceHighBar =Length-1) and VolumeHighBar=Length-1  then
ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/川上三鴉.xs

```xs
{@type:sensor}
settotalbar(3);
if TrueAll((open-close) > (high-low) * 0.5 and close <close[1],3) then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/巨量長黑.xs

```xs
{@type:sensor}
input:Amount(10000); setinputname(1,"依頻率設定巨量門檻");
settotalbar(3);
if open > Close * 1.025//實體 
and close[1] > Close * 1.035 //較前一日大跌
and volume >=amount 
then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/投信外資都賣超.xs

```xs
{@type:sensor}
input:TXT("僅適用日線"); setinputname(1,"使用限制");

settotalbar(3);

if Barfreq <> "D" then return;

if Open < Close[1] and  Close < Close[1] and
   GetField("外資買賣超")[1]<0 and GetField("投信買賣超")[1]<0
then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/散戶買單比例太高且走低.xs

```xs
{@type:sensor}
input:ratio(20); setinputname(1,"散戶買單比例%");
input:TXT("須逐筆洗價"); setinputname(2,"使用限制");

//單筆外盤成交值低於五十萬元稱為散單 //內外盤:內盤-1 外盤1
variable: intrabarpersist ACount(0);
variable: intrabarpersist TimeStamp(0);

settotalbar(3);

if barfreq ="Min" and currentdate = date then //分鐘線在今天時
begin
  TimeStamp =currenttime;
  if TimeStamp = TimeStamp[1] then  ACount=0;
  if TimeStamp[1] <= time  then // 盤中開啟 or 換Bar第一個進價
  begin
      if  GetField("內外盤","Tick") > 0 and GetField("Volume", "Tick") *Close <=500 then
            ACount = GetField("Volume", "Tick") *Close
 	    else 
	        ACount=0;
  end
  else
  begin
     if  GetField("內外盤","Tick") > 0 and GetField("Volume", "Tick") *Close <=500 then ACount+= GetField("Volume", "Tick") *Close;
  end;
  if ACount >= Ratio/100 * volume*close and  
     Close < GetField("RefPrice", "D")*0.985 and GetField("High", "D") < GetField("RefPrice", "D")*1.005 then ret=1;
end;

if barfreq ="D" then 
begin
  if  Date <> currentdate then Acount=0;
  if  GetField("內外盤","Tick") > 0 and GetField("Volume", "Tick") *Close <=500 then ACount+= GetField("Volume", "Tick") *Close;
  if ACount >= Ratio/100 * GetField("Volume", "D") * GetField("均價") and
     Close < GetField("RefPrice", "D")*0.985 and GetField("High", "D") < GetField("RefPrice", "D")*1.005 then ret=1;
end;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/海龜出場法則.xs

```xs
{@type:sensor}
input:Length(10); setinputname(1,"近N週期數");
input:TXT("僅適用日線"); setinputname(2,"使用限制");

settotalbar((Length + 3)*5);

if barfreq <> "D" and barfreq <> "AD" then Return;

if close < lowest(getfield("low","W")[1],Length)//近n週最低價
then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/盤中直線下跌.xs

```xs
{@type:sensor}
input:SlopeThre(2); setinputname(1,"下降坡度[2~15越大跌越快]");
input:Length(5); setinputname(2,"計算期數");

settotalbar(Length + 3);

variable:KBarOfDay(0),tOpen(100); KBarOfDay+=1;
if date<>date[1] then begin KBarOfDay=1; tOpen =Open; end;

if Length < KBarOfDay and currentbar > maxbarsback and
   Linearregslope(Low/tOpen*1000,Length) < SlopeThre*-1 then 
ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/竭盡缺口.xs

```xs
{@type:sensor}
input:Length(50); setinputname(1,"計算漲幅的區間");
input:Ratio(30); setinputname(2,"區間累計上漲幅度%");
input:OpenGapRatio(2); setinputname(3,"今日跳空上漲幅度%");
input:TXT("建議使用日線"); setinputname(4,"使用說明");

settotalbar(Length + 3);

if close / lowest(close,Length) >= 1+Ratio/100//區間漲幅夠大
and open[1]>close[2] //前一日已跳空
and open/close[1] >= 1+OpenGapRatio/100    //今天又跳空
then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/股價跌破走平後的高壓電線.xs

```xs
{@type:sensor}
input:Ratio(10); setinputname(1,"高壓電線幅度%");
input:Length(5); setinputname(2,"計算走平期數");

settotalbar(Length + 8);
setbarback(72);

variable: Factor(0);Factor = 100/Close;

if absvalue(linearregslope(avgprice[1]*Factor,Length))<=0.1 and  //走平
   close crosses under ((average(close,30)+average(close,72))/2 )* (1+Ratio*0.01) 
then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/股價震盪變大且收最低.xs

```xs
{@type:sensor}
input:Length(5);setinputname(1,"計算震盪幅度的區間期數");
input:BaseLength(20);setinputname(2,"震盪幅度計算區間");
input:Ratio(50);setinputname(3,"震盪放大百分比%");

settotalbar(8);
setbackbar(maxlist(Length,BaseLength));

value1=highest(high,Length)-lowest(low,Length);
value2=average(value1,BaseLength);

if	value1 crosses over value2 *(1+ratio/100) and close=low
then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/資增券減還收黑.xs

```xs
{@type:sensor}
input:V1(1000); setinputname(1,"融資增加張數");
input:V2(500); setinputname(2,"融券減少張數");
input:TXT("僅適用日線"); setinputname(3,"使用限制");

settotalbar(3);

if BarFreq <> "D" then return;

if close < close[1] and 
   GetField("融資增減張數")[1] > V1 and
   GetField("融券增減張數")[1] < V2*-1
then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/跌破n日低點.xs

```xs
{@type:sensor}
input:Length(20); setinputname(1,"計算期數");

settotalbar(Length + 3);

if close  < lowest(low[1],Length) then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/跌破上升趨勢線.xs

```xs
{@type:sensor}
input:Length(10); setinputname(1,"上升趨勢計算期數");
input:_Angle(30); setinputname(2,"上升趨勢角度");

settotalbar(Length + 3);

variable: TrendAngle(0);
variable: TrendAngleDelta(0);

if Close< Close[1] and Close[1] <Close[2] and Close[Length]>0 then begin

linearreg((high/Close[Length]-1)*100,Length,0,value1,TrendAngle,value3,value4);
 
TrendAngleDelta =TrendAngle-TrendAngle[1];
IF TrendAngleDelta-TrendAngleDelta[1] < -10 and close >Close[Length] THEN RET=1;
  
end;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/跌破均線.xs

```xs
{@type:sensor}
input: shortlength(5); setinputname(1,"短期均線期數");
input: midlength(10); setinputname(2,"中期均線期數");
input: Longlength(20); setinputname(3,"長期均線期數");

variable: shortaverage(0);
variable: midaverage(0);
variable: Longaverage(0);

settotalbar(3);
setbarback(maxlist(shortlength,midlength,Longlength));

shortaverage=Average(close,shortlength);
midaverage=Average(close,midlength) ;
Longaverage = Average(close,Longlength); 

if open > maxlist(shortaverage, midaverage, longaverage) and
   close < minlist(shortaverage, midaverage, longaverage)
then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/跳空下跌再破底.xs

```xs
{@type:sensor}
//分鐘線
input:Gapratio(1.5);setinputname(1,"跳空下跌百分比%");
input:TXT("僅適用分鐘線"); setinputname(2,"使用限制");

settotalbar(5);

if barfreq<>"Min" then return;

if Close < close[1] and Close < GetField("Open", "D") then 
   if GetField("Open", "D") < GetField("RefPrice", "D")*(100-Gapratio)/100  then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/連續n日開高走低收最低.xs

```xs
{@type:sensor}
input:Length(2); setinputname(1,"計算期數");

settotalbar(Length + 3);

if Trueall( Open > Close[1]*1.005 and Close<open and close = low , Length) then ret=1;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/階梯式下跌.xs

```xs
{@type:sensor}
input:TXT("5分鐘線以下"); setinputname(1,"使用限制");

settotalbar(13);

if barfreq<> "Min" or barinterval > 5 then return;

switch (barinterval)
begin
   case 1,2,5:
     if time =091000 and TrueAll(open=high and close=low and close< close[1],10/barinterval) then ret=1;
     break;
   case 3:
     if time =090900 and TrueAll(open=high and close=low and close< close[1],3) then ret=1;
     break;
end;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/高檔出現吊人線.xs

```xs
{@type:sensor}
settotalbar(33);

if Close < Close[1] then begin
	  
	condition1 = 
		open = High and close < open and
	   (high -low) > 2 *(high[1]-low[1]) and 
	   (close-low) > (open-close) *2;
	  
	condition2= close[1] > highest(High,30)*0.98; //昨日收盤價接近三十日高點

	if condition1 and condition2 then ret=1;

end;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/高檔出現黑暗之星.xs

```xs
{@type:sensor}
input:Length(10); setinputname(1,"計算期數");

settotalbar(Length + 3);

if (open-close)>= open *0.025 then //最近一根是長黑棒
begin

	value1 = highest(high,length);
	value2 = lowest(low,length);
	
	if value1 = value2 then return;
	
	value3 = (value1-close)/(value1-value2)*100;

	condition1 = value3 < 10; //接近近n日高點
	condition2 = (close[2]-open[2])/open[2]>=0.03;//一根長陽線
	condition3 =  open[1]>close[1]  and (high[1]-low[1])<=close[1]*0.02 
	and close[1]>close[2] - 0.5*(close[1]-open[1]) ; //一根小黑棒且未形成覆蓋線

	if condition1 and condition2 and condition3 then ret=1;

end;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/高檔覆蓋線.xs

```xs
{@type:sensor}
input: Length(10); setinputname(1,"計算期數");

settotalbar(3);
setbarback(maxlist(Length,42));

value1 = PercentR(14) - 100;
value2 = PercentR(28) - 100;
value3 = PercentR(42) - 100;

if  value1= 0 and value2=0 and value3 =0 then //用威廉指標來表示股價在高檔
begin

variable: HighPoint(0),LowPoint(0),RatioThre(0);
HighPoint = highest(high,length);
LowPoint = Lowest(Low,length);

if HighPoint > LowPoint then
 RatioThre=(HighPoint-close)/(HighPoint-LowPoint)*100
else 
 RatioThre=999;
 
if RatioThre<10 and 
   close<open and 
   close[1]>open[1] and 
   close<close[1]-1/2*(close[1]-open[1])
then ret=1;

end;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/高檔量縮收黑.xs

```xs
{@type:sensor}
input:DownPercent(4);  setinputname(1,"當期下跌幅度");
input:Ratio(20);       setinputname(2,"量縮程度%");
input:TieDays(3);      setinputname(3,"量縮持續期數");
input:UpTrendDays(20); setinputname(4,"累計上漲期數");
input:RaisingRatio(20);setinputname(5,"累計上漲幅度");

settotalbar(3);
setbarback(UpTrendDays+TieDays);

if Close[TieDays] >  close[UpTrendDays+TieDays-1] * (1+RaisingRatio/100) then
begin
  if Close< high[TieDays] * (1 - DownPercent/100) and 
     volume[TieDays] > volume *(1+Ratio/100) 
  then ret=1;
end;
```

---


---

## 腳本檔案: 警示/3.出場常用警示/高檔雙死亡交叉.xs

```xs
{@type:sensor}
//近三天內ma及macd都發生過死亡交叉
input: FastLength(12); SetInputName(1, "DIF短期期數");
input: SlowLength(26); SetInputName(2, "DIF長期期數");
input: MACDLength(9);  SetInputName(3, "MACD期數");
input: Shortlength(5); setinputname(4,"短期均線期數");
input: Longlength(10); setinputname(5,"長期均線期數");
input: Length(20);     setinputname(6,"設定波段區間"); 
input: Ratio(20);      setinputname(7,"設波段上漲幅度"); 
input: ReactRatio(5);  setinputname(8,"距波段高點的跌幅"); 
input:TXT("建議使用日線"); setinputname(9,"使用說明");

SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 3 + 11);

if close >= lowest(close,Length)* (1+ Ratio/100) and
   close >= (1-ReactRatio/100)*highest(close,Length) then
begin

variable: price(0);  
price  = WeightedClose();
Value1 = XAverage(price, FastLength) - XAverage(price, SlowLength);//DIF
Value2 = XAverage( Value1, MACDLength ) ;//MACD
Value3 = Value1 - Value2 ;//OSC
{===============================================================}
value4=average(close,5);
value5=average(close,10);
value6=value4-value5;
{===============================================================}

condition1 = TrueAny( value3 crosses under 0 ,3);
condition2 = TrueAny( value6 crosses under 0 ,3);

if condition1 and condition2 
then ret=1;

end;
```

---


---

## 腳本檔案: 警示/A股用語/九陰白骨爪.xs

```xs
{@type:sensor}
// 連續9筆K線收黑
//
settotalbar(10);
Ret = TrueAll(close < open, 9);
```

---


---

## 腳本檔案: 警示/A股用語/九陽神功.xs

```xs
{@type:sensor}
// 連續9筆上漲
settotalbar(10);
Ret = TrueAll(Close > Close[1], 9);
```

---


---

## 腳本檔案: 警示/A股用語/出水芙蓉.xs

```xs
{@type:sensor}
{股價長期低於季線 今日帶量突破季線 [僅適用日線] }
input:Length(66); setinputname(1,"計算期間[僅日線有效]");
input:downLength(100); setinputname(2,"長期低於季線的天數");
input:ratio(25); setinputname(3,"突破量超過均量百分比(%)");
input:VLength(20); setinputname(4,"突破幾日均量");
input:TXT("僅適用日線"); setinputname(5,"使用限制");

settotalbar(downLength + 8);
setbarback(maxlist(Length + vLength));

if barfreq <> "D" then return;

value1=average(close,Length);//季線值
value2=average(volume,VLength);//均量值

condition1 = TrueAll(high[1] < value1[1], downLength);

if condition1 and close crosses over value1 and volume > value2* (100+ratio)/100
then ret=1;
```

---


---

## 腳本檔案: 警示/A股用語/回頭高飛.xs

```xs
{@type:sensor}
//開高5%以上，拉回又再拉漲停
settotalbar(3);

condition1  =  (Close  =  GetField("漲停價", "D"));
condition2  =  (GetField("Open", "D") > GetField("RefPrice", "D") *1.05);
condition3  =  (GetField("Low", "D") < GetField("Open", "D"));
condition4  =   close > close[1];

if condition1 and condition2 and condition3 and condition4 then ret=1;
```

---


---

## 腳本檔案: 警示/A股用語/斷頭鍘刀.xs

```xs
{@type:sensor}
input:ShortLength(5); setinputname(1,"短期均線期數");
input:MidLength(20); setinputname(2,"中期均線期數");
input:LongLength(60); setinputname(3,"長期均線期數");

settotalbar(8);
setbarback(maxlist(ShortLength,MidLength,LongLength));

value1=average(close,ShortLength);
value2=average(close,MidLength);
value3=average(close,LongLength);

if close crosses below value1 and 
   close crosses below value2 and 
   close crosses below value3 
then ret=1;
```

---


---

## 腳本檔案: 警示/A股用語/死蜘蛛.xs

```xs
{@type:sensor}
input:ShortLength(5); setinputname(1,"短期均線期數");
input:MidLength(20); setinputname(2,"中期均線期數");
input:LongLength(60); setinputname(3,"長期均線期數");

settotalbar(3);
setbarback(maxlist(ShortLength,MidLength,LongLength));

value1=average(close,ShortLength);
value2=average(close,MidLength);
value3=average(close,LongLength);


condition1  = value1>close;
condition2  = close[1]>value3;

value4=maxlist(value1,value2,value3);
value5=minlist(value1,value2,value3);
value6=(value4-value5)/value4;

condition3 =  value6<0.02;

if condition1 and condition2 and condition3 then ret=1;
```

---


---

## 腳本檔案: 警示/A股用語/殺跌波型.xs

```xs
{@type:sensor}
//黑三兵
input:TXT("請使用1分鐘線"); setinputname(1,"使用方法");

settotalbar(5);

if    ( open - close ) > (high -low) * 0.75 and 
      ( open[1] - close[1] ) > (high[1] -low[1]) * 0.75 and
      ( open[2] - close[2] ) > (high[2] -low[2]) * 0.75 and
      close < close[1] and close[1] < close[2] 
then ret=1;
```

---


---

## 腳本檔案: 警示/A股用語/池塘底.xs

```xs
{@type:sensor}
input:Length(40); setinputname(1,"計算期數");
input:inter(10); setinputname(2,"選擇過去某一期");

settotalbar(8);
setbarback(maxlist(Length,inter));

value1=absvalue(close-close[inter]);
value2=value1/close;
value3=average(value2,length);//本日收盤價與前第inter日之收盤價之差的移動平均
value4=average(volume,20);

condition1 = value3<0.01;
condition2 =  close crosses above highest(high[1],length) ;
condition3 =  volume/value4>1.2;

if condition1 and condition2 and condition3 then ret=1;
```

---


---

## 腳本檔案: 警示/A股用語/瀑布波型.xs

```xs
{@type:sensor}
settotalbar(3);
setbarback(30);
if close[1] > lowest(close,30) * 1.2 and 
   (high-low)> close * 0.035 and 
   (close-low)> close * 0.01 
then ret=1;
```

---


---

## 腳本檔案: 警示/A股用語/火箭攻擊.xs

```xs
{@type:sensor}
settotalbar(3);
IF CLOSE >=  CLOSE[1] * 1.015 and close=high and volume>volume[1]
then ret=1;
```

---


---

## 腳本檔案: 警示/A股用語/螞蟻功.xs

```xs
{@type:sensor}
//延著均線前進
input:Length(10); setinputname(1,"均線計算期數");
input:Length1(5); setinputname(2,"沿均線前進的期數");
input:Ratio(2); setinputname(3,"沿均線的範圍定義%");

settotalbar(maxlist(Length,Length1) + 3);

variable:x(0);
variable:count(0); count=0;

value1=average(close,Length);

for x=Length-1 downto 0
begin

	if value1[x] >= close[x]  and value1[x]*100 <=  (100+ratio) *Close
	then count += 1;

end;
if count >= Length1 then ret=1;
```

---


---

## 腳本檔案: 警示/ETF策略/BBand翻多.xs

```xs
{@type:sensor}
input:Length(20,"天數");
input:Up(1,"上");
input:Down(1,"下");
input:Threshold(1,"觸發標準");

variable:up1(0),down1(0),mid1(0),bbandwidth(0);

up1 = bollingerband(Close, Length, absvalue(Up));
down1 = bollingerband(Close, Length, -1 * absvalue(Down));
mid1 = (up1 + down1) / 2;

bbandwidth = 100 * (up1 - down1) / mid1;

if bbandwidth crosses above Threshold then ret = 1;
```

---


---

## 腳本檔案: 警示/ETF策略/ETF乖離反轉作多買進訊號.xs

```xs
{@type:sensor}
input:Length(20); setinputname(1,"計算期數");
input:Ratio(21); setinputname(2,"乖離%");

variable:KPrice(0);
if close/average(close,Length)<= 1-Ratio/100 then KPrice = H;
if Close crosses over KPrice
then ret=1 ;
```

---


---

## 腳本檔案: 警示/ETF策略/KO買進訊號.xs

```xs
{@type:sensor}
Input: Length1(34, "短天期");
Input: Length2(55, "長天期");
variable: ko(0);   

ko = callfunction("KO成交量擺盪指標", Length1, Length2);

value1=average(ko,3);
value2=average(ko,13);

if value1 crosses over value2
and linearregangle(close,5)>20
then ret=1;
```

---


---

## 腳本檔案: 警示/ETF策略/KST趨勢確認策略.xs

```xs
{@type:sensor}
variable:kst(0);
 
kst=callfunction("KST確認指標");

if kst crosses over -50 then ret=1;
```

---


---

## 腳本檔案: 警示/ETF策略/OBV買進訊號.xs

```xs
{@type:sensor}
variable: obvolume(0);

if CurrentBar = 1 then
	obvolume = 0
else begin	
	if close > close[1] then
		obvolume = obvolume[1] + volume
	else begin
		if close < close[1] then
			obvolume = obvolume[1] - volume
		else
			obvolume = obvolume[1];
	end;		
end;

value1=average(obvolume,20);

if obvolume crosses over value1*1.3 then ret=1;
```

---


---

## 腳本檔案: 警示/ETF策略/Q指標買進訊號.xs

```xs
{@type:sensor}
input:t1(10,"計算累積價格變動的bar數");
input:t2(5,"計算價格累積變化量移動平均的期別");
input:t3(20,"計算雜訊的移動平均期別");
variable:Qindicator(0);

Qindicator=callfunction("Q指標",t1,t2,t3);

if linearregangle(Qindicator,5)>40
and barslast(linearregangle(Qindicator,5)>45)[1]>20
then ret=1;
```

---


---

## 腳本檔案: 警示/ETF策略/三下影線反轉直上買進訊號.xs

```xs
{@type:sensor}
input: Percent(0.5,"下影線佔股價絕對百分比");

variable:Kprice(0),OCDate(0);

condition1 = (minlist(open,close)-Low) > absvalue(open-close)*2; 
condition2 =  minlist(open, close)  > low* (100 + Percent)/100;

if trueall( condition1 and condition2, 3) then begin
	OCDate = Date;
	Kprice = average(H,3);
end;

if DateDiff(Date,OCDate) <3 and Close crosses over Kprice then ret = 1;
```

---


---

## 腳本檔案: 警示/ETF策略/中長線均線糾結後突破.xs

```xs
{@type:sensor}
input: Shortlength(10,"短期均線期數");
input: Midlength(20,"中期均線期數");
input: Longlength(40,"長期均線期數");
input: Percent(2,"均線糾結區間%");
input: Volpercent(20,"放量幅度%");//帶量突破的量是超過最長期的均量多少%

variable: shortaverage(0);
variable: midaverage(0);
variable: Longaverage(0);

if volume > average(volume,Longlength) * (1 + volpercent * 0.01) and volume > 1000 then
begin
	shortaverage = average(close,Shortlength);
	midaverage = average(close,Midlength);
	Longaverage = average(close,Longlength);
	
	value2=  maxlist(shortaverage,midaverage,Longaverage );
	value3=  minlist(shortaverage,midaverage,Longaverage );
	
	if close crosses over value2
	and (value2-value3)*100 < Percent*close 
	then ret=1;
end;
```

---


---

## 腳本檔案: 警示/ETF策略/基金投資大跌後的止跌訊號.xs

```xs
{@type:sensor}
if (open[2] - close[2] ) > (high[2] -low[2]) * 0.75
//前前期出黑K棒
and close[2] < close[3]-(high[3]-low[3])
//跌勢擴大
and ( close - open ) > (high -low) * 0.75
//當期收紅K棒
and close> close[2]					
//收復黑棒收盤價
and close[1] <= close[2] and close[1] < open
//前低收盤為三期低點
and close[40] > close[1]*1.05
//近四十日跌幅超過5%
then ret=1;
```

---


---

## 腳本檔案: 警示/ETF策略/大盤MFI多頭.xs

```xs
{@type:sensor}
if TSEMFI=1
then ret=1;
```

---


---

## 腳本檔案: 警示/ETF策略/大碗底.xs

```xs
{@type:sensor}
value1=lowestbar(low,100);
value2=lowest(low,100);
value3=highestbar(high,100);
value4=highest(high,100);
 
if value4>value2*1.15
and value3-value1>15
then begin
	if value1>15
	and value2*1.05>close[1]
	and close>close[1]*1.01
	and volume>average(volume[1],15)*1.2
	then ret=1;
end;
```

---


---

## 腳本檔案: 警示/ETF策略/大跌三成之後.xs

```xs
{@type:sensor}
input:n(30,"下跌幅度");
input:period(60,"計算天數");

if close*(1+n/100) < close[period-1] then ret=1;
```

---


---

## 腳本檔案: 警示/ETF策略/大跌後均線黃金交叉.xs

```xs
{@type:sensor}
Input: Length1(5, "短天期");
Input: Length2(20, "長天期");

value1=highest(high,100);

if value1 > close*1.2
and average(close,Length1) crosses over average(close,Length2)
then ret=1;
```

---


---

## 腳本檔案: 警示/ETF策略/大跌後的價量背離.xs

```xs
{@type:sensor}
input:period(10,"計算天數");
input:times(5,"背離次數");

if close[1]*1.2<close[40] //大跌
and countif(c>c[1] xor v>v[1],period) >= times //價漲量縮、價跌量增
and close=highest(close,period) //收近期最高
then ret=1;
```

---


---

## 腳本檔案: 警示/ETF策略/月KD高檔鈍化且日KD黃金交叉.xs

```xs
{@type:sensor}
input: Length_D(9, "日KD期間");
input: Length_M(5, "月KD期間");

variable:rsv_d(0),kk_d(0),dd_d(0);
variable:rsv_M(0),kk_M(0),dd_M(0);

stochastic(Length_D, 3, 3, rsv_d, kk_d, dd_d);
xf_stochastic("M", Length_M, 3, 3, rsv_m, kk_m, dd_m);

if xf_getvalue("M", kk_m, 1) >= 85 and kk_d crosses over dd_d then ret=1;
```

---


---

## 腳本檔案: 警示/ETF策略/烏龜進場法則.xs

```xs
{@type:sensor}
if average(close,3) crosses above average(close,55)
and volume> average(volume,5)
and atr(3) > atr(20)
then ret=1;
```

---


---

## 腳本檔案: 警示/ETF策略/理專DBCD交易法則.xs

```xs
{@type:sensor}
input:length1(10,"短天期"),length2(20,"長天期"),length3(14,"平滑天期");
input:Threshold(-2,"觸發標準");

value1=bias(length1);
value2=bias(length2);
value3=value2-value1;
value4=average(value3,length3);

if value4 crosses over Threshold
then ret=1;
```

---


---

## 腳本檔案: 警示/ETF策略/理專之雙KD向上.xs

```xs
{@type:sensor}
input: Length_D(9, "日KD期間");
input: Length_W(5, "周KD期間");

variable:rsv_d(0),kk_d(0),dd_d(0);
variable:rsv_w(0),kk_w(0),dd_w(0);

stochastic(Length_D, 3, 3, rsv_d, kk_d, dd_d);
xf_stochastic("W", Length_W, 3, 3, rsv_w, kk_w, dd_w);

condition1 = kk_d crosses above dd_d;		// 日KD crosses over
condition2 = xf_GetBoolean("W",xf_crossover("W", kk_w, dd_w),1);	// 周KD crosses over
condition3 = kk_d <= 30;							// 日K 低檔
condition4 = xf_getvalue("W", kk_w, 1) <= 50;		// 周K 低檔
ret = condition1 and condition2 and condition3 and condition4;
```

---


---

## 腳本檔案: 警示/ETF策略/趨勢翻多.xs

```xs
{@type:sensor}
input:Length(20,"計算期間");

LinearReg(close, Length, 0, value1, value2, value3, value4);
//做收盤價20天線性回歸
//value1:斜率、value4:預期值
value5=rsquare(close,value4,20);//算收盤價與線性回歸值的R平方
 
if value1>0 and value1[1]<0 and value5>0.2 then ret=1;
```

---


---

## 腳本檔案: 警示/ETF策略/週線二連紅之後.xs

```xs
{@type:sensor}
if rateofchange(close,2)[1]>0 
and rateofchange(close,2)[2]>0
and close<close[2]*1.07
and close[10]>close*1.15
then ret=1;
```

---


---

## 腳本檔案: 警示/ETF策略/週線反轉法則.xs

```xs
{@type:sensor}
input:rate1(5,"先前週線漲幅");
input:rate2(3,"本週低點跌幅");
input:TXT("僅適用日線","使用限制");

settotalbar(20);

if getfield("high","W")[2]>=getfield("close","W")[3]*(1+rate1/100) 
and low < getfield("close","W")[1]*(1-rate2/100)
then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/今日高點回跌.xs

```xs
{@type:sensor}
input:HighBound(2); setinputname(1,"高點幅度%");
input:Reaction(1); setinputname(2,"回檔預警幅度%");

settotalbar(3);

if GetField("High", "D") > GetField("RefPrice", "D")*(1+0.01*HighBound) and
   Close <=  GetField("High", "D")*(1-0.01*Reaction) then
   ret = 1;
```

---


---

## 腳本檔案: 警示/價量指標/價創近期新低量創新高.xs

```xs
{@type:sensor}
input: Price(close); setinputname(1,"比較價別");
input: Length(20); setinputname(2,"近期期數");

settotalbar(3);
setbarback(Length);

if  Price < lowest(low[1] ,Length) and 
    volume > highest(volume[1],length) then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/價量同創近期新低.xs

```xs
{@type:sensor}
input: Price(close); setinputname(1,"比較價別");
input: Length(20); setinputname(2,"近期期數");

settotalbar(3);
setbarback(Length);

if  Price < lowest(low[1] ,Length) and 
    volume < lowest(volume[1],length) then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/價量同創近期新高.xs

```xs
{@type:sensor}
input: Price(close); setinputname(1,"比較價別");
input: Length(20); setinputname(2,"近期期數");

settotalbar(3);
setbarback(Length);

if  Price > highest(high[1] ,Length) and 
    volume > highest(volume[1],length) then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/即將漲停.xs

```xs
{@type:sensor}
input: Percent(1);  setinputname(1,"距離漲停百分比");

settotalbar(3);

if close > GetField("漲停價", "D")*(1-Percent/100) then ret =1;
```

---


---

## 腳本檔案: 警示/價量指標/即將跌停.xs

```xs
{@type:sensor}
input: Percent(1);  setinputname(1,"距離跌停百分比");

settotalbar(3);

if close < GetField("跌停價", "D")*(1+Percent/100) then ret =1;
```

---


---

## 腳本檔案: 警示/價量指標/多方人氣表態.xs

```xs
{@type:sensor}
settotalbar(3);
if Close > highD(1) and GetField("Volume", "D")>  GetField("Volume", "D")[1] then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/帶量上影線.xs

```xs
{@type:sensor}
settotalbar(5);
if high - maxlist(open,close) > absvalue(open-close)*2 and
    Volume > maxlist(volume[1],volume[2],volume[3]) then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/帶量下影線.xs

```xs
{@type:sensor}
settotalbar(5);
if minlist(open,close) - low > absvalue(open-close)*2 and
    Volume > Maxlist(volume[1],volume[2],volume[3]) then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/成交量突破N倍均量.xs

```xs
{@type:sensor}
input: length(20);  setinputname(1,"均量期數");
input: VolumeXtime(3);  setinputname(2,"量增倍數");

settotalbar(3);
setbarback(Length);

if volume > Average( volume[1],length)* VolumeXtime then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/成交量突破均量.xs

```xs
{@type:sensor}
input: length(20);  setinputname(1,"均量期數");
input: confirmVolume(500);  setinputname(2,"突破均量張數");

settotalbar(3);
setbarback(Length);

if volume > Average( volume[1],length) +confirmVolume then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/步步高升.xs

```xs
{@type:sensor}
settotalbar(3);
if volume > volume[1]     and 
   volume[1] > volume[2]  and
   close > close[1]       and   
   close[1] > close[2]    and 
   close > open and 
   close[1] > open[1] and 
   close[2] > open[2]
then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/漲停回頭.xs

```xs
{@type:sensor}
settotalbar(3);
If Close[1] = GetField("漲停價", "D") And q_Last < GetField("漲停價", "D") Then ret = 1;
```

---


---

## 腳本檔案: 警示/價量指標/漲停鎖住.xs

```xs
{@type:sensor}
settotalbar(3);
If Close = GetField("漲停價", "D") And q_AskSize <=0 Then ret = 1;
```

---


---

## 腳本檔案: 警示/價量指標/爆量長紅.xs

```xs
{@type:sensor}
settotalbar(8);
if volume >  Average(volume[1],5)  *3    and 
 ( close - open ) >( high -low ) * 0.75  and 
   close > open + (high[1]- low[1])
then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/爆量長黑.xs

```xs
{@type:sensor}
settotalbar(8);
if volume >  Average(volume[1],5)  *3    and 
 ( open - close ) >( high -low ) * 0.75  and 
   open > close  + (high[1]- low[1])
then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/當日時段區間價突破.xs

```xs
{@type:sensor}
input:initialtime(090000); setinputname(1,"起算時間HHmmss");
input:timeline(100000);   setinputname(2,"截止時間HHmmss");
input:CloseAtHigh(false); setinputname(3,"收盤價亦須創新高");
input:TXT1("限用分鐘線"); setinputname(4,"使用限制");

settotalbar(50);

if barfreq<> "Min" then return;
variable: intervalhigh(0);

if date <> date[1] then  intervalhigh = 0; 

if time >= initialtime and time <= timeline then 
begin
  intervalhigh = maxlist(high,intervalhigh);
end;

if time > timeline then
begin
  if CloseAtHigh then  
    Ret = IFF(close > intervalhigh, 1, 0)
  else  
    Ret = IFF(high > intervalhigh, 1, 0); 
end;
```

---


---

## 腳本檔案: 警示/價量指標/當日時段區間價跌破.xs

```xs
{@type:sensor}
input:initialtime(090000); setinputname(1,"起算時間HHmmss");
input:timeline(100000);   setinputname(2,"截止時間HHmmss");
input:CloseAtLow(false); setinputname(3,"收盤價亦須創新低");
input:TXT1("限用分鐘線"); setinputname(4,"使用限制");

settotalbar(50);

if barfreq<> "Min" then return;

variable: intervallow(99999999);

if date <> date[1] then intervallow = 99999999;

if time >= initialtime and time <= timeline then 
begin
  intervallow = minlist(low,intervallow);
end;

if time >timeline then
begin
  if CloseAtLow  then  
	Ret = IFF(close < intervallow, 1, 0)
  else  
	Ret = IFF(low < intervallow, 1, 0);
end;
```

---


---

## 腳本檔案: 警示/價量指標/當日漲幅預警.xs

```xs
{@type:sensor}
input:AlertChangeRatio(3); setinputname(1,"預警幅度%");
settotalbar(3);
If q_PriceChangeRatio > AlertChangeRatio Then ret = 1;
```

---


---

## 腳本檔案: 警示/價量指標/當日跌幅預警.xs

```xs
{@type:sensor}
input:AlertChangeRatio(3); setinputname(1,"預警幅度%");
settotalbar(3);
If q_PriceChangeRatio < AlertChangeRatio*-1 Then ret = 1;
```

---


---

## 腳本檔案: 警示/價量指標/當日量突破.xs

```xs
{@type:sensor}
input:initialtime(090000); setinputname(1,"起算時間HHmmss");
input:timeline(100000);   setinputname(2,"截止時間HHmmss");
settotalbar(50);
variable: intervalhighv(0);
variable: keyprice(0);

if date <> date[1] then  intervalhighv =0 ; 

if time >= initialtime and time <= timeline then
begin 
   intervalhighv = maxlist(volume,intervalhighv ); 
   keyprice =close;
end;

if volume > intervalhighv and time >timeline and
   close > keyprice  and close>=open then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/當日量跌破.xs

```xs
{@type:sensor}
input:initialtime(090000); setinputname(1,"起算時間HHmmss");
input:timeline(100000);   setinputname(2,"截止時間HHmmss");
settotalbar(50);
variable: intervalhighv(0);
variable: keyprice(0);

if date <> date[1] then  intervalhighv =0 ; 

if time >= initialtime and time <= timeline then
begin 
   intervalhighv = maxlist(volume,intervalhighv ); 
   keyprice =close;
end;

if volume > intervalhighv and time >timeline and
   close < keyprice  and close>=open then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/當日開盤跳空開低.xs

```xs
{@type:sensor}
input: UseQuote(True); setinputname(1,"使用即時價欄位");
input: Gap(1.5); setinputname(2,"跳空百分比(%)");
settotalbar(3);
if UseQuote then 
	Ret = IFF(100*(GetField("RefPrice", "D") -GetField("Open", "D")) > GetField("RefPrice", "D")*Gap, 1, 0)
else 
	Ret = IFF(date <> date[1] and 100*(close[1] -open) > close[1]*Gap, 1, 0);
```

---


---

## 腳本檔案: 警示/價量指標/當日開盤跳空開高.xs

```xs
{@type:sensor}
input: UseQuote(True); setinputname(1,"使用即時價欄位");
input: Gap(1.5); setinputname(2,"跳空百分比(%)");
settotalbar(3);
if UseQuote then 
	Ret = IFF(100*(GetField("Open", "D") -GetField("RefPrice", "D")) > GetField("RefPrice", "D")*Gap, 1, 0)
else 
	Ret = IFF(date <> date[1] and 100*(open - close[1]) > close[1]*Gap, 1, 0);
```

---


---

## 腳本檔案: 警示/價量指標/當期成交量倍增.xs

```xs
{@type:sensor}
input: VolumeXtime(3);   setinputname(1,"量增倍數");
settotalbar(3);
if volume > volume[1] * VolumeXtime then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/空頭部隊進攻.xs

```xs
{@type:sensor}
settotalbar(25);
if low < lowD(1) and GetField("Volume", "D")>  GetField("Volume", "D")[1]  then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/股價創近期新低.xs

```xs
{@type:sensor}
input: Price(close); setinputname(1,"比較價別");
input: Length(20); setinputname(2,"近期期數");
settotalbar(3);
setbarback(Length);
if  Price < Lowest(Low[1] ,Length) then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/股價創近期新高.xs

```xs
{@type:sensor}
input: Price(close); setinputname(1,"比較價別");
input: Length(20); setinputname(2,"近期期數");
settotalbar(3);
setbarback(Length);
if  Price > highest(high[1] ,Length) then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/跌停回頭.xs

```xs
{@type:sensor}
settotalbar(3);
If Close[1] = GetField("跌停價", "D") And Close> GetField("跌停價", "D") Then ret = 1;
```

---


---

## 腳本檔案: 警示/價量指標/跌停鎖住.xs

```xs
{@type:sensor}
settotalbar(3);
If Close = GetField("跌停價", "D") And q_bidsize <=0 Then ret = 1;
```

---


---

## 腳本檔案: 警示/價量指標/跌跌不休.xs

```xs
{@type:sensor}
settotalbar(5);
if volume > volume[1]     and 
   volume[1] > volume[2]  and
   close < close[1]       and   
   close[1] < close[2]    and 
   close < open and 
   close[1] < open[1] and 
   close[2] < open[2]
then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/連續期間上漲.xs

```xs
{@type:sensor}
input:Length(3); setinputname(1,"連續上漲期數");
settotalbar(Length + 3);
If TrueAll(Close > Close[1],Length) then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/連續期間下跌.xs

```xs
{@type:sensor}
input:Length(3); setinputname(1,"連續下跌期數");
settotalbar(Length + 3);
If TrueAll(Close < Close[1],Length) then ret=1;
```

---


---

## 腳本檔案: 警示/價量指標/開高帶量走低.xs

```xs
{@type:sensor}
Input: AmountThre(2000); setinputname(1,"開高量(萬)");
variable: initialAmount(0);
variable: intrabarpersist XDate(0);
settotalbar(25);
if Date > XDate then
  begin
	XDate = Date;
	initialAmount = (High+low)/2 * volume/10; //計算K棒成交金額
	if Open > Close[1] and
       (open - close) > (high -low) * 0.75 and 
	   initialAmount > AmountThre then ret = 1;
  end;
```

---


---

## 腳本檔案: 警示/出場訊號/emprical指標賣出訊號.xs

```xs
{@type:sensor}
input:period(20),delta(0.1),fraction(0.1);
variable: price(0),gamma(0),alpha(0),beta(0),BP(0),mean(0),peak(0),valley(0)
,avgpeak(0),avgvalley(0);

price=(h+l)/2;

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if GetFieldDate("主力買賣超張數") <> 0 then
	Z=0 
else 
	Z=1;
beta=cosine(360/period);
gamma=1/cosine(720*delta/period);
alpha=gamma-squareroot(gamma*gamma-1);
BP=0.5*(1-alpha)*(price-price[2])
+beta*(1+alpha)*BP[1]-alpha*BP[2];
mean=average(bp,2*period);
peak=peak[1];
valley=valley[1];
if bp[1]>bp and bp[1]>bp[2] then peak=bp[1];
if bp[1]<bp and bp[1]<bp[2] then valley=bp[1];
avgpeak=average(peak,50);
avgvalley=average(valley,50);
value1=GetField("主力買賣超張數")[Z];
if mean crosses under avgpeak 
and trueall(value1<0,3)
then ret=1;
```

---


---

## 腳本檔案: 警示/出場訊號/近幾日總是收黑K.xs

```xs
{@type:sensor}
if countif(close<open,7)>=5
//過去七天有五天以上收黑
and lowest(close,90)*1.4<close
//過去九十天漲幅超過四成
and lowest(close,10)*1.2<close
//過去十天有急拉過
and volume*1.2<average(volume,20)
//成交量低於二十日均量的兩成
then ret=1;
```

---


---

## 腳本檔案: 警示/出場訊號/開盤委賣暴增.xs

```xs
{@type:sensor}
if close>close[90]*1.3 then begin
//先前有一定的漲幅
	value1=GetField("開盤委買","D");
	value2=GetField("開盤委賣","D");
	value3=value2-value1;
	if trueall(absvalue(value3[1])<250,10)
	//近十日開盤委買與開盤委賣張數差不多
	and value3>=500
	//今日開盤委賣比開盤委買多出500張以上
	and close<close[1]
	//收盤比前一日下跌
	and close<low*1.01
	//收盤接近當日最低價
	then ret=1;
end;
```

---


---

## 腳本檔案: 警示/技術分析/45度切線突破.xs

```xs
{@type:sensor}
input: period(20,"計算區間");
value1=rateofchange(close,period);
//計算區間漲跌幅
value2=arctangent(value1/period*100);
//計算上漲的角度
if value2 crosses over 45
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/ADX形成上昇趨勢.xs

```xs
{@type:sensor}
input: Length(14, "期數"), Threshold(25, "穿越值");

variable: pdi_value(0), ndi_value(0), adx_value(0);

settotalbar(maxlist(Length,6) * 13 + 8);

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if GetFieldDate("主力買賣超張數") <> 0 then
	Z=0 
else 
	Z=1;

DirectionMovement(Length, pdi_value, ndi_value, adx_value);

value1=GetField("主力買賣超張數")[Z];
if tselsindex(10,8)[Z]=1
and value1>300
and adx_value Crosses Above Threshold
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/ADX趨勢成形.xs

```xs
{@type:sensor}
// ADX趨勢成形
//
input: Length(14), Threshold(25);

variable: pdi_value(0), ndi_value(0), adx_value(0);

settotalbar(maxlist(Length,6) * 13 + 8);

SetInputName(1, "期數");
SetInputName(2, "穿越值");

DirectionMovement(Length, pdi_value, ndi_value, adx_value);

Ret = adx_value Crosses Above Threshold;
```

---


---

## 腳本檔案: 警示/技術分析/ATR通道突破策略.xs

```xs
{@type:sensor}
input:period(20,"計算truerange的區間");

value1=average(truerange,period);
value2=average(close,period)+2*value1;

if close crosses over value2 then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/CCI超買.xs

```xs
{@type:sensor}
// CCI超買
//
Input: Length(14), AvgLength(9), Overbought(100);
Variable: cciValue(0), cciMAValue(0);

SetTotalBar(maxlist(AvgLength + Length + 1,6) + 11);

SetInputName(1, "期數");
SetInputName(2, "平滑期數");
SetInputName(3, "超買值");

cciValue = CommodityChannel(Length);
cciMAValue = Average(cciValue, AvgLength);

Ret = cciMAValue Crosses Above OverBought;
```

---


---

## 腳本檔案: 警示/技術分析/CCI超賣.xs

```xs
{@type:sensor}
// CCI超賣
//
Input: Length(14), AvgLength(9), OverSold(-100);
Variable: cciValue(0), cciMAValue(0);

SetTotalBar(maxlist(AvgLength + Length + 1,6) + 11);

SetInputName(1, "期數");
SetInputName(2, "平滑期數");
SetInputName(3, "超賣值");

cciValue = CommodityChannel(Length);
cciMAValue = Average(cciValue, AvgLength);

Ret = cciMAValue Crosses Below OverSold;
```

---


---

## 腳本檔案: 警示/技術分析/DIF-MACD由正轉負.xs

```xs
{@type:sensor}
// DIF-MACD翻負
//
input: FastLength(12), SlowLength(26), MACDLength(9);
variable: difValue(0), macdValue(0), oscValue(0);

SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 3 + 8);

SetInputName(1, "DIF短期期數");
SetInputName(2, "DIF長期期數");
SetInputName(3, "MACD期數");

MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);

Ret = oscValue Crosses Below 0;
```

---


---

## 腳本檔案: 警示/技術分析/DIF-MACD由負轉正.xs

```xs
{@type:sensor}
// DIF-MACD翻正
//
input: FastLength(12), SlowLength(26), MACDLength(9);
variable: difValue(0), macdValue(0), oscValue(0);

SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 3 + 8);

SetInputName(1, "DIF短期期數");
SetInputName(2, "DIF長期期數");
SetInputName(3, "MACD期數");

MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);

Ret = oscValue Crosses Above 0;
```

---


---

## 腳本檔案: 警示/技術分析/DIF-MACD轉正買進訊號.xs

```xs
{@type:sensor}
{L.J.R. Sep.2014}
// DIF-MACD翻正
//
input: FastLength(12), SlowLength(26), MACDLength(9);
variable: difValue(0), macdValue(0), oscValue(0);

SetInputName(1, "DIF短期期數");
SetInputName(2, "DIF長期期數");
SetInputName(3, "MACD期數");

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if GetFieldDate("主力買賣超張數") <> 0 then
	Z=0 
else 
	Z=1;

MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);

value1=GetField("主力買賣超張數")[Z];
if oscValue Crosses Above 0
and trueall(value1>300,3)
and tselsindex(10,8)[Z]=1
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/MACD死亡交叉.xs

```xs
{@type:sensor}
// MACD 死亡交叉 (dif向下穿越macd)
//
input: FastLength(12), SlowLength(26), MACDLength(9);
variable: difValue(0), macdValue(0), oscValue(0);

SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 3 + 8);

SetInputName(1, "DIF短期期數");
SetInputName(2, "DIF長期期數");
SetInputName(3, "MACD期數");

MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);

Ret = difValue Crosses Below macdValue;
```

---


---

## 腳本檔案: 警示/技術分析/MACD黃金交叉.xs

```xs
{@type:sensor}
// MACD 黃金交叉 (dif向上穿越macd)
//
input: FastLength(12), SlowLength(26), MACDLength(9);
variable: difValue(0), macdValue(0), oscValue(0);

SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 3 + 8);

SetInputName(1, "DIF短期期數");
SetInputName(2, "DIF長期期數");
SetInputName(3, "MACD期數");

MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);

Ret = difValue Crosses Above macdValue;
```

---


---

## 腳本檔案: 警示/技術分析/MFO資金流震盪指標.xs

```xs
{@type:sensor}
input:period(20,"計算天期");

if range <> 0 and range[1] <> 0 then
	value1= ((high-low[1])-(high[1]-low))/((high-low[1])+(high[1]-low))*volume;
if summation(volume,period) <> 0 then
	value2= summation(value1,period)/summation(volume,period);

if value2 crosses over -0.5 then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/MTM往上穿過0.xs

```xs
{@type:sensor}
// MTM往上穿越0軸
//
Input: Length(10);

settotalbar(maxlist(Length,6) + 8);

SetInputName(1, "期數");

Ret = Momentum(Close, Length) Crosses Above 0;
```

---


---

## 腳本檔案: 警示/技術分析/MTM突破零且投信買超.xs

```xs
{@type:sensor}
//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if GetFieldDate("主力買賣超張數") <> 0 then
	Z=0 
else 
	Z=1;
	
if momentum(close,10) crosses over 0
and GetField("投信買賣超")[Z]>1000 
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/MTM背離.xs

```xs
{@type:sensor}
value1=momentum(close,10);
if linearregslope(close,6)<0
and linearregslope(value1,6)>0
and close*1.2<close[20]
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/MTM跌破0.xs

```xs
{@type:sensor}
// MTM往下跌破0軸
//
Input: Length(10);

settotalbar(maxlist(Length,6) + 8);

SetInputName(1, "期數");

Ret = Momentum(Close, Length) Crosses Below 0;
```

---


---

## 腳本檔案: 警示/技術分析/Pivot Point短多策略.xs

```xs
{@type:sensor}
variable:pivot(0);

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if currenttime > 180000 
or currenttime < 083000 then 
	Z =0 
else 
	Z=1;
	
pivot=(high+low+close)/3;
value1=2*pivot-low;

if close=value1
and tselsindex(10,6)[Z]=1
and volume>=1000
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/RSI低檔背離.xs

```xs
{@type:sensor}
// RSI由下往上, 與價格趨勢背離
//
Input: RSILength(6), Threshold(20), Region(5);
variable: rsiValue(0);

settotalbar(maxlist(RSILength,6) * 8 + 8);

SetInputName(1, "期數");
SetInputName(2, "低檔值");
SetInputName(3, "日期區間");

RSIValue = RSI(Close, RSILength);
If RSIValue Crosses Above Threshold and
   RSIValue >= Highest(RSIValue, Region) and 
   Close <= Lowest(Close, Region) then
   Ret = 1;
```

---


---

## 腳本檔案: 警示/技術分析/RSI死亡交叉.xs

```xs
{@type:sensor}
// RSI短天期往下穿越長天期
//
input: ShortLength(6), LongLength(12);

settotalbar(maxlist(ShortLength,6) * 8 + 8);

SetInputName(1, "短期期數");
SetInputName(2, "長期期數");

Ret = RSI(Close, ShortLength) Crosses Below RSI(Close, LongLength);
```

---


---

## 腳本檔案: 警示/技術分析/RSI背離.xs

```xs
{@type:sensor}
value1=rsi(close,12);
if linearregslope(close,6)<0
and linearregslope(value1,6)>0
and close*1.2<close[20]
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/RSI高檔背離.xs

```xs
{@type:sensor}
// RSI由高檔區往下, 與價格趨勢背離
//
Input: RSILength(6), Threshold(80), Region(5);
variable: rsiValue(0);

settotalbar(maxlist(RSILength,6) * 8 + 8);

SetInputName(1, "期數");
SetInputName(2, "高檔值");
SetInputName(3, "日期區間");

RSIValue = RSI(Close, RSILength);
If RSIValue Crosses Below Threshold and
   RSIValue < Lowest(RSIValue, Region) and 
   Close >= Highest(Close, Region) then
	Ret = 1;
```

---


---

## 腳本檔案: 警示/技術分析/RSI黃金交叉.xs

```xs
{@type:sensor}
// RSI短天期往上穿越長天期
//
input: ShortLength(6), LongLength(12);

settotalbar(maxlist(ShortLength,LongLength,6) * 8 + 8);

SetInputName(1, "短期期數");
SetInputName(2, "長期期數");

Ret = RSI(Close, ShortLength) Crosses Above RSI(Close, LongLength);
```

---


---

## 腳本檔案: 警示/技術分析/U型底.xs

```xs
{@type:sensor}
input:in1(20,"底部期數下限"),in2(0.5,"標準差放寬倍數"),in3(20,"連續下降趨勢天數");
variable:KP(0),HSV(0);
value1=standarddev(weightedclose,10,2);//計算一定期數標準差
value2=average(value1,250)*in2;//計算一年標準差
value3=average(C,5);//MA5
value4=average(C,10);//MA10
value5=average(C,20);//MA20
if value1 crosses over value2 //若標準差向上跨越一年平均標準差
then begin
	KP=0;
	HSV=0;
end;
if value1>=value2//在連續變動趨勢中
then begin
	if value1>HSV then HSV=value1;//尋找標準差最大點
	if HSV<>HSV[1] then KP=C;//將標準差最大的點之收盤價視為關鍵價
end;
condition2=value1<value2;//標準差小於年均標準差
condition3=trueall(condition2,in1);//連續20期
condition4=value4<value4[1];//MA10為下降趨勢
condition5=trueall(condition4,in3);//連續下降20期
condition7=trueall(not condition4,in3);//連續20期不下降
if not condition5 and condition5[1] then condition6=true;//若連續下降
if C crosses over KP and condition3 and trueall(condition6,round(in3/2,0))
//若收盤價突破關鍵價且期間內標準差小於年均且下降趨勢結束一段時間
then begin
	condition6=false;
	ret=1;//買進
end;
```

---


---

## 腳本檔案: 警示/技術分析/WVAD買進訊號.xs

```xs
{@type:sensor}
//ETF 作多  40天後出場

input:length(14);
variable:wvad(0);
value1=close-open;
value2=high-low;
if high<>low
then value3=value1/value2*volume
else
value3=value3[1];
wvad=summation(value3,length);
if wvad<0
and linearregslope(wvad,5)>0
and linearregslope(wvad,15)<0
and linearregslope(close,20)<0
and GetSymbolField("tse.tw","收盤價","W")
>average(GetSymbolField("tse.tw","收盤價","W"),13)
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/三連陽過前年最高點.xs

```xs
{@type:sensor}
//全部  持有二十天

input:period(500,"創n日新高");
settotalbar(period);

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if GetFieldDate("主力買賣超張數") <> 0 then
	Z=0 
else 
	Z=1;

value1=GetField("強弱指標","D")[Z];
value2=GetField("主力買賣超張數")[Z];
if close crosses over highest(close[1],period)
and trueall(close>close[1],3)
and trueall(value2>0,3)
and tselsindex(10,6)[Z]=1

then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/上昇趨勢確立.xs

```xs
{@type:sensor}
//市值適中的股票 20天出場

input:Length(20); //"計算期間"

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if GetFieldDate("主力買賣超張數") <> 0 then
	Z=0 
else 
	Z=1;
	
LinearReg(close, Length, 0, value1, value2, value3, value4);
//做收盤價20天線性回歸
{value1:斜率,value4:預期值}
value5=rsquare(close,value4,20);//算收盤價與線性回歸值的R平方
value6=GetField("主力買賣超張數")[Z];
if value1> 0 and value5 crosses over 0.2
and trueall(value6>100,3)
and tselsindex(10,8)[Z]=1
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/下跌後的吊人線.xs

```xs
{@type:sensor}

condition1=false;
condition2=false;
condition3=false;
if high<= maxlist(open, close)*1.01	
//條件1:小紅小黑且上影線很小
then condition1=true;
if (close-low)> (open-close)*2 and (close-low)>close*0.02
//條件2:下影線為實體兩倍以上
then condition2=true;
if highest(high,30)>close[1]*1.4
//條件3:近30日來最高點到昨天跌幅超過40%
then condition3=true;
{結果判斷}		
IF		condition1
	and	condition2
	and	condition3
and average(volume,100)>1000
//只計算有量的股票
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/下降趨勢突破.xs

```xs
{@type:sensor}
input:in1(70,"計算區間"),in2(false,"嚴格模式");
//尋找不同區間大小下目測所認為的高點。

value1=highest(H,in1);//找出一定區間的高點
if value1>value1[1] then value2=value1;
//如果高點變高則保留高點，這樣做的原因是可以找到一波下降之後的高點
condition1 = value2=value2[1];
//條件:保留之高點維持(階梯的平台)
condition2 = trueall(condition1,in1);
//在計算區間內高點都沒有變 

if condition2 and not condition2[1]

then begin
	value6=value5;
	value5=value4;
	value4=value3;
	value3=value2;
end;
condition3 = 
	value3-value2<value4-value3 
	and value4-value3<value5-value4 
	and (value5-value4<value6-value5 or not in2)//嚴格模式多判斷一階
	and value3-value2>0
	;//平台的高度一階比一階低
if condition3[1] and not condition3 then ret=1;
	//此秩序被打破時進場
```

---


---

## 腳本檔案: 警示/技術分析/中小型股趨勢成型.xs

```xs
{@type:sensor}

// ADX趨勢成形
// 用有量的中小型股，5%停利，5%停損
 
if GetSymbolField("tse.tw","收盤價")
> average(GetSymbolField("tse.tw","收盤價"),10) 
//大盤OK
then begin
input: Length(14,"期數"), Threshold(25,"穿越值");
 
variable: pdi_value(0), ndi_value(0), adx_value(0);
 
  
DirectionMovement(Length, pdi_value, ndi_value, adx_value);
 
if adx_value Crosses Above Threshold
//adx趨勢成形
and pdi_value>ndi_value
//+DI>-DI
and close <close[30]
then ret=1;
end;
```

---


---

## 腳本檔案: 警示/技術分析/主力押大注.xs

```xs
{@type:sensor}
//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if GetFieldDate("主力買賣超張數") <> 0 then
	Z=0 
else 
	Z=1;
	
value1=GetField("主力買賣超張數")[Z];
if value1=highest(value1,120)
and trueall(value1>0,3)
and volume>500
and close>close[1]*1.03
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/主力收集完開始拉.xs

```xs
{@type:sensor}
//中小型股，持股20天
//漲幅3%以上
//爆大量，且一般而言會是月均量1倍以上
//主力近1日買超要相對過去的買超有成長。
//買進家數小於賣出家數

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if GetFieldDate("主力買賣超張數") <> 0 then
	Z=0 
else 
	Z=1;
	
value1=GetField("分公司買進家數","D")[Z];
value2=GetField("分公司賣出家數","D")[Z];
value3=GetField("主力買賣超張數")[Z];
if close>close[1]*1.03
and value3>average(value3,20)
and value1<value2
and volume >2*average(volume,20)
and tselsindex(10,8)[Z]=1
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/主力累計買超比例過門檻.xs

```xs
{@type:sensor}
//作多  中小型股  持有二十天

input: Length(5); setinputname(1,"計算天數");
input:TXT("僅適用日線以上"); setinputname(2,"使用限制");
input:limit1(20);
setinputname(3,"買超佔成交量比例");

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if GetFieldDate("主力買賣超張數") <> 0 then
	Z=0 
else 
	Z=1;
	
variable: b1(0), v1(0),ratio(0);

b1 = summation(GetField("主力買賣超張數")[Z], Length);
v1 = summation(Volume, Length);
ratio=b1/v1*100;
value1=GetField("主力買賣超張數")[Z];
if v1<>0
then 
begin
if ratio>=limit1 and average(volume,20)>1000
and trueall(value1>100,3)
and tselsindex(10,6)[Z]=1
then ret=1;
end;
```

---


---

## 腳本檔案: 警示/技術分析/乖離反轉作多買進訊號.xs

```xs
{@type:sensor}
//用週線  四週後出場
input:Length(20,"計算期數");
input:Ratio(21,"乖離%");
input:TXT("僅適用日線","使用限制");

settotalbar((Length+10)*5);

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if GetFieldDate("主力買賣超張數") <> 0 then
	Z=0 
else 
	Z=1;
	
variable:KPrice(0);
if close <= average(getfield("close","W"),Length) * (1-Ratio/100) then KPrice = getfield("high","W");
value1=GetField("投信買賣超")[Z];
value2=value1*close*1000;
if countif(value2>1000000,3)>2
and close>KPrice and getfield("close","W")[1] < xf_getvalue("W",KPrice,1)
then ret=1 ;
```

---


---

## 腳本檔案: 警示/技術分析/價值股創近年新高.xs

```xs
{@type:sensor}
if close crosses over  highest(close[1],220)
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/共振策略.xs

```xs
{@type:sensor}
input: shortlength(5,"短期均線期數");
input: midlength(20,"中期均線期數");
input: Longlength(60,"長期均線期數");
input: Percent(5,"均線糾結區間%");
input: XLen(6,"均線糾結期數");
variable:sv(0),mv(0),lv(0);
sv = average(close,shortlength);
mv = average(close,midlength);
lv = average(close,Longlength);	
variable: avgh(0),avgl(0),avghlp(0);	
AvgH = maxlist(sv,mv,lv );
AvgL = minlist(sv,mv,lv );
if AvgL > 0 then AvgHLp = 100*AvgH/AvgL -100;

input: Length1(14 , "威廉指標計算天數");
value1 = PercentR(Length1);
if trueAll(AvgHLp < Percent,XLen)
and value1>80
and close>close[1]*1.025
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/布林通道超買訊號.xs

```xs
{@type:sensor}
// 布林通道超買訊號
//
Input: Length(20), UpperBand(2);

settotalbar(Length + 3);

SetInputName(1, "期數");
SetInputName(2, "通道上緣");

Ret = High >= bollingerband(Close, Length, UpperBand);
```

---


---

## 腳本檔案: 警示/技術分析/布林通道超賣訊號.xs

```xs
{@type:sensor}
// 布林通道超賣訊號
//
Input: Length(20), LowerBand(2);

settotalbar(Length + 3);

SetInputName(1, "期數");
SetInputName(2, "通道下緣");

Ret = Low <= bollingerband(Close, Length, -1 * LowerBand);
```

---


---

## 腳本檔案: 警示/技術分析/帶量突破均線.xs

```xs
{@type:sensor}
// 帶量突破均線
//
input: Length(10), VolFactor(2);

settotalbar(3);
setbarback(Length);

SetInputName(1, "期數");
SetInputName(2, "成交量放大倍數");

if close > Average(close, Length) and  close[1] <  Average(close, Length) and
   volume > Average(volume, Length) * VolFactor 
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/帶量跌破均線.xs

```xs
{@type:sensor}
// 帶量跌破均線
//
input: Length(10), VolFactor(2);

settotalbar(3);
setbarback(Length);

SetInputName(1, "期數");
SetInputName(2, "成交量放大倍數");

if close < Average(close, Length) and  close[1] >  Average(close, Length) and
   volume > Average(volume, Length) * VolFactor 
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/底部出大量.xs

```xs
{@type:sensor}
input:period(60);
if close=lowest(close,period)
and volume=highest(volume,period)
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/找起漲點的策略.xs

```xs
{@type:sensor}
Input: Length(20, "期數");
input: UpperBand(2, "通道上緣");
input: lowerband(-2,"通道下緣");
variable:Kprice(0);

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if currenttime > 180000 
or currenttime < 083000 then 
	Z =0 
else 
	Z=1;
	
value1= bollingerband(Close, Length, UpperBand);
value2= bollingerband(Close, Length, lowerBand);
value3=value1-value2;
value4=average(close,20);

if linearregslope(value4,5)>0
and value3>average(value3,20)*1.3
and close[1] crosses over value1
and close>value1
and tselsindex(10,6)[Z] = 1
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/投信天天買  股價天天小漲.xs

```xs
{@type:sensor}
//中小型股  持有二十天

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if GetFieldDate("主力買賣超張數") <> 0 then
	Z=0 
else 
	Z=1;
	
value1=GetField("投信買賣超")[Z];
value2=GetField("主力買賣超張數")[Z];
input:day(8);
if countif(value1>0,day)>=7
//八天裡至少七天投信買超
and countif(close>close[1],day)>=5
//八天裡至少五天上漲
and average(volume,10)<2000
and trueall(value2>0,3)
and tselsindex(10,8)[Z]=1

then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/投信近幾日買超比例高的.xs

```xs
{@type:sensor}
input: pastDays(5); setinputname(1,"計算天數");
input: _BuyRatio(10); setinputname(2,"買超佔比例(%)");
input:TXT("僅適用日線"); setinputname(3,"使用限制");

variable: SumForce(0);
variable: SumTotalVolume(0);

if BarFreq <> "D" then return;

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if GetFieldDate("主力買賣超張數") <> 0 then
	Z=0 
else 
	Z=1;
	
value1=GetField("主力買賣超張數")[Z];
 
SumForce = Summation(GetField("投信買賣超")[Z], pastDays);
sumTotalVolume = Summation(Volume, pastDays);
if SumForce > SumTotalVolume * _BuyRatio/100 
and tselsindex(10,8)[Z]=1
then ret =1;
```

---


---

## 腳本檔案: 警示/技術分析/景氣循環股操作法.xs

```xs
{@type:sensor}
input: shortlength(5); setinputname(1,"短期均線期數");
input: midlength(10); setinputname(2,"中期均線期數");
input: Longlength(20); setinputname(3,"長期均線期數");
input: Percent(2); setinputname(4,"均線糾結區間%");
input: Volpercent(40); setinputname(5,"放量幅度%");//帶量突破的量是超過最長期的均量多少%
variable: shortaverage(0);
variable: midaverage(0);
variable: Longaverage(0);
variable:Kprice(0);
 
if volume > average(volume,Longlength) * (1 + volpercent * 0.01) then
begin
shortaverage = average(close,shortlength);
midaverage = average(close,midlength);
Longaverage = average(close,Longlength);
if Close crosses over maxlist(shortaverage,midaverage,Longaverage) then
begin
value1= absvalue(shortaverage -midaverage);
value2= absvalue(midaverage -Longaverage);
value3= absvalue(Longaverage -shortaverage);
if maxlist(value1,value2,value3)*100 < Percent*Close then Kprice=H;
end;
end;
 
if C crosses above Kprice
//and tselsindex(10,8)=1
 then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/波動放大.xs

```xs
{@type:sensor}
// 波動放大
//
input: Length(20), Percent(7);

settotalbar(3);
setbarback(Length);

SetInputName(1, "期數");
SetInputName(2, "波動幅度%");

Ret = Highest(High, Length) / Lowest(Low, Length) -1 > Percent*0.01;
```

---


---

## 腳本檔案: 警示/技術分析/波動縮小.xs

```xs
{@type:sensor}
// 波動縮小
//
input: Length(20), Percent(7);

settotalbar(3);
setbarback(Length);

SetInputName(1, "期數");
SetInputName(2, "波動幅度%");

Ret = Highest(High, Length) / Lowest(Low, Length) -1 < Percent*0.01;
```

---


---

## 腳本檔案: 警示/技術分析/漲幅警示.xs

```xs
{@type:sensor}
input: Length(5), Percent(3);

settotalbar(3);
setbarback(Length);

SetInputName(1, "計算期數");
SetInputName(2, "累計上漲幅度(%)");

Ret = Rateofchange(Close, Length) > Percent;
```

---


---

## 腳本檔案: 警示/技術分析/潛龍昇天.xs

```xs
{@type:sensor}
input:StartDate(20150301);
input:LowMonth(3);
 
if currentbar =1 and date < startdate then raiseruntimeerror("日期不夠遠");
 
variable:iHigh(0); iHigh=maxlist(iHigh,H);
variable:iLow(100000); iLow=minlist(iLow,L);
variable:hitlow(0),hitlowdate(0);
if iLow = Low then //觸低次觸與最後一次觸低日期
begin
hitlow+=1;
hitlowdate =date;
end;
 
if DateAdd(hitlowdate,"M",1) < Date and//如果自觸低點那天三個月後都沒有再觸低
iHigh/iLow < 1.3 and //波動在三成以內
iHigh = High then
 
//來到設定日期以來最高點
ret =1;
```

---


---

## 腳本檔案: 警示/技術分析/盤整後跳空走高.xs

```xs
{@type:sensor}
//中小型股  停損停利都是5%
input:period(20,"盤整區間");

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if currenttime > 180000 
or currenttime < 083000 then 
	Z =0 
else 
	Z=1;
	
value1=highest(high[1],period);
value2=lowest(low[1],period);

if value1<value2*1.05
and open > high[1]*1.025
and tselsindex(10,7)[Z]=1
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/短期均線突破長期均線.xs

```xs
{@type:sensor}
input: Shortlength(5); setinputname(1,"短期均線期數");
input: Longlength(20); setinputname(2,"長期均線期數");

settotalbar(8);
setbarback(maxlist(Shortlength,Longlength,6));

If Average(Close,Shortlength) crosses over Average(Close,Longlength) then Ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/短期均線跌破長期均線.xs

```xs
{@type:sensor}
input: Shortlength(5); setinputname(1,"短期均線期數");
input: Longlength(20); setinputname(2,"長期均線期數");

settotalbar(8);
setbarback(maxlist(Shortlength,Longlength,6));

If Average(Close,Shortlength) crosses under Average(Close,Longlength) then Ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/突破投信成本線.xs

```xs
{@type:sensor}
//小型股
input: pastDays(3); setinputname(1,"計算天數");
input: _BuyRatio(10); setinputname(2,"買超佔比例(%)");
 
variable: SumAm(0),SumForce(0), SumTotalVolume(0),APrice(0),AVGP(0),Kprice(0),QDate(0);
 
if V[1] <> 0 then
	APrice = GetField("成交金額")[1] / V[1]/1000;
 
SumAm = Summation(GetField("投信買賣超")[1]*APrice, pastDays);
SumForce = Summation(GetField("投信買賣超")[1], pastDays);
 
sumTotalVolume = Summation(Volume[1], pastDays);
 
if SumAm > 30000 and SumForce > SumTotalVolume * _BuyRatio/100 then
begin
Kprice =highest(avgprice,pastDays);
QDate=Date;
end;
 
if DateDiff(Date,QDate) < pastDays+5 and C > Kprice and C[1] < Kprice then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/第一次站上20週均線.xs

```xs
{@type:sensor}
if barfreq<>"W" then return;
if close crosses over average(close,20)
and barslast(close crosses over average(close,20))[1]
>20
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/股價穿越突破三均線.xs

```xs
{@type:sensor}
input: shortlength(5); setinputname(1,"短期均線期數");
input: midlength(10);  setinputname(2,"中期均線期數");
input: Longlength(20); setinputname(3,"長期均線期數");

settotalbar(3);
setbarback(maxlist(shortlength,midlength,Longlength));

variable: shortaverage(0);
variable: midaverage(0);
variable: Longaverage(0);


shortaverage=Average(close,shortlength);
midaverage=Average(close,midlength) ;
Longaverage = Average(close,Longlength); 

if close > maxlist(shortaverage, midaverage, longaverage) and
     open < minlist(shortaverage, midaverage, longaverage)
     then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/股價穿越突破單均線.xs

```xs
{@type:sensor}
input: length(5); setinputname(1,"均線期數");
input: Price(Close); setinputname(2,"價格別");

settotalbar(3);
setbarback(length);

variable: avgValue(0);
avgValue = Average(Price,length);

if close > avgValue and  open < avgValue  then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/股價穿越突破雙均線.xs

```xs
{@type:sensor}
input: shortlength(5); setinputname(1,"短期均線期數");
input: Longlength(20); setinputname(2,"長期均線期數");

settotalbar(3);
setbarback(maxlist(shortlength,Longlength));

variable: Longaverage(0);
variable: shortaverage(0);

Longaverage = Average(close,Longlength);
shortaverage=Average(close,shortlength) ;


if close > maxlist(shortaverage, longaverage) and
     open < minlist(shortaverage, longaverage)
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/股價穿越跌破三均線.xs

```xs
{@type:sensor}
input: shortlength(5); setinputname(1,"短期均線期數");
input: midlength(10); setinputname(2,"中期均線期數");
input: Longlength(20); setinputname(3,"長期均線期數");

settotalbar(3);
setbarback(maxlist(shortlength,midlength,Longlength));

variable: shortaverage(0);
variable: midaverage(0);
variable: Longaverage(0);


shortaverage=Average(close,shortlength);
midaverage=Average(close,midlength) ;
Longaverage = Average(close,Longlength); 

if open > maxlist(shortaverage, midaverage, longaverage) and
   close < minlist(shortaverage, midaverage, longaverage)
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/股價穿越跌破單均線.xs

```xs
{@type:sensor}
input: length(5); setinputname(1,"均線期數");
input: Price(Close);setinputname(2,"價格別");

settotalbar(3);
setbarback(length);

variable: avgValue(0);
avgValue = Average(Price,length);

if close < avgValue and  open > avgValue  then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/股價穿越跌破雙均線.xs

```xs
{@type:sensor}
input: shortlength(5); setinputname(1,"短期均線期數");
input: Longlength(20); setinputname(2,"長期均線期數");

settotalbar(3);
setbarback(maxlist(shortlength,Longlength));

variable: Longaverage(0);
variable: shortaverage(0);

Longaverage = Average(close,Longlength);
shortaverage=Average(close,shortlength) ;

if open > maxlist(shortaverage, longaverage) and
   close < minlist(shortaverage, longaverage)
 then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/股價轉趨活躍.xs

```xs
{@type:sensor}
//小型股

input:day(66);
input:ratio(10);
variable:count(0);
 
setinputname(1,"移動平均天數");
setinputname(2,"超出均值比率");

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if GetFieldDate("主力買賣超張數") <> 0 then
	Z=0 
else 
	Z=1;
	
value1=GetField("總成交次數");
value2=average(value1,day);
value3=GetField("強弱指標")[Z];
value4=average(value3,day);
value5=GetField("外盤均量")[Z];
value6=average(value5,day);
value7=GetField("主動買力")[Z];
value8=average(value7,day);
value9=GetField("開盤委買");
value10=average(value9,day);
count=0;
if value1>=value2*(1+ratio/100)
then count=count+1;
if value3>=value4*(1+ratio/100)
then count=count+1;
if value5>=value6*(1+ratio/100)
then count=count+1;
if value7>=value8*(1+ratio/100)
then count=count+1;
if value9=value10*(1+ratio/100)
then count=count+1;
 
value11=average(count,5);
value12=average(count,20);
if value11 crosses over value12
and value12<2.2
and highest(close,20)<lowest(close,20)*1.1
and tselsindex(10,8)[Z]=1
and GetField("主力買賣超張數")[Z]>100
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/跌幅警示.xs

```xs
{@type:sensor}
input: Length(5), Percent(3);

settotalbar(3);
setbarback(length);

SetInputName(1, "計算期數");
SetInputName(2, "累計下跌幅度(%)");

Ret = RateOfChange(Close, Length) < -1 * Percent;
```

---


---

## 腳本檔案: 警示/技術分析/進入上昇趨勢.xs

```xs
{@type:sensor}

//高ROE股持有20天
input:period(12);
value1=countif(low<lowest(low[1],period),period);
value2=countif(high>highest(high[1],period),period);
value3=value2-value1;
if average(GetSymbolField("tse.tw","收盤價","D"),5)
> average(GetSymbolField("tse.tw","收盤價","D"),20)
then begin
 
if value3 crosses over 4
  
then ret=1;
 
end;
```

---


---

## 腳本檔案: 警示/技術分析/過去N日有多日跳空且未拉回.xs

```xs
{@type:sensor}
//中小型股  停損停利都是5%
input:day(5,"過去N日");
input:lowlimit(2,"符合條件天數");
input:period(20,"盤整區間");

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if currenttime > 180000 
or currenttime < 083000 then 
	Z =0 
else 
	Z=1;
	
value1=highest(high[day],period);
value2=lowest(low[day],period);

if value1<value2*1.05
and countif(high>high[1]
and low>low[1],day)>=lowlimit
and tselsindex(10,8)[Z]=1
then ret=1;
```

---


---

## 腳本檔案: 警示/技術分析/野百合的春天.xs

```xs
{@type:sensor}
//獲利穩定的公司  20天後出場

settotalbar(700);
if getsymbolfield("tse.tw","收盤價")
> average(getsymbolfield("tse.tw","收盤價"),10)
then begin
value4=GetField("總市值");
value5=average(value4,600);
if value4[1]<value5[1]*0.7
and close=highest(close,10)
then ret=1;
end;
```

---


---

## 腳本檔案: 警示/技術分析/開始有人問津.xs

```xs
{@type:sensor}
if average(truerange/close,20)*100<3
and truerange crosses over average(truerange,20)*1.2
and average(volume,30)<600
and close>close[1]*1.025
and close<30
then ret=1;
```

---


---

## 腳本檔案: 警示/抄底策略/大跌後均線糾結後上漲.xs

```xs
{@type:sensor}
input: s1(5,"短期均線期數");
input: s2(10,"中期均線期數");
input: s3(20,"長期均線期數");
input: Percent(2,"均線糾結區間%");
input: Volpercent(25,"放量幅度%");//帶量突破的量是超過最長期的均量多少%

variable: Shortaverage(0);
variable: Midaverage(0);
variable: Longaverage(0);

if volume > average(volume,s3) * (1 + volpercent * 0.01)
//放量25%
and lowest(volume,s3)<1000
//區間最低量小於一千張
and volume>2000
//今日成交量突破2000張
then begin
	Shortaverage = average(close,s1);
	Midaverage = average(close,s2);
	Longaverage = average(close,s3);
	value1= maxlist(Shortaverage,Midaverage,Longaverage) - minlist(Shortaverage,Midaverage,Longaverage);
	
	if  value1*100 < Percent*Close
	and linearregangle(value1,5)<10
	//均線糾結在一起
	and close*1.3<close[40]
	//最近四十個交易日跌了超過三成
	then ret=1; 
end;
```

---


---

## 腳本檔案: 警示/抄底策略/大跌後的低檔五連陽.xs

```xs
{@type:sensor}
if trueall(close>open,5) 
and close*1.4<close[90]
then ret=1;
```

---


---

## 腳本檔案: 警示/抄底策略/大跌後的連續跳空上漲.xs

```xs
{@type:sensor}
if close*1.5<close[40]
//過去四十個交易日跌了超過四成
and countif(open > close[1],5)>=3
//過去五天有三天以上開盤比前一天收盤高
and GetSymbolField("tse.tw","收盤價","D")
>average(GetSymbolField("tse.tw","收盤價","D"),10)
//指數位於十日均線之上
and average(volume,5)>2000
//五日均量大於2000張
then ret=1;
```

---


---

## 腳本檔案: 警示/抄底策略/底部確認.xs

```xs
{@type:sensor}
input:period(200,"天數");
variable: ld(0),hd(0),ldb(0),hdb(0),count(0),x1(0);

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if currenttime > 180000 
or currenttime < 083000 then 
	Z =0 
else 
	Z=1;
	
count=0;
ld=lowest(low,period);
ldb=lowestbar(low,period);
hd=highest(high,period);
hdb=highestbar(high,period);
x1=GetField("總市值","D")[Z];//單位：億

if hdb>ldb and hd>ld*1.4 and ld>=ld[1] and x1>20 then begin
//股價大跌後
	value1=countif((close-open)/open>1.5,ldb);
	//自最低點以來的中長紅K棒數
	if value1>=ldb/5 then count=count+1;
	
	value2=summationif(close>close[1],volume,ldb);
	//自最低點以來的上漲量
	value3=summationif(close<close[1],volume,ldb);
	//自最低點以來的下跌量
	if value2>2*value3 then count=count+1;
	
	value4=nthlowestbar(2,low,ldb);
	//第二個低點的k棒位置
	value5=nthlowestbar(3,low,ldb);
	//第三個低點的K棒位置
	value6=nthlowestbar(4,low,ldb);
	//第四個低點的K棒位置
	if value4>value5 and value5>value6 then count=count+1;
	
	value7=countif(absvalue(close[1]/close-1)/close[1]*100<1 and close<close[1],ldb);
	//自低點以來的小黑棒K棒數
	if value7>0.5*countif(close<close[1],ldb) then count=count+1;
	//小黑k棒佔下跌k棒超過一半

	value8=countif(close>low*1.01,ldb);
	//自低點以來的長下影線天數
	if value8 >=ldb/5 then count=count+1;

	value9=countif(close=high,ldb);
	//自低點以來收最高的天數
	if value9>=ldb/5 then count=count+1;

	if ldb>=5 then count=count+1;
end;

if count[1]>2 and count crosses over 5 then ret=1;
```

---


---

## 腳本檔案: 警示/抄底策略/跌深後的反彈.xs

```xs
{@type:sensor}
input:ratio(10,"近十日最小下跌幅度");

if open*1.025<close[1]//開盤重挫
and close>open //收盤比開盤高
and close*(1+ratio/100)<close[9]
//近十日跌幅超過N%
and low*1.01<open
//開低後又殺低
then ret=1;
```

---


---

## 腳本檔案: 警示/期權策略/快到期了還是價內.xs

```xs
{@type:sensor}
if  q_IOofMoney>0 
and datediff(GetSymbolInfo("到期日"),date)<10
and datediff(GetSymbolInfo("到期日"),date)>0
then ret=1;
```

---


---

## 腳本檔案: 警示/期權策略/期指短打.xs

```xs
{@type:sensor}
if barfreq<>"Min" or barinterval<>1 then raiseruntimeerror("頻率請用1分K");

variable:l1(0),l2(0),l3(0),l4(0),l5(0),l6(0),l7(0),l8(0),l9(0),l10(0),x(0),i(0), base(0);
variable:day(3);

if GetField("日期","Tick") <> currentdate then return;
if time = 091500 then begin
	base = GetField("收盤價","Tick");   // 基準點
	x = 0;
	for i=1 to day
		x=highd(i)-lowd(i)+x;
	value4=x/day;

	l1=base+value4*0.191;
	l2=base+value4*0.382;
	l3=base+value4*0.5;
	l4=base+value4*0.618;
	l5=base+value4*0.809;
	l6=base-value4*0.191;
	l7=base-value4*0.382;
	l8=base-value4*0.5;
	l9=base-value4*0.618;
	l10=base-value4*0.809;
end;

if base <> 0 then begin  
    if GetField("收盤價","Tick") crosses over base+6 then begin
		ret=1;
		retmsg="作多第一口";
    end;
    if GetField("收盤價","Tick") crosses over base+12 then begin
		ret=1;
		retmsg="作多第二口";
    end;
    if GetField("收盤價","Tick") crosses over base+18 then begin
		ret=1;
		retmsg="作多第三口";
    end;
    if GetField("收盤價","Tick") crosses over base+24 then begin
		ret=1;
		retmsg="作多第四口";
    end;
    if GetField("收盤價","Tick") crosses over base+30 then begin
		ret=1;
		retmsg="作多第五口";
    end;
    if GetField("收盤價","Tick") crosses over base+36 then begin
		ret=1;
		retmsg="作多第六口";
    end;
    if GetField("收盤價","Tick") crosses under value3-6 then begin
		ret=1;
		retmsg="作空第一口";
    end;
    if GetField("收盤價","Tick") crosses under value3-12 then begin
		ret=1;
		retmsg="作空第二口";
    end;
    if GetField("收盤價","Tick") crosses under value3-18 then begin
		ret=1;
		retmsg="作空第三口";
    end;
    if GetField("收盤價","Tick") crosses under value3-24 then begin
		ret=1;
		retmsg="作空第四口";
    end;
    if GetField("收盤價","Tick") crosses under value3-30 then begin
		ret=1;
		retmsg="作空第五口";
    end;
    if GetField("收盤價","Tick") crosses under value3-36 then begin
		ret=1;
		retmsg="作空第六口";
    end;
    
    if GetField("收盤價","Tick") crosses over l1
    or GetField("收盤價","Tick") crosses over l2
    or GetField("收盤價","Tick") crosses over l3
    or GetField("收盤價","Tick") crosses over l4
    or GetField("收盤價","Tick") crosses over l5
    then begin
		ret=1;
		retmsg="50秒後請自動平倉";
    end;
    if GetField("收盤價","Tick") crosses under l6
    or GetField("收盤價","Tick") crosses under l7
    or GetField("收盤價","Tick") crosses under l8
    or GetField("收盤價","Tick") crosses under l9
    or GetField("收盤價","Tick") crosses under l10
    then begin
		ret=1;
		retmsg="50秒後請自動平倉";
    end;
end;

print(date,time,GetField("日期","Tick"),GetField("時間","Tick"),GetField("收盤價","Tick"),l1);
```

---


---

## 腳本檔案: 警示/波段操作型/60分鐘線九連陽.xs

```xs
{@type:sensor}
input:TXT("僅適用60分鐘線"); setinputname(1,"使用限制");

settotalbar(10);

if barfreq<> "Min" or barinterval <> 60 then return;

if TrueAll(Close > Close[1] and Close > Open ,9) then Ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/SAR買進訊號.xs

```xs
{@type:sensor}
input:AFIncrement(0.02);  setinputname(1,"加速因子");
input:AFMax(0.2);  setinputname(2,"加速因子最大值");

settotalbar(100);

variable:
	sarValue(0);
	
sarValue = SAR(AFIncrement, AFIncrement, AFMax);	

if close crosses over sarValue then ret = 1;
```

---


---

## 腳本檔案: 警示/波段操作型/休息後風雲再起.xs

```xs
{@type:sensor}
settotalbar(5);

condition1 =  Close[3] > low[3]* 1.01;
condition2 =  close[2] > open[2] * 1.01 and open[2]>close[3];
condition3 =  close[1] < close[2] and high[1] < close[1]* 1.005;
condition4 =  close > close[1] * 1.01;

if condition1 and condition2 and condition3 and condition4 then ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/低PB股的逆襲.xs

```xs
{@type:sensor}
if GetSymbolField("tse.tw","收盤價") > average(GetSymbolField("tse.tw","收盤價"),10)
then begin
	if close<12
	and H = highest(H,20)
	and close<lowest(low,20)*1.07
	and highest(h,40)>close*1.1
	then ret=1;
end;
```

---


---

## 腳本檔案: 警示/波段操作型/低檔連n日拉尾盤.xs

```xs
{@type:sensor}
input:Length(3); setinputname(1,"拉尾盤日數");
input:Ratio(1); setinputname(2,"拉尾盤幅度%");
input:closetime(132500); setinputname(3,"尾盤前時間");
input:ratiotoLow(7); setinputname(4,"低檔起算漲幅%");//距離區間最低價多少%
input:daystoLow(5); setinputname(5,"距離最低價天數");//輸入區間最低價的區間是幾天
input:TXT1("最高算5天"); setinputname(6,"拉尾盤日數使用限制");
input:TXT2("限用5分鐘"); setinputname(7,"頻率限制");

settotalbar(3);
setbarback(300);

if barfreq <> "Min" or barinterval <> 5  or Length>5 or daystoLow >5 then return;

variable:i(0);
variable:TodayBars(270/barinterval);

if close >= lowest(close,daystoLow * TodayBars) *( 1 + ratiotoLow*0.01) then return;

if time >= closetime then 
begin
  for i = 0 to Length-1
  begin
	// 判斷是否拉尾盤
    if close[TodayBars*i] <= close[TodayBars*i+1] * (1+ Ratio/100) then return;
  end;
  ret=1;
end;
```

---


---

## 腳本檔案: 警示/波段操作型/反常必有妖.xs

```xs
{@type:sensor}
input:TXT("僅適用60分鐘"); setinputname(1,"使用限制");

settotalbar(30);

if barinterval <> 60  or barfreq<> "Min" then return;

if Close > close[1] * 1.02  then
begin
	value2=average(truerange,30);
	value3=average(truerange,3);
	if truerange>value3 and value3>value2 then ret=1;
end;
```

---


---

## 腳本檔案: 警示/波段操作型/均線多頭排列.xs

```xs
{@type:sensor}
input: shortlength(5,"短期均線期數");
input: midlength(10,"中期均線期數");
input: Longlength(20,"長期均線期數");
input: SuperLong(60,"超長期均線期數");
variable: shortaverage(0);
variable: midaverage(0);
variable: Longaverage(0);
variable: SuperLongaverage(0);

settotalbar(3);
setbarback(maxlist(shortlength,midlength,Longlength,SuperLong));

if Close > close[1] then
begin
 shortaverage=Average(close,shortlength);
 midaverage=Average(close,midlength) ;
 Longaverage = Average(close,Longlength); 
 SuperLongaverage = Average(close,SuperLong); 
 if  close>shortaverage and 
     shortaverage>midaverage and 
	 midaverage>Longaverage and 
	 Longaverage>SuperLongaverage
 then ret=1;
end;
```

---


---

## 腳本檔案: 警示/波段操作型/外盤買氣轉強.xs

```xs
{@type:sensor}
input:short1(5,"短期平均"),mid1(20,"長期平均");

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if currenttime > 180000 
or currenttime < 083000 then 
	Z =0 
else 
	Z=1;
	
value1=GetField("內盤量");//內盤量
value2=GetField("外盤量");//外盤量
value3=value1+value2;

if value3<>0 then value4=value2/value3*100;
//外盤比重

value5=average(value4,short1);
value6=average(value4,mid1);

if close*1.4<close[90]
and value5 crosses above value6 
and value4>60
and average(volume,100)>1000
and tselsindex(10,6)[Z]=1
then ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/多次到底而破.xs

```xs
{@type:sensor}
input:day(100,"計算區間");
input:band1(4,"三高點之高低價差");

value1=nthlowest(1,low[1],day);
value2=nthlowest(3,low[1],day);
value4=nthlowestbar(1,low,day);
value5=nthlowestbar(3,low,day);
value6=nthlowestbar(5,low,day);
value7=absvalue(value4-value6);
value8=absvalue(value5-value6);
value9=absvalue(value4-value5);

condition1=false;
if value7>3 and value8>3 and value9>3
then condition1=true;

value3=(value1-value2)/value2;
if value3<=band1/100
and close crosses under value1
and volume>2000
and condition1
then ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/多次到頂而突破.xs

```xs
{@type:sensor}
input:HitTimes(3,"設定觸頂次數");
input:RangeRatio(1,"設定頭部區範圍寬度%");
input:Length(20,"計算期數");

settotalbar(300);
setbarback(100);

variable: theHigh(0); 
variable: HighLowerBound(0);  
variable: TouchRangeTimes(0);

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if currenttime > 180000 
or currenttime < 083000 then 
	Z =0 
else 
	Z=1;
theHigh = Highest(High[1],Length);  //找到過去區間的最高點
HighLowerBound = theHigh *(100-RangeRatio)/100;  // 設為瓶頸區間上界

//回算在此區間中 進去瓶頸區的次數 
TouchRangeTimes = CountIF(High[1] > HighLowerBound, Length);
 
if  TouchRangeTimes >= HitTimes   
and close > theHigh 
and close[50]*1.2 < close[20]
and tselsindex(10,6)[Z]=1
then ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/帶量突破糾結的均線.xs

```xs
{@type:sensor}
input: shortlength(5); setinputname(1,"短期均線期數");
input: midlength(10); setinputname(2,"中期均線期數");
input: Longlength(20); setinputname(3,"長期均線期數");
input: Percent(2);  setinputname(4,"均線糾結區間%");
input: Volpercent(25);  setinputname(5,"放量幅度%");//帶量突破的量是超過最長期的均量多少%
variable: shortaverage(0);
variable: midaverage(0);
variable: Longaverage(0);

settotalbar(8);
setbarback(maxlist(shortlength,midlength,Longlength));


if volume > average(volume,Longlength) * (1 + volpercent * 0.01) then
begin
	shortaverage = average(close,shortlength);
	midaverage = average(close,midlength);
	Longaverage = average(close,Longlength);
	if Close crosses over maxlist(shortaverage,midaverage,Longaverage) then
	begin
		value1= absvalue(shortaverage -midaverage);
		value2= absvalue(midaverage -Longaverage);
		value3= absvalue(Longaverage -shortaverage);
		if maxlist(value1,value2,value3)*100 < Percent*Close then  ret=1;
	end;
end;
```

---


---

## 腳本檔案: 警示/波段操作型/帶量衝破季線.xs

```xs
{@type:sensor}
//股價長期低於季線
//帶量突破季線
input: PriceLength(66); setinputname(1,"季線計算期數");
input: BelowLength(66); setinputname(2,"低於季線期數");
input: VolLength(20);  setinputname(3,"均量期數");
input: Volpercent(20);  setinputname(4,"量增幅度%");
input:TXT("建議使用日線"); setinputname(5,"使用說明");

settotalbar(BelowLength + 8);
setbarback(maxlist(PriceLength,VolLength));

variable: PriceAverage(0); PriceAverage= average(Close,PriceLength);

if Close crosses over PriceAverage and
   volume > Average(volume[1],VolLength)* (1+Volpercent/100) and
   trueall(close[1] < PriceAverage[1],  BelowLength-1) then
   ret = 1;
```

---


---

## 腳本檔案: 警示/波段操作型/平均量黃金交叉.xs

```xs
{@type:sensor}
input: shortlength(5); setinputname(1,"短均量期數");
input: Longlength(22); setinputname(2,"長均量期數");

settotalbar(8);
setbarback(maxlist(shortlength,Longlength));

variable: Longaverage(0);
variable: shortaverage(0);

Longaverage = Average(volume,Longlength);
shortaverage=Average(volume,shortlength) ;

if shortaverage crosses over  Longaverage then ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/抗跌.xs

```xs
{@type:sensor}
settotalbar(3);
if open>open[1] and open < 1.005*low then ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/暴量剛起漲.xs

```xs
{@type:sensor}
input: Length(20);       setinputname(1,"計算期數");
input: VLength(10);      setinputname(2,"均量期數");
input: volpercent(50);   setinputname(3,"爆量增幅%");
input: Rate(5);          setinputname(4,"離低點幅度%");

settotalbar(3);
setbarback(maxlist(Length,VLength));

if Close >  Close[1] and
   Volume >=  average(volume,VLength) *(1+ volpercent/100) and
   Close <= lowest(close,Length) * (1+Rate/100)
then ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/月線連兩個月收紅的小型股.xs

```xs
{@type:sensor}
input:TXT("僅適用日線","使用限制");

settotalbar(120);

if  GetField("總市值","D")<2000000000 //單位是元
and close<40
and getfield("close","M")[1]>getfield("close","M")[2] 
and getfield("close","M")[2]>getfield("close","M")[3]
then ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/沖擊底部.xs

```xs
{@type:sensor}
input:BarPercent(75); setinputname(1,"當期回升比例");

settotalbar(3);

if q_Ask > Close[1] and high[1] > high[2] and low[1] > low[2] and close[1] > close[2] then
  if TrueAll( (close[1]-low[1])>(high[1]-low[1])*BarPercent/100 ,2) then ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/沿均線前進.xs

```xs
{@type:sensor}
//沿著均線前進
input:Length(10); setinputname(1,"計算期數");
input:FollowLength(5); setinputname(2,"貼近均線期數");
input:Ratio(2);setinputname(3,"沿均線通道幅度%");
input:LongShort(0);setinputname(4,"觸發:創新高1,創新低-1,不指定0");

settotalbar(FollowLength + 3);
setbarback(Length);

condition1= false;

switch(LongShort)
begin
case =1:
 condition1 = close > highest(high[1],Length);
case -1:
 condition1 = close < lowest(low[1],Length);
case 0:
 condition1=true;
end;


If Condition1 and 
   TrueAll(absvalue(close-average(close,Length))< Close*Ratio/100,FollowLength)
then Ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/法人作多股.xs

```xs
{@type:sensor}
input: ForceType(1); setinputname(1,"1:外資 2:投信 3:自營");
input: Atleast(1000); setinputname(2,"最少買超張數");
input:TXT("須逐筆洗價"); setinputname(3,"使用限制:日線");

settotalbar(3);

if barfreq <> "D" then return;

variable: ForcePush(0);
Switch ( ForceType ) 
Begin 
Case 1: ForcePush =Getfield("外資買賣超")[1];
Case 2: ForcePush =Getfield("投信買賣超")[1];
Case 3: ForcePush =Getfield("自營商買賣超")[1]; 
End; 

if  volume > volume[1] then 
begin
      condition1 = ( close[1]-open[1]  > 0.75 *high[1]-low[1] )  and //長紅棒
                   (high[1] -low[1]) > 2 *( high[2]-low[2]);      

      if condition1 and q_Ask > highest(high[1],3) and ForcePush >Atleast then ret=1;
end;
```

---


---

## 腳本檔案: 警示/波段操作型/法人爭下車.xs

```xs
{@type:sensor}
input: ForceType(1); setinputname(1,"法人：0=合計 1=外資 2=投信 3=自營商");
input: Periods(20); setinputname(2,"計算期間");
input: Percent(5); setinputname(3,"持股減少幅度%");
input: Type(1); setinputname(4,"使用資料：0=今日、1=昨日");
input: TXT("僅適用日線逐筆洗價"); setinputname(5,"盤中使用限制");
input: TXT2("盤中無當日即時法人買賣資料"); setinputname(6,"建議使用單次洗價模式");
variable: ForcePush(0);

settotalbar(Periods + 3);

if BarFreq <> "D" or absvalue(Type) > 1 then return;

    Switch ( ForceType ) 
    Begin 
        Case 1: 
            ForcePush = Getfield("外資持股")[Type];
        Case 2: 
            ForcePush = Getfield("投信持股")[Type]; 
        Case 3: 
            ForcePush = Getfield("自營商持股")[Type]; 
        default: 
            ForcePush = Getfield("外資持股")[Type]+Getfield("投信持股")[Type]+Getfield("自營商持股")[Type];
    End; 

if currentbar <= Periods then return;

if Close < Close[1] and
   ForcePush[Type] < ForcePush[Periods+Type] * (1 - Percent * 0.01) 
then 
   ret = 1;
```

---


---

## 腳本檔案: 警示/波段操作型/法人累計買超超過N張.xs

```xs
{@type:sensor}
input: ForceType(1); setinputname(1,"法人：0=合計 1=外資 2=投信 3=自營商");
input: Periods(20); setinputname(2,"計算期間");
input: Size(3000); setinputname(3,"累計買超張數");
input: Type(1); setinputname(4,"使用資料：0=今日 1=昨日");
input: TXT1("僅適用日線"); setinputname(5,"使用限制");
input: TXT2("盤中無當日法人資料"); setinputname(6,"建議使用單次洗價模式");

settotalbar(Periods + 3);

if barfreq <> "D" then return;

variable: ForcePush(0);

if Type = 0 then value1 = 0 else value1 = 1;

Switch ( ForceType ) 
Begin 
Case 1: 
ForcePush = Getfield("外資持股")[value1];
Case 2: 
ForcePush = Getfield("投信持股")[value1]; 
Case 3: 
ForcePush = Getfield("自營商持股")[value1]; 
default: 
ForcePush = Getfield("外資持股")[value1]+Getfield("投信持股")[value1]+Getfield("自營商持股")[value1];
End; 

if currentbar <= Periods then return;

if ForcePush[value1] - ForcePush[Periods+value1] >= Size then ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/波幅縮小後的突破.xs

```xs
{@type:sensor}
input:period2(4);  setinputname(1,"短期期數");
input:period1(12); setinputname(2,"長期期數");
input:ratio(2);    setinputname(3, "漲幅%");
input:TXT("建議使用5分鐘"); setinputname(4,"使用說明");

settotalbar(3);
setbarback(maxlist(period1,period2));

if close > close[1] * (1 + ratio*0.01) then 
begin
	value1=average(truerange,period1);
	value2=average(truerange,period2);
	if value1>value2 and value2 < close* 0.02 then ret=1;
end;
```

---


---

## 腳本檔案: 警示/波段操作型/海龜進場法則.xs

```xs
{@type:sensor}
input:Length(10); setinputname(1,"近N週期數");
input:TXT("僅適用日線"); setinputname(2,"使用限制");

settotalbar((Length + 3)*5);

if barfreq <> "D" and barfreq <> "AD" then Return;

if close > highest(getfield("High","W")[1],Length)//近n週最高價
then ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/盤整後噴出.xs

```xs
{@type:sensor}
input:Length(30); setinputname(1, "計算期間");
input:percent(2.5); setinputname(2, "設定盤整區間%");

settotalbar(9);
setbarback(Length);

value1=highest(high[1],Length);
value2=lowest(low[1],Length);

if close crosses above value1
and value1 < value2 *( 1 + percent * 0.01) //最近幾根bar的收盤價高點與低點差不到N%
then ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/突破下降趨勢線.xs

```xs
{@type:sensor}
input:Length(20); setinputname(1,"下降趨勢計算期數");
input:Rate(150); setinputname(2,"反轉率%");
variable: Factor(0);

settotalbar(Length + 3);

Factor = 100/Close[Length];

value1 = linearregslope(high*Factor,Length);
value2 = linearregslope(high*Factor,3);

if close > open and close < close[length]  and  value1 < 0 and value2-value1 > Rate*0.01 then ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/突破糾結均線.xs

```xs
{@type:sensor}
input: shortlength(5,"短期均線期數");
input: midlength(10,"中期均線期數");
input: Longlength(20,"長期均線期數");
input: Percent(5,"均線糾結區間%");
input: XLen(20,"均線糾結期數");
input: Volpercent(25,"放量幅度%"); //帶量突破的量是超過最長期的均量多少%

variable: Shortaverage(0),Midaverage(0),Longaverage(0);
variable: AvgHLp(0),AvgH(0),AvgL(0);

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if currenttime > 180000 
or currenttime < 083000 then 
	Z =0 
else 
	Z=1;

Shortaverage = average(close,shortlength);
Midaverage = average(close,midlength);
Longaverage = average(close,Longlength);
AvgH = maxlist(Shortaverage,Midaverage,Longaverage);
AvgL = minlist(Shortaverage,Midaverage,Longaverage);

if AvgL > 0 then AvgHLp = 100*AvgH/AvgL -100;

condition1 = trueAll(AvgHLp < Percent,XLen);
condition2 = V > average(V[1],XLen)*(1+Volpercent/100) ;
condition3 = C > AvgH *(1.02) and H > highest(H[1],XLen);
condition4 = average(volume[1], 5) >= 1000; 

if condition1 
and condition2 
and condition3 
and condition4 
and tselsindex(10,6)[Z]=1
then ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/自營商獨自偏好.xs

```xs
{@type:sensor}
input:Length(20); setinputname(1,"計算日數");
input:_BuyRatio(5); setinputname(2,"買超佔比%");
input:TXT("僅適用日線"); setinputname(3,"使用限制");

settotalbar(3);
setbarback(Length);

if barfreq <> "D" then return;

variable: SumForce(0);
variable: SumTotalVolume(0);
variable: OtherForce(0);

SumForce = Summation(GetField("自營商買賣超")[1], Length);
SumTotalVolume = Summation(Volume[1], Length);
OtherForce = Summation(GetField("外資買賣超")[1] + GetField("投信買賣超")[1], Length);

if SumForce > SumTotalVolume  *_BuyRatio  and SumForce > OtherForce   then ret =1;
```

---


---

## 腳本檔案: 警示/波段操作型/藍籌股RSI低檔背離.xs

```xs
{@type:sensor}
input: Periods(50); setinputname(1,"計算期間");
input: Length(6); setinputname(2,"RSI");
input: LowFilter(25); setinputname(3,"RSI低檔區");

settotalbar(maxlist(Periods,maxlist(Length,6) * 8) + 3);

variable: rsivalue(0);

condition1 = false;
condition2 = false;
condition3 = false;
condition4 = false;

rsivalue = RSI(Close,Length);
value1 = highestbar(high,Periods);//轉折高點距離
value2 = lowestbar(low,Periods);//轉折低點距離

if value2 = 0	//今日為創新低的第二隻腳
then condition1 = true
else return;

if rsivalue <= LowFilter	//RSI位於低檔區
then condition2 = true
else return;

if value2[value1] + value1 < Periods //在計算區間內存在第一隻腳
then condition3 = true
else return;

if rsivalue[value2[value1] + value1] < rsivalue //RSI不再創新低
then condition4 = true
else return;

if condition1 and condition2 and condition3 and condition4
then ret = 1;
```

---


---

## 腳本檔案: 警示/波段操作型/調整型均線黃金交叉.xs

```xs
{@type:sensor}
input:Length(6); setinputname(1,"起始期數");
input:TLength(20); setinputname(2,"終止期數");
input:AddLength(1); setinputname(3,"期數調整項");
input:TuneRatio(3); setinputname(4,"調整係數");

settotalbar(TLength + 8);

variable: AvgTR(0);

if Length >= TLength then return;

AvgTR = average(TrueRange,Length);

value2 = intportion( (TLength -Length)/ AddLength);
for value1 =  Length to TLength
begin
    if mod( value1 ,AddLength) = 0  or value1 =TLength then
	 begin
		if (AvgTR > Close *  TuneRatio*0.01 ) then
		begin
		AvgTR = average(TrueRange,value1);
		value3 = value1; 
		end;
   end;
end;

if close crosses over  average(close[1] ,value3) then ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/貪婪指數太高.xs

```xs
{@type:sensor}
input:RSILength(5); setinputname(1,"強弱計算期數");
input:CLength(5); setinputname(2,"比價期數");
input:VLength(20); setinputname(3,"量計算期數");
input:Raise(20); setinputname(4,"累計上揚幅度%");
input: TXT1("僅適用日線"); setinputname(5,"使用限制");
variable : MTRatio(0),CloseRatio(0),AVGV(0);

if barfreq <> "D" then return;

if close > lowest(low,VLength) * (1+Raise/100) then
begin
	MTRatio=getfield("融資增減張數")[1]/volume[1];
	CloseRatio = close/close[CLength];
	AVGV = volume[1]/average(volume[1],VLength);
	value1 = RSI(MTRatio,RSILength)+RSI(CloseRatio,RSILength)+RSI(AVGV,RSILength);
	if RSI(value1,RSILength) >75 then ret=1;
end;
```

---


---

## 腳本檔案: 警示/波段操作型/進入上漲軌道.xs

```xs
{@type:sensor}
input:period(12,"期數");

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if currenttime > 180000 
or currenttime < 083000 then 
	Z =0 
else 
	Z=1;
	
value1=countif(low<lowest(low[1],period),period);
value2=countif(high>highest(high[1],period),period);
value3=value2-value1;
 
if value3 crosses over 4
and tselsindex(10,6)[Z]=1 
then ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/長波段回升.xs

```xs
{@type:sensor}
input: Length1(30); setinputname(1,"落底天數");
input: Size1(2000); setinputname(2,"量縮張數");
input: Length2(20); setinputname(3,"籌碼沉澱天數");
input: Size2(1000); setinputname(4,"籌碼清洗張數");
input: Ratio(10); setinputname(5,"融資使用率%");
input: Percent(3); setinputname(6,"今日漲幅%");
input: Type(1); setinputname(7,"融資資料：0=今日 1=昨日");
input: TXT1("僅適用日線"); setinputname(8,"使用限制");
input: TXT2("盤中無當日融資資料"); setinputname(9,"建議使用單次洗價模式");

settotalbar(maxlist(Length1,Length2) + 3);

variable:newlowcount(0);

if barfreq <> "D"  or (currenttime < 133000 and Type=0) then return;
if Type = 0 then value1 = 0 else value1 = 1;

condition1=false;
condition2=false;
condition3=false;
condition4=false;

if close/close[1] > 1 + Percent * 0.01 //今日強勢股
then condition1=true
else return;


if average(volume,Length1) < Size1//長期乏人問津
then condition2=true
else return;

if  trueany( Low < Low[1],length1) then return;//多日未破底


value2=GetField("Pomremain")[value1];//融資餘額
value3=GetField("Pomusingratio")[value1];//融資使用率
if value2[Length2]-value2 > Size2 and value3 < Ratio * 0.01//籌碼長期沈澱
then condition3 = true 
else return;

if average(truerange,5)>average(truerange,10)//短線波動幅度開始變大
then condition4 = true
else return;

if condition1 and condition2 and condition3 and condition4 
then ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/雙KD向上.xs

```xs
{@type:sensor}
input: Length_D(9, "日KD期間");
input: Length_W(5, "周KD期間");

variable:rsv_d(0),kk_d(0),dd_d(0);
variable:rsv_w(0),kk_w(0),dd_w(0);

stochastic(Length_D, 3, 3, rsv_d, kk_d, dd_d);
xf_stochastic("W", Length_W, 3, 3, rsv_w, kk_w, dd_w);

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if currenttime > 180000 
or currenttime < 083000 then 
	Z =0 
else 
	Z=1;
	
condition1 = kk_d crosses above dd_d;		// 日KD crosses over
condition2 = xf_GetBoolean("W",xf_crossover("W", kk_w, dd_w),1);	// 周KD crosses over
condition3 = average(volume[1], 5) >= 1000;
condition4 = kk_d[1] <= 30;							// 日K 低檔
condition5 = xf_getvalue("W", kk_w, 1) <= 50;		// 周K 低檔

// 成交量判斷
Condition6 = Average(Volume[1], 100) >= 1000;

if condition1 
and condition2 
and condition3 
and condition4 
and condition5 
and condition6
and tselsindex(10,6)[Z]=1
then ret=1;
```

---


---

## 腳本檔案: 警示/波段操作型/領先大盤創200日新高.xs

```xs
{@type:sensor}
input:period(200,"計算創新高區間");
settotalBar(period*2);

value1 = GetSymbolField("tse.tw","收盤價");
value2 = highest(value1,period);//大盤區間高點
value3 = barslast(close=highest(close,period));

if value1<value2//大盤未過新高
and close=highest(close,period)//股價創新高
and value3[1]>100
and GetSymbolField("tse.tw","收盤價")>average(GetSymbolField("tse.tw","收盤價"),10)
and average(volume,100)>1000
then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/一分鐘K三連紅.xs

```xs
{@type:sensor}
if barfreq <> "Min" or Barinterval <>1 then RaiseRuntimeError("請設定頻率為1分鐘");

variable:BarNumberOfToday(0); 

if Date <> Date[1] then 
	BarNumberOfToday=1
else 
	BarNumberOfToday+=1;{記錄今天的Bar數}
 
if barnumberoftoday=3 then begin
//今天第三根1分鐘K，也就是開盤第三分鐘
	if trueall(close>=close[1],3)
	//連三根K棒都是紅棒
	and volume>average(volume[1],3)*2
	//成交量是過去三根量平均量的兩倍以上
	and close=highd(0)
	//收最高
	then ret=1;
end;
```

---


---

## 腳本檔案: 警示/當沖交易型/主動性買盤大增.xs

```xs
{@type:sensor}
input:Length(20); setinputname(1,"調整型外盤均量計算期數");
input:Ratio(50); setinputname(2,"外盤量增幅度%");
input:TXT("僅適用60分鐘線"); setinputname(3,"使用限制");

settotalbar(3);
setbarback(Length);

if barfreq<> "Min" or barinterval <> 60 then return;

variable: AvgOutSideVol(0),DayOSV(0);

DayOSV = GetQuote("當日外盤量");
  
AvgOutSideVol =  averageIF( close > close[1] ,volume,Length);

switch(time)
begin
	case 90000: 
	    if C>O and DayOSV > AvgOutSideVol *(1+ Ratio/100) then ret=1;
	case 100000:
		if C>O and DayOSV/2 > AvgOutSideVol *(1+ Ratio/100) then ret=1;
	case 110000:
		if C>O and DayOSV/3 > AvgOutSideVol *(1+ Ratio/100) then ret=1;
	case 120000:
		if C>O and DayOSV/4 > AvgOutSideVol *(1+ Ratio/100) then ret=1;
end;
```

---


---

## 腳本檔案: 警示/當沖交易型/五分鐘K狹幅整理後帶量破.xs

```xs
{@type:sensor}
input:Length(100,"計算期數");
input:Ratio(0.5,"突破幅度%");
input:RRatio(1.5,"盤整區間幅度%");
input:TXT1("僅適用5分鐘線","使用限制");
 
settotalbar(3);
setbarback(Length);
 
if barfreq<> "Min" or barinterval <> 5 then return;
 
variable: RangeHigh(0);
variable: RangeLow(0);
RangeHigh=highest(close[1],length);
RangeLow=lowest(close[1],length);
 
if RangeHigh[1] < RangeLow[1] * (1+ RRatio/100) then begin
	if Close crosses over RangeHigh*(1+Ratio/100)
	and volume>average(volume,length)*1.5
	and trueall(GetField("成交量","D")>500,10)
	and countif(GetField("主力買賣超張數","D")[1]>0,10)>=7
	and GetSymbolField("tse.tw","收盤價","D")>GetSymbolField("tse.tw","收盤價","D")[1]
	and GetSymbolField("tse.tw","收盤價","D")>average(GetSymbolField("tse.tw","收盤價","D"),5)
	then ret=1;
end;
```

---


---

## 腳本檔案: 警示/當沖交易型/五分鐘線整理後突破.xs

```xs
{@type:sensor}
input:Length(20); setinputname(1,"計算期數");
input:Ratio(0.5); setinputname(2,"突破幅度%");
input:RRatio(1.5); setinputname(3,"盤整區間幅度%");
input:TXT1("僅適用5分鐘線"); setinputname(4,"使用限制");

settotalbar(3);
setbarback(Length);

if barfreq<> "Min" or barinterval <> 5 then return;

variable: RangeHigh(0);
variable: RangeLow(0);
RangeHigh=highest(close[1],length);
RangeLow=lowest(close[1],length);

if Close > RangeHigh*(1+Ratio/100) then
   if RangeHigh <  RangeLow * (1+ RRatio/100) then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/即將鎖第一根漲停.xs

```xs
{@type:sensor}
input:Length(20); setinputname(1,"過去無漲停期數");
input:Ratio(1); setinputname(2,"差幾%漲停");
input:TXT("請用日線逐筆洗價"); setinputname(3,"使用限制");

settotalbar(Length + 3);

if BarFreq = "D" then 
  if Close > GetField("漲停價", "D")*(1- Ratio/100)  then
    if TrueAll(close[1] < Close[2]*1.068,Length) then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/多次到頂而破.xs

```xs
{@type:sensor}
input:HitTimes(3);    setinputname(1,"設定觸頂次數");
input:RangeRatio(1);  setinputname(2,"設定頭部區範圍寬度%");
input:Length(20);     setinputname(3,"計算期數");

settotalbar(Length + 3);

variable: theHigh(0); theHigh = Highest(High[1],Length);  //找到過去其間的最高點
variable: HighLowerBound(0);  HighLowerBound = theHigh *(100-RangeRatio)/100;  // 設為瓶頸區間上界
variable: TouchRangeTimes(0); 							  //期間中進入瓶頸區間的低點次數,每跟K棒要歸0
 
//回算在此區間中 進去瓶頸區的次數 
TouchRangeTimes = CountIF(High[1] > HighLowerBound, Length);
 
if  TouchRangeTimes >= HitTimes   and  ( q_ask> theHigh or   close > theHigh) then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/斷頭後的止跌.xs

```xs
{@type:sensor}
input:Length(4); setinputname(1,"比較N天前融資張數");
input:DVOL(3000); setinputname(2,"比N天前融資減少張數");
input:TXT1("僅適用日線"); setinputname(3,"使用限制");
input:TXT2("建議使用逐筆洗價"); setinputname(4,"盤中使用說明");

settotalbar(3);
setbarback(Length);

if barfreq = "D" and 
   Close > Close[1] and 
   Close[Length] > Close * 1.1 and
   GetField("融資餘額張數")[Length] - GetField("融資餘額張數")[1] > DVOL 
then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/會打開的跌停.xs

```xs
{@type:sensor}
settotalbar(605);
if q_ask=GetField("跌停價", "D") and
   q_bestasksize1<1500 and
   (closeD(2)-close)>0.07*Close  
then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/漲停量縮不下來.xs

```xs
{@type:sensor}
input: lastvolume1(2000);  setinputname(1,"漲停期間放量張數");
input: lastvolume2(10000); setinputname(2,"當日總成交量上限");
input:TXT1("需使用逐筆洗價"); setinputname(3,"使用限制");

settotalbar(3);

variable: UPLVol(0);

if Date <> Date[1] then UPLVol = 0;

if Close =GetField("漲停價", "D") then 
begin
  UPLVol += GetField("Volume", "Tick");
  if q_BestBidSize1 <lastvolume1 and 
     GetField("Volume", "D") >lastvolume2 and
	 UPLVol > lastvolume1 
  then RET=1;
end;
```

---


---

## 腳本檔案: 警示/當沖交易型/火箭後拉回.xs

```xs
{@type:sensor}
input:TXT1("僅適用1分鐘線"); setinputname(1,"使用限制");
settotalbar(3);
if barfreq ="Min" and barinterval =1 and
   close[1]/close[2]>1.015 and //上個1分鐘線單分鐘拉超過1.5%
   GetField("High", "D") > high and //高不過高
   Close < GetField("High", "D")*0.99 and //自高檔回1%
   Close > Low[1] 
then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/當日累計量突破.xs

```xs
{@type:sensor}
input:VolumeThre(1000); setinputname(1,"突破量門檻");
input:AmountThre(1000); setinputname(2,"突破成交值金額門檻(萬)");
settotalbar(3);
if GetField("Volume", "D") > VolumeThre or GetField("均價")*GetField("Volume", "D")/10 > AmountThre then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/當沖一號.xs

```xs
{@type:sensor}
if barfreq <>"Min" or  barinterval<> 1 then raiseruntimeerror("歹勢，本腳本只適用於1分鐘線");

variable:count(0);

if date<>date[1] then count=0;
count=count+1;

if GetField("開盤價","D")> GetField("收盤價","D")[1]*1.025
and count>20
and lowest(low[1],count-1)*1.015>highest(high[1],count-1)
and close =highest(high,count)
then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/當沖二號(空).xs

```xs
{@type:sensor}
if barfreq <>"Min" or  barinterval<> 1
then raiseruntimeerror("歹勢，本腳本只適用於1分鐘線");

variable:count(0);

if date<>date[1] then count=0;
count=count+1;
 
if GetField("開盤價","D")*1.025< GetField("收盤價","D")[1] 
and count>10
and lowest(low[1],count-1)*1.015>highest(high[1],count-1)
and close =lowest(low,count)
then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/盤中突破區間.xs

```xs
{@type:sensor}
input: timeline(100000); setinputname(1,"時間切算點");
input:TXT1("限用分鐘線"); setinputname(2,"使用限制");
input:TXT2("高點自開盤起算"); setinputname(3,"使用說明");
settotalbar(3);
if barfreq<> "Min" then return;
variable:RangeHigh(0);
if date <> date[1] then RangeHigh = 0;
if Time < timeline then RangeHigh = maxlist(RangeHigh,high)
	else if time >= timeline and  RangeHigh > 0 and Close > RangeHigh*1.005 then ret=1 ;
```

---


---

## 腳本檔案: 警示/當沖交易型/突破波動範圍.xs

```xs
{@type:sensor}
input:Length(20); setinputname(1,"高低計算期數");
settotalbar(3);
setbarback(Length);
variable:HighLow(0);
HighLow=high-low;
if C>highest(H[1],Length) *1.005 and  HighLow>highest(HighLow[1],Length) then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/賣壓很輕.xs

```xs
{@type:sensor}
input:rate(20);setinputname(1,"當日內盤量佔總成交比例%");
settotalbar(8);
if {內盤量}GetField("內盤量", "D")  < GetField("Volume", "D")*(Rate/100)  and Countif(close< close[1],5) < 3
then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/跌停一直在成交.xs

```xs
{@type:sensor}
input: lastvolume1(2000);  setinputname(1,"跌停期間放量張數");
input: lastvolume2(10000); setinputname(2,"當日總成交量上限");
input:TXT1("需使用逐筆洗價"); setinputname(3,"使用限制");
settotalbar(3);
variable: DNLVol(0);

if Date <> Date[1] then DNLVol = 0;

if Close = GetField("跌停價", "D") then 
begin
  DNLVol += GetField("Volume", "Tick");
  if q_BestAskSize1 <lastvolume1 and 
     GetField("Volume", "D") >lastvolume2 and
	 DNLVol > lastvolume1 
  then RET=1;
end;
```

---


---

## 腳本檔案: 警示/當沖交易型/近期持續強勢股階梯式上漲.xs

```xs
{@type:sensor}
if barfreq<> "Min"and barinterval<> 5 then raiseruntimeerror("本腳本只限五分鐘線");

condition1 = GetSymbolField("tse.tw","收盤價","D") > average(GetSymbolField("tse.tw","收盤價","D"),10);
//多頭市場

condition2 = GetSymbolField("tse.tw","收盤價","D") / GetSymbolField("tse.tw","收盤價","D")[2]+0.01
			  <  GetField("收盤價","D")/GetField("收盤價","D")[2];
//前兩日比大盤明顯走強

condition3 = GetField("收盤價","D")[1] <GetField("收盤價","D")[10]*1.07;
//近十日沒有漲的太兇

condition4 = Average(GetField("Volume", "D")[1], 100) >= 1000;

if condition1 and condition2 and condition3 and condition4 then begin
	if time=091500
	and trueall(close>close[1],3)
	//開盤三根五分鐘線都是紅棒
	and average(volume,3)>average(volume,20)*1.3
	//開盤的量能明顯增加
	and GetField("收盤價","D")[1]<GetField("收盤價","D")[2]
	then ret=1;
end;
```

---


---

## 腳本檔案: 警示/當沖交易型/連續五分鐘一路走高.xs

```xs
{@type:sensor}
input:TXT1("僅適用1分鐘線"); setinputname(1,"使用限制");
settotalbar(8);
if barfreq = "Min" and barinterval = 1 and
   TrueAll(close >Close[1] ,5) then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/開低不反彈再創新低.xs

```xs
{@type:sensor}
if barfreq <>"Min" or barinterval<> 1 then raiseruntimeerror("本腳本只適用於1分鐘線");

variable:count(0);

if date<>date[1] then count=0;
count=count+1;
  
if GetField("開盤價","D")*1.025< GetField("收盤價","D")[1] 
and count>10
and lowest(low[1],count-1)*1.015>highest(high[1],count-1)
and close =lowest(low,count)
then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/開大跌後未再探底.xs

```xs
{@type:sensor}
input:ratio(4);     setinputname(1,"開低幅度%"); 
input:ratio1(0.5);  setinputname(2,"開低後回升幅度%");
settotalbar(3);
if GetField("Open", "D") < GetField("RefPrice", "D") * (1 -Ratio/100) and 
   GetField("Open", "D") >= GetField("Low", "D")  and
   (GetField("Open", "D")- GetField("Low", "D"))<  Close * Ratio1 and
   Close > GetField("Open", "D") * (1 + Ratio1/100) 
then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/開盤三連陽.xs

```xs
{@type:sensor}
input:TXT("僅適用60分鐘線以內"); setinputname(1,"使用限制");
settotalbar(5);
if barfreq = "Min" and barinterval <= 60 and
   (time[2] = 84500 or time[2] = 90000) and
    Close > Close[1] and Close[1] > Close[2] and
	Close[2] > Open[2] 
then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/開盤五分鐘K線三連陽.xs

```xs
{@type:sensor}
input:TXT1("僅適用5分鐘線"); setinputname(1,"使用限制");
input:TXT2("開盤前3根K棒"); setinputname(2,"使用說明:判斷規則");
settotalbar(5);
if barfreq<> "Min" or barinterval <> 5 then return;

variable:KBarOfDay(0); KBarOfDay+=1; if date<>date[1] then  KBarOfDay=1; 

if Date = CurrentDate   and
   (time[2] = 90000 or time[2] = 84500) and
   KBarOfDay = 3 and
   Close[2] > Open[2] and 
   TrueAll(Close > Open and Close > Close[1] ,2)  then Ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/開盤五分鐘三創新高.xs

```xs
{@type:sensor}
input: volumeRatio(0.1, "分鐘量暴量比例");
input: changeRatio(3, "最近3日最大上漲幅度");
input: averageVolume(1000, "5日均量");

variable:KBarOfDay(0), BreakHigh(false); 
 
KBarOfDay+=1;
if date<>date[1] then begin
	KBarOfDay=1; 
	BreakHigh = false;
end; 
 
condition1 = KBarOfDay = 6;
//一分鐘線每天的第六根

condition2 = Countif(High > High[1] and Close > Close[1] ,5) >=3;
//近五根裡至少三根最高價比前一根高且收盤比前一根高

if KBarOfDay = 1
and close > getfield("close", "d")[1] 
then BreakHigh = true;
//開高

value1 = average(GetField("Volume", "D")[1], 5);
//五日均量

condition3 = value1 > averageVolume;
//五日均量大於某張數 

value2 = rateofchange(GetField("Close", "D")[1], 3);
condition4 = AbsValue(value2) < changeRatio;
//前三日漲帳幅小於一定標準

condition5 = summation(volume, 5) > value1 * volumeRatio;
//前五根一分鐘線成交量的合計大於五日均量某個比例

condition6 = GetSymbolField("TSE.TW","收盤價","D")>average(GetSymbolField("TSE.TW","收盤價","D"),10);
//大盤屬於多頭結構

if condition1 and condition2 and condition3
and Condition4 and Condition5 and condition6
and BreakHigh
then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/開盤五分鐘創三新低.xs

```xs
{@type:sensor}
input:TXT("僅適用1分鐘線"); setinputname(1,"使用限制");
settotalbar(8);
variable:KBarOfDay(0); KBarOfDay+=1; if date<>date[1] then  KBarOfDay=1; 

if barfreq = "Min"  and barinterval = 1 and Date = CurrentDate   and
   KBarOfDay = 6 and
   Countif(Low < Low[1] and Close < Close[1] ,5) >=3  then Ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/開盤五分鐘創三新高.xs

```xs
{@type:sensor}
input:TXT("僅適用1分鐘線"); setinputname(1,"使用限制");
settotalbar(8);
variable:KBarOfDay(0); KBarOfDay+=1; if date<>date[1] then  KBarOfDay=1; 

if barfreq<> "Min"  and barinterval = 1 and Date = CurrentDate   and
   KBarOfDay = 6 and
   Countif(High > High[1] and Close > Close[1] ,5) >=3  then Ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/開盤反轉買進訊號.xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 警示/當沖交易型/開盤委買暴增.xs

```xs
{@type:sensor}
input:iVOL(1000);                setinputname(1,"開盤委買賣差張");
input:Ratio(10);                 setinputname(2,"開盤委買力道比");
input:TXT1("適用1分鐘");         setinputname(3,"使用限制");
input:TXT2("僅開盤第1分鐘洗價"); setinputname(4,"使用說明");
settotalbar(300);
if barfreq ="Min" and barinterval =1 and Date= Currentdate and
   Time =90000 and GetQuote("總委買") - GetQuote("總委賣") >iVOL and
   GetQuote("總委買") / summation(volume[1],270) > Ratio 
then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/開盤暴量.xs

```xs
{@type:sensor}
input:Vtimes(3);            setinputname(1,"爆量倍數");
input:atVolume(100);            setinputname(2,"暴量門檻張數");
input:TXT1("僅適用1分鐘");  setinputname(3,"使用限制");
input:TXT2("盤中可用");  setinputname(4,"使用說明:建議日內單次觸發");
settotalbar(300);
if barfreq <> "Min" or Barinterval <> 1 then return;

variable: OpenVolume(0), OpenVolumeDate(0);
if CurrentBar = 1 then
  begin
	// 找到當日第一筆分鐘K線的成交量
	//
	variable: idx(0);
	idx = 0;
	while date[idx] = date
	  begin
		OpenVolume = Volume[idx];
		OpenVolumeDate = date[idx];
		idx = idx + 1;
	  end;
  end
else
	if Date <> OpenVolumeDate then
	  begin
		// 開盤量為換日後的第一筆分鐘K線的成交量
		OpenVolumeDate = Date;
		OpenVolume = Volume;
	  end;
if CurrentDate = OpenVolumeDate And 
   OpenVolume > AtVolume And
   OpenVolume > GetQuote("昨量")/270 * Vtimes then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/開高不拉回後再創新高.xs

```xs
{@type:sensor}
if barfreq <>"Min" or barinterval<> 1 then raiseruntimeerror("歹勢，本腳本只適用於1分鐘線");

variable:count(0);

if date<>date[1] then count=0;
count=count+1;
  
if GetField("開盤價","D")> GetField("收盤價","D")[1]*1.025
and count>5
and lowest(low[1],count-1)*1.015>highest(high[1],count-1)
and close =highest(high,count)
then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/開高後不拉回.xs

```xs
{@type:sensor}
input:Ratio(2.5); setinputname(1,"開高幅度%");
input:aRatio(1); setinputname(2,"拉回度%上限");
input:TXT("僅適用於15分鐘以內"); setinputname(3,"使用限制");
settotalbar(3);
if barfreq ="Min" and barinterval <=15 and time <= 091500 and
   GetField("Open", "D") > GetField("RefPrice", "D") *(1+Ratio/100) and 
   Close > GetField("High", "D")* (1- aRatio/100) 
then ret=1;
```

---


---

## 腳本檔案: 警示/當沖交易型/階梯式上漲.xs

```xs
{@type:sensor}
input:TXT1("僅適用1分鐘線"); setinputname(1,"使用限制");
input:TXT2("只於9:10判斷"); setinputname(2,"使用說明");
settotalbar(12);
if barfreq = "Min" and barinterval = 1 and time =91000 and
   TrueAll(close >Close[1] ,10) then ret=1;
```

---


---

## 腳本檔案: 警示/盤中常用/1分鐘K開盤暴量三連陽.xs

```xs
{@type:sensor}
if barfreq <> "Min" or Barinterval <>1 then RaiseRuntimeError("請設定頻率為1分鐘");

variable:BarNumberOfToday(0); 

if Date <> Date[1] then
	BarNumberOfToday=1 
else
	BarNumberOfToday+=1;{記錄今天的Bar數} 

if barnumberoftoday=3 then begin
//今天第三根1分鐘K，也就是開盤第三分鐘
	if trueall(close>=close[1],3)
	//連三根K棒都是紅棒
	and volume>average(volume[1],3)*2
	//成交量是過去三根量平均量的兩倍以上
	and close=highd(0)
	//收最高
	then ret=1;
end;
```

---


---

## 腳本檔案: 警示/盤中常用/大單敲進.xs

```xs
{@type:sensor}
input: atVolume(50,"大單門檻");
input: LaTime(10,"大單筆數");
input: TXT("須逐筆洗價","使用限制");

settotalbar(3);

variable:  intrabarpersist Xtime(0);
//計數器
variable: intrabarpersist Volumestamp(0);

Volumestamp =GetField("Volume", "D");
if time < time[1] 
or Volumestamp = Volumestamp[1]
then Xtime =0; //開盤那根要歸0次數

if GetField("Volume", "Tick") > atVolume
//單筆tick成交量超過大單門檻
and GetField("內外盤","Tick")=1
//外盤成交
then Xtime+=1; 
//量夠大就加1次
if Xtime > LaTime then begin
	ret=1; 
	Xtime=0;
end;
```

---


---

## 腳本檔案: 警示/盤中常用/盤中委買遠大於委賣.xs

```xs
{@type:sensor}
input:v1(2000,"委買五檔總金額(萬)");
input:v2(500,"委賣五檔總金額(萬)");
input:v3(1500,"委買委賣總差額(萬)");
input:v4(400,"單一價位委買金額下限");
input:v5(100,"單一價位委賣金額上限");

variable:bidtv(0),asktv(0),tb(0),ta(0),b1(0),b2(0),b3(0),b4(0),b5(0),s1(0),s2(0),s3(0),s4(0),s5(0);
condition1=false;
condition2=false;
condition3=false;

bidtv=q_SumBidSize;//總委買
asktv=q_SumAskSize;//總委賣

value1=q_BestBidSize1;//委買一
value2=q_BestBidSize2;
value3=q_bestbidsize3;
value4=q_bestbidsize4;
value5=q_bestbidsize5;

value6=q_bestasksize1;//委賣一
value7=q_bestasksize2;
value8=q_bestasksize3;
value9=q_bestasksize4;
value10=q_bestasksize5;

tb=bidtv*close/10;
ta=asktv*close/10;

if tb>v1 and ta<v2 and tb-ta>v3
then condition1=true;

b1=value1*close/10;
b2=value2*close/10;
b3=value3*close/10;
b4=value4*close/10;
b5=value5*close/10;
s1=value6*close/10;
s2=value7*close/10;
s3=value8*close/10;
s4=value9*close/10;
s5=value10*close/10;

if minlist(b1,b2,b3,b4,b5)>v4
then condition2=true;

if maxlist(s1,s2,s3,s4,s5)<v5
then condition3=true;

if close<>GetField("漲停價", "D") then begin
	if  condition1 
	or (condition2 and condition3)
	then ret=1; 
end;
```

---


---

## 腳本檔案: 警示/盤中常用/開盤跳空上漲N%且有量.xs

```xs
{@type:sensor}
if open >=close[1]*1.03
and volume*close>300000
then ret=1;
```

---


---

## 腳本檔案: 警示/盤中常用/預估量破均量.xs

```xs
{@type:sensor}
value1=GetField("內盤量", "D");//當日內盤量
value2=GetField("外盤量", "D");//當日外盤量
if GetField("估計量") > average(volume[1],10)*1.3
and value2>value1
then ret=1;
```

---


---

## 腳本檔案: 警示/短線操作型/一小時線長期盤整後突破.xs

```xs
{@type:sensor}
//盤整後噴出
input: Periods(20); setinputname(1,"計算期數");
input: Ratio(3);setinputname(2,"近期波動幅度%");
input: Direction(1);setinputname(3,"方向:1突破 -1跌破");
input: TXT1("僅適用60分鐘"); setinputname(4,"使用限制");

settotalbar(3);
setbarback(Periods);


condition1 = false;

if (highest(high[1],Periods-1) - lowest(low[1],Periods-1))/close[1] <= ratio*0.01 
then condition1=true//近期波動在?%以內
else return;

if condition1 and Direction > 0 and high = highest(high, Periods)
then ret=1;//盤整後往上突破

if condition1 and Direction < 0 and low = lowest(low, Periods)
then ret=1;//盤整後往下跌破
```

---


---

## 腳本檔案: 警示/短線操作型/一黑破三紅.xs

```xs
{@type:sensor}
input:periods(20);setinputname(1,"計算期數(最小為5)");
input:ratio(20);setinputname(2,"累計漲幅%");

settotalbar(5);
setbarback(Periods);

variable:x(0);

if periods < 5 then return;

condition1=false;
condition2=false;
condition3=false;

if (high[1] - low[periods-1])/low[periods-1] >= ratio*0.01 
then condition1=true//近n日漲幅超過?%
else return;

if high>highest(high[1],3) and c<lowest(low[1],3)
then condition2=true//開盤是四日來新高但收盤比三日前低點低
else return;

//前二天每天比前一天上漲且連續三天收紅棒
condition3 = TrueAll(c[1]>c[2], 2) and
			 TrueAll(open[1]<close[1], 3); 

if condition1 and condition2 and condition3
then ret=1;
```

---


---

## 腳本檔案: 警示/短線操作型/三根長下影線.xs

```xs
{@type:sensor}
input: Percent(1.5); setinputname(1,"下影線佔股價絕對百分比");

settotalbar(5);

condition1 = (minlist(open,close)-low) > absvalue(open-close)*3; 
condition2 = minlist(open,close) > low * (100 + Percent)/100;

if trueall( condition1 and condition2, 3) then ret=1;
```

---


---

## 腳本檔案: 警示/短線操作型/中小型股整理結束.xs

```xs
{@type:sensor}
input: Periods(20); setinputname(1,"計算期數");
input: Ratio(3);setinputname(2,"近期波動幅度%");

settotalbar(300);
setbarback(50);

condition1 = false;

if (highest(high[1],Periods-1) - lowest(low[1],Periods-1)) <= ratio*0.01*close[1]
then condition1=true//近期波動在?%以內
else return;

if condition1 
and high = highest(high, Periods)
and GetSymbolField("tse.tw","收盤價")>average(GetSymbolField("tse.tw","收盤價"),10)
and average(GetSymbolField("tse.tw","收盤價"),5)>average(GetSymbolField("tse.tw","收盤價"),20)
then ret=1;//盤整後往上突破
```

---


---

## 腳本檔案: 警示/短線操作型/主力慢慢收集籌碼後攻堅.xs

```xs
{@type:sensor}
input:period(10,"籌碼計算天期");

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if currenttime > 180000 
or currenttime < 083000 then 
	Z =0 
else 
	Z=1;

Value1=GetField("分公司買進家數","D")[Z];
value2=GetField("分公司賣出家數","D")[Z];
value3=(value2-value1);
//賣出的家數比買進家數多的部份
value4=average(close,5);
//五日移動平均

if countif(value3>30, period)/period >0.7
and linearregslope(value4,5)>0
and Average(Volume[1], 100) >= 500
and tselsindex(10,7)[Z]=1
then ret=1;
```

---


---

## 腳本檔案: 警示/短線操作型/加速趕底中.xs

```xs
{@type:sensor}
settotalbar(210);

if Close[4] > Close *1.07 and
   TrueAll (truerange/Close > 0.02,3) and
   Close < Highest(high,200) *0.7 
then Ret=1;
    
{自高檔回跌三成且近5期收低7%以上,近3期每期波動至少有2%}
```

---


---

## 腳本檔案: 警示/短線操作型/外資買超但只開平高盤.xs

```xs
{@type:sensor}
input: Atleast(1000); setinputname(1,"外資買超張數");
input: Gap(2); setinputname(2,"平盤幅度%");
input:TXT1("僅適用日線"); setinputname(3,"使用限制");
input:TXT2("需逐筆洗價"); setinputname(4,"使用說明:選日內單次觸發");

settotalbar(3);

if BarFreq = "D" and  Getfield("外資買賣超")[1] > Atleast and
   GetField("Open", "D") < GetField("RefPrice", "D") *(1+Gap/100) and
   GetField("Open", "D") > GetField("RefPrice", "D") 
then ret=1;
```

---


---

## 腳本檔案: 警示/短線操作型/外資連日大買超，股價未開高.xs

```xs
{@type:sensor}
input:Periods(3); setinputname(1,"外資連續買超天數");
input:Atleast(10000); setinputname(2,"每日買超金額(萬元)");
input:Gap(1); setinputname(3,"開盤幅度%");
input:TXT1("僅適用日線"); setinputname(4,"使用限制");
input:TXT2("需逐筆洗價"); setinputname(5,"使用說明:選日內單次觸發");

settotalbar(3);
setbarback(Periods);

if BarFreq = "D" and
   Trueall( Getfield("外資買賣超")[1]*Close*0.1 > Atleast ,Periods)  and
   GetField("Open", "D") < GetField("RefPrice", "D") *(1+Gap/100)
then ret=1;
```

---


---

## 腳本檔案: 警示/短線操作型/外資連續買超n天.xs

```xs
{@type:sensor}
input:Periods(5); setinputname(1,"外資連續買超天數");
input:TXT1("僅適用日線"); setinputname(2,"使用限制");

settotalbar(3);
setbarback(Periods);

if BarFreq <> "D"  then return;

Ret = TrueAll(GetField("外資買賣超")[1] > 0, Periods);
```

---


---

## 腳本檔案: 警示/短線操作型/投信初介入.xs

```xs
{@type:sensor}
input: day(30, "投信交易期間");

if GetSymbolField("TSE.TW","收盤價") > average(GetSymbolField("TSE.TW","收盤價"),10)
and Average(Volume[1], 100) >= 1000
then begin

	value1 = summation(GetField("投信買賣超")[1], day); 
	value2 = summation(volume[2], day);


	condition1 = value1 < value2 * 0.02;
	//先前投信不怎麼買這檔股票

	if getfielddate("投信買賣超") <> date then
		value99 = GetField("投信買賣超")[1]
	else
		value99 = GetField("投信買賣超");

	condition2 = value99>= volume[1] * 0.15;
	//投信開始較大買超

	condition3 = H > H[1];
	//買了股價有往上攻

	condition4 = C > C[1];
	//今天收盤有往上走

	condition5=close<close[10]*1.05;

	condition6=GetSymbolField("TSE.TW","收盤價") > average(GetSymbolField("TSE.TW","收盤價"),10);
	
	if condition1 
	and condition2 
	and condition3 
	and condition4
	and condition5 
	and condition6
	then ret=1;
 
end;
```

---


---

## 腳本檔案: 警示/短線操作型/投信外資同步進場.xs

```xs
{@type:sensor}
input:Fboughts(100); setinputname(1,"外資買超張數");
input:Sboughts(100); setinputname(2,"投信買超張數");
input:TXT1("僅適用日線"); setinputname(3,"使用限制");
settotalbar(3);
if BarFreq <> "D"  then return;
if GetField("外資買賣超")[1]>Fboughts and GetField("投信買賣超")[1]>Sboughts
then ret=1;
```

---


---

## 腳本檔案: 警示/短線操作型/投信搶買的股票.xs

```xs
{@type:sensor}
input: miniratio(10); setinputname(1,"投信買進佔今日總量%");
input: lv(2000); setinputname(2,"投信持股張數上限");
input: holdratio(10); setinputname(3,"投信持股比例上限%");
input:TXT1("僅適用日線"); setinputname(4,"使用限制");
input:TXT2("需選用逐筆洗價"); setinputname(5,"使用說明");
settotalbar(3);

if BarFreq <> "D"  then return;

//1.中小型股
//2.原來庫存低
//3.今天買進張數超過成交量的一成
//4.收今天最高

value1=GetField("Stotalbuy")[1];//投信買張
value2=GetField("Ssharesheld")[1];//投信持股
value3=GetField("Ssharesheldratio")[1];//投信持股比例

if close > high[1] and close[1]=high[1]   and //昨天收高 今日再漲
   value1 > volume[1] * miniratio*0.01 and //昨日買進張數超過成交量的一成
   value2 < lv and //原來庫存低
   value3 < holdratio //原來庫存低
then ret=1;
```

---


---

## 腳本檔案: 警示/短線操作型/投信殺完之跌深反彈.xs

```xs
{@type:sensor}
input:day(5); setinputname(1,"投信連續賣超天數");
input:ratio(60);setinputname(2,"合計賣超減持幅度%");
input:TXT1("僅適用日線"); setinputname(3,"使用限制");
input:TXT2("須逐筆洗價"); setinputname(4,"使用說明");
settotalbar(day + 3);

if close>open and close[3] > close[1] * 1.1  and BarFreq ="D" then
begin
  if TrueAll(GetField("Sdifference")[1] <0,day) and
     GetField("Ssharesheld")[1] < GetField("Ssharesheld")[Day+1] * (1- Ratio/100) 
  then ret=1;
end;
```

---


---

## 腳本檔案: 警示/短線操作型/投信買張超過成交量一成.xs

```xs
{@type:sensor}
input: Ratio(10); setinputname(1,"投信持股%");
input: Gap(2.5); setinputname(2,"開盤不漲過幅度%");
input:TXT1("僅適用日線"); setinputname(3,"使用限制");
input:TXT2("須逐筆洗價"); setinputname(4,"使用說明");
settotalbar(3);
if BarFreq <> "D"  or currenttime > 90500 then return;

   
value1=GetField("Stotalbuy")[1];//投信買張
value2=GetField("Ssharesheldratio")[1];//投信持股比例
if value2<Ratio and value1/volume[1]>0.1 and close < close[1] *(1 + Gap * 0.01)
then ret=1;
```

---


---

## 腳本檔案: 警示/短線操作型/投信連日大買超，股價未開高.xs

```xs
{@type:sensor}
input:Periods(3); setinputname(1,"投信連續買超天數");
input:Atleast(10000); setinputname(2,"每日買超金額(萬元)");
input:Gap(1); setinputname(3,"開盤幅度%");
input:TXT1("僅適用日線"); setinputname(4,"使用限制");
input:TXT2("需逐筆洗價"); setinputname(5,"使用說明:選日內單次觸發");
settotalbar(Periods + 3);


if BarFreq = "D" and
   Trueall( Getfield("投信買賣超")[1]*Close*0.1 > Atleast ,Periods)  and
   GetField("Open", "D") < GetField("RefPrice", "D") *(1+Gap/100) 
then ret=1;
```

---


---

## 腳本檔案: 警示/短線操作型/漲勢加速的股票.xs

```xs
{@type:sensor}
input:day2(5,"近期");
input:day1(10,"中期");

if angle(date[day1],date[day2])>0
and angle(date[day2],date)>angle(date[day1],date[day2])
and angle(date[day2],date)>25
and GetSymbolField("tse.tw","收盤價","W")
>average(GetSymbolField("tse.tw","收盤價","W"),13)
then ret=1;
```

---


---

## 腳本檔案: 警示/短線操作型/炒高後沒有量.xs

```xs
{@type:sensor}
input: Periods(120); setinputname(1,"計算期數");
input: Ratio(50);setinputname(2,"期間漲幅%");
input: Sizes(2000);setinputname(3,"五日均量量縮張數");
input:TXT1("僅適用日線"); setinputname(4,"使用限制");
input:TXT2("需選用逐筆洗價"); setinputname(5,"使用說明");
settotalbar(3);
setbarback(Periods);

if BarFreq = "D"  and currenttime>130000 and
   getfield("融資餘額張數")[1] > 2000 and //昨日融資餘額多於2000張
   getfield("融券餘額張數")[1] < 2000 and //昨日融券餘額少於2000張
   close >= close[Periods] *(1 + Ratio*0.01) and //過去半年漲幅超過五成
   average(volume[1],5) < Sizes and //五日均量低於N張
   GetQuote("DailyVolume")< 500 and //當日總量
   GetQuote("OutSize") < GetQuote("DailyVolume")*0.5 //當日外盤量小於總量一半
then ret=1;
```

---


---

## 腳本檔案: 警示/短線操作型/短線轉強.xs

```xs
{@type:sensor}
input:day(66,"移動平均天數");
input:ratio(30,"超出均值比率");
variable:count(0);

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if currenttime > 180000 
or currenttime < 083000 then 
	Z =0 
else 
	Z=1;

value1=GetField("法人買張")[Z]; value2=average(value1,day);
value3=GetField("強弱指標")[Z]; value4=average(value3,day);
value5=GetField("外盤均量")[Z]; value6=average(value5,day);
value7=GetField("主動買力")[Z]; value8=average(value7,day);
value9=GetField("開盤委買"); value10=average(value9,day);
 
count=0;
if value1>=value2*(1+ratio/100) then count=count+1;
if value3>=value4*(1+ratio/100) then count=count+1;
if value5>=value6*(1+ratio/100) then count=count+1;
if value7>=value8*(1+ratio/100) then count=count+1;
if value9>=value10*(1+ratio/100) then count=count+1;
 
if count>=4 and close<lowest(close,day)*1.1
and GetSymbolField("tse.tw","收盤價","D")>average(GetSymbolField("tse.tw","收盤價","D"),10)
and average(volume,200)>2000
then ret=1;
```

---


---

## 腳本檔案: 警示/短線操作型/突破繼續型態.xs

```xs
{@type:sensor}
input:Length(20); setinputname(1,"下降趨勢計算期數");
input:Rate(150); setinputname(2,"反轉率%");
variable: Factor(0);
settotalbar(Length + 3);

Factor = 100/Close[Length];

if close > open and  close < close[length] then
begin
	value1 = linearregslope(high*Factor,Length);
	value2 = linearregslope(high*Factor,3);
	if value1 < 0 and  value2-value1 > Rate*0.01 then ret=1;
end;
```

---


---

## 腳本檔案: 警示/短線操作型/站上五根bar高點.xs

```xs
{@type:sensor}
settotalbar(5);

if close > highest(High[1],4)
then ret=1;
```

---


---

## 腳本檔案: 警示/短線操作型/第一根漲停.xs

```xs
{@type:sensor}
input: Periods(5); setinputname(1,"N天內第一根漲停");
input: Size(1500); setinputname(2,"漲停委賣張數");
settotalbar(Periods + 3);

if Periods < 1 then return;

if q_ask=GetField("漲停價", "D") and q_bestasksize1<Size then 
begin
	for value1 = 1 to Periods
	begin
		if closeD(value1-1) > closeD(value1) * 1.065 then return;
	end;
	ret=1;
end;
```

---


---

## 腳本檔案: 警示/短線操作型/籌碼由發散轉收集.xs

```xs
{@type:sensor}
input: Length_D(9, "日KD期間");
input: Length_W(5, "周KD期間");
variable:rsv_d(0),kk_d(0),dd_d(0);
variable:rsv_w(0),kk_w(0),dd_w(0);

SetTotalBar(maxlist(Length_D,6) * 3);

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
variable: Z(0);
if GetFieldDate("主力買賣超張數") <> 0 then
	Z=0 
else 
	Z=1;
	
condition1=false;
value1=GetField("現股當沖張數","D")[Z];
value2=GetField("外資買賣超","D")[Z];
value3=GetField("投信買賣超","D")[Z];
value4=GetField("自營商買賣超","D")[Z];
value5=GetField("主力買賣超張數","D")[Z];
value6=GetField("融資增減張數","D")[Z];
value7=GetField("融券增減張數","D")[Z];
value8=volume-value1;//當日淨交易張數
value9=value2+value3+value4+value5-value6+value7;
//籌碼收集張數

if TSELSindex(10,5)[Z]=1 then begin
	if value8<>0 then 
		value10=value9/value8*100
	else
		value10=value10[1];
	
	value11=average(value10,10);
	if value11 crosses over 10 then condition1=true;

	stochastic(Length_D, 3, 3, rsv_d, kk_d, dd_d);
	xf_stochastic("W", Length_W, 3, 3, rsv_w, kk_w, dd_w);

	condition2 = kk_d crosses above dd_d;		// 日KD crosses over
	condition3 = xf_GetBoolean("W",xf_crossover("W", kk_w, dd_w),1);	// 周KD crosses over
	condition4 = kk_d[1] <= 30;							// 日K 低檔
	condition5 = xf_getvalue("W", kk_w, 1) <= 50;		// 周K 低檔
	
	if condition1 and condition2 and condition3 and condition4 and condition5
	then ret = 1;
end;
```

---


---

## 腳本檔案: 警示/短線操作型/除權前的逆襲.xs

```xs
{@type:sensor}
input:Ratio(5); setinputname(1,"逆襲上漲幅度%");
input:TXT1("僅適用日線"); setinputname(2,"使用限制");
input:TXT2("需選用逐筆洗價"); setinputname(3,"使用說明");
settotalbar(5);

if BarFreq = "D" and Close > Close[2] *(1+Ratio/100) and
   Close > Close[1] and Close[1] > Close[2]
then
begin
  if GetField("融券餘額張數")[1] = 0 and  GetField("融券餘額張數")[2] = 0 and 
     GetField("融資餘額張數")[1] >0 {推測是除權前停券} then ret=1; 
end;
```

---


---

## 腳本檔案: 警示/酒田戰法/三長下影線.xs

```xs
{@type:sensor}
input: Percent(1.5); setinputname(1,"下影線佔股價絕對百分比");
settotalbar(5);

condition1 = (minlist(open,close)-Low) > absvalue(open-close)*3; 
condition2 =  minlist(open, close)  > low* (100 + Percent)/100;

if trueall( condition1 and condition2, 3) then ret=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/三黑鴨.xs

```xs
{@type:sensor}
{																						
[檔名:]	三黑鴨			[資料夾:]	酒田戰法	[適用方向]	空															
[說明:]	連三黑K棒																																								
}		
settotalbar(5);																											
{判斷狀況}								
	condition1=	( open - close ) > (high -low) * 0.75					;//狀況1:	當期黑K棒
	condition2=	( open[1] - close[1] ) > (high[1] -low[1]) * 0.75					;//狀況2:	前期黑K棒
	condition3=	( open[2] - close[2] ) > (high[2] -low[2]) * 0.75					;//狀況3:	前前期黑K棒
	condition4=	close < close[1] and close[1] < close[2]					;//狀況4:	連續下跌	
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
	and	condition4
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/倒狀鎚子.xs

```xs
{@type:sensor}
{								
[檔名:]	倒狀鎚子			[資料夾:]	酒田戰法	[適用方向]	多	
[說明:]	前期收長黑K棒 今期開低試圖上攻後收上影線短紅棒												
}								
settotalbar(5);
{判斷狀況}								
	condition1=	( open[1] - close[1] ) >(high[1] -low[1]) * 0.75					;//狀況1:	前期出長黑K棒
	condition2=	 close[1] < close[2] - (high[2]-low[2])					;//狀況2:	前期呈波動放大下跌
	condition3=	close > open and (high -close)> (close-open) *2					;//狀況3:	收紅上影線
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/內困三日翻紅.xs

```xs
{@type:sensor}
{								
[檔名:]	內困三日翻紅			[資料夾:]	酒田戰法	[適用方向]	多	
[說明:]	黑K棒後內包前期短紅棒 當期再以紅棒突破黑棒開盤價												
}								
settotalbar(5);					
{判斷狀況}								
	condition1=	( open[2] - close[2] ) >(high[2] -low[2]) * 0.75					;//狀況1:	實體下跌K棒
	condition2=	( close[1] - open[1] ) >(high[1] -low[1]) * 0.75					;//狀況2:	實體上漲K棒
	condition3=	 high[1] < high[2] and low[1] > low[2]					;//狀況3:	前期內包於前前期
	condition4=	( close - open )  > 0.75 *(high -low)					;//狀況4:	當期實體上漲K棒
	condition5=	close > open[2]					;//狀況5:	現價突破前前期開盤價
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
	and	condition4
	and	condition5
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/內困三日翻黑.xs

```xs
{@type:sensor}
{																						
[檔名:]	內困三日翻黑			[資料夾:]	酒田戰法	[適用方向]	空															
[說明:]	前兩期為長紅棒後包黑K棒 當期往下跌破紅棒開盤價																																								
}	
settotalbar(5);																											
{判斷狀況}								
	condition1=	close[2] > open[2] + high[3]-low[3]					;//狀況1:	前前期長紅棒
	condition2=	high[2] < high[3] and low[2] > low[3]					;//狀況2:	前期內包黑K棒
	condition3=	open >= close[1] and close < open[2]					;//狀況3:	開平高跌破三日低點
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/十字線.xs

```xs
{@type:sensor}
{																						
[檔名:]	十字線			[資料夾:]	酒田戰法	[適用方向]	不指定															
[說明:]	K棒收十字線																																								
}																						
settotalbar(5);					
{判斷狀況}								
	condition1=	close =open					;//狀況1:	開盤價等於收盤價
	condition2=	high>open					;//狀況2:	有漲
	condition3=	low<open					;//狀況3:	有跌
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/吊人.xs

```xs
{@type:sensor}
{																						
[檔名:]	吊人			[資料夾:]	酒田戰法	[適用方向]	空															
[說明:]	短黑棒留長下影線																																								
}																						
settotalbar(5);						
{判斷狀況}								
	condition1=	open = High and close < open					;//狀況1:	開高收低留黑棒
	condition2=	(high -low) > 2 *(high[1]-low[1])					;//狀況2:	波動倍增
	condition3=	(close-low)> (open-close)  *2					;//狀況3:	下影線為實體兩倍以上
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/多頭三星.xs

```xs
{@type:sensor}
{																						
[檔名:]	多頭三星			[資料夾:]	酒田戰法	[適用方向]	多															
[說明:]	近三期開高低收皆呈Ｖ形排列																																								
}																						
settotalbar(5);							
{判斷狀況}								
	condition1=	open> open[1] and open[2]>open[1]					;//狀況1:	開盤價排列
	condition2=	high> high[1] and high[2]>high[1]					;//狀況2:	最高價排列
	condition3=	low> low[1] and low[2]>low[1]					;//狀況3:	最低價排列
	condition4=	close> close[1] and close[2]>close[1]					;//狀況4:	收盤價排列
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
	and	condition4
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/多頭吞噬.xs

```xs
{@type:sensor}
{																						
[檔名:]	多頭吞噬			[資料夾:]	酒田戰法	[適用方向]	多															
[說明:]	前期收短黑K棒 當期開低走高拉出長紅棒 波動率放大 穿過昨高																																									
}																												
settotalbar(5);	
{判斷狀況}								
	condition1=	( open[1] - close[1] ) >(high[1] -low[1])*0.75					;//狀況1:	前期出黑K棒
	condition2=	( close - open ) >(high -low) * 0.75					;//狀況2:	當期紅棒
	condition3=	high > high[1]					;//狀況3:	高過昨高
	condition4=	open<low[1]					;//狀況4:	開低破昨低	
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
	and	condition4
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/多頭執帶.xs

```xs
{@type:sensor}
{								
[檔名:]	多頭執帶			[資料夾:]	酒田戰法	[適用方向]	多	
[說明:]	開在最低點一路走高收在最高點附近的K棒												
}
settotalbar(5);																
{判斷狀況}								
	condition1=	close>open					;//狀況1:	
	condition2=	(Close-Open)>(high-low)*0.9					;//狀況2:	
	condition3=	Close>Close[1]+high[1]-low[1]					;//狀況3:	
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/多頭母子.xs

```xs
{@type:sensor}
{																						
[檔名:]	多頭母子			[資料夾:]	酒田戰法	[適用方向]	多															
[說明:]	前期收長黑K棒 今期開高小幅收紅不過昨高																					
}																						
settotalbar(5);	
{判斷狀況}								
	condition1=	( open[1] - close[1] ) >(high[1] -low[1])*0.75					;//狀況1:	前期出長黑K棒
	condition2=	close[1] < close[2] - high[2]-low[2]					;//狀況2:	前期呈波動放大下跌
	condition3=	( close - open ) >(high -low) * 0.75					;//狀況3:	當期紅棒
	condition4=	high < high[1]					;//狀況4:	高不過昨高
	condition5=	low>low[1]					;//狀況5:	低不破昨低
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
	and	condition4
	and	condition5
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/多頭遭遇.xs

```xs
{@type:sensor}
{																						
[檔名:]	多頭遭遇			[資料夾:]	酒田戰法	[適用方向]	多															
[說明:]	前期收黑K棒 當期開低走高紅棒嘗試反攻昨收 																																								
}
settotalbar(5);																														
{判斷狀況}								
	condition1=	 (open[1] - close[1] ) >(high[1] -low[1]) * 0.75					;//狀況1:	前期出黑K棒
	condition2=	close[1] < close[2]					;//狀況2:	前期收跌
	condition3=	( close - open ) >(high -low) * 0.75					;//狀況3:	當期收紅K棒
	condition4=	open  < close[1] and close < close[1]					;//狀況4:	開低且收跌
	condition5=	low <  low[1]					;//狀況5:	破前期低點
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
	and	condition4
	and	condition5
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/夜星.xs

```xs
{@type:sensor}
{																						
[檔名:]	夜星			[資料夾:]	酒田戰法	[適用方向]	空															
[說明:]	紅棒後 開高走低守平盤																																									
}
settotalbar(5);																														
{判斷狀況}								
	condition1=	 ( close[2] - open[2] ) > (high[2] -low[2]) * 0.75					;//狀況1:	前前期實體紅棒
	condition2=	close[2] > close[3] + (high[3]-low[3])					;//狀況2:	前前期波動放大
	condition3=	low[1] > high[2] and close[1]>open[1]					;//狀況3:	前期高開收紅
	condition4=	open < close[1] and close < open - (high[1]-low[1])					;//狀況4:	當期開低收黑K棒
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
	and	condition4
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/帶量倒狀鎚子.xs

```xs
{@type:sensor}
{								
[檔名:]	倒狀鎚子			[資料夾:]	酒田戰法	[適用方向]	多	
[說明:]	前期收長黑K棒 今期開低試圖上攻後收上影線短紅棒												
}														
settotalbar(5);	
{判斷狀況}								
	condition1=	( open[1] - close[1] ) >(high[1] -low[1]) * 0.75		;//狀況1:	前期出長黑K棒
	condition2=	 close[1] < close[2] - (high[2]-low[2])					;//狀況2:	前期呈波動放大下跌
	condition3=	close > open and (high -close)> (close-open) *2			;//狀況3:	收紅上影線	
	condition4 = Volume > Volume[1];									;//狀況4:	帶量
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
	and condition4
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/帶量吊人.xs

```xs
{@type:sensor}
{																						
[檔名:]	帶量吊人			[資料夾:]	酒田戰法	[適用方向]	空															
[說明:]	短黑棒留長下影線 量倍增																					
}																						
settotalbar(5);							
{判斷狀況}								
	condition1=	open = High and close < open					;//狀況1:	開高收低留黑棒
	condition2=	(high -low) > 2 *(high[1]-low[1])					;//狀況2:	波動倍增
	condition3=	(close-low)> (open-close)  *2					;//狀況3:	下影線為實體兩倍以上
	condition4=	Volume > Volume[1]					;//狀況4:		
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
	and	condition4
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/帶量多頭吞噬.xs

```xs
{@type:sensor}
{																						
[檔名:]	多頭吞噬			[資料夾:]	酒田戰法	[適用方向]	多															
[說明:]	前期收短黑K棒 當期開低走高拉出長紅棒 波動率放大 穿過昨高																																									
}																						
settotalbar(5);							
{判斷狀況}								
	condition1=	( open[1] - close[1] ) >(high[1] -low[1])*0.75					;//狀況1:	前期出黑K棒
	condition2=	( close - open ) >(high -low) * 0.75					;//狀況2:	當期紅棒
	condition3=	high > high[1]					;//狀況3:	高過昨高
	condition4=	open<low[1]					;//狀況4:	開低破昨低
	condition5=	Volume > Volume[1]*2					;//狀況5:	
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
	and	condition4
	and	condition5
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/帶量多頭執帶.xs

```xs
{@type:sensor}
{								
[檔名:]	帶量多頭執帶			[資料夾:]	酒田戰法	[適用方向]	多	
[說明:]	開在最低點一路走高收在最高點附近的K棒	衝出倍增量												
}								
settotalbar(5);								
{判斷狀況}								
	condition1=	close>open					;//狀況1:	
	condition2=	(Close-Open)>(high-low)*0.9					;//狀況2:	
	condition3=	Close>Close[1]+high[1]-low[1]					;//狀況3:	
	condition4=	Volume > Volume[1]*2					;//狀況4:		
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
	and	condition4
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/帶量空頭執帶.xs

```xs
{@type:sensor}
{																						
[檔名:]	帶量空頭執帶			[資料夾:]	酒田戰法	[適用方向]	空															
[說明:]	量倍增長黑棒																																									
}
settotalbar(5);																														
{判斷狀況}								
	condition1=	( open - close ) > (high -low) * 0.8					;//狀況1:	實體黑K棒
	condition2=	close < close[1] - (high[1]-low[1])					;//狀況2:	波動向下放大
	condition3=	Volume > Volume[1]*2					;//狀況3:		
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/帶量鎚頭.xs

```xs
{@type:sensor}
{									
[檔名:]	帶量鎚頭			[資料夾:]	酒田戰法	[適用方向]	多		
[說明:]	開盤後下跌試底,盤中拉升上攻後,收在高點留下下影線 衝出倍增量														
}													
settotalbar(5);	
{判斷狀況}								
	condition1=	close >=high	and 	close > open			;//狀況1:	收高
	condition2=	(high -low) > 2 *(high[1]-low[1])					;//狀況2:	波動放大
	condition3=	(open-low) > (close - open)  *2 					;//狀況3:	長下影線
	condition4=	Volume > Volume[1]*2					;//狀況4:	當期量倍增	
{結果判斷}									
IF									
		condition1							
	and	condition2							
	and	condition3							
	and	condition4														
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/晨星.xs

```xs
{@type:sensor}
{																						
[檔名:]	晨星			[資料夾:]	酒田戰法	[適用方向]	多															
[說明:]	前前期收長黑K棒 前期再開低震盪收短紅棒後  當期開高紅棒反攻起跌點 																																									
}																														
settotalbar(5);	
{判斷狀況}								
	condition1=	( open[2] - close[2] ) >(high[2] -low[2]) * 0.75					;//狀況1:	前前期出黑K棒
	condition2=	close[2] < close[3]-(high[3]-low[3])					;//狀況2:	跌勢擴大
	condition3=	( close - open ) >(high -low) * 0.75					;//狀況3:	當期收紅K棒
	condition4=	close> close[2]					;//狀況4:	收復黑棒收盤價
	condition5=	close[1] <= close[2] and close[1] < open					;//狀況5:	前低收盤為三期低點
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
	and	condition4
	and	condition5
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/空頭三星.xs

```xs
{@type:sensor}
{																						
[檔名:]	空頭三星			[資料夾:]	酒田戰法	[適用方向]	空															
[說明:]	開高低收A型排列																																										
}																												
settotalbar(5);	
{判斷狀況}								
	condition1=	open[1] > open[2] and open[1] > open					;//狀況1:	開盤價A型
	condition2=	high[1] > high[2] and high[1] > high					;//狀況2:	最高價A型
	condition3=	low[1] > low[2] and low[1] > low					;//狀況3:	最低價A型
	condition4=	close[1] > close[2] and close[1] > close					;//狀況4:	收盤價A型
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
	and	condition4
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/空頭吞噬.xs

```xs
{@type:sensor}
{																						
[檔名:]	空頭吞噬			[資料夾:]	酒田戰法	[適用方向]	空															
[說明:]	紅棒後 開高下跌破昨低收長黑K棒																																									
}																						
settotalbar(5);								
{判斷狀況}								
	condition1=	( close[1] - open[1] ) > (high[1] -low[1]) * 0.5					;//狀況1:	前期實體紅棒
	condition2=	 high-low >( high[1]-low[1])*2					;//狀況2:	當期波動倍曾
	condition3=	( open - close )>(high -low) * 0.75					;//狀況3:	當期黑K棒
	condition4=	open > close[1] and close < low[1]					;//狀況4:	開高下跌破昨低
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
	and	condition4
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/空頭執帶.xs

```xs
{@type:sensor}
{																						
[檔名:]	空頭執帶			[資料夾:]	酒田戰法	[適用方向]	空															
[說明:]	長黑棒																																									
}																						
settotalbar(5);	
{判斷狀況}								
	condition1=	( open - close ) > (high -low) * 0.8					;//狀況1:	實體黑K棒
	condition2=	close < close[1] - (high[1]-low[1])					;//狀況2:	波動向下放大
{結果判斷}		
IF		
		condition1
	and	condition2
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/空頭母子.xs

```xs
{@type:sensor}
{																						
[檔名:]	空頭母子			[資料夾:]	酒田戰法	[適用方向]	空															
[說明:]	長紅棒後 內包短黑K																																									
}																													
settotalbar(5);	
{判斷狀況}								
	condition1=	( close[1] - open[1] ) > (high[1] -low[1]) * 0.8					;//狀況1:	前期實體紅棒
	condition2=	close[1]> close[2] + high[2]-low[2]					;//狀況2:	前期波動向上放大
	condition3=	( open - close )>(high -low) * 0.5					;//狀況3:	當期黑K棒
	condition4=	high[1] > high and low[1] < Low 					;//狀況4:	高不過高 低不過低 內包K棒
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
	and	condition4
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/空頭流星.xs

```xs
{@type:sensor}
{																						
[檔名:]	空頭流星			[資料夾:]	酒田戰法	[適用方向]	空															
[說明:]	紅棒後 跳空開高收黑棒上影線																																								
}																						
settotalbar(5);						
{判斷狀況}								
	condition1=	open > close[1] and  close < open					;//狀況1:	開高且收黑
	condition2=	( close[1] - open[1] ) >(high[1] -low[1]) * 0.75					;//狀況2:	前期收實體紅K棒
	condition3=	close[1]> close[2]					;//狀況3:	當期收漲
	condition4=	(high - open ) > (open-close) * 2					;//狀況4:	留長上影線
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
	and	condition4
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/空頭遭遇.xs

```xs
{@type:sensor}
{																						
[檔名:]	空頭遭遇			[資料夾:]	酒田戰法	[適用方向]	空															
[說明:]	紅棒後 開高走低守平盤																					
}																													
settotalbar(5);	
{判斷狀況}								
	condition1=	( close[1] - open[1] ) > (high[1] -low[1]) * 0.5					;//狀況1:	前期實體紅棒
	condition2=	( open - close ) > (high -low) * 0.5					;//狀況2:	當期實體黑棒
	condition3=	open > high[1] and close > close[1]					;//狀況3:	開過昨高收守平盤	
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/紅三兵.xs

```xs
{@type:sensor}
{								
[檔名:]	紅三兵			[資料夾:]	酒田戰法	[適用方向]	多	
[說明:]	連續三根上漲實體K棒							
}															
settotalbar(5);	
{判斷狀況}								
	condition1=	( close - open ) >(high -low) * 0.75					;//狀況1:	實體上漲K棒
	condition2=	( close[1] - open[1] ) >(high[1] -low[1]) * 0.75					;//狀況2:	實體上漲K棒
	condition3=	( close[2] - open[2] ) >(high[2] -low[2]) * 0.75					;//狀況3:	實體上漲K棒
	condition4=	close > close[1]					;//狀況4:	上漲
	condition5=	close[1] > close[2]					;//狀況5:	上漲
{結果判斷}		
IF		
		condition1
	and	condition2
	and	condition3
	and	condition4
	and	condition5
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/蜻蜓十字.xs

```xs
{@type:sensor}
{																						
[檔名:]	蜻蜓十字			[資料夾:]	酒田戰法	[適用方向]	空															
[說明:]	T形線																					
}																						
settotalbar(5);							
{判斷狀況}								
	condition1=	close>=open and open>=high					;//狀況1:	開收高同價
	condition2=	(high-low)> close *0.01					;//狀況2:	波動大於1%
{結果判斷}		
IF		
		condition1
	and	condition2
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/鎚頭.xs

```xs
{@type:sensor}
{									
[檔名:]	鎚頭			[資料夾:]	酒田戰法	[適用方向]	多		
[說明:]	開盤後下跌試底,盤中拉升上攻後,收在高點留下下影線								
}																
settotalbar(5);	
{判斷狀況}								
	condition1=	close >=high	and 	close > open			;//狀況1:	收高
	condition2=	(high -low) > 2 *(high[1]-low[1])					;//狀況2:	波動放大
	condition3=	(open-low) > (close - open)  *2 					;//狀況3:	長下影線
{結果判斷}									
IF									
		condition1							
	and	condition2							
	and	condition3													
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/酒田戰法/長腳十字星.xs

```xs
{@type:sensor}
{																						
[檔名:]	長腳十字星			[資料夾:]	酒田戰法	[適用方向]	空															
[說明:]	大波動十字線																					
}																												
settotalbar(5);	
{判斷狀況}								
	condition1=	close>=open and open>=close					;//狀況1:	開收同價
	condition2=	(high-low)> close *0.015					;//狀況2:	波動大於1.5%
{結果判斷}		
IF		
		condition1
	and	condition2
THEN	RET=1;
```

---


---

## 腳本檔案: 警示/長線投資/多頭趨勢已然確立.xs

```xs
{@type:sensor}
input:CountMonth(6,"計算月數");
input:LSP(25,"多空切換百分比");

variable:pHigh(0),pLow(100000);

if  CurrentDate < DateAdd(Date,"M",CountMonth) then begin
	pHigh = maxlist(h,pHigh);
	pLow = minlist(l,pLow);
end else begin
	pHigh = C;
	pLow = C;
end;

value1= pHigh-(pHigh-pLow)*LSP/100;

if close>value1 
and close[1]<value1[1]
then ret=1;
```

---


---

## 腳本檔案: 警示/長線投資/大跌後的定存股標的.xs

```xs
{@type:sensor}
input:Length(200,"尋找高點期數");
input:percent(38.2,"自高點回檔幅度%");
 
if close < highest(high,Length)*(1- percent/100) then Ret=1;
```

---


---

## 腳本檔案: 警示/長線投資/獲利穩定的公司來到市值低位區.xs

```xs
{@type:sensor}
settotalbar(700);

if getsymbolfield("tse.tw","收盤價") > average(getsymbolfield("tse.tw","收盤價"),10) then begin
	value4=GetField("總市值");
	value5=average(value4,600);
	if value4[1]<value5[1]*0.7
	and close=highest(close,10)
	then ret=1;
end;
```

---
