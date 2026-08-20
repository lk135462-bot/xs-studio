# -*- coding: utf-8 -*-
"""xs-skill 知識庫的索引與檢索。

為什麼要自己做檢索：原版 /xs skill 跑在 Claude Code 裡，靠 Read／Grep 工具翻手冊。
本前台要能接 API key、OpenRouter、本地模型——那些後端沒有檔案工具。所以檢索必須
做在伺服器這一側，由我們把該看的段落餵進 prompt，四種後端才會有一致的品質。

知識庫共 2.4 MB，全塞進 prompt 既貴又會稀釋重點。因此分兩層：
    常駐層  編碼規範＋函數速查＋開發注意事項（每一輪都在，約 40 KB）
    檢索層  依這一輪的問題撈相關段落（欄位／函數／範例腳本），有預算上限

切段規則：手冊與範例庫都是「一個 `## ` 標題一筆」的結構——
351 個資料欄位、179 個內建函數、395 支官方範例腳本，切出來就是乾淨的原子單位。
"""
import re
from pathlib import Path

from .paths import data_dir

APP_DIR = data_dir()
KNOWLEDGE_DIR = APP_DIR / "knowledge"

# 檔名關鍵字 → 類別。類別決定它進常駐層還是檢索層、以及檢索時的權重。
_ALWAYS = "always"        # 常駐：每輪都注入全文
_SEARCH = "search"        # 檢索：依需求撈段落

_FILE_ROLES = [
    ("XScriptGuideline",                _ALWAYS, "編碼規範",        3.0),
    ("XScript_Functions_QuickRef",      _ALWAYS, "函數速查",        3.0),
    ("XScript_Dev_Practical_Notes",     _ALWAYS, "開發注意事項",    3.0),
    ("XScript_Syntax_Reference",        _SEARCH, "語法結構",        1.6),
    ("XScript_Reserved_Keywords",       _SEARCH, "保留字",          1.2),
    ("XScript_BuiltIn_Functions",       _SEARCH, "內建函數",        1.8),
    ("XScript_System_Functions",        _SEARCH, "系統函數",        1.8),
    ("XScript_SDT_Functions",           _SEARCH, "SDT 共享資料表",  1.5),
    ("DataField_General_Data",          _SEARCH, "一般資料欄位",    1.5),
    ("DataField_RealTime_Quotes",       _SEARCH, "即時報價欄位",    1.5),
    ("DataField_Stock_Selection",       _SEARCH, "選股資料欄位",    1.5),
    ("XQ_Scripts_Indicators",           _SEARCH, "指標範例",        1.3),
    ("XQ_Scripts_StockSelection",       _SEARCH, "選股範例",        1.3),
    ("XQ_Scripts_Alerts",               _SEARCH, "警示範例",        1.3),
    ("XQ_Scripts_Trading",              _SEARCH, "交易範例",        1.3),
    ("XQ_Scripts_Functions",            _SEARCH, "函數範例",        1.3),
    ("XQ_Backtest_Debug_UI",            _SEARCH, "回測 UI 規格",    1.0),
]

# 腳本類型 → 該優先加權的範例庫。使用者說「寫個選股」時，選股範例要浮上來。
KIND_BOOST = {
    "indicator": "指標範例",
    "selection": "選股範例",
    "alert":     "警示範例",
    "trading":   "交易範例",
    "function":  "函數範例",
}

# 從使用者的話判斷腳本類型。只用來加權，判斷錯了不會擋住其他來源。
_KIND_HINTS = [
    ("selection", ("選股", "篩選", "掃描全市場", "選出", "ret=1", "ret =1")),
    ("alert",     ("警示", "雷達", "提醒", "通知", "alert")),
    ("trading",   ("交易", "自動交易", "回測", "進場", "出場", "停損", "停利",
                   "setposition", "多單", "空單", "部位")),
    ("indicator", ("指標", "畫線", "副圖", "主圖", "plot", "plotk", "均線", "背離")),
    ("function",  ("自訂函數", "寫個函數", "共用函數")),
]

_HEADING = re.compile(r"^## +(.+?)\s*$", re.MULTILINE)
_ASCII_TERM = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]{1,}")
_CJK = re.compile(r"[一-鿿]{2,}")
# 手冊標題常帶 <kbd>常用</kbd> 這類標籤，比對前先剝掉
_TAG = re.compile(r"<[^>]+>")


class Record:
    """知識庫裡的一個原子段落（一個欄位／一個函數／一支範例腳本）。"""

    __slots__ = ("source", "title", "text", "weight", "_lt", "_lx")

    def __init__(self, source, title, text, weight):
        self.source = source          # 來源類別，例如「內建函數」
        self.title = title
        self.text = text
        self.weight = weight
        self._lt = _TAG.sub("", title).lower()      # 比對用小寫標題
        self._lx = text.lower()                     # 比對用小寫全文

    def cite(self):
        return f"{self.source} — {self.title}"


class KnowledgeBase:
    def __init__(self, root: Path = KNOWLEDGE_DIR):
        self.root = Path(root)
        self.always_text = ""
        self.records = []
        self.files = []
        self.missing = not self.root.is_dir()
        if not self.missing:
            self._build()

    # ── 索引建置 ──────────────────────────────────────────────────────────
    def _role_of(self, path: Path):
        name = path.name
        for key, mode, source, weight in _FILE_ROLES:
            if key in name:
                return mode, source, weight
        # 認不得的檔案仍收進檢索層——使用者自己往 knowledge/ 丟補充資料時要吃得到
        return _SEARCH, path.stem, 1.0

    def _build(self):
        always_parts = []
        for path in sorted(self.root.rglob("*.md")):
            if path.name == "SKILL.md":
                continue          # 那是 Claude Code 的載入器，本前台自己有 prompt 層
            try:
                text = path.read_text(encoding="utf-8")
            except Exception:
                continue
            mode, source, weight = self._role_of(path)
            self.files.append({"name": path.name, "source": source, "mode": mode,
                               "chars": len(text)})
            if mode == _ALWAYS:
                always_parts.append(f"===== {source}（{path.name}）=====\n{text.strip()}")
            else:
                self.records.extend(self._split(text, source, weight))
        self.always_text = "\n\n".join(always_parts)

    def _split(self, text, source, weight):
        """依 `## ` 標題切段。標題前的序言自成一筆，才不會漏掉檔案開頭的說明。"""
        out = []
        marks = list(_HEADING.finditer(text))
        if not marks:
            return [Record(source, source, text.strip(), weight)]
        head = text[: marks[0].start()].strip()
        if len(head) > 40:
            out.append(Record(source, source + "（總說明）", head, weight))
        for i, m in enumerate(marks):
            end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
            body = text[m.start():end].strip()
            if body:
                out.append(Record(source, m.group(1).strip(), body, weight))
        return out

    # ── 檢索 ──────────────────────────────────────────────────────────────
    @staticmethod
    def terms(query: str):
        """把問題拆成比對詞：英文識別字 + 中文 2/3 連字。

        中文沒有空白可切，用 n-gram 是這裡最划算的做法——不必帶進中文斷詞套件，
        綠色免安裝包才能維持零額外相依。
        """
        q = query or ""
        found = {t.lower() for t in _ASCII_TERM.findall(q)}
        for chunk in _CJK.findall(q):
            for n in (2, 3):
                for i in range(len(chunk) - n + 1):
                    found.add(chunk[i:i + n])
        return {t for t in found if len(t) >= 2}

    @staticmethod
    def guess_kind(query: str):
        q = (query or "").lower()
        for kind, hints in _KIND_HINTS:
            if any(h.lower() in q for h in hints):
                return kind
        return None

    def search(self, query, limit=8, budget_chars=45000, kind=None, per_source=3):
        """回傳排序後的 Record。

        budget_chars 是「撈回來的段落總字數」上限；per_source 限制同一來源最多幾筆。
        限制來源是有理由的：範例腳本又短又多，純比分數會讓五筆全是範例，
        把「這個欄位到底叫什麼名字」的手冊條目擠掉——而那才是寫錯最多的地方。
        """
        if self.missing or not self.records:
            return []
        terms = self.terms(query)
        if not terms:
            return []
        boost_source = KIND_BOOST.get(kind or self.guess_kind(query) or "")
        scored = []
        for rec in self.records:
            score = 0.0
            for t in terms:
                if t in rec._lt:
                    # 標題命中最有力：「getfield」出現在標題＝這就是那一條
                    score += 12.0 * (2.0 if rec._lt == t else 1.0)
                hits = rec._lx.count(t)
                if hits:
                    # 次數取上限，避免長檔靠篇幅刷分把短而準的條目壓下去
                    score += min(hits, 6) * 1.0
            if score <= 0:
                continue
            score *= rec.weight
            if boost_source and rec.source == boost_source:
                score *= 1.6
            scored.append((score, rec))
        scored.sort(key=lambda x: (-x[0], len(x[1].text)))
        out, used, taken = [], 0, {}
        # 兩輪：第一輪守 per_source 配額拿到跨來源的組合，第二輪若還有預算再補滿
        for allow_overflow in (False, True):
            for score, rec in scored:
                if len(out) >= limit:
                    break
                if rec in out:
                    continue
                if not allow_overflow and taken.get(rec.source, 0) >= per_source:
                    continue
                chunk = len(rec.text)
                if used + chunk > budget_chars:
                    if out:
                        continue      # 這條太肥，跳過看下一條，別直接收工
                    rec = Record(rec.source, rec.title,
                                 rec.text[:budget_chars] + "\n…（本段過長已截斷）", rec.weight)
                    chunk = len(rec.text)
                out.append(rec)
                taken[rec.source] = taken.get(rec.source, 0) + 1
                used += chunk
            if len(out) >= limit:
                break
        return out

    def render(self, records):
        if not records:
            return ""
        parts = []
        for rec in records:
            parts.append("----- 【" + rec.source + "】" + rec.title + " -----\n" + rec.text)
        return "\n\n".join(parts)

    def stats(self):
        return {
            "ready": not self.missing,
            "files": len(self.files),
            "records": len(self.records),
            "always_chars": len(self.always_text),
            "detail": self.files,
        }


_KB = None


def get_kb(force=False) -> KnowledgeBase:
    """單例。知識庫是唯讀的，建一次索引全程共用。"""
    global _KB
    if _KB is None or force:
        _KB = KnowledgeBase()
    return _KB
