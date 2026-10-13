"""bandit.py - epsilon-greedy ranking of tag / performer arms for the fresh-hour picker (BOLO 140, rl-02).

python _tools/stashplay/bandit.py [--arm tag|performer] [--eps 0.1] [--top 20] --dry

Reads the played ledger (_tools/dictation/_stashplay_played.json: a flat list of scene ids played) and,
if present, an outcomes file (_tools/dictation/_stashplay_outcomes.json: {scene_id: "through"|"skipped"|"spit"}).
No outcomes file yet, so a ledger id counts as "through" (weak reward 1.0); skipped = 0, spit = 2.
Arms come from the stash.sqlite COPY (_PRIVATE/dbcopies, read-only), never the live DB. Prints ids only.
--dry: print only; this script changes no set and no ledger (it has no write path).
Score = mean reward of an arm's pool scenes (unplayed count as 0, so reach is penalised); with probability
eps an arm is marked EXPLORE (a rarely-played arm to try), the rest EXPLOIT in score order.
"""
import argparse
import json
import os
import random
import sqlite3

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB = os.path.join(ROOT, "_PRIVATE", "dbcopies", "stash.sqlite")
DICT = os.path.join(ROOT, "_tools", "dictation")
REWARD = {"through": 1.0, "skipped": 0.0, "spit": 2.0}
SQL = {"tag": "SELECT tag_id, scene_id FROM scenes_tags", "performer": "SELECT performer_id, scene_id FROM performers_scenes"}


def load(name, default):
    try:
        with open(os.path.join(DICT, name), encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--arm", default="tag", choices=list(SQL))
    ap.add_argument("--eps", type=float, default=0.1)
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    played = {str(i) for i in load("_stashplay_played.json", [])}
    out = {str(k): v for k, v in load("_stashplay_outcomes.json", {}).items()}
    reward = {s: REWARD.get(out.get(s, "through"), 1.0) for s in played}
    c = sqlite3.connect("file:" + DB.replace("\\", "/") + "?mode=ro", uri=True)
    c.execute("PRAGMA query_only=1")
    pool, hit = {}, {}
    for arm, sc in c.execute(SQL[a.arm]):
        pool[arm] = pool.get(arm, 0) + 1
        if str(sc) in reward:
            hit.setdefault(arm, []).append(reward[str(sc)])
    c.close()
    rows = [(arm, n, len(hit.get(arm, [])), sum(hit.get(arm, [])) / n) for arm, n in pool.items() if n >= 5]
    rows.sort(key=lambda r: -r[3])
    rare = sorted(rows, key=lambda r: (r[2], -r[1]))[:a.top]
    print("arm=%s ledger=%d outcomes=%d arms(>=5 scenes)=%d eps=%.2f" % (a.arm, len(played), len(out), len(rows), a.eps))
    print("rank  %s_id  pool  played  score   pick" % a.arm)
    for i, r in enumerate(rows[:a.top], 1):
        mode = "EXPLORE" if random.random() < a.eps else "exploit"
        if mode == "EXPLORE" and rare:
            r = random.choice(rare)
        print("%4d  %6s  %4d  %6d  %.3f  %s" % (i, r[0], r[1], r[2], r[3], mode))
    if not a.dry:
        print("(nothing written: this script only prints; wire the ranking into the fresh-hour builder by hand)")


if __name__ == "__main__":
    main()
