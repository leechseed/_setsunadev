"""BOLO 89 · the trope system glass (Chief 10/31: "i want to be able to browse the system itself").

Builds one browsable page over the trope register (zero tokens):
  _tools/tropes/glass/tropes.html     served by the Console at /local/tropes (the pane "Tropes", behind "more")

Reads  _tools/tropes/data/domains/register.json   8,700 tropes: name · def · domains · keys · conf · links
       _tools/tropes/data/trope_graph.json        the plot graph (which register tropes it uses, and on which node)
The layer names and one-line meanings below come from the SSOT system docs each code keys to:
  character + sexuality  ssot_02_character_systems_vertical_slice (L1-L12)
  setting                ssot_03_setting_system (S1-S12)
  genre                  ssot_01_genre_system (G1-G12)
  theme                  ssot_06_theme_system (rails R1-R4)
  texture                ssot_01_texture_system (T1-T12)
  tracking               ssot_08_tracking_system (the parts)
  style                  ssot_07_1_prose_style · ssot_07_3_pages_style
The data is embedded, trimmed: link targets outside the register are dropped. Over ~8 MB it would go to a
sibling JSON; at ~3 MB it stays inside the page, so the Console's /local/ whitelist serves one file.

CLI:  python -X utf8 _tools/tropes/build_glass.py            build the page, print one line
      python -X utf8 _tools/tropes/build_glass.py --json     build the page, print the summary as JSON
      python -X utf8 _tools/tropes/build_glass.py --dry-run  build nothing, print what it would write
"""
import datetime, io, json, os, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
REG = os.path.join(HERE, "data", "domains", "register.json")
GRAPH = os.path.join(HERE, "data", "trope_graph.json")
OUT = os.path.join(HERE, "glass", "tropes.html")
LIMIT = 8 * 1024 * 1024

# ---- the system: domain -> layers, each with its name and one line from its SSOT doc ----
CHAR = [
    ("L1", "CORE", "How much cognitive and ideological mass does the mind carry?"),
    ("L2", "VITAL", "How much physical and energetic presence does the body carry?"),
    ("L3", "SOCIAL", "How does the character project into and read the social world?"),
    ("L4", "WILL", "How much resistance holds under pressure, and where does the capacity to decide bend?"),
    ("L5", "WOUND", "What damage failed to resolve, and how severe is it?"),
    ("L6", "DRIVE", "What fuels the active goal-pursuit, and from what source?"),
    ("L7", "ORIGIN", "What birth context and formation set the starting conditions?"),
    ("L8", "IMPRINT", "What formative conditioning locked in before the story began?"),
    ("L9", "EROS", "How is desire structured, armored, and made safe?"),
    ("L10", "SHADOW", "What is repressed, projected, or denied, and what does it generate?"),
    ("L11", "DESTINY", "What is the character building toward, not where they stand?"),
    ("L12", "FUNCTION", "What narrative role and mechanical job does the character carry?"),
]
DOMAINS = [
    ("character", "Character", "ssot_02 character vertical slice",
     "Who a person is, across the twelve LEECHSEED character layers. TV Tropes indexes: Characters As Device, Characterization, Archetypal Character.",
     CHAR),
    ("sexuality", "Sexuality", "ssot_02 character vertical slice (L9 EROS)",
     "Desire and sex. These tropes key onto the character layers, mostly L9 EROS. TV Tropes indexes: Sex Tropes, Queer Romance.",
     CHAR),
    ("setting", "Setting", "ssot_03 setting system",
     "Where a story happens, across the twelve setting layers. TV Tropes indexes: Settings, Religion, School, Motor Vehicle, Cyberpunk, Drugs, Military and Warfare.",
     [("S1", "BODY", "The physical fabric: geography, terrain, architecture, layout, materials."),
      ("S2", "WEATHER", "Climate, seasons, light, atmosphere, and the place's rhythms."),
      ("S3", "SENSORIUM", "How the place meets the senses: sound, smell, texture, palette."),
      ("S4", "LAW", "The rules that bind: governance, institutions, what is allowed and forbidden."),
      ("S5", "SCAR", "Damage in the fabric: ruins, erasures, renames, what was torn down."),
      ("S6", "ECONOMY", "What fuels it: resources, money, traffic, who feeds and powers it."),
      ("S7", "FOUNDING", "Origin: who built it, why, and the deep history."),
      ("S8", "HABIT", "The patterned life: rituals, routines, belonging, insiders and outsiders."),
      ("S9", "ALLURE", "The place's erotics: what it promises and what draws people in."),
      ("S10", "UNDERSIDE", "What it represses: hidden zones, the unspoken, what surfaces under pressure."),
      ("S11", "VECTOR", "Where the place is going: bloom, rot, collapse, redemption."),
      ("S12", "FUNCTION", "Which throughline the place embodies in the storyform, and its argument role.")]),
    ("genre", "Genre", "ssot_01 genre system",
     "What kind of story it is, across the twelve genre layers. TV Tropes indexes: Genres, Genre Tropes.",
     [("G1", "LABEL", "What is the work called by the industry, by marketing and by critics, and do they agree?"),
      ("G2", "FAMILY", "Which family does the genre belong to, and what is its polar opposite?"),
      ("G3", "CONTRACT", "What does the genre owe the reader: elements, steps, obligatory scenes?"),
      ("G4", "ARGUMENT", "What moral argument, what core binary, does the genre exist to prove?"),
      ("G5", "STANCE", "Where does the reader stand on what is real, and how does the doubt resolve?"),
      ("G6", "DELIVERY", "How does the strange enter the text, and is it explained, and to whom?"),
      ("G7", "VERISIMILITUDE", "Against which generic and cultural sense of the plausible is it judged?"),
      ("G8", "WORLD", "What story-world does the genre promise to build?"),
      ("G9", "UPTAKE", "What does the genre call forth, and which genre answers it next?"),
      ("G10", "AUDIENCE", "What mental model does the genre build in an audience before a scene is drafted?"),
      ("G11", "MARKET", "What cycle, budget tier and risk does the label carry in the industry?"),
      ("G12", "FUNCTION", "What does the genre do for the storyform's Grand Argument?")]),
    ("theme", "Theme", "ssot_06 theme system",
     "What the story argues, keyed to the four theme rails (each rail is a debate). TV Tropes indexes: the thematic indexes (Death, Truth and Lies, Family, Love, Power, Emotion, Identity and more).",
     [("R1", "THE WORLD", "They already know how you'll turn out. Can you prove them wrong?"),
      ("R2", "TORI", "Believe the story, or believe your eyes?"),
      ("R3", "ANNA", "Don't fight the game. Win it."),
      ("R4", "TORI AND ANNA", "Whose memory of what happened counts?")]),
    ("texture", "Texture", "ssot_01 texture system",
     "How the story is told, across the twelve texture layers. TV Tropes indexes: Narrative Devices, Framing Device, Narrative Tropes, Point of View.",
     [("T1", "VOICE", "Who speaks, at what level, how reliably, and when relative to the events?"),
      ("T2", "FOCALIZATION", "Who sees, and what is the reader denied?"),
      ("T3", "ORDER", "In what order is the story told, against the order it happened?"),
      ("T4", "DURATION", "At what speed does the telling move, scene through ellipsis?"),
      ("T5", "FREQUENCY", "How often is an event told, against how often it happened?"),
      ("T6", "WORDS", "In what words, register and distance?"),
      ("T7", "FEELING", "With what feeling and tone, and what should the reader feel?"),
      ("T8", "THRESHOLDS", "Through what thresholds (titles, epigraphs, in-world documents) does the reader cross?"),
      ("T9", "FRAMES", "Breaking which frames, and is the break allowed?"),
      ("T10", "NARRATEE", "To whom is the telling aimed, inside and outside the text?"),
      ("T11", "MEDIUM", "Which channel's grammar reshapes the telling?"),
      ("T12", "FUNCTION", "What does this telling do for the storyform's Grand Argument?")]),
    ("tracking", "Tracking", "ssot_08 tracking system",
     "Time in the story: the parts of the tracking system. TV Tropes index: Time Tropes.",
     [("world_clock", "WORLD CLOCK", "When things happened. The fabula runs on it."),
      ("told_order", "TOLD ORDER", "The order the audience is told, laid on the grid."),
      ("grid", "GRID", "The musical time layer under the timeline: ticks, beats, bars, tempo."),
      ("story_point", "STORY POINT", "A dated point on the grid where the story turns."),
      ("cable", "CABLE", "A link from a setup to its payoff."),
      ("tempo", "TEMPO", "How fast it moves: world time per beat, and beats reaching the audience.")]),
    ("style", "Style", "ssot_07_1 prose style · ssot_07_3 pages style",
     "How the work reads and looks: the two style guides. TV Tropes indexes: Language, Costume, Graphical, Lighting, Amazing Technicolor.",
     [("07.1", "PROSE", "How the LEECHSEED stories read on the page: the language tropes."),
      ("07.3", "PAGES", "How pages and pictures look: costume, graphics, lighting and color tropes.")]),
]
NULL = ("null", "UNPLACED", "Tagged to this domain, but no layer fits: the key is null.")
CONF = ["high", "medium", "low"]


def build(write=True):
    reg = json.load(io.open(REG, encoding="utf-8"))
    graph = json.load(io.open(GRAPH, encoding="utf-8"))
    ids = sorted(reg, key=lambda s: (reg[s]["name"].lower(), s))
    pos = {s: i for i, s in enumerate(ids)}
    dom = []
    lidx = {}   # (domain, code) -> (di, li)
    for di, (did, name, src, what, layers) in enumerate(DOMAINS):
        ls = [{"c": c, "n": n, "m": m} for c, n, m in layers] + [{"c": NULL[0], "n": NULL[1], "m": NULL[2]}]
        dom.append({"id": did, "name": name, "src": src, "what": what, "layers": ls})
        for li, l in enumerate(ls):
            lidx[(did, l["c"])] = (di, li)
    unknown = Counter()
    nm, df, ky, cf, ln = [], [], [], [], []
    kept = dropped = 0
    for s in ids:
        v = reg[s]
        nm.append(v["name"])
        df.append(v.get("def") or "")
        pairs = []
        keys = dict(v.get("keys") or {})
        for d in v.get("domains") or []:
            keys.setdefault(d, None)
        for d in sorted(keys, key=lambda d: [x[0] for x in DOMAINS].index(d) if d in [x[0] for x in DOMAINS] else 99):
            code = "null" if keys[d] is None else str(keys[d])
            if (d, code) not in lidx:
                unknown[(d, code)] += 1
                if not any(x["id"] == d for x in dom):
                    continue
                di = [x["id"] for x in dom].index(d)
                dom[di]["layers"].insert(-1, {"c": code, "n": code.upper(), "m": "A code the SSOT doc does not name yet."})
                for li, l in enumerate(dom[di]["layers"]):
                    lidx[(d, l["c"])] = (di, li)
            pairs += list(lidx[(d, code)])
        ky.append(pairs)
        cf.append(CONF.index(v["conf"]) if v.get("conf") in CONF else 2)
        raw = list(dict.fromkeys(v.get("links") or []))
        keep = [pos[x] for x in raw if x in pos and x != s]
        kept += len(keep); dropped += len(raw) - len(keep)
        ln.append(keep)
    nodes = {n["id"]: n for n in graph.get("nodes", [])}
    nlist, nix, pg = [], {}, {}
    def node(nid):
        if not nid or nid not in nodes:
            return -1
        if nid not in nix:
            n = nodes[nid]
            nix[nid] = len(nlist)
            nlist.append({"id": nid, "name": n.get("name", nid), "def": n.get("def", ""), "cite": n.get("cite", ""), "fam": n.get("family", "")})
        return nix[nid]
    for t in graph.get("tropes", []):
        if t.get("slug") in pos:
            pg[pos[t["slug"]]] = [node(t.get("node")), node(t.get("alt")), CONF.index(t["conf"]) if t.get("conf") in CONF else -1]
    # the counts the home shows
    by_dom = Counter(); by_layer = Counter()
    for pairs in ky:
        seen = set()
        for j in range(0, len(pairs), 2):
            by_layer[(pairs[j], pairs[j + 1])] += 1
            seen.add(pairs[j])
        for d in seen:
            by_dom[d] += 1
    for di, d in enumerate(dom):
        d["count"] = by_dom[di]
        for li, l in enumerate(d["layers"]):
            l["count"] = by_layer[(di, li)]
    built = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p").replace(" 0", " ")
    counts = {"tropes": len(ids), "no_def": sum(1 for d in df if not d), "high": cf.count(0), "medium": cf.count(1),
              "low": cf.count(2), "multi": sum(1 for p in ky if len(set(p[0::2])) > 1), "plot": len(pg),
              "both": sum(1 for i in range(len(ids)) if not df[i] and cf[i] == 2),
              "links_kept": kept, "links_dropped": dropped}
    data = {"built": built, "counts": counts, "dom": dom, "conf": CONF, "ids": ids, "nm": nm, "df": df, "ky": ky,
            "cf": cf, "ln": ln, "pg": pg, "nodes": nlist,
            "graph": {"nodes": graph.get("counts", {}).get("nodes"), "keyed": graph.get("counts", {}).get("tropes_keyed")}}
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = PAGE.replace("__CSS__", CSS).replace("__JS__", JS).replace("__DATA__", blob)
    html = _theme(html, "tropes")
    size = len(html.encode("utf-8"))
    summary = {"ok": True, "page": OUT, "bytes": size, "mb": round(size / 1048576, 2), "embedded": size <= LIMIT,
               "built": built, "domains": {d["id"]: d["count"] for d in dom},
               "unknown_codes": ["%s:%s" % k for k in unknown], **counts, "wrote": False}
    if size > LIMIT:
        summary.update(ok=False, error="page passes 8 MB; move the data to a sibling JSON")
        return summary
    if write:
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
        summary["wrote"] = True
    return summary


def _theme(h, page=None):   # BOLO 171: the one theme (_tools/brand/theme.py); never fatal
    try:
        import importlib.util as _u
        _s = _u.spec_from_file_location("cmd_theme", os.path.join(ROOT, "_tools", "brand", "theme.py"))
        _m = _u.module_from_spec(_s); _s.loader.exec_module(_m)
        return _m.apply(h, page)
    except Exception:
        return h


CSS = r"""
/* the trope system glass (BOLO 89), DARK only. Tokens come from the theme block (_tools/brand/theme.css). */
*{box-sizing:border-box}
html,body{background:var(--cmd-bg,#050608);color:var(--cmd-fg,#c6cbc8)}
body{margin:0;font:13px/1.5 var(--cmd-font,monospace)}
a{color:var(--cmd-acch,#FFB08F);text-decoration:none}
a:hover{color:var(--cmd-acc,#FF5A1F)}
header{position:sticky;top:0;z-index:20;height:var(--cmd-chrome,44px);display:flex;align-items:center;gap:12px;padding:0 16px;
  background:var(--cmd-panel,#0a0c0f);border-bottom:1px solid var(--cmd-line,#23272b)}
header h1{margin:0;font-size:14px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;white-space:nowrap}
header h1 a{color:var(--cmd-acc,#FF5A1F)}
header .sp{flex:1}
header .st{color:var(--cmd-fg2);font-size:12px;white-space:nowrap}
#q{flex:0 1 380px;min-width:120px;font:inherit;font-size:12px;background:var(--cmd-inset,#030405);color:var(--cmd-fg);border:1px solid var(--cmd-line2);padding:4px 8px}
#q:focus{border-color:var(--cmd-acc);outline:none}
button,select{font:inherit;font-size:12px;background:var(--cmd-panel2);color:var(--cmd-fg);border:1px solid var(--cmd-line);padding:3px 10px;cursor:pointer}
button:hover,button:focus-visible,select:focus-visible{border-color:var(--cmd-acc);color:var(--cmd-acch);outline:none}
#meta{display:none;padding:8px 16px;background:var(--cmd-panel);border-bottom:1px solid var(--cmd-line);color:var(--cmd-fg2);font-size:12px}
#meta.on{display:block}
#meta p{margin:4px 0}
.wrap{display:grid;grid-template-columns:270px minmax(0,1fr);min-height:calc(100vh - 44px)}
nav{position:sticky;top:44px;align-self:start;height:calc(100vh - 44px);overflow-y:auto;padding:8px 0 24px;border-right:1px solid var(--cmd-line);background:var(--cmd-panel)}
nav h2{margin:12px 14px 4px;font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--cmd-dim);font-weight:600}
nav a{display:flex;justify-content:space-between;gap:8px;padding:2px 14px;color:var(--cmd-fg2);font-size:12px;border-left:2px solid transparent}
nav a:hover{background:var(--cmd-hl);color:var(--cmd-fg)}
nav a.on{border-left-color:var(--cmd-acc);background:var(--cmd-accsoft);color:var(--cmd-white)}
nav a.dom{color:var(--cmd-fg);font-weight:600;margin-top:4px}
nav a.lay{padding-left:26px}
nav a.lay.zero{color:var(--cmd-dim)}
nav a .n{color:var(--cmd-dim);font-size:11px}
nav a .c{color:var(--cmd-acch);display:inline-block;min-width:44px}
nav .sub{display:none} nav .sub.open{display:block}
main{padding:16px 22px 60px;min-width:0}
h2.pg{margin:0 0 4px;font-size:18px;font-weight:600;color:var(--cmd-white)}
.lede{color:var(--cmd-fg2);margin:0 0 14px;max-width:820px}
.crumb{color:var(--cmd-dim);font-size:11px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:4px}
.crumb a{color:var(--cmd-fg2)}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:8px;margin:0 0 18px}
.tile{display:block;border:1px solid var(--cmd-line);background:var(--cmd-panel);padding:8px 10px;color:var(--cmd-fg)}
a.tile:hover{border-color:var(--cmd-acc)}
.tile b{display:block;font-size:22px;font-weight:600;color:var(--cmd-white);line-height:1.15}
.tile small{color:var(--cmd-fg2);font-size:11px}
.tile.work{border-color:var(--cmd-accd)} .tile.work b{color:var(--cmd-acc)}
h3{margin:18px 0 8px;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--cmd-acch);font-weight:600}
.bars{display:grid;grid-template-columns:120px minmax(0,1fr) 60px;gap:4px 10px;align-items:center;max-width:820px}
.bars .bar{height:12px;background:var(--cmd-inset);border:1px solid var(--cmd-line)}
.bars .bar i{display:block;height:100%;background:var(--cmd-acc)}
.bars .bar i.lo{background:var(--cmd-accm)}
.bars .num{text-align:right;color:var(--cmd-fg2);font-size:12px}
.filters{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:0 0 10px;padding:6px 8px;border:1px solid var(--cmd-line);background:var(--cmd-panel)}
.filters label{color:var(--cmd-fg2);font-size:11px}
.filters .cnt{margin-left:auto;color:var(--cmd-fg2);font-size:12px}
.rows{border-top:1px solid var(--cmd-line)}
.row{display:grid;grid-template-columns:minmax(160px,1.1fr) minmax(120px,.9fr) 64px minmax(0,2fr);gap:10px;padding:4px 6px;border-bottom:1px solid var(--cmd-line);color:var(--cmd-fg);align-items:baseline}
.row:hover{background:var(--cmd-hl);color:var(--cmd-white)}
.row .nm{color:var(--cmd-acch)}
.row .df{color:var(--cmd-fg2);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-size:12px}
.row .df.none,.nodef{color:var(--cmd-am);font-style:italic}
.kc{display:inline-block;white-space:nowrap;font-size:11px;border:1px solid var(--cmd-line2);padding:0 5px;margin:0 3px 2px 0;color:var(--cmd-fg2)}
.kc.null{border-style:dashed;color:var(--cmd-dim)}
.cw{font-size:11px} .cw.c0{color:var(--cmd-ok)} .cw.c1{color:var(--cmd-am)} .cw.c2{color:var(--cmd-bad)}
.more{margin:10px 0}
.empty{color:var(--cmd-dim);padding:14px 0}
.card{max-width:900px}
.card .slug{color:var(--cmd-dim);font-size:11px}
.card .def{font-size:15px;line-height:1.55;color:var(--cmd-fg);margin:10px 0 14px;max-width:780px}
.kt{width:100%;border-collapse:collapse;max-width:900px}
.kt td,.kt th{text-align:left;padding:5px 8px;border-bottom:1px solid var(--cmd-line);vertical-align:top}
.kt th{font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--cmd-dim);font-weight:600}
.kt .m{color:var(--cmd-fg2)}
.chips{display:flex;flex-wrap:wrap;gap:4px}
.chip{display:inline-block;white-space:nowrap;border:1px solid var(--cmd-line2);padding:1px 7px;font-size:12px;color:var(--cmd-acch);background:var(--cmd-panel)}
.chip:hover{border-color:var(--cmd-acc)}
.facts{display:flex;flex-wrap:wrap;gap:16px;margin:4px 0 6px;color:var(--cmd-fg2);font-size:12px}
.lt{width:100%;border-collapse:collapse;max-width:960px}
.lt td{padding:5px 8px;border-bottom:1px solid var(--cmd-line);vertical-align:top}
.lt td.n{text-align:right;color:var(--cmd-fg2);white-space:nowrap}
/* the hover layer (CK3): dotted terms open a tip; click pins it; Space locks the open tips; Esc clears; terms nest */
.t{border-bottom:1px dotted var(--cmd-accm);cursor:help}
a.t{cursor:pointer}
nav a.t,a.row.t,.bars a.t{border-bottom-color:transparent}
a.row.t{border-bottom:1px solid var(--cmd-line)}
.tip{position:fixed;z-index:50;max-width:360px;background:var(--cmd-panel2);border:1px solid var(--cmd-acc);padding:8px 10px;font-size:12px;line-height:1.45;color:var(--cmd-fg);box-shadow:0 6px 24px rgba(0,0,0,.6)}
.tip b{color:var(--cmd-acch);display:block;margin-bottom:2px;font-size:11px;letter-spacing:.1em;text-transform:uppercase}
.tip .q{display:block;margin-top:4px;color:var(--cmd-fg2)}
.tip.pin{border-style:double;border-width:3px}
.tip .hint{display:block;margin-top:5px;color:var(--cmd-dim);font-size:10px}
@media(max-width:760px){
 .wrap{grid-template-columns:minmax(0,1fr)}
 nav{position:static;height:auto;max-height:40vh;border-right:0;border-bottom:1px solid var(--cmd-line)}
 main{padding:12px 16px 40px}
 .row{grid-template-columns:minmax(0,1fr) 60px}.row .ks,.row .df{display:none}
 header .st{display:none}
}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""

JS = r"""
(function(){
"use strict";
var D=JSON.parse(document.getElementById("tg-data").textContent);
var N=D.ids.length, DOM=D.dom, CONF=D.conf;
var BYID={};D.ids.forEach(function(s,i){BYID[s]=i});
var LNAME=D.nm.map(function(s){return s.toLowerCase()}), LDEF=D.df.map(function(s){return s.toLowerCase()});
var BACK=null;   // linked-from, built on first need
function E(s){return String(s==null?"":s).replace(/[&<>"']/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})}
function F(x){return Number(x).toLocaleString("en-US")}
function H(s){return encodeURIComponent(s)}
/* a hover term: a span pins on click; an anchor navigates on click */
function T(spec,txt,cls){return '<span class="t'+(cls?" "+cls:"")+'" data-t="'+spec+'" tabindex="0">'+txt+'</span>'}
function A(spec,href,txt,cls){return '<a class="t'+(cls?" "+cls:"")+'" data-t="'+spec+'" href="'+href+'">'+txt+'</a>'}
var TERMS={
 tvt:["TV Tropes","The wiki every trope comes from. The register keeps its names and one-line definitions only; the repo is public."],
 domain:["Domain","A system a trope serves: character, sexuality, setting, genre, theme, texture, tracking or style. A trope can serve several; each gets its own {key}."],
 key:["Key","Where a trope sits inside a {domain}: one {layer} per domain, or {unplaced} when no layer fits. Keyed by Payload Specialist batches, checked by a script."],
 layer:["Layer","One slot of a system, with its code and name (L5 WOUND, S10 UNDERSIDE, G1 LABEL). Each layer has a pull list: every trope keyed to it."],
 unplaced:["Unplaced","The trope is tagged to the {domain}, but no layer fits, so its {key} is null. The rail lists these under each domain."],
 conf:["Confidence","How sure the key is: high, medium or low. Most low keys belong to tropes with {nodef}, keyed from the title alone."],
 nodef:["No definition yet","TV Tropes' index page gives this trope no one-line definition. The rule (10/04): it keys by its title and domain tags, and the record says the definition is undefined. No run is needed to fill it."],
 multi:["Multi-domain","A trope tagged to two or more {domain}s, so it sits on a {layer} in each."],
 plot:["The plot graph","ssot_04 trope graph: 1,034 tropes from TV Tropes' Plot indexes, keyed onto 135 plot nodes. Only some of them are also in this register; their cards say which {node} uses them."],
 node:["Plot node","One of the 135 nodes of the plot graph (Tobias, Polti, Vogler and others). A trope keys onto one node, sometimes with an alternate."],
 links:["Links","The trope page's links to other tropes, kept only where the target is in this register too. Outside targets are dropped at build."],
 back:["Linked from","Tropes in this register whose pages link to this one."],
 openwork:["Open work","The tropes still to finish: {nodef}, and low {conf} keys."]
};
function sub(s){return E(s).replace(/\{(\w+)\}/g,function(_,w){return TERMS[w]?T("t:"+w,TERMS[w][0].toLowerCase()):w})}
function lay(di,li){return DOM[di].layers[li]}
function code(di,li){var l=lay(di,li);return l.c==="null"?"null":l.c}
function keysOf(i){var k=D.ky[i],o=[];for(var j=0;j<k.length;j+=2)o.push([k[j],k[j+1]]);return o}
function domsOf(i){var k=D.ky[i],s={};for(var j=0;j<k.length;j+=2)s[k[j]]=1;return Object.keys(s).map(Number)}
var SHORT={character:"char",sexuality:"sex",setting:"set",genre:"genre",theme:"theme",texture:"tex",tracking:"track",style:"style"};
function kchip(di,li){var l=lay(di,li);return T("l:"+di+"."+li,E((SHORT[DOM[di].id]||DOM[di].id)+" "+(l.c==="null"?"null":l.c)),"kc"+(l.c==="null"?" null":""))}
function cword(c){return T("c:"+c,CONF[c],"cw c"+c)}
function tipHTML(spec){
 var p=spec.split(":"),k=p[0],v=p.slice(1).join(":");
 if(k==="t"){var t=TERMS[v];return t?"<b>"+E(t[0])+"</b>"+sub(t[1]):""}
 if(k==="d"){var d=DOM[+v];var top=d.layers.slice().map(function(l,li){return [l.count,li]}).sort(function(a,b){return b[0]-a[0]}).slice(0,3);
  return "<b>"+E(d.name)+" · domain</b>"+E(d.what)+'<span class="q">'+F(d.count)+" tropes. Busiest: "+top.map(function(x){return T("l:"+v+"."+x[1],E(code(+v,x[1])))+" "+F(x[0])}).join(" · ")+'</span><span class="q">Source: '+E(d.src)+"</span>"}
 if(k==="l"){var q=v.split("."),di=+q[0],li=+q[1],l=lay(di,li);
  return "<b>"+E(l.c==="null"?"null":l.c)+" "+E(l.n)+"</b>"+E(l.m)+'<span class="q">'+F(l.count)+" tropes · "+T("d:"+di,E(DOM[di].name))+" · "+'<a href="#/layer/'+DOM[di].id+"/"+H(l.c)+'">list them</a></span>'}
 if(k==="c"){var c=+v,w=["A sure fit: the key reads straight off the definition.","A fair fit: another layer could argue for it.","A guess, usually keyed from the title alone because the trope has {nodef}."][c];
  var n=D.cf.filter(function(x){return x===c}).length;
  return "<b>"+CONF[c]+" confidence</b>"+sub(w)+'<span class="q">'+F(n)+' tropes · <a href="#/list/'+CONF[c]+'">list them</a></span>'}
 if(k==="k"){var i=+v;if(!(i>=0&&i<N))return"";
  return "<b>"+E(D.nm[i])+"</b>"+(D.df[i]?E(D.df[i]):T("t:nodef","no definition yet","nodef"))+'<span class="q">'+keysOf(i).map(function(x){return kchip(x[0],x[1])}).join("")+" "+cword(D.cf[i])+'</span><span class="q"><a href="#/trope/'+H(D.ids[i])+'">open the card</a></span>'}
 if(k==="n"){var nd=D.nodes[+v];if(!nd)return"";return "<b>"+E(nd.name)+" · plot node</b>"+E(nd.def)+'<span class="q">'+E(nd.cite)+" · "+E(nd.id)+"</span>"}
 return ""
}

/* ---- the rail: domains -> layers, with counts ---- */
var nav=document.querySelector("nav");
function rail(){
 var h='<h2>'+T("t:openwork","Open work")+'</h2>'+
  '<a href="#/" data-r="home"><span>Overview</span></a>'+
  A("t:nodef","#/list/nodef",'<span>No definition</span><span class="n">'+F(D.counts.no_def)+"</span>")+
  A("c:2","#/list/low",'<span>Low confidence</span><span class="n">'+F(D.counts.low)+"</span>")+
  A("t:multi","#/list/multi",'<span>Multi-domain</span><span class="n">'+F(D.counts.multi)+"</span>")+
  A("t:plot","#/list/plot",'<span>In the plot graph</span><span class="n">'+F(D.counts.plot)+"</span>")+
  '<a href="#/list/all"><span>Every trope</span><span class="n">'+F(N)+"</span></a>"+
  '<h2>'+T("t:domain","Domains")+" → "+T("t:layer","layers")+"</h2>";
 DOM.forEach(function(d,di){
  h+=A("d:"+di,"#/domain/"+d.id,"<span>"+E(d.name)+'</span><span class="n">'+F(d.count)+"</span>","dom")+'<div class="sub" data-d="'+di+'">';
  d.layers.forEach(function(l,li){
   if(l.c==="null"&&!l.count)return;
   h+=A("l:"+di+"."+li,"#/layer/"+d.id+"/"+H(l.c),'<span><span class="c">'+E(l.c)+"</span>"+E(l.n)+'</span><span class="n">'+F(l.count)+"</span>","lay"+(l.count?"":" zero"))});
  h+="</div>"});
 nav.innerHTML=h;
 [].forEach.call(nav.querySelectorAll("a"),function(a){a.removeAttribute("tabindex")});
}
function markRail(){
 var cur=location.hash||"#/";
 [].forEach.call(nav.querySelectorAll("a"),function(a){a.classList.toggle("on",a.getAttribute("href")===cur)});
 var r=route(),open=-1;
 if(r[0]==="domain"||r[0]==="layer"){var did=r[1].split("/")[0];open=DOM.findIndex(function(d){return d.id===did})}
 if(r[0]==="trope"&&BYID[r[1]]!=null){var ds=domsOf(BYID[r[1]]);open=ds.length?ds[0]:-1}
 [].forEach.call(nav.querySelectorAll(".sub"),function(s){s.classList.toggle("open",+s.dataset.d===open)});
 var on=nav.querySelector("a.on");if(on&&on.scrollIntoView){var nr=nav.getBoundingClientRect(),ar=on.getBoundingClientRect();if(ar.top<nr.top||ar.bottom>nr.bottom)on.scrollIntoView({block:"center"})}
}

/* ---- filters: confidence, has-definition, multi-domain ---- */
var FL={conf:"any",def:"any",multi:"any"};
try{var sv=JSON.parse(localStorage.getItem("tg-filters")||"null");if(sv)FL=Object.assign(FL,sv)}catch(e){}
function pass(i){
 if(FL.conf!=="any"&&CONF[D.cf[i]]!==FL.conf)return false;
 if(FL.def==="has"&&!D.df[i])return false;
 if(FL.def==="none"&&D.df[i])return false;
 if(FL.multi==="multi"&&domsOf(i).length<2)return false;
 if(FL.multi==="single"&&domsOf(i).length>1)return false;
 return true}
function sel(id,label,opts){return '<label>'+label+' <select data-f="'+id+'">'+opts.map(function(o){return '<option value="'+o[0]+'"'+(FL[id]===o[0]?" selected":"")+">"+o[1]+"</option>"}).join("")+"</select></label>"}
function filterBar(shown,total){
 return '<div class="filters">'+sel("conf",T("t:conf","Confidence"),[["any","any"],["high","high"],["medium","medium"],["low","low"]])+
  sel("def","Definition",[["any","any"],["has","has one"],["none","none yet"]])+
  sel("multi",T("t:domain","Domains"),[["any","any"],["multi","multi-domain"],["single","one domain"]])+
  '<span class="cnt">'+F(shown)+" of "+F(total)+"</span></div>"}

/* ---- the list: rows link to cards; key chips and confidence words are hover terms ---- */
var PAGE=500;
function rowHTML(i){
 return '<a class="row t" data-t="k:'+i+'" href="#/trope/'+H(D.ids[i])+'"><span class="nm">'+E(D.nm[i])+'</span><span class="ks">'+keysOf(i).map(function(x){return kchip(x[0],x[1])}).join("")+"</span>"+cword(D.cf[i])+
  (D.df[i]?'<span class="df">'+E(D.df[i])+"</span>":'<span class="df none">no definition yet</span>')+"</a>"}
function listView(title,lede,all,crumb){
 var rows=all.filter(pass),shown=Math.min(rows.length,PAGE);
 var h=(crumb?'<div class="crumb">'+crumb+"</div>":"")+'<h2 class="pg">'+title+'</h2><p class="lede">'+lede+"</p>"+filterBar(rows.length,all.length);
 if(!rows.length)return h+'<div class="empty">Nothing here with these filters.</div>';
 h+='<div class="rows" id="rows">'+rows.slice(0,shown).map(rowHTML).join("")+"</div>";
 if(rows.length>shown)h+='<div class="more"><button id="more" data-at="'+shown+'">Show '+F(Math.min(PAGE,rows.length-shown))+" more ("+F(rows.length-shown)+" left)</button></div>";
 LAST=rows;return h}
var LAST=[];
function allIdx(){var a=new Array(N);for(var i=0;i<N;i++)a[i]=i;return a}
function inLayer(di,li){var o=[];for(var i=0;i<N;i++){var k=D.ky[i];for(var j=0;j<k.length;j+=2)if(k[j]===di&&k[j+1]===li){o.push(i);break}}return o}
function inDomain(di){var o=[];for(var i=0;i<N;i++){var k=D.ky[i];for(var j=0;j<k.length;j+=2)if(k[j]===di){o.push(i);break}}return o}

/* ---- the views ---- */
function home(){
 var c=D.counts,mx=Math.max.apply(null,DOM.map(function(d){return d.count}));
 var h='<h2 class="pg">The trope system</h2><p class="lede">'+F(N)+" "+T("t:tvt","TV Tropes")+" tropes, each tagged with the "+T("t:domain","domains")+" it serves and keyed to one "+T("t:layer","layer")+
  " of each domain's system. Pick a domain or layer on the left, search above, or open the "+T("t:openwork","open work")+" below.</p>";
 h+='<div class="tiles"><div class="tile"><b>'+F(N)+'</b><small>tropes in the register</small></div>'+
  '<a class="tile work" href="#/list/nodef"><b>'+F(c.no_def)+"</b><small>"+T("t:nodef","no definition yet")+"</small></a>"+
  '<a class="tile work" href="#/list/low"><b>'+F(c.low)+"</b><small>"+T("c:2","low confidence")+"</small></a>"+
  '<a class="tile" href="#/list/both"><b>'+F(c.both)+"</b><small>both: no definition and low</small></a>"+
  '<a class="tile" href="#/list/multi"><b>'+F(c.multi)+"</b><small>"+T("t:multi","multi-domain")+"</small></a>"+
  '<a class="tile" href="#/list/plot"><b>'+F(c.plot)+"</b><small>used by "+T("t:plot","the plot graph")+"</small></a></div>";
 h+="<h3>By domain</h3><div class=\"bars\">";
 DOM.forEach(function(d,di){h+=A("d:"+di,"#/domain/"+d.id,E(d.name))+'<span class="bar"><i style="width:'+(100*d.count/mx).toFixed(1)+'%"></i></span><span class="num">'+F(d.count)+"</span>"});
 h+="</div><h3>By "+T("t:conf","confidence")+'</h3><div class="bars">';
 [0,1,2].forEach(function(ci){var n=[c.high,c.medium,c.low][ci];h+=A("c:"+ci,"#/list/"+CONF[ci],CONF[ci])+'<span class="bar"><i class="'+(ci?"lo":"")+'" style="width:'+(100*n/N).toFixed(1)+'%"></i></span><span class="num">'+F(n)+"</span>"});
 h+="</div><h3>Links</h3><p class=\"lede\">"+F(c.links_kept)+" "+T("t:links","links")+" between register tropes kept; "+F(c.links_dropped)+" to pages outside the register dropped at build.</p>";
 return h}
function domainView(di){
 var d=DOM[di];
 var h='<div class="crumb"><a href="#/">Overview</a> / domain</div><h2 class="pg">'+E(d.name)+'</h2><p class="lede">'+E(d.what)+"<br>Source: "+E(d.src)+" · "+F(d.count)+" tropes.</p>";
 h+='<table class="lt">';
 d.layers.forEach(function(l,li){if(l.c==="null"&&!l.count)return;
  h+="<tr><td>"+A("l:"+di+"."+li,"#/layer/"+d.id+"/"+H(l.c),E(l.c))+"</td><td><b>"+E(l.n)+'</b></td><td class="m">'+E(l.m)+'</td><td class="n">'+F(l.count)+"</td></tr>"});
 h+="</table><h3>Every trope in "+E(d.name)+"</h3>";
 return h+listView("","",inDomain(di)).replace('<h2 class="pg"></h2><p class="lede"></p>',"")}
function layerView(di,li){
 var d=DOM[di],l=d.layers[li];
 return listView(E(l.c==="null"?"null":l.c)+" "+E(l.n),E(l.m)+" ("+T("t:layer","layer")+" of "+T("d:"+di,E(d.name))+")",inLayer(di,li),'<a href="#/">Overview</a> / <a href="#/domain/'+d.id+'">'+E(d.name)+"</a> / layer")}
function specialView(w){
 var all=allIdx(),c="<a href=\"#/\">Overview</a> / list";
 if(w==="nodef")return listView("No definition yet","The open work: tropes TV Tropes gives no one-line "+T("t:nodef","definition")+". Each keyed from its title.",all.filter(function(i){return !D.df[i]}),c);
 if(w==="both")return listView("No definition and low confidence","The hardest open work: no definition, and a low "+T("t:conf","confidence")+" key.",all.filter(function(i){return !D.df[i]&&D.cf[i]===2}),c);
 var ci=CONF.indexOf(w);
 if(ci>=0)return listView(E(w[0].toUpperCase()+w.slice(1))+" confidence","Tropes whose keys are "+cword(ci)+" confidence.",all.filter(function(i){return D.cf[i]===ci}),c);
 if(w==="multi")return listView("Multi-domain","Tropes that sit in two or more "+T("t:domain","domains")+".",all.filter(function(i){return domsOf(i).length>1}),c);
 if(w==="plot")return listView("Used by the plot graph","Register tropes that "+T("t:plot","the plot graph")+" also keys onto a "+T("t:node","plot node")+".",all.filter(function(i){return D.pg[i]}),c);
 return listView("Every trope","The whole register, A to Z.",all,c)}
function searchView(q){
 var s=q.toLowerCase().trim();if(!s)return listView("Search","Type in the box above: names and definitions.",[],"");
 var a=[],b=[],c=[];
 for(var i=0;i<N;i++){var n=LNAME[i];if(n.indexOf(s)===0)a.push(i);else if(n.indexOf(s)>0)b.push(i);else if(LDEF[i].indexOf(s)>=0)c.push(i)}
 return listView("Search: "+E(q),F(a.length+b.length)+" name matches, "+F(c.length)+" definition matches. Names first.",a.concat(b,c),'<a href="#/">Overview</a> / search')}
function backlinks(i){
 if(!BACK){BACK=new Array(N);for(var x=0;x<N;x++)BACK[x]=[];for(var y=0;y<N;y++){var L=D.ln[y];for(var j=0;j<L.length;j++)BACK[L[j]].push(y)}}
 return BACK[i]}
function chips(list,cap,id){
 var h='<div class="chips" id="'+id+'">'+list.slice(0,cap).map(function(j){return A("k:"+j,"#/trope/"+H(D.ids[j]),E(D.nm[j]),"chip")}).join("")+"</div>";
 if(list.length>cap)h+='<div class="more"><button data-all="'+id+'">Show all '+F(list.length)+"</button></div>";
 return h}
function card(i){
 var ks=keysOf(i),pg=D.pg[i],L=D.ln[i].slice().sort(function(a,b){return LNAME[a]<LNAME[b]?-1:1}),B=backlinks(i).slice().sort(function(a,b){return LNAME[a]<LNAME[b]?-1:1});
 var h='<div class="card"><div class="crumb"><a href="#/">Overview</a> / '+ks.map(function(x){return '<a href="#/layer/'+DOM[x[0]].id+"/"+H(lay(x[0],x[1]).c)+'">'+E(DOM[x[0]].name)+" "+E(code(x[0],x[1]))+"</a>"}).join(" · ")+" / trope</div>";
 h+='<h2 class="pg">'+E(D.nm[i])+'</h2><div class="slug">'+E(D.ids[i])+"</div>";
 h+=D.df[i]?'<p class="def">'+E(D.df[i])+"</p>":'<p class="def">'+T("t:nodef","No definition yet.","nodef")+"</p>";
 h+='<div class="facts"><span>'+T("t:conf","Confidence")+": "+cword(D.cf[i])+"</span><span>"+F(ks.length)+" "+T("t:key","key"+(ks.length>1?"s":""))+'</span><span><a href="https://tvtropes.org/pmwiki/pmwiki.php/Main/'+H(D.ids[i])+'" target="_blank" rel="noopener">Open on TV Tropes ↗</a></span></div>';
 h+='<h3>Keys</h3><table class="kt"><tr><th>'+T("t:domain","Domain")+"</th><th>"+T("t:layer","Layer")+'</th><th>Name</th><th>What it holds</th><th></th></tr>';
 ks.forEach(function(x){var l=lay(x[0],x[1]);
  h+="<tr><td>"+T("d:"+x[0],E(DOM[x[0]].name))+"</td><td>"+T("l:"+x[0]+"."+x[1],E(l.c==="null"?"null":l.c))+"</td><td><b>"+E(l.n)+'</b></td><td class="m">'+E(l.m)+'</td><td><a href="#/layer/'+DOM[x[0]].id+"/"+H(l.c)+'">all '+F(l.count)+"</a></td></tr>"});
 h+="</table>";
 if(pg){h+="<h3>Used by "+T("t:plot","the plot graph")+'</h3><p class="lede">Keyed onto '+(pg[0]>=0?T("n:"+pg[0],E(D.nodes[pg[0]].name)):"no node")+(pg[1]>=0?", alternate "+T("n:"+pg[1],E(D.nodes[pg[1]].name)):"")+(pg[2]>=0?", "+cword(pg[2])+" confidence":"")+".</p>"}
 h+="<h3>"+T("t:links","Links")+" in the register · "+F(L.length)+"</h3>"+(L.length?chips(L,80,"cl"):'<div class="empty">No links to register tropes.</div>');
 h+="<h3>"+T("t:back","Linked from")+" · "+F(B.length)+"</h3>"+(B.length?chips(B,80,"cb"):'<div class="empty">No register trope links here.</div>');
 return h+"</div>"}
var main=document.querySelector("main");
function route(){var h=decodeURIComponent((location.hash||"#/").replace(/^#\/?/,""));var i=h.indexOf("/");return i<0?[h,""]:[h.slice(0,i),h.slice(i+1)]}
function render(){
 var r=route(),v=r[0],a=r[1],h;
 if(v==="trope"&&BYID[a]!=null)h=card(BYID[a]);
 else if(v==="domain"){var di=DOM.findIndex(function(d){return d.id===a});h=di>=0?domainView(di):home()}
 else if(v==="layer"){var q=a.split("/"),dj=DOM.findIndex(function(d){return d.id===q[0]}),lj=dj>=0?DOM[dj].layers.findIndex(function(l){return l.c===q.slice(1).join("/")}):-1;h=lj>=0?layerView(dj,lj):home()}
 else if(v==="list")h=specialView(a);
 else if(v==="search"){h=searchView(a);if(document.activeElement!==qbox)qbox.value=a}
 else if(v==="trope")h='<div class="empty">No trope with the id '+E(a)+' in the register. <a href="#/">Overview</a></div>';
 else h=home();
 main.innerHTML=h;
 if(!locked)close(0);
 markRail();
 if(v!=="search")window.scrollTo(0,0);
}
main.addEventListener("click",function(e){
 var m=e.target.closest("#more");
 if(m){var at=+m.dataset.at,nx=LAST.slice(at,at+PAGE);document.getElementById("rows").insertAdjacentHTML("beforeend",nx.map(rowHTML).join(""));at+=nx.length;
  if(at>=LAST.length)m.parentNode.remove();else{m.dataset.at=at;m.textContent="Show "+F(Math.min(PAGE,LAST.length-at))+" more ("+F(LAST.length-at)+" left)"}return}
 var b=e.target.closest("[data-all]");
 if(b){var id=b.dataset.all,r=route(),i=BYID[r[1]];var list=(id==="cl"?D.ln[i]:backlinks(i)).slice().sort(function(x,y){return LNAME[x]<LNAME[y]?-1:1});
  document.getElementById(id).outerHTML=chips(list,list.length,id);b.parentNode.remove()}
});
main.addEventListener("change",function(e){var s=e.target.closest("[data-f]");if(!s)return;FL[s.dataset.f]=s.value;try{localStorage.setItem("tg-filters",JSON.stringify(FL))}catch(x){}var y=window.scrollY;render();window.scrollTo(0,y)});
var qbox=document.getElementById("q"),qt=null;
qbox.addEventListener("input",function(){clearTimeout(qt);qt=setTimeout(function(){
 var v=qbox.value,target=v.trim()?"#/search/"+H(v):"#/";
 if(route()[0]==="search"&&v.trim())history.replaceState(null,"",target),render();else location.hash=target},120)});
document.addEventListener("keydown",function(e){if(e.key==="/"&&document.activeElement!==qbox&&!/^(INPUT|SELECT|TEXTAREA)$/.test(document.activeElement.tagName)){e.preventDefault();qbox.focus();qbox.select()}});
window.addEventListener("hashchange",render);

/* the hover layer (CK3, after the desk): hover opens, click pins (anchors navigate), Space locks every open tip, Esc clears; tips nest */
var stack=[],locked=false,timer=null,otimer=null;
function close(from){while(stack.length>from){var t=stack.pop();t.el.remove()}}
function open(trg,level){
 if(stack[level]&&stack[level].trg===trg)return;
 var html=tipHTML(trg.dataset.t);
 if(!html)return;
 close(level);
 var el=document.createElement("div");el.className="tip";el.innerHTML=html+'<span class="hint">'+(trg.tagName==="A"?"click opens · ":"click pins · ")+"Space locks · Esc clears</span>";
 document.body.appendChild(el);
 var r=trg.getBoundingClientRect(),w=el.offsetWidth,h=el.offsetHeight;
 var x=Math.min(Math.max(8,r.left),innerWidth-w-8),y=r.bottom+6;if(y+h>innerHeight-8)y=Math.max(8,r.top-h-6);
 el.style.left=x+"px";el.style.top=y+"px";el.dataset.level=level;
 if(locked)el.classList.add("pin");
 stack.push({trg:trg,el:el,pin:false});
}
function levelOf(node){var t=node.closest&&node.closest(".tip");return t?(+t.dataset.level+1):0}
document.addEventListener("mouseover",function(e){
 var trg=e.target.closest&&e.target.closest("[data-t]");
 var inTip=e.target.closest&&e.target.closest(".tip");
 clearTimeout(otimer);
 if(trg){clearTimeout(timer);var lv=levelOf(trg);
  if(locked&&lv<stack.length&&!inTip)return;   // locked: the open tips hold; new ones open only from inside them
  if(trg.tagName==="A"&&lv===0){otimer=setTimeout(function(){open(trg,lv)},220)}else open(trg,lv);return}
 if(inTip){clearTimeout(timer);if(!locked)close(+inTip.dataset.level+1);return}
 if(locked||!stack.length)return;
 clearTimeout(timer);timer=setTimeout(function(){var keep=0;stack.forEach(function(s,i){if(s.pin)keep=i+1});close(keep)},260);
});
document.addEventListener("focusin",function(e){var trg=e.target.closest&&e.target.closest("[data-t]");if(trg&&trg.tagName!=="A")open(trg,levelOf(trg))});
document.addEventListener("click",function(e){
 var trg=e.target.closest&&e.target.closest("[data-t]");
 if(trg&&trg.tagName!=="A"){e.preventDefault();var lv=levelOf(trg);open(trg,lv);if(stack[lv]){stack[lv].pin=!stack[lv].pin;stack[lv].el.classList.toggle("pin",stack[lv].pin||locked)}return}
 if(!(e.target.closest&&e.target.closest(".tip"))&&!trg){if(!locked)close(0)}
});
document.addEventListener("keydown",function(e){
 if(/^(INPUT|SELECT|TEXTAREA)$/.test(document.activeElement.tagName))return;
 if(e.key===" "&&stack.length){e.preventDefault();locked=!locked;stack.forEach(function(s){s.el.classList.toggle("pin",locked||s.pin)})}
 else if(e.key==="Escape"){locked=false;close(0)}
});
document.getElementById("mb").onclick=function(){var m=document.getElementById("meta").classList.toggle("on");this.setAttribute("aria-expanded",m)};
document.getElementById("built").textContent="built "+D.built;
rail();render();
})();
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Trope System</title>
<style>__CSS__</style>
</head>
<body>
<header>
<h1><a href="#/">Trope System</a></h1>
<input id="q" type="search" placeholder="Search names and definitions  ( / )" aria-label="Search tropes" autocomplete="off">
<span class="sp"></span>
<span class="st" id="built"></span>
<button id="mb" aria-expanded="false" aria-controls="meta">Info</button>
</header>
<div id="meta">
<p>BOLO 89 · the trope register as a browsable system. Built by _tools/tropes/build_glass.py (or <b>command tropes</b>), zero tokens, from _tools/tropes/data/domains/register.json and _tools/tropes/data/trope_graph.json. The doc: ShroomsQ/_CANON/_SSOT/01_NARRATIVE_FRAMEWORKS/ssot_01_trope_register.md.</p>
<p>Layer names and one-line meanings come from each system's SSOT doc (character ssot_02 · setting ssot_03 · genre and texture ssot_01 · theme ssot_06 · tracking ssot_08 · style ssot_07.1 and 07.3). Sexuality keys onto the character layers.</p>
<p>Counts are live from register.json (rebuilt 10/05). The SSOT doc's count table (v0.5.0, 10/03) predates the re-key and reads older numbers.</p>
<p>Links to pages outside the register are dropped at build. Dotted words open a tip: click pins it (links open), Space locks the open tips, Esc clears. Press / to search.</p>
</div>
<div class="wrap">
<nav aria-label="Domains and layers"></nav>
<main></main>
</div>
<script type="application/json" id="tg-data">__DATA__</script>
<script>__JS__</script>
</body>
</html>
"""


def main(argv):
    dry = "--dry-run" in argv
    s = build(write=not dry)
    if "--json" in argv:
        print(json.dumps(s, indent=1, ensure_ascii=False))
    elif dry:
        print("would write %s · %.2f MB · %d tropes" % (s["page"], s["mb"], s["tropes"]))
    else:
        print(("tropes glass: %s · %.2f MB · %s tropes · %s no definition · %s low · %s multi-domain · %s in the plot graph"
               % (os.path.relpath(s["page"], ROOT), s["mb"], format(s["tropes"], ","), format(s["no_def"], ","),
                  format(s["low"], ","), format(s["multi"], ","), s["plot"])) if s["ok"] else "tropes glass: " + s.get("error", "failed"))
    return 0 if s["ok"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
