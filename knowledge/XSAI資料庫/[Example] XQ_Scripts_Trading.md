# XQ 官方自動交易腳本範例庫

共 64 個自動交易腳本範例。

---

## 腳本檔案: 自動交易/0-基本語法/01-SetPosition.xs

```xs
{@type:autotrade}
{
	Position代表的是這個商品在這個策略內的’預期部位’, Position是一個整數, 可以大於0, 也可以小於0.
	
	**請注意: 一個交易策略內可以跑多個商品，每個商品的Position是獨立的**
	
	當我們想要執行交易時, 就呼叫SetPosition這一個函數, 傳入我們預期的部位(同時也可以傳入委託價格).
	
	腳本開始執行時, 商品的Position預設數值是0, 當我們想要買進時, 就透過SetPosition把Position變大, 想要賣出時, 就透過
	SetPosition把Position變小.
	
	系統收到了SetPosition()的呼叫之後, 就會依照目前的Position, 目前委託/成交的執行狀態, 決定如何送單, 來讓你的策略可以達到(成交)
	這個新的預期的部位.
		
	SetPosition()可以接受兩個參數:
	
	第一個參數是預期的部位,
	第二個參數是委託的價格, 這個參數如果不傳的話, 則會採用策略的預設買進/賣出價格
	
	請看以下範例
}

{
	把部位(Position)變成1, 如果原先部位是0的話, 則等於買進1張
	第二個參數(委託價格)如果不傳的話, 則使用策略設定內的預設價格	
}
SetPosition(1);	

{
	第二個參數可以傳入價格, MARKET是系統保留字, 代表是'市價'(期貨的話則會是'範圍市價')
}
SetPosition(1, MARKET);

{
	也可以傳入K棒的價格, 例如Close
}
SetPosition(1, Close);

{
	也可以傳入數值運算式
}
SetPosition(1, Close + 1.0);

{
	也可以傳入絕對值, 例如100.0
}
SetPosition(1, 100.0);

{
	支援檔位換算功能(AddSpread), 
	AddSpread(Close, 1)表示是Close價格往上加1檔, AddSpread(Close, 2)表示加2檔
	AddSpread(Close, -1)表示是Close價格往下減1檔
	
	AddSpread也可以用在警示腳本, 以及指標腳本
}
SetPosition(1, AddSpread(Close, 1));

{
	Position也可以是負的, 如果原先部位是0的話, 則等於賣出1張
}
SetPosition(-1);

{
	除了可以SetPosition之外, 也可以讀到目前的Position

	SetPosition(Position+1)表示是加碼1張
}
value1 = Position;
SetPosition(Position+1);

{	
	SetPosition的價格如果不符合商品的交易規則的話, 系統會自動轉換,
	例如: 如果超過漲停價, 則只會送出漲停價,
	例如: 如果不符合跳動點的話, 則會自動轉換到符合跳動點價格
}
SetPosition(1, 123.1);		{ 如果是買進台積電的話, 則會送出委託價格=123元 }
```

---


---

## 腳本檔案: 自動交易/0-基本語法/02-SetPosition範例#1(多單1口).xs

```xs
{@type:autotrade}
{
	範例: 
	
	當發生做多情境時, 買進1口
	做多後發生出場情境時, 多單出場(變成空手)
}

var: 
	long_condition(false), 		{ 是否做多 }
	exit_long_condition(false); { 是否多單出場 }

{ 
	Position=0時判斷是否要做多, 
	Position=1時判斷是否要出場 
}
if Position = 0 and long_condition then SetPosition(1);
if Position = 1 and exit_long_condition then SetPosition(0);
```

---


---

## 腳本檔案: 自動交易/0-基本語法/02-SetPosition範例#2(空單1口).xs

```xs
{@type:autotrade}
{
	範例: 
	
	當發生做空情境時, 賣出1口(做空)
	做空後發生出場情境時, 空單出場(變成空手)
}

var: 
	short_condition(false), 		{ 是否做空 }
	exit_short_condition(false);	{ 是否空單出場 }

{ 
	Position=0時判斷是否要做空, 
	Position=-1時判斷是否要回補 
}
if Position = 0 and short_condition then SetPosition(-1);
if Position = -1 and exit_short_condition then SetPosition(0);
```

---


---

## 腳本檔案: 自動交易/0-基本語法/02-SetPosition範例#3(多單1口+空單1口).xs

```xs
{@type:autotrade}
{
	範例

	當發生做多情境時, 把部位變成做多1口(如果此時是空手的話, 買進1口, 如果此時是做空1口的話, 回補這一口,同時買進1口)
	當發生做空情境時, 把部位變成做空1口(如果此時是空手的話, 賣出1口, 如果此時是做多1口的話, 賣出這一口,同時做空1口)
	
	做多後發生出場情境時, 多單出場(變成空手)
	做空後發生出場情境時, 空單出場(變成空手)

	這個是範例#1跟範例#2的綜合體, 可是包含了部位翻轉的邏輯(Position可能從-1變成1, 或是從1變成-1)
}

var: 
	long_condition(false), 			{ 是否做多 }
	exit_long_condition(false), 	{ 是否多單出場 }
	short_condition(false), 		{ 是否做空 }
	exit_short_condition(false);	{ 是否空單出場 }

if Position <> 1 and long_condition then begin
	{ 如果符合做多情境(long_condition), 則把部位變成1 (可能是0->1 or -1->1) }
	SetPosition(1);

end else if Position <> -1 and short_condition then begin
	{ 如果符合做空情境(short_condition), 則把部位變成-1 (可能是0->-1 or 1->-1) }
	SetPosition(-1);

end else if Position = 1 and exit_long_condition then begin
	{ 如果已經做多, 且發生多方出場情形時(exit_long_condition), 則把部位變成0 }
	SetPosition(0);

end else if Position = -1 and exit_short_condition then begin
	{ 如果已經做空, 且發生空方出場情形時(exit_short_condition), 則把部位變成0 }
	SetPosition(0);
end;
```

---


---

## 腳本檔案: 自動交易/0-基本語法/03-Filled.xs

```xs
{@type:autotrade}
{
    Filled是Position的另外一個朋友, 代表這個策略內/這個執行商品的成交部位
    
    假設剛開始執行時, 腳本的Position是0的話, 此時Filled也會是0

    接下來當腳本執行SetPosition(1)後, 會送出一筆買進1張的委託

    如果此時尚未成交的話, Position會等於1, 可是Filled會等於0
    如果這一筆委託單成交的話, 則Position會等於1, Filled也會等於1    
    
    如果腳本內想要判斷目前成交狀態的話, 就可以透過讀取Filled這個變數來判斷.
}

{ 以下假設策略啟動時商品的Postion = 0 }

if Position = 1 and Filled = 0 then begin
    { 已經送出一筆買進1張的委託, 可是還沒有成交}

end;

if Position = 1 and Filled = 1 then begin
    { 已經送出一筆買進1張的委託, 而且這一筆委託已經成交 }

end;

if Position = -1 and Filled = 0 then begin
    { 已經送出一筆賣出1張的委託, 可是還沒有成交 }

end;

if Position = -1 and Filled = -1 then begin
    { 已經送出一筆賣出1張的委託, 而且這一筆委託已經成交 }
    
    { Filled跟Position一樣, 可能會大於0, 也可能會小於0 }
end;
```

---


---

## 腳本檔案: 自動交易/0-基本語法/04-SetPosition範例#4(追價).xs

```xs
{@type:autotrade}
{
	範例: 透過Filled來判斷是否需要追價
	
	當發生做多情境時, 買進1口
	如果發生出場情境時, 多單出場(變成空手)
	如果買進委託沒有成交的話, 則追價

}


{
	當腳本呼叫SetPosition的話, 系統會依照目前委託/成交的情形, 決定如何送出委託單.
	
    以下情境假設一開始執行時Position = 0. 

	情境#1
	
	腳本呼叫SetPosition(1)時, 系統送出一筆買進1口的委託單
	經過一段時間後, 腳本呼叫SetPosition(0), 此時會發生以下的情形
	
	- 如果剛剛那一筆委託單已經成交(Position=1, Filled=1), 接下來SetPosition(0), 就會送出一筆賣出1口的委託
	- 如果剛剛那一筆委託單還沒有成交(Position=1, Filled=0), 接下來SetPosition(0), 就會**刪除買進的那一筆委託**
	  (這樣子的話, 使用者的部位就剛好是0)
	
	情境#2
	
	腳本呼叫SetPosition(1)時, 系統送出一筆買進1口的委託單
	經過一段時間後, 腳本又呼叫SetPosition(1), 此時會發生以下的情形

	- 如果剛剛那一筆委託單已經成交(Position=1, Filled=1), 接下來SetPosition(1), 不會送出任何委託
	- 如果剛剛那一筆委託單還沒有成交(Position=1, Filled=0), 接下來SetPosition(1), 系統會執行以下的邏輯
		- 如果新的SetPosition(1)的委託價格跟先前的委託價格**不一樣**的話, 則刪除剛剛的委託, 
		  然後送出一筆買進1口的委託單(使用新的委託價格)
		- 如果新的SetPosition(1)的委託價格跟先前的委託價格一樣的話, 則不會做任何動作

	情境#3

	腳本呼叫SetPosition(2)時, 送出一筆買進2口的委託單
	經過一段時間後, 腳本又呼叫SetPosition(3), 此時會發生以下的情形
	
	- 如果剛剛那一筆委託單已經完全成交(Position=2, Filled=2)
		- 接下來SetPosition(3), 就會送出一筆買進1口的委託
	- 如果剛剛那一筆委託單都沒有成交(Position=2, Filled=0)
		- 接下來SetPosition(3), 就會刪除先前的委託, 然後送出一筆買進3口的委託
	- 如果剛剛那一筆委託單部分成交(Position=2, Filled=1)
		- 接下來SetPosition(3), 就會刪除先前的委託, 然後送出一筆買進2口的委託
	
	小結:
	
	如果Position跟Filled一樣的話, 這個表示先前送出的委託都已經完全成交, 或是已經被取消. 
	此時如果收到新的SetPosition()的話, 系統的動作是送出一筆買進或是賣出的委託

	如果Position跟Filled不一樣的話, 這個表示目前應該有一筆[尚未完全成交的委託], 如果此時收到新的SetPosition()的話,
	系統會先刪除目前這一筆委託, 確認這一筆委託的成交數量之後, 再依照新的需求決定如何送單.
	
}

var: 
	long_condition(false), 		{ 是否做多 }
	exit_long_condition(false); { 是否多單出場 }


if Position = 0 and long_condition then begin
	{ 如果目前是空手, 且符合做多情境(long_condition), 則以目前收盤價買進1口, }
	SetPosition(1, Close);

end else if Position = 1 and exit_long_condition then begin
	SetPosition(0);

	{ 多單出場: 如果已經買到了, 就賣出剛剛買到的1口, 如果還沒有買到, 就取消買進的委託單 }
	
end else if Position = 1 and Filled = 0 then begin

	{ 如果已經送出買進委託, 可是還沒有成交的話, 則追價(系統會刪除先前委託, 然後再送出買進1張) }
	
	SetPosition(1, Close);

	{ 為了確保委託單排隊的順序, 如果新的委託價跟先前委託價格一樣的話, 系統就不會執行委託異動的動作 }

end;
```

---


---

## 腳本檔案: 自動交易/0-基本語法/04-SetPosition範例#5(加碼).xs

```xs
{@type:autotrade}
{
	範例: 透過Filled來判斷是否要加碼
	
	當發生做多情境時, 買進1口
	買進成交後, 如果發生加碼情境時, 再買進1口,
	如果發生出場情境時, 多單出場(變成空手, 部位=0)
}

var: 
	long_condition(false), 			{ 是否做多 }
	raise_long_condition(false),	{ 是否多單加碼 }
	exit_long_condition(false); 	{ 是否多單出場 }


if Position = 0 and long_condition then begin
	{ 目前Position=0, 而且發生做多情境, 買進1口 }
	SetPosition(1);
	
end else if Position <> 0 and exit_long_condition then begin
	{ 已經買進, 而且發生多單出場情境, 賣出所有部位 }
	{ 請注意, Position可能是1 or 2, 所以用 <> 0 來判斷 }
	SetPosition(0);
	
end else if Position = 1 and Filled = 1 and raise_long_condition then begin
	{ 已經買進1口, 而且也成交了, 此時發生加碼情境, 所以再買進1口}
	
	SetPosition(2);
	
	{ 也可以寫成 SetPosition(position + 1) }
end;
```

---


---

## 腳本檔案: 自動交易/0-基本語法/05-FilledAvgPrice以及停損停利範例.xs

```xs
{@type:autotrade}
{
	除了可以使用Filled來知道目前的成交部位之外, 
	也可以透過FilledAvgPrice這個函數來取得目前"未平倉"部位的成本	
}

{
	範例: 多單1口進場後, +1.5%停利, -1.5%停損
}

var: 
	long_condition(false); 		{ 是否做多 }


if Position = 0 and long_condition then SetPosition(1);

if Position = 1 and Filled = 1 then begin		
	{ 多單已經買進1口 }

	{ 計算損益% }
	var: plratio(0);

	{ 
		請注意: 不管Filled是大於0還是小於0, FilledAvgPrice的數值都是'正數'(>0) 
	}
	plratio = 100 * (Close - FilledAvgPrice) / FilledAvgPrice;
	
	if plratio >= 1.5 then SetPosition(0);		{ 停利 }
	if plratio <= -1.5 then SetPosition(0);		{ 停損 }
end;	

{
	目前計算未平倉成本的方式是採用**先進先出的沖銷方式**來計算, 以下是沖銷順序的範例:
	
	範例#1
	
	假設策略執行過程總共產生三筆成交, 依照時間先後順序, 資料分別為
	
	- 第一筆: 買進1張, 成交價100元,
	- 第二筆: 買進1張, 成交價102元,
	- 第三筆: 賣出1張, 成交價101元
	
	在第一筆成交時, Filled = 1, FilledAvgPrice = 100
	在第二筆成交時, Filled = 2, FilledAvgPrice = (100 + 102) / 2 = 101
	在第三筆成交時, Filled = 1, FilledAvgPrice = 102 (第三筆-1沖銷第一筆+1, 所以未平倉剩下第二筆1張, 未平倉成本=102)
	
	
	範例#2
	
	假設策略執行過程總共產生四筆成交, 依照時間先後順序, 資料分別為
	
	- 第一筆: 買進2張, 成交價100元,
	- 第二筆: 買進2張, 成交價101元,
	- 第三筆: 買進2張, 成交價102元,
	- 第四筆: 賣出3張, 成交價101元,
	
	在第一筆成交時, Filled = 2, FilledAvgPrice = 100
	在第二筆成交時, Filled = 4, FilledAvgPrice = (100*2 + 101*2) / 4 = 100.5
	在第三筆成交時, Filled = 6, FilledAvgPrice = (100*2 + 101*2 + 102*2) / 6 = 101
	在第四筆成交時, Filled = 3, FilledAvgPrice = (101*1 + 102 * 2) / 3 = 101.66666
	(第一筆成交的2張被沖銷, 第二筆成交的1張被沖銷)

}
```

---


---

## 腳本檔案: 自動交易/0-基本語法/06-FilledRecord函數.xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 自動交易/0-基本語法/07-Position跟Filled的異動時機點.xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 自動交易/0-基本語法/08-Alert.xs

```xs
{@type:autotrade}
{
	Alert語法
	
	在交易腳本內也可以透過Alert語法產生'通知'. 	
}

var: alert_condition(false);		{ 何時通知 }

if alert_condition then begin
	{ 呼叫Alert函數, 傳入要通知的訊息 }
	alert("這是我想要顯示的通知訊息");
	
	{ 也可以一次傳入多個參數, 系統會把這些參數串連成一個字串, 用空白字元來分隔 }
	
	alert("目前Bar時間=", FormatTime("HH:mm", Time));
end;

{ 
	
	Alert的通知會出現在以下的畫面內
	
	a. 自動交易中心, 策略執行記錄內(類別為警示)
	b. 即時監控畫面(請記得來源要勾選'自動交易')
	c. 警示提示視窗(請記得來源要勾選'自動交易')
	
	如果自動交易策略啟動推播的話, Alert也會傳送到手機端		
}
```

---


---

## 腳本檔案: 自動交易/0-基本語法/09-CancelAllOrders.xs

```xs
{@type:autotrade}
{
此為 CancelAllOrders 的範例腳本
腳本將會在啟動時直接下出委託價為跌停價的買進委託 (只會委託一次)，若委託未成交的話則在N分鐘以後刪除委託。
需注意會依照策略設定和商品洗價而有所差異，並不一定會準時在N分鐘後刪除
}

Input: _n(5, "幾分鐘後刪除委託");

if _n < 0 then RaiseRunTimeError("設定分鐘需要大於0");

var: IntraBarPersist _time(0);

//啟動後進入交易指令可執行的區間後下單並計算出場時間
Once(Position = 0 and Filled = 0 and GetInfo("TradeMode") = 1) begin   
    SetPosition(1, GetField("跌停價", "D"), label:="跌停價買進委託");
    _time = TimeAdd(CurrentTime, "M", _n);
	end;    

//當洗價時
if CurrentTime > _time and Position <> Filled then CancelAllOrders(label:="刪除跌停價買進委託");
```

---


---

## 腳本檔案: 自動交易/1-常用下單方式/01-市價交易.xs

```xs
{@type:autotrade}
{
	市價交易
}

var: long_condition(false);			{ 進場買進作多 }
var: exit_long_condition(false);	{ 多單出場 }

{ 
	範例:
	
	均線穿越時以市價買進1張
	均線跌破時以市價賣出(1張)
}

long_condition = Average(Close, 5) cross over Average(Close, 20);
exit_long_condition = Average(Close, 5) cross under Average(Close, 20);	

if Position = 0 and long_condition then begin
	SetPosition(1, MARKET);		{ 以市價買進 }
end;

if Position = 1 and exit_long_condition then begin
	SetPosition(0, MARKET);		{ 以市價賣出 }
end;
```

---


---

## 腳本檔案: 自動交易/1-常用下單方式/02-金額換算.xs

```xs
{@type:autotrade}
{
	以金額計算交易數量
}

input: ordersize_w(10, "每筆交易金額(萬)");

{ 
	範例:
	
	均線穿越時以指定金額換算張數買進
	均線跌破時以市價賣出全部數量
}

var: long_condition(false);			{ 進場買進作多 }
var: exit_long_condition(false);	{ 多單出場 }


long_condition = Average(Close, 5) cross over Average(Close, 20);
exit_long_condition = Average(Close, 5) cross under Average(Close, 20);	

if Position = 0 and long_condition then begin
	var: order_price(0);		{ 預期委託價格 }
	var: order_qty(0);			{ 換算後數量 }
	
	order_price = AddSpread(Close, 1);	
	order_qty = (ordersize_w * 10000) / (order_price * 1000);
								{ 計算出來的數值如果不是整數, 傳入SetPosition時會自動捨去小數位數 }
								{ 例如 SetPosition(2.5) 執行時會被轉成 SetPosition(2) }

	SetPosition(order_qty, order_price);		{ 以指定價格買入指定數量 }
end;

if Position <> 0 and exit_long_condition then begin
	SetPosition(0, MARKET);		{ 以市價賣出全部數量 }
end;
```

---


---

## 腳本檔案: 自動交易/1-常用下單方式/03-全部賣出.xs

```xs
{@type:autotrade}
{
	多單全部賣出
}

var: long_condition(false);			{ 進場買進作多 }
var: exit_long_condition(false);	{ 多單全部出場 }

{ 
	範例:
	
	多單進場: 每次遇到均線穿越或是連續上漲3筆時就買進1張(可以買進很多張, 沒有限制)
	均線跌破時賣出全部
}

long_condition = 
	Average(Close, 5) cross over Average(Close, 20) or
	TrueAll(Close > Close[1], 3);
	
exit_long_condition = Average(Close, 5) cross under Average(Close, 20);	

if long_condition then begin
	SetPosition(Position + 1);		{ 多單+1: 使用預設買進價格 }
									{ SetPosition(Position+1)的意思就是比目前部位多買1筆 }
									{ 也可以使用 Buy(1), 代表多單加碼1張 }
end;

if Position > 0 and exit_long_condition then begin
	SetPosition(0);					{ 多單全部出場: 把Position調成0, 使用預設賣出價格 }
end;
```

---


---

## 腳本檔案: 自動交易/1-常用下單方式/04-全部回補.xs

```xs
{@type:autotrade}
{
	空單全部回補
}

var: short_condition(false);		{ 進場賣出做空 }
var: exit_short_condition(false);	{ 空單全部回補 }

{ 
	範例:
	
	空單做空: 每次遇到均線跌破或是連續下跌3筆時就賣出1張(可以做空很多張, 沒有限制)
	均線穿越時回補全部空單
}

short_condition = 
	Average(Close, 5) cross under Average(Close, 20) or
	TrueAll(Close < Close[1], 3);
	
exit_short_condition = Average(Close, 5) cross over Average(Close, 20);	

if short_condition then begin
	SetPosition(Position - 1);		{ 空單+1: 使用預設賣出價格 }
									{ SetPosition(Position-1)的意思就是比目前部位多賣1筆 }
									{ 也可以使用Short(1), 代表空單加碼1張 }
	
end;

if Position < 0 and exit_short_condition then begin
	SetPosition(0);					{ 空單全部回補: 把Position調成0, 使用預設買進價格 }
end;
```

---


---

## 腳本檔案: 自動交易/1-常用下單方式/05-多單減碼.xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 自動交易/1-常用下單方式/06-空單減碼.xs

```xs
{@type:autotrade}
{
	空單減碼
}

var: short_one_condition(false);	{ 空單加碼1張 }
var: reduce_one_condition(false);	{ 空單減碼(回補)1張}
var: exit_short_condition(false);	{ 空單全部回補 }

{ 
	範例:
	
	空單進場: 每次連續下跌3筆時就賣出1張(可以賣出很多張, 沒有限制)
	空單減碼: 每次連續上漲3筆時就減碼(回補)1張(最多減碼到0)
	均線穿越時回補全部
}

short_one_condition = TrueAll(Close < Close[1], 3);
reduce_one_condition = TrueAll(Close > Close[1], 3);	
exit_short_condition = Average(Close, 5) cross over Average(Close, 20);	

if short_one_condition then begin
	Short(1);						{ 空單+1: 使用預設賣出價格 }
end;

if Position < 0 then begin
	{ 請注意: 因為可能同時會符合空單出場以及空單減碼的情形, 所以邏輯上要依照優先順序檢查. }
	if exit_short_condition then begin
		SetPosition(0);				{ 空單全部出場: 把Position調成0, 使用預設買進價格 }
	end else if reduce_one_condition then begin
		Cover(1);					{ 空單回補1張, 使用預設的買進價格 }
	end;
end;
```

---


---

## 腳本檔案: 自動交易/1-常用下單方式/07-多單加碼.xs

```xs
{@type:autotrade}
{
	多單加碼
}

var: long_condition(false);			{ 進場買進作多 }
var: add_one_condition(false);		{ 多單加碼1張 }
var: exit_long_condition(false);	{ 多單全部出場 }

{ 
	範例:
	
	多單進場: 均線穿越做多1張(部位最多=1)
	多單加碼: 如果已經做多, 又連續上漲3筆, 則加碼1張
	均線跌破時賣出全部
}

long_condition = Average(Close, 5) cross over Average(Close, 20);
add_one_condition = TrueAll(Close > Close[1], 3);	
exit_long_condition = Average(Close, 5) cross under Average(Close, 20);	

if Position = 0 and long_condition then begin
	SetPosition(1);					{ 多單1張: 使用預設買進價格 }
end;

if Position = 1 and add_one_condition then begin
	SetPosition(2);					{ 加碼1張變成2張 }
end;

if Position > 0 and exit_long_condition then begin
	SetPosition(0);					{ 多單全部出場: 把Position調成0, 使用預設賣出價格 }
end;
```

---


---

## 腳本檔案: 自動交易/1-常用下單方式/08-空單加碼.xs

```xs
{@type:autotrade}
{
	多單加碼
}

var: short_condition(false);		{ 做空進場 }
var: add_one_condition(false);		{ 空單加碼1張 }
var: exit_short_condition(false);	{ 空單全部出場 }

{ 
	範例:
	
	空單進場: 均線跌破時做空1張(部位最多=-1)
	空單加碼: 如果已經做空, 又連續下跌3筆, 則加碼1張
	均線突破時全部回補
}

short_condition = Average(Close, 5) cross under Average(Close, 20);
add_one_condition = TrueAll(Close < Close[1], 3);	
exit_short_condition = Average(Close, 5) cross over Average(Close, 20);	

if Position = 0 and short_condition then begin
	SetPosition(-1);				{ 空單1張: 使用預設賣出價格 }
end;

if Position = -1 and add_one_condition then begin
	SetPosition(-2);				{ 空單加碼1張變成-2 }
end;

if Position < 0 and exit_short_condition then begin
	SetPosition(0);					{ 空單全部出場: 把Position調成0, 使用預設買進價格 }
end;
```

---


---

## 腳本檔案: 自動交易/1-常用下單方式/09-刪單.xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 自動交易/1-常用下單方式/10-改價.xs

```xs
{@type:autotrade}
{
	修改尚未完全成交的委託的價格
}

var: long_condition(false);		{ 進場買進作多 }
var: exit_long_condition(false);{ 多單全部出場 }

{ 
	範例:
	
	均線穿越時以短天期的均線價格買進1張
	如果等了三根K棒都沒有成交則以目前的市場價格追價
	均線跌破時多單全部平倉
}

value1 = Average(Close, 5);
value2 = Average(Close, 20);
long_condition = value1 cross over value2;
exit_long_condition = value1 cross under value2;	

if Position = 0 and long_condition then begin
	SetPosition(1, value1);		{ 以5日均線的價格買進 }
end;

if Position = 1 and exit_long_condition then begin
	SetPosition(0);				{ 多單全部平倉 }
end else if Position = 1 and TrueAll(Position <> Filled, 3) then begin
	{ 
		送出買進委託後, Position = 1, 如果成交了, Filled = 1,
		Position <> Filled 在這裡則代表著委託已經送出, 可是還沒有成交,
	
		Position, Filled, 跟value1, value2, Close一樣, 都是一個"序列",
		
		所以Position[1]是上一根K棒最後的Position, Filled[1]是上一根K棒最後的Filled,
		
		所以TrueAll(Position <> Filled, 3) 代表著連續三根K棒都沒有成交 			
	}
	SetPosition(1, Close);		{ 修改委託價格為目前成交價 }
end;
```

---


---

## 腳本檔案: 自動交易/2-下單出場方式/01-收盤前平倉.xs

```xs
{@type:autotrade}
{
	收盤前平倉
}

input: exit_period(2, "收盤前N分鐘平倉");

var: long_condition(false);			{ 進場買進作多 }
var: exit_long_condition(false);	{ 多單出場 }
var: market_close_condition(false); { 是否已經進入收盤階段 }

{ 
	範例:
	
	均線穿越時買進1張
	均線跌破時賣出
	進場後如果連續下跌3筆時賣出
	收盤前N分鐘如果還有部位的話賣出(當日部位一定歸0)
}

long_condition = Average(Close, 5) cross over Average(Close, 20);
exit_long_condition = Average(Close, 5) cross under Average(Close, 20);	

{ 判斷是否已經進入收盤階段 }
market_close_condition = EnterMarketCloseTime(exit_period);

if Position = 0 and long_condition and not market_close_condition then begin
	SetPosition(1);				{ 買進1張: 請注意如果接近收盤時間, 則不進場 }
end else if Position = 1 and exit_long_condition then begin
	SetPosition(0);				{ 出場 }
end else if Position = 1 and market_close_condition then begin
	SetPosition(0);				{ 進入收盤階段: 出場 }
end;
```

---


---

## 腳本檔案: 自動交易/2-下單出場方式/02-多單固定停利停損(點).xs

```xs
{@type:autotrade}
{
	多單停損(點)
}

input: profit_point(10, "停利(點)");
input: loss_point(10, "停損(點)");

var: long_condition(false);			{ 進場買進作多 }

{ 
	範例:
	
	均線穿越時以市價買進1張
	以成交價為基礎, 設定固定的停損/停利價格, 觸及時出場
}

long_condition = Average(Close, 5) cross over Average(Close, 20);

if Position = 0 and long_condition then begin
	SetPosition(1, MARKET);		{ 以市價買進 }
end;

if Position = 1 and Filled = 1 then begin
	{ 依照成本價格設定停損/停利 }
	
	if profit_point > 0 and Close >= FilledAvgPrice + profit_point then begin
		{ 停利 }
		SetPosition(0);
	end else if loss_point > 0 and Close <= FilledAvgPrice - loss_point then begin	
		{ 停損 }
		SetPosition(0);
	end;
end;
```

---


---

## 腳本檔案: 自動交易/2-下單出場方式/03-空單固定停利停損(點).xs

```xs
{@type:autotrade}
{
	空單停損(點)
}

input: profit_point(10, "停利(點)");
input: loss_point(10, "停損(點)");

var: short_condition(false);			{ 進場做空 }

{ 
	範例:
	
	均線跌破時以市價賣出1張做空
	以成交價為基礎, 設定固定的停損/停利價格, 觸及時出場
}

short_condition = Average(Close, 5) cross under Average(Close, 20);

if Position = 0 and short_condition then begin
	SetPosition(-1, MARKET);		{ 以市價賣出 }
end;

if Position = -1 and Filled = -1 then begin
	{ 依照成本價格設定停損/停利: 請注意當作空時, 判斷是否獲利的方向要改變 }
	
	if profit_point > 0 and Close <= FilledAvgPrice - profit_point then begin
		{ 停利 }
		SetPosition(0);
	end else if loss_point > 0 and Close >= FilledAvgPrice + loss_point then begin	
		{ 停損 }
		SetPosition(0);
	end;
end;
```

---


---

## 腳本檔案: 自動交易/2-下單出場方式/04-多單固定停利停損(%).xs

```xs
{@type:autotrade}
{
	多單停損(%)
}

input: profit_percent(2, "停利(%)");
input: loss_percent(2, "停損(%)");

var: long_condition(false);			{ 進場買進作多 }

{ 
	範例:
	
	均線穿越時以市價買進1張
	以成交價為基礎, 設定固定的停損/停利價格, 觸及時出場
}

long_condition = Average(Close, 5) cross over Average(Close, 20);

if Position = 0 and long_condition then begin
	SetPosition(1, MARKET);		{ 以市價買進 }
end;

if Position = 1 and Filled = 1 then begin
	{ 依照成本價格設定停損/停利 }
	
	if profit_percent > 0 and Close >= FilledAvgPrice*(1+0.01*profit_percent) then begin
		{ 停利 }
		SetPosition(0);
	end else if loss_percent > 0 and Close <= FilledAvgPrice*(1-0.01*loss_percent) then begin	
		{ 停損 }
		SetPosition(0);
	end;
end;
```

---


---

## 腳本檔案: 自動交易/2-下單出場方式/05-空單固定停利停損(%).xs

```xs
{@type:autotrade}
{
	空單停損(%)
}

input: profit_percent(2, "停利(%)");
input: loss_percent(2, "停損(%)");

var: short_condition(false);			{ 進場做空 }

{ 
	範例:
	
	均線跌破時以市價賣出1張做空
	以成交價為基礎, 設定固定的停損/停利價格, 觸及時出場
}

short_condition = Average(Close, 5) cross under Average(Close, 20);

if Position = 0 and short_condition then begin
	SetPosition(-1, MARKET);		{ 以市價賣出 }
end;

if Position = -1 and Filled = -1 then begin
	{ 依照成本價格設定停損/停利: 請注意當作空時, 判斷是否獲利的方向要改變 }
	
	if profit_percent > 0 and Close <= FilledAvgPrice*(1-0.01*profit_percent) then begin
		{ 停利 }
		SetPosition(0);
	end else if loss_percent > 0 and Close >= FilledAvgPrice*(1+0.01*loss_percent) then begin	
		{ 停損 }
		SetPosition(0);
	end;
end;
```

---


---

## 腳本檔案: 自動交易/2-下單出場方式/06-多單移動停損(點).xs

```xs
{@type:autotrade}
{
	多單移動停損(點)

	設定停損點, 跟停利點(如果不設定停利的話請把profit_point設定成0)
	價格碰觸到停損/停利點時出場
	如果價格上漲時, 停損點會跟著上漲	
}

input: profit_point(10, "停利(點)");
input: loss_point(10, "停損(點)");

var: long_condition(false);			{ 進場買進作多 }

{ 
	範例:
	
	均線穿越時買進1張
	以成交價為基礎, 設定固定停利以及移動停損
}

if loss_point = 0 then raiseruntimeerror("請設定停損(點)");

long_condition = Average(Close, 5) cross over Average(Close, 20);

if Position = 0 and long_condition then begin
	SetPosition(1);				{ 買進1張 }
end;

if Position = 1 and Filled = 1 then begin
	{ 依照成本價格設定停損/停利 }
	var: intrabarpersist stoploss_point(0);
	
	{ 計算停損價格 }
	if stoploss_point = 0 then begin
		stoploss_point = FilledAvgPrice - loss_point;
	end;
	
	{ 如果價格上漲的話, 則往上挪動停損價格. 停損價格只會越來越高 }
	if Close > FilledAvgPrice then begin
		if Close - loss_point > stoploss_point then begin
			stoploss_point = Close - loss_point;
		end;	
	end;	
	
	if profit_point > 0 and Close >= FilledAvgPrice + profit_point then begin
		{ 停利 }
		SetPosition(0);
		stoploss_point = 0;
	end else if Close <= stoploss_point then begin
		{ 停損 }
		SetPosition(0);
		stoploss_point = 0;
	end;
end;
```

---


---

## 腳本檔案: 自動交易/2-下單出場方式/07-空單移動停損(點).xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 自動交易/2-下單出場方式/08-多單移動停利(點).xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 自動交易/2-下單出場方式/09-空單移動停利(點).xs

```xs
{@type:autotrade}
{
	空單移動停利(點)

	設定停損點(如果不設定的話, 請把loss_point設定成0), 以及停利點, 跟回跌點數
	價格上漲到停損時出場
	價格下跌停利點後啟動移動停利, 如果價格繼續下跌, 則繼續持有, 如果價格回檔超過回跌點數時, 則停利出場
}

input: profit_point(10, "停利(點)");
input: profit_drawback_point(5, "停利回跌(點)");
input: loss_point(10, "停損(點)");

var: short_condition(false);		{ 進場買空 }

{ 
	範例:
	
	均線跌破時做空賣出1張
	以成交價為基礎, 設定固定停損以及移動停利
}

if profit_point = 0 then raiseruntimeerror("請設定停利(點)");
if profit_drawback_point = 0 then raiseruntimeerror("請設定停利回跌(點)");
if profit_drawback_point > profit_point then raiseruntimeerror("停利(點)需大於停利回跌(點)");

short_condition = Average(Close, 5) cross under Average(Close, 20);

if Position = 0 and short_condition then begin
	SetPosition(-1);			{ 做空賣出1張 }
end;

if Position = -1 and Filled = -1 then begin
	var: intrabarpersist max_profit_point(0);	{ 啟動停利後最大獲利點 }

	if loss_point > 0 and Close >= FilledAvgPrice + loss_point then begin
		{ 停損 }
		SetPosition(0);
		max_profit_point = 0;

	end else begin
	
		{ 判斷是否要啟動停利 }
		if max_profit_point = 0 and Close <= FilledAvgPrice - profit_point then begin
			max_profit_point = Close;
		end;
		
		if max_profit_point <> 0 then begin		
			if Close >= max_profit_point + profit_drawback_point then begin
				{ 停利 }
				SetPosition(0);
				max_profit_point = 0;
			end else if Close < max_profit_point then begin
				{ 移動最大獲利點 }
				max_profit_point = Close;
			end;	
		end;		
	end;

end;
```

---


---

## 腳本檔案: 自動交易/3-Algo策略委託/01-定時定量交易.xs

```xs
{@type:autotrade}
{
	定時定量: 每隔多久送出一筆委託, 下多少筆之後就停止
	
	輸入參數:

	- 下單間隔 (order_interval: 每隔幾(秒)送出一筆委託)
	- 下單數量 (order_qty: 每一筆委託的數量)
	- 買賣方向 (order_bs: 1=買進, -1=賣出)
	- 委託筆數 (order_count: 總共要送出幾筆)	

	
}

input: order_interval(60, "下單間隔(秒)");
input: order_qty(1, "每次下單數量");
input: order_bs(1, "買賣方向", inputKind:=Dict(["買進", 1], ["賣出", -1]));
input: order_count(10, "下單筆數");

{ 
	範例:
	
	策略一啟動就啟動定時定量交易, 全部送完就停止
}

var: intrabarpersist exec_order_started(false);
var: intrabarpersist exec_order_lasttime(0);
var: intrabarpersist exec_order_count(0);

if not exec_order_started and GetInfo("TradeMode") = 1 then begin
	exec_order_started = true;		{ 啟動定時定量委託 }
	exec_order_count = 0;
	exec_order_lasttime = 0;
end;

{ 定時定量的執行邏輯 }
if exec_order_started and exec_order_count < order_count then begin
	if exec_order_lasttime = 0 or TimeDiff(CurrentTime, exec_order_lasttime, "S") >= order_interval then begin
		{ 執行委託 }
		Print("order_bs=", order_bs, "order_qty=", order_qty);
		SetPosition(position + order_bs * order_qty);			{ TODO: 請填入委託價格 }
		exec_order_count = exec_order_count + 1;
		exec_order_lasttime = CurrentTime;
	end;
end;
```

---


---

## 腳本檔案: 自動交易/3-Algo策略委託/02-時間權重交易(TWAP).xs

```xs
{@type:autotrade}
{
	時間權重(TWAP): 類似定時定量交易, 差異是傳入的是執行委託總時間以及委託總數量, 由腳本自己反推算委託間隔/每次委託數量.

	輸入參數:

	- 下單總時間 (order_duration: 在未來的幾(秒)內要執行完畢)
	- 下單總數量 (order_totalqty: 委託的總數量)
	- 買賣方向 (order_bs: 1=買進, -1=賣出)
	
	
	把預期委託數量平均分配在指定的時間範圍內, 例如指定在未來的60分鐘內買進100張
}

input: order_duration(3600, "委託區間(秒)");
input: order_totalqty(100, "總委託數量");
input: order_bs(1, "買賣方向", inputKind:=Dict(["買進", 1], ["賣出", -1]));

{ 
	範例:
	
	策略一啟動就啟動定時定量交易, 全部送完就停止
}

var: intrabarpersist exec_order_started(false);
var: intrabarpersist exec_order_starttime(0);
var: intrabarpersist exec_order_startposition(0);
var: intrabarpersist exec_order_endposition(0);

if not exec_order_started and GetInfo("TradeMode") = 1 then begin
	exec_order_started = true;		{ 啟動定時定量委託 }
	exec_order_starttime = CurrentTime;
	exec_order_startposition = Position;
	exec_order_endposition = Position + order_bs * order_totalqty;
end;

{ 時間權重的執行邏輯 }
if exec_order_started and Position <> exec_order_endposition then begin
	var: duration(0), target_position(0);
	
	duration = TimeDiff(CurrentTime, exec_order_starttime, "S");
	target_position = order_bs * Floor(order_totalqty * duration / order_duration) + exec_order_startposition;
	
	if Position <> target_position then begin
		SetPosition(target_position);		{ TODO: 請填入委託價格 }
	end;	
end;
```

---


---

## 腳本檔案: 自動交易/3-Algo策略委託/03-分量權重交易(VWAP).xs

```xs
{@type:autotrade}
{
	分量權重(VWAP): 把預期委託數量依照歷史成交量分布, 在指定的時間範圍送出內, 預期成交均價可以接近歷史均價
	
	輸入參數:

	- 統計天數 (vwap_days: 決定要用前幾天的成交量統計)
	- 開始交易時間 (start_hhmm: 交易開始時間, 格式為hhmm, 例如0905, 表示從09:05開始進行交易)
	- 結束交易時間 (end_hhmm: 交易結束時間, 格式為hhmm, 例如1300, 表示交易到1300就停止)
	- 交易數量 (order_totalqty: 預計交易的數量)
	- 交易方向 (order_bs: 1=買進, -1=賣出)
	
	執行邏輯:
	
	- 策略起動時根據vwap_days統計出每分鐘的成交數量分佈比例(從09:00~13:30),
	- 依照指定的交易區間(start_hhmm ~ end_hhmm), 以及預期交易數量, 決定每分鐘的委託數量,
	- 舉例
		- start_hhmm = 09:10, end_hhmm = 10:00
		- 依照歷史統計, 09:10的成交量=1%, 09:11的成交量=0.8%, .. 09:59的成交量=1.5%
		- 假設order_totalqty = 500, 則
		- 在09:11(09:10結束時), 送出500 * 1% / (1% + 0.8% + .. + 1.5%), 
		- 在09:12(09:11結束時), 送出500 * 0.8% / (1% + 0.8% + .. + 1.5%),
		- 在10:00(09:59結束時), 送出500 * 1.5% / (1% + 0.8% + .. + 1.5%),
		- 也就是說, 在指定時間範圍內, 依照歷史成交量的分佈, 每分鐘送出委託,
	
}

input: vwap_days(1, "用前N日的資料來計算成交量分佈");
input: start_hhmm(0905, "分鐘起點(HHMM)");
input: end_hhmm(1000, "分鐘終點(HHMM)");
input: order_totalqty(1000, "總委託數量");
input: order_bs(1, "買賣方向", inputKind:=Dict(["買進", 1], ["賣出", -1]));

if start_hhmm >= end_hhmm then raiseruntimeerror("開始時間必須 < 結束時間");

{ 請確認Backbar有足夠的空間可以讀入vwap_days的資料 }

var: intrabarpersist vwap_started(false);
var: intrabarpersist vwap_base_position(0);
var: intrabarpersist vwap_time_index(0);
array: intrabarpersist vwap_dist[](0);		// N日統計分佈, 總共有total_minute格, 每一格是到目前為止的百分比
var: intrabarpersist vwap_totalminutes(0);

var: intrabarpersist start_hhmmss(0), intrabarpersist end_hhmmss(0); 

var: start_condition(false);			{ 啟動定時定量委託 }

if not vwap_started and GetInfo("TradeMode") = 1 then begin

	// 如果使用者指定 09:01 ~ 10:00, 因為分K是標在時間起點, 
	// 所以我們要統計的是09:01 ~ 09:59這些分K的成交量分佈 (所以end_hhmm會-1分鐘)

	start_hhmmss = start_hhmm * 100;
	end_hhmmss = TimeAdd(end_hhmm * 100, "M", -1);

	CalcVWAPDistribution(vwap_days, start_hhmmss, end_hhmmss, vwap_dist);
	vwap_totalminutes = Array_GetMaxIndex(vwap_dist);
	vwap_started = true;
	vwap_base_position = Position;
	vwap_time_index = 0;
end;

{ VWAP的執行邏輯 }

if vwap_started and Position <> vwap_base_position + order_bs * order_totalqty then begin
	if CurrentTime >= start_hhmmss then begin
		{ 計算目前時間是開始時間後的第幾分鐘 }
		value1 = IntPortion(TimeDiff(CurrentTime, start_hhmmss, "M"));
		
		if value1 > vwap_time_index then begin
			{ 預期的成交量比例  = vwap_dist[value1] }
			if value1 >= vwap_totalminutes then 
				value2 = 100				{ 超過時間 => 100% }
			else	
				value2 = vwap_dist[value1];

			value3 = value2	* order_totalqty * order_bs / 100;
			
			if Position <> vwap_base_position + value3 then begin
				{ 送出委託單 }
				SetPosition(vwap_base_position + value3);	{ TODO: 請填入委託價格 }
			end;	
			vwap_time_index = value1;
		end;
	end;
end;
```

---


---

## 腳本檔案: 自動交易/3-Algo策略委託/04-網格交易.xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 自動交易/3-Algo策略委託/05-冰山委託單(Iceberg).xs

```xs
{@type:autotrade}
{
	冰山單(Iceberg): 把要買進的數量分批低掛

	輸入參數:
	
	- 最高價格 (ice_maxprice: 當市價超過這個價格時, 就暫停交易)
	- 委託價差 (ice_below: 目前市價=X時, 委託價格=X-ice_below(for buying), 也就是低買的價格位置, 目前是定義成絕對值)
	- 委託方向 (ice_bs: 1=買進, -1=賣出)
	- 委託總數量 (ice_totalqty: 預期總成交數量)
	- 每次委託數量 (ice_batchqty: 每一次委託單的大小)
	
	執行邏輯(for買進)
	
	- 當目前價格 = X時, 如果X <= ice_maxprice, 送出一筆委託單, 價格 = X - ice_below, 數量 = ice_batchqty,
	- 如果成交的話, 依照目前的價格送出下一筆委託單,
	- 如果目前的價格Y >= X + 2 * ice_below, and Y <= ice_maxprice, 則取消剩餘委託, 用目前的市場價格重新送出
	- Buy the dip => 低接

	Note: 以下程式碼假設商品一開始的部位 = 0
}

input: ice_maxprice(14000, "最高價格");
input: ice_below(10, "委託單價差");
input: ice_bs(1, "買賣方向", inputKind:=Dict(["買進", 1], ["賣出", -1]));
input: ice_totalqty(100, "總委託數量");
input: ice_batchqty(10, "每次委託數量");

var: intrabarpersist ice_lastorderprice(0);		// 最後一次委託價格
var: intrabarpersist ice_started(false);		// 已經啟動Iceberg交易

if not ice_started and GetInfo("TradeMode") = 1 then begin
	ice_started = true;
	ice_lastorderprice = 0;
end;

{ 冰山交易邏輯 }
if ice_started and Filled <> ice_bs * ice_totalqty then begin

	{ 如果目前市場價格超過最大值, 則不處理. 已經送出的委託就維持不動 }
	if (ice_bs = 1 and Close > ice_maxprice) or 
	   (ice_bs = -1 and Close < ice_maxprice) then 
	   return;

	if Position = 0 then begin
		{ 送出第一次委託 }
		ice_lastorderprice = Close - ice_bs * ice_below;
		SetPosition(ice_bs * ice_batchqty, ice_lastorderprice);
	end else if Position = Filled then begin
		{ 送出下一批次委託 }
		ice_lastorderprice = Close - ice_bs * ice_below;
		SetPosition(Position + ice_bs * ice_batchqty, ice_lastorderprice);
	end else if ice_bs = 1 and Close > ice_lastorderprice + 2 * ice_below then begin
		{ 價格移動, 追價 }
		ice_lastorderprice = Close - ice_bs * ice_below;
		SetPosition(Position, ice_lastorderprice);
	end else if ice_bs = -1 and Close < ice_lastorderprice - 2 * ice_below then begin
		{ 價格移動, 追價 }
		ice_lastorderprice = Close - ice_bs * ice_below;
		SetPosition(Position, ice_lastorderprice);
	end;

end;
```

---


---

## 腳本檔案: 自動交易/常見技術分析/多頭/ATR觸發上通道.xs

```xs
{@type:autotrade}
// 宣告參數
input:period(20,"計算TrueRange的區間"),N(2,"N倍通道");

// 資料讀取筆數設定
settotalbar(period + 3);

value1=average(truerange,period);
value2=average(close,period);
value3=value2+N*value1;
value4=value2-N*value1;

// 多方進場策略：向上突破上通道。出場策略：向下跌破下通道。
if close crosses over value3 then setposition(1);
if close crosses below value4 then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/多頭/DIF-MACD從負翻正.xs

```xs
{@type:autotrade}
// 宣告參數
input: FastLength(12, "DIF短期期數"), SlowLength(26, "DIF長期期數"), MACDLength(9, "MACD期數");
variable: difValue(0), macdValue(0), oscValue(0);

// 資料讀取筆數設定
SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 3 + 8);

MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);

// 多方進場策略：DIF-MACD由負轉正。出場策略：DIF-MACD由正轉負。
if oscValue Crosses Above 0	then setposition(1);
if oscValue Crosses below 0	then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/多頭/DIF黃金交叉MACD.xs

```xs
{@type:autotrade}
// 需告參數
input: FastLength(12, "DIF短期期數"), SlowLength(26, "DIF長期期數"), MACDLength(9, "MACD期數");
variable: difValue(0), macdValue(0), oscValue(0);

// 資料讀取筆數設定
SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 3 + 8);

MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);

// 多方進場策略：DIF黃金交叉MACD；出場策略：DIF死亡交叉MACD
if difValue Crosses Above macdValue then setposition(1);
if difValue Crosses below macdValue then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/多頭/KD低檔黃金交叉.xs

```xs
{@type:autotrade}
// 宣告參數
input: Length(9, "計算期數"), RSVt(3, "RSVt權數"), Kt(3, "Kt權數"), LowBound(25, "低檔區"), HighBound(75, "高檔區");
variable: _rsv(0), _k(0), _d(0);

// 資料讀取筆數設定
SetTotalBar(maxlist(Length,6) * 3 + 8);

Stochastic(Length, RSVt, Kt, _rsv, _k, _d);

// 多方進場策略：K在低檔區由下往上突破D值。出場策略：K由上往下穿越D值。
if _k < LowBound and _k crosses above _d then setposition(1);
if _k > HighBound and _k crosses under _d then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/多頭/MTM黃金交叉0.xs

```xs
{@type:autotrade}
// 宣告參數
Input: Length(10, "期數");

// 資料讀取筆數設定
settotalbar(maxlist(Length,6) + 8);

// 多方進場策略：MTM黃金交叉0軸；出場策略：MTM死亡交叉0軸
if Momentum(Close, Length) Crosses Above 0 then setposition(1); 
if Momentum(Close, Length) Crosses below 0 then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/多頭/RSI低檔價格背離.xs

```xs
{@type:autotrade}
// 宣告參數
Input: RSILength(10, "RSI期數"), _LThreshold(20, "低檔值"), _HThreshold(80, "高檔值");
variable: rsiValue(0),RSI_linearregslope(0),Close_linearregslope(0);

// 資料讀取筆數設定
settotalbar(maxlist(RSILength,6) * 8 + 8);

if RSILength < 5 then raiseruntimeerror("計算期別請超過五期");
RSIValue = RSI(Close, RSILength);
RSI_linearregslope = linearregslope(RSIValue, RSILength);
Close_linearregslope = linearregslope(Close, RSILength);

// 多方進場策略：RSI由下往上突破低檔區，且價格趨勢背離。出場策略：RSI由上往下穿越高檔區，且價格趨勢背離。
if RSIValue Crosses Above _LThreshold and RSI_linearregslope > 0 and Close_linearregslope < 0 then setposition(1);
if RSIValue Crosses Below _HThreshold and RSI_linearregslope < 0 and Close_linearregslope > 0 then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/多頭/均線黃金交叉.xs

```xs
{@type:autotrade}
// 宣告參數
input: Shortlength(5,"短期均線期數"), Longlength(20,"長期均線期數");

// 資料讀取筆數設定
settotalbar(8);
setbarback(maxlist(Shortlength,Longlength,6));

// 多方進場策略：短期均線「黃金」交叉長期均線。出場策略：長期均線「死亡」交叉短期均線。
if Average(Close,Shortlength) Cross Above Average(Close,Longlength) then setposition(1);
if Average(Close,Shortlength) Cross Below Average(Close,Longlength) then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/多頭/布林通道觸碰下軌.xs

```xs
{@type:autotrade}
// 宣告參數
Input: Length(20, "期數"), UpperBand(2, "通道上緣"), LowerBand(2, "通道下緣");
variable: mid(0), up(0), down(0);

// 資料讀取筆數設定
settotalbar(Length + 3);

up = bollingerband(Close, Length, UpperBand);
down = bollingerband(Close, Length, -1 * LowerBand);
mid = (up + down) / 2;

// 多方包寧傑通道進場策略：最低價觸碰下軌道。出場策略：最高價觸碰上軌道。
if low cross under down then setposition(1);
if high cross over up then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/多頭/帶量黃金交叉均線.xs

```xs
{@type:autotrade}
// 宣告參數
input: Length(10, "期數"), VolFactor(2, "成交量放大倍數");
var: avgP(0), avgVol(0);

// 設定資料讀取筆數
settotalbar(3);
setbarback(Length);

avgP = Average(close, Length);
avgVol = Average(volume, Length);

// 多方進場策略：帶量黃金交叉均線；出場策略：帶量死亡交叉均線。
if close cross above avgP and volume > avgVol * VolFactor then setposition(1);
if close cross below avgP and volume > avgVol * VolFactor then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/多頭/平滑CCI超賣.xs

```xs
{@type:autotrade}
// 宣告變數
Input: Length(14, "期數"), AvgLength(9, "平滑期數"), OverSold(-100, "超賣值");
Variable: cciValue(0), cciMAValue(0);

// 資料讀取筆數設定
SetTotalBar(maxlist(AvgLength + Length + 1,6) + 11);

cciValue = CommodityChannel(Length);
cciMAValue = Average(cciValue, AvgLength);

// 多方進場策略：平滑CCI死亡交叉超賣值。出場策略：平滑CCI黃金交叉超賣值。
if cciMAValue Crosses Below OverSold then setposition(1);
if cciMAValue Crosses above OverSold then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/多頭/短期RSI黃金交叉長期RSI.xs

```xs
{@type:autotrade}
// 宣告參數
input: ShortLength(6, "短期期數"), LongLength(12, "長期期數");
var:RSI_Short(0), RSI_Long(0);

// 設定資料讀取筆數
settotalbar(maxlist(ShortLength,LongLength,6) * 8 + 8);

RSI_Short=RSI(Close, ShortLength);
RSI_Long=RSI(Close, LongLength);

//多方進場策略：短期RSI黃金交叉長期RSI；出場策略：短期RSI死亡交叉長期RSI
if RSI_Short Crosses Above RSI_Long then setposition(1);
if RSI_Short Crosses below RSI_Long then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/多頭/股價黃金交叉三均線.xs

```xs
{@type:autotrade}
// 宣告參數
input: shortlength(5,"短期均線期數"), midlength(10,"中期均線期數"), Longlength(20,"長期均線期數");
variable: shortaverage(0), midaverage(0), Longaverage(0);

// 資料讀取筆數設定
settotalbar(3);
setbarback(maxlist(shortlength,midlength,Longlength));

shortaverage=Average(close,shortlength);
midaverage=Average(close,midlength) ;
Longaverage=Average(close,Longlength); 

// 多方進場策略：收盤價黃金交叉三均線。出場策略：收盤價死亡交叉三均線。
if close cross above maxlist(shortaverage, midaverage, longaverage) then setposition(1);
if close cross below minlist(shortaverage, midaverage, longaverage) then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/多頭/股價黃金交叉單均線.xs

```xs
{@type:autotrade}
// 宣告參數
input: length(5,"均線期數");
variable: avgValue(0);

// 資料讀取筆數設定
settotalbar(3);
setbarback(length);

avgValue = Average(close,length);

// 多方進場策略：收盤價黃金交叉均線。出場策略：收盤價死亡交叉均線。
if close cross above avgValue then setposition(1);
if close cross below avgValue then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/多頭/股價黃金交叉雙均線.xs

```xs
{@type:autotrade}
// 宣告參數
input: shortlength(5,"短期均線期數"), Longlength(20,"長期均線期數");
variable: Longaverage(0), shortaverage(0);

// 資料讀取筆數設定
settotalbar(3);
setbarback(maxlist(shortlength,Longlength));

Longaverage = Average(close,Longlength);
shortaverage= Average(close,shortlength);

// 多方進場策略：收盤價黃金交叉雙均線。出場策略：收盤價死亡交叉雙均線。
if close cross above maxlist(shortaverage, longaverage) then setposition(1);
if close cross below minlist(shortaverage, longaverage) then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/空頭/ATR觸發下通道.xs

```xs
{@type:autotrade}
// 宣告參數
input:period(20,"計算TrueRange的區間"),N(2,"N倍通道");

// 資料讀取筆數設定
settotalbar(period + 3);

value1=average(truerange,period);
value2=average(close,period);
value3=value2+N*value1;
value4=value2-N*value1;

// 空方進場策略：向下跌破下通道。出場策略：向上突破上通道。
if close crosses below value4 then setposition(-1);		
if close crosses over value3 then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/空頭/DIF-MACD從正翻負.xs

```xs
{@type:autotrade}
// 宣告參數
input: FastLength(12, "DIF短期期數"), SlowLength(26, "DIF長期期數"), MACDLength(9, "MACD期數");
variable: difValue(0), macdValue(0), oscValue(0);

// 資料讀取筆數設定
SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 3 + 8);

MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);

// 空方進場策略：DIF-MACD由正轉負。出場策略：DIF-MACD由負轉正。
if oscValue Crosses below 0	then setposition(-1);		
if oscValue Crosses Above 0	then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/空頭/DIF死亡交叉MACD.xs

```xs
{@type:autotrade}
// 需告參數
input: FastLength(12, "DIF短期期數"), SlowLength(26, "DIF長期期數"), MACDLength(9, "MACD期數");
variable: difValue(0), macdValue(0), oscValue(0);

// 資料讀取筆數設定
SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 3 + 8);

MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);

// 空方進場策略：DIF死亡交叉MACD；出場策略：DIF黃金交叉MACD
if difValue Crosses below macdValue then setposition(-1);
if difValue Crosses Above macdValue then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/空頭/KD低檔死亡交叉.xs

```xs
{@type:autotrade}
// 宣告參數
input: Length(9, "計算期數"), RSVt(3, "RSVt權數"), Kt(3, "Kt權數"), LowBound(25, "低檔區"), HighBound(75, "高檔區");
variable: _rsv(0), _k(0), _d(0);

// 資料讀取筆數設定
SetTotalBar(maxlist(Length,6) * 3 + 8);

Stochastic(Length, RSVt, Kt, _rsv, _k, _d);
		
// 空方進場策略：K在高檔區由上往下穿越D值。出場策略：K由下往上突破D值。
if _k > HighBound and _k crosses under _d then setposition(-1);
if _k < LowBound and _k crosses above _d then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/空頭/MTM死亡交叉0.xs

```xs
{@type:autotrade}
// 宣告參數
Input: Length(10, "期數");

// 資料讀取筆數設定
settotalbar(maxlist(Length,6) + 8);

// 空方進場策略：MTM死亡交叉0軸；出場策略：MTM黃金交叉0軸
if Momentum(Close, Length) Crosses below 0 then setposition(-1); 
if Momentum(Close, Length) Crosses Above 0 then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/空頭/RSI高檔價格背離.xs

```xs
{@type:autotrade}
// 宣告參數
Input: RSILength(10, "RSI期數"), _LThreshold(20, "低檔值"), _HThreshold(80, "高檔值");
variable: rsiValue(0),RSI_linearregslope(0),Close_linearregslope(0);

// 資料讀取筆數設定
settotalbar(maxlist(RSILength,6) * 8 + 8);

if RSILength < 5 then raiseruntimeerror("計算期別請超過五期");
RSIValue = RSI(Close, RSILength);
RSI_linearregslope = linearregslope(RSIValue, RSILength);
Close_linearregslope = linearregslope(Close, RSILength);

// 空方進場策略：RSI由上往下穿越高檔區，且價格趨勢背離。出場策略：RSI由下往上突破低檔區，且價格趨勢背離。
if RSIValue Crosses Below _HThreshold and RSI_linearregslope < 0 and Close_linearregslope > 0 then setposition(-1);
if RSIValue Crosses Above _LThreshold and RSI_linearregslope > 0 and Close_linearregslope < 0 then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/空頭/均線死亡交叉.xs

```xs
{@type:autotrade}
// 宣告參數
input: Shortlength(5,"短期均線期數"), Longlength(20,"長期均線期數");

// 資料讀取筆數設定
settotalbar(8);
setbarback(maxlist(Shortlength,Longlength,6));

// 空方進場策略：長期均線「死亡」交叉短期均線。出場策略：短期均線「黃金」交叉長期均線。
if Average(Close,Shortlength) Cross Below Average(Close,Longlength) then setposition(-1);
if Average(Close,Shortlength) Cross Above Average(Close,Longlength) then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/空頭/布林通道觸碰上軌.xs

```xs
{@type:autotrade}
// 宣告參數
Input: Length(20, "期數"), UpperBand(2, "通道上緣"), LowerBand(2, "通道下緣");
variable: mid(0), up(0), down(0);

// 資料讀取筆數設定
settotalbar(Length + 3);

up = bollingerband(Close, Length, UpperBand);
down = bollingerband(Close, Length, -1 * LowerBand);
mid = (up + down) / 2;

// 空方包寧傑通道進場策略：最高價觸碰上軌道。出場策略：最低價觸碰下軌道。
if high cross over up then setposition(-1);
if low cross under down then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/空頭/帶量死亡交叉均線.xs

```xs
{@type:autotrade}
// 宣告參數
input: Length(10, "期數"), VolFactor(2, "成交量放大倍數");
var: avgP(0), avgVol(0);

// 設定資料讀取筆數
settotalbar(3);
setbarback(Length);

avgP = Average(close, Length);
avgVol = Average(volume, Length);

// 空方進場策略：帶量死亡交叉均線；出場策略：帶量黃金交叉均線。
if close cross below avgP and volume > avgVol * VolFactor then setposition(-1);
if close cross above avgP and volume > avgVol * VolFactor then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/空頭/平滑CCI超買.xs

```xs
{@type:autotrade}
// 宣告變數
Input: Length(14, "期數"), AvgLength(9, "平滑期數"), OverSold(100, "超買值");
Variable: cciValue(0), cciMAValue(0);

// 資料讀取筆數設定
SetTotalBar(maxlist(AvgLength + Length + 1,6) + 11);

cciValue = CommodityChannel(Length);
cciMAValue = Average(cciValue, AvgLength);

// 空方進場策略：平滑CCI黃金交叉超賣值。出場策略：平滑CCI死亡交叉超賣值。
if cciMAValue Crosses above OverSold then setposition(-1);
if cciMAValue Crosses Below OverSold then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/空頭/短期RSI死亡交叉長期RSI.xs

```xs
{@type:autotrade}
// 宣告參數
input: ShortLength(6, "短期期數"), LongLength(12, "長期期數");
var:RSI_Short(0), RSI_Long(0);

// 設定資料讀取筆數
settotalbar(maxlist(ShortLength,LongLength,6) * 8 + 8);

RSI_Short=RSI(Close, ShortLength);
RSI_Long=RSI(Close, LongLength);

// 空方進場策略：短期RSI死亡交叉長期RSI；出場策略：短期RSI黃金交叉長期RSI
if RSI_Short Crosses below RSI_Long then setposition(-1);
if RSI_Short Crosses above RSI_Long then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/空頭/股價死亡交叉三均線.xs

```xs
{@type:autotrade}
// 宣告參數
input: shortlength(5,"短期均線期數"), midlength(10,"中期均線期數"), Longlength(20,"長期均線期數");
variable: shortaverage(0), midaverage(0), Longaverage(0);

// 資料讀取筆數設定
settotalbar(3);
setbarback(maxlist(shortlength,midlength,Longlength));

shortaverage=Average(close,shortlength);
midaverage=Average(close,midlength) ;
Longaverage=Average(close,Longlength); 

// 空方進場策略：收盤價死亡交叉三均線。出場策略：收盤價黃金交叉三均線。
if close cross below minlist(shortaverage, midaverage, longaverage) then setposition(-1);
if close cross above maxlist(shortaverage, midaverage, longaverage) then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/空頭/股價死亡交叉單均線.xs

```xs
{@type:autotrade}
// 宣告參數
input: length(5,"均線期數");
variable: avgValue(0);

// 資料讀取筆數設定
settotalbar(3);
setbarback(length);

avgValue = Average(close,length);

// 空方進場策略：收盤價死亡交叉均線。出場策略：收盤價黃金交叉均線。
if close cross below avgValue then setposition(-1);
if close cross above avgValue then setposition(0);
```

---


---

## 腳本檔案: 自動交易/常見技術分析/空頭/股價死亡交叉雙均線.xs

```xs
{@type:autotrade}
// 宣告參數
input: shortlength(5,"短期均線期數"), Longlength(20,"長期均線期數");
variable: Longaverage(0), shortaverage(0);

// 資料讀取筆數設定
settotalbar(3);
setbarback(maxlist(shortlength,Longlength));

Longaverage = Average(close,Longlength);
shortaverage= Average(close,shortlength);

// 空方進場策略：收盤價死亡交叉雙均線。出場策略：收盤價黃金交叉雙均線。
if close cross below minlist(shortaverage, longaverage) then setposition(-1);
if close cross above maxlist(shortaverage, longaverage) then setposition(0);
```

---
