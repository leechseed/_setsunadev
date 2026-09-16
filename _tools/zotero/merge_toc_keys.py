# -*- coding: utf-8 -*-
"""BOLO 18 stage 2, step 2c: merge a PS's TOC-derived spine keys (spinekeys-toc44.json) into inventory-live.json,
then rebuild SPINE-KEYS.md by re-running spinekey.py (which never overwrites a key already set).

Usage: python _tools/zotero/merge_toc_keys.py [_0.1_BVX_LEARN/_meta/spinekeys-toc44.json]
"""
import io, os, sys, json, subprocess, collections
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
META = os.path.join(ROOT, "_0.1_BVX_LEARN", "_meta")
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(META, "spinekeys-toc44.json")
VALID = {"L0", "L4", "L5", "L6", "L7", "SETTING", "TEXTURE", "CRAFT-PROCESS", "OFF"}


def main():
    keys = json.load(io.open(SRC, encoding="utf-8"))
    p = os.path.join(META, "inventory-live.json"); items = json.load(io.open(p, encoding="utf-8"))
    by_bvx = collections.defaultdict(list)
    for it in items:
        by_bvx[it.get("bvx") or "NEW"].append(it)
    applied, off, bad = 0, 0, []
    for k in keys:
        spine = [s for s in k.get("spine", []) if s in VALID]
        if not spine:
            bad.append(k.get("bvx")); continue
        cands = by_bvx.get(k["bvx"], [])
        if k["bvx"] == "NEW":
            cands = [i for i in cands if i["title"].strip().lower() == (k.get("title") or "").strip().lower()]
        for it in cands:
            if it.get("spine_src") != "none":
                continue
            if spine == ["OFF"]:
                it["spine"] = []; it["spine_src"] = "toc-off"; it["subject_note"] = "not a story book (PS TOC pass)"; off += 1
            else:
                it["spine"] = spine; it["spine_src"] = "toc"; applied += 1
            it["spine_why"] = k.get("why", "")
    io.open(p, "w", encoding="utf-8", newline="\n").write(json.dumps(items, ensure_ascii=False, indent=1))
    print(f"applied {applied} · off {off} · unusable {bad}")
    r = subprocess.run([sys.executable, os.path.join(HERE, "spinekey.py")], capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(r.stdout.strip())


if __name__ == "__main__":
    main()
