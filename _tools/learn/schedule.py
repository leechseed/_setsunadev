# intervals in the spirit of hluaguo/learn-faster-kit (MIT) · BOLO 140 · 2026-10-13
# usage: schedule.py [--mark <part-id> hit|miss] [--today YYYY-MM-DD]
import json, sys, datetime as dt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import progress

OUT = Path(__file__).resolve().parent / "schedule.json"
STEPS = [1, 3, 7, 14, 30]  # days; kit uses 1,3,7,14,30,60,90 and has no miss rule

def load():
    if OUT.exists():
        return json.loads(OUT.read_text(encoding="utf-8"))
    return {}

def main(argv):
    today = dt.date.today()
    if "--today" in argv:
        today = dt.date.fromisoformat(argv[argv.index("--today") + 1])
    if not progress.LEDGER.exists():
        print(f"no ledger; expected at {progress.LEDGER}"); return 0
    parts = {p["id"]: p for p in progress.parse(progress.LEDGER) if p["state"] == "LOCKED"}
    sched = load()
    for pid, p in parts.items():
        if pid not in sched:
            base = dt.date.fromisoformat(p["date"]) if p["date"] else today
            sched[pid] = {"step": 0, "next": (base + dt.timedelta(days=STEPS[0])).isoformat()}
        sched[pid]["title"] = p["title"]; sched[pid]["say"] = p["say"]
    if "--mark" in argv:
        i = argv.index("--mark")
        pid, res = argv[i + 1], argv[i + 2]
        if pid not in sched or res not in ("hit", "miss"):
            print("usage: --mark <locked part id> hit|miss"); return 1
        s = sched[pid]
        s["step"] = min(s["step"] + 1, len(STEPS) - 1) if res == "hit" else 0
        # a hit moves up one step; a miss drops to 1 day (pushed back, back to the start)
        s["next"] = (today + dt.timedelta(days=STEPS[s["step"]])).isoformat()
        s["last"] = {"date": today.isoformat(), "result": res}
        print(f"{pid} {res}: next re-check {s['next']}")
    OUT.write_text(json.dumps(sched, indent=1, ensure_ascii=False), encoding="utf-8")
    due = sorted((k for k, v in sched.items() if v["next"] <= today.isoformat()), key=lambda k: [int(x) for x in k.split(".")])
    print(f"due {today.isoformat()}: {len(due)} of {len(sched)}")
    for k in due:
        print(f"  {k} {sched[k]['title']} (due {sched[k]['next']})\n     say: {sched[k]['say']}")
    return 0
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
