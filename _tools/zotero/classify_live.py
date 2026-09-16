# -*- coding: utf-8 -*-
"""BOLO 18 stage 2, step 2: classify the items in inventory-live.json that have no catalog subject yet,
using the approved 17-category RULES from _0.1_BVX_LEARN/_meta/classify.py (imported by text, the module is not importable).
Writes: subject + confidence back into inventory-live.json (field `subject`, `subject_src` = catalog | rule | tag | none),
and _0.1_BVX_LEARN/_meta/CLASSIFY-LIVE.md (the report + the unmatched queue for Papi's eyes).

Usage: python _tools/zotero/classify_live.py
"""
import io, os, re, sys, json, collections, datetime
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
META = os.path.join(ROOT, "_0.1_BVX_LEARN", "_meta")

# Papi's own media-type / subject tags settle the subject before any title rule runs
TAG2SUBJ = {"080007 - TABLE TOP GAME DESIGN": "GAM", "080006 - VIDEO GAME DESIGN": "GAM", "SEX": "MSX",
            "MILITARY SCIENCE": "MIL", "COMPUTER SCIENCE & WEBDEV": "TEC", "HEALTH & FITNESS": "FIT",
            "080009 - PHOTOGRAPHY": "VIS", "080002 - film & 080003 - television": "VIS", "080002 - film": "VIS",
            "080004 - art": "VIS", "080004 - art & 080005 - design": "DSN", "0800010 - ANIMATION": "VIS",
            "080008 - THEATRE": "PRF", "0800012 - SOUND": "PRD",
            "01_THEME": "CRE", "02_PLOT SYUHZET": "CRE", "03_CHARACTER": "CRE", "04_SETTING": "CRE",
            "05_SEQUENCE FABULA": "LIT", "06_NARRATOR": "LIT", "07_DIEGESIS": "LIT",
            "08_FUZZ INTERTEXT AND GENRE": "LIT", "00_THEORY OF COMPOSITION": "LIT", "09_PUBLICATION": "BIZ"}


def load_rules():
    src = io.open(os.path.join(META, "classify.py"), encoding="utf-8").read()
    block = src[src.index("RULES = ["): src.index("\n]\n", src.index("RULES = [")) + 3]
    junk = src[src.index("JUNK = re.compile("): src.index(", re.I)", src.index("JUNK = re.compile(")) + 7]
    ns = {"re": re}; exec(block + "\n" + junk, ns)
    return [(c, t, d, re.compile(p, re.I)) for c, t, d, p in ns["RULES"]], ns["JUNK"]


def main():
    rules, junk = load_rules()
    p = os.path.join(META, "inventory-live.json")
    items = json.load(io.open(p, encoding="utf-8"))
    counts = collections.Counter(); unmatched = []
    for it in items:
        if it.get("subject"):
            it["subject_src"] = "catalog"; counts["catalog"] += 1; continue
        tagged = next((TAG2SUBJ[t] for t in it["tags"] if t in TAG2SUBJ), None)
        if tagged:
            it["subject"] = tagged; it["subject_src"] = "tag"; counts["tag"] += 1; continue
        blob = " ".join([it["title"], " ".join(it["authors"]), it["publisher"], " ".join(it["tags"] + it["collections"])])
        if junk.search(it["title"].strip()) or not it["title"].strip():
            it["subject"] = None; it["subject_src"] = "junk"; counts["junk"] += 1; continue
        for code, trunk, desc, rx in rules:
            if rx.search(blob):
                it["subject"] = code; it["subject_src"] = "rule"; counts["rule"] += 1; break
        else:
            it["subject"] = None; it["subject_src"] = "none"; counts["none"] += 1; unmatched.append(it)
    io.open(p, "w", encoding="utf-8", newline="\n").write(json.dumps(items, ensure_ascii=False, indent=1))
    subj = collections.Counter(i["subject"] or "NONE" for i in items)
    story = [i for i in items if i["subject"] in ("CRE", "LIT")]
    story_unkeyed = [i for i in story if not i["spine"]]
    L = ["---", "id: BVX-LEARN.classify-live", "title: \"Classification of the live library\"", "type: report",
         f"generated: {datetime.date.today()}", "status: BOLO 18 stage 2 - step 2", "---", "",
         "# Classification of the live library", "",
         "Subject source per item: the Dec-2023 catalog where it had one, else Papi's own tags, else the approved 17-category rules.", "",
         "| Source | Items |", "|---|---|"] + [f"| {k} | {v} |" for k, v in counts.most_common()]
    L += ["", "## By subject (all 1,031)", "", "| Subject | Items |", "|---|---|"] + [f"| {k} | {v} |" for k, v in subj.most_common()]
    L += ["", f"## Story side: {len(story)} CRE + LIT · {len(story) - len(story_unkeyed)} spine-keyed from tags · **{len(story_unkeyed)} still need a spine key** (step 2b: classifier by title, then a PS pass on the TOC of each)", ""]
    L += [f"## Unmatched, needs eyes ({len(unmatched)})", "", "| Year | Title | Author | Tags |", "|---|---|---|---|"]
    L += [f"| {i['year']} | {i['title'][:70]} | {', '.join(i['authors'])[:30]} | {', '.join(i['tags'])[:40]} |" for i in unmatched]
    io.open(os.path.join(META, "CLASSIFY-LIVE.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    print("sources:", dict(counts)); print("subjects:", dict(subj.most_common()))
    print(f"story-side {len(story)} · spine-keyed {len(story) - len(story_unkeyed)} · unkeyed {len(story_unkeyed)} · unmatched {len(unmatched)}")


if __name__ == "__main__":
    main()
