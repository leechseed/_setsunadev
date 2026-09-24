# -*- coding: utf-8 -*-
"""The plot sweep (BOLO 77) — every source that could build the plot system: fabula · trope graph · syuzhet · rails.
Zero tokens. Two modes:
  python _tools/zotero/plot_sweep.py batch <outdir>   pool the candidates from Zotero + the drop folder + the z-lib gap, write PS batches
  python _tools/zotero/plot_sweep.py merge <outdir>   fan-in the PS verdicts (<outdir>/verdict*.json) -> _meta/PLOT-SWEEP.md + plot_sweep.json
The drop folder's RPG adventures are counted by family as the specimen corpus, never sent to a PS one by one."""
import io, json, os, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
META = os.path.join(ROOT, "_0.1_BVX_LEARN", "_meta")
BATCH = 140

KW = re.compile(r"plot|stor(y|ies)|narrat|screen|script|fiction|novel|writ(e|ing|er)|drama|dramatic|myth|folk|fairy|tale\b|trope|genre|structure|scene|sequence|tragedy|comedy|comic|hero|quest|archetyp|poetic|film|cinema|movie|television|\btv\b|series|episod|showrunner|game ?design|games? master|gamemaster|dungeon master|campaign|adventure|chronolog|timeline|time and|temporal|causal|suspense|mystery|thriller|twist|conflict|plotting|outlin|beat|act\b|three[- ]act|five[- ]act|premise|rhetoric|discourse|semiotic|formalis|structuralis|reader|audience|emotion.*stor|interactive|branching|hypertext|quest|lore|saga|epic|romance|crime|detective|horror|fantasy|science fiction|sci-fi|worldbuild|history of the|prophecy|fate\b|trickster|shadow|journey|cliffhanger|serial|soap|telenovela|anime|manga|comics?\b|graphic novel|improv|role-?play|rpg|larp|storyboard|montage|editing|showrunn|writers'? room", re.I)
OFF = re.compile(r"c\+\+|java\b|algorithm|data structure|real estate|landlord|property invest|mortgage|accounting|tax\b|anatomy of the human|nutrition|diet|workout|forensic|kubernetes|python|sql\b|excel\b|poultry|permaculture|agricultur", re.I)
SPINE_ON = {"L0", "L4", "L6", "L7", "TEXTURE", "CRAFT-PROCESS"}
STORY_SUBJ = {"CRE", "LIT", "GAM", "PRF", "VIS"}
# RPG families in the drop folder: specimens, counted not judged
FAM = [("Pathfinder Society scenario", r"^Scenario \d|^S\d\d-\d\d|^PFS"), ("PF2 Quest", r"^PF2 Quest"),
       ("Adventure path chapter", r" AP\b| - \d\d - |Adventure Path|Kingmaker|Curse of the Crimson Throne|Serpent's Skull|Strength of Thousands|Rise of the Runelords|Skull & Shackles|Jade Regent|Carrion Crown|Council of Thieves|Legacy of Fire|Second Darkness|Wrath of the Righteous|Reign of Winter|Mummy's Mask|Iron Gods|Giantslayer|Hell's Rebels|Hell's Vengeance|Abomination Vaults|Agents of Edgewatch|Age of Ashes|Extinction Curse|Quest for the Frozen Flame|Outlaws of Alkenstar|Blood Lords|Sky King|Gatewalkers|Stolen Fate|Season of Ghosts"),
       ("Shadowrun", r"^SR\d|Shadowrun"), ("GURPS", r"GURPS|Pyramid"), ("D&D module", r"D&D|Dungeons|^DDAL|^CCC-"),
       ("other module", r"Module|Modules|Adventure|Delve|Quests of|Rappan|Lair")]
# the canon the plot system should rest on: checked against everything held; unheld = the upload list
CANON = [
 ("Propp", "Morphology of the Folktale", "propp|morphology of the folk"), ("Genette", "Narrative Discourse", r"narrative discourse(?!.*revisit)|genette.*discours"),
 ("Genette", "Narrative Discourse Revisited", "discourse revisited"), ("Chatman", "Story and Discourse", "story and discourse"),
 ("Herman", "Story Logic", "story logic"), ("Rimmon-Kenan", "Narrative Fiction: Contemporary Poetics", "rimmon|narrative fiction: contemp"),
 ("Ryan", "Narrative as Virtual Reality", "narrative as virtual reality"), ("Ryan", "Possible Worlds, Artificial Intelligence, and Narrative Theory", "possible worlds.*narrative"),
 ("Abbott", "The Cambridge Introduction to Narrative", "cambridge introduction to narrative"), ("Brooks, P.", "Reading for the Plot", "reading for the plot"),
 ("Sternberg", "Expositional Modes and Temporal Ordering in Fiction", "expositional modes"), ("Booth", "The Rhetoric of Fiction", "rhetoric of fiction"),
 ("Bakhtin", "The Dialogic Imagination", "dialogic imagination"), ("Bakhtin", "Forms of Time and of the Chronotope", "chronotope"),
 ("Polti", "The Thirty-Six Dramatic Situations", "thirty-six dramatic|36 dramatic"), ("Booker", "The Seven Basic Plots", "seven basic plots"),
 ("Campbell", "The Hero with a Thousand Faces", "thousand faces"), ("Field", "Screenplay: The Foundations of Screenwriting", r"^screenplay|foundations of screenwriting"),
 ("Todorov", "The Poetics of Prose", "poetics of prose"), ("Barthes", "Introduction to the Structural Analysis of Narratives", "structural analysis of narrative"),
 ("Greimas", "Structural Semantics", "structural semantics"), ("Ricoeur", "Time and Narrative", "time and narrative"),
 ("Kermode", "The Sense of an Ending", "sense of an ending"), ("Forster", "Aspects of the Novel", "aspects of the novel"),
 ("Frye", "Anatomy of Criticism", "anatomy of criticism"), ("Lévi-Strauss", "Structural Anthropology", "structural anthropology"),
 ("Bordwell", "Narration in the Fiction Film", "narration in the fiction film"), ("Thompson, K.", "Storytelling in the New Hollywood", "storytelling in the new hollywood"),
 ("Mittell", "Complex TV", "complex tv"), ("Tobias", "20 Master Plots", "20 master plots"), ("Schmidt", "The Story Structure Architect", "story structure architect"),
 ("Yorke", "Into the Woods", "into the woods"), ("Snyder", "Save the Cat!", "save the cat"), ("Truby", "The Anatomy of Story", "anatomy of story"),
 ("McKee", "Story", r"^story: substance|substance, structure"), ("Weiland", "Creating Character Arcs", "creating character arcs"),
 ("Dibell", "Plot", r"^plot( \(|\s+dibell|$)|plot \(elements"), ("Lyons", "Rapid Story Development", "rapid story development"),
 ("Ingermanson", "The Snowflake Method", "snowflake"), ("Mateas & Sengers", "Narrative Intelligence", "narrative intelligence.*(mateas|sengers)|mateas"),
 ("Riedl & Young", "Narrative Planning", "narrative planning"), ("Howard", "Quests", r"^quests"), ("Robbins", "Microscope", "microscope"),
]

def load(p):
    return json.load(io.open(p, encoding="utf-8"))

def pool():
    inv = load(os.path.join(META, "inventory-live.json"))
    gap = load(os.path.join(META, "zlib_gap.json"))["gap"]
    cands, spec = [], collections.Counter()
    for n, i in enumerate(inv):
        t = i.get("title") or ""; a = ", ".join(i.get("authors") or [])[:40]
        src = i.get("src", "zotero")
        if OFF.search(t):
            continue
        if src == "drop":
            fam = next((f for f, rx in FAM if re.search(rx, t)), None)
            if fam and not re.search(r"guide|design|writing|theory|toolbox|gamemastery|game ?master", t, re.I):
                spec[fam] += 1; continue
            if not KW.search(t):
                continue
        else:
            tags = [x for x in (i.get("tags") or []) if re.match(r"0\d", x)]
            story = (set(i.get("spine") or []) & SPINE_ON) or i.get("subject") in STORY_SUBJ or tags or KW.search(t)
            if not story:
                continue
        cands.append({"id": f"{'Z' if src != 'drop' else 'D'}{n}", "src": "zotero" if src != "drop" else "drop",
                      "bvx": i.get("bvx") or "", "title": t[:150], "author": a, "year": i.get("year") or "",
                      "spine": " ".join(i.get("spine") or []), "tags": " ".join(x for x in (i.get("tags") or []) if re.match(r"0\d", x))[:60]})
    for n, g in enumerate(gap):
        t = g.get("title") or ""
        if OFF.search(t) or not KW.search(t):
            continue
        cands.append({"id": f"G{n}", "src": "zlib-gap", "bvx": "", "title": t[:150], "author": (g.get("author") or "")[:40], "year": "", "spine": "", "tags": ""})
    return inv, gap, cands, spec

def batch(out):
    os.makedirs(out, exist_ok=True)
    inv, gap, cands, spec = pool()
    bysrc = collections.Counter(c["src"] for c in cands)
    for k in range(0, len(cands), BATCH):
        rows = cands[k:k + BATCH]
        p = os.path.join(out, f"batch{k // BATCH + 1:02d}.md")
        with io.open(p, "w", encoding="utf-8") as f:
            f.write("id | src | bvx | title | author | year | spine | Chief's tags\n")
            for c in rows:
                f.write(" | ".join(str(c[x]) for x in ("id", "src", "bvx", "title", "author", "year", "spine", "tags")) + "\n")
    json.dump({"cands": cands, "specimens": spec}, io.open(os.path.join(out, "pool.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print(f"pool {len(cands)} candidates · {dict(bysrc)} · batches {-(-len(cands) // BATCH)} of {BATCH}")
    print("specimens (drop, counted):", dict(spec))

LANES = ["FABULA", "RAILS", "SCENE", "TROPES", "SERIES", "GAME-RAILS", "THEORY", "COUNTER", "AI-PLANNING"]

def merge(out):
    P = load(os.path.join(out, "pool.json")); by = {c["id"]: c for c in P["cands"]}
    keep, seen, bad = [], set(), []
    for fn in sorted(os.listdir(out)):
        if not (fn.startswith("verdict") and fn.endswith(".json")):
            continue
        for v in load(os.path.join(out, fn)):
            c = by.get(v.get("id"))
            if not c:
                bad.append(v.get("id")); continue
            seen.add(c["id"])
            if v.get("works"):
                keep.append({**c, "lane": v.get("lane", "?"), "tier": v.get("tier", 3), "why": v.get("why", ""), "clean": v.get("clean_title") or c["title"]})
    # book-summary spam and fake scans found by opening the PDF (never a source): drop them from the keepers
    JUNK = re.compile(r"SYD.?Screenplay.?PDF|Booth.The.Rhetoric.Of.Fiction", re.I)
    keep = [k for k in keep if not (k["src"] == "drop" and JUNK.search(k["title"]))]
    missing = [i for i in by if i not in seen]
    # dedupe on normalized title, prefer held (zotero > drop > gap)
    norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())[:40]
    rank = {"zotero": 0, "drop": 1, "zlib-gap": 2}
    best = {}
    for k in sorted(keep, key=lambda x: rank[x["src"]]):
        best.setdefault(norm(k["clean"]), k)
    keep = list(best.values())
    heldtxt = " || ".join((c["title"] + " " + c["author"]).lower() for c in P["cands"] if c["src"] != "zlib-gap")
    inv = load(os.path.join(META, "inventory-live.json"))
    FAKE = re.compile(r"rhetoric of fiction", re.I)  # the drop's Booth is a 34-page spam summary (DROP-INTAKE 9/16)
    heldall = [((i.get("title") or "") + " " + " ".join(i.get("authors") or [])) for i in inv
               if not (i.get("src") == "drop" and FAKE.search(i.get("title") or ""))]
    cat = load(os.path.join(META, "catalog.json")); cat = cat if isinstance(cat, list) else list(cat.values())
    heldall += [str(r.get("t") or "") + " " + str(r.get("a") or "") for r in cat if isinstance(r, dict)]
    gaptxt = [c["title"] for c in P["cands"] if c["src"] == "zlib-gap"]
    canon = []
    for au, ti, rx in CANON:
        hit = [t for t in heldall if re.search(rx, t, re.I)]
        h = bool(hit)
        g = (not h) and any(re.search(rx, t, re.I) for t in gaptxt)
        canon.append({"author": au, "title": ti, "held": h, "in_zlib_favs": g, "match": hit[0][:70] if hit else ""})
    json.dump({"keep": keep, "canon": canon, "specimens": P["specimens"], "missing": missing}, io.open(os.path.join(META, "plot_sweep.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    L = [f"---\nid: BVX-LEARN.plot-sweep\ntitle: \"The plot sweep: every source that builds the plot system\"\ntype: report\ngenerated: 2026-09-23\nstatus: BOLO 77 · Chief: \"pull more plotting sources from the zotero, run a full sweep, get me every book that works\"\n---\n",
         "# The plot sweep · 2026-09-23\n",
         f"Pool {len(P['cands'])} titles (Zotero · the drop folder · the z-lib favourites gap), judged by title in PS batches. **{len(keep)} work.** Held = a PDF is on the box; GAP = in the z-lib favourites only, upload wanted.\n"]
    for lane in LANES + ["?"]:
        rows = sorted([k for k in keep if k["lane"] == lane], key=lambda k: (k["tier"], k["src"] == "zlib-gap", k["clean"]))
        if not rows:
            continue
        L.append(f"\n## {lane} ({len(rows)})\n\n| Tier | Where | ID | Title | Author | Why |\n|---|---|---|---|---|---|")
        for k in rows:
            where = {"zotero": "held", "drop": "held (drop)", "zlib-gap": "**GAP**"}[k["src"]]
            L.append(f"| {k['tier']} | {where} | {k['bvx'] or '—'} | {k['clean']} | {k['author']} | {k['why']} |")
    L.append("\n## The canon check (named sources the plot system rests on)\n\n| Author | Title | State |\n|---|---|---|")
    for c in canon:
        L.append(f"| {c['author']} | {c['title']} | {('held · ' + c['match']) if c['held'] else ('**GAP** · in your z-lib favourites' if c['in_zlib_favs'] else '**GAP** · not found anywhere')} |")
    L.append("\n## The specimen corpus (drop folder, counted by family)\n\n| Family | PDFs |\n|---|---|")
    for f, n in sorted(P["specimens"].items(), key=lambda x: -x[1]):
        L.append(f"| {f} | {n} |")
    io.open(os.path.join(META, "PLOT-SWEEP.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    cnt = collections.Counter(k["lane"] for k in keep); src = collections.Counter(k["src"] for k in keep)
    print(f"RANGE · verdicts for {len(seen)}/{len(by)} candidates · missing {len(missing)} · unknown ids {len(bad)}")
    print(f"works {len(keep)} (deduped) · by lane {dict(cnt)} · by source {dict(src)}")
    print(f"canon held {sum(c['held'] for c in canon)}/{len(canon)} · in z-lib favs {sum(c['in_zlib_favs'] for c in canon)} · not found {sum(not c['held'] and not c['in_zlib_favs'] for c in canon)}")
    print("wrote _meta/PLOT-SWEEP.md + _meta/plot_sweep.json")

if __name__ == "__main__":
    {"batch": batch, "merge": merge}[sys.argv[1]](sys.argv[2])
