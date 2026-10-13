# progress report on the teach-back ledger · BOLO 140 · 2026-10-13
import re, sys, datetime as dt
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "_tools/bolostatus/work/95/DOC-SOP.md"
HEAD = re.compile(r"^###\s+(\d+\.\d+)\s+·\s+(.+?)\s+—\s+(LOCKED|RULED)\s+(\d{4}-\d{2}-\d{2})?")

def parse(path):
    parts, cur = [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = HEAD.match(line)
        if m:
            cur = {"id": m.group(1), "title": m.group(2), "state": m.group(3), "date": m.group(4), "say": ""}
            parts.append(cur)
        elif line.startswith(("## ", "### ")):
            cur = None
        elif cur and not cur["say"] and line.startswith("- "):
            cur["say"] = re.sub(r"\*\*|\*", "", line[2:]).strip()
    return parts

def streak(dates):
    ds = sorted({dt.date.fromisoformat(d) for d in dates})
    if not ds: return 0
    n = 1
    for a, b in zip(ds[-2::-1], ds[::-1]):
        if (b - a).days == 1: n += 1
        else: break
    return n

def main():
    if not LEDGER.exists():
        print(f"no ledger; expected at {LEDGER}"); return 0
    parts = parse(LEDGER)
    locked = [p for p in parts if p["state"] == "LOCKED"]
    nxt = next((p for p in parts if p["state"] != "LOCKED"), None)
    dates = [p["date"] for p in locked if p["date"]]
    print(f"topic: {LEDGER.parent.name} / {LEDGER.stem}")
    print(f"parts total: {len(parts)}")
    print(f"locked: {len(locked)}")
    print(f"next part: {nxt['id'] + ' ' + nxt['title'] + ' (' + nxt['state'] + ')' if nxt else 'none'}")
    print(f"last session date: {max(dates) if dates else 'none'}")
    print(f"streak (consecutive days with a lock): {streak(dates)}")
    return 0
if __name__ == "__main__":
    sys.exit(main())
