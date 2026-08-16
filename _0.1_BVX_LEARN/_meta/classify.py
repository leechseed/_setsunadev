"""Taxonomy v3 — adds author rules, fixes leaks found by reading the unmatched pile."""
import json, re, os, collections

META = r"c:\Users\U01_LEECHSEED\Desktop\_setsunadev\_0.1_BVX_LEARN\_meta"
OUT = os.path.join(META, "TAXONOMY-PROPOSAL.md")
REV = os.path.join(META, "REVIEW-QUEUE.md")

inv = json.load(open(os.path.join(META, "inventory.json"), encoding="utf-8"))
orp = json.load(open(os.path.join(META, "orphans.json"), encoding="utf-8"))

items = []
for r in inv:
    if r.get("has_pdf"):
        items.append({"t": r["title"], "a": r["authors"], "p": r.get("publisher", ""),
                      "x": " ".join(r.get("tags", []) + r.get("collections", [])),
                      "src": "catalogued", "pages": r.get("pages", "")})
for r in orp:
    if r.get("exists") and not r.get("error") and r.get("text_layer"):
        items.append({"t": r.get("pdf_title") or r.get("fn_title") or "",
                      "a": r.get("pdf_author") or r.get("authors") or "",
                      "p": "", "x": "", "src": "orphan", "pages": r.get("pages", "")})

# Not books at all — forms, the user's own working files, empty fragments.
JUNK = re.compile(
    r"^\s*(untitled|standard|introduction:|praise for|all rights reserved|"
    r"this publication|list of artists|codenamecoom|ds11 |sd updates|"
    r"[a-z0-9_-]{1,12})\s*$|\.drawio|department of state|"
    r"^d-\d|^mawcsol|^kggd\d?$", re.I)

RULES = [
# --- authored-by rules run first: an author is a near-perfect signal ---
("LIT","BLACK","Literary theory & scholarship",
 r"harold bloom|\bbloom, hobby|\bbloom\b.*(literary|canon|influence|daemon|"
 r"how to read|american dream|sin and redemption|enslavement|troubles)|"
 r"todorov|mendlesohn|genette|barthes|bakhtin"),
("VIS","BLACK","Visual art, photography, cinematography",
 r"\bebert\b|scorsese by|herzog by"),
("CRE","BLACK","Creative craft — writing & story",
 r"truby|robert mckee|\bmckee\b|lajos egri|syd field|blake snyder|"
 r"anatomy of (story|genres|a best seller)|showrunner"),

# --- strong-signal domains ---
("GAM","BLACK","Game systems & design",
 r"pathfinder|shadowrun|battletech|dungeons?\s*&?\s*dragons|\bd&d\b|srd|\bogl\b|"
 r"paizo|catalyst game|modiphius|2d20|questworlds|cepheus|traveller|call of cthulhu|"
 r"savage worlds|gurps|warhammer|bestiary|rulebook|game ?master|roleplaying|"
 r"campaign setting|dramasystem|\brpg\b|adventure path|core index|masquerade|"
 r"fate accelerated|mothership|ultraviolet grasslands|world engine|alice is missing|"
 r"crpg|game design|tabletop game|board ?game|level design|game mechanic|kobold|"
 r"kggd|systems? reference document|microlite|random tables|fallout \d|"
 r"tom clancy'?s|core rules"),
("PRD","BLACK","Production tooling & pipeline",
 r"blender|unreal engine|unity|clip studio|photoshop|after effects|davinci|premiere|"
 r"matchmoving|compositing|\bvfx\b|stable diffusion|rentry|novelai|\bnai quick|"
 r"embeddings|midjourney|substance painter|zbrush|maya|houdini|render|3d model|"
 r"motion graphic|rotoscop|ableton|sd resource|sd v1"),
("TEC","BLACK","Programming, CS, engineering",
 r"\b[a-z]{3}\d{4}\b|programming|how to program|\bc\+\+|python|javascript|typescript|"
 r"full-?stack|database|data mining|data storage|data recovery|algorithm|automata|"
 r"computability|wordpress|linux|\btmux\b|\bbash\b|\bgit\b|notes for professionals|"
 r"deep learning|machine learning|neural net|software|web dev|data structure|"
 r"operating system|precalculus|calculus|discrete math|linear algebra|engineering|"
 r"cryptograph|information security|computer organization|crash course|chatgpt|"
 r"peer-to-peer|profiler|toolkit"),
("LIT","BLACK","Literary theory & scholarship",
 r"routledge (companion|handbook|dictionary)|oxford (companion|dictionary)|"
 r"cambridge companion|narratolog|semiotic|literary theor|literary term|"
 r"literary criticism|criticism and theory|poetics|introduction to literature|"
 r"norton introduction|dictionary of literary|structural approach|allegory|"
 r"rhetorics of|film genre reader|genre and hollywood|hermeneutic|formalis|"
 r"structuralis|the fantastic|epic hero|noir thriller|hero with a thousand faces|"
 r"monomyth|^metaphor$|companion to literature|imaginary worlds|cyberpunk culture|"
 r"literature and|media fandom|big history|literature|literary|western canon|"
 r"serial drama|serial returns|ib english"),
("PRF","BLACK","Theatre, acting, performance",
 r"musical theatre|musical theater|actor prepares|stanislavsk|theatre of the oppressed|"
 r"playing shakespeare|angels in america|three uses of the knife|acting|stagecraft|"
 r"broadway|monologue|improvisation|dramaturg|playwriting|for the theatre|"
 r"sondheim|lloyd-webber|popular modern songs"),
("VIS","BLACK","Visual art, photography, cinematography",
 r"photograph|aktfotografie|akt-shooting|drawing|figure draw|anatomy for|"
 r"form of the head|composition|lighting|portrait|illustration|colou?r theory|"
 r"colored pencil|watercolor|painter|cinematograph|storyboard|concept art|"
 r"grammar of the (shot|edit)|film theory|cinema|american film|screenplay|"
 r"directing|montage|picasso|visual story|art direction|after the camera|"
 r"screen production"),
("CRE","BLACK","Creative craft — writing & story",
 r"writing|writer|screenwrit|novel|fiction|storytell|story structure|plot|"
 r"dialogue|narrative|prose|manuscript|character|scene and sequel|thesaurus|"
 r"worldbuild|into the woods|great stories|description and setting|"
 r"side characters|role and cast|sentences and paragraphs|rhetoric"),
("DSN","BLACK","Design theory & systems",
 r"universal principles of design|design methods|design system|design language|"
 r"\bui design|\bux\b|user experience|interaction design|typograph|graphic design|"
 r"information design|design thinking|innovation"),
("SOC","ORANGE","Social media, platforms, culture",
 r"tiktok|instagram|youtube|twitter|social media|influencer|creator econom|"
 r"platform stud|virality|algorithm feed|uses and gratifications|fandom|"
 r"parasocial|content creat|streaming"),
("MSX","ORANGE","Sex, relationships, erotic",
 r"\bsex|erotic|kink|bdsm|fetish|porn|seduction|dating|intimacy|tantra|orgasm|"
 r"bottoming|topping|polyamor|\bnude|nudism|courtesan|juliette society|janus chamber|"
 r"gay tourism|fkk|sauna club|fuckology|penis|anal|\bgay\b|queer|prostitut|"
 r"sprinkle|ace and aro|asexual"),
("FIT","ORANGE","Fitness, physique, sport",
 r"glute|booty|workout|training manual|boxing|skateboard|rowing|yoga|"
 r"strength|physique|bodybuild|hypertroph|calisthenic|martial art|eskrima|"
 r"powerlifting|nutrition|fitness"),
("PSY","BLACK","Psychology & typology",
 r"\b(intj|intp|entj|entp|infj|infp|enfj|enfp|istj|isfj|estj|esfj|istp|isfp|estp|esfp)\b|"
 r"enneagram|myers-?briggs|\bmbti\b|personality type|big five|psycholog|therap|trauma|"
 r"attachment|cognitive|neuro|emotion|\badhd\b|anxiety|shame|addiction|behaviou?r|"
 r"intelligence test"),
("SLF","BOTH","Learning, self-development",
 r"deep work|polymath|skill acquisition|self-discipline|habit|productivity|"
 r"learn anything|memory|mastery|focus|lessons of the masters|genius|"
 r"how to teach yourself|limitless|change the way you think|do-it-yourself|organizing"),
("PHI","BLACK","Philosophy, esoteric, religion",
 r"philosoph|spiritual|esoteric|occult|mystic|sacred|ritual|metaphys|theolog|"
 r"magick|alchem|\bmyth|tarot|angel|demon|book of enoch|christolog|gnostic|"
 r"kabbal|gods and goddesses"),
("MIL","BLACK","Military doctrine, tactics, firearms",
 r"\bmcwp\b|\bmcrp\b|\bfm \d|\batp \d|\btc \d-|\bufc \d|field manual|ranger handbook|"
 r"wargaming|military|infantry|small arms|combat shooting|army publishing|"
 r"joint publication|tactics|marksman"),
("POL","BLACK","Politics, power, radicalization",
 r"politic|radical|extrem|propaganda|ideolog|fascis|terror|insurgen|revolution|"
 r"sociolog|surveillance|doublespeak|civil disobedience|anti-caste|activism|"
 r"turner diaries|emancipation|enslavement"),
("BIZ","BOTH","Business, finance, property",
 r"business|marketing|entrepreneur|startup|finance|invest|real estate|appraisal|"
 r"valuation|negotiat|sales|brand|management|landlord|profit|homestead|"
 r"poultry|farm|agricultur|permaculture|self-build|custom home|home buying"),
]
COMPILED = [(c, t, d, re.compile(p, re.I)) for c, t, d, p in RULES]
META_ = {}
for c, t, d, _ in COMPILED:
    META_.setdefault(c, (t, d))

buckets = collections.defaultdict(list)
unmatched, junk = [], []
for it in items:
    blob = " ".join([it["t"], it["a"], it["p"], it["x"]])
    if JUNK.search(it["t"].strip()) or not it["t"].strip():
        junk.append(it); continue
    for code, trunk, desc, rx in COMPILED:
        if rx.search(blob):
            buckets[code].append(it); break
    else:
        unmatched.append(it)

TO = {"BLACK": 0, "BOTH": 1, "ORANGE": 2}
rows = sorted(buckets.items(), key=lambda kv: (TO[META_[kv[0]][0]], -len(kv[1])))
classified = sum(len(v) for v in buckets.values())

with open(OUT, "w", encoding="utf-8") as f:
    f.write(f"""---
id: BVX-LEARN.taxonomy-proposal
title: "Taxonomy — 17 categories, approved 2026-08-15"
type: proposal
status: approved
created: 2026-08-15
---

# Taxonomy — final

Derived from **{len(items):,}** usable items. `SLF` kept; `SOC` assigned to ORANGE.

| Classified | Review queue | Non-books | Coverage |
|---|---|---|---|
| **{classified:,}** | {len(unmatched)} | {len(junk)} | **{100*classified//(len(items)-len(junk))}%** |

## Categories

| Code | Trunk | Domain | Count |
|---|---|---|---|
""")
    for code, lst in rows:
        trunk, desc = META_[code]
        f.write(f"| `{code}` | {trunk} | {desc} | **{len(lst)}** |\n")
    for code, lst in rows:
        trunk, desc = META_[code]
        f.write(f"\n## `{code}` — {desc} · {trunk} · {len(lst)}\n\n"
                "| Pages | Title | Author |\n|---|---|---|\n")
        for i in lst[:40]:
            f.write(f"| {i['pages'] or '?'} | {i['t'][:66].replace('|','/')} | "
                    f"{str(i['a'])[:24].replace('|','/')} |\n")
        if len(lst) > 40:
            f.write(f"\n_+{len(lst)-40} more_\n")

with open(REV, "w", encoding="utf-8") as f:
    f.write(f"""---
id: BVX-LEARN.review-queue
title: "Review queue — needs a human call"
type: review
status: open
created: 2026-08-15
---

# Review queue — {len(unmatched)} items

Rules and author-matching could not place these. They need your call
(or mine, by opening the file).

| Title | Author | Pages |
|---|---|---|
""")
    for i in unmatched:
        f.write(f"| {i['t'][:70].replace('|','/')} | {str(i['a'])[:26].replace('|','/')} "
                f"| {i['pages'] or '?'} |\n")
    f.write(f"\n---\n\n## Not books ({len(junk)})\n\n"
            "Forms, working files, empty fragments. Excluded from the catalog.\n\n")
    for i in junk[:60]:
        f.write(f"- {i['t'][:70] or '(blank)'}\n")

print(f"items       : {len(items):,}")
print(f"classified  : {classified:,}")
print(f"review queue: {len(unmatched)}")
print(f"non-books   : {len(junk)}")
print(f"coverage    : {100*classified//(len(items)-len(junk))}%")
print()
for code, lst in rows:
    trunk, desc = META_[code]
    print(f"  {code:5s} {trunk:7s} {len(lst):5d}  {desc}")
