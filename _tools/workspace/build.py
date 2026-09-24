#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BOLO 79 · MS-UI build — the story workspace, one page, three lenses
(Fabula / Rails / Told) over OXO's plot system, filled with real data.

Reads:
  ShroomsQ/_CANON/_SSOT/04_PLOT_SYSTEMS/ssot_04_fabula.md      (THE INSTANCE, THE WORLD CLOCK)
  ShroomsQ/_CANON/_SSOT/04_PLOT_SYSTEMS/ssot_04_plot_system.md (THE INSTANCE, M2 row 9)
  _tools/tropes/data/trope_graph.json                          (135 nodes, tropes, edges)
  _tools/bolostatus/work/77/tropes/PS-R.rails.md                (throughlines, signpost structure)
  _tools/sitrep/glossary.json                                   (existing terms; bolo77)

Writes:
  _tools/workspace/out/workspace.html  (page content only — no doctype/html/head/body)
"""
import json
import re
import sys
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[2]
FABULA_MD = ROOT / "ShroomsQ/_CANON/_SSOT/04_PLOT_SYSTEMS/📐 ssot_04_fabula.md"
PLOT_MD = ROOT / "ShroomsQ/_CANON/_SSOT/04_PLOT_SYSTEMS/📐 ssot_04_plot_system.md"
TROPE_JSON = ROOT / "_tools/tropes/data/trope_graph.json"
RAILS_MD = ROOT / "_tools/bolostatus/work/77/tropes/PS-R.rails.md"
GLOSSARY_JSON = ROOT / "_tools/sitrep/glossary.json"
OUT = Path(__file__).resolve().parent / "out" / "workspace.html"

MISSING = []  # sources we could not find / had to skip — reported at the end


def read(path: Path) -> str:
    if not path.exists():
        MISSING.append(str(path))
        return ""
    return path.read_text(encoding="utf-8")


def need(haystack: str, needle: str, label: str):
    """Assert a verbatim quote is still present in the source text we read,
    so this build fails loudly instead of silently drifting from canon."""
    if needle not in haystack:
        raise SystemExit(f"SOURCE DRIFT: {label!r} no longer found verbatim in source — rebuild the extract.")


# ---------------------------------------------------------------- FABULA ---

fabula_md = read(FABULA_MD)

import yaml  # noqa: E402

def extract_instance_events(md: str):
    """Pull every ```yaml fenced block inside THE INSTANCE section."""
    m = re.search(r"## THE INSTANCE\b(.*?)\n---\n", md, re.S)
    if not m:
        MISSING.append("THE INSTANCE block in ssot_04_fabula.md")
        return []
    body = m.group(1)
    blocks = re.findall(r"```yaml\n(.*?)```", body, re.S)
    out = []
    for b in blocks:
        try:
            out.append(yaml.safe_load(b))
        except yaml.YAMLError:
            pass
    return out


fabula_events = extract_instance_events(fabula_md)

# THE WORLD CLOCK eras — prose, not YAML; quoted verbatim from the file,
# each quote checked against the loaded text so drift breaks the build.
_era_red_stick = "Red Stick Creek (founding, buried, no date given)"
_era_red_hills = "Red Hills (the first rename, reach roughly a century before the Bishop acquisition, extent unstated)"
_era_dcus = "DCUS (the current era, tied to the Bishop acquisition"
for q in (_era_red_stick, _era_red_hills, _era_dcus):
    need(fabula_md, q.split(" (")[0], f"world-clock era: {q}")

WORLD_CLOCK_ERAS = [
    {
        "id": "era_red_stick_creek",
        "label": "Red Stick Creek",
        "note": "founding, buried — no date given",
        "detail": "100+ years of private prestige; the founding name sanded to “Red Hills” a century before the Bishops arrived. No calendar date exists for this transition.",
        "order": 0,
    },
    {
        "id": "era_red_hills",
        "label": "Red Hills",
        "note": "the first rename — reach roughly a century before the Bishop acquisition, extent unstated",
        "detail": "The rename lattice: Red Stick Creek → Red Hills → DCUS — erasure done twice.",
        "order": 1,
    },
    {
        "id": "era_dcus",
        "label": "DCUS",
        "note": "the current era — tied to the Bishop acquisition",
        "detail": "Prestige converted to product; the ownership war — grandfather vs son — sold for spoils to the Bishops.",
        "order": 2,
    },
]

# ------------------------------------------------------------ PLOT / TOLD ---

plot_md = read(PLOT_MD)
need(plot_md, "OXO.primary.M2.q1.s3", "THE INSTANCE, M2 row 9 — P1 ADDRESS")
need(plot_md, "signpost 1, The Past", "P6 SIGNPOST/JOURNEY SEAT (re-seated 9/24)")

TOLD_SCENE = {
    "id": "oxo_primary_m2_q1_s3",
    "address": "OXO.primary.M2.q1.s3",
    "movement": "M2",
    "throughline": "MC",
    "signpost": "Signpost 1 · The Past (re-seated 9/24)",
    "collision": "L9×S9 (seed), Eros × Allure, trine-as-trap — echoes row 6, seeds row 8",
    "value_turn": "whole minus → plus for Tori (her read); owned plus → minus underneath (the audience's read) — ironic charge",
    "driver": "Decision, local to the CR beat: reach vs pull out (does not override the story-level ruled Driver = Action)",
    "reveal": "To the audience: the hook is a trap, dramatic irony. To Tori: nothing yet — she reads it as a win.",
    "order_told_vs_happened": "order told = order happened, no reordering; duration = scene (1:1), one licensed stretch at the sync",
    "fabula_event": "m2_grief_outbursts",
    "source": "oxo-scene-card-M2-row9.md, via ssot_04_plot_system.md THE INSTANCE",
}

# ------------------------------------------------------------------ RAILS ---

rails_md = read(RAILS_MD)
need(rails_md, "THEY", "OS throughline perspective")
need(rails_md, "16 signposts across all four throughlines", "signpost count")

THROUGHLINES = [
    {"id": "OS", "name": "Overall Story", "pov": "THEY", "role": "the problem among everyone — “the A-plot,” McKee's arch-plot, the external genre"},
    {"id": "MC", "name": "Main Character", "pov": "I", "role": "the problem from inside one skin — the hero's journey, McKee's Character lines"},
    {"id": "IC", "name": "Influence Character", "pov": "YOU", "role": "the perspective that pressures the MC to change — mentor/shadow/love interest"},
    {"id": "RS", "name": "Relationship Story", "pov": "WE", "role": "the argument between MC and IC — “the B-story,” the internal genre"},
]
ACTS = [1, 2, 3, 4]

# the movements map, RULED 9/24 (the Bourne pivot): all 16 signpost values from
# oxo-storyform.md §9 after the 8/24 rotation; M2 row 9 is the one carded scene (MC · 1)
ACT_MOVEMENTS = {1: "M1 + M2", 2: "M3", 3: "M4 + M5", 4: "M6"}
_SP = {
    "MC": ["The Past", "The Present", "How Things are Changing", "The Future"],
    "OS": ["Conceiving an Idea", "Developing a Plan", "Playing a Role", "Changing One's Nature"],
    "IC": ["Impulsive Responses", "Innermost Desires", "Contemplation", "Memories"],
    "RS": ["Obtaining", "Understanding", "Doing", "Gathering Information"],
}
SIGNPOST_FILL = {}
for tl, vals in _SP.items():
    for a, v in enumerate(vals, 1):
        SIGNPOST_FILL[(tl, a)] = {
            "state": "storyform", "label": f"Signpost {a} · {v}", "movement": ACT_MOVEMENTS[a],
            "detail": f"{tl} signpost {a}: {v}. Recorded in oxo-storyform.md §9 (after the 8/24 rotation); seated at {ACT_MOVEMENTS[a]} by the movements map ruled 9/24. No scene carded here yet.",
        }
SIGNPOST_FILL[("MC", 1)].update({
    "state": "carded", "told_id": TOLD_SCENE["id"],
    "detail": "MC signpost 1: The Past, Act 1 (M1 + M2). The one carded scene sits here: M2 row 9, re-seated 9/24 from a pre-rotation label.",
})

trope_data = json.loads(read(TROPE_JSON) or "{}")
raw_nodes = trope_data.get("nodes", [])
raw_tropes = trope_data.get("tropes", [])

PHASE_TO_COLUMN = {"beginning": "act1", "middle": "act2_3", "end": "act4", "any": "side"}
COLUMN_LABEL = {
    "act1": "Act 1 · beginning",
    "act2_3": "Acts 2–3 · middle",
    "act4": "Act 4 · end",
    "side": "Side tray · any phase",
}

def trim(s, n):
    if not s:
        return s
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"

tropes_by_node = {}
for t in raw_tropes:
    tropes_by_node.setdefault(t.get("node"), []).append(
        {
            "slug": t.get("slug"),
            "name": t.get("name"),
            "def": trim(t.get("def", ""), 160),
            "alt": t.get("alt"),
            "conf": t.get("conf"),
        }
    )

RAILS_NODES = []
for n in raw_nodes:
    nid = n["id"]
    RAILS_NODES.append(
        {
            "id": nid,
            "family": n.get("family"),
            "n": n.get("n"),
            "name": n.get("name"),
            "def": trim(n.get("def", ""), 200),
            "cite": n.get("cite"),
            "bvx": n.get("bvx"),
            "phase": n.get("phase"),
            "column": PHASE_TO_COLUMN.get(n.get("phase"), "side"),
            "same_as": n.get("same_as", []),
            "tropeCount": n.get("tropes", 0),
            "tropes": tropes_by_node.get(nid, []),
        }
    )

# -------------------------------------------------------------- GLOSSARY ---

glossary_raw = json.loads(read(GLOSSARY_JSON) or "{}")
GLOSSARY = {}
if "bolo77" in glossary_raw:
    GLOSSARY["bolo77"] = glossary_raw["bolo77"]

# terms not carried in the standing glossary — short definitions sourced only
# from the three plot docs read for this build, per the tasking order.
need(fabula_md, "logically and chronologically related events that are caused or experienced by actors", "fabula def")
need(fabula_md, "split out from the told-order half that already lives in", "syuzhet def")
need(plot_md, "consumes a fixed structural checkpoint, one per throughline, four per form", "signpost def")
need(rails_md, "No rival model has all four", "throughline def")
need(rails_md, "A trope names a recurring pattern", "trope def")
need(fabula_md, "several portions taken as if they were alike and to some extent repetitive", "repeat def")

GLOSSARY.update(
    {
        "fabula": {
            "t": "Fabula",
            "k": "noun",
            "d": "The universe-level world-time layer: “a series of logically and chronologically related events... caused or experienced by actors” (Bal 2017: 5). One fabula sits under both OXO and EVIL CHECK.",
            "w": "ssot_04_fabula.md",
        },
        "syuzhet": {
            "t": "Syuzhet",
            "k": "noun",
            "d": "The told-order half of the fourth top-layer model, split out from this world-order half (the fabula). Owns P11 TIME — order_told vs order_happened.",
            "w": "ssot_04_plot_system.md",
        },
        "signpost": {
            "t": "Signpost",
            "k": "noun",
            "d": "A fixed structural checkpoint, one per throughline, four per form (Dramatica's Signpost). 16 across the whole form.",
            "w": "ssot_04_plot_system.md · Axis 3 FUNCTION",
        },
        "throughline": {
            "t": "Throughline",
            "k": "noun",
            "d": "One of Dramatica's four perspectives on a story — OS (they), MC (I), IC (you), RS (we). No rival model has all four.",
            "w": "PS-R.rails.md §1",
        },
        "trope": {
            "t": "Trope",
            "k": "noun",
            "d": "A recurring pattern — what happens at one plot-ladder rung (beat/scene/sequence/act/story) or across a span of units.",
            "w": "PS-R.rails.md §5",
        },
        "node": {
            "t": "Node (trope graph)",
            "k": "noun",
            "d": "A book-derived structural unit in the trope graph — one of 135 seated from five story-grammar families (Tobias, Schmidt, Campbell, Vogler, Propp). Tropes attach inside a node; the node is what draws on the rails.",
            "w": "_tools/tropes/data/trope_graph.json",
        },
        "repeat": {
            "t": "Repeat / iterative",
            "k": "noun",
            "d": "One record standing for a repeated class rather than one row per occurrence — “not a single portion of elapsed time but... several portions taken as if they were alike and to some extent repetitive” (Genette 1980: 53). The fabula's `repeat` flag.",
            "w": "ssot_04_fabula.md · THE WORLD CLOCK",
        },
    }
)

# --------------------------------------------------------- ORIGIN MOMENTS ---

ORIGIN_LAYERS = [
    {"layer": "L5", "name": "WOUND", "needs": True, "event": "m1b_crash_jebb_death", "note": "“Assigned during character history entry. This is a record of what happened, not a choice.”"},
    {"layer": "L7", "name": "ORIGIN", "needs": True, "event": None, "note": "Pre-M1B racing career feeds this layer as background condition — not filled as a fabula event; Bal's definition rules a state that never changes on record out of the event schema."},
    {"layer": "L8", "name": "IMPRINT", "needs": True, "event": None, "note": "No datable antecedent filled in this wave's instance — gap, not omission."},
    {"layer": "L9", "name": "EROS", "needs": True, "event": None, "note": "No datable antecedent filled in this wave's instance — gap, not omission."},
    {"layer": "L10", "name": "SHADOW", "needs": True, "event": None, "note": "No datable antecedent filled in this wave's instance — gap, not omission."},
]

# ------------------------------------------------------------- ASSEMBLE ---

DATA = {
    "fabula": {
        "events": fabula_events,
        "eras": WORLD_CLOCK_ERAS,
    },
    "told": {
        "scene": TOLD_SCENE,
    },
    "rails": {
        "throughlines": THROUGHLINES,
        "acts": ACTS,
        "fill": {f"{k[0]}|{k[1]}": v for k, v in SIGNPOST_FILL.items()},
        "actMov": ACT_MOVEMENTS,
        "nodes": RAILS_NODES,
        "columns": COLUMN_LABEL,
    },
    "glossary": GLOSSARY,
    "character": {
        "id": "victoria_midnight",
        "name": "Victoria Midnight",
        "alias": "Tori",
        "thesis": "“I will become untouchable.” — the closed resolve, M1B, immediately post-crash",
        "age_health": "age unspecified in canon",
        "origin_layers": ORIGIN_LAYERS,
    },
    "counts": {
        "rails_nodes": len(RAILS_NODES),
        "rails_tropes": len(raw_tropes),
        "fabula_events": len(fabula_events),
    },
}

DATA_JSON = json.dumps(DATA, ensure_ascii=False).replace("</script>", "<\\/script>")

# ------------------------------------------------------------------ HTML ---

STYLE = r"""
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
  /* ---- tokens, lifted from SITREP.html: the Command's own palette (RULED 9/10 default colorway, 9/11 dark-only) ---- */
  :root {
    --bg: #0F1216; --panel: #171B21; --panel-2: #1F242C;
    --ink: #E8EAEE; --ink-2: #A9B0BC; --ink-3: #7B8492;
    --accent: #FF6B35; --accent-ink: #FF8F62; --accent-soft: #3A2117;
    --link: #FF8F62; --good: #5CC48A; --good-soft: #16301F; --warn: #D9C48A; --warn-soft: #3A3320; --bad: #E9788A; --bad-soft: #3A1B20; --help: #A9B0BC;
    --mark: #3A3320;
    --line: #2B313B; --line-2: #3C4452;
    --grid: color-mix(in srgb, var(--ink) 8%, transparent);
    --shadow: 0 1px 2px rgba(0,0,0,.4), 0 8px 24px rgba(0,0,0,.35);
    --display: "Barlow Condensed", "Arial Narrow", "Helvetica Neue", Arial, sans-serif;
    --body: "Atkinson Hyperlegible", "Segoe UI", Verdana, sans-serif;
    --mono: "IBM Plex Mono", "SFMono-Regular", Consolas, "Liberation Mono", monospace;
    color-scheme: dark;
  }
  :root[data-theme="light"] {
    --bg: #D8D8D2; --panel: #E4E4DE; --panel-2: #CBCBC4;
    --ink: #1B1B19; --ink-2: #44453F; --ink-3: #6B6C65;
    --accent: #E04E18; --accent-ink: #A83409; --accent-soft: #E9D5CA;
    --link: #A83409; --good: #1F6B45; --good-soft: #CFE0D3; --warn: #5E4F22; --warn-soft: #E2D9BE; --bad: #962C37; --bad-soft: #E6CCCF; --help: #44453F;
    --mark: #E2D9BE;
    --line: #B5B5AE; --line-2: #97978F;
    --shadow: 0 1px 2px rgba(0,0,0,.08), 0 8px 24px rgba(0,0,0,.10);
    color-scheme: light;
  }
  * { box-sizing: border-box; }
  html, body { height: 100%; }
  body {
    margin: 0; background: var(--bg); color: var(--ink);
    background-image: radial-gradient(var(--grid) 1px, transparent 1px);
    background-size: 22px 22px;
    font-family: var(--body); font-size: 16px; line-height: 1.5;
    -webkit-font-smoothing: antialiased;
    overflow: hidden;
  }
  a { color: var(--link); }
  button { font: inherit; color: inherit; background: none; border: 0; cursor: pointer; }
  button:focus-visible, .t:focus-visible, .ol-row:focus-visible, .node-chip:focus-visible, .sig-cell:focus-visible, input:focus-visible {
    outline: 2px solid var(--accent); outline-offset: 2px;
  }
  ::selection { background: var(--mark); }
  .mono { font-family: var(--mono); }
  .lbl { font-family: var(--mono); font-size: 10.5px; letter-spacing: .12em; text-transform: uppercase; color: var(--ink-3); }
  .hint { font-family: var(--mono); font-size: 11px; color: var(--ink-3); }

  /* ---- concept links (CK3 R1) ---- */
  .t { color: var(--link); text-decoration: none; border-bottom: 1px dotted color-mix(in srgb, var(--link) 55%, transparent); cursor: help; }
  .t:hover, .t.on { border-bottom-style: solid; }

  /* ---- app frame ---- */
  .app {
    height: 100%; display: grid;
    grid-template-rows: auto minmax(0,1fr) auto;
    grid-template-columns: 210px minmax(0,1fr) 320px;
    grid-template-areas: "head head head" "ol canvas detail" "log log log";
  }
  header.head {
    grid-area: head; display: flex; align-items: center; gap: 0; border-bottom: 1px solid var(--line-2);
    background: color-mix(in srgb, var(--panel) 85%, transparent); flex-wrap: wrap;
  }
  .brand { display: flex; align-items: center; gap: 8px; padding: 10px 16px; border-right: 1px solid var(--line); }
  .brand i { width: 10px; height: 10px; background: var(--accent); display: inline-block; }
  .brand b { font-family: var(--display); font-weight: 800; font-size: 22px; text-transform: uppercase; letter-spacing: .02em; }
  nav.lenses { display: flex; gap: 0; }
  nav.lenses button { font-family: var(--display); font-weight: 700; font-size: 15px; text-transform: uppercase; letter-spacing: .03em; padding: 12px 18px; border-right: 1px solid var(--line); color: var(--ink-2); }
  nav.lenses button .k { display: block; font-family: var(--mono); font-size: 9.5px; color: var(--ink-3); letter-spacing: .1em; }
  nav.lenses button:hover { color: var(--ink); background: var(--panel-2); }
  nav.lenses button.on { color: var(--accent); background: var(--panel-2); box-shadow: inset 0 -3px 0 var(--accent); }
  .headspace { flex: 1 1 auto; }
  .char-btn { font-family: var(--display); font-weight: 700; font-size: 14px; text-transform: uppercase; padding: 8px 16px; border-left: 1px solid var(--line); color: var(--ink-2); }
  .char-btn:hover, .char-btn.on { color: var(--accent); }
  .ol-toggle, .detail-toggle { display: none; font-family: var(--mono); font-size: 12px; padding: 8px 12px; border-left: 1px solid var(--line); color: var(--ink-2); }

  /* ---- outliner (left rail, CK3 R12) ---- */
  aside.ol { grid-area: ol; border-right: 1px solid var(--line-2); overflow-y: auto; padding: 12px 0 16px; background: color-mix(in srgb, var(--panel) 55%, transparent); }
  .ol h4 { margin: 14px 14px 4px; font-family: var(--mono); font-size: 10.5px; letter-spacing: .12em; text-transform: uppercase; color: var(--ink-3); }
  .ol h4:first-child { margin-top: 4px; }
  .ol-row { display: block; width: 100%; text-align: left; padding: 6px 14px; font-size: 14px; color: var(--ink-2); border-left: 2px solid transparent; }
  .ol-row:hover { background: var(--panel-2); color: var(--ink); }
  .ol-row.on { color: var(--ink); border-left-color: var(--accent); background: var(--panel-2); font-weight: 700; }
  .ol-row small { display: block; font-family: var(--mono); font-size: 10.5px; color: var(--ink-3); }

  /* ---- canvas ---- */
  main.canvas { grid-area: canvas; overflow: auto; padding: 18px 20px 24px; min-width: 0; }
  main.canvas h2 { margin: 0 0 4px; font-family: var(--display); font-weight: 800; font-size: 26px; text-transform: uppercase; letter-spacing: .02em; }
  main.canvas .sub { margin: 0 0 16px; font-size: 14px; color: var(--ink-2); max-width: 72ch; }
  .lens-view { display: none; }
  .lens-view.on { display: block; }

  /* ---- fabula timeline ---- */
  .fab-scroll { overflow-x: auto; padding-bottom: 6px; }
  .fab-track { position: relative; min-width: 760px; height: 260px; }
  .era-band { position: absolute; top: 30px; height: 90px; border: 1px dashed var(--line-2); background: color-mix(in srgb, var(--accent) 6%, transparent); border-radius: 3px; }
  .era-band .lbl2 { position: absolute; top: -20px; left: 6px; font-family: var(--display); font-weight: 700; font-size: 14px; text-transform: uppercase; color: var(--ink-2); }
  .era-band .fz { position: absolute; bottom: 6px; left: 6px; right: 6px; font-family: var(--mono); font-size: 10px; color: var(--ink-3); }
  .movement-axis { position: absolute; top: 150px; left: 0; right: 0; height: 2px; background: var(--line-2); }
  .movement-axis .tick { position: absolute; top: -4px; width: 1px; height: 10px; background: var(--line-2); }
  .movement-axis .tick span { position: absolute; top: 12px; left: -12px; font-family: var(--mono); font-size: 11px; color: var(--ink-3); }
  .ev-dot { position: absolute; top: 138px; width: 22px; height: 22px; margin-left: -11px; border-radius: 50%; background: var(--panel); border: 2px solid var(--accent); display: grid; place-items: center; }
  .ev-dot::after { content: ""; width: 8px; height: 8px; border-radius: 50%; background: var(--accent); }
  .ev-dot.on { box-shadow: 0 0 0 4px color-mix(in srgb, var(--accent) 30%, transparent); }
  .ev-dot.repeat { border-style: dashed; }
  .ev-label { position: absolute; top: 168px; width: 150px; margin-left: -75px; text-align: center; font-size: 12px; color: var(--ink-2); }
  .fab-legend { margin-top: 8px; }

  /* ---- rails grid ---- */
  .rails-toolbar { display: flex; align-items: center; gap: 14px; flex-wrap: wrap; margin-bottom: 14px; }
  .rails-toolbar input[type=text] { font: 14px var(--body); padding: 6px 10px; border: 1px solid var(--line-2); background: var(--panel); color: var(--ink); min-width: 180px; }
  .fam-filter { display: flex; gap: 6px; flex-wrap: wrap; }
  .fam-filter button { font-family: var(--mono); font-size: 10.5px; letter-spacing: .08em; text-transform: uppercase; padding: 4px 9px; border: 1px solid var(--line-2); color: var(--ink-2); }
  .fam-filter button.on { border-color: var(--accent); color: var(--accent); }
  .explore-toggle { display: flex; align-items: center; gap: 6px; font-family: var(--mono); font-size: 11px; color: var(--ink-3); margin-left: auto; }
  .explore-toggle input { accent-color: var(--ink-3); }

  .signpost-grid { display: grid; grid-template-columns: 130px repeat(4, minmax(150px,1fr)); gap: 6px; min-width: 760px; margin-bottom: 22px; }
  .sp-corner { }
  .sp-act-hd { font-family: var(--mono); font-size: 10.5px; letter-spacing: .1em; text-transform: uppercase; color: var(--ink-3); align-self: end; padding: 4px 6px; }
  .sp-row-hd { display: flex; flex-direction: column; justify-content: center; font-family: var(--display); font-weight: 800; font-size: 16px; text-transform: uppercase; padding: 8px; }
  .sp-row-hd small { font-family: var(--mono); font-size: 9.5px; color: var(--ink-3); font-weight: 400; text-transform: none; letter-spacing: 0; }
  .sig-cell { min-height: 64px; border: 1px solid var(--line-2); border-radius: 3px; padding: 8px; text-align: left; font-size: 12.5px; color: var(--ink-3); background: var(--panel); }
  .sig-cell.empty { border-style: dashed; opacity: .55; cursor: default; }
  .sig-cell.filled { border-color: var(--accent); background: var(--accent-soft); color: var(--ink); cursor: pointer; }
  .sig-cell.filled b { display: block; font-family: var(--display); font-size: 13.5px; color: var(--accent-ink); text-transform: none; }
  .sig-cell.on { box-shadow: 0 0 0 3px color-mix(in srgb, var(--accent) 40%, transparent); }
  .sig-chip { display: inline-block; margin-top: 4px; font-family: var(--mono); font-size: 9.5px; padding: 1px 6px; border: 1px solid currentColor; color: var(--good); }
  .sig-chip.gap { color: var(--ink-3); }

  .node-cols { display: grid; grid-template-columns: repeat(4, minmax(180px, 1fr)); gap: 14px; min-width: 760px; }
  .node-col h3 { margin: 0 0 4px; font-family: var(--display); font-weight: 700; font-size: 15px; text-transform: uppercase; }
  .node-col .cnt { font-family: var(--mono); font-size: 10.5px; color: var(--ink-3); margin-bottom: 8px; }
  .node-cluster { display: flex; flex-wrap: wrap; gap: 6px; max-height: 420px; overflow-y: auto; padding-right: 4px; }
  .node-chip { font-family: var(--mono); font-size: 11px; padding: 4px 8px; border: 1px solid var(--line-2); color: var(--ink-2); background: var(--panel); cursor: pointer; }
  .node-chip:hover { border-color: var(--link); color: var(--ink); }
  .node-chip.on { border-color: var(--accent); color: var(--accent); background: var(--accent-soft); }
  .provisional { margin: 10px 0 16px; font-family: var(--mono); font-size: 11px; color: var(--warn); }

  /* ---- told lens ---- */
  .told-tracks { display: grid; gap: 26px; min-width: 620px; }
  .track-row { }
  .track-row .tlbl { font-family: var(--mono); font-size: 10.5px; letter-spacing: .1em; text-transform: uppercase; color: var(--ink-3); margin-bottom: 8px; }
  .track-line { position: relative; height: 54px; border-top: 1px solid var(--line-2); border-bottom: 1px solid var(--line-2); }
  .scene-card { position: absolute; top: 10px; left: 24px; width: 260px; border: 1px solid var(--accent); background: var(--accent-soft); border-radius: 3px; padding: 6px 10px; font-size: 12.5px; cursor: pointer; }
  .scene-card b { display: block; font-family: var(--display); font-size: 13.5px; color: var(--accent-ink); }
  .empty-track { padding: 14px 4px; font-family: var(--mono); font-size: 12px; color: var(--ink-3); }
  .jump-note { margin-top: 4px; font-family: var(--mono); font-size: 11px; color: var(--ink-3); }

  /* ---- detail rail ---- */
  aside.detail { grid-area: detail; border-left: 1px solid var(--line-2); overflow-y: auto; padding: 16px 16px 22px; background: color-mix(in srgb, var(--panel) 55%, transparent); }
  .detail-tabs { display: flex; gap: 0; margin-bottom: 12px; border-bottom: 1px solid var(--line); }
  .detail-tabs button { font-family: var(--mono); font-size: 11px; letter-spacing: .08em; text-transform: uppercase; padding: 6px 10px; color: var(--ink-2); border-bottom: 2px solid transparent; }
  .detail-tabs button.on { color: var(--accent); border-bottom-color: var(--accent); }
  .dcard h3 { margin: 0 0 2px; font-family: var(--display); font-weight: 700; font-size: 20px; text-transform: uppercase; }
  .dcard .kind { font-family: var(--mono); font-size: 10.5px; color: var(--ink-3); text-transform: uppercase; letter-spacing: .1em; margin-bottom: 10px; }
  .dcard dl { margin: 10px 0 0; display: grid; gap: 8px; }
  .dcard dt { font-family: var(--mono); font-size: 10px; letter-spacing: .1em; text-transform: uppercase; color: var(--ink-3); }
  .dcard dd { margin: 2px 0 0; font-size: 13.5px; line-height: 1.45; }
  .dcard .src { margin-top: 14px; font-family: var(--mono); font-size: 10.5px; color: var(--ink-3); }
  .empty-detail { font-size: 13.5px; color: var(--ink-3); }

  /* ---- character window (CK3 sheet) ---- */
  .csheet .idblock { display: flex; gap: 12px; align-items: center; padding-bottom: 12px; border-bottom: 1px solid var(--line); }
  .csheet .portrait { width: 52px; height: 52px; border-radius: 50%; background: var(--panel-2); border: 2px solid var(--accent); display: grid; place-items: center; font-family: var(--display); font-weight: 800; font-size: 22px; color: var(--accent); flex: 0 0 auto; }
  .csheet .idtext b { display: block; font-family: var(--display); font-weight: 800; font-size: 19px; text-transform: uppercase; }
  .csheet .idtext .alias { font-family: var(--mono); font-size: 11px; color: var(--ink-3); }
  .csheet .thesis { margin: 10px 0 0; font-size: 13.5px; font-style: italic; color: var(--ink-2); }
  .csheet .agehealth { margin-top: 4px; font-family: var(--mono); font-size: 10.5px; color: var(--ink-3); }
  .csheet h4 { margin: 16px 0 6px; font-family: var(--mono); font-size: 10.5px; letter-spacing: .1em; text-transform: uppercase; color: var(--ink-3); }
  .traits { display: flex; flex-wrap: wrap; gap: 6px; }
  .trait { border: 1px solid var(--line-2); border-radius: 3px; padding: 5px 8px; font-size: 11.5px; min-width: 108px; }
  .trait.linked { border-color: var(--good); cursor: pointer; }
  .trait.linked:hover { background: var(--good-soft); }
  .trait.gap { border-style: dashed; color: var(--ink-3); }
  .trait b { display: block; font-family: var(--mono); font-size: 10px; letter-spacing: .08em; }
  .trait .tn { font-family: var(--display); font-weight: 700; text-transform: uppercase; font-size: 13px; }

  /* ---- event log ---- */
  footer.log { grid-area: log; border-top: 1px solid var(--line-2); background: color-mix(in srgb, var(--panel) 85%, transparent); display: flex; flex-direction: column; max-height: 128px; }
  .log-bar { display: flex; align-items: center; gap: 10px; padding: 6px 14px; border-bottom: 1px solid var(--line); flex-wrap: wrap; }
  .log-bar .lbl { margin-right: 4px; }
  .log-filter { display: flex; gap: 4px; }
  .log-filter button { font-family: var(--mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; padding: 2px 7px; border: 1px solid var(--line-2); color: var(--ink-2); }
  .log-filter button.on { border-color: var(--accent); color: var(--accent); }
  .log-rows { overflow-y: auto; padding: 4px 14px 8px; font-family: var(--mono); font-size: 11.5px; }
  .log-row { display: grid; grid-template-columns: 46px 60px 1fr; gap: 10px; padding: 3px 0; color: var(--ink-2); }
  .log-row .n { color: var(--ink-3); }
  .log-row .lens { color: var(--accent-ink); text-transform: uppercase; }

  /* ---- tooltips (CK3 R2-R4) ---- */
  .tip { position: fixed; z-index: 80; width: 320px; max-width: calc(100vw - 24px); background: var(--panel); border: 1px solid var(--line-2); border-top: 3px solid var(--accent); box-shadow: var(--shadow); padding: 10px 12px 8px; font-size: 13.5px; line-height: 1.4; }
  .tip .th { display: flex; align-items: baseline; gap: 8px; margin-bottom: 4px; flex-wrap: wrap; }
  .tip .th b { font-family: var(--display); font-weight: 700; font-size: 17px; text-transform: uppercase; }
  .tip .th .k { font-family: var(--mono); font-size: 9.5px; letter-spacing: .1em; text-transform: uppercase; color: var(--ink-3); }
  .tip p { margin: 0; }
  .tip ul.tlist { margin: 8px 0 0; padding: 0; list-style: none; display: grid; gap: 4px; }
  .tip ul.tlist li { border-left: 2px solid var(--line-2); padding-left: 6px; }
  .tip .or-line, .dcard .or-line { margin: 4px 0 0; font-family: var(--mono); font-size: 11px; color: var(--ink-3); font-style: italic; }
  .tip .more { margin-top: 6px; font-family: var(--mono); font-size: 10.5px; color: var(--ink-3); }
  .tip .w { margin-top: 8px; font-family: var(--mono); font-size: 10.5px; color: var(--ink-3); overflow-wrap: anywhere; }
  .tip .lock { height: 2px; background: var(--line); margin-top: 8px; position: relative; }
  .tip .lock b { position: absolute; left: 0; top: 0; bottom: 0; width: 0; background: var(--accent); }
  .tip.locked .lock b { width: 100%; }
  .tip.locked { border-top-color: var(--ink); }
  .tip .hint2 { font-family: var(--mono); font-size: 9.5px; color: var(--ink-3); margin-top: 4px; letter-spacing: .04em; }
  .tip .capped { font-family: var(--mono); font-size: 10.5px; color: var(--ink-3); font-style: italic; }

  /* ---- phone tab bar ---- */
  nav.tabbar { display: none; }

  @media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }

  @media (max-width: 600px) {
    .app { grid-template-columns: 1fr; grid-template-rows: auto minmax(0,1fr) auto auto; grid-template-areas: "head" "canvas" "log" "tabbar"; }
    nav.lenses { display: none; }
    aside.ol, aside.detail { display: none; position: fixed; top: 48px; bottom: 40px; left: 0; right: 0; z-index: 60; width: auto; }
    aside.ol.show, aside.detail.show { display: block; }
    aside.detail { border-left: 0; border-top: 1px solid var(--line-2); }
    .ol-toggle, .detail-toggle { display: block; }
    footer.log { max-height: 84px; }
    nav.tabbar { display: flex; grid-area: tabbar; border-top: 1px solid var(--line-2); background: var(--panel); }
    nav.tabbar button { flex: 1 1 0; font-family: var(--display); font-weight: 700; font-size: 13px; text-transform: uppercase; padding: 10px 0; color: var(--ink-2); }
    nav.tabbar button.on { color: var(--accent); box-shadow: inset 0 3px 0 var(--accent); }
    main.canvas { padding: 12px 14px 18px; }
    .fab-scroll, .signpost-grid, .node-cols, .told-tracks { overflow-x: auto; }
  }
</style>
"""


def build_html() -> str:
    parts = []
    parts.append("<title>Story Workspace</title>")
    parts.append(STYLE)
    parts.append(
        """
<div class="app" id="app">
  <header class="head">
    <div class="brand"><i></i><b>Story Workspace</b></div>
    <nav class="lenses" id="lensNav">
      <button data-lens="fabula" class="on">Fabula<span class="k">1</span></button>
      <button data-lens="rails">Rails<span class="k">2</span></button>
      <button data-lens="told">Told<span class="k">3</span></button>
    </nav>
    <div class="headspace"></div>
    <button class="char-btn" id="charBtn">Tori's sheet</button>
    <button class="ol-toggle" id="olToggle">Outliner</button>
    <button class="detail-toggle" id="detToggle">Detail</button>
  </header>

  <aside class="ol" id="ol"></aside>

  <main class="canvas" id="canvas">
    <section class="lens-view on" id="view-fabula">
      <h2>Fabula — the world timeline</h2>
      <p class="sub">The <span class="t" data-tt="gloss" data-id="fabula">timeline is the map</span>: Tori's five dated-in-story events over three fuzzy DCUS eras. No calendar exists for this world — dates are movement-relative or banded, never invented points.</p>
      <div class="fab-scroll"><div class="fab-track" id="fabTrack"></div></div>
      <p class="fab-legend hint">Solid dot = single event &nbsp;·&nbsp; dashed dot = <span class="t" data-tt="gloss" data-id="repeat">repeat / iterative</span> event, one record standing for a repeated class (Genette 1980: 53).</p>
    </section>

    <section class="lens-view" id="view-rails">
      <h2>Rails — the trope graph, focus-tree style</h2>
      <p class="sub">16 <span class="t" data-tt="gloss" data-id="signpost">signposts</span> across 4 acts, 4 <span class="t" data-tt="gloss" data-id="throughline">throughlines</span> down. Only the book <span class="t" data-tt="gloss" data-id="node">nodes</span> draw on the grid; <span class="t" data-tt="gloss" data-id="trope">tropes</span> live inside each node's tooltip, capped at six.</p>
      <div class="rails-toolbar">
        <input type="text" id="nodeSearch" placeholder="search nodes…">
        <div class="fam-filter" id="famFilter"></div>
        <label class="explore-toggle"><input type="checkbox" disabled> Explore (free network) — later feature</label>
      </div>
      <h3 class="lbl" style="margin:0 0 8px">The signposts — fixed rail</h3>
      <div class="signpost-grid" id="signpostGrid"></div>
      <h3 class="lbl" style="margin:0 0 4px">The book nodes — seated by phase</h3>
      <p class="provisional">provisional — call 77-I open (phase-to-act seating; no per-node throughline data exists yet)</p>
      <div class="node-cols" id="nodeCols"></div>
    </section>

    <section class="lens-view" id="view-told">
      <h2>Told — two stacked tracks</h2>
      <p class="sub">Told order above world time. A jump line marks a scene that jumps back or forward from where the reader's told order last stood.</p>
      <div class="fab-scroll"><div class="told-tracks" id="toldTracks"></div></div>
    </section>
  </main>

  <aside class="detail" id="detail"></aside>

  <footer class="log">
    <div class="log-bar">
      <span class="lbl">Event log</span>
      <div class="log-filter" id="logFilter"></div>
    </div>
    <div class="log-rows" id="logRows"></div>
  </footer>

  <nav class="tabbar" id="tabbar">
    <button data-lens="fabula" class="on">Fabula</button>
    <button data-lens="rails">Rails</button>
    <button data-lens="told">Told</button>
  </nav>
</div>
"""
    )
    parts.append(f'<script>\nconst DATA = {DATA_JSON};\n' + JS + "\n</script>")
    return "\n".join(parts)


JS = r"""
(function(){
'use strict';
const $ = (s, r) => (r||document).querySelector(s);
const $$ = (s, r) => Array.from((r||document).querySelectorAll(s));
function esc(s){ return (s==null?'':String(s)).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }

const state = { lens: 'fabula', selection: null, log: [], famOn: null, query: '' };

// ---- index helpers ----
const eventsById = {}; DATA.fabula.events.forEach(e => eventsById[e.event_id] = e);
const nodesById = {}; DATA.rails.nodes.forEach(n => nodesById[n.id] = n);
const erasById = {}; DATA.fabula.eras.forEach(e => erasById[e.id] = e);

function logEvent(lens, text){
  state.log.unshift({ n: state.log.length + 1, lens, text, t: new Date() });
  if (state.log.length > 60) state.log.pop();
  renderLog();
}

function select(type, id, opts){
  opts = opts || {};
  state.selection = { type, id };
  renderDetail();
  highlightSelection();
  if (!opts.silent) logEvent(opts.lensLabel || state.lens, describeSelection(type, id));
}

function describeSelection(type, id){
  if (type === 'event'){ const e = eventsById[id]; return 'event selected · ' + (e ? e.event_id : id); }
  if (type === 'era'){ const e = erasById[id]; return 'era selected · ' + (e ? e.label : id); }
  if (type === 'node'){ const n = nodesById[id]; return 'node selected · ' + (n ? n.name : id); }
  if (type === 'signpost'){ return 'signpost selected · ' + id; }
  if (type === 'told'){ return 'told scene selected · ' + id; }
  if (type === 'character'){ return "Tori's sheet opened"; }
  return type + ' · ' + id;
}

function highlightSelection(){
  $$('[data-sel-type].on').forEach(el => el.classList.remove('on'));  // only selection marks; lens views and filters keep their own .on
  if (!state.selection) return;
  $$(`[data-sel-type="${state.selection.type}"][data-sel-id="${CSS.escape(String(state.selection.id))}"]`).forEach(el => el.classList.add('on'));
  $$(`.lenses button[data-lens="${state.lens}"], nav.tabbar button[data-lens="${state.lens}"]`).forEach(el => el.classList.add('on'));
}

// ---- lens switching ----
function setLens(lens){
  state.lens = lens;
  $$('.lens-view').forEach(v => v.classList.toggle('on', v.id === 'view-' + lens));
  $$('#lensNav button, #tabbar button').forEach(b => b.classList.toggle('on', b.dataset.lens === lens));
  renderOutliner();
}
$('#lensNav').addEventListener('click', e => { const b = e.target.closest('button'); if (b) setLens(b.dataset.lens); });
$('#tabbar').addEventListener('click', e => { const b = e.target.closest('button'); if (b) setLens(b.dataset.lens); });

// ---- outliner ----
function renderOutliner(){
  const ol = $('#ol');
  let html = '';
  html += '<h4>Character</h4>';
  html += `<button class="ol-row" data-act="character">Victoria Midnight <small>Tori · CK3 sheet</small></button>`;
  html += '<h4>Fabula · eras</h4>';
  DATA.fabula.eras.forEach(e => { html += `<button class="ol-row" data-act="select" data-sel-type="era" data-sel-id="${e.id}">${esc(e.label)}<small>${esc(e.note)}</small></button>`; });
  html += '<h4>Fabula · events</h4>';
  DATA.fabula.events.forEach(ev => { html += `<button class="ol-row" data-act="select" data-sel-type="event" data-sel-id="${ev.event_id}">${esc(ev.time.movement)}<small>${esc(ev.event_id)}</small></button>`; });
  html += '<h4>Told</h4>';
  html += `<button class="ol-row" data-act="select" data-sel-type="told" data-sel-id="${DATA.told.scene.id}">${esc(DATA.told.scene.address)}<small>the one carded scene</small></button>`;
  html += '<h4>Rails</h4>';
  html += `<button class="ol-row" data-act="select" data-sel-type="signpost" data-sel-id="MC|1">MC · Signpost 1<small>the one carded scene</small></button>`;
  ol.innerHTML = html;
  highlightSelection();
}
$('#ol').addEventListener('click', e => {
  const b = e.target.closest('button'); if (!b) return;
  if (b.dataset.act === 'character') { openCharacter(); return; }
  select(b.dataset.selType, b.dataset.selId);
});

// ---- fabula lens ----
function renderFabula(){
  const track = $('#fabTrack');
  const eras = DATA.fabula.eras;
  const bandW = 100 / eras.length;
  let html = '';
  eras.forEach((e, i) => {
    const left = (i * bandW) + '%'; const width = bandW + '%';
    html += `<div class="era-band t" data-tt="era" data-id="${e.id}" data-sel-type="era" data-sel-id="${e.id}" tabindex="0" style="left:${left};width:${width}">`
         +  `<span class="lbl2">${esc(e.label)}</span><span class="fz">${esc(e.note)}</span></div>`;
  });
  html += '<div class="movement-axis" id="movAxis"></div>';
  track.innerHTML = html;

  // place events along a movement-ordinal axis inside the DCUS band (era index 2)
  const dcusIdx = eras.findIndex(e => e.id === 'era_dcus');
  const bandLeft = dcusIdx * bandW, bandRight = bandLeft + bandW;
  const movementOrder = { 'M1B': 0.12, 'M2': 0.52, 'M3': 0.86 };
  function xFor(mv){
    const key = Object.keys(movementOrder).find(k => (mv||'').indexOf(k) === 0) || 'M2';
    return bandLeft + (bandRight - bandLeft) * movementOrder[key];
  }
  const axis = $('#movAxis');
  Object.keys(movementOrder).forEach(k => {
    const x = bandLeft + (bandRight - bandLeft) * movementOrder[k];
    const t = document.createElement('div'); t.className = 'tick'; t.style.left = x + '%';
    t.innerHTML = `<span>${k}</span>`; axis.appendChild(t);
  });
  DATA.fabula.events.forEach(ev => {
    const x = xFor(ev.time.movement);
    const dot = document.createElement('div');
    dot.className = 'ev-dot t' + (ev.repeat ? ' repeat' : '');
    dot.style.left = x + '%';
    dot.tabIndex = 0;
    dot.dataset.tt = 'event'; dot.dataset.id = ev.event_id;
    dot.dataset.selType = 'event'; dot.dataset.selId = ev.event_id;
    track.appendChild(dot);
    const lab = document.createElement('div');
    lab.className = 'ev-label'; lab.style.left = x + '%';
    lab.textContent = ev.event_id.replace(/_/g, ' ');
    track.appendChild(lab);
  });
}

// ---- rails lens ----
function renderSignpostGrid(){
  const grid = $('#signpostGrid');
  let html = '<div class="sp-corner"></div>';
  DATA.rails.acts.forEach(a => html += `<div class="sp-act-hd">Act ${a} · ${esc((DATA.rails.actMov||{})[a]||'')}</div>`);
  DATA.rails.throughlines.forEach(tl => {
    html += `<div class="sp-row-hd t" data-tt="tl" data-id="${tl.id}" tabindex="0">${tl.id}<small>${esc(tl.pov)} — ${esc(tl.name)}</small></div>`;
    DATA.rails.acts.forEach(a => {
      const key = tl.id + '|' + a;
      const fill = DATA.rails.fill[key];
      if (fill){
        html += `<button class="sig-cell filled t" data-tt="signpost" data-id="${key}" data-sel-type="signpost" data-sel-id="${key}"><b>${esc(fill.label)}</b>${esc(fill.movement)}<span class="sig-chip">${fill.state==='carded'?'scene carded':'storyform'}</span></button>`;
      } else {
        html += `<div class="sig-cell empty">no instance found<span class="sig-chip gap">unverified</span></div>`;
      }
    });
  });
  grid.innerHTML = html;
}

function renderNodeColumns(){
  const cols = ['act1','act2_3','act4','side'];
  const wrap = $('#nodeCols');
  const q = state.query.toLowerCase();
  let html = '';
  cols.forEach(c => {
    const nodes = DATA.rails.nodes.filter(n => n.column === c)
      .filter(n => !state.famOn || n.family === state.famOn)
      .filter(n => !q || n.name.toLowerCase().includes(q) || n.id.toLowerCase().includes(q));
    html += `<div class="node-col"><h3>${esc(DATA.rails.columns[c])}</h3><div class="cnt">${nodes.length} node(s)</div>`;
    html += '<div class="node-cluster">';
    nodes.forEach(n => {
      html += `<button class="node-chip t" data-tt="node" data-id="${n.id}" data-sel-type="node" data-sel-id="${n.id}">${esc(n.name)}</button>`;
    });
    html += '</div></div>';
  });
  wrap.innerHTML = html;
}

function renderFamFilter(){
  const families = Array.from(new Set(DATA.rails.nodes.map(n => n.family)));
  const el = $('#famFilter');
  el.innerHTML = `<button data-f="" class="${state.famOn?'':'on'}">all</button>` + families.map(f => `<button data-f="${f}" class="${state.famOn===f?'on':''}">${esc(f)}</button>`).join('');
}
$('#famFilter').addEventListener('click', e => { const b = e.target.closest('button'); if (!b) return; state.famOn = b.dataset.f || null; renderFamFilter(); renderNodeColumns(); });
$('#nodeSearch').addEventListener('input', e => { state.query = e.target.value.trim(); renderNodeColumns(); });

// ---- told lens ----
function renderTold(){
  const wrap = $('#toldTracks');
  const scene = DATA.told.scene;
  let html = '';
  html += '<div class="track-row"><div class="tlbl">Told order</div><div class="track-line">';
  html += `<button class="scene-card t" data-tt="told" data-id="${scene.id}" data-sel-type="told" data-sel-id="${scene.id}"><b>${esc(scene.address)}</b>${esc(scene.signpost)}</button>`;
  html += '</div><div class="jump-note">order told = order happened here — no reordering on record; every other told-order slot has no scene carded yet.</div></div>';
  html += '<div class="track-row"><div class="tlbl">World time</div><div class="track-line">';
  const worldEv = eventsById[scene.fabula_event];
  if (worldEv){
    html += `<button class="scene-card t" data-tt="event" data-id="${worldEv.event_id}" data-sel-type="event" data-sel-id="${worldEv.event_id}" style="border-color:var(--good);background:var(--good-soft)"><b>${esc(worldEv.time.movement)}</b>${esc(worldEv.event_id)}</button>`;
  }
  html += '</div><div class="jump-note">world-time position read from the fabula event this told scene is seeded against.</div></div>';
  html += '<div class="empty-track">No other scenes carded yet — the told-order track stays sparse until more scene cards land (per the ruled default: the fabula view starts sparse and visibly thickens).</div>';
  wrap.innerHTML = html;
}

// ---- detail rail ----
let detailTab = 'detail';
function renderDetail(){
  const el = $('#detail');
  const tabs = `<div class="detail-tabs"><button data-t="detail" class="${detailTab==='detail'?'on':''}">Detail</button><button data-t="character" class="${detailTab==='character'?'on':''}">Tori</button></div>`;
  if (detailTab === 'character'){ el.innerHTML = tabs + characterSheetHtml(); wireCharacterSheet(); return; }
  if (!state.selection){ el.innerHTML = tabs + '<p class="empty-detail">Nothing selected. Click any marker, node, or scene to fill this panel.</p>'; return; }
  el.innerHTML = tabs + detailCardHtml(state.selection.type, state.selection.id);
}
$('#detail').addEventListener('click', e => {
  const t = e.target.closest('.detail-tabs button');
  if (t){ detailTab = t.dataset.t; renderDetail(); return; }
  const trait = e.target.closest('.trait.linked');
  if (trait){ detailTab = 'detail'; select('event', trait.dataset.event); return; }
});

function detailCardHtml(type, id){
  if (type === 'event'){
    const e = eventsById[id]; if (!e) return '<p class="empty-detail">Unknown event.</p>';
    return `<div class="dcard"><div class="kind">Fabula event · ${esc(e.kernel_satellite)}</div><h3>${esc(e.event_id)}</h3>
      <dl>
        <div><dt>Transition</dt><dd>${esc(e.transition)}</dd></div>
        <div><dt>Movement / reach / extent</dt><dd>${esc(e.time.movement)} — ${esc(e.time.reach)}; ${esc(e.time.extent)}</dd></div>
        <div><dt>Actors</dt><dd>${e.actors.map(a=>esc(a.actor)+' ('+esc(a.actant_role)+')').join(', ')}</dd></div>
        <div><dt>Gap / repeat</dt><dd>${esc(e.gap_type)}${e.repeat? ' · repeat (iterative)':''}</dd></div>
        <div><dt>Location</dt><dd>${esc(e.location)}</dd></div>
        <div><dt>Causal edges</dt><dd>${(e.causal_edges||[]).length? e.causal_edges.map(c=>esc(c.type)+' → '+esc(c.to)).join('; ') : 'none on record'}</dd></div>
      </dl>
      <div class="src">source: ${esc(e.provenance.source)} · ${esc(e.provenance.confidence)}</div></div>`;
  }
  if (type === 'era'){
    const e = erasById[id]; if (!e) return '';
    return `<div class="dcard"><div class="kind">World Clock era</div><h3>${esc(e.label)}</h3>
      <dl><div><dt>Reach / extent</dt><dd>${esc(e.note)}</dd></div><div><dt>Detail</dt><dd>${esc(e.detail)}</dd></div></dl>
      <div class="src">source: ssot_04_fabula.md, THE WORLD CLOCK (cross-referenced from ssot_03_setting_system.md)</div></div>`;
  }
  if (type === 'node'){
    const n = nodesById[id]; if (!n) return '';
    const tropes = n.tropes || [];
    const shown = tropes.slice(0, 6);
    return `<div class="dcard"><div class="kind">Rails node · ${esc(n.family)} #${n.n} · ${esc(n.phase)} phase</div><h3>${esc(n.name)}</h3>
      <p style="font-size:13.5px;margin:4px 0 0">${esc(n.def)}</p>
      <dl><div><dt>Tropes keyed (${tropes.length})</dt><dd><ul class="tlist" style="list-style:none;padding:0;margin:6px 0 0">${shown.map(t=>{ const alt = t.alt ? nodesById[t.alt] : null; return `<li style="border-left:2px solid var(--line-2);padding-left:6px;margin-bottom:4px">${esc(t.name)}${alt?`<div class="or-line">or: ${esc(alt.name)}</div>`:''}</li>`; }).join('')}${tropes.length>6?`<li class="more">+ ${tropes.length-6} more — hover the node on the rails for the capped tooltip</li>`:''}</dd></div>
      ${n.same_as && n.same_as.length ? `<div><dt>Same as</dt><dd>${n.same_as.map(esc).join(', ')}</dd></div>`:''}
      </dl>
      <div class="src">source: ${esc(n.cite||'')} · ${esc(n.bvx||'')} · _tools/tropes/data/trope_graph.json</div></div>`;
  }
  if (type === 'signpost'){
    const [tl, act] = id.split('|');
    const fill = DATA.rails.fill[id];
    if (!fill) return `<div class="dcard"><div class="kind">Signpost cell</div><h3>${esc(tl)} · Act ${esc(act)}</h3><p style="font-size:13.5px">No instance found — rail-required, unverified. Fixed order stays walkable; this cell renders bypassed-empty until a source fills it.</p></div>`;
    return `<div class="dcard"><div class="kind">Signpost cell · ${esc(fill.state)}</div><h3>${esc(fill.label)}</h3>
      <dl><div><dt>Movement</dt><dd>${esc(fill.movement)}</dd></div><div><dt>Detail</dt><dd>${esc(fill.detail)}</dd></div></dl>
      ${fill.told_id?'<button class="node-chip" style="margin-top:8px" data-jump="told">Open the told scene →</button>':''}
      <div class="src">source: PS-R.rails.md §4 · ssot_04_plot_system.md THE INSTANCE</div></div>`;
  }
  if (type === 'told'){
    const s = DATA.told.scene;
    return `<div class="dcard"><div class="kind">Told scene</div><h3>${esc(s.address)}</h3>
      <dl>
        <div><dt>Signpost</dt><dd>${esc(s.signpost)} (${esc(s.throughline)})</dd></div>
        <div><dt>Driver (local)</dt><dd>${esc(s.driver)}</dd></div>
        <div><dt>Value turn</dt><dd>${esc(s.value_turn)}</dd></div>
        <div><dt>Reveal</dt><dd>${esc(s.reveal)}</dd></div>
        <div><dt>Collision</dt><dd>${esc(s.collision)}</dd></div>
        <div><dt>Told vs happened</dt><dd>${esc(s.order_told_vs_happened)}</dd></div>
      </dl>
      <div class="src">source: ${esc(s.source)}</div></div>`;
  }
  return '<p class="empty-detail">Nothing selected.</p>';
}
$('#detail').addEventListener('click', e => {
  const jb = e.target.closest('[data-jump="told"]');
  if (jb){ setLens('told'); select('told', DATA.told.scene.id); }
});

// ---- character window ----
function openCharacter(){ detailTab = 'character'; renderDetail(); logEvent(state.lens, "Tori's sheet opened"); }
$('#charBtn').addEventListener('click', openCharacter);
function characterSheetHtml(){
  const c = DATA.character;
  return `<div class="csheet">
    <div class="idblock"><div class="portrait">T</div><div class="idtext"><b>${esc(c.name)}</b><span class="alias">${esc(c.alias)}</span></div></div>
    <p class="thesis">${esc(c.thesis)}</p>
    <p class="agehealth">${esc(c.age_health)}</p>
    <h4>Origin moments — the layers that need one</h4>
    <div class="traits">
      ${c.origin_layers.map(l => l.event
        ? `<div class="trait linked" data-event="${l.event}"><b>${esc(l.layer)}</b><span class="tn">${esc(l.name)}</span>linked → ${esc(l.event)}</div>`
        : `<div class="trait gap"><b>${esc(l.layer)}</b><span class="tn">${esc(l.name)}</span>gap — not yet fabula-linked</div>`
      ).join('')}
    </div>
    <p class="hint" style="margin-top:10px">${esc(c.origin_layers.find(l=>!l.event).note)}</p>
  </div>`;
}
function wireCharacterSheet(){}

// ---- event log ----
let logFilterOn = null;
function renderLog(){
  const rows = $('#logRows');
  const items = state.log.filter(r => !logFilterOn || r.lens === logFilterOn);
  rows.innerHTML = items.map(r => `<div class="log-row"><span class="n">#${r.n}</span><span class="lens">${esc(r.lens)}</span><span>${esc(r.text)}</span></div>`).join('') || '<div class="log-row"><span></span><span></span><span>no entries yet</span></div>';
}
function renderLogFilter(){
  const lenses = ['fabula','rails','told'];
  $('#logFilter').innerHTML = `<button data-f="" class="${logFilterOn?'':'on'}">all</button>` + lenses.map(l => `<button data-f="${l}" class="${logFilterOn===l?'on':''}">${l}</button>`).join('');
}
$('#logFilter').addEventListener('click', e => { const b = e.target.closest('button'); if (!b) return; logFilterOn = b.dataset.f || null; renderLogFilter(); renderLog(); });

// ---- canvas click delegation (fabula/rails/told selection) ----
$('#canvas').addEventListener('click', e => {
  const el = e.target.closest('[data-sel-type]'); if (!el) return;
  select(el.dataset.selType, el.dataset.selId);
});

// ---- mobile toggles ----
$('#olToggle').addEventListener('click', () => { $('#ol').classList.toggle('show'); $('#detail').classList.remove('show'); });
$('#detToggle').addEventListener('click', () => { $('#detail').classList.toggle('show'); $('#ol').classList.remove('show'); });

// ==================================================================
// ---- tooltip layer: CK3 nested tooltips, depth<=3, hover/lock/esc ----
// ==================================================================
let tips = [];
let openTimer = null, closeTimer = null;

function depthOf(target){ const p = target.closest('.tip'); return p ? (+p.dataset.depth + 1) : 1; }

function tropeTipHtml(node, trope, depth){
  const deep = depth >= 3;
  // call 77-N (Chief 9/24, all recs): show a trope's alt node as a visible
  // "or:" line, never drawn as an edge.
  const altNode = trope.alt ? nodesById[trope.alt] : null;
  const altLine = altNode ? `<p class="or-line">or: ${esc(altNode.name)}</p>` : '';
  return `<div class="th"><b>${esc(trope.name)}</b><span class="k">trope</span></div>
    <p>${esc(trope.def || '')}</p>
    ${altLine}
    ${deep ? '<div class="capped">nesting capped at depth 3</div>' : `<div class="w">from ${esc(node.name)} · conf: ${esc(trope.conf||'n/a')}</div>`}
    <div class="lock"><b></b></div><div class="hint2">hold 1.2s or Space to lock · Esc closes</div>`;
}
function nodeTipHtml(node, depth){
  const tropes = (node.tropes||[]).slice(0,6);
  const rest = (node.tropes||[]).length - tropes.length;
  return `<div class="th"><b>${esc(node.name)}</b><span class="k">${esc(node.family)} node</span></div>
    <p>${esc(node.def)}</p>
    <ul class="tlist">${tropes.map(t => `<li><span class="t" data-tt="trope-of" data-node="${node.id}" data-id="${esc(t.slug)}">${esc(t.name)}</span></li>`).join('')}</ul>
    ${rest > 0 ? `<div class="more">+ ${rest} more</div>` : ''}
    <div class="lock"><b></b></div><div class="hint2">hold 1.2s or Space to lock · Esc closes</div>`;
}
function eventTipHtml(ev, depth){
  return `<div class="th"><b>${esc(ev.event_id)}</b><span class="k">fabula event</span></div>
    <p>${esc(ev.transition)}</p>
    <div class="w">${esc(ev.time.movement)} · ${esc(ev.time.reach)}${ev.repeat?' · <span class="t" data-tt="gloss" data-id="repeat">repeat</span>':''}</div>
    <div class="lock"><b></b></div><div class="hint2">hold 1.2s or Space to lock · Esc closes</div>`;
}
function eraTipHtml(era){
  return `<div class="th"><b>${esc(era.label)}</b><span class="k">world-clock era</span></div>
    <p>${esc(era.detail)}</p>
    <div class="w">${esc(era.note)}</div>
    <div class="lock"><b></b></div><div class="hint2">hold 1.2s or Space to lock · Esc closes</div>`;
}
function signpostTipHtml(key){
  const fill = DATA.rails.fill[key];
  if (!fill) return `<div class="th"><b>${esc(key.replace('|',' · act '))}</b><span class="k">signpost</span></div><p>No instance found — rail-required, unverified.</p>`;
  return `<div class="th"><b>${esc(fill.label)}</b><span class="k">signpost · ${esc(fill.state)}</span></div><p>${esc(fill.detail)}</p>
    <div class="lock"><b></b></div><div class="hint2">hold 1.2s or Space to lock · Esc closes</div>`;
}
function toldTipHtml(scene){
  return `<div class="th"><b>${esc(scene.address)}</b><span class="k">told scene</span></div><p>${esc(scene.signpost)}</p>
    <div class="w">${esc(scene.order_told_vs_happened)}</div>
    <div class="lock"><b></b></div><div class="hint2">hold 1.2s or Space to lock · Esc closes</div>`;
}
function throughlineTipHtml(id, depth){
  const tl = DATA.rails.throughlines.find(t => t.id === id); if (!tl) return '';
  const deep = depth >= 3;
  return `<div class="th"><b>${esc(tl.id)}</b><span class="k">throughline · ${esc(tl.pov)}</span></div>
    <p>${esc(tl.name)} — ${esc(tl.role)}</p>
    ${!deep ? `<p><span class="t" data-tt="gloss" data-id="throughline">what a throughline is →</span></p>` : '<div class="capped">nesting capped at depth 3</div>'}
    <div class="lock"><b></b></div><div class="hint2">hold 1.2s or Space to lock · Esc closes</div>`;
}
function glossTipHtml(key, depth){
  const g = DATA.glossary[key]; if (!g) return '';
  const deep = depth >= 3;
  return `<div class="th"><b>${esc(g.t)}</b><span class="k">${esc(g.k)}</span></div>
    <p>${esc(g.d)}</p>
    ${!deep ? `<div class="w">${esc(g.w||'')}</div>` : '<div class="capped">nesting capped at depth 3</div>'}
    <div class="lock"><b></b></div><div class="hint2">hold 1.2s or Space to lock · Esc closes</div>`;
}

function contentFor(target, depth){
  const tt = target.dataset.tt, id = target.dataset.id;
  if (tt === 'node') return nodeTipHtml(nodesById[id], depth);
  if (tt === 'trope-of'){ const node = nodesById[target.dataset.node]; const trope = (node.tropes||[]).find(t => t.slug === id); return trope ? tropeTipHtml(node, trope, depth) : '<p>unknown trope</p>'; }
  if (tt === 'event') return eventTipHtml(eventsById[id], depth);
  if (tt === 'era') return eraTipHtml(erasById[id]);
  if (tt === 'signpost') return signpostTipHtml(id);
  if (tt === 'told') return toldTipHtml(DATA.told.scene);
  if (tt === 'tl') return throughlineTipHtml(id, depth);
  if (tt === 'gloss') return glossTipHtml(id, depth);
  return '';
}

function openTip(target, depth){
  if (depth > 3) return null;
  const el = document.createElement('div');
  el.className = 'tip'; el.dataset.depth = depth;
  el.innerHTML = contentFor(target, depth);
  document.body.appendChild(el);
  const r = target.getBoundingClientRect(); const w = 320, h = el.offsetHeight;
  let x = Math.min(Math.max(12, r.left), window.innerWidth - w - 12);
  let y = r.bottom + 8; if (y + h > window.innerHeight - 12) y = Math.max(12, r.top - h - 8);
  el.style.left = x + 'px'; el.style.top = y + 'px';
  const rec = { el, target, depth, locked: false, timer: null };
  const bar = el.querySelector('.lock b');
  if (bar) { requestAnimationFrame(() => { bar.style.transition = 'width 1.2s linear'; bar.style.width = '100%'; }); rec.timer = setTimeout(() => lockTip(rec), 1200); }
  el.addEventListener('mouseenter', () => clearTimeout(closeTimer));
  el.addEventListener('mouseleave', () => scheduleClose(depth));
  target.classList.add('on');
  tips.push(rec);
  return rec;
}
function lockTip(rec){ rec.locked = true; rec.el.classList.add('locked'); }
function closeTips(fromDepth){
  tips.filter(t => t.depth >= fromDepth).forEach(t => { clearTimeout(t.timer); t.el.remove(); t.target.classList.remove('on'); });
  tips = tips.filter(t => t.depth < fromDepth);
}
function scheduleClose(depth){
  clearTimeout(closeTimer);
  closeTimer = setTimeout(() => {
    const unlocked = tips.filter(t => t.depth >= depth && !t.locked);
    if (unlocked.length) closeTips(Math.min(...unlocked.map(t => t.depth)));
  }, 200);
}
function onEnter(target){
  clearTimeout(openTimer); clearTimeout(closeTimer);
  const d = depthOf(target);
  openTimer = setTimeout(() => { closeTips(d); openTip(target, d); }, 110);
}
document.addEventListener('mouseover', e => { const t = e.target.closest('.t'); if (t) onEnter(t); });
document.addEventListener('mouseout', e => { const t = e.target.closest('.t'); if (t) { clearTimeout(openTimer); scheduleClose(depthOf(t)); } });
document.addEventListener('focusin', e => { const t = e.target.closest('.t'); if (t) onEnter(t); });
document.addEventListener('focusout', e => { const t = e.target.closest('.t'); if (t) scheduleClose(depthOf(t)); });
document.addEventListener('click', e => { if (!e.target.closest('.tip') && !e.target.closest('.t')) closeTips(1); });

// ---- keyboard: 1/2/3 lenses, Esc close, Space lock ----
document.addEventListener('keydown', e => {
  if (e.target.matches('input')) { if (e.key === 'Escape') e.target.blur(); return; }
  if (e.key === '1') { setLens('fabula'); return; }
  if (e.key === '2') { setLens('rails'); return; }
  if (e.key === '3') { setLens('told'); return; }
  if (e.key === 'Escape') { if (tips.length) closeTips(1); else { $('#ol').classList.remove('show'); $('#detail').classList.remove('show'); } return; }
  if (e.key === ' ' && tips.length) { e.preventDefault(); lockTip(tips[tips.length-1]); return; }
});

// ==================================================================
// ---- boot: a realistic working state ----
// ==================================================================
renderOutliner();
renderFabula();
renderSignpostGrid();
renderFamFilter();
renderNodeColumns();
renderTold();
renderLogFilter();
detailTab = 'detail';
// seed the log with the session's opening moves, then land on the crash event
logEvent('fabula', 'workspace opened · Fabula lens (default)');
select('event', 'm1b_crash_jebb_death', { lensLabel: 'fabula' });
logEvent('fabula', "Tori's five fabula events loaded · 3 DCUS eras banded (fuzzy)");
})();
"""

# --------------------------------------------------------------- CHECKS ---

class TagBalanceChecker(HTMLParser):
    VOID = {
        "area","base","br","col","embed","hr","img","input","link","meta",
        "param","source","track","wbr",
    }

    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag in self.VOID:
            return
        self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        pass  # self-closed, fine either way

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        if not self.stack:
            self.errors.append(f"stray closing tag </{tag}> with nothing open")
            return
        if self.stack[-1] == tag:
            self.stack.pop()
            return
        if tag in self.stack:
            # close everything up to it (script/style pairs are exact, but be lenient)
            while self.stack and self.stack[-1] != tag:
                self.errors.append(f"unclosed <{self.stack.pop()}> before </{tag}>")
            if self.stack:
                self.stack.pop()
        else:
            self.errors.append(f"</{tag}> has no matching open tag")


def check_html(html: str):
    parser = TagBalanceChecker()
    parser.feed(html)
    parser.close()
    if parser.stack:
        parser.errors.append("unclosed at EOF: " + ", ".join(parser.stack))
    return parser.errors


def main():
    html = build_html()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    size = OUT.stat().st_size
    errors = check_html(html)
    print(f"wrote {OUT} ({size:,} bytes / {size/1024/1024:.3f} MB)")
    print(f"rails nodes: {DATA['counts']['rails_nodes']}  tropes: {DATA['counts']['rails_tropes']}  fabula events: {DATA['counts']['fabula_events']}")
    if errors:
        print("HTML PARSE ISSUES:")
        for e in errors:
            print("  -", e)
    else:
        print("HTML parse check: OK, no unclosed tags.")
    if MISSING:
        print("MISSING SOURCES (skipped):")
        for m in MISSING:
            print("  -", m)
    if size > 1_500_000:
        print("WARNING: over the 1.5 MB budget.")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
