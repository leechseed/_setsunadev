#!/usr/bin/env python
"""mcdp_codex_build.py — build the MCDP Codex (BOLO 33) from the eleven MIL one-sheets.

Reads  _0.1_BVX_LEARN/KNOWLEDGE_AREAS/🧬 MIL.*.md  (+ _meta/VOCABULARY.md, + _vocab/*.vocab.md)
Emits  a JSON data model, and injects it into the HTML template to produce the single-file app.

Usage:
  python _tools/mcdp_codex_build.py --json out.json           # data only
  python _tools/mcdp_codex_build.py --template T.html --out MCDP-CODEX.html
"""
import argparse, glob, html, io, json, os, re, sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEARN = os.path.join(ROOT, "_0.1_BVX_LEARN")
KA = os.path.join(LEARN, "KNOWLEDGE_AREAS")

SECTION_KEYS = [
    ("CORE THESIS", "thesis"), ("INVARIANTS", "invariants"), ("HEURISTICS", "heuristics"),
    ("CORE CONCEPTS", "concepts"), ("KEY VOCABULARY", "vocabulary"), ("NOTABLE QUOTES", "quotes"),
    ("WHAT DOESN", "doesnt_work"), ("QUICK SELF-CHECK", "selfcheck"), ("APPLICATION", "application"),
]


def read(p):
    return io.open(p, encoding="utf-8").read()


# ---------- inline markdown -> html (trusted house content) ----------
def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"==([^=\n]+?)==", r'<mark class="rm">\1</mark>', s)
    s = re.sub(r"\*\*([^*\n]+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![A-Za-z0-9])_([^_\n]+?)_(?![A-Za-z0-9])", r"<i>\1</i>", s)
    s = re.sub(r"(?<![*\w])\*([^*\n]+?)\*(?![*\w])", r"<i>\1</i>", s)
    s = re.sub(r"`([^`\n]+?)`", r"<code>\1</code>", s)
    s = re.sub(r"\[\[([^\]|\n]+?)(?:\|([^\]\n]+?))?\]\]", lambda m: '<a class="wl">%s</a>' % (m.group(2) or m.group(1)), s)
    s = re.sub(r"\[([^\]\n]+?)\]\(([^)\n]+?)\)", r"\1", s)
    return s


def plain(s):
    s = re.sub(r"==([^=\n]+?)==", r"\1", s)
    s = re.sub(r"\*\*([^*\n]+?)\*\*", r"\1", s)
    s = re.sub(r"(?<![A-Za-z0-9])_([^_\n]+?)_(?![A-Za-z0-9])", r"\1", s)
    s = re.sub(r"`([^`\n]+?)`", r"\1", s)
    return s.strip()


# ---------- frontmatter (yaml subset) ----------
def frontmatter(text):
    fm, body = {}, text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end > 0:
            raw = text[3:end].strip("\n").splitlines()
            body = text[end + 4:]
            key, cur = None, None
            for line in raw:
                if not line.strip():
                    continue
                m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
                if m and not line.startswith(" "):
                    key, val = m.group(1), m.group(2).strip()
                    if val == "":
                        fm[key] = []
                        cur = fm[key]
                    elif val.startswith("[") and val.endswith("]"):
                        fm[key] = [v.strip().strip('"') for v in val[1:-1].split(",") if v.strip()]
                        cur = None
                    else:
                        fm[key] = val.strip('"')
                        cur = None
                    continue
                m2 = re.match(r"^\s+-\s+(.*)$", line)
                if m2 and cur is not None:
                    item = m2.group(1).strip()
                    m3 = re.match(r"^([A-Za-z_]+):\s*(.*)$", item)
                    if m3:
                        cur.append({m3.group(1): m3.group(2).strip().strip('"')})
                    else:
                        cur.append(item.strip('"'))
                    continue
                m4 = re.match(r"^\s+([A-Za-z_]+):\s*(.*)$", line)
                if m4 and cur is not None and cur and isinstance(cur[-1], dict):
                    cur[-1][m4.group(1)] = m4.group(2).strip().strip('"')
    return fm, body


# ---------- sections ----------
def split_sections(body):
    out, cur, buf = {}, None, []
    for line in body.splitlines():
        h = re.match(r"^##\s+(.*)$", line)
        if h:
            if cur:
                out[cur] = buf
            cur, buf = h.group(1).strip(), []
            continue
        if cur:
            buf.append(line)
    if cur:
        out[cur] = buf
    keyed = {}
    for name, lines in out.items():
        for prefix, key in SECTION_KEYS:
            if name.upper().startswith(prefix):
                keyed[key] = lines
    return keyed


def table_rows(lines):
    rows = []
    for line in lines:
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.match(r"^:?-{2,}:?$", c) for c in cells if c):
            continue
        rows.append(cells)
    return rows[1:] if rows else []


def parse_thesis(lines):
    paras = [l.strip() for l in lines if l.strip() and not re.match(r"^_.*_$", l.strip())]
    return " ".join(paras)


def parse_lead_items(lines):
    items = []
    for line in lines:
        s = line.strip()
        m = re.match(r"^(?:\d+\.|-|\*)\s+(.*)$", s)
        if not m:
            continue
        rest = m.group(1)
        b = re.match(r"^\*\*(.+?)\*\*\s*(.*)$", rest)
        if b:
            items.append({"lead": b.group(1).strip(), "body": b.group(2).strip()})
        else:
            items.append({"lead": "", "body": rest.strip()})
    return items


def parse_concepts(lines):
    items, cur = [], None
    for line in lines:
        s = line.strip()
        if not s:
            continue
        if re.match(r"^_.*_$", s) and cur is None:
            continue
        t = re.match(r"^\*\*(.+?)\*\*\s*$", s) or re.match(r"^###\s+(.*)$", s)
        if t:
            cur = {"title": re.sub(r"^\d+[.)]\s*", "", t.group(1)).strip(), "body": ""}
            items.append(cur)
            continue
        t2 = re.match(r"^\*\*(\d+[.)])\*\*\s+(.*)$", s)
        if t2:
            cur = {"title": t2.group(2).strip().rstrip("*").strip(), "body": ""}
            items.append(cur)
            continue
        if cur is not None:
            cur["body"] = (cur["body"] + " " + s).strip()
    return items


def parse_quotes(lines):
    """Two house formats: (a) > "quote" / blank / _caption_   (b) > "quote" / > — caption / blank."""
    items, q, pending = [], [], False

    def flush(cap=""):
        if q:
            items.append({"quote": " ".join(q).strip().strip('"“”'), "caption": cap.strip()})
            q.clear()

    for line in lines:
        s = line.strip()
        if s.startswith(">"):
            body = s.lstrip(">").strip()
            if body == "":
                continue
            if q and re.match(r"^[—–-]\s*\S", body):
                flush(re.sub(r"^[—–-]\s*", "", body))
                pending = False
                continue
            if q and pending:
                flush()
            pending = False
            q.append(body)
            continue
        if re.match(r"^_.*_$", s) and q:
            flush(s.strip("_"))
            pending = False
            continue
        if s == "":
            pending = True
            continue
        flush()
        pending = False
    flush()
    return items


def parse_selfcheck(lines):
    items, note = [], ""
    for line in lines:
        s = line.strip()
        m = re.match(r"^-\s+\[[ xX]\]\s+(.*)$", s)
        if m:
            items.append(m.group(1).strip())
        elif re.match(r"^_.*_$", s):
            note = s.strip("_").strip()
    return items, note


def parse_text(lines):
    return " ".join(l.strip() for l in lines if l.strip() and not l.strip().startswith("---") and not l.strip().startswith("`"))


def marks_of(text):
    seen, out = set(), []
    for m in re.finditer(r"==([^=\n]+?)==", text):
        t = m.group(1).strip()
        if t.lower() not in seen:
            seen.add(t.lower())
            out.append(t)
    return out


def parse_sheet(path):
    text = read(path)
    fm, body = frontmatter(text)
    sec = split_sections(body)
    sc, scnote = parse_selfcheck(sec.get("selfcheck", []))
    sheet = {
        "id": fm.get("id", ""),
        "bvx_id": fm.get("bvx_id", ""),
        "title": fm.get("title", ""),
        "author": fm.get("author", ""),
        "year": fm.get("year", ""),
        "edition": fm.get("edition", ""),
        "domain": fm.get("domain", ""),
        "tags": [t for t in fm.get("tags", []) if isinstance(t, str)],
        "related": [re.sub(r"^\[\[|\]\]$", "", r).strip() for r in fm.get("related", []) if isinstance(r, str)],
        "feeds": [f for f in fm.get("feeds", []) if isinstance(f, dict)],
        "file": os.path.basename(path),
        "thesis": inline(parse_thesis(sec.get("thesis", []))),
        "invariants": [{"lead": inline(i["lead"]), "body": inline(i["body"])} for i in parse_lead_items(sec.get("invariants", []))],
        "heuristics": [{"situation": inline(r[0]), "do": inline(r[1]), "not": inline(r[2] if len(r) > 2 else "")} for r in table_rows(sec.get("heuristics", [])) if len(r) >= 2],
        "concepts": [{"title": inline(c["title"]), "body": inline(c["body"])} for c in parse_concepts(sec.get("concepts", []))],
        "vocabulary": [{"term": plain(r[0]), "definition": inline(r[1])} for r in table_rows(sec.get("vocabulary", [])) if len(r) >= 2],
        "quotes": [{"quote": inline(q["quote"]), "caption": inline(q["caption"])} for q in parse_quotes(sec.get("quotes", []))],
        "doesnt_work": inline(parse_text(sec.get("doesnt_work", []))),
        "selfcheck": [inline(i) for i in sc],
        "selfcheck_note": inline(scnote),
        "application": [{"lead": inline(i["lead"]), "body": inline(i["body"])} for i in parse_lead_items(sec.get("application", []))],
        "marks": marks_of(text),
        "plain": plain(body).lower(),
    }
    return sheet


def parse_register(path):
    rows = []
    if not os.path.exists(path):
        return rows
    for line in read(path).splitlines():
        m = re.match(r"^\|\s*(.+?)\s*\|\s*(.*?)\s*\|\s*(\S+)\s*\|\s*(.*?)\s*\|$", line)
        if m and m.group(1).lower() not in ("term", "---"):
            if re.match(r"^-+$", m.group(1)):
                continue
            rows.append({"term": m.group(1), "sense": inline(m.group(2)), "source": m.group(3), "section": m.group(4)})
    return rows


def build_terms(sheets, register):
    """term -> {senses:[{sense, source, section, kind}], appears:[sheet ids]}"""
    terms = {}
    for r in register:
        k = r["term"].lower()
        t = terms.setdefault(k, {"term": r["term"], "senses": [], "appears": []})
        t["senses"].append({"sense": r["sense"], "source": r["source"], "section": r["section"], "kind": "reader" if "KEY VOCABULARY" not in r["section"] else "author"})
    for s in sheets:
        for v in s["vocabulary"]:
            k = v["term"].lower()
            t = terms.setdefault(k, {"term": v["term"], "senses": [], "appears": []})
            if not any(x["source"] == s["id"] and x["kind"] == "author" for x in t["senses"]):
                t["senses"].append({"sense": v["definition"], "source": s["id"], "section": "KEY VOCABULARY", "kind": "author"})
    for k, t in terms.items():
        pat = re.compile(r"(?<![a-z])" + re.escape(k) + r"(?![a-z])")
        t["appears"] = [s["id"] for s in sheets if pat.search(s["plain"])]
    return terms


def make_linker(terms):
    """One combined regex, longest term first, whole-word, case-insensitive, optional plural.
    Wraps matches in <span class="t" data-t="key"> inside text segments only (never inside tags)."""
    keys = sorted(terms.keys(), key=len, reverse=True)
    if not keys:
        return lambda h: h
    alt = "|".join(re.escape(k) for k in keys)
    rx = re.compile(r"(?<![A-Za-z0-9_-])(" + alt + r")(s|es)?(?![A-Za-z0-9_-])", re.I)
    tag = re.compile(r"(<[^>]+>)")

    def link(h):
        if not h:
            return h
        out = []
        for seg in tag.split(h):
            if seg.startswith("<"):
                out.append(seg)
            else:
                out.append(rx.sub(lambda m: '<span class="t" data-t="%s">%s%s</span>' % (m.group(1).lower(), m.group(1), m.group(2) or ""), seg))
        return "".join(out)
    return link


def link_sheet(s, link):
    s["thesis"] = link(s["thesis"])
    for i in s["invariants"]:
        i["body"] = link(i["body"])
    for r in s["heuristics"]:
        r["situation"], r["do"], r["not"] = link(r["situation"]), link(r["do"]), link(r["not"])
    for c in s["concepts"]:
        c["body"] = link(c["body"])
    for v in s["vocabulary"]:
        v["definition"] = link(v["definition"])
    for q in s["quotes"]:
        q["quote"] = link(q["quote"])
    s["doesnt_work"] = link(s["doesnt_work"])
    s["selfcheck"] = [link(i) for i in s["selfcheck"]]
    for a in s["application"]:
        a["body"] = link(a["body"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    ap.add_argument("--template")
    ap.add_argument("--out")
    a = ap.parse_args()

    files = sorted(glob.glob(os.path.join(KA, "*MIL.*.md")))
    sheets = [parse_sheet(f) for f in files]
    register = parse_register(os.path.join(LEARN, "_meta", "VOCABULARY.md"))
    terms = build_terms(sheets, register)
    link = make_linker(terms)
    for s in sheets:
        link_sheet(s, link)
        s.pop("plain", None)
    for t in terms.values():
        for x in t["senses"]:
            x["sense"] = link(x["sense"])
    data = {"generated": date.today().isoformat(), "sheets": sheets, "register": register, "terms": terms}

    print("sheets: %d | register rows: %d | terms: %d" % (len(sheets), len(register), len(terms)))
    for s in sheets:
        print("  %s %-38s inv %2d · heur %2d · con %2d · voc %2d · quo %2d · chk %2d · app %2d · marks %2d" % (
            s["id"], s["title"][:38], len(s["invariants"]), len(s["heuristics"]), len(s["concepts"]),
            len(s["vocabulary"]), len(s["quotes"]), len(s["selfcheck"]), len(s["application"]), len(s["marks"])))

    if a.json:
        io.open(a.json, "w", encoding="utf-8", newline="\n").write(json.dumps(data, ensure_ascii=False, indent=1))
        print("json -> %s" % a.json)
    if a.template and a.out:
        tpl = read(a.template)
        payload = json.dumps(data, ensure_ascii=False).replace("</script", "<\\/script")
        assert "/*__DATA__*/" in tpl, "template lacks /*__DATA__*/ slot"
        out = tpl.replace("/*__DATA__*/", payload, 1)
        io.open(a.out, "w", encoding="utf-8", newline="\n").write(out)
        print("html -> %s (%d KB)" % (a.out, len(out.encode("utf-8")) // 1024))


if __name__ == "__main__":
    sys.exit(main())
