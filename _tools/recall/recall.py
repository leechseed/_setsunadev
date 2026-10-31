# -*- coding: utf-8 -*-
"""recall: ranked search over the Command's own notes (BOLO 162 call 3, Chief "take all recs" 10/31).

"Where did we rule X" becomes one ranked query, not a grep sweep. Zero tokens: SQLite FTS5 (built into Python's
sqlite3), BM25 ranking, porter stemming. Sources, each split by markdown heading into sections:
  cache   _CACHE/*.md            log     _LOG/*.session.md
  memory  the auto-memory folder  sop     SOP.md     state   STATE.md
The index lives at _PRIVATE/recall/index.sqlite (gitignored; the memory notes are private) and rebuilds itself
when any source file is newer than it, or a source was added or removed.

    python -X utf8 _tools/recall/recall.py where did we rule the school name
    python -X utf8 _tools/recall/recall.py "oscar mike" -n 5 --source memory --json
    python -X utf8 _tools/recall/recall.py --rebuild
Verb: `command recall ...` (_tools/cmdtui/recall.go) passes the arguments through.
"""
import argparse, glob, json, os, re, sqlite3, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
MEMORY = os.path.join(os.path.expanduser("~"), ".claude", "projects", "c--Users-U01-LEECHSEED-Desktop--setsunadev", "memory")
INDEX = os.path.join(ROOT, "_PRIVATE", "recall", "index.sqlite")
SCHEMA = 2
STOP = set("a an and are as at be by did do does for from had has have how i in is it its of on or so that the this "
           "to was we were what when where which who why will with you me my our".split())


def sources():
    out = []
    for kind, pat in (("cache", os.path.join(ROOT, "_CACHE", "*.md")),
                      ("log", os.path.join(ROOT, "_LOG", "*.session.md")),
                      ("memory", os.path.join(MEMORY, "*.md"))):
        out += [(kind, p) for p in sorted(glob.glob(pat))]
    for kind, name in (("sop", "SOP.md"), ("state", "STATE.md")):
        p = os.path.join(ROOT, name)
        if os.path.isfile(p):
            out.append((kind, p))
    return out


def show_path(p):
    if p.startswith(MEMORY):
        return "memory/" + os.path.basename(p)
    return os.path.relpath(p, ROOT).replace("\\", "/")


def sections(text):
    """Split by '#'/'##'/'###' headings (outside code fences). Yields (start_line, heading, body)."""
    lines = text.splitlines()
    head, start, buf, fence = "", 1, [], False
    for i, ln in enumerate(lines, 1):
        if ln.startswith("```"):
            fence = not fence
        m = None if fence else re.match(r"^(#{1,3})\s+(.*)", ln)
        if m:
            if "".join(buf).strip():
                yield start, head, "\n".join(buf)
            head, start, buf = m.group(2).strip(), i, [ln]
        else:
            buf.append(ln)
    if "".join(buf).strip():
        yield start, head, "\n".join(buf)


def memory_title(text, path):
    m = re.search(r"^name:\s*(.+)$", text, re.M)
    d = re.search(r"^description:\s*(.+)$", text, re.M)
    t = (m.group(1).strip() if m else os.path.basename(path)[:-3])
    return t + (" · " + d.group(1).strip() if d else "")


def stamp(srcs):
    return json.dumps([SCHEMA, len(srcs), max((os.path.getmtime(p) for _, p in srcs), default=0)])


def fresh(db, srcs):
    try:
        row = db.execute("select v from meta where k='stamp'").fetchone()
        return bool(row) and row[0] == stamp(srcs)
    except sqlite3.Error:
        return False


def build(db, srcs):
    db.executescript("""drop table if exists docs; drop table if exists meta;
        create virtual table docs using fts5(kind unindexed, path unindexed, line unindexed, heading, body,
                                             tokenize='porter unicode61');
        create table meta(k text primary key, v text);""")
    n = 0
    for kind, p in srcs:
        try:
            with open(p, encoding="utf-8", errors="replace") as f:
                text = f.read()
        except OSError:
            continue
        if kind == "memory":  # one fact a file: one section, titled from the frontmatter
            db.execute("insert into docs values (?,?,?,?,?)", (kind, show_path(p), 1, memory_title(text, p), text))
            n += 1
            continue
        for line, head, body in sections(text):
            db.execute("insert into docs values (?,?,?,?,?)", (kind, show_path(p), line, head, body))
            n += 1
    db.execute("insert into meta values ('stamp', ?)", (stamp(srcs),))
    db.execute("insert into meta values ('sections', ?)", (str(n),))
    db.commit()
    return n


def fts_query(words):
    toks = [t for t in re.findall(r"[\w'-]+", " ".join(words).lower()) if t not in STOP]
    toks = [t.replace('"', "") for t in toks if t.strip("'-")]
    return " OR ".join('"%s"' % t for t in dict.fromkeys(toks))


def search(db, q, n, kind):
    sql = ("select kind, path, line, heading, snippet(docs, 4, '[', ']', ' … ', 18), bm25(docs, 0, 0, 0, 3.0, 1.0) "
           "from docs where docs match ?" + (" and kind = ?" if kind else "") + " order by 6 limit ?")
    args = [q] + ([kind] if kind else []) + [n]
    return [dict(kind=k, path=p, line=int(l), heading=h, snippet=re.sub(r"\s+", " ", s).strip(), score=round(-sc, 3))
            for k, p, l, h, s, sc in db.execute(sql, args)]


def main():
    ap = argparse.ArgumentParser(prog="recall", description="Ranked search over _CACHE, _LOG, the memory folder, SOP and STATE.")
    ap.add_argument("query", nargs="*")
    ap.add_argument("-n", type=int, default=8, help="how many hits (default 8)")
    ap.add_argument("--source", choices=["cache", "log", "memory", "sop", "state"], help="search one source only")
    ap.add_argument("--json", action="store_true", help="print the hits as JSON")
    ap.add_argument("--rebuild", action="store_true", help="rebuild the index now")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    os.makedirs(os.path.dirname(INDEX), exist_ok=True)
    db = sqlite3.connect(INDEX)
    srcs = sources()
    built = None
    if a.rebuild or not fresh(db, srcs):
        built = build(db, srcs)
    total = int(db.execute("select v from meta where k='sections'").fetchone()[0])

    q = fts_query(a.query)
    if not q:
        info = {"index": show_path(INDEX), "sections": total, "files": len(srcs), "rebuilt": built is not None, "hits": []}
        if a.json:
            print(json.dumps(info, indent=1))
        else:
            print("recall · %d sections from %d files · index %s%s" % (total, len(srcs), info["index"], " (rebuilt)" if built is not None else ""))
            print("usage: recall <words> [-n N] [--source cache|log|memory|sop|state] [--json] [--rebuild]")
        return
    hits = search(db, q, a.n, a.source)
    if a.json:
        print(json.dumps({"query": " ".join(a.query), "fts": q, "sections": total, "rebuilt": built is not None, "hits": hits}, indent=1, ensure_ascii=False))
        return
    print("recall · %r · %d hit(s) of %d sections%s" % (" ".join(a.query), len(hits), total, " · index rebuilt" if built is not None else ""))
    for i, h in enumerate(hits, 1):
        print("%2d. %s:%d · %s · %s" % (i, h["path"], h["line"], h["kind"], (h["heading"] or "(top)")[:90]))
        print("    " + h["snippet"][:220])


if __name__ == "__main__":
    main()
