---
title: XS完整手冊 - 關鍵字
category: 關鍵字
tags: [XS語法, 關鍵字, 流程控制, 常數, 忽略字, 宣告]
last_updated: 2026-01-08
total_functions: 3
---

# 關鍵字 (完整收錄)

> 本文件收錄了 [關鍵字] 下的所有子分類與函數說明，共 3 筆。
> 包含子分類：流程控制, 常數, 忽略字, 宣告

---


## 忽略字
--- 

### ignore
#### 忽略字

XS 語法內有一些特殊的忽略字，這些忽略字通常是英文常見的介系詞或連接詞，可以任意使用在語法內，以便增加程式碼的可讀性。
若我們在語法中使用這些忽略字，系統會在編譯時自動忽略它們，並不影響運算結果。

目前提供的忽略字列表如下：

|  |  |  |  |
| ---- | ---- | ---- | ---- |
| A | By | Of | The |
| An | Does | On | Was |
| At | From | Place |  |
| Based | Is | Than |  |


___


## 常數
--- 


## 流程控制
--- 

### flow
#### 流程控制

在腳本撰寫的過程當中，我們可能會使用到一些比較複雜的邏輯進行運算。簡單的條列陳述沒有辦法達到這個需求，這時候我們就會需要一些流程控制的語法來幫忙。

##### 條件判斷

條件判斷是最常使用的一種流程控制，會依執行的順序依序判斷，符合後即條出。XSscript提供以下三種條件判斷式：

###### IF THEN ELSE

IF / THEN / ELSE

使用 IF/THEN/ELSE 這三個語法來判斷某個條件成立時該執行那個動作，不成立時又該執行那個動作。

如果只需要判斷某個條件成立時該執行那個動作，則使用以下的語法:

```xs
If Close > Open Then Ret = 1;

```

在上述範例內如果Close值大於Open值的話則 Ret 變數的數值會被設定為1。

如果當條件成立時需要執行多個指令的話，則使用Begin / End的語法來包圍所需要執行的指令。

```xs
If Close > Open Then
Begin
    Value1 = Close - Open;
    Value2 = High - Low;
End;

```

如果條件成立時跟不成立時都需要執行不同的指令的話，則可以加入 ELSE 語法來定義條件不成立時該執行的動作。

```xs
If Close > Open Then
    Value1 = Close - Open
Else
    Value1 = Open - Close;

```

在上述範例內當Close的數值不大於Open的數值時，程式會執行Else內的語法。以這個例子為例，Value1的數值就是這根bar的實體高度。

同樣的，Else之後也可以使用Begin/End語法來定義多個指令，範例如下:

```xs
If Close > Open Then
Begin
    Value1 = Close - Open;
    Value2 = High - Low;
End
Else
Begin
    Value1 = Open - Close;
    Value2 = High - Low;
End;

```

Else後面也可以接if，用else if來進行多層次的條件判斷，從腳本上至下依序縮小判斷範圍，範例如下:

```xs
if value1 < 0 then
    value2 = 1
else if value1 < 10 then //等同於if  0 <= value1 and value1 < 10
    value2 = 2
else if value1 < 20 then //等同於if  0 <= value1 and value1 < 10
    value2 = 3
else  //等同於if  20<= value1
    value2 = 4;

```
 
###### Switch Case Default
Switch / Case / Default

Switch 語法是用來判斷某個變數的值是否符合某些運算式，同時定義符合時的執行指令。

語法如下：

```xs
Switch (變數)
Begin
  Case 運算式1:
     符合運算式1時所執行的指定;
  Case 運算式2:
     符合運算式2時所執行的指定;
  Default:
     都不符合時所執行的指令;
End;

```

在 Switch 語法內必須傳入一個變數，同時使用 Case 語法定義各種不同的運算式，以及當這個運算式符合時要執行的指令。同時也可以使用 Default 語法來定義當所有的Case都不符合時所需要執行的指令。

以下是一個範例:

```xs
Value1 =DayOfMonth(date);
Switch (value1)
Begin
  Case 1:   // value1=1時執行這段程式碼
        print(Text("今天的日期是",numtoStr(date,0),
        "。是",numtoStr(DayOfMonth(date),0),"日")
        ,"value1=1時執行這段程式碼");

  Case 2:   // value1=2時執行這段程式碼
        print(Text("今天的日期是",numtoStr(date,0),
        "。是",numtoStr(DayOfMonth(date),0),"日"),
        "value1=2時執行這段程式碼");
  Case 3:   // value1=3時執行這段程式碼
        print(Text("今天的日期是",numtoStr(date,0),
        "。是",numtoStr(DayOfMonth(date),0),"日"),
        "value1=3時執行這段程式碼");

  Case 4:   // value1=4時執行這段程式碼
        print(Text("今天的日期是",numtoStr(date,0),
        "。是",numtoStr(DayOfMonth(date),0),"日"),
        "value1=4時執行這段程式碼");

  Case 5:   // value1=5時執行這段程式碼
        print(Text("今天的日期是",numtoStr(date,0),
        "。是",numtoStr(DayOfMonth(date),0),"日"),
        "value1=5時執行這段程式碼");
  Case 6 to 20: // value1= 6 ~ 20 時執行這段程式碼
        print(Text("今天的日期是",numtoStr(date,0),
        "。是",numtoStr(DayOfMonth(date),0),"日"),
        "value1=6~20時執行這段程式碼");

  Default:  // 其他情形都執行這段程式碼
        print(Text("今天的日期是",numtoStr(date,0),
        "。是",numtoStr(DayOfMonth(date),0),"日"),
        "其他情形都執行這段程式碼");
End;

```

在上述範例內這個變數為 Value1，然後使用 Case 語法一一檢查 Value1 是否為1，2，3，4，5，6 20同時也使用 Default 語法定義當 Value1 不是1，2，3，4，5，6 20時所需要執行的指令。

由於DayOfMonth這個函數會計算出今天為幾日(如果是01日的話則回1，02日則回2，03日則回3)，所以以上的範例：
  * 在 01 日會印出「今天的日期是19941101。是1日 value1=1時執行這段程式碼」
  * 在 02 日會印出「今天的日期是19941102。是2日 value1=2時執行這段程式碼」
  * 在 03 日會印出「今天的日期是19941103。是3日 value1=3時執行這段程式碼」
  * 在 04 日會印出「今天的日期是19941104。是4日 value1=4時執行這段程式碼」
  * 在 05 日會印出「今天的日期是19941105。是5日 value1=5時執行這段程式碼」
  * 在 06 ~ 20 日會印出「今天的日期是19941107。是7日 value1=6~20時執行這段程式碼 」
  * 在 21 ~ 月底會印出「今天的日期是19941121。是21日 其他情形都執行這段程式碼 」
 


###### Once

Once

Once 語法用來定義某些 只需要執行一次的程式碼。

舉例而言：

```xs
Once(High = Highest(High, 5))
Begin
    HighDate = Date;
    HighPrice = High;
End;

```

Once 語法之後必須填入一個判斷式，以上例而言，這個判斷式是 High = Highest(High, 5)，在判斷式之後，可以填入當判斷式成立時要執行的指令，如果有多行指令的話則可以使用 Begin/End 來包圍。

所以上面這個範例執行的邏輯是，當創5日新高時，執行HighDate = Date，以及HighPrice = High這兩個指令，而且一旦出現創5日新高的情形之後，就不再執行HighDate = Date, 以及HighPrice = High這兩個指令。

如果要達到同樣的目的，也可以使用IF指令，搭配一個紀錄是否曾經執行過的變數：

```xs
Var: FirstTime(False);
If High = Highest(High, 5) And Not FirstTime Then
Begin
    HighDate = Date;
    HighPrice = High;
    FirstTime = True;
End;

```

在上述範例內，程式使用 FirstTime 這個變數來紀錄這個IF狀態是否曾經發生過，以確保只會執行一次。

可是由於系統會根據執行的設定方式在每一筆bar甚至每一筆tick更新時都會執行完整的程式碼，所以如果是使用If的寫法的話，每一次執行時還是會去判斷 High是否等於Highest(High, 5)！反之，如果是使用Once的寫法的話，一旦Once的運算式成立之後，未來不管執行任意bar，系統都會 自動跳過Once的判斷式以及程式碼。由於在這個例子內，IF內所需要執行的指令比較複雜且費時，所以就可以使用 Once 的語法來提升執行的速度。

##### 迴圈

另一種流程控制是迴圈，迴圈用在計算或比較需要重複執行的情況，例如計算過去10期的值，就可以利用迴圈來完成。XSscript提供以下三種條件判斷式：

###### For To (DownTo)

For To / DownTo

For 語法是用來定義一段迴圈的執行邏輯。

For 迴圈語法內必須使用一個變數，指定這個變數的 初始值 跟 結束值，同時指定這個迴圈內要執行的指令:

```xs
For 變數 = 初始值 to 結束值
  執行的指令;

```

如果要執行的指定超過一行的話則使用 Begin/End 語法來包裝需要執行的指定

```xs
For 變數 = 初始值 to 結束值
Begin
  執行的指令1;
  執行的指令2;
End;

```

迴圈內的指令總共會被執行**(結束值 - 初始值 + 1)次，在期間每次執行時，變數的值會從 初始值 一一遞增到 結束值**為止。

以下是一個實例:

```xs
SumValue = 0;
For i = 0 to 4
Begin
    SumValue = SumValue + Close[i];
End;
AvgValue = SumValue / 5;

```

上述的範例是一個累加的用法，透過For迴圈總共執行了5次(4 - 0 + 1)，第一次執行時i = 0(初始值), 第二次執行時i = 1(遞增), 最後一次執行時i = 4(結束值)。所以執行完For迴圈後SumValue的數值是最近５期Close欄位的累加值，把SumValue的值除以5之後就可以得到Close值的平均數值。

如果迴圈的控制方式希望是從 初始值 一直減少直到 結束值 為止的話，則可以使用 DownTo 指令。

```xs
SumValue = 0;
For i = 4 downto 0
Begin
    SumValue = SumValue + Close[i];
End;
AvgValue = SumValue / 5;

```

上述範例執行的結果與先前相同，唯一的差異是 DownTo 語法，所以迴圈執行的方式是第一次i = 4, 第二次 i = 3(遞減), 第三次 i = 2, 第四次 i = 1, 最後一次 i = 0。
一般而言迴圈的執行次數是透過初始值跟結束值來控制的，可是如果需要在執行過程內 提前跳出 的話，則可以使用Break指令。

系統內還提供不同的迴圈控制方式，請參考Repeat/Until以及 While。
 

###### While

While

While 語法是用來定義一段迴圈的執行邏輯。語法如下：

```xs
While 判斷式
  執行的指令;

```

當判斷式成立時，While迴圈會重複的執行，一直到判斷式回傳False為止。

如果在迴圈內需要執行多個指令的話，則可以使用 Begin/End 的方式來包圍。

```xs
While 判斷式
Begin
  執行的指令1;
  執行的指令2;
End;

```

以下是一個範例:

```xs
SumValue = 0;
While i < 5
  Begin
    SumValue = SumValue + Close[i];
    i = i + 1;
  End;
AvgValue = SumValue / 5;

```

上述範例內While的迴圈會一直執行，直到 i 的數值 >= 5時才會停止。每次執行時SumValue會累加前幾期的Close數值，同時變數i 會每次加1。以這個範例而言，SumValue的數值會變成是最近５期收盤價的加總，最後算出AvgValue為最近５期的平均收盤價。
系統內還提供不同的迴圈控制方式，請參考Repeat/Until以及 For。
 

###### Repeat Until

Repeat / Until

Repeat/Until 的語法是用來定義一段迴圈的執行邏輯。，語法如下:

```xs
Repeat
  執行的指令;
Until 判斷式;

```

程式會不斷的執行Repeat之後的指令，一直到Until後續的判斷式變成True值時才會離開迴圈。

如果迴圈內需要執行的指令超過一個的話，則可以使用 Begin/End 來包圍:

```xs
Repeat
  Begin
    執行的指令1;
    執行的指令2;
  End;
Until 判斷式;

```

以下是一個範例:

```xs
SumValue = 0;
Repeat
  Begin
    SumValue = SumValue + Close[i];
    i = i + 1;
  End;
Until i = 4;
AvgValue = SumValue / 5;

```

上述範例內Repeat的迴圈會一直執行，每次執行時SumValue會累加前幾期的Close數值，同時變數 i 會每次加1。這個迴圈會一直跑到 i = 4 的時候才會離開。以這個範例而言，SumValue的數值會變成是最近５期收盤價的加總，最後算出AvgValue為最近５期的平均收盤價。

系統內還提供不同的迴圈控制方式，請參考While以及 For。
 


##### 中斷

在執行的過程中，為了提升效率，可以控制電腦跳過某些計算不執行。就可以用中斷語法來達成。

###### Break : 跳出迴圈

Break

Break 指令的用處是控制迴圈執行時跳出迴圈的時機點，一般是用在For 迴圈或是While 迴圈內。

以下是 For 迴圈的範例:

```xs
i = 0;
For i = 0 to 10
Begin
    If Close[i] < 20 Then Break;
End;

```

一般而言上面的迴圈會執行11次(從I = 0 到 10)。可是在執行過程內，如果某一期的Close欄位值比20小的話，就會馬上跳出 For 迴圈。


###### Return: 跳出腳本

Return

Return 指令用來中斷正在執行的腳本。當程式遇到這個指令時，執行將會中斷。

```xs
If CurrentTime < 123000 Then Return;

If Close > Close[1] and Close = High Then Ret = 1;

```

上述範例利用CurrentTime來判斷執行時間，如果是在12:30之前的話則不做任何動作(腳本直接中斷，等待下一根bar)。在12:30過後如果收盤價創當日新高的話則觸發。
 

###### Ret ( `RetVal` )

Ret

Ret是一個系統的內建變數，他的數值會決定警示腳本以及選股腳本執行結果。

當警示腳本以及選股腳本在每根bar重新執行時 Ret的數值會被設定為0，當這根bar結束完成時如果Ret的數值不是0的話，則會產生觸發訊號(警示腳本)，或是選取這檔商品(選股腳本)。

以下是一個範例，在收盤價大於五日平均值時把Ret的數值設為1，用來觸發警示或是選取這個商品。

```xs
If Close > Average(Close, 5) Then Ret = 1;
```

##### 多行語法

###### Begin End

Begin / End

Begin / End 語法用在 If, While, For 等控制指令內。當需要輸入超過一行的程式碼時，就必須使用 Begin/End 來把程式碼 包圍 起來。

```xs
If Close >= Close[1] Then ret = 1;  // 計算漲跌

```

上述範例內當Close >= Close[1]時因為只需要執行一行指令，所以可以把指令直接寫出來。

可是在以下的範例內，由於當Close >= Close[1]時我們希望要執行兩個指令，所以透過 Begin/End 把這兩個指令包圍起來。

```xs
If Close >= Close[1] Then
Begin
   Value1 = Close - Close[1];  // 計算漲跌
   Value2 = Value1 / Close[1]; // 計算漲跌幅
End;

```



XSscript的執行是一行為單位 ( 用分號";"結尾 ) 。所以在流程控制中，通常都會搭配Begin...End使用。Begin...End可以讓我們用多行的陳述式進行運算，而非原先僅能使用單行陳述式。

##### 數列關係

###### Cross Over ( `Cross Above` ) ：判斷是否黃金交叉
###### Cross Under ( `Cross Below` ) ：判斷是否死亡交叉

Cross Above - Cross Below.md

Cross Above / Cross Below

Cross 相關的語法共有兩種：

  * Cross Above 或是 Cross Over 是用來檢查目前的欄位數值是否 向上穿越 某個欄位的前期數值。
  * Cross Below 或是 Cross Under 則是用來檢查目前的欄位數值是否 向下跌破 某個欄位的前期數值。

以下是 向上穿越 均線的寫法：

```xs
If Close Cross Above Average(Close, 5) Then ret = 1;

```

當這一期的Close欄位大於等於近5期的平均值(Average(Close,5))且前一期的Close欄位小於前一期的近5期的平均值的話，則ret會被設定成1。

以下則是 向下跌破均線 的寫法：

```xs
If Close Cross Below Average(Close, 5) Then ret = 1;

```

如果這一期的Close欄位小於等於近5期的平均值(Average(Close,5))且前一期的Close欄位大於前一期的近5期的平均值的話，則ret會被設定成1。

Cross 也可以寫成 Crosses。




##### 邏輯判斷

###### Not ：取得相反值

NOT

說明
NOT語法回傳運算式的相反值。

請看以下的範例程式：

```xs
If Close > Close[1] Then Ret = 1;
```
這個例子會在Close值大於Close的前期值時設定Ret為1。

如果使用者希望的是在Close值**不是**大於Close的前期值時才設定Ret為1的話，則可以寫成：

```xs
If Not (Close > Close[1]) Then Ret = 1;
```

上述的範例會在Close值**不是**大於Close的前期值時設定Ret為1。

###### And ：判斷條件是否同時成立

AND

AND 語法用來檢查運算式是否 同時成立。

```xs
If Close >= Close[1] And Volume >= Volume[1] Then ret = 1;

```

在上述範例內如果close欄位 >= 前期值 而且同時 volume欄位 >= 前期值的話，則ret會被設定成1。

請參考OR語法。



###### Or ：判斷是否有任一條件成立

OR

OR 語法用來檢查運算式 是否有任一個成立。

```xs
If Close >= Close[1] Or Close >= Close[2] Then ret = 1;

```

在上述範例內如果Close欄位 >= 前期值 或是 Close欄位 >= 前兩期值的話，則ret會被設定成1。

請參考AND語法。
 

###### XOR ：計算差集

XOR

XOR運算式是用來計算兩個邏輯數值的 差集。

運算方式如下：

  * True XOR True 傳回False
  * True XOR False 傳回True
  * False XOR True 傳回True
  * False XOR False 傳回False

___


## 宣告
--- 

### declare
#### 宣告

宣告是在腳本中引入變數使用，變數是用來存放計算後的數值，方便重複使用或增加腳本的可讀性。

變數需要先經過宣告的程序後才能使用，並且在宣告的同時也需要指定變數的類型、名稱或初始值等變數的屬性。

在XSscript中，一共有下列宣告變數的語法：

##### 宣告變數
###### Var ( `Variable` ‧ `Variables` ‧ `Vars` )


Var 語法用來宣告變數，並且給定變數的預設值。

系統會根據 Var 語法內給定的預設值的型態來決定變數的類型。目前系統提供以下三種變數類型:

  * 數值，例如 10, 5.3,
  * 字串, 例如 "String"，
  * 邏輯值, 例如 True, False

語法如下:

```xs
Var: SumValue(0);
Var: StrValue("");
Var: Flag(True);
```

在上述的範例內宣告了三個變數:

  * SumValue 是一個數值變數，初始值為0，
  * StrValue 是一個字串變數，初始值為"" (空白字串)，
  * Flag 是一個邏輯變數，初始值為True

多個變數也可以在同一行內宣告，例如可以把上述範例寫成:

```xs
Var: SumValue(0), StrValue(""), Flag(True);
```

除了 Var 語法之外，也可以使用 Vars 語法，Variable 語法，或是 Variables 語法來宣告變數，範例如下：
```xs
Vars: SumValue(0);
Variable: StrValue("");
Variables: Flag(True);
```

###### IntrabarPersist

IntrabarPersist 語法用來控制變數數值在執行時的變化邏輯。

在程式執行時，變數的數值會自動延續前一筆bar最後的計算值。

以下是一個簡單的示意圖，說明變數的數值在執行時的變化情形。

Image

注意到在上圖內變數的數值都會從上一筆執行後的結果延續到下一筆bar。

如果上述的腳本被設定成逐筆洗價的話(也就是說同一筆bar可能執行很多次)，則變數的數值變化情形如下:

Image

請注意，雖然第二筆bar因為價位變化的關係被執行了兩次，可是每次執行時，Counter變數的數值還是都會先變成上一筆bar最後執行的結果(1)之後才開始執行第二筆bar。(圖示內紅色標記處)。所以雖然第二筆bar執行了兩次，Counter在離開第二筆bar的時时候的數值還是為2。
這個行為是為了要保證逐筆洗價時最後算出來的數值只跟這一筆bar的價位有關，而不是跟這一筆bar被執行了多少次有關。

可是在某些情境底下可能需要保留最後一次計算後的數值(不管是否有換bar)，此時就可以使用 IntrabarPersist 的語法:

```xs
input: atVolume(100); setinputname(1,"大單門檻");
```

```xs
variable: intrabarpersist Xtime(0);         //計數器
```

```xs
Volumestamp = q_DailyVolume;
```

```xs
if Date > date[1] then Xtime = 0; // 開盤那根要歸0次數
```

```xs
if q_tickvolume > 100 then Xtime += 1; // 量夠大就加1次
```

```xs
if Xtime > 10  then
begin
	ret = 1;
	Xtime = 0;
end;
```
上述範例是一個警示腳本，使用日線頻率，逐筆洗價模式來執行。我們希望當大單(目前定義成單筆成交量 > 100張)的個數超過10之後就觸發。由於是日線模式，所以每次重新執行時 XTime都會變成0，無法實際統計發生大單的次數。

解決方式則是把XTime設為IntrabarPersist．一旦這樣設定之後，XTime的數值就不會因為重新執行這根bar而被還原，也因此可以正確的統計到在當日出現大單的個數。

##### 宣告陣列
###### Array ( `Arrays` )

Array 語法用來宣告一個陣列變數，同時設定陣列的大小以及陣列內儲存數值的資料型態(也可以寫成 Arrays)。

所謂陣列就是一個可以儲存 多個數值 的變數，陣列內儲存數值的個數，以及數值的資料型態可以透過Array語法來定義。

系統提供兩種控制陣列數值個數的方式。第一種方式是固定個數，語法如下:

```xs
Array: NumArray[10](0);
Array: StrArray[10]("");
Array: BoolArray[10](True);


在以上的範例設定了三個陣列變數：

  * NumArray，這是一個數值陣列，總共有10個數值，每個數值的初始值都是0，
  * StrArray，這是一個字串陣列，總共有10個數值，每個數值的初始值都是""，
  * BoolArray，這是一個布林值陣列，總共有10個數值，每個數值的初始值都是True

以下是NumArray在宣告後的示意圖。

Image: 示意圖

如果要存取NumArray的話，則使用以下的語法：
```xs
NumArray[1] = 5;
Value1 = NumArray[1];
```

在中括弧[]內傳入的數值稱之為 索引值，索引值的範圍由1開始，一直到陣列宣告的最大個數。

如果陣列的大小無法預先知道的話，則可以使用第二種語法來宣告陣列：

```xs
Array: NumArray[](0);
Array: StrArray[]("");
Array: BoolArray[](True);
```

請注意在上述語法內並未指定陣列的個數 ([] 內並沒有任何數值)。此時陣列已經被宣告，也已經定義這個陣列內可以存放的資料的格式，可以此時陣列還不可以被使用。

等到程式知道陣列的實際所需大小時，程式必須透過 Array_SetMaxIndex 函數來設定陣列的大小。

```xs
Var: Count(0);
Array: NumArray[](0);
```

```xs
If High > Highest(High,20)[1] Then Count = Count + 1;
Array_SetMaxIndex(NumArray, Count);
NumArray[Count] = High;
```

在上述範例內每當創近20期新高時 (High > Highest(High,20)[1])，NumArray就會多存放當時的新高價。由於無法預先知道所需要儲存的個數，所以使用上述語法來動態設定陣列的大小。

以上所定義的陣列變數都是屬於一維陣列，也就是說一個陣列變數內有多個數值，使用時像序列般的方式來存取。如果需要陣列內的數值可以以類似矩陣的方式來存取的話，則可以以下列語法來宣告二維陣列。

```xs
Array: NumArray[10,2](0);
```

在上例內，中括弧[]內有兩個數值，分別是10跟2。透過這樣子的語法我們宣告了一個二維陣列，他的內容如下:

Image: 示意圖

我們可以想像一個二維陣列就好像是一個Excel的表格一樣。中括弧內的第一個數值宣告這個表格的行數，第二個數字則是宣告表格的欄數。

當需要存取二維陣列時、我們使用以下的語法:
```xs
NumArray[5,1] = 10;
Value1 = NumArray[1,2];
```

存取時需要傳入兩個索引值，索引值的範圍是從１開始，不能超過陣列的行數跟欄數。

※ Array 維度最多 9 個。元素數量最多 7000。例如：Array:LimitArray[a,b,c,d,e,f,g,h,i]; 則 (a+1) * (b+1) * (c+1) * (d+1) * (e+1) * (f+1) * (g+1) * (h+1) * (i+1) 所得到的元素值最多為 7000 個。

##### 宣告輸入
###### Input ( `Inputs` )

Input 語法用來宣告腳本參數的名稱以及資料類型(也可以寫成 Inputs)。

Input 的語法依照腳本類型而有差異。

如果是指標腳本，警示腳本，或是選股腳本的話，則使用以下語法。以下是一個指標的範例：

```xs
Input: Length(10);
```

```xs
Plot1(Average(Close, Length));
```

在上述的指標範例內宣告了一個名為 Length 的參數，用來存放計算收盤價平均值的天期。這個參數的預設值為10，資料類型為數字。

一旦宣告之後，程式內則可以像變數 Var 一樣的使用這個參數。可是跟變數不同的是，使用者在使用這個腳本時，可以透過參數設定的畫面來動態控制這個參數的數值。以下是設定指標時的參數設定畫面:

Image: Input設定

由於使用者可以在引用腳本時動態控制參數的數值，腳本的應用上會更有彈性。

在上面的參數設定畫面內看到參數名稱顯示為 Length，也就是Input語法內設定的變數名稱。如果希望畫面上看到的參數名稱是中文的話，則可以在Input語法內傳入參數名稱:
以下是修改後的範例:

```xs
Input: Length(10, "天期");
```

```xs
Plot1(Average(Close, Length));
```

底下是設定參數畫面:

Image: Input設定2

注意到畫面上出現的參數名稱已經變成 "天期"了。這樣子的作法可以讓腳本的使用上更為清楚。

Input語法如果應用在函數腳本內的話，則必須使用不同的語法:

```xs
Input: Price(NumericSeries);
Input: Length(NumericSimple);
```

```xs
Value1 = Summation(Price, Length) / Length;
```

在上述範例內宣告了兩個參數，第一個參數叫做 Price，他的資料格式是一個數字序列，第二個參數叫做 Length，他的資料格式是一個數字(不是序列)。

```xs
Input: Price(NumericSeries,"價格");
Input: Length(NumericSimple,"天期");
```
在上述範例內宣告了兩個參數，第一個參數叫做 Price，他的資料格式是一個數字序列，且參數名稱為 價格；第二個參數叫做 Length，他的資料格式是一個數字(不是序列)，且參數名稱為 天期。

```xs
Input: Price(close,NumericSeries,"價格");
Input: Length(10,NumericSimple,"天期");
```

在上述範例內宣告了兩個參數，第一個參數叫做 Price，預設值為 Close，他的資料格式是一個數字序列，參數名稱為 價格；第二個參數叫做 Length，預設值為 10，他的資料格式是一個數字(不是序列)，參數名稱為 天期。

關於函數所支援的各種不同的參數類型，請參考以下章節:
  * Numeric
  * NumericSimple
  * NumericSeries
  * NumericRef
  * NumericArray
  * NumericArrayRef
  * String
  * StringSimple
  * StringSeries
  * StringRef
  * StringArray
  * StringArrayRef
  * TrueFalse
  * TrueFalseSimple
  * TrueFalseSeries
  * TrueFalseRef
  * TrueFalseArray
  * TrueFalseArrayRef
 
###### inputkind ( `inputkind` )

input宣告的時候，可以使用 inputkind 這個命名參數(named parameter)，用來控制系統參數設定的介面(UI)。再搭配 Dict 、 DateRange 或 SymbolPrice 函數來產生對應的內容。

Dict 產生選項的範例如下：

```xs
input: IndexPomUnit(1, "大盤融資單位", inputkind:=Dict(["金額",1],["張數",2]));
```

在上述的範例內宣告了一個名為 IndexPomUnit 的參數，用來存放計算大盤融資的數值，不過此數值的單位有 金額 與 張數 兩種，故可以使用 inputkind 搭配 Dict 函數，就能在介面設定單位為金額或者張數，此範例預設單位為金額。

Image: inputkind_dict

也可以改寫成以下範例，使用字串型態的方式來撰寫相關程式碼：
```xs
input: IndexPomUnit("Amount", "大盤融資單位", inputkind:=Dict(["金額","Amount"],["張數","Sheets"]));
```

DateRange 產生日期範圍選項的範例如下：

```xs
input:FdifferenceDate(20180301,"外資買賣超查詢日期",inputkind:=daterange(20160301,20190301,"D"));
//daterange(最小查詢日期,最大查詢日期,"支援日/週/月/季/半年/年頻率")
```

在上述的範例內宣告了一個名為 FdifferenceDate 的參數，用來存放外資買賣超查詢日期的數值，就能方便在介面上勾選日曆選項使用，此範例預設查詢日期為2018年03月01日。

Image: inputkind_date range

SymbolPrice 產生 Open、High、Low、Close 四個選項的範例如下：
```xs
input:OHLC_Opti(200,"價格：",inputkind:=SymbolPrice());
```

在上述的範例中，宣告了一個名為 OHLC_Opti 的參數，用來存放價格的數值，就能方便在介面上勾選 Open、High、Low、Close 四個選項使用。

Image: inputkind_symbolprice


##### 宣告數值輸入 ( 函數 )
###### Numeric
###### NumericSimple
###### NumericSeries

(僅適用於函數腳本內)

Numeric 語法是用來定義函數腳本的參數為數值型態。

```xs
Input: Price(Numeric);
Input: Length(Numeric);
```

```xs
Value1 = Summation(Price, Length) / Length;
```

假設上例是一個名稱為 MyFunction 的函數, 在此 Price 參數跟 Length 參數都被定義成 Numeric, 表示使用這個函數的腳本必須傳遞數值型態的參數，否則腳本編譯時會產生錯誤。

以下是使用這個函數的腳本的範例:

```xs
Value1 = MyFunction(Close, 5);
```

在上例內呼叫MyFunction時傳入了 Close(收盤價序列)，以及數值5。

Numeric 型態還有以下兩個變形:

  * NumericSeries: 表示傳入的數值為一個序列，例如傳入 Close(收盤價序列),
  * NumericSimple: 表示傳入的數值為一個單一數值，例如 5
這兩種變形的用意是要幫忙系統可以更精確的處理腳本跟函數之間的運作關係。所以上述MyFunction可以被改寫成:

```xs
Input: Price(NumericSeries);
Input: Length(NumericSimple);
```

```xs
Value1 = Summation(Price, Length) / Length;
```

在這個函數內，由於 Price 是被當成序列來使用(計算加總時會用到前期值)，所以可以宣告成 NumericSeries。而 Length 因為只會用到當下的數值，所以可以宣告成 NumericSimple。

目前XS系統內，只要是數值參數，腳本內可以混用 Numeric, NumericSimple, 以及 NumericSeries 這三種宣告方式，不影響腳本執行的結果。

###### NumericRef

(僅適用於函數腳本內)

NumericRef 語法用來定義函數腳本的參數為數值型態，並且可以從函數內修改呼叫者傳入的數值。

當一個函數變數被宣告成 Numeric 時，在函數內對這個數值的修改並不會影響呼叫者端傳入的變數，這個行為稱之為 Call By Value。

如果有需要從函數內可以更改呼叫者端的變數的話，則可以使用 NumericRef 的語法，此時的行為會變成Call By Reference。
```xs
// MACD function
//  Input: Price序列, FastLength, SlowLength, MACDLength
//  Output: DifValue, MACDValue, OscValue
//
Input: Price(numericseries);
Input: FastLength(numericsimple);
Input: SlowLength(numericsimple);
Input: MACDLength(numericsimple);
```

```xs
Input: DifValue(numericref);
Input: MACDValue(numericref);
Input: OscValue(numericref);
DifValue = XAverage(price, FastLength) - XAverage(price, SlowLength);
MACDValue = XAverage(DifValue, MACDLength) ;
OscValue = DifValue - MACDValue;
```

在上述MACD函數內，呼叫者端傳入了價格序列(Price), 短天期(FastLength), 長天期(SlowLength)，以及MACD的天期(MACDLength)，函數內要算出 DIF 的數值, MACD 的數值, 以及 OSC 的數值。由於總共有三個數值需要回傳，所以利用 NumericRef 的方式來完成。

呼叫者端的程式碼範例如下：

```xs
input: FastLength(12), SlowLength(26), MACDLength(9);
variable: difValue(0), macdValue(0), oscValue(0);
MACD(Close, FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);
```

```xs
Ret = difValue Crosses Above macdValue;
```

注意到當呼叫完 MACD 函數後, difValue, macdValue, 以及 oscValue 的數值都會從MACD函數內回傳。

###### NumericArray

(僅適用於函數腳本內)

NumericArray 語法用來定義函數腳本的參數為數值陣列型態。

```xs
Input: MyNumericArray[X](NumericArray);
```

```xs
For Value1 = 1 to X
  Value2 = Value2 + MyNumericArray[Value1];
```

NumericArray 與Numeric最大的差異是在Input語法內陣列變數名稱之後還需要定義*[陣列大小變數]。在上例內[X]*就宣告了一個變數 X，他的數值會是傳入的陣列的大小(陣列內有多少數值)。

透過這個機制，函數內就可以知道傳入的陣列的大小，然後利用這個資訊來正確的判斷可以讀取哪些數值。 上述範例內使用一個 For迴圈來加總傳入陣列的每個數值，迴圈的範圍是從1開始，直到 X 結束。

如果需要傳入的陣列是二維的，則語法如下:

```xs
Input: MyNumericArray[X,Y](NumericArray);
```

在上例內中括弧內必須填入兩個變數(X, Y)，這兩個變數的數值將會分別是傳入的陣列的行數跟欄數。

###### NumericArrayRef

(僅適用於函數腳本內)

NumericArrayRef 語法用來定義函數腳本的參數為數值陣列型態，並且可以從函數內修改呼叫者傳入的數值陣列。

```xs
Input: MyNumericArray[X](NumericArrayRef);
```

NumericArrayRef 可以視為NumericArray以及NumericRef的綜合體。請參考以上兩種語法的說明。
 

##### 宣告字串輸入 ( 函數 )
###### String
###### StringSimple
###### StringSeries

(僅適用於函數腳本內)

String 語法用來定義函數腳本的參數為字串型態。

```xs
Input: MyString(String);
```

String 型態也有兩種變形:

  * StringSeries: 代表傳入的是一個字串序列，
  * StringSimple: 代表傳入的是一個字串的單一值

相關的語法請參考Numeric

###### StringRef

(僅適用於函數腳本內)

StringRef 語法用來定義函數腳本的參數為字串型態，並可以從函數內修改呼叫者傳入的數值。

```xs
Input: MyString(StringRef);
```

關於從函數內回傳數值的行為，請參考 NumericRef

###### StringArray

(僅適用於函數腳本內)

StringArray 語法用來定義函數腳本的參數為字串陣列型態。

```xs
Input: MyStringArray[X](StringArray);
```

相關的語法請參考NumericArray

###### StringArrayRef

(僅適用於函數腳本內)

StringArrayRef 語法用來定義函數腳本的參數為字串陣列型態，並且可以從函數內修改呼叫者傳入的字串陣列。

```xs
Input: MyStringArray[X](StringArrayRef);
```

StringArrayRef 可以視為StringArray以及StringRef的綜合體。請參考以上兩種語法的說明。


##### 宣告布林輸入 ( 函數 )
###### TrueFalse
###### TrueFalseSimple
###### TrueFalseSeries

(僅適用於函數腳本內)

TrueFalse 語法用來定義函數腳本的參數為邏輯值型態(TRUE 或是 FALSE)。

```xs
Input: MyFlag(TrueFalse);
```

TrueFalse 型態也有兩種變形:

  * TrueFalseSeries: 代表傳入的是一個邏輯值序列，
  * TrueFalseSimple: 代表傳入的是一個邏輯值的單一值

相關的語法請參考Numeric

###### TrueFalseRef

(僅適用於函數腳本內)

TrueFalseRef 語法用來定義函數腳本的參數為邏輯值型態，並可以從函數內修改呼叫者傳入的數值。

```xs
Input: MyFlag(TrueFalseRef);
```

關於從函數內回傳數值的行為，請參考 NumericRef

###### TrueFalseArray

(僅適用於函數腳本內)

TrueFalseArray 語法用來定義函數腳本的參數為邏輯值陣列型態。

```xs
Input: MyFlagArray[X](TrueFalseArray);
```

相關的語法請參考NumericArray

###### TrueFalseArrayRef

(僅適用於函數腳本內)

TrueFalseArrayRef 語法用來定義函數腳本的參數為邏輯值陣列型態，並且可以從函數內修改呼叫者傳入的邏輯值陣列。

```xs
Input: MyFlagArray[X](TrueFalseArrayRef);
```

TrueFalseArrayRef 可以視為TrueFalseArray以及TrueFalseRef的綜合體。請參考以上兩種語法的說明。

___
