"""hour.py — `command hour` / `fresh hour` (Chief 10/30): a fresh hour of BBC straight into a new VLC window.

  python hour.py                      # 60 min, gay BBC lists + straight BBC from Stash, no PMVs, nothing played today
  python hour.py --minutes 90 --only gay|straight --side left|right
  python hour.py --dry-run --json     # build the list, print it, write and launch nothing

Rules (Chief): "just BBC in general, no PMV cause I'm watching the anime". PMV = any scene tagged pmv* or with pmv in its
name; those are out. The played ledger is every playlist file dated today in _PRIVATE/playlists/ (SP-012). The new window
never closes another VLC (stashplay.launch does not stop anything). Straight BBC = a Black male performer or BBC in the
title, plus a woman, no gay tag, no PMV (stash-bbc-filter, 10/4). The m3u written here counts as today's ledger next time.
"""
import argparse
import json
import os
import random
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "_tools", "dictation"))
import stashplay as sp  # noqa: E402

PL = os.path.join(ROOT, "_PRIVATE", "playlists")
GAY_POOLS = ["gay-bbc-all-left-2026-10-12.m3u"]
MAX_CLIP = 900
MIN_CLIP = 20


def norm(p):
    return os.path.normpath(p).lower()


def played_today():
    day = time.strftime("%Y-%m-%d")
    used = set()
    for f in os.listdir(PL):
        if day in f and f.endswith((".m3u", ".m3u8")):
            for line in open(os.path.join(PL, f), encoding="utf-8", errors="replace"):
                if line.strip() and not line.startswith("#"):
                    used.add(norm(line.strip()))
    return used


def is_pmv(*texts):
    return any("pmv" in (t or "").lower() for t in texts)


def gay_pool(used):
    out = []
    for f in GAY_POOLS:
        lines = [l.rstrip("\n") for l in open(os.path.join(PL, f), encoding="utf-8", errors="replace")]
        for i, l in enumerate(lines):
            m = re.match(r"#EXTINF:(\d+),(.*)", l)
            if m and i + 1 < len(lines):
                d, title, p = int(m.group(1)), m.group(2), lines[i + 1].strip()
                if p and norm(p) not in used and MIN_CLIP <= d <= MAX_CLIP and not is_pmv(title, p):
                    out.append({"kind": "gay", "dur": d, "title": title, "path": p})
    return out


def straight_pool(used):
    ids = [p["id"] for p in sp.gql('query{ findPerformers(performer_filter:{ethnicity:{value:"Black",modifier:EQUALS}, gender:{value:MALE,modifier:EQUALS}}, filter:{per_page:-1}){ performers{ id } } }')["findPerformers"]["performers"]]
    tags = sp.gql('query{ findTags(filter:{q:"pmv", per_page:50}){ tags{ id name } } }')["findTags"]["tags"]
    gay = sp.gql('query{ findTags(filter:{q:"gay", per_page:50}){ tags{ id name } } }')["findTags"]["tags"]
    bad = [t["id"] for t in tags if t["name"].lower().startswith("pmv")] + [t["id"] for t in gay if t["name"].lower() == "gay"]
    seed = random.randint(1, 10**9)
    q = ('query($f:SceneFilterType,$s:String){ findScenes(scene_filter:$f, filter:{per_page:500, sort:$s}) { scenes { %s } } }' % sp.FIELDS)
    scenes = sp.gql(q, {"f": {"performers": {"value": ids, "modifier": "INCLUDES"}, "tags": {"value": bad, "modifier": "EXCLUDES"}}, "s": "random_%d" % seed})["findScenes"]["scenes"]
    scenes += sp.gql(q, {"f": {"title": {"value": "bbc", "modifier": "INCLUDES"}, "tags": {"value": bad, "modifier": "EXCLUDES"}}, "s": "random_%d" % seed})["findScenes"]["scenes"]
    out, seen_t, seen_i = [], set(), set()
    for s in scenes:
        if s["id"] in seen_i or not s.get("files"):
            continue
        seen_i.add(s["id"])
        f = s["files"][0]
        d = int(f.get("duration") or 0)
        title = (s.get("title") or f.get("basename") or "").strip()
        if not (MIN_CLIP <= d <= MAX_CLIP) or norm(f["path"]) in used or is_pmv(title, f["path"]):
            continue
        if not any((p.get("gender") or "").upper() in ("FEMALE", "TRANSGENDER_FEMALE") for p in s.get("performers") or []):
            continue
        if title.lower() in seen_t:
            continue
        seen_t.add(title.lower())
        out.append({"kind": "straight", "dur": d, "title": title, "path": f["path"]})
    return out


def build(minutes, only):
    used = played_today()
    pools = []
    if only in (None, "gay"):
        pools.append(gay_pool(used))
    if only in (None, "straight"):
        pools.append(straight_pool(used))
    want = minutes * 60
    picked, total = [], 0
    for pool in pools:
        random.shuffle(pool)
        share, got = want / len(pools), 0
        for c in pool:
            if got >= share:
                break
            picked.append(c)
            got += c["dur"]
        total += got
    random.shuffle(picked)
    return picked, total, len(used)


def next_name():
    day = time.strftime("%Y-%m-%d")
    n = 1 + sum(1 for f in os.listdir(PL) if f.startswith("bbc-hour") and day in f)
    return os.path.join(PL, "bbc-hour%d-%s.m3u" % (n, day))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--minutes", type=int, default=60)
    ap.add_argument("--only", choices=["gay", "straight"])
    ap.add_argument("--side", default="left")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    picked, total, nused = build(a.minutes, a.only)
    if not picked:
        sys.exit("Nothing fresh left in the pool for today.")
    kinds = {k: sum(1 for c in picked if c["kind"] == k) for k in ("gay", "straight")}
    line = "%d clips, %d min (%d gay, %d straight), skipped %d already played today" % (len(picked), round(total / 60), kinds["gay"], kinds["straight"], nused)
    if a.json:
        print(json.dumps({"summary": line, "dry_run": a.dry_run, "clips": picked}, indent=1))
    if a.dry_run:
        if not a.json:
            print("dry run: " + line)
        return
    out = next_name()
    with open(out, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n" + "".join("#EXTINF:%d,%s\n%s\n" % (c["dur"], c["title"].replace("\n", " "), c["path"]) for c in picked))
    ok = sp.launch(out, side=a.side)
    if not a.json:
        print(("Fresh hour is up: " if ok else "Built, but the window did not report in: ") + line + "  [" + os.path.basename(out) + "]")


main()
