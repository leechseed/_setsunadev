"""build_editor_library.py — 10/30: the glass page of books behind the eight OXO script editors.
Writes _tools/pages/oxo-editor-library.html. W = wired into the agent file today, D = distilled (in KNOWLEDGE_AREAS),
N = in the catalog, not distilled. Run: python -X utf8 _tools/pages/build_editor_library.py
"""
import html
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CAT = {b["id"]: b for b in json.load(open(os.path.join(ROOT, "_0.1_BVX_LEARN/_meta/catalog.json"), encoding="utf8"))}
DONE = {f[:-3] for f in os.listdir(os.path.join(ROOT, "_0.1_BVX_LEARN/KNOWLEDGE_AREAS"))}

# seat -> (lens, wired ids, add ids with a one-line why)
SEATS = [
    ("editing-structure", "Act shape, turning points, pacing, setups and payoffs",
     ["0163", "0175", "0193", "1124", "0236", "1123", "1126", "0054", "0089"],
     [("0092", "screenplay act structure, the closest match to a script"),
      ("0176", "structure for film and TV, first word to last frame"),
      ("0136", "suspense, structure and plot"),
      ("0195", "the architecture of a scene and a story, technical"),
      ("1046", "the transformational arc as the spine"),
      ("0043", "twenty plot shapes to name what the script is doing"),
      ("0169", "outline method, to rebuild the shape from the pages"),
      ("0053", "structures that break the Hollywood formula"),
      ("0565", "how a long series stacks arcs (the Outliers is a series)"),
      ("0250", "TV act and episode shape"), ("0262", "writing for TV, series beats")]),
    ("editing-character", "Want vs need, arcs, motivation, choices, consistency",
     ["0045", "0064", "0075", "0196", "0233", "0209", "0061", "0273", "1123"],
     [("0057", "characterization toolkit"),
      ("0122", "hero growth and transformation"),
      ("0207", "tools to develop characters and cause scenes"),
      ("0062", "character, scene and story"),
      ("0047", "supporting roles with purpose"),
      ("0264", "villain craft"), ("0265", "writing about villains"),
      ("0255", "how a character reads on screen"),
      ("0290", "youth subcultures in fiction and film (school-age cast)")]),
    ("editing-dialogue", "Voice, subtext, on-the-nose lines, exposition, rhythm",
     ["0084", "0175", "0279", "0196"],
     [("0121", "dazzling dialogue, the fast fix for a manuscript"),
      ("0267", "hooks in dialogue and foreshadowing"),
      ("0062", "dialogue inside the scene"),
      ("0207", "subtext tools")]),
    ("editing-theme-tone", "What it is about underneath, tone, motifs, genre promises",
     ["0191", "0576", "0580", "0581", "0279", "0175", "0841", "1124", "0236"],
     [("0068", "conventions and obligatory moments, what the audience expects"),
      ("0049", "action as a genre"), ("0050", "action as an art of excitement"),
      ("0577", "genre from iconography to ideology"),
      ("0578", "film genre, Hollywood and beyond"), ("0579", "film genre reader"),
      ("0142", "how popular film names its genres"), ("1021", "cinema genre"),
      ("0281", "scary scenes, tone control"), ("0840", "why horror works"),
      ("0290", "youth subcultures in fiction and film"),
      ("0614", "Todorov on the fantastic"), ("0599", "rhetorics of fantasy")]),
    ("editing-continuity", "Timeline, who-knows-what, names, props, world rules",
     ["0100", "0458", "0141", "0596", "0598"],
     [("0562", "building imaginary worlds"), ("0575", "exploring imaginary worlds"),
      ("0630", "companion to imaginary worlds"),
      ("0167", "Chatman, story and discourse in fiction and film"),
      ("0563", "characters in fictional worlds"),
      ("0654", "unnatural narratology, for time that breaks the rules")]),
    ("editing-line", "Action-line economy, scene headings, format, readability",
     [],
     [("0159", "revision and self-editing, the cut-and-tighten method"),
      ("0188", "the 21st-century screenplay, current format and style"),
      ("0228", "the process of screenwriting"),
      ("0221", "the nutshell technique, scene by scene"),
      ("0201", "the coffee-break screenwriter, page-sized drills"),
      ("0267", "active hooks and description"),
      ("0056", "active setting, how to describe fast"),
      ("0081", "description and setting"),
      ("0200", "copyediting fiction, house rules on consistency")]),
    ("editing-production", "Cost and demand to shoot or animate; the cheapest way to the same beat",
     [],
     [("0013", "film production management, the budget view"),
      ("1036", "directing fundamentals, see the film before shooting"),
      ("1054", "master shots, 100 setups and what each costs"),
      ("0066", "cinematic storytelling for directors and cinematographers"),
      ("0197", "the art of cinematic storytelling"),
      ("1103", "the visual story, structure in images"),
      ("1090", "the language of the lens"),
      ("1047", "layout and composition for animation"),
      ("0255", "costume and look as story"),
      ("0868", "digital compositing, what effects shots take")]),
    ("reading-cold", "A first-time reader's honest coverage, no canon",
     [],
     [("1093", "Ebert's Hollywood clichés, the checklist a cold reader needs"),
      ("1076", "Ebert, how a working critic judges"),
      ("0044", "twenty-seven fiction blunders"),
      ("0159", "revision and self-editing"),
      ("0094", "conflict and suspense"),
      ("0565", "complex TV, how long stories hold a viewer")]),
]
GAPS = [
    "A screenplay format manual (Trottier's Screenwriter's Bible, Riley's Hollywood Standard). Nothing in the library covers scene headings and parentheticals directly; editing-line leans on Aronson and Bell.",
    "A script-coverage guide (how readers rate and pass on scripts). reading-cold has Ebert's clichés but no book on coverage.",
    "Adaptation and teen-ensemble drama craft (the Outliers is a school ensemble). Only Youth Subcultures (0290) comes near.",
    "Animation production and storyboarding for the cost seat. The library has Layout and Composition for Animation (1047) and no budget book for animation.",
]


def title(i):
    b = CAT.get("BVX." + i)
    if not b:
        return "(not in catalog)", ""
    t = b["t"].split(" 97")[0]
    return t[:88], (b.get("a") or "")[:34]


def row(i, why, kind):
    t, a = title(i)
    tag = {"W": "WIRED", "D": "READY", "N": "DISTILL"}[kind]
    pg = CAT.get("BVX." + i, {}).get("pages")
    pgs = f" · {pg}p" if pg else ""
    return (f'<li class="k{kind}"><span class="tag">{tag}</span><span class="id">BVX.{i}</span>'
            f'<span class="t">{html.escape(t)}</span><span class="a">{html.escape(a)}{pgs}</span>'
            f'<span class="w">{html.escape(why)}</span></li>')


cards, need = [], []
for seat, lens, wired, add in SEATS:
    lis = []
    for i in wired:
        lis.append(row(i, "in the agent file", "W"))
    for i, why in add:
        agent = open(os.path.join(ROOT, ".claude", "agents", seat + ".md"), encoding="utf8").read()
        kind = "W" if f"BVX.{i} " in agent else ("D" if "BVX." + i in DONE else "N")
        lis.append(row(i, why, kind))
        if kind == "N":
            need.append(i)
    nw = len(wired)
    nn = sum(1 for i, _ in add if "BVX." + i not in DONE)
    cards.append(f'<section><h2>{seat} <small>{html.escape(lens)}</small></h2>'
                 f'<p class="n">{nw} wired · {len(add)} recommended ({nn} still need the distill)</p><ul>{"".join(lis)}</ul></section>')
uniq = sorted(set(need))
gap = "".join(f"<li>{html.escape(g)}</li>" for g in GAPS)
page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>OXO Editor Library</title><style>
:root{{--bg:#111;--panel:#1a1a1a;--line:#2e2e2e;--fg:#e8e6e1;--mut:#9b978f;--or:#FF5A1F}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.45 system-ui,sans-serif}}
header{{position:sticky;top:0;height:44px;display:flex;align-items:center;gap:16px;padding:0 16px;background:#0b0b0b;border-bottom:1px solid var(--line);z-index:2}}
header b{{color:var(--or)}}header span{{color:var(--mut);font-size:13px}}
main{{max-width:1100px;margin:0 auto;padding:16px}}
section{{background:var(--panel);border:1px solid var(--line);border-radius:8px;margin:0 0 16px;padding:14px 16px}}
h2{{margin:0;font-size:18px;color:var(--or)}}h2 small{{display:block;color:var(--mut);font-size:13px;font-weight:400}}
.n{{margin:4px 0 8px;color:var(--mut);font-size:13px}}ul{{list-style:none;margin:0;padding:0}}
li{{display:grid;grid-template-columns:70px 78px 1fr;gap:2px 10px;padding:6px 0;border-top:1px solid var(--line)}}
.tag{{font-size:11px;font-weight:700;letter-spacing:.05em;padding:2px 6px;border-radius:4px;align-self:start;text-align:center}}
.kW .tag{{background:#2a3a24;color:#9fdc86}}.kD .tag{{background:#3a2e14;color:#f0c060}}.kN .tag{{background:#3a1d12;color:var(--or)}}
.id{{color:var(--mut);font-size:13px;font-variant-numeric:tabular-nums}}.t{{font-weight:600}}
.a,.w{{grid-column:3;color:var(--mut);font-size:13px}}.w{{color:var(--fg);opacity:.85}}
.sum{{display:flex;gap:16px;flex-wrap:wrap;margin:0 0 16px}}.sum div{{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:10px 14px}}
.sum b{{font-size:22px;color:var(--or);display:block}}
.gaps li{{display:list-item;list-style:disc;margin-left:20px;border:0;padding:3px 0}}
@media(max-width:600px){{li{{grid-template-columns:62px 1fr}}.id{{grid-column:2}}.t,.a,.w{{grid-column:1/-1}}}}
</style></head><body>
<header><b>OXO EDITOR LIBRARY</b><span>8 script editors · books behind each lens</span></header><main>
<div class="sum"><div><b>{sum(1 for s in SEATS for i in [x for x,_ in s[3]]+list(s[2]) if 'BVX.'+i in DONE)}</b>wired today</div><div><b>{len(uniq)}</b>to distill (unique)</div>
<div><b>{sum(1 for s in SEATS for i,_ in s[3] if 'BVX.'+i in DONE)}</b>ready to wire</div><div><b>3</b>seats with no book yet</div></div>
<p style="color:var(--mut)">WIRED = in the agent file now. READY = already distilled, add the line to the agent. DISTILL = in the library but not yet distilled; the distill order turns each into a KNOWLEDGE_AREAS entry the editors can read. Books are evidence, not verdicts.</p>
{"".join(cards)}
<section class="gaps"><h2>Not in the library <small>worth finding, Chief attaches the PDF in Zotero</small></h2><ul>{gap}</ul></section>
<section><h2>Distill order <small>{len(uniq)} books, paste-ready</small></h2><p class="n">{" · ".join("BVX."+i for i in uniq)}</p></section>
</main></body></html>"""
out = os.path.join(ROOT, "_tools", "pages", "oxo-editor-library.html")
open(out, "w", encoding="utf8").write(page)
print(out, len(uniq), "to distill")
