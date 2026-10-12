"""dupes.py — clear duplicate videos out of Stash (Chief 10/12: "go thru stash and delete any duplicate videos you can find").

Two kinds of duplicate, both found by Stash itself:
  copies   one scene holding two or more files with the same fingerprint (byte-identical copies)
  matches  separate scenes whose perceptual hashes are identical (distance 0) and whose lengths agree within 1 s:
           the same video, often at a different size or encode

For each group the script keeps the best file (most pixels, then highest bitrate, then largest), merges every other
scene into the keeper's scene (play history, O history, tags and performers carried over), makes the best file
primary, and deletes the rest through Stash. Deletes go to a trash folder outside the library (Stash's own
deleteTrashPath, set for the run and restored after), so nothing is gone until the trash is emptied.

Usage: python dupes.py              dry run: counts and the GB to free, writes the plan
       python dupes.py --apply      do it
The plan and the action log (file paths) go to _PRIVATE/stashdupes/.
"""

import json
import os
import sys
import time
import urllib.request

API = "http://127.0.0.1:9999/graphql"
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "_PRIVATE", "stashdupes")
TRASH = "Q:\\_STASH_TRASH"          # outside every library root, so a rescan never re-adds it
MIN_LEN = 20                       # seconds; short clips (intros, loops) collide on phash, so they are never matched

SCENE = "id title o_counter play_count tags { id } performers { id } files { id path size width height bit_rate duration }"


def gql(q, v=None):
    req = urllib.request.Request(API, data=json.dumps({"query": q, "variables": v or {}}).encode(),
                                 headers={"Content-Type": "application/json"})
    r = json.load(urllib.request.urlopen(req, timeout=600))
    if r.get("errors"):
        raise RuntimeError(r["errors"][0]["message"])
    return r["data"]


def rank(f):
    return ((f.get("width") or 0) * (f.get("height") or 0), f.get("bit_rate") or 0, f.get("size") or 0)


def groups():
    out = []
    multi = gql("query { findScenes(scene_filter:{file_count:{value:1,modifier:GREATER_THAN}}, filter:{per_page:-1})"
                " { scenes { %s } } }" % SCENE)["findScenes"]["scenes"]
    for s in multi:
        out.append({"kind": "copies", "scenes": [s]})
    dup = gql("query { findDuplicateScenes(distance:0, duration_diff:1) { %s } }" % SCENE)["findDuplicateScenes"]
    seen = {s["id"] for s in multi}
    for g in dup:
        if any((f.get("duration") or 0) < MIN_LEN for s in g for f in s["files"]):
            continue
        ratios = [f["width"] / f["height"] for s in g for f in s["files"] if f.get("width") and f.get("height")]
        if not ratios or max(ratios) / min(ratios) > 1.02:   # a crop or a portrait cut of the same scene is not a duplicate
            continue
        out = [x for x in out if not (x["kind"] == "copies" and x["scenes"][0]["id"] in {s["id"] for s in g})]
        out.append({"kind": "matches", "scenes": g})
    return out


def plan(gs):
    rows = []
    for g in gs:
        files = [(s, f) for s in g["scenes"] for f in s["files"]]
        keep_s, keep_f = max(files, key=lambda sf: rank(sf[1]))
        drop = [f for s, f in files if f["id"] != keep_f["id"]]
        rows.append({"kind": g["kind"], "keep_scene": keep_s["id"], "keep_file": keep_f["id"], "keep_path": keep_f["path"],
                     "merge": [s["id"] for s in g["scenes"] if s["id"] != keep_s["id"]],
                     "tags": sorted({t["id"] for s in g["scenes"] for t in s["tags"]}),
                     "performers": sorted({p["id"] for s in g["scenes"] for p in s["performers"]}),
                     "drop": [{"id": f["id"], "path": f["path"], "size": f["size"]} for f in drop]})
    return rows


def apply(rows, log):
    old = gql("query { configuration { general { deleteTrashPath } } }")["configuration"]["general"]["deleteTrashPath"]
    os.makedirs(TRASH, exist_ok=True)
    gql("mutation($p:String){ configureGeneral(input:{deleteTrashPath:$p}) { deleteTrashPath } }", {"p": TRASH})
    done = failed = 0
    try:
        for r in rows:
            try:
                if r["merge"]:
                    gql("mutation($i:SceneMergeInput!){ sceneMerge(input:$i) { id } }",
                        {"i": {"source": r["merge"], "destination": r["keep_scene"], "play_history": True, "o_history": True,
                               "values": {"id": r["keep_scene"], "tag_ids": r["tags"], "performer_ids": r["performers"]}}})
                gql("mutation($i:SceneUpdateInput!){ sceneUpdate(input:$i) { id } }",
                    {"i": {"id": r["keep_scene"], "primary_file_id": r["keep_file"]}})
                gql("mutation($ids:[ID!]!){ deleteFiles(ids:$ids) }", {"ids": [d["id"] for d in r["drop"]]})
                done += 1
                log.write(json.dumps(dict(r, ok=True), ensure_ascii=False) + "\n")
            except Exception as e:
                failed += 1
                log.write(json.dumps(dict(r, ok=False, error=str(e)), ensure_ascii=False) + "\n")
            log.flush()
    finally:
        gql("mutation($p:String){ configureGeneral(input:{deleteTrashPath:$p}) { deleteTrashPath } }", {"p": old})
    return done, failed


def main():
    os.makedirs(OUT, exist_ok=True)
    rows = plan(groups())
    gb = sum(d["size"] for r in rows for d in r["drop"]) / 1e9
    by = {k: sum(1 for r in rows if r["kind"] == k) for k in ("copies", "matches")}
    nfiles = sum(len(r["drop"]) for r in rows)
    stamp = time.strftime("%Y%m%d-%H%M")
    json.dump(rows, open(os.path.join(OUT, f"plan-{stamp}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"groups: {by['copies']} copy groups · {by['matches']} match groups · {nfiles} files to delete · {gb:.1f} GB")
    if "--apply" not in sys.argv:
        print("dry run; --apply does it")
        return
    with open(os.path.join(OUT, f"log-{stamp}.jsonl"), "w", encoding="utf-8") as log:
        done, failed = apply(rows, log)
    print(f"applied: {done} groups cleared · {failed} failed · trash {TRASH} (empty it to free the {gb:.1f} GB)")


if __name__ == "__main__":
    main()
