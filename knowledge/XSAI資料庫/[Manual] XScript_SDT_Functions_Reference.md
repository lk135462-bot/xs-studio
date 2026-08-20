---
title: XS完整手冊 - SDT 共享資料表函數
category: 系統函數
tags: [XS語法, SDT, 共享資料表, SharedDataTable, SDT_SetValue, SDT_GetValue, SDT_SetString, SDT_GetString, SDT_SetValueIf, SDT_SetStringIf, SDT_HasKey, SDT_GetKeys, SDT_RemoveKey, SDT_RemoveAll, SDT_SetColumnName, SDT_Sum, SDT_Average, SDT_Max, SDT_Min, SDT_Median, SDT_Sort, SDT_SortKey, SDT_SortString, 跨商品排名, 全市場排名]
source: https://xshelp.xq.com.tw/XSHelp/lists?a=SDTFUNC
fetched: 2026-08-10
version_introduced: XQ 個人版 3.20.01 / 企業版 7.20.01
total_functions: 38（19 種 × 商品範圍／策略範圍兩版）
---

# SDT 共享資料表函數 (完整收錄)

> 本文件收錄 XSHelp「SDT函數」(`group=SDTFUNC`) 分類下的全部 38 筆，共 19 種函數，每種都有
> **商品範圍版**與**策略範圍版（函數名加 `_L` 後綴）**兩個版本。
> 2026-08-10 自 XSHelp 官網逐頁抓取。§0 的補充說明來自 XQ 3.20.01 版本說明 PPT 的 Demo Q&A。

---

## 0. SDT 是什麼（先讀這段）

**SDT = Shared Data Table，共享資料表**。它是一種類似表格的共享資料結構：

| 概念 | 說明 |
|---|---|
| **row（列）** | 用 **key** 索引。key 是字串，**通常為商品代碼**，**大小寫不分** |
| **column（行）** | 可用 **1~100 的數字**，也可以用 **直行名稱字串** |
| **容量上限** | **row 上限 5000、column 上限 100** |
| **兩種範圍** | **商品範圍**：單一商品內使用（原函數名）<br>**策略範圍**：同一策略內共用（函數名加 `_L` 後綴） |
| **csv 連結** | 在**自動交易**中可與 csv 檔案連結 |

### 為什麼重要

XS 的執行模型是「每個商品各跑各的腳本」，**跨商品的橫向比較一直很難做**。SDT 提供一張所有商品都能寫入、
都能讀取的共用表，因此可以做出「把每一檔的分數寫進同一張表 → 排序 → 取前 N 名」這類
**全市場排名（cross-sectional ranking）** 的邏輯 —— 這在此之前，選股腳本要靠 `rank` 區塊、
而指標／警示／交易腳本根本做不到。

### 使用限制與已知行為（來自 3.20.01 Demo Q&A，官方回覆）

1. **回測會失敗**：「包含 SDT 語法的腳本回測時會出現錯誤」。SDT 不是回測時被跳過，是**直接報錯**。
2. **資料讀取筆數階段就會運作**：資料讀取筆數運算時就可以寫入 SDT。
3. **csv 只在啟動時讀一次**：啟動後不會再讀取，**也不會偵測檔案異動後重讀**。
4. **csv 寫回是定期的**：程式內有 Timer **每 10 秒**檢查有啟用「異動自動儲存 csv」的 SDT，
   發現內容有異動就寫回 csv。
5. **閃退不保證完整**：DAQEngine 閃退時，無法確保 csv 保存到 SDT 的最新狀態，也無法保證 csv 完整性。

### 快速上手骨架

```pascal
// 寫入：把自己的分數放進共用表
SDT_SetValue_L(symbol, "分數", value1);

// 排序：拿到依「分數」由大到小排好的 key 陣列
Array: sortedKeys[5000]("");
SDT_Sort_L("分數", sortedKeys, order:=1);

// 讀取：取第一名的分數
value2 = SDT_GetValue_L(sortedKeys[1], "分數", default:=0);
```

> ⚠️ `_L`（策略範圍）與無後綴（商品範圍）**語法完全相同**，差別只在資料的共用範圍。
> 要做跨商品排名，**必須用 `_L` 版本**，否則每個商品各自有一張表、比較不到別人。

---

## 函數總表

| 函數 | 用途 |
|---|---|
| `SDT_SetValue` / `_L` | 寫入 SDT 數值欄位 |
| `SDT_GetValue` / `_L` | 讀取 SDT 數值欄位 |
| `SDT_SetString` / `_L` | 寫入 SDT 字串欄位 |
| `SDT_GetString` / `_L` | 讀取 SDT 字串欄位 |
| `SDT_SetValueIf` / `_L` | 條件寫入數值（比對舊值才覆寫） |
| `SDT_SetStringIf` / `_L` | 條件寫入字串（比對舊值才覆寫） |
| `SDT_HasKey` / `_L` | 檢查 key 是否存在 |
| `SDT_GetKeys` / `_L` | 取得所有 key |
| `SDT_RemoveKey` / `_L` | 移除指定 key 及該列資料 |
| `SDT_RemoveAll` / `_L` | 清空整張表 |
| `SDT_SetColumnName` / `_L` | 設定／修改直行名稱 |
| `SDT_Sum` / `_L` | 指定行加總 |
| `SDT_Average` / `_L` | 指定行平均 |
| `SDT_Max` / `_L` | 指定行最大值與對應 key |
| `SDT_Min` / `_L` | 指定行最小值與對應 key |
| `SDT_Median` / `_L` | 指定行中位數與對應 key |
| `SDT_Sort` / `_L` | 依指定行的**數值**排序，輸出 key 陣列 |
| `SDT_SortString` / `_L` | 依指定行的**字串**排序，輸出 key 陣列 |
| `SDT_SortKey` / `_L` | 依 **key** 排序，輸出 key 陣列 |

---

## SDT_SetValue
--- 

### SDT_SetValue
#### SDT_SetValue – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> 寫入 SDT 中指定欄位的數值。  
> **SDT_SetValue(key, column, value)**  
> 傳入三個參數：  
> - `key`：要寫入的資料列鍵值，字串，**大小寫不分**。  
> - `column`：要寫入的直行，可傳入 **1~100 的數字**，或**直行名稱字串**。  
> - `value`：要寫入的數值。  

---

##### 說明
- 若 `column` 為字串且不存在，**會在最後一行之後新增該行**。
- 若 `column` 傳數字且大於現有行數，**會建立中間的空白欄位**。
- **欄號超過 100，或直行總數超過 100 時會回傳錯誤。**

策略範圍版本：`SDT_SetValue_L(key, column, value)`

___

## SDT_GetValue
--- 

### SDT_GetValue
#### SDT_GetValue – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> 取得 SDT 中指定欄位的數值。  
> **回傳數值=SDT_GetValue(key, column, default:=0)**  
> - `key`（必填）：要讀取的資料列鍵值，字串，可為商品代碼或任意字串，大小寫不分。  
> - `column`（必填）：要讀取的直行，可傳入 1~100 的數字，或直行名稱字串。  
> - `default`（選填）：當 key 或 column 不存在時要回傳的預設值，**預設為 0**。  

---

##### 說明
回傳指定位置的數值。若找不到鍵值或欄位則回傳預設值。
**若欄位實際存放的是字串，會嘗試自動轉為數值**，轉換失敗回傳 0。

策略範圍版本：`SDT_GetValue_L(key, column, default:=0)`

___

## SDT_SetString
--- 

### SDT_SetString
#### SDT_SetString – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> 寫入 SDT 中指定欄位的字串。  
> **SDT_SetString(key, column, value)**  
> - `key`：要寫入的資料列鍵值，字串，大小寫不分。  
> - `column`：要寫入的直行，可傳入 1~100 的數字，或直行名稱字串。  
> - `value`：要寫入的字串內容。  

---

##### 說明
- 若 `column` 為字串且不存在，會在最後一行之後新增該行。
- 若 `column` 傳數字且大於現有行數，會自動補齊中間的空白欄位。
- 欄號超過 100 或直行總數超過 100 時會回傳錯誤。

策略範圍版本：`SDT_SetString_L(key, column, value)`

___

## SDT_GetString
--- 

### SDT_GetString
#### SDT_GetString – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> 讀取 SDT 中指定欄位的字串。  
> **回傳字串=SDT_GetString(key, column, default:="")**  
> - `key`（必填）：資料列鍵值，字串，不區分大小寫。  
> - `column`（必填）：要存取的欄位，可用 1~100 的數字或欄位名稱字串。  
> - `default`（選填）：鍵值或欄位不存在時的預設回傳值，**預設為空字串**。  

---

##### 說明
回傳指定位置的字串內容。**若欄位實際存放的是數值，會自動轉為字串**（轉換樣式由系統決定）。

策略範圍版本：`SDT_GetString_L(key, column, default:="")`

___

## SDT_SetValueIf
--- 

### SDT_SetValueIf
#### SDT_SetValueIf – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> SDT 條件寫入數值。  
> **回傳布林值=SDT_SetValueIf(key, column, newvalue, oldvalue)**  
> - `key`：目標資料列鍵值，字串，大小寫不分。  
> - `column`：目標直行，1~100 的數字或直行名稱字串。  
> - `newvalue`：要寫入的新數值。  
> - `oldvalue`：**預期的現有數值**，用於驗證。  

---

##### 說明
**只有在目前 SDT 指定欄位數值等於 `oldvalue` 時，才會將其覆寫為 `newvalue` 並回傳 True；
否則不寫入並回傳 False。**

用途：這是 SDT 的**原子性寫入（compare-and-swap）**機制，可確保
**同一時間點只有一個商品或策略能成功寫入**。做「先搶先贏」的部位配額、
或避免多商品同時搶寫同一格時，用這個而不是 `SDT_SetValue`。

策略範圍版本：`SDT_SetValueIf_L(key, column, newvalue, oldvalue)`

___

## SDT_SetStringIf
--- 

### SDT_SetStringIf
#### SDT_SetStringIf – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> SDT 條件寫入字串。  
> **回傳布林值=SDT_SetStringIf(key, column, newvalue, oldvalue)**  
> - `key`：要寫入的資料列鍵值，字串，大小寫不分。  
> - `column`：要寫入的直行，1~100 的數字或直行名稱字串。  
> - `newvalue`：欲寫入的新字串。  
> - `oldvalue`：預期的目前字串，用於比對驗證。  

---

##### 說明
**只有在目前 SDT 指定欄位字串等於 `oldvalue` 時，才會將其覆寫為 `newvalue`** 並回傳 True；
不符合時回傳 False 且不寫入。與 `SDT_SetValueIf` 同為原子性寫入保護。

策略範圍版本：`SDT_SetStringIf_L(key, column, newvalue, oldvalue)`

___

## SDT_HasKey
--- 

### SDT_HasKey
#### SDT_HasKey – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> 檢查字串是否存在 SDT key 中。  
> **回傳布林值=SDT_HasKey(key)**  
> - `key`：要檢查的資料列鍵值，字串，**大小寫不分**。  

---

##### 說明
key 存在時回傳 `True`，不存在回傳 `False`。

策略範圍版本：`SDT_HasKey_L(key)`

___

## SDT_GetKeys
--- 

### SDT_GetKeys
#### SDT_GetKeys – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> 取得 SDT 中目前所有的 key。  
> **SDT_GetKeys(output_key_array)**  
> - `output_key_array`：一維字串陣列（輸出用），函數會把 SDT 內目前存在的 key 寫入此陣列。  

---

##### 說明
⚠️ **取回的 key 沒有保證順序** —— 寫入順序與取回順序不一致。
若需要依序處理，改用 `SDT_SortKey` 或 `SDT_Sort`。

策略範圍版本：`SDT_GetKeys_L(output_key_array)`

___

## SDT_RemoveKey
--- 

### SDT_RemoveKey
#### SDT_RemoveKey – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> 移除指定 SDT key。  
> **SDT_RemoveKey(key)**  
> - `key`：要移除的資料列鍵值，字串，大小寫不分。  

---

##### 說明
將指定 key 對應的**整列資料移除**，key 本身也會被刪除。

策略範圍版本：`SDT_RemoveKey_L(key)`

___

## SDT_RemoveAll
--- 

### SDT_RemoveAll
#### SDT_RemoveAll – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> 清空整個 SDT。  
> **SDT_RemoveAll()**  
> 無參數。  

---

##### 說明
一次移除此 SDT 內的所有資料（**清空整張表**）。

策略範圍版本：`SDT_RemoveAll_L()`

___

## SDT_SetColumnName
--- 

### SDT_SetColumnName
#### SDT_SetColumnName – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> 設定 SDT 直行名稱。  
> **SDT_SetColumnName(column_num, column_name)**  
> - `column_num`：要命名的直行序號（數字）。  
> - `column_name`：該直行的新名稱（字串）。  

---

##### 說明
將 SDT 中第 `column_num` 行的名稱設定或修改為 `column_name`。
適用於初次建立 SDT 時未指定欄名、或要修改既有欄名的情況，
通常搭配 `SDT_SetValue` / `SDT_SetString` 使用。

策略範圍版本：`SDT_SetColumnName_L(column_num, column_name)`

___

## SDT_Sum
--- 

### SDT_Sum
#### SDT_Sum – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> 取得 SDT 中指定行的數值加總。  
> **回傳數值=SDT_Sum(column)**  
> - `column`（必填）：要加總的直行，1~100 的數字或直行名稱字串。  

---

##### 說明
統計前會嘗試將直行值轉為數值，**無法轉換的列以 0 計算**。

策略範圍版本：`SDT_Sum_L(column)`

___

## SDT_Average
--- 

### SDT_Average
#### SDT_Average – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> 取得 SDT 中指定行的數值平均。  
> **回傳數值=SDT_Average(column)**  
> - `column`（必填）：要計算平均的直行，1~100 的數字或直行名稱字串。  

---

##### 說明
統計前會嘗試將直行值轉為數值，**無法轉換的列以 0 計算後納入平均**
（注意：不是排除，是當成 0 一起算）。

策略範圍版本：`SDT_Average_L(column)`

___

## SDT_Max
--- 

### SDT_Max
#### SDT_Max – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> 取得 SDT 中指定行的最大值以及對應 key。  
> **回傳數值=SDT_Max(column)**  
> **回傳數值=SDT_Max(column, output_key)**  
> - `column`（必填）：要取最大值的直行，1~100 的數字或直行名稱字串。  
> - `output_key`（選填）：字串變數，接收最大值所在列的 key。  

---

##### 說明
- **無法轉為數值的列會被忽略**（與 Sum／Average 的「以 0 計算」不同）。
- 多個 key 擁有相同最大值時，`output_key` 回傳**字串排序較小的 key**。

策略範圍版本：`SDT_Max_L(column [, output_key])`

___

## SDT_Min
--- 

### SDT_Min
#### SDT_Min – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> 取得 SDT 中指定行的最小值以及對應 key。  
> **回傳數值=SDT_Min(column)**  
> **回傳數值=SDT_Min(column, output_key)**  
> - `column`（必填）：要取最小值的直行，1~100 的數字或直行名稱字串。  
> - `output_key`（選填）：字串變數，接收最小值所在列的 key。  

---

##### 說明
- 無法轉為數值的列會被忽略。
- 多個 key 擁有相同最小值時，`output_key` 回傳字串排序較小的 key。

策略範圍版本：`SDT_Min_L(column [, output_key])`

___

## SDT_Median
--- 

### SDT_Median
#### SDT_Median – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> 取得 SDT 中指定行的中位數以及對應 key。  
> **回傳數值=SDT_Median(column)**  
> **回傳數值=SDT_Median(column, output_key)**  
> - `column`（必填）：要計算中位數的直行，1~100 的數字或直行名稱字串。  
> - `output_key`（選填）：字串變數，接收中位數所在列的 key。  

---

##### 說明
計算時**排除無法轉為數值的列**。

策略範圍版本：`SDT_Median_L(column [, output_key])`

___

## SDT_Sort
--- 

### SDT_Sort
#### SDT_Sort – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> 取得依照 SDT 指定行的**數值**排序後的 key 陣列。  
> **SDT_Sort(column, sorted_key_array, order:=-1)**  
> - `column`：作為排序依據的直行，1~100 的數字或直行名稱字串。  
> - `sorted_key_array`：一維字串陣列（輸出用），接收排序後的 key。  
> - `order`（選填）：排序方向，**-1 為由小到大（預設）**、**1 為由大到小**。  

---

##### 說明
**欄位值會先轉為數值再排序，無法轉換的列會排在陣列最後面。**

> 做「全市場前 N 強」時，記得 `order:=1`（由大到小），預設的 -1 是由小到大。

策略範圍版本：`SDT_Sort_L(column, sorted_key_array, order:=-1)`

___

## SDT_SortString
--- 

### SDT_SortString
#### SDT_SortString – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> 取得依照 SDT 指定行的**字串**排序後的 key 陣列。  
> **SDT_SortString(column, sorted_key_array, order:=-1)**  
> - `column`：作為排序依據的直行，1~100 的數字或直行名稱字串。  
> - `sorted_key_array`：一維字串陣列（輸出用），接收排序後的 key。  
> - `order`（選填）：-1 為由小到大（預設）、1 為由大到小。  

---

##### 說明
欄位值會先轉為字串後排序，**無法轉換的列置於結果最後面**。

策略範圍版本：`SDT_SortString_L(column, sorted_key_array, order:=-1)`

___

## SDT_SortKey
--- 

### SDT_SortKey
#### SDT_SortKey – （系統函數） <kbd>SDT函數</kbd>

##### 語法
> 依 SDT 的 **key** 排序，並將排序後的 key 寫入字串陣列。  
> **SDT_SortKey(sorted_key_array, order:=-1)**  
> - `sorted_key_array`：一維字串陣列（輸出用），接收排序後的 key。  
> - `order`（選填）：-1 為由小到大（預設）、1 為由大到小。  

---

##### 說明
便於在腳本中依序讀取各列資訊（`SDT_GetKeys` 取回的 key 是沒有順序的，需要固定順序就用這個）。

策略範圍版本：`SDT_SortKey_L(sorted_key_array, order:=-1)`

___

## 綜合應用範例：全市場相對強度排名

```pascal
// ============================================================
// 腳本名稱：用 SDT 做跨商品相對強度排名
// 邏輯說明：每檔商品把自己的 20 日報酬率寫進共用表，再排序取出前 10 名
// ============================================================

// ------------------------------
// 1. 變數宣告區
// ------------------------------
input:
    _lookback(20, "報酬率計算期數"),
    _topn(10, "取前幾名");

var:
    _ret(0), _myrank(0), _i(0);

array:
    _sortedkeys[5000]("");

// ------------------------------
// 2. 邏輯判斷區
// ------------------------------
if currentbar > _lookback then begin
    // 算自己的報酬率，寫進策略範圍的共用表
    _ret = (close / close[_lookback] - 1) * 100;
    SDT_SetColumnName_L(1, "報酬率");
    SDT_SetValue_L(symbol, "報酬率", _ret);

    // 依報酬率由大到小排序，拿回 key 陣列
    SDT_Sort_L("報酬率", _sortedkeys, order:=1);

    // 找出自己排第幾名
    _myrank = 0;
    for _i = 1 to _topn begin
        if _sortedkeys[_i] = symbol then _myrank = _i;
    end;
end;

// ------------------------------
// 3. 腳本輸出區
// ------------------------------
if _myrank > 0 and _myrank <= _topn then ret = 1;
```

> ⚠️ 這支**不能拿去回測**（含 SDT 語法的腳本回測會出現錯誤），只能在即時環境跑。
> ⚠️ 陣列宣告上限請留意 `XScriptGuideline.md` 第三節的 1002 錯誤防呆（單一陣列元素上限約 7000）。
