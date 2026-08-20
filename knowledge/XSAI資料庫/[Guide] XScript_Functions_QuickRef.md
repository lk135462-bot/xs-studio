# XS 核心函數速查指南

本文件將常用函數依「基本→進階→高階」三層分級，提供快速查閱的使用場景與範例代碼。完整參數細節請對照 `[Manual] XScript_BuiltIn_Functions_Reference.md`。

---

## 第一章：基本函數篇（變化性最低的核心函數）

### 一、數學與數值處理類

| 函數 | 說明 | 範例 |
|------|------|------|
| `ceiling` | 無條件進位 | `ceiling(10.1)` → 11 |
| `floor` | 無條件捨去 | `floor(10.5)` → 10 |
| `intportion` | 取整數部分 | `intportion(10.5)` → 10 |
| `fracportion` | 取小數部分 | `fracportion(10.5)` → 0.5 |
| `mod` | 取餘數 | `mod(10, 3)` → 1 |
| `square` | 平方 | `square(10)` → 100 |
| `squareroot` | 平方根 | `squareroot(100)` → 10 |
| `neg` | 負絕對值 | `neg(5)` → -5 |

### 二、數列與集合比較類

| 函數 | 說明 | 範例 |
|------|------|------|
| `maxlist` | 多個數值取最大 | `maxlist(v1, v2, v3)` |
| `minlist` | 多個數值取最小 | `minlist(v1, v2, v3)` |
| `maxlist2` | 第二大值 | `maxlist2(1,2,3,4,5)` → 4 |
| `minlist2` | 第二小值 | `minlist2(1,2,3,4,5)` → 2 |
| `nthmaxlist` | 第N大值 | `nthmaxlist(1, 50,40,30)` → 50 |
| `nthminlist` | 第N小值 | `nthminlist(1, 50,40,30)` → 30 |
| `sumlist` | 加總 | `sumlist(open,high,low,close) / 4` |

```xs
// 實戰：判斷收盤價是否突破三條均線
value1 = average(close, 5);
value2 = average(close, 10);
value3 = average(close, 20);
if open < minlist(value1, value2, value3) and
   close > maxlist(value1, value2, value3) then
    ret = 1;
```

### 三、基本價格與區間定義

| 函數 | 說明 | 公式 |
|------|------|------|
| `avgprice` | 平均價 | (O+H+L+C) / 4 |
| `typicalprice` | 典型價 | (H+L+C) / 3 |
| `weightedclose` | 加權平均價 | (H+L+2*C) / 4 |
| `range` | 高低價區間 | H - L |
| `truerange` | 真實區間 | max(H-L, |H-昨C|, |L-昨C|) |

### 四、邏輯轉換

```xs
// iff：單行 if/else 判斷
value1 = iff(close > close[1], 1, 0);
```

---

## 第二章：進階函數篇（歷史區間與序列運算）

### 一、歷史區間極值與位置

| 函數 | 說明 | 範例 |
|------|------|------|
| `highest` | 區間最大值 | `highest(high, 20)` |
| `lowest` | 區間最小值 | `lowest(low, 20)` |
| `highestbar` | 最大值的相對K棒位置 | `highestbar(high, 20)` → 0=當根 |
| `lowestbar` | 最小值的相對K棒位置 | `lowestbar(low, 20)` |

```xs
// 判斷今日是否創近20日新高
if close = highest(high, 20) then ret = 1;
```

### 二、移動平均與平滑運算

| 函數 | 說明 | 特性 |
|------|------|------|
| `average` | 簡單移動平均 (SMA) | 等權重 |
| `xaverage` | 指數移動平均 (EMA) | 近期權重大，反應靈敏 |
| `wma` | 加權移動平均 | 依距離遞減權重 |

```xs
value1 = average(close, 5);   // SMA
value2 = xaverage(close, 5);  // EMA
value3 = wma(close, 5);       // WMA
```

### 三、序列條件判斷與次數統計

| 函數 | 說明 | 範例 |
|------|------|------|
| `crossover` | 向上穿越（黃金交叉） | `crossover(ma5, ma10)` |
| `crossunder` | 向下跌破（死亡交叉） | `crossunder(ma5, ma10)` |
| `trueall` | 期間內全部成立 | `trueall(close > open, 3)` → 連3紅 |
| `trueany` | 期間內任一成立 | `trueany(high = highest(high,20), 3)` |
| `countif` | 條件符合次數 | `countif(open > close, 5)` |

```xs
// 5日均線和10日均線黃金交叉
value1 = average(close, 5);
value2 = average(close, 10);
condition1 = crossover(value1, value2);
```

### 四、變動率與統計學

| 函數 | 說明 | 範例 |
|------|------|------|
| `rateofchange` | 變動率/漲跌幅 | `rateofchange(close, 5)` |
| `standarddev` | 標準差 | `standarddev(close, 20, 2)` → 樣本 |
| `correlation` | 相關係數 (-1~1) | `correlation(v1, v2, 20)` |

---

## 第三章：高階函數篇（跨維度與群體運算）

### 一、跨維度資料讀取

| 函數 | 說明 | 範例 |
|------|------|------|
| `getfield` | 跨頻率取值+防呆 | `getfield("本益比", "d", default:=0)` |
| `getsymbolfield` | 跨商品取值 | `getsymbolfield("1101.tw", "收盤價", "1")` |
| `xf_getvalue` | 跨頻率序列前期值 | `xf_getvalue("w", value1, 1)` |

```xs
// getfield 跨頻率 + 還原 + 防呆
value1 = getfield("收盤價", "1", adjusted:=true);
value2 = getfield("本益比", "d", default:=0);

// getsymbolfield 跨商品
value3 = getsymbolfield("1101.tw", "收盤價", "1", adjusted:=true, default:=0);

// 取得期貨近月收盤價
value4 = getsymbolfield("Future*1", "收盤價");
```

### 二、群體清單與陣列運算

```xs
// 計算指數成分股營收加總
group: _symbolgroup();
var: _sum(0), _num(0), _i(0);

_symbolgroup = getsymbolgroup("成分股");
value1 = groupsize(_symbolgroup);
_sum = 0;
_num = 0;

for _i = 1 to value1 begin
    if checksymbolfield(_symbolgroup[_i], "月營收", "m") then begin
        _sum += getsymbolfield(_symbolgroup[_i], "月營收", "m");
        _num += 1;
    end;
end;
plot1(_sum, "成分股月營收總和");
```

### 三、rank 排行（選股專用）

```xs
// 依照收盤價由大到小排序
rank _myrank begin
    retval = close;
end;

if _myrank.pos <= 10 then ret = 1;
outputfield(1, _myrank.value, 2, "排行數值");
outputfield(2, _myrank.pos, 0, "排名名次");
```

**四大鐵律**：僅限選股 / 必須放在最外層 / 獨立變數空間 / 屬性小數點前後不可有空白

### 四、動態參數介面

```xs
// 建立下拉式選單
input: _mode(1, "交易模式", inputkind:=dict(["金額",1],["張數",2]));

// 建立日期區間選擇器
input: _mydate(20230101, "起始日期", inputkind:=daterange(20200101,20240101,"d"));

if _mode = 1 then begin
    // 金額模式邏輯
end else begin
    // 張數模式邏輯
end;
```

### 五、達人鎖碼（優惠碼解鎖）

達人上架策略 / 指標時，可用 `referralcode` 把腳本「鎖」給綁定特定優惠碼的用戶 —— 沒綁碼的人執行時直接跳錯誤、看不到內容。

| 函數 | 說明 | 回傳 |
|------|------|------|
| `referralcode("優惠碼")` | 判斷目前帳號是否已綁定指定優惠碼 | 布林值（已綁定 → `true`；未綁定 → `false`） |

```xs
// 標準鎖碼寫法：放在腳本最上方（邏輯判斷區第一行）
// 未綁定優惠碼 @MOFI 的用戶 → 直接 RaiseRunTimeError 中斷，看不到後續內容
if referralcode("@MOFI") = false then
    raiseruntimeerror("請綁定優惠碼 @MOFI 解鎖");
```

- **優惠碼帶 `@` 前綴**（例：`@MOFI`），整串當字串傳入。
- **務必放在腳本最前面**（頻率防呆之後、實際運算之前），未綁碼就提早中斷，避免運算內容外洩。
- 四大類腳本（指標／選股／警示／交易）皆適用，是達人策略上架的標準保護手段。

#### 老墨標準鎖碼寫法（含白名單）

老墨上架腳本一律用「綁碼 **或** 白名單帳號」的雙條件，讓自己與授權帳號免綁碼也能跑。`userid` 是系統內建變數，回傳目前執行帳號 ID。白名單帳號清單（2026-06 更新）：`mophyfeix`、`mophyfei113011`、`alicelee`、`coco111444`、`emmachou0324`。

```xs
// 老墨標準鎖碼：未綁定 @MOFI、且不在白名單者 → 直接中斷
if referralcode("@MOFI") = false
    and userid <> "mophyfeix" and userid <> "mophyfei113011"
    and userid <> "alicelee" and userid <> "coco111444"
    and userid <> "emmachou0324" then
    raiseruntimeerror("無使用權限、請綁定優惠碼 @MOFI 解鎖");
```

- 白名單用 `userid <> "..."` 逐個 `and` 串接（全部不符才中斷）。
- 新增 / 移除白名單帳號時同步更新此清單。
