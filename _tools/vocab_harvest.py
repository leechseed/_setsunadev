#!/usr/bin/env python
"""vocab_harvest.py — harvest reader marks (==term==) from a BVX-LEARN one-sheet.

Reader protocol (SSOT: 05_OPERATIONS/📐 ssot_05_operations_markdown_marking):
  the reader marks a load-bearing term as ==term== while reading;
  this script pulls every mark with its section and sentence and writes
  (1) the per-source VOCAB page  KNOWLEDGE_AREAS/_vocab/<ID>.vocab.md
  (2) new rows in the house register  _0.1_BVX_LEARN/_meta/VOCABULARY.md

Usage:
  python _tools/vocab_harvest.py "<one-sheet.md>" [--senses senses.json]
         [--convert-bold terms.txt] [--vocab-dir DIR] [--register FILE] [--dry]

  --convert-bold terms.txt   one exact bold span per line; each **span** in the
                             sheet becomes ==span== before harvesting (retro-conversion
                             of marks made in bold). Template bolds are never touched
                             because only the listed spans are converted.
  --senses senses.json       {"term": "sense", ...}; matched case-insensitively.
"""
import argparse, io, json, os, re, sys
from datetime import date

MARK = re.compile(r"==([^=\n]+?)==")
HEAD = re.compile(r"^(#{1,6})\s+(.*)$")
SENT = re.compile(r"(?<=[.!?])\s+")


def read(p):
    return io.open(p, encoding="utf-8").read()


def write(p, s):
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)


def frontmatter(text):
    fm = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end > 0:
            for line in text[3:end].splitlines():
                m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
                if m:
                    fm[m.group(1)] = m.group(2).strip().strip('"')
    return fm


def clean(s):
    s = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", s)          # list prefix
    s = re.sub(r"==([^=]+?)==", r"\1", s)                # marks
    s = re.sub(r"\*\*([^*]+?)\*\*", r"\1", s)            # bold
    s = re.sub(r"(?<![A-Za-z0-9])_([^_]+?)_(?![A-Za-z0-9])", r"\1", s)  # italic
    s = re.sub(r"`([^`]+?)`", r"\1", s)
    s = re.sub(r"\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]", r"\1", s)
    return s.strip()


def snippet(sentence, term, window=9):
    """Sentences longer than ~28 words are windowed to ±window words around the term."""
    words = sentence.split()
    if len(words) <= 28:
        return sentence
    low = [w.lower() for w in words]
    tw = term.lower().split()
    start = -1
    for i in range(len(low) - len(tw) + 1):
        if all(tw[j] in low[i + j] for j in range(len(tw))):
            start = i
            break
    if start < 0:
        return " ".join(words[:28]) + " …"
    a = max(0, start - window)
    b = min(len(words), start + len(tw) + window)
    return ("… " if a > 0 else "") + " ".join(words[a:b]) + (" …" if b < len(words) else "")


def convert_bold(text, terms):
    n = 0
    for t in terms:
        pat = re.compile(r"\*\*" + re.escape(t) + r"\*\*")
        text, k = pat.subn("==" + t + "==", text)
        n += k
    return text, n


def harvest(text):
    """Return ordered list of dicts: term, section, sentence. Dedupe by term.lower()."""
    out, seen, section = [], set(), "(top)"
    for line in text.splitlines():
        h = HEAD.match(line)
        if h:
            section = clean(h.group(2))
            continue
        if "==" not in line:
            continue
        for sent in SENT.split(line):
            for m in MARK.finditer(sent):
                term = m.group(1).strip()
                key = term.lower()
                if key in seen:
                    continue
                seen.add(key)
                out.append({"term": term, "section": section, "sentence": snippet(clean(sent), term)})
    return out


def vocab_page(fm, sheet_name, rows, senses):
    sid = fm.get("id", "UNKNOWN")
    title = fm.get("title", sheet_name)
    lines = [
        "---",
        "id: %s.vocab" % sid,
        "type: vocab",
        'source: "[[%s]]"' % sheet_name,
        "bvx_id: %s" % fm.get("bvx_id", ""),
        "marks: %d" % len(rows),
        "harvested: %s" % date.today().isoformat(),
        "rule: reader marks ==term== in the one-sheet; this page is the harvest; register = _meta/VOCABULARY.md",
        "---",
        "",
        "# %s — VOCAB — %s" % (sid, title),
        "",
        "_Load-bearing terms as marked by the reader, in reading order, with their sense in this source and the sentence they sat in._",
        "",
    ]
    cur = None
    for r in rows:
        if r["section"] != cur:
            cur = r["section"]
            lines += ["## %s" % cur, ""]
        sense = senses.get(r["term"].lower(), "")
        lines.append("- **%s**%s" % (r["term"], (" — " + sense) if sense else ""))
        lines.append('  - ↳ "%s"' % r["sentence"])
    lines.append("")
    return "\n".join(lines)


REG_HEAD = [
    "---",
    "title: VOCABULARY — the house register of load-bearing terms",
    "type: register",
    "rule: one row per (term, source); rows are appended by _tools/vocab_harvest.py, never hand-typed; sense is the term's meaning IN THAT SOURCE",
    "---",
    "",
    "# VOCABULARY — the register",
    "",
    "| Term | Sense (in source) | Source | Section |",
    "|---|---|---|---|",
]


def update_register(path, sid, rows, senses):
    existing = read(path) if os.path.exists(path) else "\n".join(REG_HEAD) + "\n"
    have = set()
    for line in existing.splitlines():
        m = re.match(r"^\|\s*(.+?)\s*\|.*?\|\s*(\S+)\s*\|", line)
        if m:
            have.add((m.group(1).lower(), m.group(2)))
    add = []
    for r in rows:
        k = (r["term"].lower(), sid)
        if k in have:
            continue
        have.add(k)
        add.append("| %s | %s | %s | %s |" % (r["term"], senses.get(r["term"].lower(), ""), sid, r["section"]))
    if not existing.endswith("\n"):
        existing += "\n"
    return existing + ("\n".join(add) + "\n" if add else ""), len(add)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sheet")
    ap.add_argument("--senses")
    ap.add_argument("--convert-bold")
    ap.add_argument("--vocab-dir")
    ap.add_argument("--register")
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()

    sheet = os.path.abspath(a.sheet)
    text = read(sheet)
    fm = frontmatter(text)
    sheet_name = os.path.splitext(os.path.basename(sheet))[0]
    sid = fm.get("id", sheet_name)

    if a.convert_bold:
        terms = [t.rstrip("\n") for t in io.open(a.convert_bold, encoding="utf-8") if t.strip()]
        text, n = convert_bold(text, terms)
        print("converted %d bold spans to marks" % n)
        if not a.dry:
            write(sheet, text)

    rows = harvest(text)
    senses = {}
    if a.senses:
        senses = {k.lower(): v for k, v in json.load(io.open(a.senses, encoding="utf-8")).items()}
    missing = [r["term"] for r in rows if r["term"].lower() not in senses]

    vocab_dir = a.vocab_dir or os.path.join(os.path.dirname(sheet), "_vocab")
    vpath = os.path.join(vocab_dir, sid + ".vocab.md")
    page = vocab_page(fm, sheet_name, rows, senses)

    root = sheet
    while root and os.path.basename(root) != "_0.1_BVX_LEARN":
        nxt = os.path.dirname(root)
        if nxt == root:
            root = None
            break
        root = nxt
    rpath = a.register or os.path.join(root or os.path.dirname(sheet), "_meta", "VOCABULARY.md")
    reg, added = update_register(rpath, sid, rows, senses)

    print("source: %s | marks: %d | sections: %d | senses missing: %d" % (
        sid, len(rows), len(set(r["section"] for r in rows)), len(missing)))
    if missing:
        print("  no sense for: " + " | ".join(missing))
    if a.dry:
        print("dry run: nothing written")
        return
    write(vpath, page)
    write(rpath, reg)
    print("wrote %s" % os.path.relpath(vpath))
    print("register %s (+%d rows)" % (os.path.relpath(rpath), added))


if __name__ == "__main__":
    sys.exit(main())
