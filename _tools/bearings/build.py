"""bearings/build.py — THE BEARINGS glass (10/14): repos · Kit · SOPs, matched, with run counts.

Reads _tools/bearings/data/: repos.json · kit.json · sops.json · runs.json (collect.py, zero tokens) and
briefs.skills.json · briefs.agents.json · match.json (the three specialists). Checks the fan-in (RANGE, the script
reviewer): every kit piece has a brief, every matched name is a real kit piece or repo. Writes _tools/bearings/bearings.html.
Usage: python _tools/bearings/build.py
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
OUT = os.path.join(HERE, "bearings.html")


def load(name, default):
    p = os.path.join(DATA, name)
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return default


def range_check(kit, repos, briefs, match):
    names = {k["name"] for k in kit}
    slugs = {r["repo"] for r in repos}
    f = []
    miss = sorted(names - set(briefs))
    if miss:
        f.append(f"{len(miss)} kit piece(s) without a brief: {', '.join(miss[:8])}")
    bad_k = sorted(set(match.get("by_kit", {})) - names)
    if bad_k:
        f.append(f"match names unknown kit piece(s): {', '.join(bad_k[:8])}")
    bad_r = sorted({m["repo"] for v in match.get("by_kit", {}).values() for m in v} - slugs)
    bad_r += sorted(set(match.get("by_repo", {})) - slugs)
    if bad_r:
        f.append(f"match names unknown repo(s): {', '.join(sorted(set(bad_r))[:8])}")
    nore = sorted(slugs - set(match.get("by_repo", {})))
    if nore and match:
        f.append(f"{len(nore)} repo(s) without a gist: {', '.join(nore[:8])}")
    return f


def main():
    repos, kit, sops, runs = load("repos.json", []), load("kit.json", []), load("sops.json", []), load("runs.json", {})
    briefs = {**load("briefs.skills.json", {}), **load("briefs.agents.json", {})}
    match = load("match.json", {})
    # the sitrep skill and the sitrep workflow share a name: the workflow rides as "<name> workflow" everywhere
    for k in kit:
        if k["kind"] == "workflow" and any(o["name"] == k["name"] and o["kind"] != "workflow" for o in kit):
            old, k["name"] = k["name"], k["name"] + " workflow"
            if "workflow:" + old in briefs:
                briefs[k["name"]] = briefs.pop("workflow:" + old)
    findings = range_check(kit, repos, briefs, match)
    # drop match rows that point nowhere, so the page never shows a dead chip
    slugs, names = {r["repo"] for r in repos}, {k["name"] for k in kit}
    match["by_kit"] = {k: [m for m in v if m.get("repo") in slugs] for k, v in match.get("by_kit", {}).items() if k in names}
    payload = {"repos": repos, "kit": kit, "sops": sops, "runs": runs, "briefs": briefs, "match": match,
               "built": time.strftime("%b %d, %I:%M %p").replace(" 0", " "), "findings": findings}
    blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    html = open(os.path.join(HERE, "template.html"), encoding="utf-8").read().replace("/*__DATA__*/null", blob)
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"BEARINGS build · repos {len(repos)} · kit {len(kit)} · briefs {len(briefs)} · "
          f"matched {sum(1 for v in match['by_kit'].values() if v)} · sops {len(sops)} · {len(html) // 1024} KB -> {OUT}")
    for x in findings:
        print("  RANGE:", x)
    return 1 if any("unknown" in x for x in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
