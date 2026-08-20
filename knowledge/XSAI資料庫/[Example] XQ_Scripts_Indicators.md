# XQ 官方指標腳本範例庫

共 395 個指標腳本範例。

---

## 腳本檔案: 指標/XQ技術指標/3-6 乖離率.xs

```xs
{@type:indicator}
// XQ 3-6 乖離率
//
input: Length1(3), Length2(6);

SetInputName(1, "天數一");
SetInputName(2, "天數二");

Plot1(Bias(Length1) - Bias(Length2), "3-6乖離率(%)");
```

---


---

## 腳本檔案: 指標/XQ技術指標/3-6乖離率轉折點.xs

```xs
{@type:indicator}
// XQ: 3-6乖離率轉折點
//
Value1 = 2 * Close[3] - Close[6];
Plot1(Value1, "T");
```

---


---

## 腳本檔案: 指標/XQ技術指標/ACC (加速量指標).xs

```xs
{@type:indicator}
// XQ: ACC指標
//
input: Length(10);

SetInputName(1, "天數");

value1 = Momentum(Close, Length); 
value2 = Momentum(value1, Length);

Plot1(value2, "ACC");
```

---


---

## 腳本檔案: 指標/XQ技術指標/AD-Osc(聚散擺盪指標).xs

```xs
{@type:indicator}
// XQ: A/D Osc 指標
// 
variable: bp(0), sp(0), ado(0);

bp = High - Open;
sp = Close - Low;
if High <> low then
	ado = (bp + sp)/(2*(High - Low))*100
else
	ado = 50;

plot1(ado, "A/D-Osc");
```

---


---

## 腳本檔案: 指標/XQ技術指標/ADI (累積分配指標).xs

```xs
{@type:indicator}
// XQ: A/DI 指標
//
variable: adi(0);

if Close > Close[1] then
	adi = adi[1] + (Close - minlist(low, close[1])) 
else
  begin
	if Close < Close[1] then
		adi = adi[1] - (maxlist(high, close[1]) - close)
	else
		adi = adi[1];
  end;

Plot1(adi, "A/DI");
```

---


---

## 腳本檔案: 指標/XQ技術指標/AR 指標.xs

```xs
{@type:indicator}
// XQ: AR指標
// 
input: Length(26);
variable: sum(0), ar(0);

SetInputName(1, "天數");

sum = Summation((Open - Low), Length);
if sum <> 0 then
	ar = 100 * Summation((High - Open), length) / sum
else
	ar = ar[1];

Plot1(ar, "AR(%)");
```

---


---

## 腳本檔案: 指標/XQ技術指標/ATR (平均真實區域).xs

```xs
{@type:indicator}
// XQ: ATR指標
//
input: Length(14);

SetInputName(1, "天數");

value1 = Average(TrueRange, Length);
Plot1(value1, "ATR");
```

---


---

## 腳本檔案: 指標/XQ技術指標/BBand width (布林通道寬度指標).xs

```xs
{@type:indicator}
// XQ: BBandWidth指標
//
input: Length(20), UpperBand(2), LowerBand(2), EMALength(3);
variable: up(0), down(0), mid(0), bbandwidth(0), ema(0);

SetInputName(1, "天數");
SetInputName(2, "上");
SetInputName(3, "下");
SetInputName(4, "EMA");

up = bollingerband(Close, Length, UpperBand);
down = bollingerband(Close, Length, -1 * LowerBand);
mid = (up + down) / 2;

bbandwidth = 100 * (up - down) / mid;
ema = XAverage(bbandwidth, EMALength);

Plot1(bbandwidth , "BBand width(%)");
Plot2(ema, "Band% EMA");
```

---


---

## 腳本檔案: 指標/XQ技術指標/BIAS 乖離率.xs

```xs
{@type:indicator}
// XQ 乖離率
//
input: Length1(5), Length2(10), Length3(20);

SetInputName(1, "天數一");
SetInputName(2, "天數二");
SetInputName(3, "天數三");

Plot1(Bias(Length1), "BIAS1(%)");
Plot2(Bias(Length2), "BIAS2(%)");
Plot3(Bias(Length3), "BIAS3(%)");
```

---


---

## 腳本檔案: 指標/XQ技術指標/BR 指標.xs

```xs
{@type:indicator}
// XQ BR指標
//
input: Length(26);
variable: sum(0), _br(0);

SetInputName(1, "天數");

sum= Summation((Close[1] - Low), length);
if sum <> 0 then
	_br = 100 * Summation((High - Close[1]), length) / sum
else
	_br = _br[1];

Plot1(_br, "BR(%)");
```

---


---

## 腳本檔案: 指標/XQ技術指標/CCI (商品通道指標).xs

```xs
{@type:indicator}
// XQ: CCI指標
//
input: 
Length1(14,"天數一"), 
Length2(28,"天數二"), 
Length3(42,"天數三"),
UpBaseLine(100,"上基準線"), 
MidBaseLine(0,"中基準線"), 
UnderBaseLine(-100,"下基準線");

Plot1(CommodityChannel(Length1), "CCI1");
Plot2(CommodityChannel(Length2), "CCI2");
Plot3(CommodityChannel(Length3), "CCI3");
plot4(UpBaseLine, "上基準線", checkbox:=0);
plot5(MidBaseLine, "中基準線", checkbox:=0);
plot6(UnderBaseLine, "下基準線" , checkbox:=0);
```

---


---

## 腳本檔案: 指標/XQ技術指標/DMI (趨向指標).xs

```xs
{@type:indicator}
// XQ: DMI指標
//
input: Length(14);
variable: pdi_value(0), ndi_value(0), adx_value(0);

SetInputName(1, "天數");

DirectionMovement(Length, pdi_value, ndi_value, adx_value);

// 初始區波動較大, 先不繪出
//
if CurrentBar < Length then
 begin
	pdi_value = 0;
	ndi_value = 0;
	adx_value = 0;
 end;
 
Plot1(pdi_value, "+DI");
Plot2(ndi_value, "-DI");
Plot3(adx_value, "ADX");
```

---


---

## 腳本檔案: 指標/XQ技術指標/DMI-Osc(趨向擺盪線).xs

```xs
{@type:indicator}
// XQ: DMI-Osc指標
//
input: Length( 14 );
variable: pdi_value(0), ndi_value(0), adx_value(0);

SetInputName(1, "天數");

DirectionMovement(Length, pdi_value, ndi_value, adx_value);

// 初始區波動較大, 先不繪出
//
if CurrentBar < Length then
 begin
	pdi_value = 0;
	ndi_value = 0;
	adx_value = 0;
 end;

Plot1(pdi_value - ndi_value, "DMI-Osc");
```

---


---

## 腳本檔案: 指標/XQ技術指標/DPO (非趨勢價格擺盪指標).xs

```xs
{@type:indicator}
// XQ: DPO指標
//
input: Length(10);
variable: dpo(0);

SetInputName(1, "天數");

dpo = Close - Average(Close, Length)[(Length /2) + 1];

Plot1(dpo, "DPO");
```

---


---

## 腳本檔案: 指標/XQ技術指標/HL-Osc (高低價擺盪指標).xs

```xs
{@type:indicator}
// XQ: HL-Osc 指標
//
variable: tr(0), hlo(0);

tr = TrueRange;
if tr <> 0 then
	hlo = 100 * (H - C[1]) / tr
else
	hlo = 0;

plot1(hlo, "HL-Osc");
```

---


---

## 腳本檔案: 指標/XQ技術指標/KD 隨機指標.xs

```xs
{@type:indicator}
// XQ: KD指標
//
input: Length(9), RSVt(3), Kt(3);
variable: rsv(0), k(0), _d(0);

SetInputName(1, "天數");
SetInputName(2, "RSVt權數");
SetInputName(3, "Kt權數");

Stochastic(Length, RSVt, Kt, rsv, k, _d);

Plot1(k, "K(%)");
Plot2(_d, "D(%)");
```

---


---

## 腳本檔案: 指標/XQ技術指標/KDJ 隨機指標.xs

```xs
{@type:indicator}
// XQ: KDJ指標
//
input: Length(9), RSVt(3), Kt(3), JType(0);
variable: rsv(0), k(0), _d(0), j(0);

SetInputName(1, "天數");
SetInputName(2, "RSVt權數");
SetInputName(3, "Kt權數");

Stochastic(Length, RSVt, Kt, rsv, k, _d);

Plot1(k, "K(%)");
Plot2(_d, "D(%)");

if JType = 0 then
	j = 3 * k - 2 * _d
else
	j = 3 * _d - 2 * k;

Plot3(j, "J(%)");
```

---


---

## 腳本檔案: 指標/XQ技術指標/MA-Osc (移動平均線擺盪指標).xs

```xs
{@type:indicator}
// XQ: MA-Osc
//
input: Length1(5), Length2(10);

SetInputName(1, "天數一");
SetInputName(2, "天數二");

value1 = Average(close, Length1);
value2 = Average(close, Length2);
value3 = (value1 - value2);

Plot1(value3, "MA-Osc");
```

---


---

## 腳本檔案: 指標/XQ技術指標/MACD 指標.xs

```xs
{@type:indicator}
// XQ: MACD指標
//
input: FastLength(12), SlowLength(26), MACDLength(9);
variable: price(0);

SetInputName(1, "DIF短天數");
SetInputName(2, "DIF長天數");
SetInputName(3, "MACD天數");

price = WeightedClose();

Value1 = XAverage(price, FastLength) - XAverage(price, SlowLength);
Value2 = XAverage(Value1, MACDLength) ;
Value3 = Value1 - Value2 ;

// 前面區段資料變動較大, 先不繪出
//
if CurrentBar <= SlowLength then
begin
	Value1 = 0;
	Value2 = 0;
	Value3 = 0;
end;

Plot1(Value1, "DIF");
Plot2(Value2, "MACD");
Plot3(Value3, "Osc");
```

---


---

## 腳本檔案: 指標/XQ技術指標/MAM(移動平均動量指標).xs

```xs
{@type:indicator}
// XQ: MAM指標
//
Input: Length(10), Distance(10);
Variable: mam(0);

SetInputName(1, "天數一");
SetInputName(2, "天數二");

Value1 = Average(Close, Length);
Value2 = Average(Close, Length)[Distance];

mam = Value1 - Value2;
	
Plot1(mam, "MAM");
```

---


---

## 腳本檔案: 指標/XQ技術指標/MI(質量指標).xs

```xs
{@type:indicator}
// XQ: MI指標
//
input: Length(9), SumLength(25);
variable: ema1(0), ema2(0), divSeries(0), mi(0);

SetInputName(1, "天數一");
SetInputName(2, "天數二");

ema1 = XAverage(High - Low, length);
ema2 = XAverage(ema1, length);

if ema2 <> 0 then
	divSeries = ema1 / ema2
else
	divSeries = 0;

if CurrentBar >= sumLength then
	mi = Summation(divSeries, sumLength)
else
	mi = 0;
	
Plot1(mi, "MI");
```

---


---

## 腳本檔案: 指標/XQ技術指標/MO(運動量擺盪指標).xs

```xs
{@type:indicator}
// XQ: MO指標
//
input: Length(10);
variable: mo(0);

SetInputName(1, "天數");

mo = 100 * Close / Close[Length];

Plot1(mo, "MO");
```

---


---

## 腳本檔案: 指標/XQ技術指標/MTM(動量指標).xs

```xs
{@type:indicator}
// XQ: MTM指標
//
input: Length(10);

SetInputName(1, "天數");

value1 = Momentum(Close, Length); 
if CurrentBar >= Length then
	Value2 = Average(Value1, Length)
else
	Value2 = Value1;
	
Plot1(value1, "MTM");
Plot2(value2, "MA");
```

---


---

## 腳本檔案: 指標/XQ技術指標/PSY 心理線.xs

```xs
{@type:indicator}
// XQ: 心理線
//
input: Length1(12), Length2(24);

SetInputName(1, "天數一");
SetInputName(2, "天數二");

Value1 = 100 * CountIf(Close > Close[1], Length1) / Length1;
Value2 = 100 * CountIf(Close > Close[1], Length2) / Length2;

Plot1(Value1, "PSY1");
Plot2(Value2, "PSY2");
```

---


---

## 腳本檔案: 指標/XQ技術指標/RC(價格變動率指標).xs

```xs
{@type:indicator}
// XQ: RC指標
//
input: Length(12), EMALength(12);

SetInputName(1, "天數");
SetInputName(2, "平滑天數");

value1 = (Close - Close[Length]) / Close[Length];
value2 = XAverage(value1, EMALength);

Plot1(value1, "RC");
Plot2(value2, "ERC");
```

---


---

## 腳本檔案: 指標/XQ技術指標/RSI指標.xs

```xs
{@type:indicator}
// XQ: RSI指標
//
input: Length1(6), Length2(12);

SetInputName(1, "天數一");
SetInputName(2, "天數二");

Plot1(RSI(Close, Length1), "RSI1");
Plot2(RSI(Close, Length2), "RSI2");
```

---


---

## 腳本檔案: 指標/XQ技術指標/RSV 指標.xs

```xs
{@type:indicator}
// XQ: RSV指標
//
input: Length(9);
variable: RSVt(3), Kt(3), rsv(0), k(0), _d(0);

SetInputName(1, "天數");

Stochastic(Length, RSVt, Kt, rsv, k, _d);

Plot1(rsv, "RSV(%)");
```

---


---

## 腳本檔案: 指標/XQ技術指標/TRIX(三重指數平滑移動平均指標).xs

```xs
{@type:indicator}
// XQ: TRIX指標
//
input: Length1(9), Length2(15);

SetInputName(1, "天數一");
SetInputName(2, "天數二");

Value1 = TRIX(Close, Length1) * 100;
Value2 = TRIX(Close, Length2) * 100;

Plot1(Value1, "TRIX1");
Plot2(Value2, "TRIX2");
```

---


---

## 腳本檔案: 指標/XQ技術指標/VHF(垂直水平過濾指標).xs

```xs
{@type:indicator}
// XQ: VHF指標
//
input: Length(42);
Variable: hp(0), lp(0), numerator(0), denominator(0), _vhf(0);

SetInputName(1, "天數");

hp = highest(Close, Length);
lp = lowest(Close, Length);

numerator = hp - lp;
denominator = Summation(absvalue((Close - Close[1])), Length);

if denominator <> 0 then
	_vhf = numerator / denominator
else
	_vhf = 0;

Plot1(_vhf, "VHF");
```

---


---

## 腳本檔案: 指標/XQ技術指標/WAD 威廉多空力度線.xs

```xs
{@type:indicator}
// XQ: WA/D 指標
//

variable: wad(0), _ad(0);

if CurrentBar = 1 then
	wad = 0
else
  begin	
	if close = close[1] then
		_ad = 0
	else	
	  begin
		if close < close[1] then
			_ad = close - TrueHigh
		else { close > close[1] }
			_ad = close - TrueLow;
	  end;

	wad = _ad + wad[1];
  end;
  
Plot1(wad, "WA/D");
```

---


---

## 腳本檔案: 指標/XQ技術指標/威廉指標.xs

```xs
{@type:indicator}
// XQ: 威廉指標
//
input: Length1(14), Length2(28), Length3(42);

SetInputName(1, "天數一");
SetInputName(2, "天數二");
SetInputName(3, "天數三");

value1 = PercentR(Length1) - 100;
value2 = PercentR(Length2) - 100;
value3 = PercentR(Length3) - 100;

Plot1(value1, "威廉指標1");
Plot2(value2, "威廉指標2");
Plot3(value3, "威廉指標3");
```

---


---

## 腳本檔案: 指標/XQ技術指標/快速KD 隨機指標.xs

```xs
{@type:indicator}
// XQ: 快速KD指標
//
input: Length(9), RSVt(3);
variable: rsv(0), k(0), _d(0);

SetInputName(1, "天數");
SetInputName(2, "RSVt權數");

Stochastic(Length, RSVt, 3, rsv, k, _d);

Plot1(rsv, "K(%)");
Plot2(k, "D(%)");
```

---


---

## 腳本檔案: 指標/XQ量能指標/CV(積量指標).xs

```xs
{@type:indicator}
// XQ: CV指標
//
Variable: _cv(0);

If CurrentBar = 1 then
	_cv = Close * Volume
else	
	_cv = _cv[1] + (Close - Close[1]) * Volume;

Plot1(_cv, "CV");
```

---


---

## 腳本檔案: 指標/XQ量能指標/CVI(累計成交量指標).xs

```xs
{@type:indicator}
// XQ: CVI指標
//
variable: _cvi(0);

If CurrentBar > 1 then
	_cvi = _cvi[1] + GetField("UpVolume") - GetField("DownVolume");

Plot1(_cvi, "CVI");
```

---


---

## 腳本檔案: 指標/XQ量能指標/EMV(簡易波動指標).xs

```xs
{@type:indicator}
// XQ: EMV指標
//
Input: Length(14);
variable: _emv(0), factor(10000), avg(0);

SetInputName(1, "天數");

if Volume = 0 then
	_emv = 0
else
	_emv = factor * (((High + Low) / 2 - (High[1] + Low[1]) / 2) * (High - Low)) / Volume;

Plot1(_emv, "EMV");


If CurrentBar >= Length Then
	avg = Average(_emv, Length)
else
	avg = _emv;	

Plot2(avg, "EMVA");
```

---


---

## 腳本檔案: 指標/XQ量能指標/MFI(資金流向指標).xs

```xs
{@type:indicator}
// XQ: MFI指標
//
Input: Length(6);
variable: tp(0), tv(0), utv(0), dtv(0), pmf(0), nmf(0), mfivalue(0);

SetInputName(1, "天數");

tp = TypicalPrice;
tv = tp * Volume;

if tp > tp[1] then
  begin
	utv = tv;
	dtv = 0;
  end
else
  begin
	utv = 0;
	dtv = tv;
  end;

pmf = Average(utv, MinList(CurrentBar, length));
nmf = Average(dtv, MinList(CurrentBar, length));


if CurrentBar < Length or (pmf + nmf) = 0 then
	mfivalue = 50
else 
	mfivalue = 100 * pmf /(pmf + nmf);

Plot1(mfivalue, "MFI");
```

---


---

## 腳本檔案: 指標/XQ量能指標/NVI(負量指標).xs

```xs
{@type:indicator}
// XQ: NVI指標
//
Variable: _nvi(1);

if CurrentBar = 1 then
	_nvi = 1
else
  begin	
	if Volume < Volume[1] then
		_nvi = _nvi[1] + (Close - Close[1]) / Close[1]
	else
		_nvi = _nvi[1];
  end;
  
Plot1(_nvi, "NVI");
```

---


---

## 腳本檔案: 指標/XQ量能指標/OBV(能量潮指標).xs

```xs
{@type:indicator}
// XQ: OBV指標
//
input:SMAlength(5,"OBV的短MA期數"), MMAlength(20,"OBV的中MA期數");
variable: obvolume(0), obvSMA(0), obvSMA_Str(""), obvMMA(0), obvMMA_Str("");

if CurrentBar = 1 then
	obvolume = 0
else
  begin	
	if close > close[1] then
		obvolume = obvolume[1] + volume
	else
	  begin
		if close < close[1] then
			obvolume = obvolume[1] - volume
		else
			obvolume = obvolume[1];
	  end;		
  end;

obvSMA = average(obvolume,SMAlength);
obvMMA = average(obvolume,MMAlength);

obvSMA_Str = text(numToStr(SMAlength,0),"MA");
obvMMA_Str = text(numToStr(MMAlength,0),"MA");
  
Plot1(obvolume,"OBV");
plot2(obvSMA,"SMA",checkbox:=1);
plot3(obvMMA,"MMA",checkbox:=1);
setplotLabel(2,obvSMA_Str);
setplotLabel(3,obvMMA_Str);
```

---


---

## 腳本檔案: 指標/XQ量能指標/PVC(成交量變動百分比指標).xs

```xs
{@type:indicator}
// XQ: PVC指標
//
Input: Length(10);
Variable: _pvc(0);

SetInputName(1, "天數");

value1 = Average(Volume, Length);
if value1 <> 0 then
	_pvc = 100 * (Volume - value1) / value1
else
	_pvc = 0;

Plot1(_pvc, "PVC");
```

---


---

## 腳本檔案: 指標/XQ量能指標/PVI(正量指標).xs

```xs
{@type:indicator}
// XQ: PVI指標
//
Variable: _pvi(1);

If CurrentBar = 1 then
	_pvi = 1
else
  begin	
	if Volume > Volume[1] then
		_pvi = _pvi[1] + (Close - Close[1]) / Close[1]
	else
		_pvi = _pvi[1];
  end;
  
Plot1(_pvi, "PVI");
```

---


---

## 腳本檔案: 指標/XQ量能指標/PVT(價量趨勢指標).xs

```xs
{@type:indicator}
// XQ: PVT指標
//
variable: _pvt(0);

If CurrentBar = 1 then
	_pvt = 0
else	
	_pvt = _pvt[1] + (close - close[1])/close[1] * Volume;

Plot1(_pvt, "PVT");
```

---


---

## 腳本檔案: 指標/XQ量能指標/TAPI(每點成交值指標).xs

```xs
{@type:indicator}
// XQ: TAPI指標
//

Plot1(Volume / Close, "TAPI");
```

---


---

## 腳本檔案: 指標/XQ量能指標/VA(成交量累積散佈指標).xs

```xs
{@type:indicator}
// XQ: VA指標
//
Variable: _va(0);

if High <> Low then
	Value1 = ((Close - Low) - (High - Close))/(High - Low) * Volume
else
	Value1 = 0;

If CurrentBar = 1 then
	_va = Value1
else	
	_va = Value1 + _va[1];

Plot1(_va, "VA");
```

---


---

## 腳本檔案: 指標/XQ量能指標/VAOsc(成交量累積散佈擺盪指標).xs

```xs
{@type:indicator}
// XQ: VA-Osc指標
//
variable: support(0), resist(0), hlDiff(0), netSupportResist(0);
 
support = (Close - Low);
resist = (High - Close);
hlDiff = (High - Low);

if hlDiff = 0 then
	netSupportResist = 0
else
	netSupportResist = (support - resist) / hlDiff;
	
Plot1(netSupportResist * Volume, "VA-Osc");
```

---


---

## 腳本檔案: 指標/XQ量能指標/VR(成交量比率指標).xs

```xs
{@type:indicator}
// XQ: VR指標
//
input: Length(26);
variable: _index(0), qu(0), qd(0), qf(0), _vr(0);

SetInputName(1, "天數");

qf = 0;
qu = 0;
qd = 0;
for _index = 1 to length
  begin
	if close[(_index - 1)] > close[_index] then
		qu = qu + Volume[(_index - 1)]
	else
	  begin
		if close[(_index - 1)] < close[_index] then
			qd = qd + Volume[(_index - 1)]
		else { close[(_index - 1)] = close[_index] }
			qf = qf + Volume[(_index - 1)];
	  end;
  end;

if (qd + qf/2) <> 0 then
  _vr = 100 * (qu + qf/2) /(qd + qf/2)
else
  _vr = 1000;

Plot1(_vr, "VR");
```

---


---

## 腳本檔案: 指標/XQ量能指標/VRC(成交量變動指標).xs

```xs
{@type:indicator}
// XQ: VRC指標
//
Input: Length(12);
Variable: _vrc(0);

SetInputName(1, "天數");

if volume[Length] <> 0 then
	_vrc = 100 * (volume - volume[Length])/volume[Length]
else
	_vrc = 50;

Plot1(_vrc, "VRC");
```

---


---

## 腳本檔案: 指標/XQ量能指標/VVA指標.xs

```xs
{@type:indicator}
// XQ: VVA指標
//
variable: _vva(0);

if High <> Low then
	Value1 = (Close - Open)/(High - Low) * Volume
else
	Value1 = 0;

If CurrentBar = 1 then
	_vva = Value1
else	
	_vva = Value1 + _vva[1];

Plot1(_vva, "VVA");
```

---


---

## 腳本檔案: 指標/XQ量能指標/投資建議目標價潛在獲利率.xs

```xs
{@type:indicator}
//支援頻率：不定期
//支援商品 ：美(股票)
var:exchange("");
exchange = GetSymbolInfo("交易所");
if exchange <> "NYSE" and exchange <> "NASDAQ" and exchange <> "AMEX" then raiseruntimeerror("僅支援美股");

if getField("投資建議目標價") <> 0 then
value1 = (getField("投資建議目標價")-close)/getField("投資建議目標價")
else value1 = 0;

plot1(value1,"潛在獲利率");
```

---


---

## 腳本檔案: 指標/XQ量能指標/投資建議評級(%).xs

```xs
{@type:indicator}
//支援頻率：不定期
//支援商品 ：美(股票)
{ 說明：
value1 = getField("投資建議評級");
1<= value1 < 1.5 (SB_積極買進)
1.5 <= value1 < 2.5 (B_買進)
2.5 <= value1 < 3.5 (H_中立)
3.5 <= value1 < 4.5 (S_賣出)
4.5 <= value1 <= 5(SS_積極賣出) 
}
var:exchange("");
exchange = GetSymbolInfo("交易所");
if exchange <> "NYSE" and exchange <> "NASDAQ" and exchange <> "AMEX" then raiseruntimeerror("僅支援美股");

var:_rank(0);
value1 = getField("投資建議評級");
if value1 = 0 then raiseruntimeerror("無投資建議評級的歷史紀錄");
_rank = (5-value1)/4; //將投資建議評級，轉成0~100的分布形式

plot1(_rank);

if 1>=_rank and _rank>0.875 then begin
	plot20(_rank);
	setplotLabel(1,"積極買進");
end else if 0.875>=_rank and _rank>0.625 then begin 
	plot21(_rank);
	setplotLabel(1,"買進");
end else if 0.625>=_rank and _rank>0.375 then begin
	plot22(_rank);
	setplotLabel(1,"中立");
end else if 0.375>=_rank and _rank>0.125 then begin
	plot23(_rank);
	setplotLabel(1,"賣出");
end else if 0.125>=_rank and _rank>=0 then begin
	plot24(_rank);
	setplotLabel(1,"積極賣出");
end;
```

---


---

## 腳本檔案: 指標/XQ量能指標/新聞分數.xs

```xs
{@type:indicator}
{
	XQ量能指標。
	支援日頻率。支援上市櫃普通股商品。
}

value1 = GetField("新聞正向分數") - GetField("新聞負向分數"); 
//新聞總分=正向分數－負向分數。來判斷目前的新聞聲量為正向或者負向。

plot1(value1,"新聞總分");//正向分數-負向分數
plot2(GetField("新聞聲量分數"),"新聞總量",checkbox:=1);//正向分數+負向分數
plot3(GetField("新聞正向分數"),"新聞正總量",checkbox:=0);
plot4(GetField("新聞負向分數"),"新聞負總量",checkbox:=0);
```

---


---

## 腳本檔案: 指標/主圖指標/BBand軌道線.xs

```xs
{@type:indicator}
input: 
	Length(20, "MA的天數"), 
	UpperBand(2, "上通道標準差倍數"), 
	LowerBand(2, "下通道標準差倍數");
variable: mid(0), up(0), down(0);

up = bollingerband(Close, Length, UpperBand);
mid = average(close, Length);
down = bollingerband(Close, Length, -1 * LowerBand);

plot1(up, "UB");
plot2(mid, "BBandMA");
plot3(down, "LB");
```

---


---

## 腳本檔案: 指標/主圖指標/CDP.xs

```xs
{@type:indicator}
{
    PlotLine(PlotIndex, x1, y1, x2, y2, add:=0);
	    PlotIndex為 1 ~ 999，作用如同 Plot 的序列編號
		x1 為起點的 Bar Number (可用 CurrentBar 確認)
		y1 為起點的 Y 軸數值 (ex. 價格)
		x2 為終點的 Bar Number
		add 為非必要參數，預設為 0，執行後會先清除之前的趨勢線，若不希望清除的話則可以設為 1。
		
    CDP指標
 
    CDP＝(H[1] + L[1] + 2C[1])/4
    AH = CDP + (H[1]-L[1])
	NH = 2*CDP - L[1]
	NL = 2*CDP - H[1]
    AL = CDP - (H[1]-L[1])
 
	只支援分鐘線
}

input: plotLen(1, "繪圖區間", inputkind:= Dict(["每日", 1], ["當日", 2]));

if BarFreq <> "Min" then RaiseRunTimeError("請跑分鐘頻率");
 
var: HH(0), LL(0), CC(0);
var: CDP(0), AH(0), NH(0), NL(0), AL(0);
 
var: bar_count(0);
var: x1_bar(0);
 
//換日時計算當日的CDP數值
if GetFieldDate("Date") <> GetFieldDate("Date")[1] then begin

    bar_count = 0;
    x1_bar = CurrentBar;
 
    HH = GetField("High", "D")[1];
    LL = GetField("Low", "D")[1];
    CC = GetField("Close", "D")[1];

    CDP = (HH + LL + 2*CC) / 4;
    AH = CDP + HH - LL;
	NH = 2*CDP - LL;
	NL = 2*CDP - HH;
    AL = CDP - (HH - LL);
end;

if plotLen = 1 then begin
	if x1_bar <> 0 then begin
		PlotLine(1, x1_bar, CDP, CurrentBar, CDP, "CDP", add:=1);
		PlotLine(2, x1_bar, NH, CurrentBar, NH, "NH", add:=1);
		PlotLine(3, x1_bar, NL, CurrentBar, NL, "NL", add:=1);
		PlotLine(4, x1_bar, AH, CurrentBar, AH, "AH", add:=1);
		PlotLine(5, x1_bar, AL, CurrentBar, AL, "AL", add:=1);
	    end;
	end
else if plotLen = 2 then begin
	if islastBar then begin
		PlotLine(1, x1_bar, CDP, CurrentBar, CDP, "CDP");
		PlotLine(2, x1_bar, NH, CurrentBar, NH, "NH");
		PlotLine(3, x1_bar, NL, CurrentBar, NL, "NL");
		PlotLine(4, x1_bar, AH, CurrentBar, AH, "AH");
		PlotLine(5, x1_bar, AL, CurrentBar, AL, "AL");
	    end;
	end;
```

---


---

## 腳本檔案: 指標/主圖指標/EMA.xs

```xs
{@type:indicator}
Input: Period1(50); SetInputName(1, "EMA1");
Input: Period2(120); SetInputName(2, "EMA2");
Input: Period3(240); setinputname(3, "EMA3");

Plot1(EMA(Close, Period1), "EMA1");
Plot2(EMA(Close, Period2), "EMA2");
Plot3(EMA(Close, Period3), "EMA3");
```

---


---

## 腳本檔案: 指標/主圖指標/SAR.xs

```xs
{@type:indicator}
input:		
	AFInitial(0.02, "加速因子起始值"), 
	AFIncrement(0.02, "加速因子累加值"), 
	AFMax(0.2, "加速因子最高值");

plot1(SAR(AFInitial, AFIncrement, AFMax), "SAR");
```

---


---

## 腳本檔案: 指標/主圖指標/ZigZag.xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 指標/主圖指標/一目均衡表.xs

```xs
{@type:indicator}
input: ConvPeriod(9, "轉換天數");
input: BasePeriod(26, "樞紐天數");
input: LagPeriod(52, "延遲天數");

// 轉換線
Value1 = (Highest(High, ConvPeriod) + Lowest(Low, ConvPeriod)) / 2;

// 樞紐線
Value2 = (Highest(High, BasePeriod) + Lowest(Low, BasePeriod)) / 2;

// 先行帶 A
Value3 = (Value1 + Value2) / 2;

// 先行帶 B
Value4 = (Highest(High, LagPeriod) + Lowest(Low, LagPeriod)) / 2;  

Plot(1, value1, "轉換線");
Plot(2, value2, "樞紐線");
Plot(3, Close, "後行時間", shift:=-BasePeriod);
Plot(4, Value3, "先行時間(1)", shift:=BasePeriod);
Plot(5, Value4, "先行時間(2)", shift:=BasePeriod);
if value3 > value4 then begin 
    PlotFill(6, Value3, Value4, shift:=BasePeriod);
	noplot(7);
	end
else begin 
    plotfill(7, Value3, Value4, shift:=BasePeriod);	
	noplot(6);
	end;
```

---


---

## 腳本檔案: 指標/主圖指標/修正式移動平均線.xs

```xs
{@type:indicator}
input:n(20,"計算期數");
variable: w(0);

if barfreq = "Tick" or barfreq = "Min" then
begin
	value1=GetField("內盤量");//單位:元
	value2=GetField("外盤量");//單位:元
end else begin
	value1=GetField("內盤量","D");//單位:元
	value2=GetField("外盤量","D");//單位:元
end;

//計算內外盤比
if value2<>0 then
	value3=value1/value2*100
else
	value3=100;

if close>close[1] then begin
	if value3>130 then 
		w=2.5
	else if value3>120 then
		w=2.2
	else if value3>110 then
		w=2.1
	else if value3>100 then
		w=1.9
	else
		w=1.8;
end else if value3<70 then 
		w=2.5
	else if value3<80 then 
		w=2.2
	else if value3<90 then 
		w=2.1
	else if value3<100 then 
		w=1.9
	else
		w=1.8;

value4=(w/(n+1))*close+(n-1)/(n+1)*value4[1];
value5=average(close,n);

plot2(value5,"移動平均線");
```

---


---

## 腳本檔案: 指標/主圖指標/個股儀表板.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/打造個股儀表板/
收錄於「三週學會程式交易：打造你的第一筆自動化交易」 330頁
https://www.ipci.com.tw/books_in.php?book_id=724
}

if barfreq <> "D" then raiseruntimeerror("不支援此頻率");

condition1=false;
condition2=false;
condition3=false;
condition4=false;
condition5=false;
condition6=false;
condition7=false;
condition8=false;
condition9=false;
condition10=false;

switch(close)
begin
	case >150: value5=low*0.9;
	case <50 : value5=low*0.98;
	default: value5=low*0.95;
end;

//==========日KD黃金交叉================
input: _TEXT1("===============","KD參數");
input: Length_D(9,"日KD期間");

variable:rsv_d(0),kk_d(0),dd_d(0),c5(0);

stochastic(Length_D, 3, 3, rsv_d, kk_d, dd_d);
c5=barslast(kk_d crosses over dd_d);
if c5=0 and c5[1]>20 then 
	condition1=true;
if condition1 then
	plot1(value5,"月KD高檔鈍化且日KD黃金交叉");

//============內外盤量比差====================
variable:c3(0);
value6=GetField("內盤量");//單位:元
value7=GetField("外盤量");//單位:元
if volume<>0 then begin
	value8=value7/volume*100;//外盤量比
	value9=value6/volume*100;//內盤量比
end;
value10=average(value8,5);
value11=average(value9,5);
value7=value10-value11+5;
c3=barslast(value7 crosses over 0);
if c3=0 and c3[1]>20 then
	condition2=true;
if condition2 then
	plot2(value5*0.99,"內外盤量比差");

//===========淨力指標==============
input: _TEXT2("===============","淨力指標參數");
input:period2(10,"長期參數");

variable:c4(0);

value12=summation(high-close,period2);//上檔賣壓
value13=summation(close-open,period2); //多空實績
value14=summation(close-low,period2);//下檔支撐
value15=summation(open-close[1],period2);//隔夜力道
if close<>0 then
	value16=(value13+value14+value15-value12)/close*100;
c4=barslast(value16 crosses over -4);
if c4=0 and c4[1]>20 then
	condition3=true;
if condition3 then
	plot3(value5*0.98,"淨力指標");

//===========多頭起漲前的籌碼收集================
variable:c2(0);
//狀況1.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量=0，則交易家數相關指標回傳0。
//狀況2.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量<>0，則交易家數相關指標正常運算。
if getfieldDate("date") <> getfieldDate("分公司買進家數") and GetField("成交量") = 0 then value1=GetField("分公司買進家數");
if getfieldDate("date") <> getfieldDate("分公司賣出家數") and GetField("成交量") = 0 then value2=GetField("分公司賣出家數");
value3=value2-value1;
value4=countif(value3>20,10);
c2=barslast(value4>6);
if c2=0 and c2[1]>20 then
	condition4=true;
if condition4=true then
	plot4(value5*0.97,"籌碼收集");

//===========法人同步買超====================
variable: v1(0),v2(0),v3(0),c1(0);
v1=GetField("外資買賣超");
v2=GetField("投信買賣超");
v3=GetField("自營商買賣超");
c1= barslast(maxlist2(v1,v2,v3)>100);
if c1=0 and c1[1]>20 then
	condition5=true;
if condition5=true then
	plot5(value5*0.96,"法人同步買超");

//========DIF-MACD 翻正=============
input: _TEXT3("===============","MACD參數");
input: FastLength(12,"DIF短天數"), SlowLength(26, "DIF長天數"), MACDLength(9, "MACD天數");
variable: difValue(0), macdValue(0), oscValue(0);
MACD(weightedclose(), FastLength, SlowLength,MACDLength, difValue, macdValue, oscValue);
variable:c6(0);
c6=barslast(oscValue Crosses Above 0);
if c6=0 and c6[1]>20 then
	condition6=true;
if condition6 then
	plot6(value5*0.95,"DIF-MACD 翻正");

//========資金流向======================
variable: m1(0),ma1(0),c7(0);
m1=GetField("資金流向");
ma1=average(m1,20)*1.5;
c7=barslast(m1 crosses over ma1 and close>close[1]);
if c7=0 and c7[1]>20 then
	condition7=true;
if condition7 then
	plot7(value5*0.94,"資金流向");
	
//=========總成交次數================
variable: t1(0),mat1(0),c8(0);
t1=GetField("總成交次數","D");
mat1=average(t1,20)*1.5;
c8=barslast(t1 crosses over mat1 and close>close[1]);
if c8=0 and c8[1]>20 then
	condition8=true;
if condition8 then 
	plot8(value5*0.93,"成交次數");
	
//=========強弱指標==================
variable:s1(0),c9(0);
s1=GetField("強弱指標","D");
c9=barslast(trueall(s1>0,3));
if c9=0 and c9[1]>20 then
	condition9=true;
if condition9 then
	plot9(value5*0.92,"強弱指標");
	
//============開盤委買================
variable:b1(0),mab1(0),c10(0);
b1=GetField("主力買張");
mab1=average(b1,10);
c10=barslast(b1 crosses over mab1);
if c10=0 and c10[1]>10 then
	condition10=true;
if condition10 then 
	plot10(value5*0.91,"主力買張");
```

---


---

## 腳本檔案: 指標/主圖指標/內盤成本線.xs

```xs
{@type:indicator}
{內盤成本線 = 累計當日賣出金額(元) / 累計當日賣出量*1000, 就是特大+大+中+小, 不分大小單
支援商品：台股}

value91 = GetField("買進特大單金額");

if barfreq <> "Min" and barfreq <> "D" then 
	raiseruntimeerror("僅支援分鐘與日頻率");

value1 = GetField("賣出特大單金額","D") + GetField("賣出大單金額","D") + GetField("賣出中單金額","D") + GetField("賣出小單金額","D");
value2 = GetField("賣出特大單量","D") + GetField("賣出大單量","D") + GetField("賣出中單量","D") + GetField("賣出小單量","D");
if value2 <> 0 then
	value3 = value1 / (value2 * 1000)
else
	value3 = value3[1];
	
plot1(value3,"內盤成本線");
```

---


---

## 腳本檔案: 指標/主圖指標/唐奇安通道.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/唐奇安通道/
}

input:Period(13,"天數");

value1 = Highest(H, period);
value2 = Lowest(L, period);

plot1(value1[1],"通道上緣");
plot2((value1+value2)/2,"通道中線");
plot3(value2[1],"通道下緣" );
```

---


---

## 腳本檔案: 指標/主圖指標/外盤成本線.xs

```xs
{@type:indicator}
{外盤成本線 = 累計當日買進金額(元) / 累計當日買進量*1000, 就是特大+大+中+小, 不分大小單
支援商品：台股}

value91 = GetField("買進特大單金額");

if barfreq <> "Min" and barfreq <> "D" then 
	raiseruntimeerror("僅支援分鐘與日頻率");

value1 = GetField("買進特大單金額","D") + GetField("買進大單金額","D") + GetField("買進中單金額","D") + GetField("買進小單金額","D");
value2 = GetField("買進特大單量","D") + GetField("買進大單量","D") + GetField("買進中單量","D") + GetField("買進小單量","D");
if value2 <> 0 then
	value3 = value1 / (value2 * 1000)
else
	value3 = value3[1];

plot1(value3,"外盤成本線");
```

---


---

## 腳本檔案: 指標/主圖指標/外資均價線.xs

```xs
{@type:indicator}
Input: period(20);	setinputname(1, "期間(天)");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

variable: avg_b(0), avg_s(0);
if GetField("Volume") > 0 then 
begin
	Value5 = GetField("外資買張")*GetField("成交金額")/(GetField("Volume")*1000);
	Value6 = GetField("外資賣張")*GetField("成交金額")/(GetField("Volume")*1000);
end else begin
	Value5 = 0;
	Value6 = 0;
end;

Value1 = summation(Value5, period);
Value2 = summation(GetField("外資買張"), period);
Value3 = summation(Value6, period);
Value4 = summation(GetField("外資賣張"), period);
 
if Value2 > 0 and Value2 <> Value2[1] then avg_b = Value1 / Value2;
if Value4 > 0 and Value4 <> Value4[1]  then avg_s = Value3 / Value4;

Plot1(avg_b, "外資買進均價");
Plot2(avg_s, "外資賣出均價");
```

---


---

## 腳本檔案: 指標/主圖指標/大戶成本線.xs

```xs
{@type:indicator}
{大戶成本線有兩個線圖, 可以分開勾選, 
一個是買進成本線, 計算方式都是累計當日大單+特大單的買進金額/買進量
一個是賣出成本線, 計算方式都是累計當日大單+特大單的賣出金額/買進量
支援商品：台股}

value91 = GetField("買進特大單金額");

if barfreq <> "Min" and barfreq <> "D" then 
	raiseruntimeerror("僅支援分鐘與日頻率");
	
//買進成本
value1 = GetField("買進特大單金額","D") + GetField("買進大單金額","D");
value2 = GetField("買進特大單量","D") + GetField("買進大單量","D");
if value2 <> 0 then
	value3 = value1 / (value2*1000)
else
	value3 = value3[1];

//賣出成本
value11 = GetField("賣出特大單金額","D") + GetField("賣出大單金額","D");
value21 = GetField("賣出特大單量","D") + GetField("賣出大單量","D");
if value21 <> 0 then 
	value31 = value11 / (value21*1000)
else
	value31 = value31[1];

plot1(value3,"大戶買進成本線",checkbox:=1);
plot2(value31,"大戶賣出成本線",checkbox:=1);
```

---


---

## 腳本檔案: 指標/主圖指標/寶塔線.xs

```xs
{@type:indicator}
input: _len(3, "天數"), _reversal(1, "趨勢反轉判斷", inputkind:=Dict(["依據K線圖高/低點",1],["依據寶塔線高低/點",2]));

var: _name("");

SetBackBar(_len);

if _reversal = 1 then begin
    value1 = highest(high[1], _len);
    value2 = lowest(low[1], _len);
	end
else if _reversal = 2 then begin
    value1 = highest(value3[1], _len);
    value2 = lowest(value4[1], _len);
	end;

value3 = maxlist(close, close[1]);
value4 = minlist(close, close[1]);

if close cross over value1 then begin
    condition1 = True;
	condition2 = False;
	end
else if close cross under value2 then begin
    condition1 = False;
	condition2 = True;
	end;


if currentbar > _len then begin
    if not condition1[1] and condition1 then
	    _name = "翻紅"
	else if condition1 then
	    _name = "續紅"
	else if not condition2[1] and condition2 then
	    _name = "翻黑"
	else if condition2 then
	    _name = "續黑";
		
	if condition1 then 
	    plotk(1, value4, value3, value4, value3)
	else if condition2 then
	    plotk(1, value3, value3, value4, value4);
	end;
	
setplotLabel(1, text(_name));
```

---


---

## 腳本檔案: 指標/主圖指標/平均K線.xs

```xs
{@type:indicator}
var: ha_open(0), ha_high(0), ha_low(0), ha_close(0);


if currentbar = 1 then
  ha_open = (open + close) / 2
else
  ha_open = (ha_open[1] + ha_close[1]) / 2;


ha_close = (open + high + low + close) / 4;
ha_high = maxlist(high, ha_open, ha_close);
ha_low = minlist(low, ha_open, ha_close);


PlotK(1, ha_open, ha_high, ha_low, ha_close, "平均K線");
```

---


---

## 腳本檔案: 指標/主圖指標/平均波幅通道.xs

```xs
{@type:indicator}
input : length(5);			setinputname(1, "天期");
input : atrlength(15);		setinputname(2, "ATR天期");
input : k(1.35);			setinputname(3, "通道常數");
  
variable : hband(0),lband(0);  
       
hband = average(close,length)+average(truerange,atrlength)*k;  
lband = average(close,length)-average(truerange,atrlength)*k;  
       
plot1(hband, "通道上限");  
plot2(lband, "通道下限");
```

---


---

## 腳本檔案: 指標/主圖指標/投信均價線.xs

```xs
{@type:indicator}
Input: period(20);	setinputname(1, "期間(天)");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
variable: avg_b(0), avg_s(0);

if GetField("Volume") > 0 then 
begin
	Value5 = GetField("投信買張")*GetField("成交金額")/(GetField("Volume")*1000);
	Value6 = GetField("投信賣張")*GetField("成交金額")/(GetField("Volume")*1000);
end else begin
	Value5 = 0;
	Value6 = 0;
end;

Value1 = summation(Value5, period);
Value2 = summation(GetField("投信買張"), period);
Value3 = summation(Value6, period);
Value4 = summation(GetField("投信賣張"), period);
 
if Value2 > 0 and Value2 <> Value2[1] then avg_b = Value1 / Value2;
if Value4 > 0 and Value4 <> Value4[1]  then avg_s = Value3 / Value4;

Plot1(avg_b, "投信買進均價");
Plot2(avg_s, "投信賣出均價");
```

---


---

## 腳本檔案: 指標/主圖指標/投資建議目標價.xs

```xs
{@type:indicator}
//支援頻率：不定期
//支援商品 ：美(股票)
var:exchange("");
exchange = GetSymbolInfo("交易所");
if exchange <> "NYSE" and exchange <> "NASDAQ" and exchange <> "AMEX" then raiseruntimeerror("僅支援美股");

plot1(getField("投資建議目標價"),"目標價");
```

---


---

## 腳本檔案: 指標/主圖指標/散戶成本線.xs

```xs
{@type:indicator}
{散戶成本線內有兩個線圖, 可以分開勾選, 
一個是散戶買進成本線, 計算方式都是累計當日小單的買進金額/買進量
一個是散戶賣出成本線, 計算方式都是累計當日小單的賣出金額/買進量
支援商品：台股}

value91 = GetField("買進小單金額");

if barfreq <> "Min" and barfreq <> "D" then 
	raiseruntimeerror("僅支援分鐘與日頻率");
	
//買進成本
value1 = GetField("買進小單金額","D");
value2 = GetField("買進小單量","D");
if value2 <> 0 then
	value3 = value1 / (value2*1000)
else
	value3 = value3[1];

//賣出成本
value11 = GetField("賣出小單金額","D");
value21 = GetField("賣出小單量","D");
if value21 <> 0 then 
	value31 = value11 / (value21*1000)
else
	value31 = value31[1];

plot1(value3,"散戶買進成本線",checkbox:=1);
plot2(value31,"散戶賣出成本線",checkbox:=1);
```

---


---

## 腳本檔案: 指標/主圖指標/樂活五線譜.xs

```xs
{@type:indicator}
input:period(720,"計算期間");
array: line_diff[](0);
var: diff_avg(0), _sum(0);

Array_SetMaxIndex(line_diff, period);
linearreg(close,period,0,value2,value3,value4,value5);

{計算(收盤-迴歸)標準差}
//先計算區間內的 收盤 - 迴歸 值
_sum = 0;
for value1 = 1 to period begin
    line_diff[value1] = close[period - value1] - (value2 * value1 + value4);
	_sum += close[period - value1] - (value2 * value1 + value4);
	end;
// 收盤-迴歸的平均	
diff_avg = _sum / period;

//計算標準差
_sum = 0;
for value1 = 1 to period begin
    _sum += power((line_diff[value1] - diff_avg), 2);
	end;
value6 = squareroot(_sum / period);

value7=value5+value6;
value8=value5+2*value6;
value9=value5-value6;
value10=value5-2*value6;
plot1(value8,"+2SD");
plot2(value7,"+1SD");
plot3(value5,"TL");
plot4(value9,"-1SD");
plot5(value10,"-2SD");
```

---


---

## 腳本檔案: 指標/主圖指標/樂活五線譜_趨勢線.xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 指標/主圖指標/權益線分析.xs

```xs
{@type:indicator}
input:Update(-1);

variable:hHigh(0),pC(0),iHigh(0),iLow(10000),iDate(0),ALow(0),ND(0),EP(0);
array:peak[300,5](0);


if currentbar = 1 then begin 
	iHigh =high; 
	iDate =Date; 
	value1=open; 
end;

hHigh = maxlist(high,hHigh); 
if hHigh > iHigh  then begin
	if iHigh <> iLow then begin
		peak[pc,0] = date;
		peak[pc,1] = iHigh;
		peak[pc,2] = iLow;
		peak[pc,3] = (iHigh- iLow)/iHigh*100;
		peak[pc,4] = datediff(date,iDate);
		if pc > 0  and peak[pc-1,2] <> 0 then peak[pc,5] = (iHigh/ peak[pc-1,2]-1)*100;
		pc+=1;
	end;
	iHigh =hHigh;
	iLOw = hHigh;
	iDate =Date;
end else 
	iLow =minlist(Low,iLow);

if  DateDiff(currentdate,date) > update and value1 > 0 and pc > 1 then begin
	variable: summ(0),avg(0); 
	summ=0; 
	for value2 = 1 to pc -1  
		summ += peak[value2,3]; 
	avg=summ/(pc-1);
	variable: summeans(0); 
	summeans=0;
	for value2 = 1 to pc -1 begin
		summeans += square(peak[value2,3]-avg);
	end;
	variable:stdev(0); 
	if pc-1 > 0 then 
		stdev = squareroot( summeans/(pc-1)) 
	else 
		stdev=0;
    variable:msg("Hold"),poLow(0);
	poLow = iHigh*(1- (avg+stdev)/100);
	if Close < PoLow then msg ="Sell";
end;

if date <>currentdate then ALow =Polow;
if C > alow and ALow > 0 then  plot1(Alow,"95%CF");  //95%信心水準回檔最大值
if C > iHigh*0.86 then begin
	plot3(iHigh*0.92,"N1D"); //第1減碼線
	plot4(iHigh*0.86,"N2D"); //第2減碼線
end;
plot5(Close,"現價");
plot6(V,"成交量");

ND=100*(average(H/L-1,20)+standarddev(H/L-1,20,1)*3);
if ND < 3 and trueall(ND[1]> 3,5) then  EP=h;
if ND < 5 and trueall(ND[1]> 5,5) then EP=h;
if c > EP and c[1] < EP then plot8(v,"作多點量");
if EP > 0 then plot9(EP,"關鍵價");
```

---


---

## 腳本檔案: 指標/主圖指標/當日成本線.xs

```xs
{@type:indicator}
{均線 = 當日所有成交Tick的平均價格(sum(pv)/sum(v)), 也就是當日的成本
支援商品：台股/期貨/選擇權/陸股/港股/美股/大盤/類股}

if barfreq <> "Min" and barfreq <> "D" then 
	raiseruntimeerror("僅支援分鐘與日頻率");
	
plot1(GetField("均價"),"均價");
```

---


---

## 腳本檔案: 指標/主圖指標/肯特納通道.xs

```xs
{@type:indicator}
Input: Length(20); setinputname(1, "天期");
Input: UpperBand(2); SetInputName(2, "上通道寬度");
Input: LowerBand(2); SetInputName(3, "下通道寬度");

variable : hband(0),lband(0),midline(0); 

midline = XAverage(close, Length);
hband = midline + ATR(Length) * UpperBand;
lband = midline - ATR(Length) * LowerBand;

Plot1(hband, "UB");
Plot2(midline, "KeltnerMA");
Plot3(lband, "LB");
```

---


---

## 腳本檔案: 指標/主圖指標/自營商均價線.xs

```xs
{@type:indicator}
Input: period(20);	setinputname(1, "期間(天)");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
variable: avg_b(0), avg_s(0);

if GetField("Volume") > 0 then 
begin
	Value5 = GetField("自營商買張")*GetField("成交金額")/(GetField("Volume")*1000);
	Value6 = GetField("自營商賣張")*GetField("成交金額")/(GetField("Volume")*1000);
end else begin
	Value5 = 0;
	Value6 = 0;
end;
	
Value1 = summation(Value5, period);
Value2 = summation(GetField("自營商買張"), period);
Value3 = summation(Value6, period);
Value4 = summation(GetField("自營商賣張"), period);
 
if Value2 > 0 and Value2 <> Value2[1] then avg_b = Value1 / Value2;
if Value4 > 0 and Value4 <> Value4[1]  then avg_s = Value3 / Value4;

Plot1(avg_b, "自營商買進均價");
Plot2(avg_s, "自營商賣出均價");
```

---


---

## 腳本檔案: 指標/主圖指標/處置期間.xs

```xs
{@type:indicator}
if BarFreq <> "d" and BarFreq <> "ad" then raiseruntimeerror("僅支援日與還原日頻率");

value1 = GetField("處置開始日期");
value2 = GetField("處置結束日期");
value3 = getField("Date");
if value1 = 0 then raiseruntimeerror("無處置的歷史紀錄");

//用點顯示處置區間
if value3 >= value1 and value3 <= value2 then plot1(value1,"處置中") //尚在處置中
else noplot(1);

//用來顯示處置相關的日期數值
if value1 <> value1[1] or (value3 >= value1 and value3 <= value2) then begin
	plot3(value1,"開始日期");
	plot4(value2,"結束日期");
end else begin
	noplot(3);
	noplot(4);
end;
```

---


---

## 腳本檔案: 指標/主圖指標/融券均價線.xs

```xs
{@type:indicator}
Input: period(20);	setinputname(1, "期間(天)");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

variable: avg(0);

if GetField("Volume") > 0 then 
	Value3 = GetField("融券賣出張數")*GetField("成交金額")/(GetField("Volume")*1000)
else
	Value3 = 0;

Value1 = summation(Value3, period);
Value2 = summation(GetField("融券賣出張數"), period);
 
if Value2 > 0 and Value2 <> Value2[1] then avg = Value1 / Value2;

Plot1(avg, "融券賣出均價");
```

---


---

## 腳本檔案: 指標/主圖指標/融資均價線.xs

```xs
{@type:indicator}
Input: period(20);	setinputname(1, "期間(天)");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

variable: avg(0);

if GetField("Volume") > 0 then 
	Value3 = GetField("融資買進張數")*GetField("成交金額")/(GetField("Volume")*1000)
else
	Value3 = 0;

Value1 = summation(Value3, period);
Value2 = summation(GetField("融資買進張數"), period);
 
if Value2 > 0 and Value2 <> Value2[1] then avg = Value1 / Value2;

Plot1(avg, "融資買進均價");
```

---


---

## 腳本檔案: 指標/主圖指標/趨勢線.xs

```xs
{@type:indicator}
input: periods(30, "期間");
input: startyear(2017, "起始年份");

variable: maxh_bar(0), idx(0), line_a(0), line_b(0), x_bar(0), idx2(0), temp_y(0), base_bar(0);

// 起始年之前的資料不計算
if year(date) < startyear then return;

// 如果已經有趨勢線的話, 檢查是否突破
if base_bar > 0 then begin
	temp_y = line_a * (currentbar - base_bar) + line_b;
	if high > temp_y then 
		plot1(high) 
	else 
		noplot(1);	
end;

// 計算過去N期的趨勢線
maxh_bar = nthhighestbar(1, high, periods);

base_bar = 0;	// 用來追蹤最近一個趨勢線的x=0的位置
idx = maxh_bar-1;
while idx >= 0 begin
	// 畫一條曲線從maxh_bar to idx, 假設maxh_bar的位置x=0
	//
	// x0 = 0, y0 = high[maxh_bar] == b
	// x1 = maxh_bar - idx, y1 = high[idx]
	//
	line_b = high[maxh_bar];
	line_a = (high[idx] - line_b) / (maxh_bar - idx);
	x_bar = idx;

	// 檢查是否所有的點都落在這條切線底下
	//
	condition1 = false;
	for idx2 = maxh_bar - 1 downto 0 begin
		// x = maxh_bar - idx2
		//
		temp_y = line_a * (maxh_bar - idx2) + line_b;
		if high[idx2] > temp_y then begin
			condition1 = true;
			break;
		end;
	end;
	if not condition1 then begin
		base_bar = currentbar - maxh_bar;
		break; 
	end;
    idx = idx - 1;	
end;
```

---


---

## 腳本檔案: 指標/主圖指標/開盤第N根的每日高低價線.xs

```xs
{@type:indicator}
Input:Length(1,"第N根K棒");

Var:_MH(0), _ML(0), _HHMMSS(0), _ChageDNum(0), _MaxCDN(0);

if barfreq <> "Min" then raiseRunTimeError("僅支援分鐘頻率");
if Length = 0 then raiseRunTimeError("參數請設定大於0的合理數值");
if gettotalBar = currentBar and Length - 1 > _MaxCDN then raiseRunTimeError("參數設定超過每日分鐘K棒數");

if getfieldDate("date") <> getfieldDate("date")[1] then 
	_ChageDNum = 0
else begin
	_ChageDNum += 1;
end;

if _ChageDNum > _MaxCDN then _MaxCDN = _ChageDNum;

if _ChageDNum < Length - 1  then begin
	NoPlot(1);
	NoPlot(2);
	NoPlot(3);
end else if _ChageDNum = Length - 1  then begin
	_MH = GetField("最高價", "D");
	_ML = GetField("最低價", "D");
	_HHMMSS = time;
	plot1(_HHMMSS,"時間");
	plot2(_MH,"最高價");
	plot3(_ML,"最低價");
end else begin
	plot1(_HHMMSS,"時間");
	plot2(_MH,"最高價");
	plot3(_ML,"最低價");
end;

setplotLabel(1,Text("第",NumToStr(Length, 0),"根時間"));
```

---


---

## 腳本檔案: 指標/即時籌碼/分時大戶買賣力(金額).xs

```xs
{@type:indicator}
{指標數值定義："大戶單=特大單+大單資料為分鐘統計金額"
支援商品：台(股票)}

if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
	
value91 = GetField("賣出特大單金額");

value1 = GetField("賣出特大單金額") + GetField("賣出大單金額");
value2 = GetField("買進特大單金額") + GetField("買進大單金額");
value3 = value2 - value1;
plot1(value3,"大戶買賣力(金額)");
plot2(value2,"大戶外盤量(金額)",checkbox:=0);
plot3(value1,"大戶內盤量(金額)",checkbox:=0);
```

---


---

## 腳本檔案: 指標/即時籌碼/分時大戶買賣力.xs

```xs
{@type:indicator}
{指標數值定義："大戶單=特大單+大單資料為分鐘統計張數"

支援商品：台(股票)}

if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");

value1 = GetField("賣出特大單量") + GetField("賣出大單量");
value2 = GetField("買進特大單量") + GetField("買進大單量");
value3 = value2 - value1;
plot1(value3,"大戶買賣力");
plot2(value2,"大戶外盤量",checkbox:=0);
plot3(value1,"大戶內盤量",checkbox:=0);
```

---


---

## 腳本檔案: 指標/即時籌碼/分時散戶買賣力(金額).xs

```xs
{@type:indicator}
{指標數值定義："散戶單=小單資料為分鐘統計金額"
支援商品：台(股票)}

if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
	
value91 = GetField("賣出小單金額");

value1 = GetField("賣出小單金額");
value2 = GetField("買進小單金額");
value3 = value2 - value1;
plot1(value3,"散戶買賣力(金額)");
plot2(value2,"散戶外盤量(金額)",checkbox:=0);
plot3(value1,"散戶內盤量(金額)",checkbox:=0);
```

---


---

## 腳本檔案: 指標/即時籌碼/分時散戶買賣力.xs

```xs
{@type:indicator}
{指標數值定義："散戶單=小單資料為分鐘統計張數"
支援商品：台(股票)}

if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
	
value91 = GetField("賣出小單量");

value1 = GetField("賣出小單量");
value2 = GetField("買進小單量");
value3 = value2 - value1;
plot1(value3,"散戶買賣力"); 
plot2(value2,"散戶外盤量",checkbox:=0); 
plot3(value1,"散戶內盤量",checkbox:=0);
```

---


---

## 腳本檔案: 指標/即時籌碼/分時漲跌成交量.xs

```xs
{@type:indicator}
{支援商品類型：台股/期權/選擇權/大盤/類股指數}

if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");

value1 = GetField("上漲量");
value2 = GetField("下跌量");
value3 = value1 - value2;
plot1(value3,"漲跌成交(分時)");
plot2(value1,"上漲量",checkbox:=0);
plot3(value2,"下跌量",checkbox:=0);
```

---


---

## 腳本檔案: 指標/即時籌碼/分時買賣力.xs

```xs
{@type:indicator}
{支援商品：指數/台股/期貨/選擇權}

if symbolexchange <> "TW" and symbolexchange <> "TF" then raiseruntimeerror("不支援此商品");
if SymbolType <> 1 and SymbolType <> 2 and SymbolType <> 3 and SymbolType <> 5 then raiseruntimeerror("不支援此商品");

if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");

value1 = GetField("外盤量");
value2 = GetField("內盤量");
value3 = value1 - value2;
plot1(value3,"買賣力");
plot2(value1,"外盤量",checkbox:=0);
plot3(value2,"內盤量",checkbox:=0);
```

---


---

## 腳本檔案: 指標/即時籌碼/大戶散戶籌碼流向(金額).xs

```xs
{@type:indicator}
{指標數值定義："大戶=特大單+大單, 散戶=小單 
資料為大戶/散戶從開盤累計到現在的(外盤-內盤)金額"

支援商品：台(股票)}

if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
	
value91 = GetField("賣出特大單金額");

value1 = GetField("賣出特大單金額","D") + GetField("賣出大單金額","D");
value2 = GetField("買進特大單金額","D") + GetField("買進大單金額","D");
value3 = value2 - value1;
value11 = GetField("賣出小單金額","D");
value21 = GetField("買進小單金額","D");
value31 = value21 - value11;
plot1(value3,"大戶買賣力(金額)");
plot2(value31,"散戶買賣力(金額)");
```

---


---

## 腳本檔案: 指標/即時籌碼/大戶散戶籌碼流向.xs

```xs
{@type:indicator}
{指標數值定義："大戶=特大單+大單, 散戶=小單 
資料為大戶/散戶從開盤累計到現在的(外盤-內盤)張數"

支援商品：台(股票)}

if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
	
value91 = GetField("賣出特大單量");

value1 = GetField("賣出特大單量","D") + GetField("賣出大單量","D");
value2 = GetField("買進特大單量","D") + GetField("買進大單量","D");
value3 = value2 - value1;
value11 = GetField("賣出小單量","D");
value21 = GetField("買進小單量","D");
value31 = value21 - value11;
plot1(value3,"大戶買賣力");
plot2(value31,"散戶買賣力");
```

---


---

## 腳本檔案: 指標/即時籌碼/大戶買賣力(金額).xs

```xs
{@type:indicator}
{大戶買賣力(金額)是特大單金額+大單金額，資料為開盤迄今的累計
支援商品：台(股票)}

if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
	
value91 = GetField("賣出特大單金額");
	
value1 = GetField("賣出特大單金額","D") + GetField("賣出大單金額","D");
value2 = GetField("買進特大單金額","D") + GetField("買進大單金額","D");
value3 = value2 - value1;
plot1(value3,"大戶買賣力(金額)");
plot2(value2,"大戶外盤金額",checkbox:=0);
plot3(value1,"大戶內盤金額",checkbox:=0);
```

---


---

## 腳本檔案: 指標/即時籌碼/大戶買賣力.xs

```xs
{@type:indicator}
{"大戶=特大單+大單，資料為開盤迄今的累計張數"
支援商品：台(股票)}

if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
	
value91 = GetField("賣出特大單量");

value1 = GetField("賣出特大單量","D") + GetField("賣出大單量","D");
value2 = GetField("買進特大單量","D") + GetField("買進大單量","D");
value3 = value2 - value1;
plot1(value3,"大戶買賣力");
plot2(value2,"大戶外盤量",checkbox:=0);
plot3(value1,"大戶內盤量",checkbox:=0);
```

---


---

## 腳本檔案: 指標/即時籌碼/散戶買賣力(金額).xs

```xs
{@type:indicator}
{散戶買賣力(金額)是小單金額，資料為開盤迄今的累計
支援商品：台(股票)}

if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");

value91 = GetField("賣出小單金額");

value1 = GetField("賣出小單金額","D");
value2 = GetField("買進小單金額","D");
value3 = value2 - value1;
plot1(value3,"散戶買賣力(金額)"); //bar，axis2
plot2(value2,"散戶外盤金額",checkbox:=0); //line，axis11
plot3(value1,"散戶內盤金額",checkbox:=0); //line，axis11
```

---


---

## 腳本檔案: 指標/即時籌碼/散戶買賣力.xs

```xs
{@type:indicator}
{指標數值定義："散戶單=小單資料為開盤迄今的累計張數"

支援商品：台(股票)}

if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");

value91 = GetField("賣出小單量");

value1 = GetField("賣出小單量","D");
value2 = GetField("買進小單量","D");
value3 = value2 - value1;
plot1(value3,"散戶買賣力"); //bar，axis2
plot2(value2,"散戶外盤量",checkbox:=0); //line，axis11
plot3(value1,"散戶內盤量",checkbox:=0); //line，axis11
```

---


---

## 腳本檔案: 指標/即時籌碼/流動大戶買賣力.xs

```xs
{@type:indicator}
{近15分鐘累計的(買進大單量+買進特大單量)-(賣出大單量+賣出特大單量)
抓近15分鐘的目的是希望可以看到最近的買賣力。}
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
value3 = value1 - value2;
plot1(value3,"流動大戶買賣力");
```

---


---

## 腳本檔案: 指標/即時籌碼/漲跌成交量.xs

```xs
{@type:indicator}
{指標數值定義：(上漲)量 = 開盤累計到目前比前一價(上漲)的成交量的加總

支援商品：台股,大盤,類股,期貨,選擇權}

if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
	
value91 = GetField("上漲量");

value1 = GetField("上漲量","D");
value2 = GetField("下跌量","D");
value3 = value1 - value2;
plot1(value3,"漲跌成交");
plot2(value1,"上漲量",checkbox:=0);
plot3(value2,"下跌量",checkbox:=0);
```

---


---

## 腳本檔案: 指標/即時籌碼/自訂大戶買賣力.xs

```xs
{@type:indicator}
{指標數值定義：主力 = 成交單量 >= X的委託由Tick資料去累積計算
支援商品：台(股票)、台(期貨)}

value91 = GetField("上漲量");

if symbolexchange <> "TW" and symbolexchange <> "TF" then raiseruntimeerror("不支援此商品");
if SymbolType <> 2 and SymbolType <> 3 then raiseruntimeerror("不支援此商品");

if barfreq <> "Min" then 
	raiseruntimeerror("僅支援分鐘頻率");

{
	顯示開盤迄今的累計外盤大單 - 累計內盤大單, 也就是盤中大戶的買賣力趨勢
	大單定義: 成交單量 > X
}

input: threshold(100, "大單門檻(張or口)");

var: intrabarpersist _v_buy_acc(0), intrabarpersist _v_sell_acc(0);
var: intrabarpersist _last_seq(0);
var: _cur_seq(0), _i(0), _curbar_date(0); 
var: _last_date(0);

if getfielddate("date") <> _last_date then begin
	_last_date = getfielddate("date");
	_v_buy_acc = 0;
	_v_sell_acc = 0;
	_last_seq = 0;
end;

// 抓洗價當時最新一筆Tick的位置跟日期
//
_cur_seq = GetField("SeqNo", "Tick");
_curbar_date = GetField("Date", "Tick");

if symbolexchange = "TW" and SymbolType = 2 then begin	//台(股票)
	if _curbar_date <> date then begin
		// 如果開盤到有某些分鐘沒有成交, 此時會對到昨日之前的Tick => 這些分鐘不要計算
		//
		_cur_seq = 0;

	end else if _cur_seq > 0 and _cur_seq > _last_seq then begin
		// _last_seq是上一次畫圖時最後一筆Tick的位置
		//
		// 所以就統計 _cur_seq .. _last_seq之間的Tick的成交資料
		//
		_i = _last_seq + 1;	
		while _i <= _cur_seq begin
			var: tv(0), _first(0), _complete(0);
		
			value1 = GetField("BidAskFlag", "Tick")[_cur_seq - _i];	// 外盤=1, 內盤=-1
			value2 = GetField("Close", "Tick")[_cur_seq - _i];		// 價格
			value3 = GetField("Volume", "Tick")[_cur_seq - _i];		// 單量
			value4 = GetField("SeqNo", "Tick")[_cur_seq - _i];		// Tick編號
			//-------------------------------------------------
			// multitick的處理
			//
			// TickGroup回傳以下數值
			//  -1 = 集合競價(每天第一盤, 最後一盤, 包含暫緩之後的搓合, etc.) 
			//	0 = 逐筆搓合單筆
			//	1 = 逐筆搓合開始
			//  2 = 逐筆搓合中間
			//  3 = 逐筆搓合結束
			//
			value5 = GetField("TickGroup", "Tick")[_cur_seq - _i];

			tv = value3;
			_complete = 0;

			if value5 = -1 then begin
				// 集合競價: 不列入統計
				_i = _i + 1;
				tv = 0;
			end else if value5 = 0 then begin
				// 獨立一筆: 列入統計
				_i = _i + 1;
			end else if value5 = 1 then begin
				// 把連續撮合的所有資料合併成一筆統計
				// 連續撮合的第一筆 = 1, 中間 = 2, 最後 = 3
				_first = _i;
				_i = _i + 1;
				while _i <= _cur_seq and _complete = 0 begin
					value99 = GetField("Time", "Tick")[_cur_seq - _i];			// 價格
					value22 = GetField("Close", "Tick")[_cur_seq - _i];			// 價格
					value33 = GetField("Volume", "Tick")[_cur_seq - _i];		// 單量
					value44 = GetField("SeqNo", "Tick")[_cur_seq - _i];			// Seq
					value55 = GetField("TickGroup", "Tick")[_cur_seq - _i];
					tv = tv + value33;
					
					_i = _i + 1;
					if value55 = 3 then _complete = 1;
				end;

				if _complete = 0 then begin
					// 有可能交易所還沒有傳送完整的連續撮合Ticks, 所以等下一次洗價時再處理
					//
					_cur_seq = _first;
					break;
				end;
			end else begin	
				// 異常狀況: 跳過
				_i = _i + 1;
			end;	

			
			// 如果超過門檻, 則依照外盤/內盤分別累計(成交量)
			//
			if tv > threshold then begin
				if value1 = 1 then _v_buy_acc = _v_buy_acc + tv;
				if value1 = -1 then _v_sell_acc = _v_sell_acc + tv;
			end;	
		end;
	end;
end;

if symbolexchange = "TF" and SymbolType = 3 then begin	//台(期貨)
	if _curbar_date <> date then begin
		// 如果開盤到有某些分鐘沒有成交, 此時會對到昨日之前的Tick => 這些分鐘不要計算
		//
		_cur_seq = 0;

	end else if _cur_seq > 0 and _cur_seq > _last_seq then begin
		// _last_seq是上一次畫圖時最後一筆Tick的位置
		//
		// 所以就統計 _cur_seq .. _last_seq之間的Tick的成交資料
		//
		_i = _last_seq + 1;	
		while _i <= _cur_seq begin
			value1 = GetField("BidAskFlag", "Tick")[_cur_seq - _i];	// 外盤=1, 內盤=-1
			value2 = GetField("Close", "Tick")[_cur_seq - _i];		// 價格
			value3 = GetField("Volume", "Tick")[_cur_seq - _i];		// 單量
			value4 = GetField("SeqNo", "Tick")[_cur_seq - _i];		// Tick編號
			
			// 如果超過門檻, 則依照外盤/內盤分別累計(成交量)
			//
			if value3 >= threshold then begin
				if value1 = 1 then _v_buy_acc = _v_buy_acc + value3;
				if value1 = -1 then _v_sell_acc = _v_sell_acc + value3;
			end;	
			_i = _i + 1;
		end;
	end;
end;

_last_seq = _cur_seq;

plot1(_v_buy_acc - _v_sell_acc, "大戶買賣力(自訂)");
plot2(_v_buy_acc, "大戶(自訂)外盤量",checkbox:=0);
plot3(_v_sell_acc, "大戶(自訂)內盤量",checkbox:=0);
```

---


---

## 腳本檔案: 指標/即時籌碼/自訂散戶買賣力.xs

```xs
{@type:indicator}
{指標數值定義：散戶 = 成交單量 < X的委託由Tick資料去累計計算
支援商品：台(股票)、台(期貨)}

if symbolexchange <> "TW" and symbolexchange <> "TF" then raiseruntimeerror("不支援此商品");
if SymbolType <> 2 and SymbolType <> 3 then raiseruntimeerror("不支援此商品");

if barfreq <> "Min" then 
	raiseruntimeerror("僅支援分鐘頻率");
	
value91 = GetField("上漲量");

{
	顯示開盤迄今的累計外盤小單 - 累計內盤小單, 也就是盤中散戶的買賣力趨勢
	小單定義: 成交單量 <= X
}

input: threshold(30, "小單門檻(張or口)");

var: intrabarpersist _v_buy_acc(0), intrabarpersist _v_sell_acc(0);
var: intrabarpersist _last_seq(0);
var: _cur_seq(0), _i(0), _curbar_date(0); 
var: _last_date(0);

if getfielddate("date") <> _last_date then begin
	_last_date = getfielddate("date");
	_v_buy_acc = 0;
	_v_sell_acc = 0;
	_last_seq = 0;
end;

// 抓洗價當時最新一筆Tick的位置跟日期
//
_cur_seq = GetField("SeqNo", "Tick");
_curbar_date = GetField("Date", "Tick");

if symbolexchange = "TW" and SymbolType = 2 then begin	//台(股票)
	if _curbar_date <> date then begin
		// 如果開盤到有某些分鐘沒有成交, 此時會對到昨日之前的Tick => 這些分鐘不要計算
		//
		_cur_seq = 0;

	end else if _cur_seq > 0 and _cur_seq > _last_seq then begin
		// _last_seq是上一次畫圖時最後一筆Tick的位置
		//
		// 所以就統計 _cur_seq .. _last_seq之間的Tick的成交資料
		//
		_i = _last_seq + 1;	
		while _i <= _cur_seq begin
			var: tv(0), _first(0), _complete(0);
		
			value1 = GetField("BidAskFlag", "Tick")[_cur_seq - _i];	// 外盤=1, 內盤=-1
			value2 = GetField("Close", "Tick")[_cur_seq - _i];		// 價格
			value3 = GetField("Volume", "Tick")[_cur_seq - _i];		// 單量
			value4 = GetField("SeqNo", "Tick")[_cur_seq - _i];		// Tick編號
			//-------------------------------------------------
			// multitick的處理
			//
			// TickGroup回傳以下數值
			//  -1 = 集合競價(每天第一盤, 最後一盤, 包含暫緩之後的搓合, etc.) 
			//	0 = 逐筆搓合單筆
			//	1 = 逐筆搓合開始
			//  2 = 逐筆搓合中間
			//  3 = 逐筆搓合結束
			//
			value5 = GetField("TickGroup", "Tick")[_cur_seq - _i];

			tv = value3;
			_complete = 0;

			if value5 = -1 then begin
				// 集合競價: 不列入統計
				_i = _i + 1;
				tv = 0;
			end else if value5 = 0 then begin
				// 獨立一筆: 列入統計
				_i = _i + 1;
			end else if value5 = 1 then begin
				// 把連續撮合的所有資料合併成一筆統計
				// 連續撮合的第一筆 = 1, 中間 = 2, 最後 = 3
				_first = _i;
				_i = _i + 1;
				while _i <= _cur_seq and _complete = 0 begin
					value99 = GetField("Time", "Tick")[_cur_seq - _i];			// 價格
					value22 = GetField("Close", "Tick")[_cur_seq - _i];			// 價格
					value33 = GetField("Volume", "Tick")[_cur_seq - _i];		// 單量
					value44 = GetField("SeqNo", "Tick")[_cur_seq - _i];			// Seq
					value55 = GetField("TickGroup", "Tick")[_cur_seq - _i];
					tv = tv + value33;
					
					_i = _i + 1;
					if value55 = 3 then _complete = 1;
				end;

				if _complete = 0 then begin
					// 有可能交易所還沒有傳送完整的連續撮合Ticks, 所以等下一次洗價時再處理
					//
					_cur_seq = _first;
					break;
				end;
			end else begin	
				// 異常狀況: 跳過
				_i = _i + 1;
			end;	
			
			// 如果小於門檻, 則依照外盤/內盤分別累計(成交量)
			//
			if tv <= threshold then begin
				if value1 = 1 then _v_buy_acc = _v_buy_acc + tv;
				if value1 = -1 then _v_sell_acc = _v_sell_acc + tv;
			end;	
		end;
	end;	
end;

if symbolexchange = "TF" and SymbolType = 3 then begin	//台(期貨)
	if _curbar_date <> date then begin
		// 如果開盤到有某些分鐘沒有成交, 此時會對到昨日之前的Tick => 這些分鐘不要計算
		//
		_cur_seq = 0;

	end else if _cur_seq > 0 and _cur_seq > _last_seq then begin
		// _last_seq是上一次畫圖時最後一筆Tick的位置
		//
		// 所以就統計 _cur_seq .. _last_seq之間的Tick的成交資料
		//
		_i = _last_seq + 1;	
		while _i <= _cur_seq begin
			value1 = GetField("BidAskFlag", "Tick")[_cur_seq - _i];	// 外盤=1, 內盤=-1
			value2 = GetField("Close", "Tick")[_cur_seq - _i];		// 價格
			value3 = GetField("Volume", "Tick")[_cur_seq - _i];		// 單量
			value4 = GetField("SeqNo", "Tick")[_cur_seq - _i];		// Tick編號
			
			// 如果超過門檻, 則依照外盤/內盤分別累計(成交量)
			//
			if value3 < threshold then begin
				if value1 = 1 then _v_buy_acc = _v_buy_acc + value3;
				if value1 = -1 then _v_sell_acc = _v_sell_acc + value3;
			end;	
			
			_i = _i + 1;
		end;
	end;
end;

_last_seq = _cur_seq;

plot1(_v_buy_acc - _v_sell_acc, "散戶買賣力(自訂)");
plot2(_v_buy_acc, "大戶(自訂)外盤量",checkbox:=0);
plot3(_v_sell_acc, "大戶(自訂)內盤量",checkbox:=0);
```

---


---

## 腳本檔案: 指標/即時籌碼/買賣力.xs

```xs
{@type:indicator}
{指標數值定義：(外盤)量 = 開盤累計到目前的(外盤)成交量

支援商品：台股/期貨/選擇權}

value91 = GetField("外盤量");

value1 = GetField("外盤量","D");
value2 = GetField("內盤量","D");
value3 = value1 - value2;
plot1(value3,"買賣力");
plot2(value1,"外盤量",checkbox:=0);
plot3(value2,"內盤量",checkbox:=0);
```

---


---

## 腳本檔案: 指標/大盤指標/ALF亞歷山大過濾指標.xs

```xs
{@type:indicator}
input: length(10);		setinputname(1, "天期");

Value1 = close / close[length-1];
plot1(Value1, "亞歷山大過濾指標");
```

---


---

## 腳本檔案: 指標/大盤指標/BBand寬度指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/bband-width/
}

input: 
	Length(20, "MA的天數"), 
	UpperBand(2, "上通道標準差倍數"), 
	LowerBand(2, "下通道標準差倍數");
variable: mid(0), up(0), down(0), bbandwidth(0) ;

up = bollingerband(Close, Length, UpperBand);
down = bollingerband(Close, Length, -1 * LowerBand);
mid = (up + down) / 2;

bbandwidth = 100 * (up - down) / mid;
 
Plot1(bbandwidth , "BBand width(%)");
plot2(4,"低檔");
```

---


---

## 腳本檔案: 指標/大盤指標/ETF成交量統計指標.xs

```xs
{@type:indicator}
array:ETF[50](0);
etf[1]=GetSymbolField("0050.tw","成交金額");
etf[2]=GetSymbolField("0051.tw","成交金額");
etf[3]=GetSymbolField("0052.tw","成交金額");
etf[4]=GetSymbolField("0053.tw","成交金額");
etf[5]=GetSymbolField("0054.tw","成交金額");
etf[6]=GetSymbolField("0055.tw","成交金額");
etf[7]=GetSymbolField("0056.tw","成交金額");
etf[8]=GetSymbolField("0057.tw","成交金額");
etf[9]=GetSymbolField("0058.tw","成交金額");
etf[10]=GetSymbolField("0059.tw","成交金額");
etf[11]=GetSymbolField("0061.tw","成交金額");
etf[12]=GetSymbolField("006201.tw","成交金額");
etf[13]=GetSymbolField("006203.tw","成交金額");
etf[14]=GetSymbolField("006204.tw","成交金額");
etf[15]=GetSymbolField("006205.tw","成交金額");
etf[16]=GetSymbolField("006206.tw","成交金額");
etf[17]=GetSymbolField("006207.tw","成交金額");
etf[18]=GetSymbolField("006208.tw","成交金額");
etf[19]=GetSymbolField("00631L.tw","成交金額");
etf[20]=GetSymbolField("00632R.tw","成交金額");
etf[21]=GetSymbolField("00633L.tw","成交金額");
etf[22]=GetSymbolField("00634R.tw","成交金額");
etf[23]=GetSymbolField("00635U.tw","成交金額");
etf[24]=GetSymbolField("00636.tw","成交金額");
etf[25]=GetSymbolField("00637L.tw","成交金額");
etf[26]=GetSymbolField("00638R.tw","成交金額");
etf[27]=GetSymbolField("00639.tw","成交金額");
etf[28]=GetSymbolField("00640L.tw","成交金額");
etf[29]=GetSymbolField("00641R.tw","成交金額");
etf[30]=GetSymbolField("00642U.tw","成交金額");
etf[31]=GetSymbolField("00643.tw","成交金額");
etf[32]=GetSymbolField("00645.tw","成交金額");
etf[33]=GetSymbolField("00646.tw","成交金額");
etf[34]=GetSymbolField("00647L.tw","成交金額");
etf[35]=GetSymbolField("00648R.tw","成交金額");
etf[36]=GetSymbolField("00649.tw","成交金額");
etf[37]=GetSymbolField("00650L.tw","成交金額");
etf[38]=GetSymbolField("00651R.tw","成交金額");
etf[39]=GetSymbolField("00652.tw","成交金額");
etf[40]=GetSymbolField("00653L.tw","成交金額");
etf[41]=GetSymbolField("00654R.tw","成交金額");
etf[42]=GetSymbolField("00655L.tw","成交金額");
etf[43]=GetSymbolField("00656R.tw","成交金額");
etf[44]=GetSymbolField("00657.tw","成交金額");
etf[45]=GetSymbolField("00658L.tw","成交金額");
etf[46]=GetSymbolField("00659R.tw","成交金額");
etf[47]=GetSymbolField("00660.tw","成交金額");
etf[48]=GetSymbolField("00661.tw","成交金額");
etf[49]=GetSymbolField("00662.tw","成交金額");
etf[50]=GetSymbolField("008201.tw","成交金額");

value1=array_sum(etf,1,50);

if volume<>0 then 
	value3=value1/volume*100;
plot1(value3);
```

---


---

## 腳本檔案: 指標/大盤指標/KST確認指標.xs

```xs
{@type:indicator}
variable:kst(0);

value1=average(rateofchange(close,12),10);
value2=average(rateofchange(close,20),10);
value3=average(rateofchange(close,30),8);
value4=average(rateofchange(close,40),15);

kst=value1+value2*2+value3*3+value4*4;

plot1(kst,"KST確認指標");
```

---


---

## 腳本檔案: 指標/大盤指標/OTC佔大盤成交量比.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/otc跟上市成交量比值是股市多空指標/
}

input: Period(5,"期數");

value1=GetSymbolField("tse.tw","成交量");
value2=GetSymbolField("otc.tw","成交量");
value3=value2/value1*100;
value4=average(value3,Period);

plot1(value4,"OTC/TSE(%)");
Plot2(value2,"OTC成交量");
```

---


---

## 腳本檔案: 指標/大盤指標/Q指標.xs

```xs
{@type:indicator}
input:t1(10);	setinputname(1,"天期");
input:t2(5);	setinputname(2,"平均天期");
input:t3(20);	setinputname(3,"雜訊平滑天期");


value1=close-close[1];			//價格變化
value2=summation(value1,t1);	//累積價格變化
value3=average(value2,t2);
value4=absvalue(value2-value3);	//雜訊
value5=average(value4,t3);		//把雜訊移動平均

variable:Qindicator(0);
if value5 = 0 then 
	Qindicator = 0
else
	Qindicator = value3 / value5*5;
	
plot1(Qindicator,"Q-indicator");
```

---


---

## 腳本檔案: 指標/大盤指標/上漲下跌家數差RSI指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/上漲下跌家數差RSI指標/
收錄於「三週學會程式交易：打造你的第一筆自動化交易」 256頁
https://www.ipci.com.tw/books_in.php?book_id=724
}

input:period(10,"RSI計算天數");

if barfreq <> "D" then raiseruntimeerror("不支援此頻率");

value1=getfield("上漲家數");
value2=getfield("下跌家數");
value3=value1-value2;
value4=summation(value3,period);
value5=rsi(value4,period);
plot1(value5,"上漲家數RSI");
```

---


---

## 腳本檔案: 指標/大盤指標/上漲下跌量差.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/進場點一目了然的大盤儀表板/
收錄於「三週學會程式交易：打造你的第一筆自動化交易」 244頁
https://www.ipci.com.tw/books_in.php?book_id=724
}

input:period1(3,"短天期");
input:period2(5,"長天期");

if barfreq = "Tick" or barfreq = "Min" then
begin
	value1=GetField("上漲量");
	value2=getfield("下跌量");
end else begin
	value1=GetField("上漲量","D");
	value2=getfield("下跌量","D");
end;
value3=average(value1,period1);
value4=average(value2,period1);
value5=value3-value4;//上漲量與下跌量比例
value6=average(value5,period2);
 
plot1(value6,"上漲下跌量差");
```

---


---

## 腳本檔案: 指標/大盤指標/上漲佔比.xs

```xs
{@type:indicator}
value1=GetField("上漲家數");
value2=GetField("下跌家數");
value3=value1+value2;
if value3 = 0 then value4 = 0 else value4=value1/value3*100;

plot1(value4,"上漲佔比");
```

---


---

## 腳本檔案: 指標/大盤指標/上漲家數.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/大盤多空轉換點之探討系列一-上漲的股票有沒有200/
收錄於「三週學會程式交易：打造你的第一筆自動化交易」 252頁
https://www.ipci.com.tw/books_in.php?book_id=724
}

input:shortterm(5,"期間");
input:midterm(15,"平均");

value1=GetField("上漲家數");
value2=lowest(value1,shortterm);
value3=average(value2,midterm);
plot1(value3,"平均上漲家數");
plot2(200,"多");
plot3(100,"空");
```

---


---

## 腳本檔案: 指標/大盤指標/上漲家數佔比指標.xs

```xs
{@type:indicator}
input:period1(5,"短天期");
input:period2(20,"長天期");
value1=GetField("上漲家數");
value2=GetField("下跌家數");
value3=value1+value2;
if value3 = 0 then 
	value4 = 0 
else
	value4=value1/value3*100;
value5=average(value4,period1);
value6=average(value4,period2);

plot1(value5,"上漲佔比短期平均");
plot2(value6,"上漲佔比長期平均");
plot3(value5-value6,"長短天期差");
```

---


---

## 腳本檔案: 指標/大盤指標/上漲量比重.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/盤上成交是否真的是重要指標/
}

if barfreq = "Tick" or barfreq = "Min" then 
begin
	value1=GetField("上漲量");
end else begin
	value1=GetField("上漲量","D");
end;

if volume<>0 then
	value2=value1/volume;
plot1(average(value2,5),"上漲量比重");
```

---


---

## 腳本檔案: 指標/大盤指標/主力買賣超佔市場成交量比.xs

```xs
{@type:indicator}
{市場成交量定義

加權成交量 GetSymbolField("TSE.TW", "成交量"):
https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html
總計(1~15)欄位的成交金額(元)

上櫃成交量 GetSymbolField("OTC.TW", "成交量"):
https://www.tpex.org.tw/web/stock/aftertrading/market_statistics/statistics.php?l=zh-tw
股票合計(1~3)欄位的成交金額(元)
}

if barfreq = "Tick" or barfreq = "Min" then raiseruntimeerror("只支援日線以上");

value1 = GetSymbolField("TSE.TW", "主力買進金額") - GetSymbolField("TSE.TW", "主力賣出金額") 
		+ GetSymbolField("OTC.TW", "主力買進金額") - GetSymbolField("TSE.TW", "主力賣出金額");
value2 = GetSymbolField("TSE.TW", "成交量") + GetSymbolField("OTC.TW", "成交量");
if value2 = 0 then value3 = 0 else value3 = value1/value2*100;

plot1(value3,"佔比(%)");
```

---


---

## 腳本檔案: 指標/大盤指標/估波指標(Coppock Indicator).xs

```xs
{@type:indicator}
{ 一般適用於大盤月線資料 }

input:length1(14);		setinputname(1, "天期一");
input:length2(11);		setinputname(2, "天期二");
input:length3(10);   	setinputname(3, "平均天期");

variable:coppock(0); 
Value1=rateofchange(close,length1);   
Value2=rateofchange(close,length2);   
coppock=xaverage(Value1+Value2,length3);   

plot1(coppock,"Coppock Indicator");
```

---


---

## 腳本檔案: 指標/大盤指標/作多意願指標.xs

```xs
{@type:indicator}
input:length1(20,"長天期"),length2(9,"短天期");

variable:count1(0),x1(0);

count1=0;
for x1=1 to length2-1 begin
	if high < close*1.01 then 
		count1=count1+1;
	if open > close[1]*1.005 then
		count1=count1+1;
	if close > close[1] and volume>volume[1] then
		count1=count1+1;
	if GetField("外盤量") > GetField("內盤量") then
		count1=count1+1;
end;


value2=average(count1,length1);
value3=average(count1,length2);

plot1(value2,"長期意願");
plot2(value3,"短期意願");
```

---


---

## 腳本檔案: 指標/大盤指標/內外盤量差.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/內外盤量比在預測大盤後市上的應用/
收錄於「三週學會程式交易：打造你的第一筆自動化交易」242頁
https://www.ipci.com.tw/books_in.php?book_id=724
}

if barfreq = "Tick" or barfreq = "Min" then 
begin
	value1=GetField("內盤量");//單位:元
	value2=GetField("外盤量");//單位:元
end else begin
	value1=GetField("內盤量","D");//單位:元
	value2=GetField("外盤量","D");//單位:元
end;

if volume <> 0 then begin
	value3=value2/volume*100;//外盤量比
	value4=value1/volume*100;//內盤量比
end else begin
	value3=value3[1];
	value4=value4[1];
end;

value5=average(value3,5);
value6=average(value4,5);
value7=value5-value6+5;
plot1(value7,"內外盤量比差");
```

---


---

## 腳本檔案: 指標/大盤指標/內盤長短期累積量比值差.xs

```xs
{@type:indicator}
input:length1(5,"短天期"),length2(20,"長天期");

variable:ac(0),ds(0),ac1(0),ds1(0);

if barfreq = "Tick" or barfreq = "Min" then 
begin
	value1=GetField("內盤量");//單位:元
	value2=GetField("外盤量");//單位:元
end else begin
	value1=GetField("內盤量","D");//單位:元
	value2=GetField("外盤量","D");//單位:元
end;
value3=summation(value1,length1);
value4=summation(value2,length1);
value5=summation(value1,length2);
value6=summation(value2,length2);
value7=summation(volume,length1);
value8=summation(volume,length2);

ac=value4/value7*100;//外盤短期積量比值
ds=value3/value7*100;//內盤短期積量比值
ac1=value6/value8*100;//外盤長期積量比值
ds1=value5/value8*100;//內盤長期積量比值

value11=ds1-ds;
plot1(value11,"內盤長短期積量比值差");
```

---


---

## 腳本檔案: 指標/大盤指標/反脆弱指標.xs

```xs
{@type:indicator}
array:ValueArray[21](0);
valuearray[1]=GetSymbolField("1477.tw","總市值");
valuearray[2]=GetSymbolField("1536.tw","總市值");
valuearray[3]=GetSymbolField("1702.tw","總市值");
valuearray[4]=GetSymbolField("2231.tw","總市值");
valuearray[5]=GetSymbolField("2207.tw","總市值");
valuearray[6]=GetSymbolField("2355.tw","總市值");
valuearray[7]=GetSymbolField("2377.tw","總市值");
valuearray[8]=GetSymbolField("2379.tw","總市值");
valuearray[9]=GetSymbolField("2383.tw","總市值");
valuearray[10]=GetSymbolField("2492.tw","總市值");
valuearray[11]=GetSymbolField("2905.tw","總市值");
valuearray[12]=GetSymbolField("3023.tw","總市值");
valuearray[13]=GetSymbolField("3552.tw","總市值");
valuearray[14]=GetSymbolField("4938.tw","總市值");
valuearray[15]=GetSymbolField("4958.tw","總市值");
valuearray[16]=GetSymbolField("5347.tw","總市值");
valuearray[17]=GetSymbolField("5871.tw","總市值");
valuearray[18]=GetSymbolField("5904.tw","總市值");
valuearray[19]=GetSymbolField("8016.tw","總市值");
valuearray[20]=GetSymbolField("9910.tw","總市值");
valuearray[21]=GetSymbolField("9938.tw","總市值");
value1=array_sum(valuearray,1,21);
plot1(value1);
```

---


---

## 腳本檔案: 指標/大盤指標/台指選倉P／C.xs

```xs
{@type:indicator}
value1=getsymbolfield("txo00.tf","買賣權未平倉量比率");
plot1(value1,"台指選倉P／C");
```

---


---

## 腳本檔案: 指標/大盤指標/噪音指標.xs

```xs
{@type:indicator}

input:n1(5); setinputname(1,"計算天期");  
input:n2(5); setinputname(2,"移動平均天期");
  
value1=absvalue(close-close[n1-1]);  
value2=summation(range,n1);  
if value1 <> 0 then  
begin
	value3 = value2 / value1;  
	value4 = average(value3,n2);  
end;
  
plot1(value4,"噪音指標");
```

---


---

## 腳本檔案: 指標/大盤指標/外資買賣超佔市場成交量比.xs

```xs
{@type:indicator}
{市場成交量定義

加權成交量 GetSymbolField("TSE.TW", "成交量"):
https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html
總計(1~15)欄位的成交金額(元)

上櫃成交量 GetSymbolField("OTC.TW", "成交量"):
https://www.tpex.org.tw/web/stock/aftertrading/market_statistics/statistics.php?l=zh-tw
股票合計(1~3)欄位的成交金額(元)
}

if barfreq = "Tick" or barfreq = "Min" then raiseruntimeerror("只支援日線以上");

value1 = GetSymbolField("TSE.TW", "外資買賣超金額") + GetSymbolField("OTC.TW", "外資買賣超金額");
value2 = GetSymbolField("TSE.TW", "成交量") + GetSymbolField("OTC.TW", "成交量");
if value2 = 0 then value3 = 0 else value3 = value1/value2*100;

plot1(value3,"佔比(%)");
```

---


---

## 腳本檔案: 指標/大盤指標/多空點數指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/多空點數指標/
}

variable:i(0),Lscore(0),Sscore(0);

Lscore=0;
Sscore=0;

for i = 1 to 100 begin
	if C> H[i] then 
		Lscore += 1 
	else if C < L[i] then 
		Sscore += 1;
end;
PLOT1(LSCORE-SSCORE,"多空點數");
```

---


---

## 腳本檔案: 指標/大盤指標/大盤儀表板.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/進場點一目了然的大盤儀表板/
收錄於「三週學會程式交易：打造你的第一筆自動化交易」 260頁
https://www.ipci.com.tw/books_in.php?book_id=724
}

if barfreq <> "D" then raiseruntimeerror("不支援此頻率");

condition1=false;
condition2=false;
condition3=false;
condition4=false;
condition5=false;

//==========OTC 佔大盤成交量比================
value1=GetSymbolField("tse.tw","成交量");
value2=GetSymbolField("otc.tw","成交量");
value3=value2/value1*100;
value4=average(value3,5);
value5=low*0.98;
if value4 crosses over 20 then
	condition1=true;
if condition1 then
	plot1(value5,"OTC 進場訊號");

//============內外盤量比差====================
value6=GetField("內盤量");//單位:元
value7=GetField("外盤量");//單位:元
value8=value7/volume*100;//外盤量比
value9=value6/volume*100;//內盤量比
value10=average(value8,5);
value11=average(value9,5);
value7=value10-value11+5;
if value7 crosses over 0 then 
	condition2=true;
if condition2 then 
	plot2(value5*0.98,"內外盤量比差");

//===========上漲下跌家數 RSI 指標==============
input: _TEXT1("===============","上漲下跌家數RSI指標參數");
input:period(10,"RSI計算天數");
value12=GetField("上漲家數");
value13=GetField("下跌家數");
value14=value12-value13;
value15=summation(value14,period);
value16=rsi(value15,period);
if value16 crosses over 50 then
	condition3=true;
if condition3 then
	plot3(value5*0.97,"上漲下跌家數 RSI");

//===========上漲家數突破 200 檔================
value17=lowest(value12,5);
value18=average(value17,15);
if value18 crosses over 200 then
	condition4=true;
if condition4=true then
	plot4(value5*0.96,"上漲家數突破 200 家");

//==========上漲下跌量指標=====================
input: _TEXT2("===============","上漲下跌量指標參數");
input:p1(3,"上漲下跌量平均天數");
value19=GetField("上漲量");
value20=GetField("下跌量");
value21=average(value19,period);
value22=average(value20,period);
value23=value21-value22;
value24=average(value23,5);
if value24 crosses over 0 then
	condition5=true;
if condition5=true then
	plot5(value5*0.95,"上漲量突破下跌量");
```

---


---

## 腳本檔案: 指標/大盤指標/大盤六度空間切割法.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/多空六大階段指標/
收錄於「三週學會程式交易：打造你的第一筆自動化交易」 259頁
https://www.ipci.com.tw/books_in.php?book_id=724
}

var:m50(0),m200(0);
m50=average(close,50);
m200=average(close,200);
if close > m50 and c< m200 and m50<m200
then value1=10
else value1=0;
if close > m50 and c> m200 and m50<m200
then value2=20
else value2=0;
if close > m50 and c> m200 and m50 > m200
then value3=30
else value3=0;
if close < m50 and c>m200 and m50>m200
then value4=-10
else value4=0;
if close < m50 and c <m200
then value5=-20
else value5=0;
if close < m50 and c <m200 then value6=-30
else value6=0;
plot1(value1,"復甦期");
plot2(value2,"收集期");
plot3(value3,"多頭");
plot4(value4,"警示期");
plot5(value5,"發散期");
plot6(value6,"空頭");
```

---


---

## 腳本檔案: 指標/大盤指標/大盤多空對策判斷分數.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/大盤多空對策訊號/
收錄於「三週學會程式交易：打造你的第一筆自動化交易」 265頁
https://www.ipci.com.tw/books_in.php?book_id=724
}

if barfreq <> "D" then raiseruntimeerror("僅支援日頻率");

variable: XData(0),YData(0),ZData(0),Z(0),count(0);

//透過Z的時間安排來決定現在用的是那一根Bar的資料 
if currenttime > 180000 
or currenttime < 083000 then 
	Z =0 
else 
	Z=1;

//每天的分數都先歸零
if date <> date[1] then 
	count=0;

//外資買超
XData = GetField("外資買賣超金額")[Z];
if xdata > 0 then 
	count=count+1;

//投信買超
YData = GetField("投信買賣超金額")[Z];
if ydata > 0 then
	count=count+1;

//自營商買超
ZData = GetField("自營商買賣超金額")[Z];
if zdata > 0 then 
	count=count+1;

//上漲量超過一半
value6 = GetField("上漲量");
if value6/volume > 0.5 then
	count=count+1;

//外盤量超過一半
value7 = GetField("外盤量");
if value7/volume>0.5 then
	count=count+1;

//RSI多頭
value8=rsi(close,5);
value9=rsi(close,10);
if value8 > value9 and value8 < 90 then
	count=count+1;

//MACD 多頭
variable:Dif_val(0), MACD_val(0), Osc_val(0);
MACD(Close, 12, 26, 9, Dif_val, MACD_val, Osc_val);
if osc_val > 0 then
	count=count+1;

//MTM  多頭
value10=mtm(10);
if value10 > 0 then
	count=count+1;

//KD多頭
variable:rsv1(0),k1(0),d1(0);
stochastic(9,3,3,rsv1,k1,d1);
if k1 > d1 and k1 < 80 then
	count=count+1;

//+DI>-DI
variable:pdi_value(0),ndi_value(0),adx_value(0);
DirectionMovement(14,pdi_value,ndi_value,adx_value);
if pdi_value > ndi_value then
	count=count+1;

//AR趨勢向上
value14=ar(26);
value15=linearregslope(value14,5);
if value15 > 0 then 
	count=count+1;

//ACC大於零
value16=acc(10);
if value16 > 0 then 
	count=count+1;

//TRIX多頭
value17=trix(close,9);
value18=trix(close,15);
if value17 > value18 then
	count=count+1;

//SAR多頭
value19=SAR(0.02, 0.02, 0.2);
if close > value19 then
	count=count+1;

//週線大於月線
if average(close,5) > average(close,20) then
	count=count+1;

//計算平均分數
value11=average(count,10);
plot1(value11,"分數");
Plot2(10,"多");
plot3(5,"空");
```

---


---

## 腳本檔案: 指標/大盤指標/大盤多空指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/打造自己的大盤多空函數/
}

input:Length(7,"計算天數");
input:LowLimit(5,"外資買超天數");

plot1(tselsindex(Length,LowLimit));
```

---


---

## 腳本檔案: 指標/大盤指標/委買委賣均張差額.xs

```xs
{@type:indicator}
{
指標說明
收錄於「三週學會程式交易：打造你的第一筆自動化交易」 246頁
https://www.ipci.com.tw/books_in.php?book_id=724
}

input:period(10,"天數");

if barfreq = "Tick" or barfreq = "Min" then begin
	value1=GetField("委買均");
	value2=GetField("委賣均");
end else begin
	value1=GetField("委買均","D");
	value2=GetField("委賣均","D");
end;
	
	
value3=value1-value2;
value4=average(value3,period);
 
plot1(value4,"委買賣均張差額的移動平均");
```

---


---

## 腳本檔案: 指標/大盤指標/實質買賣盤比指標.xs

```xs
{@type:indicator}
input:length(5,"期數");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
value1=GetField("實質買盤比");
value2=GetField("實質賣盤比");
value3=average(value1,length)-80;
plot1(value3,"實質買賣盤比");
```

---


---

## 腳本檔案: 指標/大盤指標/尼古斯指標.xs

```xs
{@type:indicator}
input: length(30);		setinputname(1, "天期");

value1=GetField("上漲家數");
value2=GetField("下跌家數");
value3=average(value1,length);
value4=average(value2,length);
if value4 <> 0 then value5=value3/value4;

plot1(value5, "尼古斯指標");
```

---


---

## 腳本檔案: 指標/大盤指標/投信買賣超佔市場成交量比.xs

```xs
{@type:indicator}
{市場成交量定義

加權成交量 GetSymbolField("TSE.TW", "成交量"):
https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html
總計(1~15)欄位的成交金額(元)

上櫃成交量 GetSymbolField("OTC.TW", "成交量"):
https://www.tpex.org.tw/web/stock/aftertrading/market_statistics/statistics.php?l=zh-tw
股票合計(1~3)欄位的成交金額(元)
}

if barfreq = "Tick" or barfreq = "Min" then raiseruntimeerror("只支援日線以上");

value1 = GetSymbolField("TSE.TW", "投信買賣超金額") + GetSymbolField("OTC.TW", "投信買賣超金額");
value2 = GetSymbolField("TSE.TW", "成交量") + GetSymbolField("OTC.TW", "成交量");
if value2 = 0 then value3 = 0 else value3 = value1/value2*100;

plot1(value3,"佔比(%)");
```

---


---

## 腳本檔案: 指標/大盤指標/本土天王平均.xs

```xs
{@type:indicator}
array:ValueArray[12](0);

valuearray[1]=GetSymbolField("1216.tw","收盤價");
valuearray[2]=GetSymbolField("2201.tw","收盤價");
valuearray[3]=GetSymbolField("2412.tw","收盤價");
valuearray[4]=GetSymbolField("1707.tw","收盤價");
valuearray[5]=GetSymbolField("2207.tw","收盤價");
valuearray[6]=GetSymbolField("2905.tw","收盤價");
valuearray[7]=GetSymbolField("2912.tw","收盤價");
valuearray[8]=GetSymbolField("5530.tw","收盤價");
valuearray[9]=GetSymbolField("8454.tw","收盤價");
valuearray[10]=GetSymbolField("1507.tw","收盤價");
valuearray[11]=GetSymbolField("9933.tw","收盤價");
valuearray[12]=GetSymbolField("9941.tw","收盤價");
value1=array_sum(valuearray,1,12);

plot1(value1);
```

---


---

## 腳本檔案: 指標/大盤指標/法人買賣超佔市場成交量比.xs

```xs
{@type:indicator}
{市場成交量定義

加權成交量 GetSymbolField("TSE.TW", "成交量"):
https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html
總計(1~15)欄位的成交金額(元)

上櫃成交量 GetSymbolField("OTC.TW", "成交量"):
https://www.tpex.org.tw/web/stock/aftertrading/market_statistics/statistics.php?l=zh-tw
股票合計(1~3)欄位的成交金額(元)
}

if barfreq = "Tick" or barfreq = "Min" then raiseruntimeerror("只支援日線以上");

value1 = GetSymbolField("TSE.TW", "法人買賣超金額") + GetSymbolField("OTC.TW", "法人買賣超金額");
value2 = GetSymbolField("TSE.TW", "成交量") + GetSymbolField("OTC.TW", "成交量");
if value2 = 0 then value3 = 0 else value3 = value1/value2*100;

plot1(value3,"佔比(%)");
```

---


---

## 腳本檔案: 指標/大盤指標/法人買進賣出比重指標.xs

```xs
{@type:indicator}
input:period(5,"期數");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
value1=GetField("法人買進比重");
value2=GetField("法人賣出比重");
value3=value1-value2;
value4=average(value3,period);
plot1(value4,"法人買賣比重差額的移動平均");
```

---


---

## 腳本檔案: 指標/大盤指標/漲跌停家數.xs

```xs
{@type:indicator}
value1=GetField("漲停家數");
value2=GetField("跌停家數");
plot1(value1,"漲停家數");
plot2(value2,"跌停家數");
```

---


---

## 腳本檔案: 指標/大盤指標/當日沖銷張數.xs

```xs
{@type:indicator}
input:length(5,"期數");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

value1=GetField("當日沖銷張數");
value2=average(value1,length);
plot1(value2,"當日沖銷張數的移動平均");
```

---


---

## 腳本檔案: 指標/大盤指標/移動平均線再平均指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/移動平均線再平均指標/
收錄於「三週學會程式交易：打造你的第一筆自動化交易」 257頁
https://www.ipci.com.tw/books_in.php?book_id=724
}
input: Period1(5,"一次平均期數");
input: Period2(5,"二次平均期數");
input: Period3(10,"累計期數");

value1=average(close,Period1);
value2=average(value1,Period2);
value3=value1-value2;
value4=summation(value3,Period3);
plot1(value4,"多空");
```

---


---

## 腳本檔案: 指標/大盤指標/自營商買賣超佔市場成交量比.xs

```xs
{@type:indicator}
{市場成交量定義

加權成交量 GetSymbolField("TSE.TW", "成交量"):
https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html
總計(1~15)欄位的成交金額(元)

上櫃成交量 GetSymbolField("OTC.TW", "成交量"):
https://www.tpex.org.tw/web/stock/aftertrading/market_statistics/statistics.php?l=zh-tw
股票合計(1~3)欄位的成交金額(元)
}

if barfreq = "Tick" or barfreq = "Min" then raiseruntimeerror("只支援日線以上");

value1 = GetSymbolField("TSE.TW", "自營商買賣超金額") + GetSymbolField("OTC.TW", "自營商買賣超金額");
value2 = GetSymbolField("TSE.TW", "成交量") + GetSymbolField("OTC.TW", "成交量");
if value2 = 0 then value3 = 0 else value3 = value1/value2*100;

plot1(value3,"佔比(%)");
```

---


---

## 腳本檔案: 指標/大盤指標/軍火商指數.xs

```xs
{@type:indicator}
array:ValueArray[6](0);

valuearray[1]=GetSymbolField("LMT.US","收盤價");
valuearray[2]=GetSymbolField("BA.US","收盤價");
valuearray[3]=GetSymbolField("RTN.US","收盤價");
valuearray[4]=GetSymbolField("GD.US","收盤價");
valuearray[5]=GetSymbolField("NOC.US","收盤價");
valuearray[6]=GetSymbolField("UTX.US","收盤價");

value1=array_sum(valuearray,1,6);

plot1(value1);
```

---


---

## 腳本檔案: 指標/大盤指標/開盤委買委賣差.xs

```xs
{@type:indicator}
{
指標說明
收錄於「三週學會程式交易：打造你的第一筆自動化交易」 245頁
https://www.ipci.com.tw/books_in.php?book_id=724
}

input:length(5,"天期");

value1=GetField("開盤委買", "D");
value2=GetField("開盤委賣", "D");
value3=value1-value2;
value4=average(value3,length);

plot1(value4,"開盤委買賣差之移動平均");
```

---


---

## 腳本檔案: 指標/大盤指標/麥克連震盪指標.xs

```xs
{@type:indicator}
input:length1(19,"短天期"),length2(39,"長天期");

if barfreq = "Tick" or barfreq = "Min" then
begin
	value1=GetField("上漲量");
	value2=getfield("下跌量");
end else begin
	value1=GetField("上漲量","D");
	value2=getfield("下跌量","D");
end;

value3=value1-value2;
value4=Xaverage(value3,length1)-Xaverage(value3,length2);
plot1(value4,"麥克連震盪指標");
```

---


---

## 腳本檔案: 指標/市場動能/台灣50KD多方家數.xs

```xs
{@type:indicator}
{統計台灣50成分股內, 目前K > D的家數
使用KD指標，資料期數為9，K值平滑期數為3，D值平滑期數為3。}

value1 = GetSymbolField("TSE50.SJ","TW50KD多空家數");

plot1(value1,"台灣50KD多方家數");
```

---


---

## 腳本檔案: 指標/市場動能/台灣50MTM多方家數.xs

```xs
{@type:indicator}
{統計台灣50成分股內, Momentum(10) > 0的家數.
Momentum(N) = 目前價格 - N筆資料前的Close。}

value1 = GetSymbolField("TSE50.SJ","TW50MTM多空家數");

plot1(value1,"台灣50MTM多方家數");
```

---


---

## 腳本檔案: 指標/市場動能/台灣50上昇趨勢家數.xs

```xs
{@type:indicator}
{統計台灣50成分股, 趨勢向上的家數.
趨勢向上的定義是計算近6根K棒(含當前這一根K棒)的線性回歸線是否向上}

value1 = GetSymbolField("TSE50.SJ","TW50上昇趨勢家數");

plot1(value1,"台灣50上昇趨勢家數");
```

---


---

## 腳本檔案: 指標/市場動能/台灣50上漲家數.xs

```xs
{@type:indicator}
{統計台灣50成分股，這一根K棒上漲的家數。
K棒上漲的定義為，目前收盤價 > 前一根K棒的收盤價}

value1 = GetSymbolField("TSE50.SJ","TW50價格上漲家數");

plot1(value1,"台灣50上漲家數");
```

---


---

## 腳本檔案: 指標/市場動能/台灣50創新低家數.xs

```xs
{@type:indicator}
{統計台灣50成分股, 最低價創近20期新低的家數。}

value1 = GetSymbolField("TSE50.SJ","TW50創新低家數");

plot1(value1,"台灣50創新低家數");
```

---


---

## 腳本檔案: 指標/市場動能/台灣50創新高家數.xs

```xs
{@type:indicator}
{統計台灣50成分股，最高價創近20期新高的家數。}

value1 = GetSymbolField("TSE50.SJ","TW50創新高家數");

plot1(value1,"台灣50創新高家數");
```

---


---

## 腳本檔案: 指標/市場動能/台灣50均線多方家數.xs

```xs
{@type:indicator}
{統計台灣50成分股內, 目前股價大於10期簡單移動均線之上的家數。}

value1 = GetSymbolField("TSE50.SJ","TW50均線多空家數");

plot1(value1,"台灣50均線多方家數");
```

---


---

## 腳本檔案: 指標/市場動能/台灣50大單成交次數.xs

```xs
{@type:indicator}
{統計台灣50成分股, 近10分鐘(買進大單次數+買進特大單次數)的平均值}

value1 = GetSymbolField("TSE50.SJ","TW50大單成交次數");

plot1(value1,"台灣50大單成交次數");
```

---


---

## 腳本檔案: 指標/市場動能/台灣50大單買進金額.xs

```xs
{@type:indicator}
{統計台灣50成分股，近10根K棒的買進大單金額平均值。
因為不跨日，所以開盤不足10根K棒時則依照開盤根棒數平均（跨K棒時送出前一根K棒的統計值）}

value1 = GetSymbolField("TSE50.SJ","TW50大單買進金額");

plot1(value1,"台灣50大單買進金額（元）");
```

---


---

## 腳本檔案: 指標/市場動能/台灣50大戶買賣力.xs

```xs
{@type:indicator}
{統計台灣50成分股, 當分鐘大戶買賣力金額。
大戶買賣力為，買進(大單+特大單)-賣出(大單+特大單)}

value1 = GetSymbolField("TSE50.SJ","TW50大戶買賣力");

plot1(value1,"台灣50大戶買賣力（元）");
```

---


---

## 腳本檔案: 指標/市場動能/台灣50紅K家數.xs

```xs
{@type:indicator}
{統計台灣50成分股內, 目前這根K棒是紅K棒的家數.
紅K棒的定義為，收盤價大於開盤價。}

plot1(GetSymbolField("TSE50.SJ","TW50紅K家數"),"台灣50紅K家數");
```

---


---

## 腳本檔案: 指標/技術指標/%b指標.xs

```xs
{@type:indicator}
input: Length(20);	SetInputName(1, "布林通道天數");
input: BandRange(2);SetInputName(2, "上下寬度");
input: MALength(10);SetInputName(3, "MA天期");

variable: up(0), down(0), mid(0);

up = bollingerband(Close, Length, BandRange);
down = bollingerband(Close, Length, -1 * BandRange);

if up - down = 0 then value1 = 0 else value1 = (close - down) * 100 / (up - down);
value2 = average(value1, MALength);

Plot1(value1, "%b");
Plot2(value2, "%b平均");
```

---


---

## 腳本檔案: 指標/技術指標/adaptive price zone.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/adaptive-price-zone/
}

input: 
	Length(14,"期數"), 
	BandPct(2.0,"通道寬度");

variable: DSEMA(0), UpBand(0), DownBand(0), RangeEMA(0), period(0), var0(0);

period = squareroot(Length);
DSEMA = xaverage(xaverage(close, period), period);
RangeEMA = xaverage(xaverage(high-low, period), period);
UpBand = DSEMA + BandPct*RangeEMA;
DownBand = DSEMA - BandPct*RangeEMA;

Plot1(UpBand, "Upperband");
Plot2(close, "Close");
Plot3(DownBand, "BottomBand");
```

---


---

## 腳本檔案: 指標/技術指標/ado聚散擺盪平均線.xs

```xs
{@type:indicator}
input:period(10,"移動平均線天期");
value1=average(ado,period);
plot1(value1,"ado聚散擺盪平均線");
```

---


---

## 腳本檔案: 指標/技術指標/ADTM動態買賣氣指標.xs

```xs
{@type:indicator}
input: length(23);		setinputname(1, "天期");
input: period(8);		setinputname(2, "平均");

variable:DTM(0),DBM(0),STM(0),SBM(0),ADTM(0),ADTMMA(0);

if open > open[1] then 
	DTM = maxlist(high-open,open-open[1])
else
	DTM = 0;
   
if open < open[1] then 
	DBM = open-low
else 
    DBM = 0;

STM = Summation(DTM,length);
SBM = Summation(DBM,length);

if STM > SBM then 
	ADTM = (STM-SBM)/STM
else
  if STM < SBM then 
	ADTM = (STM-SBM)/SBM
  else 
    ADTM = 0;

ADTMMA = average(ADTM,period);

plot1(ADTM, "ADTM");
plot2(ADTMMA, "ADTM移動平均");
```

---


---

## 腳本檔案: 指標/技術指標/Aroon.xs

```xs
{@type:indicator}
input:length(25); setinputname(1, "計算週期");
   
variable: aroon_up(0), aroon_down(0), aroon_oscillator(0);   

aroon_up = (length-nthhighestbar(1,high,length))/length*100;   
aroon_down = (length-nthlowestbar(1,low,length))/length*100;   
aroon_oscillator=aroon_up-aroon_down;   

plot1(aroon_up,"aroon_up");   
plot2(aroon_down,"aroon_down");   
plot3(aroon_oscillator,"aroon_oscillator");
```

---


---

## 腳本檔案: 指標/技術指標/ASI(Accumulation Swing Index)振動升降指標.xs

```xs
{@type:indicator}
input:length(10,"si的累計長度");

variable:si(0),asi(0);

value1=high-low;
value2=low-close[1];
value3=high-low[1];
value4=close[1]-open[1];

value5=absvalue(close-close[1]);
value6=absvalue(close-open);
value7=absvalue(close[1]-open[1]);

value8=(value5+0.5*value6+value7);

switch(maxlist(value1,value2,value3)) begin
	case value1:
		value9=value1+0.5*value2+0.25*value4;
	case value2:
		value9=value2+0.5*value1+0.25*value4;
	case value3:
		value9=value3+0.25*value4;
end;

value10=maxlist(value1,value2);
if value9*value10<>0 then 
	si=50*value8/value9*value10/3
else 
	si=si[1];
asi+=si;

plot1(asi,"ASI");
```

---


---

## 腳本檔案: 指標/技術指標/bandpass filter.xs

```xs
{@type:indicator}
input:
	period(20),
	delta(0.1);
	
variable: price(0),gamma(0),alpha(0),beta(0),BP(0);
price=(h+l)/2;

beta=cosine(360/period);
gamma=1/cosine(720*delta/period);
alpha=gamma-squareroot(gamma*gamma-1);
BP=0.5*(1-alpha)*(price-price[2])+beta*(1+alpha)*BP[1]-alpha*BP[2];

plot1(BP);
plot2(0);
```

---


---

## 腳本檔案: 指標/技術指標/bband當沖操作指標.xs

```xs
{@type:indicator}
input:length(30,"期數");
variable:up1(0),down1(0),mid1(0),bbandwidth(0);
variable:dayprofit(0),accprofit(0);
up1 = bollingerband(Close[1], Length, 2);
down1 = bollingerband(Close[1], Length, -2 );
if open*1.01>up1 then begin
	dayprofit=open-close;
end else if down1*1.01>open then begin
	dayprofit=close-open;
end else
	dayprofit=0;
accprofit=accprofit[1]+dayprofit;
plot1(accprofit,"累計獲利");
```

---


---

## 腳本檔案: 指標/技術指標/BB指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/％b指標/
}

input: 
	Length(20, "天數"), 
	UpperBand(2, "上"), 
	LowerBand(2, "下"), 
	pbLength(5, "%B平均天數");
	
variable: up(0), down(0), mid(0), bbandwidth(0), pb(0);

up = bollingerband(Close, Length, UpperBand);
down = bollingerband(Close, Length, -1 * LowerBand);
mid = (up + down) / 2;

bbandwidth = 100 * (up - down) / mid;
pb=(close-down)/(up-down);
value1=average(pb,pbLength);

plot1(pb,"%b");
plot2(value1,"%b移動平均");
```

---


---

## 腳本檔案: 指標/技術指標/BW MFI.xs

```xs
{@type:indicator}
{
指標說明
Market Facilitation Index
}

if volume <> 0 then
	value1=(high-low)/volume;
if value1>value1[1] and volume>volume[1] then begin
	plot1(volume,"綠燈");
	noplot(2);
	noplot(3);
	noplot(4);
end;
if value1>value1[1] and volume<=volume[1] then begin
	plot2(volume,"偽裝");
	noplot(1);
	noplot(3);
	noplot(4);
end;
if value1<=value1[1] and volume>volume[1] then begin
	plot3(volume,"蟄伏");
	noplot(1);
	noplot(2);
	noplot(4);
end;
if value1<=value1[1] and volume<=volume[1] then begin
	plot4(volume,"衰退");
	noplot(1);
	noplot(2);
	noplot(3);
end;
```

---


---

## 腳本檔案: 指標/技術指標/Chaikin 蔡金波動性指標.xs

```xs
{@type:indicator}
// Chaikin Volatility 指標
//
input: Length(10), LengthROC(12);
variable: _chaikin(0);

SetInputName(1, "天數一");
SetInputName(2, "天數二");

Value1 = XAverage(High - Low, Length);

if CurrentBar >= LengthROC And Value1[LengthROC] <> 0 then
	_chaikin = 100 * (Value1 - Value1[LengthROC]) / Value1[LengthROC]
else
	_chaikin = 0;
	
Plot1(_chaikin, "Chaikin");
```

---


---

## 腳本檔案: 指標/技術指標/CMI市場波動指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/如何判斷現在是趨勢還是盤整-一個還在研究的課/
}

input:period(10,"計算區間");
value1=(close-close[period-1])/(highest(high,period)-lowest(low,period))*100;
value2=absvalue(value1)-30;
value3=average(value2,3);
plot1(value3,"市場波動指標");
```

---


---

## 腳本檔案: 指標/技術指標/CMO(錢德動量擺盪指標).xs

```xs
{@type:indicator}
Input:length(10);   setinputname(1, "天期");

variable: SU(0),SD(0);   

if close >= close[1] then   
  SU = CLOSE - CLOSE[1]   
else   
  SU = 0;   

if close < close[1] then   
  SD = CLOSE[1] - CLOSE   
else   
  SD = 0;    

value1 = summation(SU,length);   
value2 = summation(SD,length);   
if value1+value2 <> 0 then value3 = (value1-value2)/(value1+value2)*100;
plot1(value3, "CMO");
```

---


---

## 腳本檔案: 指標/技術指標/coppock indicator.xs

```xs
{@type:indicator}
variable:coppock(0);
value1=rateofchange(close,14);
value2=rateofchange(close,11);
value3=value1+value2;
value4=xaverage(value3,10);
plot1(value4,"coppock indicator");
```

---


---

## 腳本檔案: 指標/技術指標/CPC指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/自訂指標的撰寫技巧以q指標為例/
收錄於「三週學會程式交易：打造你的第一筆自動化交易」 317頁
https://www.ipci.com.tw/books_in.php?book_id=724
}

input:t1(10,"計算累積價格變動的bar數");
input:t2(5,"短期平均天期");
input:t3(20,"長期平均天期");

value1=close-close[1];//價格變化
value2=summation(value1,t1);//累積價格變化
value3=average(value2,t2);//短期平均
value4=average(value2,t3);//長期平均

plot1(value3,"短期累積價格變化平均");
plot2(value4,"長期累積價格變化平均");
```

---


---

## 腳本檔案: 指標/技術指標/CR指標.xs

```xs
{@type:indicator}
input:Length(26,"N日累積");
variable:Upsum(0),Downsum(0),CR(0); 
 
Upsum =  summation(high - WeightedClose[1],Length);
Downsum = summation(WeightedClose[1] - low,Length); 
 
if Downsum <> 0 then
	CR = Upsum / Downsum *100
else
	CR = CR[1]; 
 
plot1(CR,"CR(%)");
```

---


---

## 腳本檔案: 指標/技術指標/DBCD 異同離差乖離率 .xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/異同離差乖離率dbcd在單一國家股票型基金的應用/
}

input:
	length1(10,"短天期"),
	length2(20,"長天期"),
	length3(14,"平均天期");

value1=bias(length1);
value2=bias(length2);
value3=value2-value1;
value4=average(value3,length3);
plot1(value4,"DBCD");
```

---


---

## 腳本檔案: 指標/技術指標/demand index.xs

```xs
{@type:indicator}
{ 
James Sibbet's Demand Index Indicator 
The Demand Index combines price and volume in 
such a way that it is often a leading indicator of 
price change. 
} 

input: Length (10,"期數"); 

variable : 
	WtCRatio(1), VolRatio(1), VolAvg(Volume), 
	bu(1), sel(1), Sign1(+1), 
	WghtClose(Close), AvgTR(High - Low), 
	Constant(1), bures(1), selres(1), 
	TempDI(1), DMI(1); 

If CurrentBar = 1 then 
	VolAvg = Average(Volume, Length); 

WghtClose = (High + Low + Close + Close) * 0.25; 
AvgTR = Average (Highest (High, 2) - Lowest ( Low, 2), Length); 
VolAvg = ((VolAvg [1] * (Length - 1)) + Volume) / Length; 

If WghtClose <> 0 and WghtClose[1] <> 0 and 
	AvgTR <> 0 and VolAvg <> 0 then Begin 
	WtCRatio = (WghtClose - WghtClose[1]) / MinList(WghtClose,WghtClose[1]) ; 
	VolRatio = Volume / VolAvg; 
	Constant = ((WghtClose * 3) /AvgTR) * AbsValue (WtCRatio); 
	If Constant > 88 then Constant = 88; 
	Constant = VolRatio / ExpValue (Constant); 
	If WtCRatio > 0 then Begin 
		bu = VolRatio; 
		sel = Constant; 
	End Else Begin 
		bu = Constant; 
		sel = VolRatio; 
	End; 

	bures = ((bures [1] * (Length - 1)) + bu) / Length; 
	selres = ((selres [1] * (Length - 1)) + sel) / Length; 

	TempDI = +1; 

	If selres > bures then Begin 
		Sign1 = -1; 
		If selres <> 0 then TempDI = bures / selres; 
	End Else Begin 
		Sign1 = +1; 
		If bures <> 0 then TempDI = selres / bures; 
	End; 

	TempDI = TempDI * Sign1; 
	If TempDI < 0 then 
		DMI = -1 - TempDI 
	else 
		DMI = +1 - TempDI ; 
End;

Plot1(dmi);
```

---


---

## 腳本檔案: 指標/技術指標/DMI.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/787/
}

input:length(10,"期數");

variable: pdi_value(0), ndi_value(0), adx_value(0);

DirectionMovement(Length, pdi_value, ndi_value, adx_value);
value1=pdi_value-ndi_value;

plot1(pdi_value,"向上力量");
plot2(ndi_value,"向下力量");
plot3(value1,"多空力道差");
```

---


---

## 腳本檔案: 指標/技術指標/ease of movement指標.xs

```xs
{@type:indicator}
input:
	length1(9,"一次平滑期數"),
	length2(9,"二次平滑期數");

value1=(high+low)/2;
value2=value1-value1[1];
value3=volume/(high-low);
value4=value2/value3;
value5=average(value4,length1);
value6=average(value5,length2);

plot1(value5,"EMV");
plot2(value6,"EMV-MA");
```

---


---

## 腳本檔案: 指標/技術指標/Elder 多頭力道指標.xs

```xs
{@type:indicator}
// Elder 多頭力道指標
//
input: Length(13);

SetInputName(1, "天數");
Value1 = High - XAverage(Close, Length);

Plot1(Value1, "多頭");
```

---


---

## 腳本檔案: 指標/技術指標/Elder 空頭力道指標.xs

```xs
{@type:indicator}
// Elder 空頭力道指標
//
input: Length(13);

SetInputName(1, "天數");

Value1 = Low - XAverage(Close, Length);

Plot1(Value1, "空頭");
```

---


---

## 腳本檔案: 指標/技術指標/EMA-SMA.xs

```xs
{@type:indicator}
input:period(20,"計算期間");

value1=EMA(close,period);
value2=average(close,period);
if close<>0 then 
	value3=(value1-value2)/close*100;

plot1(value3,"EMA-SMA");
```

---


---

## 腳本檔案: 指標/技術指標/empirical mode decomposition.xs

```xs
{@type:indicator}
input:
	period(20),
	delta(0.1),
	fraction(0.1);
	
variable: 
	price(0),gamma(0),alpha(0),beta(0),BP(0),
	mean(0),peak(0),valley(0),avgpeak(0),avgvalley(0);

price=(h+l)/2;

beta=cosine(360/period);
gamma=1/cosine(720*delta/period);
alpha=gamma-squareroot(gamma*gamma-1);
BP=0.5*(1-alpha)*(price-price[2])+beta*(1+alpha)*BP[1]-alpha*BP[2];
mean=average(bp,2*period);
peak=peak[1];
valley=valley[1];

if bp[1]>bp and bp[1]>bp[2] then peak=bp[1];
if bp[1]<bp and bp[1]<bp[2] then valley=bp[1];
avgpeak=average(peak,50);
avgvalley=average(valley,50);

plot1(mean);
plot2(fraction*avgpeak);
plot3(fraction*avgvalley);
```

---


---

## 腳本檔案: 指標/技術指標/extracting the trend.xs

```xs
{@type:indicator}
input:
	period(20),
	delta(0.1);
	
variable: price(0),gamma(0),alpha(0),beta(0),BP(0),trend(0);
price=(h+l)/2;

beta=cosine(360/period);
gamma=1/cosine(720*delta/period);
alpha=gamma-squareroot(gamma*gamma-1);
BP=0.5*(1-alpha)*(price-price[2])+beta*(1+alpha)*BP[1]-alpha*BP[2];
trend=average(bp,2*period);

plot1(trend);
plot2(0);
```

---


---

## 腳本檔案: 指標/技術指標/HV歷史波動率指標.xs

```xs
{@type:indicator}
input:LENGTH1(6,"短天期"),LENGTH2(100,"短天期");

variable:HVS(0),HVL(0),HVindex(0);
value1=log(close/close[1]);
HVS=STANDARDDEV(value1,LENGTH1,1)*100*SQUAREROOT(252);
HVL=STANDARDDEV(VALUE1,LENGTH2,1)*100*SQUAREROOT(252);
HVindex=HVS/HVL;

plot1(hvindex,"歷史波動率指標");
```

---


---

## 腳本檔案: 指標/技術指標/IMI日內動能指標.xs

```xs
{@type:indicator}
input:length(10);		setinputname(1, "天期");
   
variable:up(0),dn(0),upi(0),dni(0),imi(0);   

if close > open then   
  up = close-open   
else   
  up = 0;   

if close < open then   
  dn = open-close   
else   
  dn = 0;   

upi = summation(up,length);   
dni = summation(dn,length);   
if upi+dni = 0 then imi = 0 else imi = upi/(upi+dni)*100;   

plot1(imi, "IMI");
```

---


---

## 腳本檔案: 指標/技術指標/KO能量潮指標.xs

```xs
{@type:indicator}
variable: kovolume(0);

value1=(close+high+low)/3;
if CurrentBar = 1 then
	kovolume = 0
else begin	
	if value1 > value1[1] then
		kovolume = kovolume[1] + volume
	else begin
		if value1 < value1[1] then
			kovolume = kovolume[1] - volume
		else
			kovolume = kovolume[1];
	end;		
end;
  
Plot1(kovolume, "KO能量潮指標");
```

---


---

## 腳本檔案: 指標/技術指標/K棒衍生指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/雙k棒可以延伸的多空趨勢指標/
}

array:k[22](0);
if close<>0 then begin
	//最近一日與前一日的多空力道總差額
	k[1]=(open-open[1])/close;
	k[2]=(high-high[1])/close;
	k[3]=(low-low[1])/close;
	k[4]=(close-close[1])/close;
	//當日
	k[5]=(high-low)/close;
	k[6]=(high-close)/close;
	k[7]=(high-open)/close;
	k[8]=(open-low)/close;
	k[9]=(close-open)/close;
	k[10]=(close-low)/close;
	k[11]=(open-high[1])/close;
	k[12]=(open-low[1])/close;
	k[13]=(open-close[1])/close;
	k[14]=(high-open[1])/close;
	k[15]=(high-low[1])/close;
	k[16]=(high-close[1])/close;
	k[17]=(low-open[1])/close;
	k[18]=(low-high[1])/close;
	k[19]=(low-close[1])/close;
	k[20]=(close-open[1])/close;
	k[21]=(close-high[1])/close;
	k[22]=(close-low[1])/close;
end;

array: v1[8](0);
v1[1]=k[1]+k[11]+k[12]+k[13];//隔日開盤多空總力道
v1[2]=k[1]+k[2]+k[3]+k[4];//隔日多空總力道
v1[3]=k[20]+k[21]+k[22];//隔日收盤多空結果
v1[4]=k[9]+k[10]-k[6];//當日收盤多空結果
v1[5]=k[14]+k[15]+k[16];//多頭最大力量
v1[6]=(k[17]+k[18]+k[19])*-1;//空頭最大力量
v1[7]=k[7]+k[9]+k[10];//當日多頭最大力量
v1[8]=k[6]+k[8]-k[10];//當日空頭最大力量

value1=v1[1]+v1[2]+v1[3]+v1[4];
value2=v1[5]+v1[7];
value3=v1[6]+v1[8];
plot1(average(value1,5),"多空淨力");
plot2(average(value2,5),"多頭總力");
plot3(average(value3,5),"空頭總力");
```

---


---

## 腳本檔案: 指標/技術指標/LRR線性迴歸反轉指標.xs

```xs
{@type:indicator}
input:period(10,"期數");

variable:lrr(0);

value1=linearregslope(close,period);
if value1>value1[1] then
	lrr=1
else
	lrr=-1;

plot1(lrr,"線性迴歸反轉指標");
```

---


---

## 腳本檔案: 指標/技術指標/Mass Index.xs

```xs
{@type:indicator}
input: length1(9);	setinputname(1, "天期一");
input: length2(25); setinputname(2, "天期二");
  
value1 = average(range,length1);   
value2 = average(value1,length1);   
if value2 = 0 then value3 = 0 else value3 = value1/value2;
value4 = summation(value3,length2); 

plot1(value4,"Mass Index");
```

---


---

## 腳本檔案: 指標/技術指標/MFO資金流震盪指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/大盤多空轉換點之探討系列三-mfo資金流震盪指標/
}

input:period(20,"計算天期");

if ((high-low[1])+(high[1]-low)) <> 0 then
	value1= ((high-low[1])-(high[1]-low))/((high-low[1])+(high[1]-low))*volume
else
	value1=value1[1];
	
value2= summation(value1,period)/summation(volume,period);

plot1(value2,"MFO資金流震盪指標");
```

---


---

## 腳本檔案: 指標/技術指標/MF錢流指標.xs

```xs
{@type:indicator}
INPUT:N(10,"期數");

variable: AP(0),tv(0),UTV(0),DTV(0),MF(0),UP(0),DN(0);

ap=(high+low+close)/3;
tv=ap*volume;
if ap>ap[1] then begin
	utv=tv;
	dtv=0;
end else begin
	utv=0;
	dtv=tv;
end;
up=UP[1]+(UTV-UP[1])/N;
DN=DN[1]+(DTV-DN[1])/N;
IF DN<>0 THEN 
	MF=100-(100/(1+UP/DN))
else
	MF=MF[1];
	
PLOT1(MF,"MF");
```

---


---

## 腳本檔案: 指標/技術指標/N日來漲幅較大天數.xs

```xs
{@type:indicator}
{
指標說明
收錄於「三週學會程式交易：打造你的第一筆自動化交易」 327頁
https://www.ipci.com.tw/books_in.php?book_id=724
}

input:ratio(2,"列入計算之漲幅下限");
input:period(20,"計算區間");
input:period1(10,"移動平均天數");

if close[1]<>0 then
	value1=(close-close[1])/close[1]*100;
value2=countif(value1>=ratio,period);

plot1(value2,"漲幅大的天數");
plot2(average(value2,period1),"移動平均");
```

---


---

## 腳本檔案: 指標/技術指標/N日內上漲天數.xs

```xs
{@type:indicator}
input:length(20,"期數");

variable:count(0);
variable:x1(0);

count=countif(close>close[1],length);

plot1(count,"上漲天數");
```

---


---

## 腳本檔案: 指標/技術指標/range trading指標.xs

```xs
{@type:indicator}
value1=average(range,200);
value2=average(range,3);
value3=(value2-value1)/value1;
plot1(value3,"長短天期range差");
```

---


---

## 腳本檔案: 指標/技術指標/RunScore.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/Runscore指標/
}

input:QDate(20140630,"起算日");
//先設定一個季結束的日子
variable:RunScore(0),vs(0),i(0);

if date > QDate then begin
	if C>C[1] then RunScore += 1;//收漲加1分
	if H>H[1] then RunScore += 1;//漲過昨高加1分
	if C>H[1] then RunScore += 1;//收過昨高加1分
	if C<C[1] then RunScore -= 1;//收跌扣1分
	if L<L[1] then RunScore -= 1;//破昨低扣1分
	if C<L[1] then RunScore -= 1;//收破昨低扣1分
	vs += v; 
	i += 1;
end;

plot1( RunScore,"漲跌分數");
```

---


---

## 腳本檔案: 指標/技術指標/R平方.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/趨勢檢定器/
}

input:Length(20,"計算期間");
 
LinearReg(close, Length, 0, value1, value2, value3, value4);
//做收盤價20天線性回歸
{value1:斜率,value4:預期值}
value5=rsquare(close,value4,Length);//算收盤價與線性回歸值的R平方 

plot1(value5,"R平方");
plot2(0.2,"趨勢成形線");
```

---


---

## 腳本檔案: 指標/技術指標/Stoller平均波幅通道.xs

```xs
{@type:indicator}
input:
	avlength(5,"均線期數"),
	atrlength(15,"ATR平均期數"),
	k(1.35,"常數");
variable:hband(0),lband(0);

hband=average(close,avlength)+average(truerange,atrlength)*k;
lband=average(close,avlength)-average(truerange,atrlength)*k;

plot1(hband,"通道上限");
plot2(close,"收盤價");
plot3(lband,"通道下限");
```

---


---

## 腳本檔案: 指標/技術指標/vortex indicator.xs

```xs
{@type:indicator}
input: period(14,"設定區間");

variable:pvm(0);
variable:nvm(0);

pvm=absvalue(high-low[1]);
nvm=absvalue(low-high[1]);
value1=summation(pvm,period);
value2=summation(nvm,period);
value3=summation(truerange,period);
value4=value1/value3;
value5=value2/value3;
value6=value4-value5;

plot1(value6,"vortex");
```

---


---

## 腳本檔案: 指標/技術指標/ZDZB築底指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/築底指標-2/
}

input:
	period(125,"計算期數"),
	length1(5,"短MA期數"),
	length2(20,"長MA期數");
	
variable:zd(0),zdma1(0),zdma2(0);

zd=countif(close>=close[1],period)/countif(close<close[1],period);
zdma1=average(zd,length1);
zdma2=average(zd,length2);

plot1(zdma1,"短天期築底指標");
plot2(zdma2,"長天期築底指標");
plot3(1,"多空分界");
```

---


---

## 腳本檔案: 指標/技術指標/Zero Lag Heikin-Ashi.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/先進指標zero-lag-heikinashi/
}

input: Length(14,"期數");

variable: 
		price(0), haO(0), haC(0), haMax(0), haMin(0), 
		TEMA1(0), EMAValue1(0), DbEMAValue1(0), 
		TEMA2(0), EMAValue2(0), DbEMAValue2(0), ZeroLagHA(0);
 
price = (close+open+high+low)/4;
haO = (haO[1]+price)/2;
haMax = maxlist(high, haO);
haMin = minlist(low, haO);
 
haC = (price+haO+haMax+haMin)/4;
 
EMAValue1 = xaverage(haC, Length);
DbEMAValue1 = xaverage(EMAValue1, Length);
TEMA1 = 3*EMAValue1-3*DbEMAValue1+xaverage(DbEMAValue1, Length);
EMAValue2 = xaverage(TEMA1, Length);
DbEMAValue2 = xaverage(EMAValue2, Length);
TEMA2 = 3*EMAValue2-3*DbEMAValue2+xaverage(DbEMAValue2, Length);
 
ZeroLagHA = 2*TEMA1-TEMA2;
 
plot1(ZeroLagHA, "Zero Lag HeikinAshi");
plot2(average(C,20),"Average");
```

---


---

## 腳本檔案: 指標/技術指標/上影線佔實體比例五日平均.xs

```xs
{@type:indicator}
value1=average(upshadow,5);

plot1(value1,"五日平均上影線佔實體比例");
```

---


---

## 腳本檔案: 指標/技術指標/上漲下跌幅度強弱度指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/雲端策略中心精進版之34多頭轉強策略/
}

input:length(10,"期數"); 

variable: sumUp(0), sumDown(0), up(0), down(0),RS(0);

if CurrentBar = 1 then begin
	sumUp = Average(maxlist(close - close[1], 0), length); 
	sumDown = Average(maxlist(close[1] - close, 0), length); 
end else begin
	up = maxlist(close - close[1], 0);
	down = maxlist(close[1] - close, 0);	 
	sumUp = sumUp[1] + (up - sumUp[1]) / length;
	sumDown = sumDown[1] + (down - sumDown[1]) / length;
end;
if sumdown<>0 then rs=sumup/sumdown;

plot1(rs,"強弱度");
```

---


---

## 腳本檔案: 指標/技術指標/上漲下跌角度線.xs

```xs
{@type:indicator}
input: periods(5, "期數");
 
Value1 = Angle(Date[periods], Date);

Plot1(Value1, "角度");
```

---


---

## 腳本檔案: 指標/技術指標/上漲天數指標.xs

```xs
{@type:indicator}
input:count1(20);
input:count2(10);

value1=countif(close>close[1],count1);
value2=countif(close>close[1],count2);
value3=value1-value2;

plot1(value1);
plot2(value2);
plot3(value3);
```

---


---

## 腳本檔案: 指標/技術指標/主動買力.xs

```xs
{@type:indicator}
input:p1(5,"短天期");
input:p2(20,"長天期");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

value1=GetField("主動買力");
value2=average(value1,p1);
value3=average(value1,p2);

plot1(value2,"主動買力短天期MA");
plot2(value3,"主動買力長天期MA");
```

---


---

## 腳本檔案: 指標/技術指標/倉 put call ratio.xs

```xs
{@type:indicator}
//台指選擇權現貨(TXO00.TF) 的 買賣權未平倉量比率

value1=GetSymbolField("TXO00.TF", "買賣權未平倉量比率");
plot1(value1,"put call ratio");
```

---


---

## 腳本檔案: 指標/技術指標/價格震盪指標.xs

```xs
{@type:indicator}
input: length1(5);	setinputname(1, "短天期");
input: length2(20);	setinputname(2, "長天期");

value1 = average(close, length1);
value2 = average(close, length2);

if value1 = 0 then value3 = 0 else value3 = 100 * (value1 - value2) / value1;

plot1(value3, "OSCP");
```

---


---

## 腳本檔案: 指標/技術指標/價量斜率指標.xs

```xs
{@type:indicator}
value1=average(close,5);
value2=average(volume,5);
value3=linearregslope(value1,5);
value4=linearregslope(value2,5);
value5=value4-value3;

plot1(value3,"價斜率");
plot2(value4,"量斜率");
plot3(value5,"斜率差");
```

---


---

## 腳本檔案: 指標/技術指標/價量齊揚天數.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/從相對的角度尋找真正價量齊揚的股票/
}

input:sp(10,"短計算區間");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

variable:count1(0) ;

value1=GetField("資金流向");
value2=GetField("強弱指標");
count1=countif(value2>0and value1>value1[1],sp);
value3=average(count1,5);

plot1(value3/SP*100,"短期價量齊揚天數");
```

---


---

## 腳本檔案: 指標/技術指標/六合神拳指數.xs

```xs
{@type:indicator}
input:length1(6,"短天期RSI參數");
input:length2(10,"長天期RSI參數");
input:length3(10,"MTM天期");
input:length4(10,"DMI天期");

variable:count(0);

count=0;
if RSI(Close, Length1) > RSI(Close, Length2)
and rsi(close,length1)<50 then
	count=1;
if Momentum(Close, Length3) > 0 then
	count=count+1;

variable:pdi_value(0);
variable:ndi_value(0);
variable:adx_value(0);
directionmovement(length4,pdi_value,ndi_value,adx_value);
if pdi_value > ndi_value then 
	count=count+1;
	

variable:rsv1(0),k1(0),d1(0);
stochastic(9,3,3,rsv1,k1,d1);
if k1 > d1 then 
	count=count+1;

value1=average(volume,10);
if linearregslope(value1,8)>0 then
	count=count+1;

value2=average(close,8);
if linearregslope(value2,5)>0 then
	count=count+1;
	
plot1(count,"分數");
```

---


---

## 腳本檔案: 指標/技術指標/創新高天數減破底天數.xs

```xs
{@type:indicator}
input:period(12,"期數");

value1=countif(low<lowest(low[1],period),period);//近期創新低天數
value2=countif(high>highest(high[1],period),period);//近期創新高天數
value3=value2-value1;

plot1(value3,"天數差");
plot2(3);
plot3(-3);
```

---


---

## 腳本檔案: 指標/技術指標/力度指標force index.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/這個盤接下來到底會不會大跌-建構專屬的大盤儀/
}

input:
	length(10,"短天期"),
	length1(30,"長天期");
	
variable:fis(0),fil(0);
fis=average(volume*(close-close[1]),length);
fil=average(volume*(close-close[1]),length1);

plot1(fis,"短期力度");
plot2(fil,"長期力度");
plot3(fis-fil,"長短力度差");
```

---


---

## 腳本檔案: 指標/技術指標/加速器指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/495/
}

variable:Xslope(0); 

Xslope = linearregslope((H+L)/(H+L)[20],20);

plot1(Xslope,"方向速度" );
plot2(Xslope-Xslope[1],"速度變化");
```

---


---

## 腳本檔案: 指標/技術指標/加速指標.xs

```xs
{@type:indicator}
input:period1(5,"計算天期");
input:period2(9,"MA天期");

variable:aspeed(0),dspeed(0),a1(0),d1(0),p1(0),ap1(0);

if close>close[1] then
	aspeed=(close-close[1])/close*100
else 
	aspeed=0;
	
if close<close[1] then
	dspeed=(close[1]-close)/close*100
else
	dspeed=0;

a1=average(aspeed,period1);
d1=average(dspeed,period1);


p1=a1-d1;
ap1=average(p1,period2);

plot1(p1,"加速度");
plot2(ap1,"移動平均");
```

---


---

## 腳本檔案: 指標/技術指標/勁道指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/積極勁道指標/
}

input:day(13,"期數");

if barfreq = "Tick" or barfreq = "Min" then
begin
	value1=GetField("外盤量");//單位:元
	value6=GetField("內盤量");//單位:元
end else begin
	value1=GetField("外盤量","D");//單位:元
	value6=GetField("內盤量","D");//單位:元
end;
value2=volume*(close-close[1]);
value8=average(volume,day);
if value6<>0 then 
	value7=(value1/value6)*volume*(close-close[1]);
value3=value7*(close-close[1]);
value4=average(value2,day)/value8;
value5=average(value3,day)/value8;


plot1(value4,"勁道指標");
plot2(value5,"積極勁道指標");
```

---


---

## 腳本檔案: 指標/技術指標/動量指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/尋找趨勢是否成形的指標動量指標/
}

if barfreq = "Tick" or barfreq = "Min" then
begin
	value1=GetField("內盤量");//單位:元
	value2=GetField("外盤量");//單位:元
end else begin
	value1=GetField("內盤量","D");//單位:元
	value2=GetField("外盤量","D");//單位:元
end;
value3=(high+low)/2;//計算當天波動的平均價位
//質量就是內外盤差乘均價
if value2>value1 then
	value4=value3*(value2-value1)
else
	value4=value3*(value1-value2);
if close>=close[1] then begin //(方向是往上)
	value5=(close-close[1])/close[1]*value4;//質量乘以速度
	value6=0;
end else begin//(方向是往下)
	value5=0;
	value6=(close[1]-close)/close[1]*value4;
end;
value8=average(value5,2);
value9=average(value6,2);
value10=value8-value9;

plot1(value10,"動能差");
```

---


---

## 腳本檔案: 指標/技術指標/向上拉動與向下殺盤力道指標.xs

```xs
{@type:indicator}
input:period(5,"加權移動平均線天期");

//當日向上拉動的力量
value1=(high-open)+(close-low);
//當日向下殺盤的力量
value2=(open-low)+(high-close);
if close<>0 then begin
	//上拉力道
	value3=average(value1,period)/close*100;
	//下殺力道
	value4=xaverage(value2,period)/close*100;
end;
value5=value3-value4;
plot1(value5,"上拉下殺淨力道");
```

---


---

## 腳本檔案: 指標/技術指標/外盤成交比例指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/外盤成交比例指標/
}

input:
	short1(5,"短期平均"),
	mid1(12,"長期平均");

if barfreq = "Tick" or barfreq = "Min" then
begin
	value1=GetField("內盤量");//單位:元
	value2=GetField("外盤量");//單位:元
end else begin
	value1=GetField("內盤量","D");//單位:元
	value2=GetField("外盤量","D");//單位:元
end;
value3=value1+value2;
if value3<>0 then 
	value4=value2/value3*100;
value5=average(value4,short1);
value6=average(value4,mid1);

plot1(value5,"短期均線");
plot2(value6,"長期均線");
```

---


---

## 腳本檔案: 指標/技術指標/多方力道線.xs

```xs
{@type:indicator}
input:
	period1(10,"計算期數"),
	period2(5,"平滑期數");

value1=summation(high-close,period1);//上檔賣壓
value2=summation(close-open,period1); //多空實績
value3=summation(close-low,period1);//下檔支撐
value4=summation(open-close[1],period1);//隔夜力道
if close<>0 then
	value5=(value2+value3+value4-value1)/close;
value6=average(value5,period2);

plot1(value6,"多方力道");
```

---


---

## 腳本檔案: 指標/技術指標/多空判斷分數.xs

```xs
{@type:indicator}

value1 = techscore;

plot1(value1, "多空指標");
plot2(3, "低點");
plot3(11, "高點");
```

---


---

## 腳本檔案: 指標/技術指標/多空力道指標.xs

```xs
{@type:indicator}
input: length(5);	setinputname(1, "天期");

Value1 = high - close;   
Value2 = close - low; 

Value3 = average(Value1,length);   
Value4 = average(Value2,length);   

plot1(Value4 - Value3, "力道");
```

---


---

## 腳本檔案: 指標/技術指標/多頭動能.xs

```xs
{@type:indicator}
input:period(10,"平均值天期");

value1=high-close[1]+low-low[1];
value2=average(value1,period);

plot1(value2,"多頭動能平均值");
```

---


---

## 腳本檔案: 指標/技術指標/天羅地網線.xs

```xs
{@type:indicator}
input:period(60,"期數");

value5=average(close,period);
value6=standarddev(close,period,1);
value7=value5+value6;
value8=value5+2*value6;
value9=value5-value6;
value10=value5-2*value6;

plot1(value8,"+2SD");
plot2(value7,"+1SD");
plot3(value5,"MA");
plot4(value9,"-1SD");
plot5(value10,"-2SD");
```

---


---

## 腳本檔案: 指標/技術指標/循環指標.xs

```xs
{@type:indicator}
input:period(20);
input:delta(0.5);
input:fraction(0.1);

variable:price(0);
variable:alpha(0),beta(0),gamma(0),bp(0),i(0),mean(0),peak(0),valley(0),avgpeak(0),avgvalley(0);

price=(h+l)/2;
beta=cosine(360/period);
gamma=1/cosine(720*delta/period);
alpha=gamma-squareroot(gamma*gamma-1);
bp=0.5*(1-alpha)*(price-price[2])+beta*(1+alpha)*bp[1]-alpha*bp[2];
mean=average(bp,2*period);
peak=peak[1];
valley=valley[1];
if bp[1]>bp and bp[1]>bp[2] then peak=bp[1];
if bp[1]<bp and bp[1]<bp[2] then valley=bp[1];
avgpeak=average(peak,50);
avgvalley=average(valley,50);

plot1(mean);
```

---


---

## 腳本檔案: 指標/技術指標/月線與收盤價差.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/自訂指標/
}

value1=average(close,22);
value2=close-value1;
value3=average(value2,3);

plot1(value3,"月線與收盤價差三日移動平均");
plot2(0);
```

---


---

## 腳本檔案: 指標/技術指標/比大盤強的天數.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/股性系列之七-比大盤強的天數/
}

input:day(10,"統計天數");
input:period(20,"平滑天數");

if barfreq <> "D" then raiseruntimeerror("不支援此頻率");

value1=GetField("強弱指標");
value2=countif(value1>1,day);
value3=average(value2,period);

plot1(Value2,"比大盤強的天數");
plot2(value3,"移動平均");
```

---


---

## 腳本檔案: 指標/技術指標/比大盤強的天數趨勢斜率.xs

```xs
{@type:indicator}
input:period(10,"計算天期");

if barfreq <> "D" then raiseruntimeerror("不支援此頻率");

value1=GetField("強弱指標");
value2=countif(value1>1,period);
value3=average(value2,period);
linearreg(value3,period,0,value4,value5,value6,value7);

plot1(value4,"強度斜率");
```

---


---

## 腳本檔案: 指標/技術指標/波動區間指標.xs

```xs
{@type:indicator}
input:
	short1(3,"短期平均"),
	mid1(20,"長期平均");

value1=highest(high,5);
value2=lowest(low,5);
if value2 <> 0 then
	value3=(value1-value2)/value2*100;
value4=average(value3,short1);
value5=average(value3,mid1);

plot1(value4,"短期平均區間");
plot2(value5,"長期平均區間");
```

---


---

## 腳本檔案: 指標/技術指標/波動率指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/918/
}

value1 = 100*(average(H/L-1,20)+standarddev(H/L-1,20,1)*3);
value2 = value1- average(value1,10);

plot1(value1,"波動指標");
if value2> 0 then plot2(value2,"波動放大");
if value2<= 0 then plot3(value2,"波動縮小");
```

---


---

## 腳本檔案: 指標/技術指標/淨買賣力指標.xs

```xs
{@type:indicator}
input: Period(20,"期數");

if high<>low and truerange <> 0 then begin 
	value1=((high-open)+(close-low))/truerange;
	value2=((open-low)+(high-close))/truerange;
end else begin
	value1=value1[1];
	value2=value2[1];
end;
value3=value1-value2;
value4=average(value3,Period);
 
plot1(value4,"平均淨買賣力");
```

---


---

## 腳本檔案: 指標/技術指標/真實波動區間指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/股性系列之六真實波動區間/
}

input: Length1(3, "短天數");
input: Length2(20,"長天數");

value1 = Average(TrueRange, Length1);
value2 = Average(TrueRange, Length2);

Plot1(value1, "短期ATR");
plot2(value2, "長期ATR");
```

---


---

## 腳本檔案: 指標/技術指標/短線交易比例.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/短線過熱的指標/
}

input:p1(5,"移動平均線天期");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

value1=GetField("融資買進張數");
value2=GetField("現股當沖張數");
value3=GetField("資券互抵張數");

value4=value1+value2+value3;

if volume>0 then 
	value5=value4/volume;
value6=average(value5,p1);

plot1(value5,"短線交易比例");
plot2(value6,"移動平均線");
```

---


---

## 腳本檔案: 指標/技術指標/終極擺盪指標.xs

```xs
{@type:indicator}

input:length1(7);		setinputname(1, "天期一");
input:length2(14);		setinputname(2, "天期二");
input:length3(28);   	setinputname(3, "天期三");

variable : ruo(0),uo(0),bp(0);  

bp = close-truelow;
   
Value1=summation(bp,length1);   
Value2=summation(bp,length2);   
Value3=summation(bp,length3);   

Value4=summation(truerange,length1);   
Value5=summation(truerange,length2);   
Value6=summation(truerange,length3);
   
ruo = (value1/value4)*4+(value2/value5)*2+(value3/value6);   

uo= ruo / 7 * 100;   

plot1(uo, "UO");
```

---


---

## 腳本檔案: 指標/技術指標/線性迴歸斜率.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/尋找目前趨勢還向上的股票/
}

input:Length(20,"計算期間");

variable: _Output(0);

LinearReg(close, Length, 0, value1, value2, value3, value4);
{value1:斜率,value4:預期值}

plot1(value1,"線性迴歸斜率");
```

---


---

## 腳本檔案: 指標/技術指標/股性綜合分數指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/把股性拿來作為過濾條件/
}

input:day(20);
input:ratio(10);

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

variable:count(0),x(0);

value1=GetField("總成交次數","D");
value2=average(value1,day);
value3=GetField("強弱指標");
value5=GetField("外盤均量");
value6=average(value5,day);
value7=GetField("主動買力");
value8=average(value7,day);
value9=GetField("開盤委買");
value10=average(value9,day);
value11=GetField("資金流向");
value12=average(value11,day);
value13=countif(value3>1,day);
value14=average(value13,day);//比大盤強天數
value16=GetField("法人買張");

count=0;
if value1>value2*(1+ratio/100) then count=count+1;
//比大盤強的天數
if value13>value14*(1+ratio/100) then count=count+1;
if value5>value6*(1+ratio/100) then count=count+1;
if value7>value8*(1+ratio/100) then count=count+1;
if value9>value10*(1+ratio/100) then count=count+1;
//真實波動區間
if truerange> average(truerange,20) then count=count+1;
//計算承接的力道
if truerange<>0 then begin
	if close<=open then
		value15=(close-low)/truerange*100
	else
		value15=(open-low)/truerange*100;
end;
if value15 > average(value15,day)*(1+ratio/100) then count=count+1;
//法人買張佔成交量比例
if volume<>0 then value17=value16/volume*100;
if value17>average(value17,10)*(1+ratio/100) then count=count+1;
if value11>average(value11,10)*(1+ratio/100) then count=count+1;

value18=countif(close>=close[1]*1.02,5);
//N日來漲幅較大的天數
if value18 >= 2 then count=count+1;

value19=GetField("融資買進張數");
value20=GetField("融券買進張數");
value21=(value19+value20);
value22=average(value21,day);
//散戶作多指標
if value21<value22*0.9 then count=count+1;

plot1(average(count,3),"股性綜合分數指標");
plot2(3);
```

---


---

## 腳本檔案: 指標/技術指標/蔡金波動指標.xs

```xs
{@type:indicator}
input:length(9,"期數");

variable:REMA(0),cv1(0);

if currentbar=1 then begin
	cv1=0;
end else if range<>0 then begin
	REMA=xaverage(range,length);
	if rema[length-1]=0 then 
		cv1=cv1[1]
	else 
		cv1=(REMA-REMA[length-1])/rema[length-1];
end;
plot1(cv1,"波動率");
```

---


---

## 腳本檔案: 指標/技術指標/變異數指標.xs

```xs
{@type:indicator}
input:length1(10,"短天期期別");
input:length2(20,"長天期期別");

value1=varianceps(close,length1,1);
value2=varianceps(close,length2,1);

plot1(value1,"短天期變異數");
plot2(value2,"長天期變異數");
```

---


---

## 腳本檔案: 指標/技術指標/逢低承接的力道.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/短線止跌的訊號/
收錄於「三週學會程式交易：打造你的第一筆自動化交易」 324頁
https://www.ipci.com.tw/books_in.php?book_id=724
}

input:
	short1(5,"短期平均"),
	mid1(20,"長期平均");

if truerange<>0 then begin
	if close<=open then 
		value1=(close-low)/truerange*100
	else
		value1=(open-low)/truerange*100;
end;

value2=average(value1,short1);
value3=average(value2,mid1);

plot1(value2,"短期均線");
plot2(value3,"長期均線");
```

---


---

## 腳本檔案: 指標/技術指標/進攻力道線.xs

```xs
{@type:indicator}
input:period(5,"期別");
value1=summationif(close>close[1],high-close[1],period);
plot1(value1,"進攻力道線");
```

---


---

## 腳本檔案: 指標/技術指標/隨機漫步指標.xs

```xs
{@type:indicator}

input:length(10);		setinputname(1, "天期");   

variable:RWIH(0),RWIL(0);   

value1 = standarddev(close,length,1);   
value2 = average(truerange,length);   
RWIH = (high-low[length-1])/value2*value1;   
RWIL = (high[length-1]-low)/value2*value1;   

plot1(RWIH - RWIL, "RWI");
```

---


---

## 腳本檔案: 指標/技術指標/順勢指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/為自己的觀察名單標上交易訊號/
}

input:
	length1(5,"短期平均"),
	length2(10,"長期平均");

variable:bp1(0),abp1(0),abp2(0);

bp1=(close-close[1])/truerange*100;
abp1=average(bp1,length1);
abp2=average(bp1,length2);

plot1(abp1,"短期平均");
plot2(abp2,"長期平均");
```

---


---

## 腳本檔案: 指標/期權指標/Delta.xs

```xs
{@type:indicator}
plot1(GetField("Delta"),"Delta");
```

---


---

## 腳本檔案: 指標/期權指標/Gamma.xs

```xs
{@type:indicator}
plot1(GetField("Gamma"),"Gamma");
```

---


---

## 腳本檔案: 指標/期權指標/Theta.xs

```xs
{@type:indicator}
plot1(GetField("Theta"),"Theta");
```

---


---

## 腳本檔案: 指標/期權指標/Vega.xs

```xs
{@type:indicator}
plot1(GetField("Vega"),"Vega");
```

---


---

## 腳本檔案: 指標/期權指標/三大法人交易金額.xs

```xs
{@type:indicator}
if symbolType<>3 and symbolType<>5 then raiseRunTimeError("僅支援期權");
if SymbolExchange <> "TF" then raiseRunTimeError("僅支援台灣市場");
if barFreq<>"d" then raiseRunTimeError("僅支援日線");

value1 = getField("三大法人交易買進金額");
value2 = getField("三大法人交易賣出金額");
value3 = value1 - value2;

plot1(value1,"三大法人交易買進金額");
plot2(value2,"三大法人交易賣出金額");
plot3(value3,"三大法人交易淨額");
```

---


---

## 腳本檔案: 指標/期權指標/價內外.xs

```xs
{@type:indicator}
variable:vRatio(0);

if symboltype <> 5 then 
	raiseruntimeerror("僅支援選擇權");

vRatio = iff(leftstr(getsymbolinfo("買賣權"),1)="C",1,-1)*(100*getsymbolfield("Underlying","收盤價")/getsymbolinfo("履約價")-100);

plot1(vRatio,"價內外%");
```

---


---

## 腳本檔案: 指標/期權指標/價差.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TF";//期貨
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
condition993 = symbolexchange = "TF" and symboltype = 5;//選擇權

if (condition999 = false and condition994 = true) or symbolType = 5	//僅支援期貨
	then raiseruntimeerror("不支援此商品");
	
if symbolexchange = "TF" and symboltype = 3  then	//期貨
	value1 = GetSymbolField("Underlying", "收盤價");	

plot1(close-value1,"價差");
```

---


---

## 腳本檔案: 指標/期權指標/台指選Delta.xs

```xs
{@type:indicator}
input: 
	iRate100(2,"無風險利率%"),
	iVolity100(20,"波動率%"),
	iHV(false, "波動率", inputkind:=dict(["標的20日歷史波動率",true],["固定波動率",false]));

variable:vStrikePrice(0),vVolity100(0);

if instr(symbol,".TF") = 0 or leftstr(symbol,1) = "F" or instr(symbol,"TX") = 0 then 
	raiseruntimeerror("僅支援台指選擇權");



if iHV then 
	vVolity100 = HVolatility(getsymbolfield("FITX*1.TF","收盤價","D"),20)
else 
	vVolity100 = iVolity100;

vStrikePrice = getsymbolinfo("履約價");

value1 = bsdelta(leftstr(getsymbolinfo("買賣權"),1),getsymbolfield("FITX*1.TF","收盤價"),vStrikePrice,daystoexpirationtf,iRate100,0,vVolity100);

plot1(value1,"Delta");
```

---


---

## 腳本檔案: 指標/期權指標/台指選IV.xs

```xs
{@type:indicator}
input: 
	iRate100(2,"無風險利率%");

variable:vStrikePrice(0);

if instr(symbol,".TF") = 0 or leftstr(symbol,1) = "F" or instr(symbol,"TX") = 0 then 
	raiseruntimeerror("僅支援台指選擇權");

vStrikePrice = getsymbolinfo("履約價");

value1 = ivolatility(leftstr(getsymbolinfo("買賣權"),1),getsymbolfield("FITX*1.TF","收盤價"),vStrikePrice,daystoexpirationtf,iRate100,0,c);

plot1(value1,"隱含波動率%");
```

---


---

## 腳本檔案: 指標/期權指標/台股指數近月外資未平倉.xs

```xs
{@type:indicator}
value1 = getsymbolfield("FITX*1.TF","外資買方未平倉口數");
value2 = getsymbolfield("FITX*1.TF","外資賣方未平倉口數");
value3 = value1 - value2;
plot1(value1,"外資未平倉買口");
plot2(value2,"外資未平倉賣口");
plot3(value3,"外資未平倉淨口");
```

---


---

## 腳本檔案: 指標/期權指標/台股指數近月投信未平倉.xs

```xs
{@type:indicator}
value1 = getsymbolfield("FITX*1.TF","投信買方未平倉口數");
value2 = getsymbolfield("FITX*1.TF","投信賣方未平倉口數");
value3 = value1 - value2;
plot1(value1,"投信未平倉買口");
plot2(value2,"投信未平倉賣口");
plot3(value3,"投信未平倉淨口");
```

---


---

## 腳本檔案: 指標/期權指標/台股指數近月自營商未平倉.xs

```xs
{@type:indicator}
value1 = getsymbolfield("FITX*1.TF","自營商買方未平倉口數");
value2 = getsymbolfield("FITX*1.TF","自營商賣方未平倉口數");
value3 = value1 - value2;
plot1(value1,"自營商未平倉買口");
plot2(value2,"自營商未平倉賣口");
plot3(value3,"自營商未平倉淨口");
```

---


---

## 腳本檔案: 指標/期權指標/外資交易金額.xs

```xs
{@type:indicator}
if symbolType<>3 and symbolType<>5 then raiseRunTimeError("僅支援期權");
if SymbolExchange <> "TF" then raiseRunTimeError("僅支援台灣市場");
if barFreq<>"d" then raiseRunTimeError("僅支援日線");

value1 = getField("外資交易買進金額");
value2 = getField("外資交易賣出金額");
value3 = value1 - value2;

plot1(value1,"外資交易買進金額");
plot2(value2,"外資交易賣出金額");
plot3(value3,"外資交易淨額");
```

---


---

## 腳本檔案: 指標/期權指標/外資期權動態.xs

```xs
{@type:indicator}
input:length(3,"期數");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

value1=GetField("外資交易買口");
value2=GetField("外資交易賣口");
value3=GetField("外資買方未平倉口數");
value4=GetField("外資賣方未平倉口數");
value5=value1-value2;//外資今日淨買賣口數
plot1(value5,"外資今日淨買賣口數");
plot2(average(value5,length),"移動平均");
```

---


---

## 腳本檔案: 指標/期權指標/委買委賣張數.xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 指標/期權指標/委買委賣筆數.xs

```xs
{@type:indicator}
{指標數值定義：(委買)筆數 = 交易所資料(開盤到目前累計(委買)筆數)
for 大盤,  委買委賣資料不含權證, 多一個成交筆數

支援商品：大盤/期貨/選擇權}

condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
	
if barfreq <> "Min" and barfreq <> "D" then 
	raiseruntimeerror("僅支援分鐘與日頻率");

if condition994 then begin//大盤
	value1 = GetField("累委買筆");
	value2 = GetField("累委賣筆");
	value3 = GetField("累委買筆") - GetField("累委賣筆");
	value4 = GetField("累成交筆");
	plot1(value3,"委買委賣筆數差");
	plot2(value1,"委買筆數",checkbox:=0);
	plot3(value2,"委賣筆數",checkbox:=0);
	plot4(value4,"累成交筆");
end else begin//期貨與選擇權
	value1 = GetField("累委買筆");
	value2 = GetField("累委賣筆");
	value3 = GetField("累委買筆") - GetField("累委賣筆");
	plot1(value3,"委買委賣筆數差");
	plot2(value1,"委買筆數",checkbox:=0);
	plot3(value2,"委賣筆數",checkbox:=0);
	noplot(4);
end;
```

---


---

## 腳本檔案: 指標/期權指標/投信交易金額.xs

```xs
{@type:indicator}
if symbolType<>3 and symbolType<>5 then raiseRunTimeError("僅支援期權");
if SymbolExchange <> "TF" then raiseRunTimeError("僅支援台灣市場");
if barFreq<>"d" then raiseRunTimeError("僅支援日線");

value1 = getField("投信交易買進金額");
value2 = getField("投信交易賣出金額");
value3 = value1 - value2;

plot1(value1,"投信交易買進金額");
plot2(value2,"投信交易賣出金額");
plot3(value3,"投信交易淨額");
```

---


---

## 腳本檔案: 指標/期權指標/摩台近月未平倉.xs

```xs
{@type:indicator}
value1 = getsymbolfield("STW*1.SG","未平倉");
plot1(value1,"摩台近月未平倉");
```

---


---

## 腳本檔案: 指標/期權指標/期貨散戶多空比.xs

```xs
{@type:indicator}
variable: OI_all(0), OI_small_bull(0), OI_small_bear(0), OI_small_ratio(0), OI_big_ratio(0);

OI_all = getsymbolfield("FITX*1.TF","未平倉","D") 
	+ getsymbolfield("FITX*2.TF","未平倉","D")
	+ getsymbolfield("FIMTX*1.TF","未平倉","D") * 0.25 
	+ getsymbolfield("FIMTX*2.TF","未平倉","D") * 0.25;
OI_small_bull = OI_all - getsymbolfield("FITX*1.TF","十大交易人未沖銷買口","D");
OI_small_bear = OI_all - getsymbolfield("FITX*1.TF","十大交易人未沖銷賣口","D");
if OI_small_bull + OI_small_bear = 0 then
	OI_small_ratio = 0
else
	OI_small_ratio = 100 * OI_small_bull / (OI_small_bull + OI_small_bear) - 50;
plot1(OI_small_ratio,"散戶");
```

---


---

## 腳本檔案: 指標/期權指標/溢價率.xs

```xs
{@type:indicator}
variable:vRatio(0);

if symboltype <> 5 then 
	raiseruntimeerror("僅支援選擇權");

vRatio = 100 * (
iff(leftstr(getsymbolinfo("買賣權"),1)="C",1,-1) * (getsymbolinfo("履約價") - getsymbolfield("Underlying","收盤價")) + close)
/getsymbolfield("Underlying","收盤價");

plot1(vRatio,"溢價率%");
```

---


---

## 腳本檔案: 指標/期權指標/自營商交易金額.xs

```xs
{@type:indicator}
if symbolType<>3 and symbolType<>5 then raiseRunTimeError("僅支援期權");
if SymbolExchange <> "TF" then raiseRunTimeError("僅支援台灣市場");
if barFreq<>"d" then raiseRunTimeError("僅支援日線");

value1 = getField("自營商交易買進金額");
value2 = getField("自營商交易賣出金額");
value3 = value1 - value2;

plot1(value1,"自營商交易買進金額");
plot2(value2,"自營商交易賣出金額");
plot3(value3,"自營商交易淨額");
```

---


---

## 腳本檔案: 指標/期權指標/買賣成交筆數.xs

```xs
{@type:indicator}
{指標數值定義："委買委賣成筆差 = 委賣成交筆數 - 委買成交筆數"
支援商品：期貨/選擇權}

if barfreq <> "Min" and barfreq <> "D" then 
	raiseruntimeerror("僅支援分鐘與日頻率");

value1 = GetField("累買成筆");
value2 = GetField("累賣成筆");
value3 = GetField("累賣成筆") - GetField("累買成筆");

plot1(value3,"委買委賣成筆差");
plot2(value1,"委買成筆",checkbox:=0);
plot3(value2,"委賣成筆",checkbox:=0);
```

---


---

## 腳本檔案: 指標/期權指標/選擇權理論價.xs

```xs
{@type:indicator}
input: 
	iRate100(2,"無風險利率%"),
	iHV(20,"標的歷史波動率計算期間");

variable:vStrikePrice(0),vVolity100(0),vTTMdays(0);

if symboltype <> 5 then 
	raiseruntimeerror("僅支援選擇權");

if iHV > 0 then 
	vVolity100 = HVolatility(getsymbolfield("Underlying","收盤價","D"),iHV)
else 
	vVolity100 = 20;

vStrikePrice = getsymbolinfo("履約價");
vTTMdays = DateDiff(GetSymbolInfo("到期日"), Date) + 1;

value1 = bsprice(leftstr(getsymbolinfo("買賣權"),1),getsymbolfield("Underlying","收盤價"),vStrikePrice,vTTMdays,iRate100,0,vVolity100);

plot1(value1,"理論價");
```

---


---

## 腳本檔案: 指標/期權指標/隱含波動率.xs

```xs
{@type:indicator}
input: 
	iRate100(2,"無風險利率%");

variable:vStrikePrice(0),vTTMdays(0);

if symboltype <> 5 then 
	raiseruntimeerror("僅支援選擇權");

vStrikePrice = getsymbolinfo("履約價");
vTTMdays = DateDiff(GetSymbolInfo("到期日"), Date) + 1;

value1 = ivolatility(leftstr(getsymbolinfo("買賣權"),1),getsymbolfield("Underlying","收盤價"),vStrikePrice,vTTMdays,iRate100,0,c);

plot1(value1,"隱含波動率%");
```

---


---

## 腳本檔案: 指標/籌碼指標/不明買盤指標.xs

```xs
{@type:indicator}
input:period(5,"期數");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
value1=GetField("法人買張");
value2=GetField("當日沖銷張數");
value3=GetField("散戶買張");
value4=volume-value1-value2-value3;
if volume <> 0 then
	value5=value4/volume;
value6=average(value5,period);
plot1(value6,"不明買盤比例");
```

---


---

## 腳本檔案: 指標/籌碼指標/主力作多成本線.xs

```xs
{@type:indicator}
input:period(40,"期數");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
value1=GetField("主力買張");
value2=(o+h+l+c)/4;

value3=value1*value2;//做多金額
 
if summation(value1,period)<>0 then
	value4=summation(value3,period)/summation(value1,period);
 
plot1(value4,"主力作多成本線");
```

---


---

## 腳本檔案: 指標/籌碼指標/主力成本線.xs

```xs
{@type:indicator}

{
	籌碼指標。
	支援日以上頻率。支援台股商品。
}

plot1(GetField("主力成本"),"主力成本線");//系統估算值。計算主力持股成本。
```

---


---

## 腳本檔案: 指標/籌碼指標/主力累計買賣超.xs

```xs
{@type:indicator}
input: Length(5); setinputname(1,"計算天數");
input:TXT("僅適用日線以上"); setinputname(2,"使用限制");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
variable: _buyTotal(0), volTotal(0), _Ratio(0);

_buyTotal = summation(GetField("主力買賣超張數"), Length);
volTotal = summation(Volume, Length);

if volTotal <> 0 then
	_Ratio = _buyTotal * 100 / volTotal
else
	_Ratio = 0;

Plot1(_buyTotal, "累計買賣超");
Plot2(_Ratio, "比例%");
```

---


---

## 腳本檔案: 指標/籌碼指標/主力買超佔成交量比重.xs

```xs
{@type:indicator}
input:length(5,"期數"),TXT("僅支援日線以上");
var:_strplot1("");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率，僅支援日線以上");

value4=getField("主力買賣超張數", "D");
if volume<>0 then 
value5=(summation(value4,length)/summation(volume,length))*100;

_strplot1 = text("近 ",numToStr(length,0)," 期，主力買超佔成交量比重");
plot1(value5,"主力買超佔成交量比重");
setplotLabel(1,_strplot1);
```

---


---

## 腳本檔案: 指標/籌碼指標/分公司交易家數差.xs

```xs
{@type:indicator}
input:period1(22,"MA天期");
input:period2(10,"差異MA天期");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

//狀況1.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量=0，則交易家數相關指標回傳0。
//狀況2.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量<>0，則交易家數相關指標正常運算。	
if getfieldDate("date") <> getfieldDate("分公司交易家數") and GetField("成交量") = 0 then value1 = 0 else value1=GetField("分公司交易家數");

value2=average(value1,period1);
value3=value1-value2;
value4=average(value3,period2);
plot1(value3,"分公司家數差");
plot2(value4,"家數差移動平均線");
```

---


---

## 腳本檔案: 指標/籌碼指標/分公司淨買賣超家數指標.xs

```xs
{@type:indicator}
if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

//狀況1.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量=0，則交易家數相關指標回傳0。
//狀況2.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量<>0，則交易家數相關指標正常運算。
if getfieldDate("date") <> getfieldDate("分公司淨買超金額家數") and GetField("成交量") = 0 then value1 = 0 else value1 = GetField("分公司淨買超金額家數");
if getfieldDate("date") <> getfieldDate("分公司淨賣超金額家數") and GetField("成交量") = 0 then value2 = 0 else value2 = GetField("分公司淨賣超金額家數");

value3=value2-value1;

plot1(value3,"家數差");
```

---


---

## 腳本檔案: 指標/籌碼指標/分公司買賣家數指標.xs

```xs
{@type:indicator}
if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

//狀況1.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量=0，則交易家數相關指標回傳0。
//狀況2.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量<>0，則交易家數相關指標正常運算。
if getfieldDate("date") <> getfieldDate("分公司買進家數") and GetField("成交量") = 0 then value1 = 0 else value1=GetField("分公司買進家數");
if getfieldDate("date") <> getfieldDate("分公司賣出家數") and GetField("成交量") = 0 then value2 = 0 else value2=GetField("分公司賣出家數");

value3=value2-value1;

plot1(value3,"家數差");
```

---


---

## 腳本檔案: 指標/籌碼指標/外資成本線.xs

```xs
{@type:indicator}

{
	籌碼指標。
	支援日以上頻率。支援台股商品。
}

plot1(GetField("外資成本"),"外資成本線");//系統估算值。計算外資持股成本。
```

---


---

## 腳本檔案: 指標/籌碼指標/外資換手比例.xs

```xs
{@type:indicator}
input: Length(5); setinputname(1,"計算天數");
input:TXT("僅適用日線以上"); setinputname(2,"使用限制");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
variable: _buyTotal(0), volTotal(0);

_buyTotal = summation(GetField("外資買張") + GetField("外資賣張"), Length);
volTotal = summation(Volume * 2, Length);

Plot1(_buyTotal, "換手張數");
Plot2(_buyTotal * 100 / volTotal, "比例%");
```

---


---

## 腳本檔案: 指標/籌碼指標/外資累計買賣超.xs

```xs
{@type:indicator}
input: Length(5); setinputname(1,"計算天數");
input:TXT("僅適用日線以上"); setinputname(2,"使用限制");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
variable: _buyTotal(0), volTotal(0), _Ratio(0);

_buyTotal = summation(GetField("外資買賣超"), Length);
volTotal = summation(Volume, Length);

if volTotal <> 0 then
	_Ratio = _buyTotal * 100 / volTotal
else
	_Ratio = 0;

Plot1(_buyTotal, "累計買賣超");
Plot2(_Ratio, "比例%");
```

---


---

## 腳本檔案: 指標/籌碼指標/外資買超佔成交量比重.xs

```xs
{@type:indicator}
input:length(5,"期數"),TXT("僅支援日線以上");
var:_strplot1("");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率，僅支援日線以上");

value4=getField("外資買賣超張數", "D");
if volume<>0 then 
value5=(summation(value4,length)/summation(volume,length))*100;

_strplot1 = text("近 ",numToStr(length,0)," 期，外資買超佔成交量比重");
plot1(value5,"外資買超佔成交量比重");
setplotLabel(1,_strplot1);
```

---


---

## 腳本檔案: 指標/籌碼指標/多空淨力場.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/自訂指標step-by-step/
}

input:sd(5,"短天期");
input:ld(20,"長天期");

variable:H1(0),L1(0),C1(0),NF(0),SNF(0),LNF(0),dd(0);

H1=HIGH-HIGH[1];
L1=LOW-LOW[1];
C1=CLOSE-CLOSE[1];

if truerange<>0 then begin
	NF=(H1+L1)/truerange;
	SNF=average(NF,sd);
	LNF=average(NF,ld);
	dd=SNF-LNF;
end;

plot1(dd,"多空淨力");
```

---


---

## 腳本檔案: 指標/籌碼指標/大戶買張比例.xs

```xs
{@type:indicator}
input:period1(5,"短移動平均線天期");
input:period2(20,"長移動平均線天期");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
value1=GetField("主力買張");
value2=GetField("實戶買張");
value3=GetField("散戶買張");
value4=GetField("控盤者買張");
value5=GetField("法人買張");
value6=value1+value2+value3+value4+value5;
//合計的買張數當分母，這有可能超出成交量
value7=value1+value4+value5;
//主力+法人+控盤者的買張合計作為大戶的買張
if value6<>0 then
	value8=value7/value6*100;
//計算大戶買張佔各方勢力買張的比例
value9=average(value8,period1)-average(value8,period2);
plot1(value9,"大戶買張比例");
```

---


---

## 腳本檔案: 指標/籌碼指標/實戶累計買賣超.xs

```xs
{@type:indicator}
input: Length(5); setinputname(1,"計算天數");
input:TXT("僅適用日線以上"); setinputname(2,"使用限制");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
variable: _buyTotal(0), volTotal(0);

_buyTotal = summation(GetField("實戶買賣超張數"), Length);
volTotal = summation(Volume, Length);

Plot1(_buyTotal, "累計買賣超");
Plot2(_buyTotal * 100 / volTotal, "比例%");
```

---


---

## 腳本檔案: 指標/籌碼指標/投信成本線.xs

```xs
{@type:indicator}

{
	籌碼指標。
	支援日以上頻率。支援台股商品。
}

plot1(GetField("投信成本"),"投信成本線");//系統估算值。計算投信持股成本。
```

---


---

## 腳本檔案: 指標/籌碼指標/投信累計買賣超.xs

```xs
{@type:indicator}
input: Length(5); setinputname(1,"計算天數");
input:TXT("僅適用日線以上"); setinputname(2,"使用限制");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
variable: _buyTotal(0), volTotal(0);

_buyTotal = summation(GetField("投信買賣超"), Length);
volTotal = summation(Volume, Length);

Plot1(_buyTotal, "累計買賣超");
Plot2(_buyTotal * 100 / volTotal, "比例%");
```

---


---

## 腳本檔案: 指標/籌碼指標/投信買超佔成交量比重.xs

```xs
{@type:indicator}
input:length(5,"期數"),TXT("僅支援日線以上");
var:_strplot1("");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率，僅支援日線以上");

value4=getField("投信買賣超張數", "D");
if volume<>0 then 
value5=(summation(value4,length)/summation(volume,length))*100;

_strplot1 = text("近 ",numToStr(length,0)," 期，投信買超佔成交量比重");
plot1(value5,"投信買超佔成交量比重");
setplotLabel(1,_strplot1);
```

---


---

## 腳本檔案: 指標/籌碼指標/控盤者成本線.xs

```xs
{@type:indicator}
if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
value1=GetField("控盤者成本線");
plot1(value1,"控盤者成本線");
```

---


---

## 腳本檔案: 指標/籌碼指標/放空佔成交均量倍數.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/借券相關欄位在交易策略上的應用/
}

if barfreq <> "D" then raiseruntimeerror("不支援此頻率");

value1=GetField("借券餘額張數","D");
value2=GetField("融券餘額張數","D");
if volume<>0 then 
	value3=(value1+value2)/average(volume,20);
plot1(value3,"放空佔成交均量倍數");
```

---


---

## 腳本檔案: 指標/籌碼指標/散戶作多指標.xs

```xs
{@type:indicator}
input:Period(10,"MA期數");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
value1=GetField("融資買進張數");
value2=GetField("融券買進張數");
if volume <> 0 then
	value3=(value1+value2)/volume;
value4=average(value3,Period);

plot1(value4,"散戶作多指標");
```

---


---

## 腳本檔案: 指標/籌碼指標/散戶買進比例.xs

```xs
{@type:indicator}
input:Period(5,"MA期數");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
value1=GetField("散戶買張");
if volume<>0 then 
	value2=value1/volume*100;
value3=average(value2,Period);

plot1(value3,"散戶買進比例");
```

---


---

## 腳本檔案: 指標/籌碼指標/散戶賣出比例.xs

```xs
{@type:indicator}
input:Period(5,"MA期數");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
value1=GetField("散戶賣張");
if volume<>0 then 
	value2=value1/volume*100;
value3=average(value2,Period);

plot1(value3,"散戶賣出比例");
```

---


---

## 腳本檔案: 指標/籌碼指標/整體籌碼收集指標.xs

```xs
{@type:indicator}
input:Period(5,"MA期數");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
value1=GetField("現股當沖張數","D");
value2=GetField("外資買賣超","D");
value3=GetField("投信買賣超","D");
value4=GetField("自營商買賣超","D");
value5=GetField("主力買賣超張數","D");
value6=GetField("融資增減張數","D");
value7=GetField("融券增減張數","D");
value8=volume-value1;//當日淨交易張數
value9=value2+value3+value4+value5-value6+value7;

//籌碼收集張數
if value8<>0 then 
	value10=value9/value8*100
else
	value10=value10[1];

value11=average(value10,Period);
plot1(value11,"集中度");
```

---


---

## 腳本檔案: 指標/籌碼指標/法人累計買賣超.xs

```xs
{@type:indicator}
input: Length(5); setinputname(1,"計算天數");
input:TXT("僅適用日線以上"); setinputname(2,"使用限制");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
variable: _buyTotal(0), volTotal(0);

_buyTotal = summation(GetField("法人買賣超張數"), Length);
volTotal = summation(Volume, Length);

Plot1(_buyTotal, "累計買賣超");
Plot2(_buyTotal * 100 / volTotal, "比例%");
```

---


---

## 腳本檔案: 指標/籌碼指標/法人買超佔成交量比重.xs

```xs
{@type:indicator}
input:length(5,"期數"),TXT("僅支援日線以上");
var:_strplot1("");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率，僅支援日線以上");

value4=getField("法人買賣超", "D");
if volume<>0 then 
value5=(summation(value4,length)/summation(volume,length))*100;

_strplot1 = text("近 ",numToStr(length,0)," 期，法人買超佔成交量比重");
plot1(value5,"法人買超佔成交量比重");
setplotLabel(1,_strplot1);
```

---


---

## 腳本檔案: 指標/籌碼指標/法人買進及賣出比例.xs

```xs
{@type:indicator}
if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
value1=GetField("外資買張");
value2=GetField("外資賣張");
value3=GetField("投信買張");
value4=GetField("投信賣張");
value5=value1+value3;
value6=value2+value4;
if volume <> 0 then begin
	value7=value5/volume*100;
	value8=value6/volume*100;
end;

plot1(value7,"法人買進比例");
plot2(value8,"法人賣出比例");
```

---


---

## 腳本檔案: 指標/籌碼指標/法人買進比例.xs

```xs
{@type:indicator}
{
指標說明
收錄於「三週學會程式交易：打造你的第一筆自動化交易」 326頁
https://www.ipci.com.tw/books_in.php?book_id=724
}

input:length1(5,"短天期均線天期");
input:length2(20,"長天期均線天期");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
value1=GetField("法人買張");
if volume<>0 then value2=value1/volume*100;
//法人買張佔成交量比例
value3 = Average(value2,length1);
value4 = Average(value2,length2);
plot1(value3,"短期均線");
plot2(value4,"長期均線");
```

---


---

## 腳本檔案: 指標/籌碼指標/股東人數.xs

```xs
{@type:indicator}
//說明：
//交易所公布的總持股人數。
//執行商品為股票時，支援「週」以上的頻率。
//執行商品為可轉債時，支援「月」以上的頻率。

condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and (symboltype = 2 or symbolType = 1 or symboltype = 6);//個股+類股+可轉債

if condition998 = false //個股+興櫃+類股
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

if symboltype = 2 or symbolType = 1 then begin
	if barFreq = "D" then
		value1 = GetField("總持股人數","W")
	else
		value1 = GetField("總持股人數");
end;

if symboltype = 6 then begin
	if barFreq = "D" or barFreq = "W"  then
		value1 = GetField("總持股人數","M")
	else
		value1 = GetField("總持股人數");
end;

plot1(value1,"總持股人數");
```

---


---

## 腳本檔案: 指標/籌碼指標/自營商成本線.xs

```xs
{@type:indicator}

{
	籌碼指標。
	支援日以上頻率。支援台股商品。
}

plot1(GetField("自營商成本"),"自營商成本線");//系統估算值。計算自營商持股成本。
```

---


---

## 腳本檔案: 指標/籌碼指標/自營商累計買賣超.xs

```xs
{@type:indicator}
input: Length(5); setinputname(1,"計算天數");
input:TXT("僅適用日線以上"); setinputname(2,"使用限制");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
variable: _buyTotal(0), volTotal(0);

_buyTotal = summation(GetField("自營商買賣超"), Length);
volTotal = summation(Volume, Length);

Plot1(_buyTotal, "累計買賣超");
Plot2(_buyTotal * 100 / volTotal, "比例%");
```

---


---

## 腳本檔案: 指標/籌碼指標/自營商買超佔成交量比重.xs

```xs
{@type:indicator}
input:length(5,"期數"),TXT("僅支援日線以上");
var:_strplot1("");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率，僅支援日線以上");

value4=getField("自營商買賣超", "D");
if volume<>0 then 
value5=(summation(value4,length)/summation(volume,length))*100;

_strplot1 = text("近 ",numToStr(length,0)," 期，自營商買超佔成交量比重");
plot1(value5,"自營商買超佔成交量比重");
setplotLabel(1,_strplot1);
```

---


---

## 腳本檔案: 指標/籌碼指標/融資累計張數.xs

```xs
{@type:indicator}
input: Length(5); setinputname(1,"計算天數");
input:TXT("僅適用日線以上"); setinputname(2,"使用限制");

variable: _buyTotal(0), volTotal(0);

_buyTotal = summation(GetField("融資增減張數"), Length);
volTotal = summation(Volume, Length);

Plot1(_buyTotal, "累計增減");
Plot2(_buyTotal * 100 / volTotal, "比例%");
```

---


---

## 腳本檔案: 指標/籌碼指標/資金流向.xs

```xs
{@type:indicator}
{
指標說明
收錄於「三週學會程式交易：打造你的第一筆自動化交易」 327頁
https://www.ipci.com.tw/books_in.php?book_id=724
}

input:
	short1(5,"短期平均"),
	mid1(12,"長期平均");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
value1=GetField("資金流向");
value2=average(value1,20);
value3=value1-value2;
value4=average(value3,short1);
value5=average(value3,mid1);

plot1(value4,"短期均線");
plot2(value5,"長期均線");
```

---


---

## 腳本檔案: 指標/籌碼高手/CB剩餘張數.xs

```xs
{@type:indicator}
if SymbolType <> 6 then RaiseRunTimeError("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

if barFreq = "D" then
	value1 = getField("CB剩餘張數","w")
else
	value1 = GetField("CB剩餘張數");

plot1(value1,"CB剩餘張數");
```

---


---

## 腳本檔案: 指標/籌碼高手/CB轉換溢價率.xs

```xs
{@type:indicator}
{
	支援商品：可轉債商品。
	支援頻率：分鐘以上的頻率。
	繪圖序列1是「可轉債轉換溢價率」的線條。
}
if SymbolType <> 6 then RaiseRunTimeError("不支援此商品");
if GetSymbolInfo("轉換價格") <> 0 then	//避免分母為0
	value1 = (100 / GetSymbolInfo("轉換價格")) * GetSymbolField("Underlying", "收盤價");//轉換價值 = (100 / 轉換價格) x 股票現價
if value1 <> 0 then
	value2 = (close - value1)/value1;//轉換溢價率(%) = (CB價格 - 轉換價值) / 轉換價值
	
plot1(value2,"轉換溢價率");
```

---


---

## 腳本檔案: 指標/籌碼高手/三方買盤.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and symboltype = 2;//個股+興櫃

if condition998 = false //個股+興櫃
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

plot1(GetField("散戶買張"),"散戶買進(張)",axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
plot2(GetField("實戶買張"),"實戶買進(張)",axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
plot3(GetField("控盤者買張"),"控盤者買進(張)",axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
```

---


---

## 腳本檔案: 指標/籌碼高手/三方賣盤.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and symboltype = 2;//個股+興櫃

if condition998 = false //個股+興櫃
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

plot1(GetField("散戶賣張"),"散戶賣出(張)",axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
plot2(GetField("實戶賣張"),"實戶賣出(張)",axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
plot3(GetField("控盤者賣張"),"控盤者賣出(張)",axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
```

---


---

## 腳本檔案: 指標/籌碼高手/主力進出.xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 指標/籌碼高手/借券.xs

```xs
{@type:indicator}
//借券餘額市值公式參考：
//http://www.twse.com.tw/ch/trading/SBL/TWT72U/TWT72U.php

condition996 = symbolexchange = "TW" = true and symboltype = 2;//個股
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤

if condition994 = false and condition996 = false //大盤+個股
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

if symboltype = 1 then begin
	plot1(GetField("借券賣出餘額張數"),"借券賣出餘額(張)",axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);			//單位：張
	plot2(GetField("借券餘額張數"),"借券餘額(張)",axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);				//單位：張
	//plot3(GetField("借券餘額張數")*1000*close,"借券餘額市值(元)",axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);	//單位：元，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
end else begin
	plot1(GetField("借券賣出餘額張數"),"借券賣出餘額(張)",axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);			//單位：張
	plot2(GetField("借券餘額張數"),"借券餘額(張)",axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);				//單位：張
	plot3(GetField("借券餘額張數")*1000*close,"借券餘額市值(元)",axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);	//單位：元，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
end;
```

---


---

## 腳本檔案: 指標/籌碼高手/借券賣出.xs

```xs
{@type:indicator}
condition996 = symbolexchange = "TW" = true and symboltype = 2;//個股
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤

if condition994 = false and condition996 = false //大盤+個股
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

if symboltype = 1 then begin
	plot1(GetField("借券賣出餘額張數"),"借券賣出餘額(張)",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張
	plot2(GetField("借券賣出張數")+GetField("借券賣出庫存異動張數"),"差額(張)",checkbox:=1,axis:=2);//增減bar，請RD加"借券還券"與"借券調整"
	plot3(GetField("借券賣出張數"),"賣出(張)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
	plot4(GetField("借券賣出庫存異動張數"),"還券(張)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//請RD加
end else begin
	plot1(GetField("借券賣出餘額張數"),"借券賣出餘額(張)",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
	plot2(GetField("借券賣出張數")+GetField("借券賣出庫存異動張數"),"差額(張)",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//增減bar，請RD加"借券還券"與"借券調整"
	plot3(GetField("借券賣出張數"),"賣出(張)",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
	plot4(GetField("借券賣出庫存異動張數"),"還券(張)",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);//請RD加
end;
```

---


---

## 腳本檔案: 指標/籌碼高手/借券餘額.xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 指標/籌碼高手/內部人持股.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and symboltype = 2;//個股+興櫃

if condition998 = false //個股+興櫃+類股
	then raiseruntimeerror("不支援此商品");


if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

plot1(0.01*Getfield("內部人持股比例","M"),"內部人持股比例",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//請RD加
plot2(Getfield("內部人持股張數","M"),"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
```

---


---

## 腳本檔案: 指標/籌碼高手/內部人持股異動.xs

```xs
{@type:indicator}
{支援頻率：日、週、月}
{支援商品：美(股票)}

if barfreq <> "d" and barfreq <> "w" and barfreq <> "m" then raiseruntimeerror("不支援此頻率");

var:exchange("");
exchange = GetSymbolInfo("交易所");
if exchange <> "NYSE" and exchange <> "NASDAQ" and exchange <> "AMEX" then raiseruntimeerror("僅支援美股");

plot1(Getfield("內部人持股異動"),"內部人持股異動",Checkbox:=1);//計算內部人的交易總股數
plot2(Getfield("內部人持股"),"內部人持股",Checkbox:=0);//計算有持股異動的內部人總股數
```

---


---

## 腳本檔案: 指標/籌碼高手/分公司交易家數.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition997 = condition999 and (symboltype = 2 or symboltype = 4);//個股+權證+興櫃

if condition997 = false //個股+權證+興櫃
	then raiseruntimeerror("不支援此商品");

if barfreq <> "D" and barfreq <> "AD" 
	then raiseruntimeerror("不支援此頻率");

//狀況1.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量=0，則交易家數相關指標回傳0。
//狀況2.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量<>0，則交易家數相關指標正常運算。
if getfieldDate("date") <> getfieldDate("分公司交易家數") and GetField("成交量") = 0 then value11 = 0 else value11 = GetField("分公司交易家數");
if getfieldDate("date") <> getfieldDate("分公司買進家數") and GetField("成交量") = 0 then value21 = 0 else value21 = GetField("分公司買進家數");
if getfieldDate("date") <> getfieldDate("分公司賣出家數") and GetField("成交量") = 0 then value31 = 0 else value31 = GetField("分公司賣出家數");
if GetField("市場總分點數") <> 0 then value1 = value11/GetField("市場總分點數");
plot1(value11,"交易家數",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：家
plot2(value1,"參與率",checkbox:=0,axis:=2,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
plot3(value21,"買進家數",checkbox:=0,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：家，可勾選畫圖選項 (參數設定) 
plot4(value31,"賣出家數",checkbox:=0,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：家，可勾選畫圖選項 (參數設定)
```

---


---

## 腳本檔案: 指標/籌碼高手/分公司淨買賣金額家數.xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 指標/籌碼高手/分公司買進賣出家數.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition992 = condition999 and  (symbol <> "TSE.TW" and symbol <> "TWSE.FS" and symbol <> "OTC.TW");//類股+個股+權證+興櫃

if condition992 = false //類股+個股+權證+興櫃
	then raiseruntimeerror("不支援此商品");

if barfreq <> "D" and barfreq <> "AD" 
	then raiseruntimeerror("不支援此頻率");

//狀況1.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量=0，則交易家數相關指標回傳0。
//狀況2.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量<>0，則交易家數相關指標正常運算。
if getfieldDate("date") <> getfieldDate("分公司買進家數") and GetField("成交量") = 0 then value1 = 0 else value1 = GetField("分公司買進家數");
if getfieldDate("date") <> getfieldDate("分公司賣出家數") and GetField("成交量") = 0 then value2 = 0 else value2 = GetField("分公司賣出家數");

plot1(value2-value1,"家數差",checkbox:=1,axis:=2);//單位：家
plot2(value1,"買進",checkbox:=0,axis:=1);//單位：家，可勾選畫圖選項 (參數設定) 
plot3(value2,"賣出",checkbox:=0,axis:=1);//單位：家，可勾選畫圖選項 (參數設定)
```

---


---

## 腳本檔案: 指標/籌碼高手/券資比.xs

```xs
{@type:indicator}
condition996 = symbolexchange = "TW" and symboltype = 2;//個股
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
condition993 = symbolexchange = "TW" and symboltype = 1;//類股

if condition994 =false and condition993 = false and condition996 = false //大盤+類股+個股
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

if symboltype = 1 then begin
	plot1(0.01 * GetField("券資比"),"券資比",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位：
	plot2(GetField("融券餘額張數"),"融券餘額",axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
	plot3(GetField("融資餘額"),"融資餘額",axis:=12,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
end else begin
	plot1(0.01 * GetField("券資比"),"券資比",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位：
	plot2(GetField("融券餘額張數"),"融券餘額",axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
	plot3(GetField("融資餘額"),"融資餘額",axis:=12,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
end;
```

---


---

## 腳本檔案: 指標/籌碼高手/吉尼系數.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and symboltype = 2;//個股+興櫃

if condition998 = false //個股+興櫃
	then raiseruntimeerror("不支援此商品");

if barfreq <> "D" and barfreq <> "AD" 
	then raiseruntimeerror("不支援此頻率");

plot1(Getfield("吉尼係數","D"),"吉尼係數",axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd2);

//狀況1.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量=0，則交易家數相關指標回傳0。
//狀況2.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量<>0，則交易家數相關指標正常運算。	
if getfieldDate("date") <> getfieldDate("分公司交易家數") and GetField("成交量") = 0 then value1 = 0 else value1=GetField("分公司交易家數");
plot2(value1,"分公司交易家數",axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：家
```

---


---

## 腳本檔案: 指標/籌碼高手/地緣券商買賣超.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW";//台股

if condition999 = false //個股
	then raiseruntimeerror("不支援此商品");

if barfreq <> "D" and barfreq <> "AD"
	then raiseruntimeerror("不支援此頻率");

value1 = GetField("地緣券商買賣超張數");
value2 += value1;
plot1(value1,"買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //bar，axis2
plot2(value2,"地緣券商累計買賣超",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //line，axis1
```

---


---

## 腳本檔案: 指標/籌碼高手/外資.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
condition993 = symbolexchange = "TW" and symboltype = 1;//類股

if condition999 = false and condition994 = false//大盤, 個股, 權證, 興櫃, 類股指數
	then raiseruntimeerror("不支援此商品");


if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

if condition994 then begin
	value1 = GetField("外資買進金額");
	value2 = GetField("外資賣出金額");
	value3 = GetField("外資買賣超金額");
	value4 = value4 + GetField("外資買賣超金額");
	plot2(value4,"外資累計買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis1
	setplotlabel(1,"買賣超(元)");
	setplotlabel(2,"外資累計買賣超(元)");
	setplotlabel(3,"買進(元)");
	setplotlabel(4,"賣出(元)");
	plot1(value3,"買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //bar，axis2
	plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
	plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
end else 
begin
	if symbolexchange <> "TE" and condition993 = false and date >= 20110106 then begin
		value1 = GetField("外資買張");
		value2 = GetField("外資賣張");
	end;
	value3 = GetField("外資買賣超張數");
	plot2(GetField("外資持股"),"外資持股",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis1
	setplotlabel(1,"買賣超(張)");
	setplotlabel(2,"外資持股(張)");
	setplotlabel(3,"買進(張)");
	setplotlabel(4,"賣出(張)");
	if condition993 = false then begin
		plot5(0.01*GetField("外資持股比例"),"外資持股比例",axis:=12,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
	end;
	plot1(value3,"買賣超",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0); //bar，axis2
	if symbolexchange <> "TE" and condition993 = false then begin
		plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis2
		plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis2
	end;
end;
```

---


---

## 腳本檔案: 指標/籌碼高手/外資持股比例.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and symboltype = 2;//個股+興櫃

if condition998 = false //個股+興櫃
	then raiseruntimeerror("不支援此商品");



if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
plot1(0.01*GetField("外資持股比例"),"外資持股比例",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
```

---


---

## 腳本檔案: 指標/籌碼高手/大戶持股.xs

```xs
{@type:indicator}
{由集保公司所提供的，「指定級距以上」的持股資料所計算}

input: _input1(50,"大戶標準",inputkind:= Dict(["1",1],["5",5],["10",10],["15",15],["20",20],["30",30],["40",40],["50",50],["100",100],["200",200],["400",400],["600",600],["800",800],["1000",1000]),quickedit:=true);

condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and (symboltype = 2 or symbolType = 1);//個股+興櫃+類股

if condition998 = false //個股+興櫃+類股
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
switch (_input1)
begin
	case 1:
		if barFreq = "D" then begin
			value1 = Getfield("大戶持股比例","W",param:=1);
			value2 = Getfield("大戶持股張數","W",param:=1);
			value3 = Getfield("大戶持股人數","W",param:=1);
		end else begin
			value1 = Getfield("大戶持股比例",param:=1);
			value2 = Getfield("大戶持股張數",param:=1);
			value3 = Getfield("大戶持股人數",param:=1);
		end;	
		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
		
	case 5:
		if barFreq = "D" then begin
			value1 = Getfield("大戶持股比例","W",param:=5);
			value2 = Getfield("大戶持股張數","W",param:=5);
			value3 = Getfield("大戶持股人數","W",param:=5);
		end else begin
			value1 = Getfield("大戶持股比例",param:=5);
			value2 = Getfield("大戶持股張數",param:=5);
			value3 = Getfield("大戶持股人數",param:=5);
		end;	
		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);

	case 10:
		if barFreq = "D" then begin
			value1 = Getfield("大戶持股比例","W",param:=10);
			value2 = Getfield("大戶持股張數","W",param:=10);
			value3 = Getfield("大戶持股人數","W",param:=10);
		end else begin
			value1 = Getfield("大戶持股比例",param:=10);
			value2 = Getfield("大戶持股張數",param:=10);
			value3 = Getfield("大戶持股人數",param:=10);
		end;	
		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
			
	case 15:
		if barFreq = "D" then begin
			value1 = Getfield("大戶持股比例","W",param:=15);
			value2 = Getfield("大戶持股張數","W",param:=15);
			value3 = Getfield("大戶持股人數","W",param:=15);
		end else begin
			value1 = Getfield("大戶持股比例",param:=15);
			value2 = Getfield("大戶持股張數",param:=15);
			value3 = Getfield("大戶持股人數",param:=15);
		end;	
		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
		
	case 20:
		if barFreq = "D" then begin
			value1 = Getfield("大戶持股比例","W",param:=20);
			value2 = Getfield("大戶持股張數","W",param:=20);
			value3 = Getfield("大戶持股人數","W",param:=20);
		end else begin
			value1 = Getfield("大戶持股比例",param:=20);
			value2 = Getfield("大戶持股張數",param:=20);
			value3 = Getfield("大戶持股人數",param:=20);
		end;	
		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
		
	case 30:
		if barFreq = "D" then begin
			value1 = Getfield("大戶持股比例","W",param:=30);
			value2 = Getfield("大戶持股張數","W",param:=30);
			value3 = Getfield("大戶持股人數","W",param:=30);
		end else begin
			value1 = Getfield("大戶持股比例",param:=30);
			value2 = Getfield("大戶持股張數",param:=30);
			value3 = Getfield("大戶持股人數",param:=30);
		end;	
		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
	
	case 40:
		if barFreq = "D" then begin
			value1 = Getfield("大戶持股比例","W",param:=40);
			value2 = Getfield("大戶持股張數","W",param:=40);
			value3 = Getfield("大戶持股人數","W",param:=40);
		end else begin
			value1 = Getfield("大戶持股比例",param:=40);
			value2 = Getfield("大戶持股張數",param:=40);
			value3 = Getfield("大戶持股人數",param:=40);
		end;	
		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
		
	case 50:
		if barFreq = "D" then begin
			value1 = Getfield("大戶持股比例","W",param:=50);
			value2 = Getfield("大戶持股張數","W",param:=50);
			value3 = Getfield("大戶持股人數","W",param:=50);
		end else begin
			value1 = Getfield("大戶持股比例",param:=50);
			value2 = Getfield("大戶持股張數",param:=50);
			value3 = Getfield("大戶持股人數",param:=50);
		end;
		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);

	case 100:
		if barFreq = "D" then begin
			value1 = Getfield("大戶持股比例","W",param:=100);
			value2 = Getfield("大戶持股張數","W",param:=100);
			value3 = Getfield("大戶持股人數","W",param:=100);
		end else begin
			value1 = Getfield("大戶持股比例",param:=100);
			value2 = Getfield("大戶持股張數",param:=100);
			value3 = Getfield("大戶持股人數",param:=100);
		end;
		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
		
	case 200:
		if barFreq = "D" then begin
			value1 = Getfield("大戶持股比例","W",param:=200);
			value2 = Getfield("大戶持股張數","W",param:=200);
			value3 = Getfield("大戶持股人數","W",param:=200);
		end else begin
			value1 = Getfield("大戶持股比例",param:=200);
			value2 = Getfield("大戶持股張數",param:=200);
			value3 = Getfield("大戶持股人數",param:=200);
		end;
		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
		
	case 400:
		if barFreq = "D" then begin
			value1 = Getfield("大戶持股比例","W",param:=400);
			value2 = Getfield("大戶持股張數","W",param:=400);
			value3 = Getfield("大戶持股人數","W",param:=400);
		end else begin
			value1 = Getfield("大戶持股比例",param:=400);
			value2 = Getfield("大戶持股張數",param:=400);
			value3 = Getfield("大戶持股人數",param:=400);
		end;
		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
	
	case 600:
		if barFreq = "D" then begin
			value1 = Getfield("大戶持股比例","W",param:=600);
			value2 = Getfield("大戶持股張數","W",param:=600);
			value3 = Getfield("大戶持股人數","W",param:=600);
		end else begin
			value1 = Getfield("大戶持股比例",param:=600);
			value2 = Getfield("大戶持股張數",param:=600);
			value3 = Getfield("大戶持股人數",param:=600);
		end;
		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
		
	case 800:
		if barFreq = "D" then begin
			value1 = Getfield("大戶持股比例","W",param:=800);
			value2 = Getfield("大戶持股張數","W",param:=800);
			value3 = Getfield("大戶持股人數","W",param:=800);
		end else begin
			value1 = Getfield("大戶持股比例",param:=800);
			value2 = Getfield("大戶持股張數",param:=800);
			value3 = Getfield("大戶持股人數",param:=800);
		end;
		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
	
	default:
		if barFreq = "D" then begin
			value1 = Getfield("大戶持股比例","W",param:=1000);
			value2 = Getfield("大戶持股張數","W",param:=1000);
			value3 = Getfield("大戶持股人數","W",param:=1000);
		end else begin
			value1 = Getfield("大戶持股比例",param:=1000);
			value2 = Getfield("大戶持股張數",param:=1000);
			value3 = Getfield("大戶持股人數",param:=1000);
		end;
		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);

end;
```

---


---

## 腳本檔案: 指標/籌碼高手/大盤法人比重.xs

```xs
{@type:indicator}
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤

if condition994 = false //大盤
	then raiseruntimeerror("不支援此商品");

if barfreq <> "D" and barfreq <> "AD" and
	barfreq <> "W" and barfreq <> "AW" and
	barfreq <> "M" and barfreq <> "AM"
	then raiseruntimeerror("不支援此頻率");
	
plot1(0.005*(GetField("法人買進比重")+GetField("法人賣出比重")),"交易比重",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
plot2(0.01*GetField("法人買進比重"),"買進比重",checkbox:=0,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
plot3(0.01*GetField("法人賣出比重"),"賣出比重",checkbox:=0,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
```

---


---

## 腳本檔案: 指標/籌碼高手/官股券商.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and (symboltype = 2 or symboltype = 1);//個股+興櫃+類股
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤

if condition994 =false and condition998 = false //大盤+個股+興櫃+類股
	then raiseruntimeerror("不支援此商品");

if barfreq <> "D" and barfreq <> "AD"
	then raiseruntimeerror("不支援此頻率");

if condition994 then begin
	value1 = GetField("官股券商買進金額");
	value2 = GetField("官股券商賣出金額");
	value3 = value1 - value2;
	value4 = GetField("官股券商累計買賣超金額");
	setplotlabel(1,"買賣超(元)");
	setplotlabel(2,"累計買賣超(元)");
	setplotlabel(3,"買進(元)");
	setplotlabel(4,"賣出(元)");
	plot1(value3,"買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //bar，axis2
	plot1(value3,"買賣超"); //bar，axis2
	plot2(value4,"官股券商累計買賣超",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis1
	plot3(value1,"買進(元)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
	plot4(value2,"賣出(元)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
end else if condition994 = false then begin
	value1 = GetField("官股券商買進金額");
	value2 = GetField("官股券商賣出金額");
	value3 = GetField("官股券商買賣超張數");
	value4 = value4 + value3;
	setplotlabel(1,"買賣超(張)");
	setplotlabel(2,"累計買賣超(張)");
	setplotlabel(3,"買進(張)");
	setplotlabel(4,"賣出(張)");
	plot1(value3,"買賣超(張)",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //bar，axis2
	plot2(value4,"官股券商累計買賣超(張)",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //line，axis1
	plot3(value1,"買進(張)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
	plot4(value2,"賣出(張)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
end;
```

---


---

## 腳本檔案: 指標/籌碼高手/實戶買賣盤.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and symboltype = 2;//個股+興櫃

if condition998 = false //個股+興櫃
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

value1 = GetField("實戶買賣超張數")+value1;
plot1(value1,"累計買賣超(張)",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位:張
plot2(GetField("實戶買賣超張數"),"實戶買賣超(張)",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位:張
```

---


---

## 腳本檔案: 指標/籌碼高手/實質買賣盤比.xs

```xs
{@type:indicator}
condition996 = symbolexchange = "TW" and symboltype = 2;//個股
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
condition993 = symbolexchange = "TW" and symboltype = 1;//類股

if condition994 =false and condition993 = false and condition996 = false //大盤+類股+個股
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

plot1(0.01*(GetField("實質買盤比")-GetField("實質賣盤比")),"買賣差值",checkbox:=1,axis:=2,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
plot2(0.01*GetField("實質買盤比"),"買盤比",checkbox:=0,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
plot3(0.01*GetField("實質賣盤比"),"賣盤比",checkbox:=0,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
```

---


---

## 腳本檔案: 指標/籌碼高手/庫藏股指標.xs

```xs
{@type:indicator}
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW" or symbolType = 1;//大盤、類股

if condition994 = false //大盤、類股
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

plot1(GetField("庫藏股申請總市值")*1000,"申報總市值",axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位:千元
plot2(GetField("庫藏股申請家數"),"申報家數",checkbox:=0,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位:家
```

---


---

## 腳本檔案: 指標/籌碼高手/投信.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
condition993 = symbolexchange = "TW" and symboltype = 1;//類股

if condition999 = false and condition994 = false//大盤, 個股, 權證, 興櫃, 類股指數
	then raiseruntimeerror("不支援此商品");


if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

if condition994 then begin
	value1 = GetField("投信買進金額");
	value2 = GetField("投信賣出金額");
	value3 = GetField("投信買賣超金額");
	value4 = value4 + GetField("投信買賣超金額");
	plot2(value4,"投信累計買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis1
	setplotlabel(1,"買賣超(元)");
	setplotlabel(2,"投信累計買賣超(元)");
	setplotlabel(3,"買進(元)");
	setplotlabel(4,"賣出(元)");
	plot1(value3,"買賣超",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //bar，axis2
	plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
	plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
end else begin
	if symbolexchange <> "TE" and condition993 = false then begin
		value1 = GetField("投信買張");
		value2 = GetField("投信賣張");
	end;
	value3 = GetField("投信買賣超張數");
	plot2(GetField("投信持股"),"投信持股",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis1
	setplotlabel(1,"買賣超(張)");
	setplotlabel(2,"投信持股(張)");
	setplotlabel(3,"買進(張)");
	setplotlabel(4,"賣出(張)");
	if condition993 = false then begin
		plot5(0.01*GetField("投信持股比例"),"投信持股比例",axis:=12,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
	end;
	plot1(value3,"買賣超",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0); //bar，axis2
	if symbolexchange <> "TE" and condition993 = false then begin
		plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis2
		plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis2
	end;
end;
```

---


---

## 腳本檔案: 指標/籌碼高手/投信持股比例.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and symboltype = 2;//個股+興櫃

if condition998 = false //個股+興櫃
	then raiseruntimeerror("不支援此商品");



if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

plot1(0.01*GetField("投信持股比例"),"投信持股比例",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
```

---


---

## 腳本檔案: 指標/籌碼高手/控盤者主動買賣力.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and symboltype = 2;//個股+興櫃

if condition998 = false //個股+興櫃
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

plot1(GetField("主動性交易比重"),"交易比重",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd2);
plot2(GetField("主動買力"),"主動買力",checkbox:=0,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd2);
plot3(GetField("主動賣力"),"主動賣力",checkbox:=0,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd2);
```

---


---

## 腳本檔案: 指標/籌碼高手/控盤者買賣盤.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and symboltype = 2;//個股+興櫃

if condition998 = false //個股+興櫃
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

value1 = GetField("控盤者買賣超張數")+value1;
plot1(value1,"累計買賣超(張)",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位:張
plot2(GetField("控盤者買賣超張數"),"控盤者買賣超(張)",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位:張
```

---


---

## 腳本檔案: 指標/籌碼高手/散戶持股.xs

```xs
{@type:indicator}
{由集保公司所提供的，「指定級距以下」的持股資料所計算}

input: _input1(50,"散戶標準",inputkind:= Dict(["1",1],["5",5],["10",10],["15",15],["20",20],["30",30],["40",40],["50",50],["100",100],["200",200],["400",400],["600",600],["800",800],["1000",1000]),quickedit:=true);

condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and (symboltype = 2 or symbolType = 1);//個股+興櫃+類股

if condition998 = false //個股+興櫃+類股
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
switch (_input1)
begin
	case 1:
		if barFreq = "D" then begin
			value1 = Getfield("散戶持股比例","W",param:=1);
			value2 = Getfield("散戶持股張數","W",param:=1);
			value3 = Getfield("散戶持股人數","W",param:=1);
		end else begin
			value1 = Getfield("散戶持股比例",param:=1);
			value2 = Getfield("散戶持股張數",param:=1);
			value3 = Getfield("散戶持股人數",param:=1);
		end;	
		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
		
	case 5:
		if barFreq = "D" then begin
			value1 = Getfield("散戶持股比例","W",param:=5);
			value2 = Getfield("散戶持股張數","W",param:=5);
			value3 = Getfield("散戶持股人數","W",param:=5);
		end else begin
			value1 = Getfield("散戶持股比例",param:=5);
			value2 = Getfield("散戶持股張數",param:=5);
			value3 = Getfield("散戶持股人數",param:=5);
		end;	
		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);

	case 10:
		if barFreq = "D" then begin
			value1 = Getfield("散戶持股比例","W",param:=10);
			value2 = Getfield("散戶持股張數","W",param:=10);
			value3 = Getfield("散戶持股人數","W",param:=10);
		end else begin
			value1 = Getfield("散戶持股比例",param:=10);
			value2 = Getfield("散戶持股張數",param:=10);
			value3 = Getfield("散戶持股人數",param:=10);
		end;	
		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
			
	case 15:
		if barFreq = "D" then begin
			value1 = Getfield("散戶持股比例","W",param:=15);
			value2 = Getfield("散戶持股張數","W",param:=15);
			value3 = Getfield("散戶持股人數","W",param:=15);
		end else begin
			value1 = Getfield("散戶持股比例",param:=15);
			value2 = Getfield("散戶持股張數",param:=15);
			value3 = Getfield("散戶持股人數",param:=15);
		end;	
		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
		
	case 20:
		if barFreq = "D" then begin
			value1 = Getfield("散戶持股比例","W",param:=20);
			value2 = Getfield("散戶持股張數","W",param:=20);
			value3 = Getfield("散戶持股人數","W",param:=20);
		end else begin
			value1 = Getfield("散戶持股比例",param:=20);
			value2 = Getfield("散戶持股張數",param:=20);
			value3 = Getfield("散戶持股人數",param:=20);
		end;	
		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
		
	case 30:
		if barFreq = "D" then begin
			value1 = Getfield("散戶持股比例","W",param:=30);
			value2 = Getfield("散戶持股張數","W",param:=30);
			value3 = Getfield("散戶持股人數","W",param:=30);
		end else begin
			value1 = Getfield("散戶持股比例",param:=30);
			value2 = Getfield("散戶持股張數",param:=30);
			value3 = Getfield("散戶持股人數",param:=30);
		end;	
		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
	
	case 40:
		if barFreq = "D" then begin
			value1 = Getfield("散戶持股比例","W",param:=40);
			value2 = Getfield("散戶持股張數","W",param:=40);
			value3 = Getfield("散戶持股人數","W",param:=40);
		end else begin
			value1 = Getfield("散戶持股比例",param:=40);
			value2 = Getfield("散戶持股張數",param:=40);
			value3 = Getfield("散戶持股人數",param:=40);
		end;	
		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
		
	case 50:
		if barFreq = "D" then begin
			value1 = Getfield("散戶持股比例","W",param:=50);
			value2 = Getfield("散戶持股張數","W",param:=50);
			value3 = Getfield("散戶持股人數","W",param:=50);
		end else begin
			value1 = Getfield("散戶持股比例",param:=50);
			value2 = Getfield("散戶持股張數",param:=50);
			value3 = Getfield("散戶持股人數",param:=50);
		end;
		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);

	case 100:
		if barFreq = "D" then begin
			value1 = Getfield("散戶持股比例","W",param:=100);
			value2 = Getfield("散戶持股張數","W",param:=100);
			value3 = Getfield("散戶持股人數","W",param:=100);
		end else begin
			value1 = Getfield("散戶持股比例",param:=100);
			value2 = Getfield("散戶持股張數",param:=100);
			value3 = Getfield("散戶持股人數",param:=100);
		end;
		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
		
	case 200:
		if barFreq = "D" then begin
			value1 = Getfield("散戶持股比例","W",param:=200);
			value2 = Getfield("散戶持股張數","W",param:=200);
			value3 = Getfield("散戶持股人數","W",param:=200);
		end else begin
			value1 = Getfield("散戶持股比例",param:=200);
			value2 = Getfield("散戶持股張數",param:=200);
			value3 = Getfield("散戶持股人數",param:=200);
		end;
		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
		
	case 400:
		if barFreq = "D" then begin
			value1 = Getfield("散戶持股比例","W",param:=400);
			value2 = Getfield("散戶持股張數","W",param:=400);
			value3 = Getfield("散戶持股人數","W",param:=400);
		end else begin
			value1 = Getfield("散戶持股比例",param:=400);
			value2 = Getfield("散戶持股張數",param:=400);
			value3 = Getfield("散戶持股人數",param:=400);
		end;
		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
	
	case 600:
		if barFreq = "D" then begin
			value1 = Getfield("散戶持股比例","W",param:=600);
			value2 = Getfield("散戶持股張數","W",param:=600);
			value3 = Getfield("散戶持股人數","W",param:=600);
		end else begin
			value1 = Getfield("散戶持股比例",param:=600);
			value2 = Getfield("散戶持股張數",param:=600);
			value3 = Getfield("散戶持股人數",param:=600);
		end;
		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
		
	case 800:
		if barFreq = "D" then begin
			value1 = Getfield("散戶持股比例","W",param:=800);
			value2 = Getfield("散戶持股張數","W",param:=800);
			value3 = Getfield("散戶持股人數","W",param:=800);
		end else begin
			value1 = Getfield("散戶持股比例",param:=800);
			value2 = Getfield("散戶持股張數",param:=800);
			value3 = Getfield("散戶持股人數",param:=800);
		end;
		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
	
	default:
		if barFreq = "D" then begin
			value1 = Getfield("散戶持股比例","W",param:=1000);
			value2 = Getfield("散戶持股張數","W",param:=1000);
			value3 = Getfield("散戶持股人數","W",param:=1000);
		end else begin
			value1 = Getfield("散戶持股比例",param:=1000);
			value2 = Getfield("散戶持股張數",param:=1000);
			value3 = Getfield("散戶持股人數",param:=1000);
		end;
		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);

end;
```

---


---

## 腳本檔案: 指標/籌碼高手/散戶指標(量).xs

```xs
{@type:indicator}
condition996 = symbolexchange = "TW" and symboltype = 2;//個股
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
condition993 = symbolexchange = "TW" and symboltype = 1;//類股

//原始spec要求支援類股，6.30暫不支援，等DB補資料
//if condition994 =false and condition993 = false and condition996 = false //大盤+類股+個股
if condition994 =false and condition996 = false //大盤+個股
	then raiseruntimeerror("不支援此商品");

if barfreq <> "D" and barfreq <> "AD"
	then raiseruntimeerror("不支援此頻率");

if condition994 then
	value1 =  GetField("累計成交") - (GetField("資券互抵張數") + GetField("現股當沖張數"))
else
	value1 = volume - (GetField("資券互抵張數") + GetField("現股當沖張數"));
value2 = GetField("融資買進張數") + GetField("融券買進張數");
value3 = GetField("融資賣出張數") + GetField("融券賣出張數");
if value1 <> 0 then begin
	value4 = value2 / value1;
	value5 = value3 / value1;
end else begin
	value4 = 0;
	value5 = 0;
end;

plot1(value4 - value5,"買賣差值",checkbox:=1,axis:=2,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位：張
plot2(value4,"買進",checkbox:=0,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位：張
plot3(value5,"賣出",checkbox:=0,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位：張
```

---


---

## 腳本檔案: 指標/籌碼高手/散戶買賣盤.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and symboltype = 2;//個股+興櫃

if condition998 = false //個股+興櫃
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

value1 = GetField("散戶買賣超張數")+value1;
plot1(value1,"累計買賣超(張)",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位:張
plot2(GetField("散戶買賣超張數"),"散戶買賣超(張)",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位:張
```

---


---

## 腳本檔案: 指標/籌碼高手/本益比.xs

```xs
{@type:indicator}
//支援商品：台(股票)、美(股票)、美(特別股）
value1 = GetField("本益比");

if value1 > 0 then begin
	plot1(value1);
	setplotLabel(1,"PE");
end
else begin
	plot1(0);
	setplotLabel(1,"近4季EPS為負");
end;
```

---


---

## 腳本檔案: 指標/籌碼高手/機構持股.xs

```xs
{@type:indicator}
//資料更新頻率：季
//支援商品：美(股票)
if barfreq = "Tick" or barfreq = "Min" then raiseruntimeerror("不支援此頻率");
	
var:exchange("");
exchange = GetSymbolInfo("交易所");
if exchange <> "NYSE" and exchange <> "NASDAQ" and exchange <> "AMEX" then raiseruntimeerror("僅支援美股");

plot1(GetField("機構持股比重", "Q")/100,"機構持股比重",Checkbox:=1);//機購持股比重
plot2(GetField("機構持股", "Q"),"持股數值",Checkbox:=0);//持股數值
```

---


---

## 腳本檔案: 指標/籌碼高手/殖利率.xs

```xs
{@type:indicator}
//支援商品：台(股票)、台(ETF)、美(股票)、美(ETF)、美(特別股)。
value1 = GetField("殖利率");

if value1 > 0 then begin
	plot1(value1/100);
	setplotLabel(1,"殖利率");
end	
else begin
	plot1(0);
	setplotLabel(1,"無配息紀錄");
end;
```

---


---

## 腳本檔案: 指標/籌碼高手/法人.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
condition997 = condition999 and (symboltype = 2 or symboltype = 4);//個股+權證+興櫃

if condition999 = false and condition994 = false//大盤, 個股, 權證, 興櫃, 類股指數
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

if condition994 then begin
	value1 = GetField("法人買進金額");
	value2 = GetField("法人賣出金額");
	value3 = GetField("法人買賣超金額");
	value4 = value4 + GetField("法人買賣超金額");
	plot2(value4,"法人累計買賣超",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis1
	setplotlabel(1,"買賣超(元)");
	setplotlabel(2,"法人累計買賣超(元)");
	setplotlabel(3,"買進(元)");
	setplotlabel(4,"賣出(元)");
	plot1(value3,"買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //bar，axis2
	plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
	plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
end else begin
	if symbolexchange <> "TE" and symboltype <> 1 and date >= 20110106 then begin
		value1 = GetField("法人買張");
		value2 = GetField("法人賣張");
	end;
	value3 = GetField("法人買賣超張數");
	plot2(GetField("法人持股"),"法人持股",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis1
	setplotlabel(1,"買賣超(張)");
	setplotlabel(2,"法人持股(張)");
	setplotlabel(3,"買進(張)");
	setplotlabel(4,"賣出(張)");
	if symboltype <> 1 then 
		value5 = 0.01*GetField("法人持股比例");
	plot5(value5,"法人持股比例",axis:=12,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
	plot1(value3,"買賣超",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0); //bar，axis2
	if symbolexchange <> "TE" and symboltype <> 1 then begin
		plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis2
		plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis2
	end;
end;
```

---


---

## 腳本檔案: 指標/籌碼高手/法人持股比例.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and symboltype = 2;//個股+興櫃

if condition998 = false //個股+興櫃
	then raiseruntimeerror("不支援此商品");


if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
plot1(0.01*GetField("法人持股比例"),"法人持股比例",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
```

---


---

## 腳本檔案: 指標/籌碼高手/營收.xs

```xs
{@type:indicator}
Var:_Sales(0);

condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and (symboltype = 2 or symboltype = 1);//個股+興櫃+類股

if condition998 = false //個股+興櫃+類股
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min" or barfreq = "Q" or barfreq = "H" or barfreq = "Y"
	then raiseruntimeerror("不支援此頻率");

if GetField("月營收","M") <> 0 then
	value1 = rateOfChange(GetField("月營收","M"),1) / 100;

if GetField("月營收","M")[12] <> 0 then
	value2 = (GetField("月營收","M") - GetField("月營收","M")[12]) / GetField("月營收","M")[12];

plot1(GetField("月營收","M")*100000000,"月營收",axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sd2);
plot2(value1,"月增率",checkbox:=1,axis:=2,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
plot3(value2,"年增率",checkbox:=1,axis:=2,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
```

---


---

## 腳本檔案: 指標/籌碼高手/現股當沖金額.xs

```xs
{@type:indicator}
condition996 = symbolexchange = "TW" and symboltype = 2;//個股
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
condition993 = symbolexchange = "TW" and symboltype = 1;//類股

if condition994 =false and condition993 = false and condition996 = false //大盤+類股+個股
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

if symboltype = 1 then begin
	if volume <> 0 then
		value1 = (GetField("現股當沖買進金額")+GetField("現股當沖賣出金額"))/(volume*2)
	else
		value1 = 0;
	plot1(value1,"當沖比率",checkbox:=1,axis:=2,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位：％
	plot2(GetField("現股當沖買進金額"),"買進",checkbox:=0,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：元，可勾選畫圖選項 (參數設定) 
	plot3(GetField("現股當沖賣出金額"),"賣出",checkbox:=0,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：元，可勾選畫圖選項 (參數設定) 
end else begin
	if GetField("成交金額(元)") <> 0 then
		value1 = (GetField("現股當沖買進金額")+GetField("現股當沖賣出金額"))/(GetField("成交金額(元)")*2)
	else
		value1 = 0;
	plot1(value1,"當沖比率",checkbox:=1,axis:=2,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位：％
	plot2(GetField("現股當沖買進金額"),"買進",checkbox:=0,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：元，可勾選畫圖選項 (參數設定) 
	plot3(GetField("現股當沖賣出金額"),"賣出",checkbox:=0,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：元，可勾選畫圖選項 (參數設定) 
end;
```

---


---

## 腳本檔案: 指標/籌碼高手/申報轉讓.xs

```xs
{@type:indicator}
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
condition993 = symbolexchange = "TW" and symboltype = 1;//類股

if condition994 =false and condition993 = false //大盤+類股
	then raiseruntimeerror("不支援此商品");

if barfreq <> "D" and barfreq <> "AD" and
	barfreq <> "W" and barfreq <> "AW" and
	barfreq <> "M" and barfreq <> "AM"
	then raiseruntimeerror("不支援此頻率");


plot1(Getfield("申報總市值"),"申報總市值",axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
plot2(Getfield("申報家數"),"申報家數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
plot3(Getfield("申報人數"),"申報人數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
```

---


---

## 腳本檔案: 指標/籌碼高手/當沖.xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 指標/籌碼高手/累計每股盈餘(發佈值).xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and (symboltype = 2 or symboltype = 1);//個股+興櫃+類股

if condition998 = false //個股+興櫃+類股
	then raiseruntimeerror("不支援此商品");

if GetField("累計每股盈餘(發佈值)","Q")[4] <> 0 then
	value1 = (GetField("累計每股盈餘(發佈值)","Q") - GetField("累計每股盈餘(發佈值)","Q")[4]) / GetField("累計每股盈餘(發佈值)","Q")[4]*100;

plot1(GetField("累計每股盈餘(發佈值)","Q"),"累計每股盈餘(發佈值)");
plot2(value1,"年增率(%)");
```

---


---

## 腳本檔案: 指標/籌碼高手/累計淨利(發佈值).xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and (symboltype = 2 or symboltype = 1);//個股+興櫃+類股

if condition998 = false //個股+興櫃+類股
	then raiseruntimeerror("不支援此商品");

if GetField("累計淨利(發佈值)","Q")[4] <> 0 then
	value1 = (GetField("累計淨利(發佈值)","Q") - GetField("累計淨利(發佈值)","Q")[4]) / GetField("累計淨利(發佈值)","Q")[4]*100;

plot1(GetField("累計淨利(發佈值)","Q"),"累計淨利(發佈值)");
plot2(value1,"年增率(%)");
```

---


---

## 腳本檔案: 指標/籌碼高手/綜合前十大券商.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and (symboltype = 2 or symboltype = 1);//個股+興櫃+類股
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤


if condition994 =false and condition998 = false //大盤+個股+興櫃+類股
	then raiseruntimeerror("不支援此商品");
//if condition994 = false //大盤
	//then raiseruntimeerror("不支援此商品");

if barfreq <> "D" and barfreq <> "AD"
	then raiseruntimeerror("不支援此頻率");

if condition994 then begin
	value1 = GetField("綜合前十大券商買進金額");
	value2 = GetField("綜合前十大券商賣出金額");
	value3 = value1 - value2;
	value4 = GetField("綜合前十大券商累計買賣超金額");
	plot1(value3,"買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //bar，axis2
	plot2(value4,"綜合前十大券商累計買賣超",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis1
	plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
	plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
end else begin
	value3 = GetField("綜合前十大券商買賣超張數");
	value4 = value4 + value3;
	plot1(value3,"買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //bar，axis2
	plot2(value4,"綜合前十大券商累計買賣超",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //line，axis1
end;
```

---


---

## 腳本檔案: 指標/籌碼高手/總持股人數.xs

```xs
{@type:indicator}
//說明：
//交易所公布的總持股人數。
//執行商品為股票時，支援「週」以上的頻率。
//執行商品為可轉債時，支援「月」以上的頻率。

condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and (symboltype = 2 or symbolType = 1 or symboltype = 6);//個股+類股+可轉債

if condition998 = false //個股+興櫃+類股
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

if symboltype = 2 or symbolType = 1 then begin
	if barFreq = "D" then
		value1 = GetField("總持股人數","W")
	else
		value1 = GetField("總持股人數");
end;

if symboltype = 6 then begin
	if barFreq = "D" or barFreq = "W"  then
		value1 = GetField("總持股人數","M")
	else
		value1 = GetField("總持股人數");
end;

plot1(value1,"總持股人數");
```

---


---

## 腳本檔案: 指標/籌碼高手/自營商.xs

```xs
{@type:indicator}
input: _input1(1,"自營商",inputkind:= Dict(["全部",1],["自行買賣",2],["避險",3]),quickedit:=true);

condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
condition993 = symbolexchange = "TW" and symboltype = 1;//類股

if condition999 = false and condition994 = false//大盤, 個股, 權證, 興櫃, 類股指數
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

if condition994 then begin
	switch (_input1)
	begin
		case 2:
			value1 = GetField("自營商自行買賣買進金額");
			value2 = GetField("自營商自行買賣賣出金額");
			value3 = GetField("自營商自行買賣買賣超金額");
			value4 = value4 + GetField("自營商自行買賣買賣超金額");
		case 3:
			value1 = GetField("自營商避險買進金額");
			value2 = GetField("自營商避險賣出金額");
			value3 = GetField("自營商避險買賣超金額");
			value4 = value4 + GetField("自營商避險買賣超金額");
		default:
			value1 = GetField("自營商買進金額");
			value2 = GetField("自營商賣出金額");
			value3 = GetField("自營商買賣超金額");
			value4 = value4 + GetField("自營商買賣超金額");
	end;
	plot2(value4,"自營商累計買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis1
	setplotlabel(1,"買賣超(元)");
	setplotlabel(2,"自營商累計買賣超(元)");
	setplotlabel(3,"買進(元)");
	setplotlabel(4,"賣出(元)");
	plot1(value3,"買賣超",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //bar，axis2
	plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
	plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
end else begin
	switch (_input1)
	begin
		case 2:
			if symbolexchange <> "TE" and condition993 = false and date >= 20110106 then begin
				value1 = GetField("自營商自行買賣買張");
				value2 = GetField("自營商自行買賣賣張");
			end;
			value3 = GetField("自營商自行買賣買賣超");
		case 3:
			if symbolexchange <> "TE" and condition993 = false and date >= 20110106 then begin
				value1 = GetField("自營商避險買張");
				value2 = GetField("自營商避險賣張");
			end;
			value3 = GetField("自營商避險買賣超");
		default:
			if symbolexchange <> "TE" and condition993 = false and date >= 20110106 then begin
				value1 = GetField("自營商買張");
				value2 = GetField("自營商賣張");
			end;
			value3 = GetField("自營商買賣超張數");
	end;
	plot2(GetField("自營商持股"),"自營商持股",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis1
	setplotlabel(1,"買賣超(張)");
	setplotlabel(2,"自營商持股(張)");
	setplotlabel(3,"買進(張)");
	setplotlabel(4,"賣出(張)");
	if condition993 = false then begin
		plot5(0.01*GetField("自營商持股比例"),"自營商持股比例",axis:=12,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
	end;
	plot1(value3,"買賣超",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0); //bar，axis2
	if symbolexchange <> "TE" and condition993 = false then begin
		plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis2
		plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis2
	end;
end;
```

---


---

## 腳本檔案: 指標/籌碼高手/自營商持股比例.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
condition998 = condition999 = true and symboltype = 2;//個股+興櫃

if condition998 = false //個股+興櫃
	then raiseruntimeerror("不支援此商品");


if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");
	
plot1(0.01*GetField("自營商持股比例"),"自營商持股比例",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
```

---


---

## 腳本檔案: 指標/籌碼高手/融券.xs

```xs
{@type:indicator}
condition996 = symbolexchange = "TW" and symboltype = 2;//個股
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
condition993 = symbolexchange = "TW" and symboltype = 1;//類股
condition991 = symbolexchange = "SH" and symboltype = 2;//滬股
condition990 = symbolexchange = "SZ" and symboltype = 2;//深股

if condition994 =false and condition993 = false and condition996 = false //大盤+類股+個股
	and condition991 = false and condition990 = false //陸股
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

if condition994 then begin
	plot1(GetField("融券餘額張數"),"融券(張)",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張
	plot2(GetField("融券增減張數"),"差額(張)",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張
	plot3(GetField("融券買進張數"),"買進(張)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張，可勾選畫圖選項 (參數設定) 
	plot4(GetField("融券賣出張數"),"賣出(張)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張，可勾選畫圖選項 (參數設定) 
	plot5(GetField("現券償還張數"),"券償(張)",checkbox:=0,axis:=12,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張，可勾選畫圖選項 (參數設定) 
end else begin
	plot1(GetField("融券餘額張數"),"融券(張)",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
	plot2(GetField("融券增減張數"),"差額(張)",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
	if condition996 then begin
		value1 = GetField("融券買進張數");
		value2 = GetField("融券賣出張數");
		value3 = GetField("現券償還張數");
	end;
	plot3(value1,"買進(張)",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張，可勾選畫圖選項 (參數設定) 
	plot4(value2,"賣出(張)",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張，可勾選畫圖選項 (參數設定) 
	plot5(value3,"券償(張)",checkbox:=0,axis:=12,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張，可勾選畫圖選項 (參數設定) 
end;
if condition996 then
	plot6(GetField("融券使用率")*0.01,"使用率",axis:=13,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位%隱藏，不畫圖，僅查價，缺欄位
```

---


---

## 腳本檔案: 指標/籌碼高手/融券使用率.xs

```xs
{@type:indicator}
condition996 = symbolexchange = "TW" = true and symboltype = 2;//個股

if condition996 = false //個股
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

plot1(0.01 * GetField("融券使用率"),"融券使用率",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//請RD加
```

---


---

## 腳本檔案: 指標/籌碼高手/融資.xs

```xs
{@type:indicator}
input: _input1(1,"大盤融資單位",inputkind:= Dict(["金額",1],["張數",2]));//1=金額、2=張數

condition996 = symbolexchange = "TW" and symboltype = 2;//個股
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
condition993 = symbolexchange = "TW" and symboltype = 1;//類股
condition991 = symbolexchange = "SH" and symboltype = 2;//滬股
condition990 = symbolexchange = "SZ" and symboltype = 2;//深股

if condition994 =false and condition993 = false and condition996 = false //大盤+類股+個股
	and condition991 = false and condition990 = false //陸股
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

if condition994 and _input1 = 1 then begin
	plot1(GetField("融資餘額金額"),"融資(元)",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張
	plot2(GetField("融資增減金額"),"差額(元)",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張
	plot3(GetField("融資買進金額"),"買進(元)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//可勾選畫圖選項 (參數設定) 
	plot4(GetField("融資賣出金額"),"賣出(元)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//可勾選畫圖選項 (參數設定) 
	plot5(GetField("現金償還張數"),"現償(張)",checkbox:=0,axis:=12,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//可勾選畫圖選項 (參數設定) 
	setplotlabel(1,"融資(元)");
	setplotlabel(2,"差額(元)");
	setplotlabel(3,"買進(元)");
	setplotlabel(4,"賣出(元)");
end else begin
	plot1(GetField("融資餘額張數"),"融資(張)",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
	plot2(GetField("融資增減張數"),"差額(張)",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
	if condition996 then begin
		value1 = GetField("融資買進張數");
		value2 = GetField("融資賣出張數");
		value3 = GetField("現金償還張數");
	end;
	plot3(value1,"買進(張)",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);//可勾選畫圖選項 (參數設定) 
	plot4(value2,"賣出(張)",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);//可勾選畫圖選項 (參數設定) 
	plot5(value3,"現償(張)",checkbox:=0,axis:=12,ScaleLabel:=slfull,ScaleDecimal:=sd0);//可勾選畫圖選項 (參數設定) 
	setplotlabel(1,"融資(張)");
	setplotlabel(2,"差額(張)");
	setplotlabel(3,"買進(張)");
	setplotlabel(4,"賣出(張)");
end;
if condition996 then
	plot6(GetField("融資使用率")*0.01,"使用率",axis:=13,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位%，隱藏，不畫圖，僅查價
```

---


---

## 腳本檔案: 指標/籌碼高手/融資使用率.xs

```xs
{@type:indicator}
condition996 = symbolexchange = "TW" = true and symboltype = 2;//個股

if condition996 = false //個股
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

plot1(GetField("融資使用率")*0.01,"融資使用率",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位%
```

---


---

## 腳本檔案: 指標/籌碼高手/融資維持率.xs

```xs
{@type:indicator}
condition996 = symbolexchange = "TW" = true and symboltype = 2;//個股
condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤

if condition994 = false and condition996 = false //大盤+個股
	then raiseruntimeerror("不支援此商品");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

plot1(GetField("融資維持率")*0.01, "融資維持率",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
//plot1(1, "融資維持率",checkbox:=1,axis:=1);

if symboltype = 1 then begin
	plot2(GetField("融資增減金額"),"融資增減(元)",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：元
	setplotlabel(2,"融資增減(元)");
end else begin
	plot2(GetField("融資增減張數"),"融資增減(張)",checkbox:=0,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
	setplotlabel(2,"融資增減(張)");
end;
```

---


---

## 腳本檔案: 指標/籌碼高手/關聯券商買賣超.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW";//台股
condition998 = symbolType = 2;//股票

if condition999 = false or condition998 = false//個股
	then raiseruntimeerror("不支援此商品");

if barfreq <> "D" and barfreq <> "AD"
	then raiseruntimeerror("不支援此頻率");

value1 = GetField("關聯券商買賣超張數");
value2 += value1;
plot1(value1,"買賣超(張)",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //bar，axis2
plot2(value2,"累計買賣超(張)",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //line，axis1
```

---


---

## 腳本檔案: 指標/籌碼高手/關鍵券商買賣超.xs

```xs
{@type:indicator}
condition999 = symbolexchange = "TW";//台股

if condition999 = false //個股
	then raiseruntimeerror("不支援此商品");

if barfreq <> "D" and barfreq <> "AD"
	then raiseruntimeerror("不支援此頻率");

value1 = GetField("關鍵券商買賣超張數");
value2 += value1;
plot1(value1,"買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //bar，axis2
plot2(value2,"關鍵券商累計買賣超",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //line，axis1
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/10年EPS預估之10倍本益比線.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

input:pe(10,"合理本益比");
var: _EPSSum1(0), _count1(0), _EPSSum2(0), _count2(0);

_EPSSum1 = 0;
_count1 = 0;
for value1 = 0 to 10 begin
    if CheckField("每股稅後淨利(元)", "Y")[value1] then begin
	    _EPSSum1 += getField("每股稅後淨利(元)", "Y")[value1];
		_count1 += 1;
		//print(currentBar, date, getFielddate("每股稅後淨利(元)", "Y")[value1], getField("每股稅後淨利(元)", "Y")[value1]);
		end;
	if _count1 = 10 then break;
	end;
	
_EPSSum2 = 0;
_count2 = 0;
for value1 = 0 to 5 begin
    if CheckField("每股稅後淨利(元)", "Q")[value1] then begin 
	    _EPSSum2 += getField("每股稅後淨利(元)", "Q")[value1];
		_count2 += 1;
		print(currentBar, date, getFielddate("每股稅後淨利(元)", "Q")[value1], getFielddate("每股稅後淨利(元)", "Q")[value1]);
		end;
	if _count2 = 4 then break;
	end;

if _count1 > 0 then value3=((_EPSSum1 / _count1)+_EPSSum2)/2;
value4=value3*pe;
plot1(value4,"10倍長期PE線");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/PB倍數線.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);


value1 = getField("每股淨值(元)", "Q", default := value1[1]);
input:ratio1(0.8);
input:ratio2(1);
input:ratio3(1.2);
input:ratio4(1.5);
input:ratio5(1.8);

if value1 <> 0 then value2 = close / value1;

plot1(value2*ratio1, "0.8倍");
plot2(value2*ratio2, "1.0倍");
plot3(value2*ratio3, "1.2倍");
plot4(value2*ratio4, "1.5倍");
plot5(value2*ratio5, "1.8倍");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/員工人數.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

value1 = getField("員工人數", "Q", default:=value1[1]);
plot1(value1,"員工人數");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/季營收年增率.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

if checkfield("營業收入淨額", "Q")[4] and checkField("營業收入淨額", "Q") and getField("營業收入淨額", "Q")[4] <> 0 then 
    value1 = 100 * (getField("營業收入淨額", "Q") - getField("營業收入淨額", "Q")[4]) / getField("營業收入淨額", "Q")[4];
	
plot1(value1, "季營收年增率");

value2 = getField("營業收入淨額", "Q", default := value2[1]);
plot2(value2, "季營收(百萬)");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/年營收年增率.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

if CheckField("營業收入淨額", "Y") and CheckField("營業收入淨額", "Y")[1] and getField("營業收入淨額", "Y")[1] <> 0 then begin
    value1 = (getField("營業收入淨額", "Y") - getField("營業收入淨額", "Y")[1]) / getField("營業收入淨額", "Y")[1] * 100;
	end;

plot1(value1, "年營收年增率");

value2=getField("營業收入淨額", "Y", default := value2[1]);
plot2(value2,"年營收(百萬)");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/應收帳款週轉率.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

value1=getField("應收帳款週轉率(次)", "Q", default:= value1[1]);
plot1(value1,"應收帳款週轉率(次)");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/月營收年增率.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

value1=getField("月營收年增率", "M", default := value1[1]);
plot1(value1,"月營收年增率");

value2 = getfield("月營收", "M", default:= value2[1]);
plot2(value2*100, "月營收(百萬)");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/月營收長期移動平均線.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

input:period(4,"移動平均月份數");
var: _sum(0), _count(0);

_sum = 0;
_count = 0;
for value1 = 0 to (period + 5) begin
    if CheckField("月營收年增率", "M")[value1] then begin
	    _sum += getField("月營收年增率", "M")[value1];
		_count += 1;
		end;
	if _count = period then break;
	end;

if _count > 0 then value1 = _sum / _count;
plot1(value1, "月營收年增率移動平均");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/殖利率.xs

```xs
{@type:indicator}
value1=getField("殖利率", "D", default := value1[1]);
plot1(value1,"殖利率");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/每股淨值.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

value1=getField("每股淨值(元)", "Q", default := value1[1]);
plot1(value1,"每股淨值(元)");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/每股營收.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

var: _sum(0), _count(0);

_sum = 0;
_count = 0;
for value1 = 0 to 17 begin
    if checkfield("月營收", "M")[value1] then begin
	    _sum += getField("月營收", "M")[value1];
		_count += 1;
		end;
	if _count = 12 then break;
	end;
	
value2 = getField("普通股股本", "Q", default:= 0);
if value2 <> 0 then value3 = _sum / value2 * 10;
plot1(value3, "每股營收(元)");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/流動比率.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

value1=getField("流動比率", "Q", default := value1[1]);
plot1(value1,"流動比率");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/營業利益率.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

value1=getField("營業利益率", "Q", default := value1[1]);
plot1(value1,"營業利益率");

if checkfield("營業利益率", "Q")[4] and checkField("營業利益率", "Q") and getField("營業利益率", "Q")[4] <> 0 then 
    value2 = 100 * (getField("營業利益率", "Q") - getField("營業利益率", "Q")[4]) / getField("營業利益率", "Q")[4];
	
plot2(value2, "營業利益率年增率");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/營業毛利率.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

value1=getField("營業毛利率", "Q", default := value1[1]);
plot1(value1,"營業毛利率");

if checkfield("營業毛利率", "Q")[4] and checkField("營業毛利率", "Q") and getField("營業毛利率", "Q")[4] <> 0 then 
    value2 = 100 * (getField("營業毛利率", "Q") - getField("營業毛利率", "Q")[4]) / getField("營業毛利率", "Q")[4];
	
plot2(value2, "營業毛利率年增率");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/盈轉佔股本比重.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

value1=getField("盈餘轉增資佔股本比重", "Y", default:=value1[1]);
plot1(value1,"盈餘轉增資佔股本比重" );
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/研發費用.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

value1=getField("研發費用", "Q", default:=value1[1]);
value2=getField("研發費用率", "Q", default:=value2[1]);
plot1(value1,"研發費用(百萬)");
plot2(value2,"研發費用率");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/稅前淨利率.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

value1=getField("稅前淨利率", "Q", default := value1[1]);
plot1(value1,"稅前淨利率");

if checkfield("稅前淨利率", "Q")[4] and checkField("稅前淨利率", "Q") and getField("稅前淨利率", "Q")[4] <> 0 then 
    value2 = 100 * (getField("稅前淨利率", "Q") - getField("稅前淨利率", "Q")[4]) / getField("稅前淨利率", "Q")[4];
	
plot2(value2, "稅前淨利率年增率");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/稅後淨利率.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

value1=getField("稅後淨利率", "Q", default := value1[1]);
plot1(value1,"稅後淨利率");

if checkfield("稅後淨利率", "Q")[4] and checkField("稅後淨利率", "Q") and getField("稅後淨利率", "Q")[4] <> 0 then 
    value2 = 100 * (getField("稅後淨利率", "Q") - getField("稅後淨利率", "Q")[4]) / getField("稅後淨利率", "Q")[4];
	
plot2(value2, "稅後淨利率年增率");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/自由現金流量.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

var: _sum1(0), _count1(0), _sum2(0), _count2(0);

_sum1 = 0;
_count1 = 0;
_sum2 = 0;
_count2 = 0;
for value1 = 0 to 5 begin
    if checkField("自由現金流量", "Q")[value1] then begin
	    _sum1 += getField("自由現金流量", "Q")[value1];
		_count1 += 1;
		end;
	if _count1 = 4 then break;
	end;

for value1 = 0 to 5 begin
	if checkField("自由現金流量營收比", "Q")[value1] then begin
	    _sum2 += getField("自由現金流量營收比", "Q")[value1];
		_count2 += 1;
		end;
	if _count2 = 4 then break;
	end;
	
if _count1 <> 0 then value2 = _sum1 / _count1;
if _count2 <> 0 then value3 = _sum2 / _count2;

plot1(value2,"自由現金流量(百萬)");
plot2(value3,"自由現金流量營收比");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/行銷費用.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

value1=getField("推銷費用", "Q", default := value1[1]);
value2=getField("銷售費用比", "Q", default := value2[1]);
plot1(value1,"推銷費用(百萬)");
plot2(value2,"銷售費用比");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/資本支出長期走勢.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

var: _sum(0), _count(0);

_sum = 0;
_count = 0;
for value1 = 0 to 5 begin
    if checkField("資本支出金額", "Q")[value1] then begin
	    _sum += getField("資本支出金額", "Q")[value1];
		_count += 1;
		end;
	if _count = 4 then break;
	end;

plot1(_sum, "資本支出(百萬)");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/速動比率.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

value1=getField("速動比率", "Q", default := value1[1]);
plot1(value1,"速動比率");
```

---


---

## 腳本檔案: 指標/財報指標/基本面指標/預收款.xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

value1 = GetField("預收款項", "Q", default:= value1[1]);
if checkfield("預收款項", "Q") and checkfield("預收款項", "Q")[4] and GetField("預收款項", "Q")[4] <> 0 then 
    value2 = (GetField("預收款項", "Q") - GetField("預收款項", "Q")[4]) / GetField("預收款項", "Q")[4];
	
plot1(value1,"預收款(百萬)");
plot2(value2,"預收款年增率");
```

---


---

## 腳本檔案: 指標/財報指標/產業面指標/整體營收(執行商品).xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

group: _symbolGroup();
var: _sum(0), _num(0);

_symbolGroup = GetSymbolGroup("成分股");
value1 = GroupSize(_symbolGroup);

_sum = 0;
_num = 0;
for value2 = 1 to value1 begin
    if CheckSymbolField(_symbolGroup[value2], "月營收", "M") then begin
        _sum += GetSymbolField(_symbolGroup[value2], "月營收", "M");
        _num += 1;
        end;
    end;
	
plot1(_sum);
SetPlotLabel(1, "成分股月營收");
plot2(_num);
SetPlotLabel(2, "有月營收家數");
plot3(value1);
SetPlotLabel(3, "成分股家數");
```

---


---

## 腳本檔案: 指標/財報指標/產業面指標/整體營收(指定指數代碼).xs

```xs
{@type:indicator}
input: _setalign(0, "營收財報對位方式", inputkind:=dict(["絕對對位", 0], ["公佈日對位", 1]), quickedit := True);
setalign("營收財報", _setalign);

input: _index("I026010.TW", "指標代碼");
group: _symbolGroup();
var: _sum(0), _num(0);

_symbolGroup = GetSymbolGroup(_index, "成分股");
value1 = GroupSize(_symbolGroup);

_sum = 0;
_num = 0;
for value2 = 1 to value1 begin
    if CheckSymbolField(_symbolGroup[value2], "月營收", "M") then begin
        _sum += GetSymbolField(_symbolGroup[value2], "月營收", "M");
		_num += 1;
        end;
	end;
	
plot1(_sum);
SetPlotLabel(1, text(_index, "成分股月營收"));
plot2(_num);
SetPlotLabel(2, text(_index, "有月營收家數"));
plot3(value1);
SetPlotLabel(3, text(_index, "成分股家數"));
```

---


---

## 腳本檔案: 指標/跨頻率指標/分鐘與日DMI-Osc.xs

```xs
{@type:indicator}
// 跨頻率DMI-Osc指標，預設跨頻率為30分鐘
// 不支援大頻率跨小頻率，例如：
// 不支援主頻率60分鐘，跨頻率計算30分鐘DMI-Osc技術指標。
//
input:	Length(14, "天數"),
		FreqType("30", "跨頻率週期", inputkind:=dict(["1分鐘","1"],["5分鐘","5"],["10分鐘","10"],["15分鐘","15"],["30分鐘","30"],["60分鐘","60"],["日","D"],["還原日","AD"]));

variable: pdi_value(0), ndi_value(0), adx_value(0);

if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("此範例僅支援分鐘、日與還原日頻率");

xfMin_DirectionMovement(FreqType, Length, pdi_value, ndi_value, adx_value);

// 初始區波動較大, 先不繪出
//
if CurrentBar < Length then
 begin
	pdi_value = 0;
	ndi_value = 0;
	adx_value = 0;
 end;

Plot1(pdi_value - ndi_value, "分鐘與日DMI-Osc");

// 防呆，大頻率跨小頻率時，在線圖秀不支援
//
switch (FreqType)
begin
	case  "1":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
		if barinterval <> 1 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
		setplotlabel(1, "1分DMI-Osc");

	case  "5":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
		setplotlabel(1, "5分DMI-Osc");

	case "10":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
		setplotlabel(1, "10分DMI-Osc");

	case "15":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
		setplotlabel(1, "15分DMI-Osc");
		
	case "30":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
		setplotlabel(1, "30分DMI-Osc");

	case "60":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 and barinterval <> 45 and barinterval <> 60 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
		setplotlabel(1, "60分DMI-Osc");
	
	case "D":
		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於日");
		setplotlabel(1, "日DMI-Osc");
		
	case "AD":
		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於還原日");
		setplotlabel(1, "還原日DMI-Osc");

end;
```

---


---

## 腳本檔案: 指標/跨頻率指標/分鐘與日DMI.xs

```xs
{@type:indicator}
// 分頻率DMI指標，預設跨分頻率為30分鐘
// 不支援大頻率跨小頻率，例如：
// 不支援主頻率60分鐘，跨頻率計算30分鐘DMI技術指標。
//
input:	Length(14, "天數"),
		FreqType("30", "跨頻率週期", inputkind:=dict(["1分鐘","1"],["5分鐘","5"],["10分鐘","10"],["15分鐘","15"],["30分鐘","30"],["60分鐘","60"],["日","D"],["還原日","AD"]));

variable: pdi_value(0), ndi_value(0), adx_value(0);

if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("此範例僅支援分鐘、日與還原日頻率");

xfMin_DirectionMovement(FreqType, Length, pdi_value, ndi_value, adx_value);

// 初始區波動較大, 先不繪出
//
if CurrentBar < Length then
 begin
	pdi_value = 0;
	ndi_value = 0;
	adx_value = 0;
 end;

Plot1(pdi_value, "分鐘與日+DI");
Plot2(ndi_value, "分鐘與日-DI");
Plot3(adx_value, "分鐘與日ADX");


// 防呆，大頻率跨小頻率時，在線圖秀不支援
//
switch (FreqType)
begin
	case  "1":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
		if barinterval <> 1 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
		setplotlabel(1, "1分+DI");
		setplotlabel(2, "1分-DI");
		setplotlabel(3, "1分ADX");

	case  "5":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
		setplotlabel(1, "5分+DI");
		setplotlabel(2, "5分-DI");
		setplotlabel(3, "5分ADX");

	case "10":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
		setplotlabel(1, "10分+DI");
		setplotlabel(2, "10分-DI");
		setplotlabel(3, "10分ADX");

	case "15":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
		setplotlabel(1, "15分+DI");
		setplotlabel(2, "15分-DI");
		setplotlabel(3, "15分ADX");
		
	case "30":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
		setplotlabel(1, "30分+DI");
		setplotlabel(2, "30分-DI");
		setplotlabel(3, "30分ADX");

	case "60":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 and barinterval <> 45 and barinterval <> 60 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
		setplotlabel(1, "60分+DI");
		setplotlabel(2, "60分-DI");
		setplotlabel(3, "60分ADX");
		
	case "D":
		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於日");
		setplotlabel(1, "日+DI");
		setplotlabel(2, "日-DI");
		setplotlabel(3, "日ADX");
	
	case "AD":
		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於還原日");
		setplotlabel(1, "還原日+DI");
		setplotlabel(2, "還原日-DI");
		setplotlabel(3, "還原日ADX");
	
end;
```

---


---

## 腳本檔案: 指標/跨頻率指標/分鐘與日KD.xs

```xs
{@type:indicator}
// 跨頻率KD指標，預設跨頻率為30分
// 不支援大頻率跨小頻率，例如：
// 不支援主頻率60分鐘，跨頻率計算30分鐘KD技術指標。
//
input:	Length(9, "天數"), RSVt(3, "RSVt權數"), Kt(3, "Kt權數"),
		FreqType("30", "跨頻率週期", inputkind:=dict(["1分鐘","1"],["5分鐘","5"],["10分鐘","10"],["15分鐘","15"],["30分鐘","30"],["60分鐘","60"],["日","D"],["還原日","AD"]));
variable: rsv(0), k(0), _d(0);

if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("此範例僅支援分鐘、日與還原日頻率");

xfMin_stochastic(FreqType, Length, RSVt, Kt, rsv, k, _d);

Plot1(k, "分鐘與日K(%)");
Plot2(_d, "分鐘與日D(%)");

// 防呆，大頻率跨小頻率時，在線圖秀不支援
//
switch (FreqType)
begin
	case  "1":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
		if barinterval <> 1 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
		setplotlabel(1, "1分K(%)");
		setplotlabel(2, "1分D(%)");

	case  "5":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
		setplotlabel(1, "5分K(%)");
		setplotlabel(2, "5分D(%)");

	case "10":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
		setplotlabel(1, "10分K(%)");
		setplotlabel(2, "10分D(%)");

	case "15":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
		setplotlabel(1, "15分K(%)");
		setplotlabel(2, "15分D(%)");
		
	case "30":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
		setplotlabel(1, "30分K(%)");
		setplotlabel(2, "30分D(%)");

	case "60":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 and barinterval <> 45 and barinterval <> 60 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
		setplotlabel(1, "60分K(%)");
		setplotlabel(2, "60分D(%)");
	
	case "D":
		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於日");
		setplotlabel(1, "日K(%)");
		setplotlabel(2, "日D(%)");

	case "AD":
		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於還原日");
		setplotlabel(1, "還原日K(%)");
		setplotlabel(2, "還原日D(%)");		

end;
```

---


---

## 腳本檔案: 指標/跨頻率指標/分鐘與日MACD.xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 指標/跨頻率指標/分鐘與日RSI.xs

```xs
[Binary file]
```

---


---

## 腳本檔案: 指標/跨頻率指標/分鐘與日威廉指標.xs

```xs
{@type:indicator}
// 跨頻率威廉指標，預設跨頻率為30分
// 不支援大頻率跨小頻率，例如：
// 不支援主頻率60分鐘，跨頻率計算30分鐘威廉技術指標。
//
input: 
	Length1(14, "天數一"), Length2(28, "天數二"), Length3(42, "天數三"),
	FreqType("30", "跨頻率週期", inputkind:=dict(["1分鐘","1"],["5分鐘","5"],["10分鐘","10"],["15分鐘","15"],["30分鐘","30"],["60分鐘","60"],["日","D"],["還原日","AD"]));

if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("此範例僅支援分鐘、日與還原日頻率");

value1 = xfMin_PercentR(FreqType, Length1) - 100;
value2 = xfMin_PercentR(FreqType, Length2) - 100;
value3 = xfMin_PercentR(FreqType, Length3) - 100;

Plot1(value1, "分鐘與日威廉指標1");
Plot2(value2, "分鐘與日威廉指標2");
Plot3(value3, "分鐘與日威廉指標3");

// 防呆，大頻率跨小頻率時，在線圖秀不支援
//
switch (FreqType)
begin
	case  "1":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
		if barinterval <> 1 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
		setplotlabel(1, "1分威廉指標1");
		setplotlabel(2, "1分威廉指標2");
		setplotlabel(3, "1分威廉指標3");

	case  "5":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
		setplotlabel(1, "5分威廉指標1");
		setplotlabel(2, "5分威廉指標2");
		setplotlabel(3, "5分威廉指標3");

	case "10":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
		setplotlabel(1, "10分威廉指標1");
		setplotlabel(2, "10分威廉指標2");
		setplotlabel(3, "10分威廉指標3");

	case "15":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
		setplotlabel(1, "15分威廉指標1");
		setplotlabel(2, "15分威廉指標2");
		setplotlabel(3, "15分威廉指標3");
		
	case "30":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
		setplotlabel(1, "30分威廉指標1");
		setplotlabel(2, "30分威廉指標2");
		setplotlabel(3, "30分威廉指標3");

	case "60":
		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 and barinterval <> 45 and barinterval <> 60 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
		setplotlabel(1, "60分威廉指標1");
		setplotlabel(2, "60分威廉指標2");
		setplotlabel(3, "60分威廉指標3");
		
	case "D":
		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於日");
		setplotlabel(1, "日威廉指標1");
		setplotlabel(2, "日威廉指標2");
		setplotlabel(3, "日威廉指標3");
		
	case "AD":
		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於還原日");
		setplotlabel(1, "還原日威廉指標1");
		setplotlabel(2, "還原日威廉指標2");
		setplotlabel(3, "還原日威廉指標3");

end;
```

---


---

## 腳本檔案: 指標/跨頻率指標/週DMI-Osc.xs

```xs
{@type:indicator}
// 跨頻率週DMI-Osc指標
// 不支援大頻率跨小頻率，例如：
// 不支援主頻率週資料，跨頻率計算日DMI-Osc技術指標。
//
if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "W" and barfreq <> "AD" and barfreq <> "AW" then raiseruntimeerror("不支援大頻率跨小頻率");

input: Length( 14 );
variable: pdi_value(0), ndi_value(0), adx_value(0);

SetInputName(1, "天數");

xf_DirectionMovement("W", Length, pdi_value, ndi_value, adx_value);

// 初始區波動較大, 先不繪出
//
if CurrentBar < Length then
 begin
	pdi_value = 0;
	ndi_value = 0;
	adx_value = 0;
 end;

Plot1(pdi_value - ndi_value, "週DMI-Osc");
```

---


---

## 腳本檔案: 指標/跨頻率指標/週DMI.xs

```xs
{@type:indicator}
// 跨頻率週DMI指標
// 不支援大頻率跨小頻率，例如：
// 不支援主頻率週資料，跨頻率計算日DMI技術指標。
//
if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "W" and barfreq <> "AD" and barfreq <> "AW" then raiseruntimeerror("不支援大頻率跨小頻率");

input: Length(14);
variable: pdi_value(0), ndi_value(0), adx_value(0);

SetInputName(1, "天數");

xf_DirectionMovement("W", Length, pdi_value, ndi_value, adx_value);

// 初始區波動較大, 先不繪出
//
if CurrentBar < Length then
 begin
	pdi_value = 0;
	ndi_value = 0;
	adx_value = 0;
 end;
 
Plot1(pdi_value, "週+DI");
Plot2(ndi_value, "週-DI");
Plot3(adx_value, "週ADX");
```

---


---

## 腳本檔案: 指標/跨頻率指標/週KD.xs

```xs
{@type:indicator}
// 跨頻率週KD指標
// 不支援大頻率跨小頻率，例如：
// 不支援主頻率週資料，跨頻率計算日KD技術指標。
//
if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "W" and barfreq <> "AD" and barfreq <> "AW" then raiseruntimeerror("不支援大頻率跨小頻率");

input: Length(5), RSVt(3), Kt(3);
variable: rsv(0), k(0), _d(0);

SetInputName(1, "天數");
SetInputName(2, "RSVt權數");
SetInputName(3, "Kt權數");

xf_stochastic("W", Length, RSVt, Kt, rsv, k, _d);

Plot1(k, "週K(%)");
Plot2(_d, "週D(%)");
```

---


---

## 腳本檔案: 指標/跨頻率指標/週MACD.xs

```xs
{@type:indicator}
// 跨頻率週MACD指標
// 不支援大頻率跨小頻率，例如：
// 不支援主頻率週資料，跨頻率計算日MACD技術指標。
//
if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "W" and barfreq <> "AD" and barfreq <> "AW" then raiseruntimeerror("不支援大頻率跨小頻率");

input: FastLength(12), SlowLength(26), MACDLength(9);

SetInputName(1, "DIF短天數");
SetInputName(2, "DIF長天數");
SetInputName(3, "MACD天數");

xf_macd("W",xf_weightedclose("W"),FastLength,SlowLength,MACDLength,value1,value2,value3);

// 前面區段資料變動較大, 先不繪出
//
if CurrentBar <= SlowLength then
begin
	Value1 = 0;
	Value2 = 0;
	Value3 = 0;
end;

Plot1(Value1, "週DIF");
Plot2(Value2, "週MACD");
Plot3(Value3, "週Osc");
```

---


---

## 腳本檔案: 指標/跨頻率指標/週RSI.xs

```xs
{@type:indicator}
// 跨頻率週RSI指標
// 不支援大頻率跨小頻率，例如：
// 不支援主頻率週資料，跨頻率計算日RSI技術指標。
//
if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "W" and barfreq <> "AD" and barfreq <> "AW" then raiseruntimeerror("不支援大頻率跨小頻率");

input: Length1(6), Length2(12);

SetInputName(1, "天數一");
SetInputName(2, "天數二");

Plot1(xf_RSI("W", GetField("Close","W"), Length1), "週RSI1");
Plot2(xf_RSI("W", GetField("Close","W"), Length2), "週RSI2");
```

---


---

## 腳本檔案: 指標/跨頻率指標/週威廉指標.xs

```xs
{@type:indicator}
// 跨頻率週威廉指標
// 不支援大頻率跨小頻率，例如：
// 不支援主頻率週資料，跨頻率計算日威廉技術指標。
//
if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "W" and barfreq <> "AD" and barfreq <> "AW" then raiseruntimeerror("不支援大頻率跨小頻率");

input: 
	Length1(14, "天數一"), 
	Length2(28, "天數二"), 
	Length3(42, "天數三");

value1 = xf_PercentR("W", Length1) - 100;
value2 = xf_PercentR("W", Length2) - 100;
value3 = xf_PercentR("W", Length3) - 100;

Plot1(value1, "週威廉指標1");
Plot2(value2, "週威廉指標2");
Plot3(value3, "週威廉指標3");
```

---


---

## 腳本檔案: 指標/量能指標/BBI多空指數.xs

```xs
{@type:indicator}
input:
a1(3,"第一根均線天期"),
a2(6,"第二根均線天期"),
a3(12,"第三根均線天期"),
a4(24,"第四根均線天期");

variable:BBI(0);

BBI=(average(close,a1)+average(close,a2)+average(close,a3)+average(close,a4))/4;
plot1(close-bbi,"多空線");
```

---


---

## 腳本檔案: 指標/量能指標/DKX多空線.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/dkx多空線/
}

input:length(10,"MA期數");

variable:MID(0),midsum(0),DKX(0),DKXMA(0),r1(0);

MID=(close*3+open+high+low)/6;

DKX=WMA(MID,20);
dkxma=average(dkx,length);

plot1(close,"收盤價");
plot2(dkxma,"多空線的移動平均線");
```

---


---

## 腳本檔案: 指標/量能指標/KO成交量擺盪指標.xs

```xs
{@type:indicator}
Input: length1(34);	setinputname(1, "短天期");
Input: length2(55);	setinputname(2, "長天期");
Input: length3(13);	setinputname(3, "平均天期");

variable: kovolume(0), tp(0), ko(0), koaverage(0);   

tp =(close+high+low)/3;   

if tp >= tp[1] then   
	kovolume = volume   
else    
	kovolume = -volume;
  
ko = average(kovolume, length1) - average(kovolume, length2);
koaverage = average(ko, length3);

Plot1(ko, "KO");
Plot2(koaverage, "平均");
```

---


---

## 腳本檔案: 指標/量能指標/VSTD成交量標準差.xs

```xs
{@type:indicator}
input:Period(22,"期數");

variable:VSTD(0);
VSTD=standarddev(VOLUME,Period,1);

PLOT1(VSTD,"VSTD");
```

---


---

## 腳本檔案: 指標/量能指標/WVAD威廉變異離散量.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/wvad威廉變異離散量/
}

input:length(5,"期數");

variable:wvad(0);

value1=close-open;
value2=high-low;

if high<>low then 
	value3=value1/value2*volume
else
	value3=value3[1];

wvad=summation(value3,length);

plot1(wvad,"威廉變異離散量");
```

---


---

## 腳本檔案: 指標/量能指標/上昇趨勢分數.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/上昇趨勢分數/
}

input:length(10,"期數");

variable: count1(0),count2(0),count3(0),count4(0),x1(0);

count1=0;
count2=0;
count3=0;
count4=0;

for x1=0 to length-1
	if h[x1]>h[x1+1] then count1=count1+1;

for x1=0 to length-1
	if o[x1]>o[x1+1] then count2=count2+1;

for x1=0 to length-1
	if low[x1]>low[x1+1] then count3=count3+1;

for x1=0 to length-1
	if close[x1]>close[x1+1] then count4=count4+1;

value1=count1+count2+count3+count4;
value2=value1-20;

plot1(value2,"趨勢分數");
```

---


---

## 腳本檔案: 指標/量能指標/交易活躍度指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/交易異常活躍指標/
}

input:day(66,"移動平均天數");
input:ratio(10,"超出均值比率");

if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

variable:count(0);

value3=GetField("強弱指標");
value4=average(value3,day);
value5=GetField("外盤均量");
value6=average(value5,day);
value7=GetField("主動買力");
value8=average(value7,day);
value9=GetField("開盤委買");
value10=average(value9,day);

count=0;
if value3>=value4*(1+ratio/100) then
	count=count+1;
if value5>=value6*(1+ratio/100) then
	count=count+1;
if value7>=value8*(1+ratio/100) then
	count=count+1;
if value9=value10*(1+ratio/100) then
	count=count+1;

value11=average(count,5);

plot1(value11,"交易活躍度指標");
```

---


---

## 腳本檔案: 指標/量能指標/修正式價量指標.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/修正式價量指標vptvolume-price-trend/
}

input:day(5,"移動平均線天數");

variable:tvp(0),mpc(0);
mpc=(open+high+low+close)/4;
 
if mpc[1]<>0 then
	tvp=tvp[1]+(mpc-mpc[1])/mpc[1]*volume
else
	tvp=tvp[1];

plot1(tvp,"修正型價量指標");
```

---


---

## 腳本檔案: 指標/量能指標/四大力道線.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/改良版的移動平均線四大力道線/
}

input:period(10,"天期參數");

value1=summation(high-close,period);//上檔賣壓
value2=summation(close-open,period); //多空實績
value3=summation(close-low,period);//下檔支撐
value4=summation(open-close[1],period);//隔夜力道
if close<>0 then
	value5=(value2+value3+value4-value1)/close;

plot1(value5,"四大力道線");
```

---


---

## 腳本檔案: 指標/量能指標/外盤量bband.xs

```xs
{@type:indicator}
{
指標說明
https://www.xq.com.tw/xstrader/外盤量異常突出的買進策略/
}

input:length(20,"期數");

variable:bv(0),bva(0);

if volume<>0 then 
	bv=GetField("外盤量")/volume*100;
bva=average(bv,3);

variable:up1(0),down1(0),mid1(0),bbandwidth(0);

up1 = bollingerband(bva, Length, 1);
down1 = bollingerband(bva, Length, -1 );
mid1 = (up1 + down1) / 2;
if mid1<>0 then 
	bbandwidth = 100 * (up1 - down1) / mid1;

plot1(up1, "UB");
plot2(bva, "外盤量佔比");
plot3(down1, "LB");
plot4(bbandwidth, "BW");
```

---


---

## 腳本檔案: 指標/量能指標/成交量擺盪指標.xs

```xs
{@type:indicator}
Input: length1(5);	setinputname(1, "短天期");
Input: length2(20);	setinputname(2, "長天期");

Value1 = Average(Volume, length1);
Value2 = Average(Volume, length2);

if value1 = 0 then value3 = 0 else Value3 = (Value1 - Value2) * 100 / Value1;

Plot1(Value3, "OSCV");
```

---


---

## 腳本檔案: 指標/量能指標/當日成交密度.xs

```xs
{@type:indicator}
variable:II(0);

if high-low<>0 and volume<>0 then 
	II=(2*CLOSE-HIGH-LOW)/(HIGH-LOW)*VOLUME;

PLOT1(average(II,5),"成交密度");
```

---


---

## 腳本檔案: 指標/量能指標/當日成交總筆數.xs

```xs
{@type:indicator}
input:p1(5,"短天期");
input:p2(20,"長天期");

value1=GetField("總成交次數");
value2=average(value1,p1);
value3=average(value2,p2);

plot1(value2,"成交筆數短期均線");
plot2(value3,"成交筆數長期均線");
```

---


---

## 腳本檔案: 指標/量能指標/累積量.xs

```xs
{@type:indicator}
variable:tv(0);//當日累積量

if date<>date[1] then
	tv=volume
else
	tv=tv[1]+volume;

plot1(tv,"累積量");
```

---


---

## 腳本檔案: 指標/量能指標/週轉率.xs

```xs
{@type:indicator}
if barfreq = "Tick" or barfreq = "Min"
	then raiseruntimeerror("不支援此頻率");

if GetField("發行張數(張)") <> 0 then begin
	value1 = volume / GetField("發行張數(張)") * 100;
	plot1(value1,"週轉率(%)");
end else 
	noplot(1);
```

---


---

## 腳本檔案: 指標/量能指標/量比.xs

```xs
{@type:indicator}
{量比公式 = 估計量 / 昨量
當量比 > 1時表示量是放大的, 數值越大表示越強
支援商品：台(股票)}

if barfreq <> "Min" and barfreq <> "D" then 
	raiseruntimeerror("僅支援分鐘與日頻率");

value1 = GetField("量比");

plot1(value1, "量比");
plot2(1, "基準線");
```

---
