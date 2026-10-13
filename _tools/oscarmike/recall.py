# -*- coding: utf-8 -*-
"""Session-note recall (BOLO 140, claude-mem-03): search -> timeline -> fetch, over _LOG and _CACHE *.session.md.

Usage:  python _tools/oscarmike/recall.py search <words...>
        python _tools/oscarmike/recall.py timeline <id> [--n 2]
        python _tools/oscarmike/recall.py fetch <id> [--section Ruled|Built|Open]
ids are the file stems (2026-10-12-5.session). Private spans ([private]..[/private] or
<!-- private -->..<!-- /private -->) are never printed (claude-mem-05).
"""
import io, os, re, sys, glob

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
PRIVATE_RE = re.compile(r"\[private\].*?\[/private\]|<!--\s*private\s*-->.*?<!--\s*/private\s*-->", re.S | re.I)

def strip_private(text):
    return PRIVATE_RE.sub("", text)

def split_private(text):
    """Return (public_text, [private spans])."""
    return PRIVATE_RE.sub("", text), [m.group(0) for m in PRIVATE_RE.finditer(text)]

def notes():
    out = {}
    for d in ("_LOG", "_CACHE"):
        for p in glob.glob(os.path.join(ROOT, d, "*.session.md")):
            out[os.path.basename(p)[:-3]] = p  # stem keeps ".session"; id below drops it
    return {k[:-len(".session")] if k.endswith(".session") else k: v for k, v in out.items()}

def read(p):
    with io.open(p, encoding="utf-8", errors="replace") as f:
        return strip_private(f.read())

def title(text):
    m = re.search(r"^# (.+)$", text, re.M)
    t = re.sub(r"^Session note\s*[—-]\s*", "", m.group(1)) if m else "(no title)"
    return re.sub(r"\s*\(session .*$", "", t)[:90]

def date_of(i):
    m = re.match(r"\d{4}-\d{2}-\d{2}", i)
    return m.group(0) if m else "????-??-??"

def find(i, idx):
    if i in idx: return i
    i = i.replace(".session", "")
    if i in idx: return i
    print("no such id:", i); sys.exit(1)

def search(words):
    ws = [w.lower() for w in words]
    hits = []
    for i, p in notes().items():
        t = read(p); low = t.lower()
        n = sum(low.count(w) for w in ws)
        if n and all(w in low for w in ws):
            hits.append((n, i, title(t)))
    for n, i, t in sorted(hits, key=lambda h: (-h[0], h[1]))[:20]:
        print(f"{i} · {date_of(i)} · {t} · {n} hit(s)")
    if not hits: print("no match")

def timeline(i, n=2):
    idx = notes(); i = find(i, idx)
    order = sorted(idx)
    k = order.index(i)
    for j in range(max(0, k - n), min(len(order), k + n + 1)):
        o = order[j]
        print(f"{'>' if j == k else ' '} {o} · {date_of(o)} · {title(read(idx[o]))}")

def section(text, name):
    lines = text.splitlines(); out = []; on = False
    for ln in lines:
        top = re.match(r"- \*\*", ln) or re.match(r"#+ ", ln)
        if top:
            on = bool(re.match(r"(- \*\*|#+ \**)\s*" + re.escape(name), ln, re.I))
        if on: out.append(ln)
    return "\n".join(out)

def fetch(i, sec=None):
    idx = notes(); i = find(i, idx)
    t = read(idx[i])
    print(section(t, sec) or f"(no section {sec})" if sec else t)

def main():
    a = sys.argv[1:]
    if len(a) < 2 or a[0] not in ("search", "timeline", "fetch"):
        print(__doc__); sys.exit(1)
    if a[0] == "search": search(a[1:])
    elif a[0] == "timeline":
        n = int(a[a.index("--n") + 1]) if "--n" in a else 2
        timeline(a[1], n)
    else:
        fetch(a[1], a[a.index("--section") + 1] if "--section" in a else None)

if __name__ == "__main__":
    main()
