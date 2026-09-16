# -*- coding: utf-8 -*-
"""BOLO 18 stage 2, step 2b: give every story-side item (CRE + LIT) a story-spine key.
Order of authority: Papi's 0N_ tags (already imported by inventory.py, never overwritten) > title rules here (marked `spine_src: rule`).
Items no rule reaches get `spine: ["L0?"]` + `spine_src: none` and land in the review list for a PS pass on their TOC.
Spine levels: L0 root theory · L4 plot · L5 character · L6 theme · L7 genre/medium/audience · SETTING · TEXTURE (telling / narration).

Usage: python _tools/zotero/spinekey.py
"""
import io, os, re, sys, json, collections, datetime
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
META = os.path.join(ROOT, "_0.1_BVX_LEARN", "_meta")

RULES = [  # first match wins per level; an item may take several levels
 ("L5", r"character|protagonist|hero|villain|antagonist|side characters|archetype|persona|psychology of|motivation|dialogue"),
 ("L4", r"\bplot|structure|beat sheet|save the cat|story grid|steps|outline|scene|sequence|act\b|three-act|pacing|suspense|conflict|action:|screenplay|screenwriting|scriptwriting|story engineering|story physics|anatomy of story"),
 ("L7", r"genre|science fiction|fantasy|horror|romance|thriller|mystery|crime|noir|comedy|serial drama|television|film\b|video game writing|game writing|interactive|transmedia|multiplatform|audience|reader|publishing|market"),
 ("TEXTURE", r"narrat|point of view|viewpoint|voice|focaliz|diegesis|dialogue|description|prose|style|sentence|show.*tell|exposition|tense"),
 ("SETTING", r"world-?building|setting|fictional worlds|world\b|place|landscape|geography|environment|milieu"),
 ("L6", r"theme|meaning|moral|premise|allegory|ideology|ethic|value"),
 ("L0", r"narratolog|theory of|poetics|semiotic|structuralis|formalis|rhetoric of|philosophy of|what is (a )?story|storytelling animal|why fiction|affective|cognitive|neuro|mythology|monomyth|hero with a thousand|dramatica"),
]
COMPILED = [(lvl, re.compile(rx, re.I)) for lvl, rx in RULES]


def main():
    p = os.path.join(META, "inventory-live.json")
    items = json.load(io.open(p, encoding="utf-8"))
    story = [i for i in items if i.get("subject") in ("CRE", "LIT")]
    c = collections.Counter(); review = []
    for it in story:
        if it.get("spine"):
            it.setdefault("spine_src", "tag"); c["tag"] += 1; continue
        blob = " ".join([it["title"], " ".join(it["tags"]), " ".join(it["collections"])])
        lv = [lvl for lvl, rx in COMPILED if rx.search(blob)]
        if lv:
            it["spine"] = lv[:3]; it["spine_src"] = "rule"; c["rule"] += 1
        else:
            it["spine"] = ["L0?"]; it["spine_src"] = "none"; c["none"] += 1; review.append(it)
    io.open(p, "w", encoding="utf-8", newline="\n").write(json.dumps(items, ensure_ascii=False, indent=1))
    lvc = collections.Counter(l for i in story for l in i["spine"])
    L = ["---", "id: BVX-LEARN.spine-keys", "title: \"Story-side spine keys (BOLO 18 stage 2)\"", "type: report",
         f"generated: {datetime.date.today()}", "status: BOLO 18 stage 2 - step 2b", "---", "",
         "# Story-side spine keys", "",
         f"{len(story)} CRE + LIT items. Authority: Papi's tags, then title rules, then a review list for a PS pass on each TOC.", "",
         "| Source | Items |", "|---|---|"] + [f"| {k} | {v} |" for k, v in c.most_common()]
    L += ["", "## Items per level", "", "| Level | Items |", "|---|---|"] + [f"| {k} | {v} |" for k, v in lvc.most_common()]
    L += ["", "## The shelves", ""]
    for lvl in ["L0", "L4", "L5", "L6", "L7", "SETTING", "TEXTURE"]:
        rows = sorted((i for i in story if lvl in i["spine"]), key=lambda i: (i["spine_src"] != "tag", i["title"].lower()))
        L += [f"### {lvl} ({len(rows)})", "", "| BVX | Title | Author | Year | Key from |", "|---|---|---|---|---|"]
        L += [f"| {i['bvx'] or 'NEW'} | {i['title'][:72]} | {', '.join(i['authors'])[:28]} | {i['year']} | {i['spine_src']} |" for i in rows] + [""]
    L += [f"## Review list, no rule reached them ({len(review)})", "", "| BVX | Title | Author |", "|---|---|---|"]
    L += [f"| {i['bvx'] or 'NEW'} | {i['title'][:72]} | {', '.join(i['authors'])[:28]} |" for i in review]
    io.open(os.path.join(META, "SPINE-KEYS.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    print("story-side", len(story), dict(c)); print("levels", dict(lvc.most_common()))


if __name__ == "__main__":
    main()
