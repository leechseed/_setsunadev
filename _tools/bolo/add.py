# -*- coding: utf-8 -*-
"""BOLO add — capture a tasking as a numbered row with the housekeeping done (BOLO 51 phase 8; pure script).

Usage:  python _tools/bolo/add.py "<title>" "<body markdown>" [--trunk "BLACK, feeds X"] [--status "🟡 open"] [--dry]

Does:   next number = max row + 1 · row appended after the last active row · header `updated:` stamped today ·
        glossary.json gets a boloN stub (t · k=item · d = the title · w) · prints the DOPE SHEET prep command.
The wording is the main line's; the numbering, dating, and stubs are the script's.
"""
import io, json, os, re, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

def main():
    a = sys.argv[1:]
    if len(a) < 2: print(__doc__); sys.exit(2)
    title, body = a[0], a[1]
    trunk = a[a.index("--trunk") + 1] if "--trunk" in a else "OPERATOR"
    status = a[a.index("--status") + 1] if "--status" in a else "🟡 open — captured, not started"
    dry = "--dry" in a
    today = datetime.date.today()
    bp = os.path.join(ROOT, "BOLO.md")
    text = io.open(bp, encoding="utf-8").read()
    rows = [(int(m.group(1)), m.start(), m.end()) for m in re.finditer(r"^\| (\d+) \| .+\|$", text, re.M)]
    n = max(r[0] for r in rows) + 1
    last_end = max(r[2] for r in rows)
    row = f"\n| {n} | **{title}** [{trunk}] - spoken {today.month}/{today.day}. {body} | {today.isoformat()} | {status} |"
    new = text[:last_end] + row + text[last_end:]
    new = re.sub(r"^updated: .*$", f"updated: {today.isoformat()}", new, count=1, flags=re.M)
    gp = os.path.join(ROOT, "_tools", "sitrep", "glossary.json")
    g = json.load(io.open(gp, encoding="utf-8"))
    stub = {"t": f"BOLO {n}", "k": "item", "d": f"{title}. Captured {today.month}/{today.day}.", "w": f"BOLO.md #{n} · DOPE SHEET {n}"}
    print(f"BOLO {n} · {title[:70]} · [{trunk}] · {status}")
    if dry:
        print("--dry: nothing written"); print(row.strip()[:300]); return
    io.open(bp, "w", encoding="utf-8", newline="\n").write(new)
    if f"bolo{n}" not in g:
        g[f"bolo{n}"] = stub
        io.open(gp, "w", encoding="utf-8", newline="\n").write(json.dumps(g, ensure_ascii=False, indent=1))
    print(f"row {n} appended · BOLO.md updated: {today.isoformat()} · glossary bolo{n} stubbed")
    print(f"next: python _tools/bolostatus/prep.py {n}  (the DOPE SHEET formation)")

if __name__ == "__main__":
    main()
