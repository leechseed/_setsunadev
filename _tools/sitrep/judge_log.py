"""Escalation Judge ledger helper (BOLO 122).
Usage:  python _tools/sitrep/judge_log.py "<trigger>" "<note>"
Triggers: rerun, fable-job, gear-above-2, two-failed-fixes (ids in judge_triggers.json).
The main line calls it for the two triggers that leave no trace: gear-above-2, two-failed-fixes.
Appends one line to judge_ledger.jsonl (assemble.py appends one per board).
"""
import datetime, io, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

def main():
    if len(sys.argv) != 3:
        print(__doc__); sys.exit(2)
    ids = {t["id"] for t in json.load(io.open(os.path.join(HERE, "judge_triggers.json"), encoding="utf-8"))["triggers"]}
    trig, note = sys.argv[1], sys.argv[2]
    if trig not in ids:
        print("unknown trigger %r; use one of: %s" % (trig, ", ".join(sorted(ids)))); sys.exit(1)
    line = {"ts": datetime.datetime.now().isoformat(timespec="seconds"), "src": "judge_log", "trigger": trig, "note": note}
    with io.open(os.path.join(HERE, "judge_ledger.jsonl"), "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(line, ensure_ascii=False) + "\n")
    print("logged", trig)

if __name__ == "__main__":
    main()
