"""autotag.py - BOLO 28 v1 auto-tagger, DRY RUN ONLY (reads Stash, writes a report; never writes tags, never touches media).
v1a = text pass: propose EXISTING Stash tags from title / filename / folder / duration. v1b (frame/CLIP pass) is a later call.
    python autotag.py [--limit N]
Out: _PRIVATE/stash_autotag_dryrun.md + _PRIVATE/stash_autotag_dryrun.json"""
import io, json, os, re, sys, urllib.request, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "_PRIVATE", "stash_autotag_dryrun")
# tag -> regex over title+path (word-bounded). Only existing tag names. Identity tags (gay/straight/bbc) left to Chief.
RULES = {
 "Blowjob": r"blow ?job|\bbj\b|sucks?\b|cock ?sucking", "Deep Throat": r"deep ?throat|deepthroat", "throat": r"throat|face ?fuck",
 "anal": r"\banal\b|ass ?fuck", "Squirting": r"squirt", "Gangbang": r"gang ?bang|\bgb\b", "Group Sex": r"orgy|foursome|threesome|group",
 "Amateur": r"amateur|homemade", "public": r"public|outdoor|beach|park\b", "gloryhole": r"glory ?hole",
 "Bareback": r"bareback|raw\b", "fist": r"fist", "pegging": r"pegg", "Rimjob": r"rim ?job|rimming|ass licking",
 "Big Tits": r"big tits|busty|big boobs", "Big Ass": r"big ass|phat ass|\bpawg\b", "Booty": r"booty|twerk",
 "MILF": r"milf|mom\b|mother", "Wife": r"\bwife\b|hotwife", "Redhead": r"redhead|ginger", "Twink": r"twinks?\b",
 "Gangbang ": r"^$", "compilation": r"compilation|compil\b|best of|\bpmv\b|\bhmv\b", "pmv": r"\bpmv\b", "hmv": r"\bhmv\b",
 "Stretching": r"stretch|gape", "Squirting Orgasm": r"^$", "Interracial": r"interracial|\bir\b|bbc.*(white|blonde)|blacked",
 "Big Dick": r"big dick|huge cock|monster cock|big cock", "Cumming": r"\bcum(s|ming)?\b|cumshot|facial", "solo": r"\bsolo\b|masturbat|jerk(ing)? off",
 "Nude": r"nude|naked", "Rough Sex": r"rough|brutal", "Challenge": r"challenge",
}
RULES = {k.strip(): re.compile(v, re.I) for k, v in RULES.items() if v != "^$"}
def gql(q, v=None):
    r = urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:9999/graphql", data=json.dumps({"query": q, "variables": v or {}}).encode(), headers={"Content-Type": "application/json"}), timeout=60)
    d = json.load(r)
    if d.get("errors"): raise RuntimeError(d["errors"][0]["message"])
    return d["data"]
def main():
    lim = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else 0
    have = {t["name"] for t in gql('{findTags(filter:{per_page:-1}){tags{name}}}')["findTags"]["tags"]}
    rules = {k: v for k, v in RULES.items() if k in have}
    scenes, page = [], 1
    while True:
        d = gql('query($p:Int){findScenes(filter:{per_page:500,page:$p,sort:"id"}){count scenes{id title files{path duration} tags{name}}}}', {"p": page})["findScenes"]
        scenes += d["scenes"]
        if len(scenes) >= d["count"] or not d["scenes"] or (lim and len(scenes) >= lim): break
        page += 1
    props, hits, untagged, covered = [], collections.Counter(), 0, 0
    for s in scenes:
        cur = {t["name"] for t in s["tags"]}
        if not cur: untagged += 1
        f = (s["files"] or [{}])[0]
        text = " ".join([s.get("title") or "", f.get("path") or ""])
        new = [t for t, rx in rules.items() if t not in cur and rx.search(text)]
        if f.get("duration") and f["duration"] < 300 and "pmv" not in cur and False: pass
        if new:
            covered += 1; hits.update(new)
            props.append({"id": s["id"], "title": s.get("title"), "have": sorted(cur), "propose": new})
    json.dump(props, io.open(OUT + ".json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    with io.open(OUT + ".md", "w", encoding="utf-8") as o:
        o.write(f"# Stash auto-tagger v1a DRY RUN\n\nScenes scanned {len(scenes)} · untagged {untagged} · scenes with a proposal {covered}. Nothing written to Stash.\n\n## Proposals by tag\n")
        for t, n in hits.most_common(): o.write(f"- {t}: {n}\n")
        o.write("\n## Sample (first 60)\n")
        for p in props[:60]: o.write(f"- [{p['id']}] {p['title']} -> {', '.join(p['propose'])}\n")
    print(len(scenes), untagged, covered, hits.most_common(8))
main()
