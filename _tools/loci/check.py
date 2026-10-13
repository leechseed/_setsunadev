# -*- coding: utf-8 -*-
"""LOCI check — the reviewer at the fan-in: every fetched link is covered by the register (script, zero tokens).

Usage:  python _tools/loci/check.py <name> <register.md>
Proves (1) every fetched link is covered; (2) every claim line (a bullet or table row) with a URL cites one that exists in the manifest (else ERROR);
a claim line with no URL is listed under "unsourced lines" (advisory count, does not fail the run).
Then (mar-07) stamps one `run:` line in the locus frontmatter from work/<name>/run.json and the COST token estimate; after a --narrow run, only the narrow link set must be covered.
"""
import io, json, os, re, sys, time, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from collect import COST, trace

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

def stamp_locus(name, wd, t0):
    """mar-07: write or update one `run:` line in the locus frontmatter (adds a minimal frontmatter if none)."""
    try:
        run = json.load(io.open(os.path.join(wd, "run.json"), encoding="utf-8"))
        loc = run["src"]
        if not loc.lower().endswith(".md") or not os.path.exists(loc): return
        tokens = run["batches"] * COST["ps_tokens_per_batch"] + COST["ms_tokens_per_register"]
        line = f"run: {datetime.date.today().isoformat()} · agents {run['agents']} · batches {run['batches']} · links {run['links']} · dead {run['dead']} · ~tokens {tokens}"
        txt = io.open(loc, encoding="utf-8").read()
        m = re.match(r"\A---?
(.*?)?
---[ 	]*(?
|\Z)", txt, re.S)
        if m:
            fm = m.group(1)
            fm = re.sub(r"(?m)^run:.*$", lambda _: line, fm) if re.search(r"(?m)^run:", fm) else fm + "
" + line
            txt = "---
" + fm + "
---" + m.group(2) + txt[m.end():]
        else:
            txt = f"---
{line}
---

" + txt
        with io.open(loc, "w", encoding="utf-8", newline="") as f: f.write(txt)
        trace(wd, "check", run["batches"], run["links"], 1, time.time() - t0)
        print("  frontmatter · " + line)
    except Exception as e:
        print(f"  note  frontmatter not stamped: {e}")

def main():
    try: sys.stdout.reconfigure(encoding="utf-8")
    except Exception: pass
    if len(sys.argv) < 3 or sys.argv[1] in ("-h", "--help"):
        print(__doc__); sys.exit(0 if len(sys.argv) > 1 else 2)
    name, reg = sys.argv[1], sys.argv[2]
    man = json.load(io.open(os.path.join(HERE, "work", name, "manifest.json"), encoding="utf-8"))
    text = io.open(reg, encoding="utf-8").read()
    norm = lambda u: re.sub(r"^https?://(www\.)?", "", u).rstrip("/").lower()
    body = norm(text)
    fetched = [m for m in man if m["status"] == 200]
    t0 = time.time(); wd = os.path.join(HERE, "work", name)
    try: nar = json.load(io.open(os.path.join(wd, "narrow.json"), encoding="utf-8"))
    except Exception: nar = []
    if nar: fetched = [m for m in fetched if m["n"] in nar]  # a narrow run covers only its picked links
    missing = [m["url"] for m in fetched if norm(m["url"]) not in body and (m["title"] and m["title"].lower()[:40] not in body)]
    dead = [m["url"] for m in man if m["status"] != 200]
    ext = sorted(f for f in os.listdir(os.path.join(HERE, "work", name)) if f.startswith("extract.") and f.endswith(".json"))
    items = 0
    for f in ext:
        try: items += sum(len(x.get("items", [])) for x in json.load(io.open(os.path.join(HERE, "work", name, f), encoding="utf-8")))
        except Exception: print("  note  unreadable " + f)
    print(f"CHECK · {name} · {len(fetched)} fetched · {len(missing)} not covered · {len(dead)} dead links · {items} extracted item(s) in {len(ext)} batch file(s)")
    for u in missing: print("  MISSING " + u)
    for u in dead: print("  dead    " + u)
    # mar-04: claim lines = bullets and table rows (not headers or separators); each should carry a manifest URL
    known = {norm(m["url"]) for m in man}
    lines = text.splitlines(); bad = []; unsourced = []; claims = 0
    for i, ln in enumerate(lines):
        st = ln.strip()
        is_bullet = bool(re.match(r"^([-*+]|\d+\.)\s+\S", st))
        is_row = st.startswith("|") and not re.match(r"^\|[\s:|-]+\|?$", st)
        if is_row and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|?\s*$", lines[i + 1]): is_row = False  # header row
        if not (is_bullet or is_row): continue
        claims += 1
        urls = [u.rstrip(".,;:") for u in re.findall(r"https?://[^\s)>\]|]+", st)]
        if not urls: unsourced.append((i + 1, st)); continue
        for u in urls:
            if norm(u) not in known: bad.append((i + 1, u))
    print(f"  claims · {claims} claim line(s) · {len(bad)} URL(s) not in the manifest (error) · {len(unsourced)} unsourced line(s) (advisory)")
    for n, u in bad: print(f"  ERROR   line {n}: URL not in manifest: {u}")
    if unsourced:
        print("  unsourced lines:")
        for n, t in unsourced: print(f"    line {n}: {t[:90]}")
    stamp_locus(name, wd, t0)
    sys.exit(1 if (missing or bad) else 0)

if __name__ == "__main__":
    main()
