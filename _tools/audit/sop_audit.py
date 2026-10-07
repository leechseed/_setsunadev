# -*- coding: utf-8 -*-
"""The SOP audit ("audit", RULED 2026-10-06) — a script checks the live Command against the SOP and lists every gap.
Zero tokens. Archives are out of scope (_LOG, _CLAUDE_ARCHIVE*, journals, _PRIVATE); STATE's Moved sections are history.

Usage:  python _tools/audit/sop_audit.py          # print the findings, write _tools/audit/out/sop-audit-<date>.md
Checks:
  R  retired words still in live files (SOP §1/§5 rulings; a line that names the retirement is allowed)
  P  private detail in public files (health · sexual · provider detail lives only in _PRIVATE/, ruled 10/4)
  B  BOLO hygiene: active rows with no status mark, or untouched for 21+ days
  K  the rack: _CACHE holds today's note only (SOP §3, the flush)
  T  the tree: nothing uncommitted beyond the session log
  A  the Claude Code practice rows (BOLO 51, rows.json): open count and age
"""
import datetime as dt, glob, io, json, os, re, subprocess, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
TODAY = dt.date.today()

LIVE = ["SOP.md", "STATE.md", "BOLO.md", "PROJECTS.md", "CLAUDE.md"] \
    + glob.glob(os.path.join(ROOT, ".claude", "skills", "**", "*.md"), recursive=True) \
    + glob.glob(os.path.join(ROOT, "_tools", "**", "*.py"), recursive=True) \
    + glob.glob(os.path.join(ROOT, "_CANON_NODES", "*.md")) \
    + glob.glob(os.path.join(ROOT, "_CACHE", "*.md"))
SKIP_DIRS = ("_PRIVATE", "_LOG", "_CLAUDE_ARCHIVE", "_devlog_journals", "work" + os.sep, "out" + os.sep)

RETIRED = [  # (pattern, the ruled word, ruling)
    (r"\bPapi\b", "Chief", "9/17"),
    (r"\bthe house\b(?! tongue)", "the Command", "9/16"),
    (r"\bhouse tongue\b", "the lexicon", "9/11"),
    (r"\bhouse format\b", "the Command format", "9/16"),
    (r"\bin-house\b", "organic", "9/16"),
    (r"\bENDEX\b", "Oscar Mike", "9/11"),
    (r"\bOPORD\b", "DOPE SHEET", "9/11"),
    (r"\bsonnet specialist\b", "MS (Mission Specialist)", "9/16"),
    (r"\bagents in flight\b", "agents deployed", "9/24"),
    (r"\b12-layer character (system|database)\b", "LEECHSEED", "10/5"),
    (r"\bThe Outsiders\b", "The Outliers", "standing"),
    (r"\bparking card", "the DOPE SHEET resume order", "9/11"),
    (r"\bwhite glove\b", "audit", "10/6"),
    (r"\bfield day\b", "deep clean", "10/6"),
]
ALLOWED = re.compile(r"RETIRED|retired|lineage|legacy|replac|supersed|was \"|was '|\(was |dropped|never \"|not \"|garble|codebook|reads as", re.I)

PRIVATE = [  # acronyms match case-sensitively (PrEP, not "prep"); "diagnos" skips the fiction in _CANON_NODES
    (r"\bPrEP\b", 0), (r"\bHIV\b", 0), (r"\bSTIs?\b", 0), (r"\bSTDs?\b", 0), (r"\bMRO\b", 0), (r"\bA1c\b", 0),
    (r"\bcataract", re.I), (r"drug[- ]screen", re.I), (r"psych med", re.I), (r"Zellner", re.I), (r"Frank Dental", re.I),
    (r"Eye Associates", re.I), (r"Davalos", re.I), (r"Blind Services", re.I), (r"sexual[- ]health", re.I), (r"\bdiagnos", re.I)]

def rel(p): return os.path.relpath(p if os.path.isabs(p) else os.path.join(ROOT, p), ROOT).replace("\\", "/")

def lines_of(path):
    full = path if os.path.isabs(path) else os.path.join(ROOT, path)
    if any(s in full for s in SKIP_DIRS) or not os.path.isfile(full): return []
    txt = io.open(full, encoding="utf-8", errors="replace").read().split("\n")
    if rel(full) == "STATE.md":  # Moved sections are history
        out, hist = [], False
        for i, l in enumerate(txt, 1):
            if l.startswith("## "): hist = "Moved" in l
            if not hist: out.append((i, l))
        return out
    return list(enumerate(txt, 1))

def main():
    F = {k: [] for k in "RPBKTA"}
    for p in sorted(set(LIVE)):
        if rel(p) == "_tools/audit/sop_audit.py": continue
        for n, l in lines_of(p):
            for pat, new, when in RETIRED:
                if re.search(pat, l, re.I if pat != r"\bENDEX\b" else 0) and not ALLOWED.search(l):
                    F["R"].append(f"{rel(p)}:{n} · '{re.search(pat, l, re.I).group(0)}' → {new} (ruled {when})")
            if rel(p) not in ("BOLO.md", "STATE.md", "SOP.md", "PROJECTS.md") and not rel(p).startswith(("_CACHE", "_CANON_NODES", ".claude")):
                continue
            for pat, fl in PRIVATE:
                if pat == r"diagnos" and rel(p).startswith("_CANON_NODES"): continue
                m = re.search(pat, l, fl)
                if m: F["P"].append(f"{rel(p)}:{n} · '{m.group(0)}'")
    # B · BOLO hygiene
    bolo = io.open(os.path.join(ROOT, "BOLO.md"), encoding="utf-8").read().split("\n")
    for n, l in enumerate(bolo, 1):
        m = re.match(r"\| (\d+) \|", l)
        if not m: continue
        cells = l.split("|"); status = cells[-2] if len(cells) > 3 else ""
        if re.search(r"✅|DONE|CLOSED|RETIRED|MERGED", status): continue
        if not re.search(r"[🟢🟡🔴⏸️⚪🔵✅⛔]", status): F["B"].append(f"BOLO {m.group(1)} (line {n}) · no status mark")
        dates = [dt.date(2026, int(a), int(b)) for a, b in re.findall(r"\b(1[0-2]|0?[1-9])/([0-3]?\d)\b", l) if 1 <= int(b) <= 31 and int(a) >= 6]
        dates = [d for d in dates if d <= TODAY]
        if dates and (TODAY - max(dates)).days >= 21:
            F["B"].append(f"BOLO {m.group(1)} · last touched {max(dates):%m/%d} ({(TODAY - max(dates)).days} days)")
    # K · the rack
    notes = [os.path.basename(x) for x in glob.glob(os.path.join(ROOT, "_CACHE", "*.session.md"))]
    stale = [x for x in notes if not x.startswith(TODAY.isoformat())]
    if stale: F["K"].append("unflushed notes: " + ", ".join(stale))
    extra = [os.path.basename(x) for x in glob.glob(os.path.join(ROOT, "_CACHE", "*")) if not x.endswith((".session.md", "README.md"))]
    if extra: F["K"].append(f"{len(extra)} non-note file(s) in the rack: " + ", ".join(extra))
    # T · the tree
    st = subprocess.run(["git", "status", "--short"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout.split("\n")
    dirty = [s for s in st if s.strip() and "judy.session.log" not in s]
    if dirty: F["T"].append(f"{len(dirty)} uncommitted: " + ", ".join(s[3:] for s in dirty[:8]))
    # A · the practice rows
    rows = json.load(io.open(os.path.join(ROOT, "_tools", "audit", "rows.json"), encoding="utf-8"))["rows"]
    op = [r for r in rows if not r["closed"]]
    added = max(dt.date.fromisoformat(r["added"]) for r in rows)
    F["A"].append(f"{len(op)} of {len(rows)} practice rows open · {sum(r['status']=='GAP' for r in op)} GAP, {sum(r['status']=='PARTIAL' for r in op)} PARTIAL · last pass {added:%m/%d} ({(TODAY-added).days} days)")

    names = {"R": "Retired words in live files", "P": "Private detail in public files", "B": "BOLO hygiene",
             "K": "The rack", "T": "The tree", "A": "Claude Code practice rows (BOLO 51)"}
    out = [f"# SOP AUDIT · {TODAY:%Y-%m-%d}", "", f"{sum(len(v) for k, v in F.items() if k != 'A')} findings across {len(set(LIVE))} live files.", ""]
    print(out[0]); print(out[2])
    for k in "RPBKTA":
        out += [f"## {k} · {names[k]} ({len(F[k])})", ""] + [f"- {x}" for x in F[k]] + ([] if F[k] else ["- clean"]) + [""]
        print(f"  {k}  {names[k]:<38} {len(F[k])}")
    os.makedirs(os.path.join(ROOT, "_tools", "audit", "out"), exist_ok=True)
    rp = os.path.join(ROOT, "_tools", "audit", "out", f"sop-audit-{TODAY}.md")
    io.open(rp, "w", encoding="utf-8", newline="\n").write("\n".join(out))
    print("wrote", rel(rp))

main()
