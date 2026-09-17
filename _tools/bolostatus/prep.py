# -*- coding: utf-8 -*-
"""DOPE SHEET prep — the zero-token half of building BOLO N's status page (BOLO 51 phase 4, the formation).

Usage:  python _tools/bolostatus/prep.py <N>

Writes  _tools/bolostatus/work/<N>/sources.md    BOLO row N · every BOLO row it names · STATE lines that mention it ·
                                                 cache/log notes that mention it (last 5) · related DOPE SHEET status lines
        _tools/bolostatus/work/<N>/schema.json   a trimmed sheet (the newest board) as the shape to copy
        _tools/bolostatus/work/<N>/brief.SHEET.md the sonnet brief: write boards/<N>.draft.json (S · E · A · L + mantra)
Then the main line writes Mission (M), Command & Signal (C), frago.order/default/calls off the draft, runs check.py N, build.py N, publishes.
"""
import io, json, os, re, sys, glob
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

def rel(p): return os.path.relpath(p, ROOT).replace("\\", "/")
def load(p): return io.open(p, encoding="utf-8").read()
def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)

def main():
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    n = sys.argv[1]
    wd = os.path.join(HERE, "work", n)
    bolo = load(os.path.join(ROOT, "BOLO.md"))
    rows = {m.group(1): m.group(0) for m in re.finditer(r"^\| (\d+) \| .+$", bolo, re.M)}
    row = rows.get(n)
    if not row: print(f"BOLO {n} not in BOLO.md"); sys.exit(1)
    named = sorted({x for x in re.findall(r"BOLO (\d+)", row) if x != n and x in rows}, key=int)
    state = load(os.path.join(ROOT, "STATE.md"))
    smentions = [l for l in state.splitlines() if re.search(rf"BOLO {n}\b", l)][:12]
    notes = sorted(glob.glob(os.path.join(ROOT, "_CACHE", "*.session.md")) + glob.glob(os.path.join(ROOT, "_LOG", "*.session.md")), key=os.path.getmtime)[-8:]
    nmentions = []
    for p in notes:
        for l in load(p).splitlines():
            if re.search(rf"BOLO {n}\b", l): nmentions.append(f"{os.path.basename(p)}: {l.strip()[:400]}")
    sheets = []
    for m in named:
        sp = os.path.join(HERE, "boards", f"{m}.json")
        if os.path.exists(sp):
            b = json.load(io.open(sp, encoding="utf-8"))["bolo"]
            sheets.append(f"DOPE SHEET {m}: {b.get('title','')} · {b.get('status','')[:160]}")
    src = [f"# SOURCES · BOLO {n}\n", "## The row\n", row, "\n## Rows it names\n"] + [rows[m] for m in named] + \
          ["\n## STATE.md mentions\n"] + smentions + ["\n## Session notes (newest 8 searched)\n"] + nmentions[-10:] + ["\n## Related sheets\n"] + sheets
    write(os.path.join(wd, "sources.md"), "\n".join(src) + "\n")

    boards = sorted(glob.glob(os.path.join(HERE, "boards", "*.json")), key=os.path.getmtime)
    ex = json.load(io.open(boards[-1], encoding="utf-8"))
    for p in ex["paragraphs"]:
        for k in ("items", "phases", "files", "entries", "cost", "endstate"):
            if k in p and isinstance(p[k], list): p[k] = p[k][:2]
        for g in p.get("groups", [])[:2]: g["items"] = g["items"][:1]
        if "groups" in p: p["groups"] = p["groups"][:2]
    ex["bolo"]["related"] = ex["bolo"].get("related", [])[:2]
    write(os.path.join(wd, "schema.json"), json.dumps(ex, ensure_ascii=False, indent=1))
    title = re.sub(r"\*\*", "", re.search(r"^\| \d+ \| \*\*(.+?)\*\*", row).group(1)) if re.search(r"^\| \d+ \| \*\*(.+?)\*\*", row) else f"BOLO {n}"
    brief = f"""You are SHEET, the DOPE SHEET specialist for BOLO {n}. Model: sonnet.
READ: {rel(os.path.join(wd, 'sources.md'))} (everything the house has on it) and {rel(os.path.join(wd, 'schema.json'))} (the exact JSON shape; copy keys, not content).
WRITE: {rel(os.path.join(HERE, 'boards', n + '.draft.json'))} — the whole sheet in the schema's shape, filled for BOLO {n} ("{title}"):
  bolo: n · title · trunk · issued (the row's date) · asof (today) · s · status (one header line) · decider "HOTLINE ACTUAL" · feeds · related (n + why, from the rows it names) · home "BOLO.md · row {n}" · card "none" · version "v0.1 · DOPE SHEET"
  mantra: three lines (speed · focus · boldness) specific to this BOLO
  paragraphs S (Situation: groups = the transmission, verbatim where Chief ruled · what exists already · what the record says) · E (Execution: main_effort + phases with n/t/s/when, done phases first) · A (Admin & Logistics: files with path/what/s · cost with k/v) · L (Log: one entry per transmission in the sources, dated, who = Chief or Claude).
  Leave paragraphs M and C as the schema's shape with empty strings; leave frago.order / default / calls empty. The main line writes those.
RULES: every strand (last · plan · you · next) in plain words for a reader who was not there; nothing not in the sources; file paths verbatim; [[key|label]] links only for keys you saw in schema.json. Do not read any other file. Reply with the path and nothing else.
"""
    write(os.path.join(wd, "brief.SHEET.md"), brief)
    print(f"DOPE SHEET prep · BOLO {n} · names {named or '-'} · STATE mentions {len(smentions)} · note mentions {len(nmentions)} · sheets {len(sheets)}")
    print(f"sources {rel(os.path.join(wd, 'sources.md'))} ({os.path.getsize(os.path.join(wd, 'sources.md'))//1024} KB) · brief {rel(os.path.join(wd, 'brief.SHEET.md'))}")
    print(f"next: launch SHEET (sonnet) → main line fills M · C · frago on boards/{n}.draft.json → python check.py {n} → build.py {n} → publish")

if __name__ == "__main__":
    main()
