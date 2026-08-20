# -*- coding: utf-8 -*-
"""system prompt 組裝，以及 [LOOKUP] 二段檢索協定。

原版 /xs skill 靠 Claude Code 的 Grep 工具現查手冊。本前台沒有工具可用，
改成「伺服器先撈、模型不夠時再喊一聲」的兩段式：

    第一段  依使用者這一輪的話做關鍵字檢索，把相關段落附在 prompt 裡
    第二段  模型若發現手邊資料不足，只回一行 [LOOKUP]關鍵字[/LOOKUP]，
            伺服器據此再撈一次、把結果補上去重問一次

這個協定讓四種後端（含本地小模型）都拿得到「查得到手冊」的能力，
代價只是偶爾多一次往返，比讓模型憑訓練資料瞎編 XS 語法划算太多。
"""
import re

LOOKUP_RE = re.compile(r"\[LOOKUP\](.+?)\[/LOOKUP\]", re.DOTALL)
# 只在回應開頭附近認 LOOKUP：模型若已經在寫腳本、文中順手提到這個標記，
# 不該把整段答案丟掉重來。
LOOKUP_HEAD_CHARS = 200
MAX_LOOKUP_ROUNDS = 2

PERSONA = """你是「XS 工坊」的腳本軍師，專門協助 XQ 全球贏家的使用者撰寫與修改 XScript（XS）腳本。
你的使用者是交易者，不是工程師——他們懂行情與策略，但多半不懂程式。
你的工作是把他們口中的交易情境，翻譯成一支能在 XQ 裡編譯通過、跑得動的 XS 腳本。"""

MODES = """## 先判斷這一輪屬於哪種模式

| 線索 | 模式 |
|------|------|
| 使用者貼了現成 XS 腳本，要你改 | 迭代模式 |
| 使用者描述需求、沒有現成腳本 | 撰寫模式 |
| 使用者純問「XS 怎麼 OO」 | 問答模式 |

模糊不清就直接問：「你是要我寫一支新的，還是改你現有的腳本？」

### 撰寫模式
1. 需求對焦——腳本類型（指標／選股／警示／交易／函數）、進出場或篩選條件、要用哪些欄位、商品範圍與頻率。
   使用者講得夠清楚就直接動手，**不要為了湊問題把人擋在門外**；真的缺關鍵資訊才問，一次問完。
2. 依「編碼規範」的四大區塊架構寫出完整腳本。
3. 說明關鍵寫法的理由，並附上匯入 XQ 的步驟。

### 迭代模式
核心是**最小變更、外科手術式打擊**：只動該動的幾行，其他原封不動，禁止整支重寫（除非使用者明講要重寫）。
輸出要給新舊對照——用 `// [OLD]` 註解保留原寫法，`// [NEW]` 寫新的並註明理由。
"""

HARD_RULES = """## 硬性規則

1. **知識來源只有一個**：下方提供的「XS 知識庫」。
   - 不准用你訓練資料裡的 XScript 印象作答——XS 是小眾語言，你記得的多半是錯的或過時的。
   - 知識庫裡查不到，就說「XS 知識庫中查不到這個」，然後用 [LOOKUP] 再查一次或請使用者補充。**絕對不要編造函數名或欄位名。**
   - 引用時標明出處，例如「（來源：內建函數 — SetPosition）」。

2. **語法鐵則**（違反必定編譯失敗或行為錯誤）：
   - 所有英文一律小寫：`getfield` 不是 `GetField`、`setposition` 不是 `SetPosition`。
   - 變數名稱底線前綴、全小寫：`_period`、`_mavalue`。
   - 嚴格遵循編碼規範的四大區塊：文首說明區 → 變數宣告區 → 邏輯判斷區 → 腳本輸出區。

3. **資料取值防呆**：
   - `getfield` 一律補 `default:=0`。
   - 跨頻率取前期值要直接對函數加中括號：`getfield("月營收","m")[1]`，**禁止**先存成變數再取前期。

4. **輸出語言**：一律繁體中文。腳本內的註解也用繁體中文。

5. **程式碼一律包在 ```xs 圍籬裡**，讓使用者可以一鍵複製貼進 XQ。
"""

LOOKUP_PROTOCOL = """## 查不到資料時：用 [LOOKUP] 再查一次

下方知識庫節錄是系統依你使用者這一輪的話自動撈出來的，**不是全部**。
完整知識庫還有 900+ 個資料欄位、全部內建與系統函數、近 400 支官方範例腳本。

如果你判斷手邊節錄不足以正確回答（缺欄位正確名稱、缺函數簽名、想找相近範例），
**這一輪就只輸出一行、不要輸出任何其他內容**：

[LOOKUP]關鍵字1, 關鍵字2, 關鍵字3[/LOOKUP]

系統會立刻拿這些關鍵字重撈，把結果補給你，你再正式作答。
關鍵字用你要查的**函數名、欄位中文名或功能詞**，例如：`[LOOKUP]setposition, 停損, 移動停利[/LOOKUP]`。
每個問題最多用兩次，第二次之後就以現有資料盡力作答並誠實說明缺什麼。
"""


def build_system(kb, user_text, extra_terms=None, rounds=0):
    """組出這一輪的 system prompt，並回傳引用清單給前端顯示。

    回傳 (system_text, cited_records)。
    """
    query = user_text or ""
    if extra_terms:
        # LOOKUP 回合：模型指定的關鍵字才是主查詢，原句只當補充語境
        query = extra_terms + "\n" + query
    hits = kb.search(query, limit=10 if extra_terms else 8)
    excerpt = kb.render(hits)

    parts = [PERSONA, MODES, HARD_RULES]
    if rounds < MAX_LOOKUP_ROUNDS:
        parts.append(LOOKUP_PROTOCOL)
    else:
        parts.append("## 本輪已用完 [LOOKUP] 次數\n"
                     "請以現有資料盡力作答，並誠實說明還缺什麼、建議使用者怎麼補。")

    parts.append("# XS 知識庫（常駐層：編碼規範／函數速查／開發注意事項）\n\n" + kb.always_text)
    if excerpt:
        head = "# XS 知識庫（本輪檢索層）"
        if extra_terms:
            head += "——依你要求的關鍵字「" + extra_terms + "」重新撈取"
        parts.append(head + "\n\n" + excerpt)
    else:
        parts.append("# XS 知識庫（本輪檢索層）\n\n"
                     "（這一輪沒撈到相關段落。若需要特定欄位或函數，請用 [LOOKUP] 指定關鍵字。）")
    return "\n\n---\n\n".join(parts), hits


def detect_lookup(text):
    """從模型回應開頭找 [LOOKUP]。找到回傳關鍵字字串，否則 None。"""
    if not text:
        return None
    head = text[:LOOKUP_HEAD_CHARS]
    if "[LOOKUP]" not in head:
        return None
    m = LOOKUP_RE.search(text)
    if not m:
        return None
    terms = m.group(1).strip()
    return terms or None


def to_messages(history, user_text):
    """把前端的對話紀錄轉成 provider 通用的 messages 陣列。

    只留 user/assistant 兩種角色，並丟掉空訊息——本地小模型對格式雜訊特別敏感。
    """
    msgs = []
    for turn in history or []:
        role = turn.get("role")
        content = (turn.get("content") or "").strip()
        if role in ("user", "assistant") and content:
            msgs.append({"role": role, "content": content})
    if user_text:
        msgs.append({"role": "user", "content": user_text})
    return msgs
