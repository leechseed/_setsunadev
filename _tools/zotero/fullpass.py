# -*- coding: utf-8 -*-
"""BOLO 18 stage 2: THE FULL PASS over all 1,031 items, every spine key at once (ruled 9/16, "run the full pass").
Keys: L0 · L4 · L5 · L6 · L7 · SETTING · TEXTURE · CRAFT-PROCESS · OFF (not a story book).

  python _tools/zotero/fullpass.py key      step 2: tags (never overwritten) > title/tag rules > subject default; writes inventory-live.json
  python _tools/zotero/fullpass.py batch    step 3 prep: bundle every still-unkeyed item (first pages of its PDF) into PS batches of 50
  python _tools/zotero/fullpass.py merge    step 4: merge every spinekeys-batch*.json a PS wrote back (keys + repaired titles), rebuild shelves
  python _tools/zotero/fullpass.py shelves  rebuild SPINE-KEYS.md over the whole library
"""
import io, os, re, sys, json, glob, subprocess, collections, datetime
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
META = os.path.join(ROOT, "_0.1_BVX_LEARN", "_meta"); INV = os.path.join(META, "inventory-live.json")
BATCH_DIR = os.environ.get("FULLPASS_BATCH_DIR") or os.path.join(os.environ.get("TEMP", "."), "fullpass")
VALID = {"L0", "L4", "L5", "L6", "L7", "SETTING", "TEXTURE", "CRAFT-PROCESS", "OFF"}
JUNK = re.compile(r"e23 sourcebook|all rights reserved|^introduction|praise for|crescent books|^untitled|^chapter|^contents|^copyright|library of congress|^isbn|^table of|^part (one|1)\b|^preface|^foreword|^acknowledg|^the author|^about the|^[a-z0-9_ -]{1,14}$", re.I)
# subjects that are off the story spine unless a title rule says otherwise
OFF_SUBJECTS = {"TEC", "BIZ", "FIT", "SOC", "PRD", "MIL", "MSX", "PHI", "POL", "DSN", "SLF", "PSY"}
# title/tag rules, all subjects (an item may take several keys)
RULES = [
 ("SETTING", r"world-?building|worldbuild|setting|fictional worlds|sourcebook|campaign setting|gazetteer|atlas of|kingdoms?|empire|realm|planet|city of|cities|places?\b|landscape|geography|environment|milieu|lore|biome|ecology|civilization|cultures?\b|societ|architecture|dungeon fantasy|transhuman space|forgotten realms|eberron|ravenloft|greyhawk|golarion|shadowrun|traveller|space opera"),
 ("L5", r"character|protagonist|hero\b|villain|antagonist|archetype|persona\b|motivation|psychology of|npc|non-player"),
 ("L4", r"\bplot|structure|beat sheet|save the cat|story grid|steps to|outline|scene|sequence|\bacts?\b|three-act|pacing|suspense|conflict|screenplay|screenwriting|scriptwriting|story engineering|story physics|anatomy of story|quest|adventure design|encounter design|narrative design|storytelling|story design|interactive story|branching"),
 ("L7", r"genre|science fiction|fantasy\b|horror|romance|thriller|mystery|crime\b|noir|comedy|serial drama|television|\bfilm\b|cinema|video game writing|game writing|transmedia|multiplatform|audience|reader|publishing|market|comics|manga|anime|animation|musical|theatre|theater|stage|radio|podcast"),
 ("TEXTURE", r"narrat|point of view|viewpoint|voice|focaliz|diegesis|dialogue|description|prose|style\b|sentence|show.*tell|exposition|tense|cinematography|shot|editing|montage|visual story|storyboard"),
 ("L6", r"theme|meaning|moral|premise|allegory|ideology|ethic|values?\b|philosophy of story"),
 ("L0", r"narratolog|theory of|poetics|semiotic|structuralis|formalis|rhetoric|what is (a )?story|storytelling animal|why fiction|affective|cognitive|mytholog|monomyth|hero with a thousand|dramatica|story and discourse|fabula|sjuzhet"),
 ("CRAFT-PROCESS", r"writer'?s life|writing life|productivity|habit|block\b|mental game|fearless writing|just write|how to write (a|your)|self-?publish|freelance|career|blueprint|blunders|smart notes|deep work"),
]
COMPILED = [(k, re.compile(rx, re.I)) for k, rx in RULES]


def load(): return json.load(io.open(INV, encoding="utf-8"))
def save(items): io.open(INV, "w", encoding="utf-8", newline="\n").write(json.dumps(items, ensure_ascii=False, indent=1))


# manual keys (9/16, the drop intake): by BVX id, never overwritten, like a tag
MANUAL = {"BVX.1123": ["L5", "L6", "L0"], "BVX.1124": ["L4", "L5"], "BVX.1125": ["L4", "L7"], "BVX.1126": ["L0", "L4", "L6", "L7"], "BVX.1127": ["L5"]}

def key():
    items = load(); c = collections.Counter()
    for it in items:
        if it.get("bvx") in MANUAL:
            it["spine"] = MANUAL[it["bvx"]]; it["spine_src"] = "manual"; c["manual"] += 1; continue
        if it.get("src") == "drop" and not it.get("bvx"):
            it["spine"] = []; it["spine_src"] = "drop-unkeyed"; c["drop-unkeyed (held)"] += 1; continue  # the bulk is held until an intake pass is ordered; title rules over-key RPG sheets
        src = it.get("spine_src")
        if src in ("tag", "toc", "toc-off", "manual") and (it.get("spine") or src == "toc-off"):
            c[src] += 1; continue
        blob = " ".join([it["title"], " ".join(it["tags"]), " ".join(it["collections"])])
        junk = bool(JUNK.search(it["title"].strip()) or len(it["title"].strip()) < 6)
        hits = [k for k, rx in COMPILED if rx.search(blob)]
        subj = it.get("subject") or "NONE"
        if hits and not junk:
            it["spine"] = hits[:3]; it["spine_src"] = "rule"; c["rule"] += 1
        elif subj in OFF_SUBJECTS and not junk:
            it["spine"] = []; it["spine_src"] = "subject-off"; c["subject-off"] += 1
        elif it.get("src") == "drop":
            it["spine"] = []; it["spine_src"] = "drop-unkeyed"; c["drop-unkeyed (held)"] += 1
        else:
            it["spine"] = []; it["spine_src"] = "none"; c["none (to PS)"] += 1
        it["junk_title"] = junk
    save(items); print("key:", dict(c))


def batch(size=50):
    items = load(); os.makedirs(BATCH_DIR, exist_ok=True)
    for f in glob.glob(os.path.join(BATCH_DIR, "batch*.md")): os.remove(f)
    todo = [i for i in items if i.get("spine_src") == "none"]
    todo.sort(key=lambda i: ((i.get("subject") or "NONE"), i["title"].lower()))
    tmp = os.path.join(BATCH_DIR, "t.txt"); n = 0
    for b in range(0, len(todo), size):
        n += 1; L = [f"# Full-pass batch {n:02d} · {len(todo[b:b+size])} items · first pages of each PDF · 2026-09-16", ""]
        for i in todo[b:b+size]:
            head = f"## zid {i['zid']} · {i['bvx'] or 'NEW'} · {i['title'][:90]} · {', '.join(i['authors'])[:40]} ({i['year']}) · subject {i.get('subject') or 'NONE'}" + (" · TITLE IS BOILERPLATE, read the real title off the page" if i.get("junk_title") else "")
            if not i["pdf_exists"]:
                L += [head + " · NO PDF", ""]; continue
            subprocess.run(["pdftotext", "-f", "1", "-l", "7", "-layout", i["pdf"], tmp], capture_output=True)
            body = io.open(tmp, encoding="utf-8", errors="replace").read() if os.path.exists(tmp) else ""
            body = re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n", body))[:3000]
            L += [head, "", "```", body, "```", ""]
        io.open(os.path.join(BATCH_DIR, f"batch{n:02d}.md"), "w", encoding="utf-8").write("\n".join(L))
    print(f"batch: {len(todo)} items -> {n} batch files in {BATCH_DIR}")


def merge():
    items = load(); by = {i["zid"]: i for i in items}
    applied = collections.Counter(); files = sorted(glob.glob(os.path.join(META, "spinekeys-batch*.json")))
    for f in files:
        for k in json.load(io.open(f, encoding="utf-8")):
            it = by.get(k.get("zid"))
            if not it: applied["no zid"] += 1; continue
            spine = [s for s in k.get("spine", []) if s in VALID]
            if not spine: applied["unusable"] += 1; continue
            if it.get("spine_src") in ("tag", "toc", "manual"): applied["kept (tag/toc/manual)"] += 1; continue
            if spine == ["OFF"]: it["spine"] = []; it["spine_src"] = "toc-off"; applied["off"] += 1
            else: it["spine"] = spine; it["spine_src"] = "toc"; applied["keyed"] += 1
            it["spine_why"] = k.get("why", "")
            if k.get("title") and it.get("junk_title") and len(k["title"]) > 5:
                it["title_zotero"] = it["title"]; it["title"] = k["title"]; applied["title repaired"] += 1
    save(items); print(f"merge: {len(files)} file(s) ·", dict(applied)); shelves()


def shelves():
    items = load(); c = collections.Counter(i.get("spine_src") or "?" for i in items)
    keyed = [i for i in items if i.get("spine")]
    lvc = collections.Counter(l for i in keyed for l in i["spine"])
    L = ["---", "id: BVX-LEARN.spine-keys", "title: \"Spine keys over the whole library (BOLO 18 stage 2, the full pass)\"", "type: report",
         f"generated: {datetime.date.today()}", "status: BOLO 18 stage 2 - the full pass", "---", "",
         "# Spine keys over the whole library", "",
         f"All {len(items)} items. Authority: Chief's tags · a PS TOC pass · title rules · subject default (off-spine). `OFF` = not a story book.", "",
         "| Source | Items |", "|---|---|"] + [f"| {k} | {v} |" for k, v in c.most_common()]
    L += ["", "## Items per shelf", "", "| Shelf | Items |", "|---|---|"] + [f"| {k} | {v} |" for k, v in lvc.most_common()]
    L += ["", "## The shelves", ""]
    for lvl in ["L0", "L4", "L5", "L6", "L7", "SETTING", "TEXTURE", "CRAFT-PROCESS"]:
        rows = sorted((i for i in keyed if lvl in i["spine"]), key=lambda i: (i["spine_src"] != "tag", (i.get("subject") or "ZZ"), i["title"].lower()))
        L += [f"### {lvl} ({len(rows)})", "", "| BVX | Subject | Title | Author | Year | Key from | Distill |", "|---|---|---|---|---|---|---|"]
        L += [f"| {i['bvx'] or 'NEW'} | {i.get('subject') or ''} | {i['title'][:72]} | {', '.join(i['authors'])[:26]} | {i['year']} | {i['spine_src']} | {'✅' if i.get('bvx') and os.path.exists(os.path.join(ROOT, '_0.1_BVX_LEARN', 'KNOWLEDGE_AREAS', i['bvx'] + '.md')) else ''} |" for i in rows] + [""]
    off = [i for i in items if not i.get("spine")]
    L += [f"## Off the spine ({len(off)}): not story books, or still unkeyed", "", "| Source | Items |", "|---|---|"] + [f"| {k} | {v} |" for k, v in collections.Counter(i.get('spine_src') for i in off).most_common()]
    io.open(os.path.join(META, "SPINE-KEYS.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    print("shelves:", dict(lvc.most_common()), "| sources:", dict(c))


if __name__ == "__main__":
    {"key": key, "batch": batch, "merge": merge, "shelves": shelves}[sys.argv[1]]()
