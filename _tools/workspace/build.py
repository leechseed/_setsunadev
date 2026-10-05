#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BOLO 79 · MS-UI build — the story workspace, one page, three views
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

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tracking  # noqa: E402 — ShroomsQ/_CANON/_TRACKING/<story>.yaml loader (BOLO 79/90, RULED 9/29)

ROOT = Path(__file__).resolve().parents[2]
FABULA_MD = ROOT / "ShroomsQ/_CANON/_SSOT/04_PLOT_SYSTEMS/📐 ssot_04_fabula.md"
PLOT_MD = ROOT / "ShroomsQ/_CANON/_SSOT/04_PLOT_SYSTEMS/📐 ssot_04_plot_system.md"
TROPE_JSON = ROOT / "_tools/tropes/data/trope_graph.json"
RAILS_MD = ROOT / "_tools/bolostatus/work/77/tropes/PS-R.rails.md"
GLOSSARY_JSON = ROOT / "_tools/sitrep/glossary.json"
OUT = Path(__file__).resolve().parent / "out" / "workspace.html"

# the playhead inspector's base records (BOLO 90 step 7, RULED 9/29): parsed at
# build time from canon, per ssot_02_character_state_architecture.md
# §"Querying a Character at a Narrative Moment" (base -> diffs -> derived -> flags).
CHARACTER_NODE_MD = ROOT / "_CANON_NODES" / "victoria-midnight.md"
SETTING_SYSTEM_MD = ROOT / "ShroomsQ/_CANON/_SSOT/03_SETTING_SYSTEMS/📐 ssot_03_setting_system.md"

# the Told view (The Arrangement, BOLO 79 ruled 9/29): one tracking file per story,
# `stories:` scope kept at OXO only — tracking.py fails loudly on a bad code/slug.
TRACKING = tracking.load("oxo")

# the edits ledger (BOLO 90 step 6, RULED 9/29 · the edit contract): the pull's
# record of what's already folded into oxo.yaml. The page never re-applies an
# id already in one of these three lists — see EDIT-CONTRACT.md "the ledger".
LEDGER_PATH = ROOT / "ShroomsQ/_CANON/_TRACKING/oxo.edits.ledger.json"


def _load_ledger():
    default = {"applied": [], "undone": [], "flagged": {}}
    if not LEDGER_PATH.exists():
        return default
    try:
        raw = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return default
    return {
        "applied": raw.get("applied") or [],
        "undone": raw.get("undone") or [],
        "flagged": raw.get("flagged") or {},
    }


AR_LEDGER = _load_ledger()

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


# ------------------------------------------------------- BASES (BOLO 90 step 7) ---
# the playhead inspector's base records: parsed straight out of the canon tables
# named in the tasking (victoria-midnight.md's 12-layer table + Flags line;
# ssot_03_setting_system.md's DCUS proof table). Every parser fails loudly
# (SystemExit) on a missing section, a short table, or a missing Flags line —
# never guesses a layer value or invents a flag.

_MD_WIKI_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")
_MD_BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
_MD_ITAL_RE = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")
_MD_CODE_RE = re.compile(r"`([^`]+)`")


def strip_md(text):
    """Strip the light markdown canon prose carries — wiki links, markdown
    links, bold, italics, inline code — down to plain display text."""
    if not text:
        return ""
    t = text
    t = _MD_WIKI_RE.sub(lambda m: m.group(2) or m.group(1), t)
    t = _MD_LINK_RE.sub(r"\1", t)
    t = _MD_BOLD_RE.sub(r"\1", t)
    t = _MD_ITAL_RE.sub(r"\1", t)
    t = _MD_CODE_RE.sub(r"\1", t)
    return t.strip()


_LAYER_ROW_RE = re.compile(r"^\|\s*([LS]\d+)\s+([A-Z]+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$")
_LAYER_ROW_2COL_RE = re.compile(r"^\|\s*([LS]\d+)\s+([A-Z]+)\s*\|\s*(.*?)\s*\|$")


def parse_character_base(path):
    """Tori's base record (BOLO 90 step 7 ruling 1): the '## The 12 layers'
    table (L1..L12 | Value | Fed by) plus the '**Flags:**' line under it."""
    md = read(path)
    if not md:
        raise SystemExit(f"build.py: can't read character base at {path}")
    sec = re.search(r"##\s*The 12 layers\b(.*?)(?:\n##\s|\Z)", md, re.S)
    if not sec:
        raise SystemExit(f"build.py: no '## The 12 layers' section in {path}")
    body = sec.group(1)
    layers = []
    for line in body.splitlines():
        m = _LAYER_ROW_RE.match(line.strip())
        if not m:
            continue
        code, name, value, fed_by = m.groups()
        layers.append({"code": code, "name": name, "value": strip_md(value), "fed_by": strip_md(fed_by)})
    if len(layers) < 12:
        raise SystemExit(f"build.py: '## The 12 layers' table in {path} has only {len(layers)} L-rows — need 12")
    flag_m = re.search(r"\*\*Flags:\*\*\s*(.+)", body)
    if not flag_m:
        raise SystemExit(f"build.py: no '**Flags:**' line under the 12-layer table in {path}")
    flags = [{"name": n, "state": s} for n, s in re.findall(r"([A-Z][A-Z0-9_]*)\s*`([^`]+)`", flag_m.group(1))]
    if not flags:
        raise SystemExit(f"build.py: '**Flags:**' line in {path} carries no NAME `state` entries")
    return {"layers": layers, "flags": flags}


def parse_place_base(path):
    """DCUS's base record (BOLO 90 step 7 ruling 2): the DCUS proof table
    (S1..S12 | DCUS). No 'Fed by' column here — values are long prose, kept
    full for the tooltip and trimmed for display on the page side."""
    md = read(path)
    if not md:
        raise SystemExit(f"build.py: can't read place base at {path}")
    sec = re.search(r"##\s*THE INSTANCE\s*—\s*DCUS starter slice\b(.*?)\n---\n", md, re.S)
    if not sec:
        raise SystemExit(f"build.py: no DCUS starter-slice instance table in {path}")
    body = sec.group(1)
    layers = []
    for line in body.splitlines():
        m = _LAYER_ROW_2COL_RE.match(line.strip())
        if not m:
            continue
        code, name, value = m.groups()
        layers.append({"code": code, "name": name, "value": strip_md(value), "fed_by": ""})
    if len(layers) < 12:
        raise SystemExit(f"build.py: DCUS proof table in {path} has only {len(layers)} S-rows — need 12")
    return {"layers": layers, "flags": []}


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
_era_red_stick = "Skeeter Creek (founding, buried, no date given)"
_era_red_hills = "Red Hills (the first rename, reach roughly a century before the Bishop acquisition, extent unstated)"
_era_dcus = "DCUS (the current era, tied to the Bishop acquisition"
for q in (_era_red_stick, _era_red_hills, _era_dcus):
    need(fabula_md, q.split(" (")[0], f"world-clock era: {q}")

WORLD_CLOCK_ERAS = [
    {
        "id": "era_skeeter_creek",
        "label": "Skeeter Creek",
        "note": "universe era 1 · founding, buried — no date given",
        "detail": "100+ years of private prestige; the founding name sanded to “Red Hills” a century before the Bishops arrived. No calendar date exists for this transition.",
        "order": 0,
    },
    {
        "id": "era_red_hills",
        "label": "Red Hills",
        "note": "universe era 1 · the first rename — reach roughly a century before the Bishop acquisition, extent unstated",
        "detail": "The rename lattice: Skeeter Creek → Red Hills → DCUS — erasure done twice.",
        "order": 1,
    },
    {
        "id": "era_dcus",
        "label": "DCUS",
        "note": "universe era 2 · tied to the Bishop acquisition",
        "detail": "Prestige converted to product; the ownership war — grandfather vs son — sold for spoils to the Bishops.",
        "order": 2,
    },
]

# the universe eras after DCUS (fabula THE WORLD CLOCK, RULED 2026-09-29): the stories move outward
# from Earth. Chief 9/29 session 4: "after DCUS, there's the cislunar space, and then the moon, and
# then beyond" — era 5 (renumbered 9/29 when Skeeter Creek became era 1) is named in canon only as "beyond" (⧗).
for q in ("the LAKAD era", "the ASTRO7EX era", "the beyond era"):
    need(fabula_md, q, f"universe era: {q}")
UNIVERSE_ERAS = [
    {"id": "era_lakad", "label": "LAKAD", "note": "era 3 · cislunar space — band only, no events on record",
     "detail": "The third universe era: LAKAD (codename), set in cislunar space. Sequential after DCUS, overlap allowed at the seam.", "order": 3, "universe": True},
    {"id": "era_astro7ex", "label": "ASTRO7EX", "note": "era 4 · the Moon — band only, backstory events not yet loaded",
     "detail": "The fourth universe era: ASTRO7EX, on the Moon. The Deep Meridian beam is the hinge into it.", "order": 4, "universe": True},
    {"id": "era_beyond", "label": "Beyond ⧗", "note": "era 5 · past the Moon — unnamed, no story yet",
     "detail": "The fifth universe era, past the Moon. Named only as 'beyond' (Chief, 9/29); no story or events yet.", "order": 5, "universe": True},
]
WORLD_CLOCK_ERAS = WORLD_CLOCK_ERAS + UNIVERSE_ERAS

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
    "act1": "Act 1 · M1 + M2",
    "act2": "Act 2 · M3",
    "act3": "Act 3 · M4 + M5",
    "act4": "Act 4 · M6",
    "side": "Any act · whole-plot patterns",
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
            # seated 9/24 (call 77-I) on the ruled Bourne map · seat calls 1–3 RULED 9/24; Tobias/Schmidt ride any act
            "column": f"act{n['act']}" if isinstance(n.get("act"), int) else "side",
            "throughline": n.get("throughline"),
            "seat_why": n.get("seat_why"),
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
        # ---- the Told view's own terms, ported from The Arrangement's TERMS (BOLO 90 × 79, ruled 9/29) ----
        "timecode": {
            "t": "Time code", "k": "grid",
            "d": "Where a moment sits: movement · sequence · scene | bar.beat.tick. M2 · Q1 · S02 | 006.3.2 is movement 2, sequence 1, scene 2, bar 6, beat 3, tick 2.",
            "w": "ssot_08 §4 · ruled 9/29",
        },
        "tick": {
            "t": "Tick", "k": "grid",
            "d": "The smallest thing that happens: one line, one gesture, one look. Counted in order, no fixed number per beat.",
            "w": "ssot_08 §3",
        },
        "beat": {
            "t": "Beat", "k": "grid",
            "d": "One action and its reaction. The ladder's R1.",
            "w": "ssot_08 §3 · ssot_01_scale_ladder R1",
        },
        "bar": {
            "t": "Bar", "k": "grid",
            "d": "A run of beats that lands one push: a tactic tried and answered. Sits between beat and scene. Chief's word over 'measure'.",
            "w": "ssot_08 §3 · ruled 9/29",
        },
        "sig": {
            "t": "Time signature", "k": "grid",
            "d": "A scene's meter: beats per bar. 4/4 steady · 3/4 lilting · 7/8 off-balance, a lurch. Set per scene, default 4/4.",
            "w": "ssot_08 §3",
        },
        "tempo": {
            "t": "Tempo", "k": "automation",
            "d": "Two lanes. Planned is the pace you intend. Measured is counted from the draft (beats per 1,000 words). Where they split, the draft drags or rushes.",
            "w": "ssot_08 §7",
        },
        "storypoint": {
            "t": "Story point", "k": "record",
            "d": "One field changing at one time code: a trait ticks, a flag fires, a label lands. Like an Ableton automation point. Values step and hold unless ramp is on.",
            "w": "ssot_08 §5",
        },
        "checkpoint": {
            "t": "Checkpoint", "k": "record",
            "d": "A full state at a fabula event, like an Ableton clip. Story points ride between checkpoints.",
            "w": "ssot_08 §5 · character state v1.2",
        },
        "cable": {
            "t": "Cable", "k": "setup → payoff",
            "d": "A setup linked to its payoff, on any tracks, any distance apart. Rides the fabula's enable edge.",
            "w": "ssot_08 §6",
        },
        "provisional": {
            "t": "Provisional", "k": "cable state",
            "d": "Both ends exist in the story, but at least one time code is still proposed (⧗).",
            "w": "ssot_08 §6 · ruled 9/29",
        },
        "orphan": {
            "t": "Orphan", "k": "cable state",
            "d": "A setup with no payoff, or a payoff with no setup. Drawn as a dangling cable with a red end.",
            "w": "ssot_08 §6",
        },
        "told": {
            "t": "Told order", "k": "ruler",
            "d": "The order and speed the audience gets the story. Runs on the grid.",
            "w": "ssot_08 §2",
        },
        "world": {
            "t": "World clock", "k": "ruler",
            "d": "When things actually happened: backstory, M1, M2… No bars, no tempo. Nobody experiences world time at a pace.",
            "w": "ssot_08 §2 · fabula",
        },
        "stack": {
            "t": "Stack", "k": "ruler",
            "d": "Both rulers at once, with a line from each told scene down to its world event. A flashback is a line that runs backward.",
            "w": "ssot_08 §2 · ruled 9/29",
        },
        "ramp": {
            "t": "Ramp", "k": "value behavior",
            "d": "A value that slopes between two points (tension, exposure, dread). Everything else steps and holds.",
            "w": "ssot_08 §5",
        },
        "freedom": {
            "t": "The Freedom scale", "k": "theme",
            "d": "Tori's value gauge. Two tracks here: in-world (what the system records) and audience (what the reader sees). The gap is the ironic charge.",
            "w": "ssot_06 · the value scale",
        },
        "toldzoom": {
            "t": "Zoom stops", "k": "ladder",
            "d": "The scroll wheel walks the ladder: tick · beat · bar · scene · sequence · movement · story. Zoomed out, story points bundle into a count.",
            "w": "ssot_08 §4",
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

# the playhead inspector's base records (BOLO 90 step 7), keyed by the same
# subject id the tracking file's story_points use.
AR_BASES = {
    "character:victoria_midnight": parse_character_base(CHARACTER_NODE_MD),
    "place:dcus": parse_place_base(SETTING_SYSTEM_MD),
}

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
    "tracking": TRACKING,
    "ar_ledger": AR_LEDGER,
    "bases": AR_BASES,
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
        "told_scenes": len(TRACKING["scenes"]),
        "told_points": len(TRACKING["points"]),
    },
}

DATA_JSON = json.dumps(DATA, ensure_ascii=False).replace("</script>", "<\\/script>")

# ------------------------------------------------------------------ HTML ---

STYLE = r"""
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
  /* ---- tokens, lifted from SITREP.html: the Command's own palette (RULED 9/10 default colorway, 9/11 dark-only) ---- */
  :root {
    --bg: #0F1216; --panel: #171B21; --panel-2: #1F242C; --well: #12161B;
    --ink: #E8EAEE; --ink-2: #A9B0BC; --ink-3: #7B8492;
    --accent: #FF6B35; --accent-ink: #FF8F62; --accent-soft: #3A2117;
    --link: #FF8F62; --good: #5CC48A; --good-soft: #16301F; --warn: #D9C48A; --warn-soft: #3A3320; --bad: #E9788A; --bad-soft: #3A1B20; --help: #A9B0BC;
    --mark: #3A3320;
    --c-char: #7FB2E5; --c-char-soft: #1B2A3A;
    --c-place: #D2AE72; --c-place-soft: #33291A;
    --c-theme: #B89AE6; --c-theme-soft: #2A2238;
    --c-trope: #6CC4A1; --c-trope-soft: #16302A;
    --line: #2B313B; --line-2: #3C4452;
    --grid: color-mix(in srgb, var(--ink) 8%, transparent);
    --shadow: 0 1px 2px rgba(0,0,0,.4), 0 8px 24px rgba(0,0,0,.35);
    --display: "Barlow Condensed", "Arial Narrow", "Helvetica Neue", Arial, sans-serif;
    --body: "Atkinson Hyperlegible", "Segoe UI", Verdana, sans-serif;
    --mono: "IBM Plex Mono", "SFMono-Regular", Consolas, "Liberation Mono", monospace;
    color-scheme: dark;
  }
  :root[data-theme="light"] {
    --bg: #D8D8D2; --panel: #E4E4DE; --panel-2: #CBCBC4; --well: #D0D0C9;
    --ink: #1B1B19; --ink-2: #44453F; --ink-3: #6B6C65;
    --accent: #E04E18; --accent-ink: #A83409; --accent-soft: #E9D5CA;
    --link: #A83409; --good: #1F6B45; --good-soft: #CFE0D3; --warn: #5E4F22; --warn-soft: #E2D9BE; --bad: #962C37; --bad-soft: #E6CCCF; --help: #44453F;
    --mark: #E2D9BE;
    --c-char: #2F5F8F; --c-char-soft: #C9D3DC;
    --c-place: #7A5A1E; --c-place-soft: #DCD2BE;
    --c-theme: #5E4394; --c-theme-soft: #D3CCDD;
    --c-trope: #1E6B52; --c-trope-soft: #C6D8CF;
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

  /* ---- app frame (canvas-first: side rails + log start collapsed, BOLO 79 call 79-B) ---- */
  .app {
    height: 100%; display: grid;
    --w-ol: 0px; --w-det: 0px;
    grid-template-rows: 44px minmax(0,1fr) auto;
    grid-template-columns: var(--w-ol) minmax(0,1fr) var(--w-det);
    grid-template-areas: "head head head" "ol canvas detail" "foot foot foot";
  }
  .app.show-ol { --w-ol: 210px; }
  .app.show-det { --w-det: 320px; }
  .app.maximized { --w-ol: 0px !important; --w-det: 0px !important; }
  /* the thin one-strip header (~44px), ported from The Arrangement (BOLO 79 ruled 9/29) — one strip for the whole app */
  header.head {
    grid-area: head; height: 44px; display: flex; align-items: stretch; gap: 0; border-bottom: 1px solid var(--line-2);
    background: color-mix(in srgb, var(--panel) 85%, transparent); overflow-x: auto; overflow-y: hidden; scrollbar-width: none;
  }
  .brand { display: flex; align-items: center; gap: 8px; padding: 0 14px; border-right: 1px solid var(--line); white-space: nowrap; flex: 0 0 auto; }
  .brand i { width: 9px; height: 9px; background: var(--accent); display: inline-block; transform: translateY(-1px); }
  .brand b { font-family: var(--display); font-weight: 800; font-size: 18px; text-transform: uppercase; letter-spacing: .02em; }
  nav.lenses { display: flex; align-items: stretch; gap: 0; flex: 0 0 auto; }
  nav.lenses button { height: 100%; display: flex; align-items: center; font-family: var(--display); font-weight: 700; font-size: 13.5px; text-transform: uppercase; letter-spacing: .03em; padding: 0 13px; border-right: 1px solid var(--line); color: var(--ink-2); white-space: nowrap; }
  nav.lenses button .k { display: inline-block; margin-left: 7px; font-family: var(--mono); font-size: 9.5px; font-weight: 500; letter-spacing: .06em; color: var(--ink-3); border: 1px solid var(--line-2); padding: 1px 5px; border-radius: 2px; }
  nav.lenses button:hover { color: var(--ink); background: var(--panel-2); }
  nav.lenses button.on { color: var(--accent); background: var(--panel-2); box-shadow: inset 0 -3px 0 var(--accent); }
  nav.lenses button.on .k { color: var(--accent-ink); border-color: var(--accent-ink); }
  .headspace { flex: 1 1 auto; }
  .char-btn { height: 100%; display: flex; align-items: center; font-family: var(--display); font-weight: 700; font-size: 13px; text-transform: uppercase; padding: 0 15px; border-left: 1px solid var(--line); color: var(--ink-2); white-space: nowrap; flex: 0 0 auto; }
  .char-btn:hover, .char-btn.on { color: var(--accent); }
  .paneltoggles { display: flex; align-items: stretch; flex: 0 0 auto; }
  .ptbtn { height: 100%; display: flex; align-items: center; font-family: var(--mono); font-size: 10.5px; letter-spacing: .04em; padding: 0 9px; border-left: 1px solid var(--line); color: var(--ink-2); white-space: nowrap; }
  .ptbtn:hover { color: var(--ink); background: var(--panel-2); }
  .ptbtn.on { color: var(--accent); background: var(--panel-2); box-shadow: inset 0 -3px 0 var(--accent); }

  /* ---- outliner (left rail, CK3 R12) — hidden unless .app.show-ol ---- */
  aside.ol { display: none; grid-area: ol; border-right: 1px solid var(--line-2); overflow-y: auto; padding: 12px 0 16px; background: color-mix(in srgb, var(--panel) 55%, transparent); }
  .app.show-ol aside.ol { display: block; }
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

  /* ---- fabula timeline (call 79-1: era bands sized by content, events spread + truncated) ---- */
  .fab-scroll { overflow-x: auto; padding-bottom: 6px; }
  .fab-track { position: relative; min-width: 1240px; height: 260px; }
  .era-band { position: absolute; top: 30px; height: 90px; border: 1px dashed var(--line-2); background: color-mix(in srgb, var(--accent) 6%, transparent); border-radius: 3px; }
  .era-band .lbl2 { position: absolute; top: -20px; left: 6px; font-family: var(--display); font-weight: 700; font-size: 14px; text-transform: uppercase; color: var(--ink-2); white-space: nowrap; }
  .era-band.stub .lbl2 { font-size: 12px; }
  .era-band.later { background: color-mix(in srgb, var(--c-theme) 7%, transparent); border-color: color-mix(in srgb, var(--c-theme) 45%, var(--line-2)); }
  .era-band .fz { position: absolute; top: 20px; bottom: 6px; left: 6px; right: 6px; font-family: var(--mono); font-size: 9.5px; line-height: 1.25; color: var(--ink-3); white-space: normal; overflow-wrap: anywhere; overflow: hidden; }
  .movement-axis { position: absolute; top: 150px; left: 0; right: 0; height: 2px; background: var(--line-2); }
  .movement-axis .tick { position: absolute; top: -4px; width: 1px; height: 10px; background: var(--line-2); }
  .movement-axis .tick span { position: absolute; top: 12px; left: -12px; font-family: var(--mono); font-size: 11px; color: var(--ink-3); }
  .ev-dot { position: absolute; top: 138px; width: 22px; height: 22px; margin-left: -11px; border-radius: 50%; background: var(--panel); border: 2px solid var(--accent); display: grid; place-items: center; }
  .ev-dot::after { content: ""; width: 8px; height: 8px; border-radius: 50%; background: var(--accent); }
  .ev-dot.on { box-shadow: 0 0 0 4px color-mix(in srgb, var(--accent) 30%, transparent); }
  .ev-dot.repeat { border-style: dashed; }
  .ev-label { position: absolute; top: 168px; text-align: center; font-size: 12px; color: var(--ink-2); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .fab-legend { margin-top: 8px; }

  /* ---- rails grid ---- */
  .rails-toolbar { display: flex; align-items: center; gap: 14px; flex-wrap: wrap; margin-bottom: 14px; }
  .rails-toolbar input[type=text] { font: 14px var(--body); padding: 6px 10px; border: 1px solid var(--line-2); background: var(--panel); color: var(--ink); min-width: 180px; }
  .fam-filter { display: flex; gap: 6px; flex-wrap: wrap; }
  .fam-filter button { font-family: var(--mono); font-size: 10.5px; letter-spacing: .08em; text-transform: uppercase; padding: 4px 9px; border: 1px solid var(--line-2); color: var(--ink-2); }
  .fam-filter button.on { border-color: var(--accent); color: var(--accent); }
  .explore-toggle { display: flex; align-items: center; gap: 6px; font-family: var(--mono); font-size: 11px; color: var(--ink-3); margin-left: auto; }
  .explore-toggle input { accent-color: var(--ink-3); }
  .zoom-ctl { display: flex; align-items: center; gap: 8px; }
  .zoom-ctl button { font-family: var(--mono); font-size: 11px; padding: 4px 10px; border: 1px solid var(--line-2); color: var(--ink-2); }
  .zoom-ctl button.on { border-color: var(--accent); color: var(--accent); }

  .tl-legend { display: flex; flex-wrap: wrap; gap: 12px; margin: 0 0 10px; }
  .tl-chip { display: inline-flex; align-items: center; gap: 5px; font-family: var(--mono); font-size: 10.5px; color: var(--ink-2); }
  .tl-chip i { width: 9px; height: 9px; border-radius: 50%; background: var(--tlc); display: inline-block; }

  .signpost-grid { display: grid; grid-template-columns: 130px repeat(4, minmax(150px,1fr)); gap: 6px; min-width: 760px; margin-bottom: 22px; }
  .sp-corner { }
  .sp-act-hd { font-family: var(--mono); font-size: 10.5px; letter-spacing: .1em; text-transform: uppercase; color: var(--ink-3); align-self: end; padding: 4px 6px; }
  .sp-row-hd { display: flex; flex-direction: column; justify-content: center; font-family: var(--display); font-weight: 800; font-size: 16px; text-transform: uppercase; padding: 8px; border-left: 3px solid var(--tlc, transparent); }
  .sp-row-hd small { font-family: var(--mono); font-size: 9.5px; color: var(--ink-3); font-weight: 400; text-transform: none; letter-spacing: 0; overflow-wrap: anywhere; }
  .sig-cell { min-height: 64px; border: 1px solid var(--line-2); border-radius: 3px; padding: 8px; text-align: left; font-size: 12.5px; color: var(--ink-3); background: var(--panel); overflow-wrap: anywhere; }
  .sig-cell.empty { border-style: dashed; opacity: .7; cursor: help; }
  .sig-cell.filled { border-color: var(--accent); background: var(--accent-soft); color: var(--ink); cursor: pointer; }
  .sig-cell.filled b { display: block; font-family: var(--display); font-size: 13.5px; color: var(--accent-ink); text-transform: none; }
  .sig-cell.on { box-shadow: 0 0 0 3px color-mix(in srgb, var(--accent) 40%, transparent); }
  .sig-chip { display: inline-block; margin-top: 4px; font-family: var(--mono); font-size: 9.5px; padding: 1px 6px; border: 1px solid currentColor; color: var(--good); }
  .sig-chip.gap { color: var(--ink-3); }
  .sig-count { display: inline-flex; align-items: center; gap: 4px; font-family: var(--mono); font-size: 10px; color: var(--ink-3); margin-top: 6px; }
  .sig-count::before { content: ""; width: 7px; height: 7px; border-radius: 50%; background: var(--tlc, var(--ink-3)); display: inline-block; flex: 0 0 auto; }

  .node-cols { display: grid; grid-template-columns: repeat(5, minmax(160px, 1fr)); gap: 14px; min-width: 760px; }
  .node-col h3 { margin: 0 0 4px; font-family: var(--display); font-weight: 700; font-size: 15px; text-transform: uppercase; }
  .node-col .cnt { font-family: var(--mono); font-size: 10.5px; color: var(--ink-3); margin-bottom: 8px; }
  .node-cluster { display: flex; flex-wrap: wrap; gap: 6px; max-height: 420px; overflow-y: auto; padding-right: 4px; }
  .node-chip { font-family: var(--mono); font-size: 11px; padding: 4px 8px; border: 1px solid var(--line-2); border-left: 3px solid var(--tlc, var(--line-2)); color: var(--ink-2); background: var(--panel); cursor: pointer; }
  .node-chip .tlc { font-size: 9.5px; color: var(--accent-ink); }
  .node-chip:hover { border-color: var(--link); color: var(--ink); }
  .node-chip.on { border-color: var(--accent); color: var(--accent); background: var(--accent-soft); }
  .provisional { margin: 10px 0 16px; font-family: var(--mono); font-size: 11px; color: var(--warn); overflow-wrap: anywhere; }

  /* ---- told view: The Arrangement, ported (BOLO 90 × 79, ruled 9/29) ---- */
  .told-toolbar { display: flex; align-items: center; gap: 14px; flex-wrap: wrap; margin-bottom: 10px; }
  .told-toolbar .seg { display: flex; border: 1px solid var(--line-2); }
  .told-toolbar .seg button { font-family: var(--mono); font-size: 10.5px; letter-spacing: .06em; text-transform: uppercase; padding: 5px 9px; color: var(--ink-2); white-space: nowrap; }
  .told-toolbar .seg button + button { border-left: 1px solid var(--line-2); }
  .told-toolbar .seg button[aria-pressed="true"] { background: var(--accent); color: #fff; }
  .told-tc { margin-left: auto; display: flex; align-items: baseline; gap: 8px; white-space: nowrap; }
  .told-tc small { font-family: var(--mono); font-size: 10px; letter-spacing: .12em; text-transform: uppercase; color: var(--ink-3); }
  .told-tc b { font-family: var(--mono); font-weight: 500; font-size: 15px; color: var(--accent-ink); }
  .told-empty { padding: 14px 2px; font-family: var(--mono); font-size: 12px; color: var(--ink-3); }

  .ar-wrap { display: grid; grid-template-columns: 172px minmax(0,1fr); border: 1px solid var(--line-2); min-width: 620px; }
  .ar-tracks { position: relative; border-right: 1px solid var(--line-2); background: var(--panel); overflow: hidden; height: 560px; }
  .ar-th { position: absolute; left: 0; right: 0; display: flex; flex-direction: column; justify-content: center; padding: 0 8px 0 10px; border-bottom: 1px solid var(--line); overflow: hidden; }
  .ar-th::before { content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 3px; background: var(--k, var(--line-2)); }
  .ar-th .nm { font-family: var(--display); font-weight: 700; font-size: 13.5px; line-height: 1.05; text-transform: uppercase; letter-spacing: .02em; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .ar-th .sub { font-family: var(--mono); font-size: 9.5px; color: var(--ink-3); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .ar-th.ruler { background: var(--panel-2); }
  .ar-th.ar-th-pick { cursor: pointer; }
  .ar-th.ar-th-sel { background: color-mix(in srgb, var(--k, var(--accent)) 12%, transparent); }
  .ar-th.ar-th-sel .nm { color: var(--accent-ink); }
  .ar-th .ar-resize { position: absolute; left: 0; right: 0; bottom: -3px; height: 7px; cursor: row-resize; z-index: 2; }
  .ar-th .ar-resize::after { content: ""; position: absolute; left: 40%; right: 40%; top: 3px; height: 1px; background: var(--ink-3); opacity: 0; }
  .ar-th:hover .ar-resize::after, .ar-th .ar-resize:hover::after { opacity: 1; }
  .ar-th .ar-resize:hover { background: color-mix(in srgb, var(--accent) 35%, transparent); }
  .ar-lane { position: relative; overflow: hidden; background: var(--well); cursor: crosshair; touch-action: none; height: 560px; }
  svg.ar-svg { display: block; width: 100%; height: 100%; }
  svg.ar-svg text { font-family: var(--mono); font-size: 10px; fill: var(--ink-2); }
  .ar-band { fill: var(--panel-2); }
  .ar-band-lbl { font-family: var(--display); font-weight: 700; font-size: 12px; letter-spacing: .04em; fill: var(--ink); text-transform: uppercase; }
  .ar-grid-bar { stroke: var(--line-2); stroke-width: 1; }
  .ar-grid-beat { stroke: var(--line); stroke-width: 1; }
  .ar-rowline { stroke: var(--line); }
  .ar-clip { stroke-width: 1; }
  .ar-clip-lbl { font-family: var(--body); font-size: 11px; fill: var(--ink); }
  .ar-sig { font-family: var(--mono); font-size: 10px; fill: var(--accent-ink); font-weight: 500; }
  .ar-pt { stroke: var(--bg); stroke-width: 1.5; cursor: pointer; }
  .ar-pt:hover { stroke: var(--ink); }
  .ar-badge { fill: var(--panel); stroke: var(--line-2); }
  .ar-badge-t { font-size: 10px; fill: var(--ink); font-weight: 500; }
  .ar-cable { fill: none; stroke-width: 2; cursor: pointer; }
  .ar-cable.provisional { stroke-dasharray: 6 5; }
  .ar-orphan { fill: var(--bad); }
  .ar-playhead { stroke: var(--accent); stroke-width: 1.5; }
  .ar-ph-cap { fill: var(--accent); }
  .ar-auto-fill { opacity: .18; }
  .ar-gap { fill: var(--bad); opacity: .16; }
  .ar-world-ev { stroke-width: 1; }
  .ar-link { fill: none; stroke: var(--ink-3); stroke-width: 1.2; opacity: .7; }
  .ar-link.back { stroke: var(--accent); opacity: .95; stroke-width: 2; }
  .ar-pt.selected { stroke: #fff; stroke-width: 2.5; }
  .ar-pt-pending-ring { fill: none; stroke: var(--accent-ink); stroke-width: 1.5; stroke-dasharray: 3 2; pointer-events: none; }
  .ar-flag-pt { fill: var(--bad); stroke: var(--bg); stroke-width: 1.5; stroke-dasharray: 2 2; cursor: help; }
  .ar-flag-cable { fill: none; stroke: var(--bad); stroke-width: 2; stroke-dasharray: 3 3; cursor: help; }
  .ar-cable.pending { stroke-dasharray: 5 4 !important; }
  .ar-cable.selected { stroke-width: 3.5; }

  /* ---- edit layer chrome (BOLO 90 step 6, RULED 9/29 · the edit contract) ---- */
  .told-edit-seg button[data-e="edit"][aria-pressed="true"] { background: var(--good); color: #06170F; }
  .told-edit-seg button[data-e="cable"][aria-pressed="true"] { background: var(--accent); color: #fff; }
  .told-pending-btn { font-family: var(--mono); font-size: 10.5px; letter-spacing: .04em; padding: 5px 9px; border: 1px dashed var(--accent-ink); color: var(--accent-ink); background: var(--accent-soft); white-space: nowrap; }
  .told-pending-btn:hover { border-style: solid; }
  .told-readonly { font-family: var(--mono); font-size: 10.5px; letter-spacing: .08em; text-transform: uppercase; color: var(--ink-3); border: 1px solid var(--line-2); padding: 4px 8px; white-space: nowrap; }
  .told-msg { font-family: var(--mono); font-size: 11px; color: var(--warn); white-space: nowrap; }

  .told-addform, .told-history { position: fixed; z-index: 90; background: var(--panel); border: 1px solid var(--line-2); border-top: 3px solid var(--accent); box-shadow: var(--shadow); padding: 10px 12px; font-size: 13px; }
  .told-addform { width: 240px; display: grid; gap: 7px; }
  .told-addform label { display: block; font-family: var(--mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; color: var(--ink-3); margin-bottom: 2px; }
  .told-addform input { width: 100%; font: 13px var(--body); padding: 5px 7px; border: 1px solid var(--line-2); background: var(--well); color: var(--ink); }
  .told-addform .row { display: flex; gap: 8px; justify-content: flex-end; margin-top: 4px; }
  .told-addform button { font-family: var(--mono); font-size: 11px; text-transform: uppercase; padding: 5px 10px; border: 1px solid var(--line-2); }
  .told-addform button.go { border-color: var(--accent); color: var(--accent); }

  .told-history { width: 360px; max-height: 60vh; overflow-y: auto; }
  .told-history h4 { margin: 0 0 8px; font-family: var(--display); font-weight: 700; font-size: 15px; text-transform: uppercase; }
  .told-history .hrow { display: grid; grid-template-columns: 1fr auto; gap: 2px 10px; padding: 6px 0; border-top: 1px solid var(--line); font-size: 12px; }
  .told-history .hrow:first-of-type { border-top: 0; }
  .told-history .hop { font-family: var(--mono); font-size: 10px; text-transform: uppercase; color: var(--ink-3); }
  .told-history .htarget { overflow-wrap: anywhere; }
  .told-history .hstate { font-family: var(--mono); font-size: 9.5px; text-transform: uppercase; letter-spacing: .06em; padding: 1px 6px; border: 1px solid currentColor; white-space: nowrap; align-self: start; }
  .told-history .hstate.pending { color: var(--accent-ink); }
  .told-history .hstate.applied { color: var(--good); }
  .told-history .hstate.undone, .told-history .hstate.undone-pending { color: var(--ink-3); }
  .told-history .hstate.flagged { color: var(--bad); }
  .told-history .hreason { grid-column: 1 / -1; font-size: 11.5px; color: var(--bad); }
  .told-history .hclose { position: absolute; top: 6px; right: 8px; font-family: var(--mono); font-size: 11px; color: var(--ink-3); }

  /* the playhead inspector — replaces the selection card while the Told view is open */
  .told-insp .grp { display: grid; gap: 6px; }
  .told-insp .grp > .glbl { font-family: var(--mono); font-size: 10px; letter-spacing: .14em; text-transform: uppercase; color: var(--ink-3); border-bottom: 1px solid var(--line); padding-bottom: 4px; display: flex; gap: 8px; align-items: center; }
  .told-insp .grp > .glbl i { width: 8px; height: 8px; display: inline-block; background: var(--k); }
  .told-insp .kv { display: grid; grid-template-columns: minmax(0,1fr) auto; gap: 3px 10px; font-size: 13px; }
  .told-insp .kv dt { color: var(--ink-2); font-family: var(--mono); font-size: 11px; padding-top: 1px; overflow-wrap: anywhere; }
  .told-insp .kv dd { margin: 0; text-align: right; color: var(--ink); }
  .told-insp .kv dd.chg { color: var(--accent-ink); }
  .told-insp .kv dd.pending { border-bottom: 1px dashed var(--warn); padding-bottom: 1px; }
  .told-insp .kv dt.base-only { color: var(--ink-3); }
  .told-insp .meter { height: 6px; background: var(--well); border: 1px solid var(--line); position: relative; margin-top: 2px; }
  .told-insp .meter b { position: absolute; left: 0; top: 0; bottom: 0; background: var(--c-char); }
  .told-insp .chip { display: inline-flex; align-items: center; gap: 5px; font-family: var(--mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; padding: 1px 7px; border: 1px solid currentColor; white-space: nowrap; }
  .told-insp .chip.prov { color: var(--warn); border-style: dashed; }
  .told-insp .chip.orph { color: var(--bad); }
  .told-insp .chip.ok { color: var(--good); }
  .told-insp .chip.who { all: unset; display: inline-flex; align-items: center; gap: 5px; font-family: var(--mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; padding: 1px 7px; border: 1px solid var(--line); color: var(--ink-2); cursor: pointer; white-space: nowrap; }
  .told-insp .chip.who.on { color: var(--ink); border-color: var(--accent); }
  .told-insp .chip.who:hover { border-color: var(--accent-ink); }
  .told-insp .cab { display: grid; gap: 3px; padding: 7px 8px; border: 1px solid var(--line); background: var(--well); font-size: 12px; margin-bottom: 6px; }
  .told-insp .cab b { font-weight: 700; }

  /* ---- detail rail (selection-only inspector, call 79-3) — hidden unless .app.show-det ---- */
  aside.detail { display: none; grid-area: detail; border-left: 1px solid var(--line-2); overflow-y: auto; overflow-wrap: anywhere; padding: 16px 16px 22px; background: color-mix(in srgb, var(--panel) 55%, transparent); }
  .app.show-det aside.detail { display: block; }
  .detail-tabs { display: flex; gap: 0; margin-bottom: 12px; border-bottom: 1px solid var(--line); }
  .detail-tabs button { font-family: var(--mono); font-size: 11px; letter-spacing: .08em; text-transform: uppercase; padding: 6px 10px; color: var(--ink-2); border-bottom: 2px solid transparent; }
  .detail-tabs button.on { color: var(--accent); border-bottom-color: var(--accent); }
  .dcard h3 { margin: 0 0 2px; font-family: var(--display); font-weight: 700; font-size: 20px; text-transform: uppercase; overflow-wrap: anywhere; }
  .dcard .kind { font-family: var(--mono); font-size: 10.5px; color: var(--ink-3); text-transform: uppercase; letter-spacing: .1em; margin-bottom: 10px; }
  .dcard dl { margin: 10px 0 0; display: grid; gap: 8px; }
  .dcard dt { font-family: var(--mono); font-size: 10px; letter-spacing: .1em; text-transform: uppercase; color: var(--ink-3); }
  .dcard dd { margin: 2px 0 0; font-size: 13.5px; line-height: 1.45; overflow-wrap: anywhere; }
  .dcard .src { margin-top: 14px; font-family: var(--mono); font-size: 10.5px; color: var(--ink-3); overflow-wrap: anywhere; }
  .empty-detail { font-size: 13.5px; color: var(--ink-3); }
  .more-block { margin-top: 10px; border-top: 1px dashed var(--line); padding-top: 8px; }
  .more-block summary { cursor: pointer; font-family: var(--mono); font-size: 10.5px; letter-spacing: .08em; text-transform: uppercase; color: var(--ink-3); }
  .more-block summary:hover { color: var(--ink-2); }
  .more-block dl { margin-top: 8px; }

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
  .trait { overflow-wrap: anywhere; }
  .trait b { display: block; font-family: var(--mono); font-size: 10px; letter-spacing: .08em; }
  .trait .tn { font-family: var(--display); font-weight: 700; text-transform: uppercase; font-size: 13px; }

  /* ---- footer: Info View strip (Ableton) + event log as a toggled tab (call 79-4) ---- */
  footer.footbar { grid-area: foot; border-top: 1px solid var(--line-2); background: color-mix(in srgb, var(--panel) 85%, transparent); display: flex; flex-direction: column; }
  .logpanel { display: none; flex-direction: column; max-height: 140px; border-bottom: 1px solid var(--line); }
  .app.show-log .logpanel { display: flex; }
  .log-bar { display: flex; align-items: center; gap: 10px; padding: 6px 14px; border-bottom: 1px solid var(--line); flex-wrap: wrap; }
  .log-bar .lbl { margin-right: 4px; }
  .log-filter { display: flex; gap: 4px; }
  .log-filter button { font-family: var(--mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; padding: 2px 7px; border: 1px solid var(--line-2); color: var(--ink-2); }
  .log-filter button.on { border-color: var(--accent); color: var(--accent); }
  .log-rows { overflow-y: auto; padding: 4px 14px 8px; font-family: var(--mono); font-size: 11.5px; }
  .log-row { display: grid; grid-template-columns: 46px 60px 1fr; gap: 10px; padding: 3px 0; color: var(--ink-2); overflow-wrap: anywhere; }
  .log-row .n { color: var(--ink-3); }
  .log-row .lens { color: var(--accent-ink); text-transform: uppercase; }
  .infoview { display: flex; align-items: center; gap: 10px; padding: 6px 14px; font-family: var(--mono); font-size: 11.5px; min-height: 20px; }
  .infoview .iv-icon { color: var(--accent); font-weight: 700; flex: 0 0 auto; }
  .infoview #ivText { flex: 1 1 auto; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: var(--ink); }
  .infoview .footer-hint { flex: 0 0 auto; color: var(--ink-3); font-size: 10px; white-space: nowrap; }

  /* ---- tooltips (CK3 R2-R4) ---- */
  .tip { position: fixed; z-index: 80; width: 320px; max-width: calc(100vw - 24px); background: var(--panel); border: 1px solid var(--line-2); border-top: 3px solid var(--accent); box-shadow: var(--shadow); padding: 10px 12px 8px; font-size: 13.5px; line-height: 1.4; }
  .tip .th { display: flex; align-items: baseline; gap: 8px; margin-bottom: 4px; flex-wrap: wrap; }
  .tip .th b { font-family: var(--display); font-weight: 700; font-size: 17px; text-transform: uppercase; }
  .tip .th .k { font-family: var(--mono); font-size: 9.5px; letter-spacing: .1em; text-transform: uppercase; color: var(--ink-3); }
  .tip p { margin: 0; overflow-wrap: anywhere; }
  .tip ul.tlist { margin: 8px 0 0; padding: 0; list-style: none; display: grid; gap: 4px; }
  .tip ul.tlist li { border-left: 2px solid var(--line-2); padding-left: 6px; overflow-wrap: anywhere; }
  .tip .or-line, .dcard .or-line { margin: 4px 0 0; font-family: var(--mono); font-size: 11px; color: var(--ink-3); font-style: italic; }
  .tip .more { margin-top: 6px; font-family: var(--mono); font-size: 10.5px; color: var(--ink-3); }
  .tip .w { margin-top: 8px; font-family: var(--mono); font-size: 10.5px; color: var(--ink-3); overflow-wrap: anywhere; }
  .tip.locked { border-top-color: var(--ink); }
  .tip .hint2 { font-family: var(--mono); font-size: 9.5px; color: var(--ink-3); margin-top: 8px; letter-spacing: .04em; }
  .tip .capped { font-family: var(--mono); font-size: 10.5px; color: var(--ink-3); font-style: italic; }

  /* ---- phone tab bar ---- */
  nav.tabbar { display: none; }

  @media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }

  @media (max-width: 600px) {
    .app { grid-template-columns: 1fr !important; grid-template-rows: auto minmax(0,1fr) auto auto; grid-template-areas: "head" "canvas" "foot" "tabbar"; }
    nav.lenses { display: none; }
    .paneltoggles .ptbtn[data-p="ol"], .paneltoggles .ptbtn[data-p="det"] { display: block; }
    aside.ol, aside.detail { position: fixed; top: 48px; bottom: 40px; left: 0; right: 0; z-index: 60; width: auto; }
    aside.detail { border-left: 0; border-top: 1px solid var(--line-2); }
    .logpanel { max-height: 96px; }
    .infoview .footer-hint { display: none; }
    nav.tabbar { display: flex; grid-area: tabbar; border-top: 1px solid var(--line-2); background: var(--panel); }
    nav.tabbar button { flex: 1 1 0; font-family: var(--display); font-weight: 700; font-size: 13px; text-transform: uppercase; padding: 10px 0; color: var(--ink-2); }
    nav.tabbar button.on { color: var(--accent); box-shadow: inset 0 3px 0 var(--accent); }
    main.canvas { padding: 12px 14px 18px; }
    .fab-scroll, .signpost-grid, .node-cols, .ar-wrap { overflow-x: auto; }
    .ar-tracks, .ar-lane { height: 420px; }
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
      <button data-lens="fabula" class="on" title="Map workspace — key 1">Fabula<span class="k">1</span></button>
      <button data-lens="rails" title="Seat workspace — key 2">Rails<span class="k">2</span></button>
      <button data-lens="told" title="Write workspace — key 3">Told<span class="k">3</span></button>
    </nav>
    <div class="headspace"></div>
    <div class="paneltoggles" id="panelToggles">
      <button class="ptbtn" data-p="ol" title="Outliner — key [">[ Outliner</button>
      <button class="ptbtn" data-p="det" title="Inspector — key ]">] Inspector</button>
      <button class="ptbtn" data-p="log" title="Event log — key L">L Log</button>
      <button class="ptbtn" data-p="max" title="Maximize canvas — key &#96;">&#96; Max</button>
    </div>
    <button class="char-btn" id="charBtn">Tori's sheet</button>
  </header>

  <aside class="ol" id="ol"></aside>

  <main class="canvas" id="canvas">
    <section class="lens-view on" id="view-fabula">
      <h2>Fabula — the world timeline</h2>
      <p class="sub">The <span class="t" data-tt="gloss" data-id="fabula">timeline is the map</span>: Tori's six dated-in-story events over three fuzzy DCUS eras, then the universe eras that follow outward from Earth: LAKAD (cislunar space), ASTRO7EX (the Moon), and beyond. No calendar exists for this world — dates are movement-relative or banded, never invented points.</p>
      <div class="fab-scroll"><div class="fab-track" id="fabTrack"></div></div>
      <p class="fab-legend hint">Solid dot = single event &nbsp;·&nbsp; dashed dot = <span class="t" data-tt="gloss" data-id="repeat">repeat / iterative</span> event, one record standing for a repeated class (Genette 1980: 53). Truncated labels — hover or select a dot for the full event id.</p>
    </section>

    <section class="lens-view" id="view-rails">
      <h2>Rails — the trope graph, focus-tree style</h2>
      <p class="sub">16 <span class="t" data-tt="gloss" data-id="signpost">signposts</span> across 4 acts, 4 <span class="t" data-tt="gloss" data-id="throughline">throughlines</span> down. Only the book <span class="t" data-tt="gloss" data-id="node">nodes</span> draw on the grid; <span class="t" data-tt="gloss" data-id="trope">tropes</span> live inside each node's tooltip, capped at six.</p>
      <div class="rails-toolbar">
        <div class="zoom-ctl" id="zoomCtl">
          <span class="lbl">Zoom</span>
          <button data-z="out" class="on" title="Zoom out — key -">− cells</button>
          <button data-z="in" title="Zoom in — key =">+ chips</button>
        </div>
      </div>
      <h3 class="lbl" style="margin:0 0 8px">The signposts — fixed rail</h3>
      <div class="tl-legend" id="tlLegend"></div>
      <div class="signpost-grid" id="signpostGrid"></div>
      <div id="nodeSection">
        <div class="rails-toolbar">
          <input type="text" id="nodeSearch" placeholder="search nodes…">
          <div class="fam-filter" id="famFilter"></div>
          <label class="explore-toggle"><input type="checkbox" disabled> Explore (free network) — later feature</label>
        </div>
        <h3 class="lbl" style="margin:0 0 4px">The book nodes — seated by act and throughline</h3>
        <p class="provisional">seated 9/24 (call 77-I) on the ruled Bourne map · seat calls 1–3 RULED 9/24 · left border color = throughline, the small tag is its code</p>
        <div class="node-cols" id="nodeCols"></div>
      </div>
    </section>

    <section class="lens-view" id="view-told">
      <h2>Told — The Arrangement</h2>
      <p class="sub" id="toldSub">The <span class="t" data-tt="gloss" data-id="told">told order</span> the audience gets it in, on the <span class="t" data-tt="gloss" data-id="timecode">grid</span> — <span class="t" data-tt="gloss" data-id="bar">bar</span>.<span class="t" data-tt="gloss" data-id="beat">beat</span>.<span class="t" data-tt="gloss" data-id="tick">tick</span>. From <span class="mono">ShroomsQ/_CANON/_TRACKING/oxo.yaml</span> plus any pending edits. A lane with no data draws nothing — never a fake line.</p>
      <div class="told-toolbar" id="toldToolbar">
        <div class="seg" role="group" aria-label="Told ruler" id="toldRulerSeg">
          <button data-v="told" aria-pressed="true" class="t" data-tt="gloss" data-id="told">Told order</button>
          <button data-v="world" aria-pressed="false" class="t" data-tt="gloss" data-id="world">World clock</button>
          <button data-v="stack" aria-pressed="false" class="t" data-tt="gloss" data-id="stack">Stack</button>
        </div>
        <div class="seg" id="toldZoomSeg"></div>
        <div class="seg told-edit-seg" id="toldEditSeg" hidden>
          <button data-e="edit" aria-pressed="true" title="Toggle edit mode">Edit</button>
          <button data-e="cable" aria-pressed="false" title="Cable tool — or Alt+drag a point">Cable</button>
          <button data-e="undo" title="Undo the newest pending edit — Ctrl+Z">Undo</button>
        </div>
        <button class="told-pending-btn" id="toldPendingBtn" hidden title="Open the edit history">0 edits pending pull</button>
        <span class="told-msg" id="toldMsg" hidden></span>
        <span class="told-readonly" id="toldReadonly" hidden>read-only</span>
        <div class="told-tc"><small class="t" data-tt="gloss" data-id="timecode">Time code</small><b id="toldTcOut">—</b></div>
      </div>
      <div class="ar-wrap" id="arWrap">
        <div class="ar-tracks" id="arTracks" aria-hidden="true"></div>
        <div class="ar-lane" id="arLane"><svg class="ar-svg" id="arSvg" role="img" aria-label="Told-order timeline: scenes, tempo, story points and cables"></svg></div>
      </div>
      <p class="hint" style="margin-top:8px">Key <b class="mono">T</b> flips this ruler (told / world / stack) · wheel to zoom, shift+wheel or drag to pan, click the ruler to move the playhead, ← → step one beat. In edit mode: drag a point to move it, dbl-click a state track to add one, select + Delete to remove, Alt+drag (or the Cable tool) to link a cable, Ctrl+Z to undo.</p>
      <div class="told-addform" id="toldAddForm" hidden></div>
      <div class="told-history" id="toldHistory" hidden></div>
    </section>
  </main>

  <aside class="detail" id="detail"></aside>

  <footer class="footbar" id="footbar">
    <div class="logpanel" id="logpanel">
      <div class="log-bar">
        <span class="lbl">Event log</span>
        <div class="log-filter" id="logFilter"></div>
      </div>
      <div class="log-rows" id="logRows"></div>
    </div>
    <div class="infoview" id="infoView">
      <span class="iv-icon">i</span><span id="ivText">Hover a term, node, event, or cell for its definition.</span>
      <span class="footer-hint">[ outliner &nbsp;·&nbsp; ] inspector &nbsp;·&nbsp; L log &nbsp;·&nbsp; &#96; maximize &nbsp;·&nbsp; 1/2/3 view (Map/Seat/Write) &nbsp;·&nbsp; − / = zoom (Rails) &nbsp;·&nbsp; T ruler (Told)</span>
    </div>
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
function trimJs(s, n){ s = s || ''; return s.length > n ? s.slice(0, n - 1).trimEnd() + '…' : s; }

// throughline color, existing tokens only (call 79-6: color carries throughline, not a text tag alone)
const TL_COLOR = { OS: 'var(--accent)', MC: 'var(--good)', IC: 'var(--warn)', RS: 'var(--bad)' };

// three workspaces bound to the views (call 79-5): Map / Seat / Write panel presets
const WORKSPACE = {
  fabula: { ol: false, det: false },
  rails:  { ol: true,  det: false },
  told:   { ol: false, det: true  },
};

const DEFAULT_INFO = 'Hover a term, node, event, or cell for its definition.';

const state = {
  lens: 'fabula', selection: null, log: [], famOn: null, query: '',
  panels: { ol: false, det: false, log: false },   // canvas-first: all start collapsed (call 79-2)
  maximized: false, railsZoom: 'out', hoverTarget: null,
};

// ---- index helpers ----
const eventsById = {}; DATA.fabula.events.forEach(e => eventsById[e.event_id] = e);
const nodesById = {}; DATA.rails.nodes.forEach(n => nodesById[n.id] = n);
const erasById = {}; DATA.fabula.eras.forEach(e => erasById[e.id] = e);

function logEvent(lens, text){
  state.log.unshift({ n: state.log.length + 1, lens, text, t: new Date() });
  if (state.log.length > 60) state.log.pop();
  renderLog();
}

// ---- panel layout: outliner / inspector / log collapse, maximize hides all three ----
function applyLayout(){
  const app = $('#app');
  app.classList.toggle('maximized', state.maximized);
  app.classList.toggle('show-ol', !state.maximized && state.panels.ol);
  app.classList.toggle('show-det', !state.maximized && state.panels.det);
  app.classList.toggle('show-log', !state.maximized && state.panels.log);
  $$('.ptbtn').forEach(b => {
    const on = b.dataset.p === 'max' ? state.maximized : state.panels[b.dataset.p];
    b.classList.toggle('on', !!on);
  });
  if (state.lens === 'fabula') requestAnimationFrame(renderFabula);
  if (state.lens === 'told') requestAnimationFrame(toldRender);
}
function setPanel(name, val){ state.panels[name] = val; applyLayout(); }
function togglePanel(name){ state.panels[name] = !state.panels[name]; applyLayout(); }
function toggleMaximize(){ state.maximized = !state.maximized; applyLayout(); }
$('#panelToggles').addEventListener('click', e => {
  const b = e.target.closest('.ptbtn'); if (!b) return;
  if (b.dataset.p === 'max') { toggleMaximize(); return; }
  togglePanel(b.dataset.p);
});

function select(type, id, opts){
  opts = opts || {};
  state.selection = { type, id };
  renderDetail();
  highlightSelection();
  setPanel('det', true);  // selection-only inspector opens on selection (call 79-3)
  if (!opts.silent) logEvent(opts.lensLabel || state.lens, describeSelection(type, id));
}
function clearSelection(){
  state.selection = null;
  renderDetail();
  highlightSelection();
  setPanel('det', false);
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
  $$('[data-sel-type].on').forEach(el => el.classList.remove('on'));  // only selection marks; views and filters keep their own .on
  if (!state.selection) return;
  $$(`[data-sel-type="${state.selection.type}"][data-sel-id="${CSS.escape(String(state.selection.id))}"]`).forEach(el => el.classList.add('on'));
  $$(`.lenses button[data-lens="${state.lens}"], nav.tabbar button[data-lens="${state.lens}"]`).forEach(el => el.classList.add('on'));
}

// ---- view switching (machine name: lens): 1/2/3 also apply that workspace's panel layout (call 79-5) ----
function setLens(lens){
  state.lens = lens;
  $$('.lens-view').forEach(v => v.classList.toggle('on', v.id === 'view-' + lens));
  $$('#lensNav button, #tabbar button').forEach(b => b.classList.toggle('on', b.dataset.lens === lens));
  const preset = WORKSPACE[lens] || { ol: false, det: false };
  state.panels.ol = preset.ol;
  state.panels.det = preset.det;
  applyLayout();
  renderOutliner();
  renderDetail();  // told's inspector is playhead-driven, not selection-gated — refresh on every view switch
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

// ---- fabula view (call 79-1: era bands sized by content, events spread + truncated) ----
function renderFabula(){
  const track = $('#fabTrack');
  if (!track || track.offsetParent === null) return;  // hidden view — skip, re-render on show/resize
  const eras = DATA.fabula.eras;
  const dcusEra = eras.find(e => e.id === 'era_dcus');
  const emptyEras = eras.filter(e => e.id !== 'era_dcus' && !e.universe);
  const laterEras = eras.filter(e => e.universe);  // LAKAD · ASTRO7EX · beyond, stacked after DCUS in order
  const LATER = 128;
  const STUB = 96; // px — a narrow fixed stub for eras with no events, label still readable
  let html = '';
  let cum = 0;
  emptyEras.forEach(e => {
    html += `<div class="era-band stub t" data-tt="era" data-id="${e.id}" data-sel-type="era" data-sel-id="${e.id}" tabindex="0" style="left:${cum}px;width:${STUB}px">`
         +  `<span class="lbl2">${esc(e.label)}</span><span class="fz">${esc(e.note)}</span></div>`;
    cum += STUB;
  });
  const dcusLeft = cum;
  html += `<div class="era-band t" id="dcusBand" data-tt="era" data-id="${dcusEra.id}" data-sel-type="era" data-sel-id="${dcusEra.id}" tabindex="0" style="left:${dcusLeft}px;right:${laterEras.length * LATER}px">`
       +  `<span class="lbl2">${esc(dcusEra.label)}</span><span class="fz">${esc(dcusEra.note)}</span></div>`;
  laterEras.forEach((e, i) => {
    html += `<div class="era-band stub later t" data-tt="era" data-id="${e.id}" data-sel-type="era" data-sel-id="${e.id}" tabindex="0" style="right:${(laterEras.length - 1 - i) * LATER}px;width:${LATER - 6}px">`
         +  `<span class="lbl2">${esc(e.label)}</span><span class="fz">${esc(e.note)}</span></div>`;
  });
  html += '<div class="movement-axis" id="movAxis"></div>';
  track.innerHTML = html;

  // the DCUS era carries every event on record — size it by content (the rest of the
  // track), then spread events across each movement's own span so no two share an x
  const dcusBand = $('#dcusBand');
  const dcusWidth = Math.max(dcusBand.offsetWidth, 240);
  const MV_KEYS = ['M1B', 'M2', 'M3'];
  const groups = {}; MV_KEYS.forEach(k => groups[k] = []);
  DATA.fabula.events.forEach(ev => {
    const key = MV_KEYS.find(k => (ev.time.movement || '').indexOf(k) === 0) || 'M2';
    groups[key].push(ev);
  });
  const zoneW = dcusWidth / MV_KEYS.length;
  const axis = $('#movAxis');
  MV_KEYS.forEach((k, zi) => {
    const zoneLeft = dcusLeft + zi * zoneW;
    const tick = document.createElement('div'); tick.className = 'tick'; tick.style.left = (zoneLeft + zoneW / 2) + 'px';
    tick.innerHTML = `<span>${k}</span>`; axis.appendChild(tick);
    const evs = groups[k];
    const slotW = zoneW / Math.max(evs.length, 1);
    evs.forEach((ev, i) => {
      const cx = zoneLeft + slotW * (i + 0.5);
      const dot = document.createElement('div');
      dot.className = 'ev-dot t' + (ev.repeat ? ' repeat' : '');
      dot.style.left = cx + 'px';
      dot.tabIndex = 0;
      dot.dataset.tt = 'event'; dot.dataset.id = ev.event_id;
      dot.dataset.selType = 'event'; dot.dataset.selId = ev.event_id;
      track.appendChild(dot);
      const lab = document.createElement('div');
      lab.className = 'ev-label t';
      lab.dataset.tt = 'event'; lab.dataset.id = ev.event_id;
      lab.dataset.selType = 'event'; lab.dataset.selId = ev.event_id;
      const labW = Math.max(46, Math.min(150, slotW - 8));
      lab.style.left = cx + 'px'; lab.style.width = labW + 'px'; lab.style.marginLeft = (-labW / 2) + 'px';
      lab.textContent = ev.event_id.replace(/_/g, ' ');
      track.appendChild(lab);
    });
  });
}
window.addEventListener('resize', () => { if (state.lens === 'fabula') renderFabula(); });

// ---- rails view ----
function nodeCountFor(tlId, act){ return DATA.rails.nodes.filter(n => n.throughline === tlId && n.column === 'act' + act).length; }
function anyActCountFor(tlId){ return DATA.rails.nodes.filter(n => n.throughline === tlId && n.column === 'side').length; }

function renderTlLegend(){
  const el = $('#tlLegend'); if (!el) return;
  el.innerHTML = DATA.rails.throughlines.map(tl => `<span class="tl-chip" style="--tlc:${TL_COLOR[tl.id]}"><i></i>${esc(tl.id)} · ${esc(tl.name)}</span>`).join('');
}

// semantic zoom (call 79-6): zoomed out shows 16 signpost cells with label + node
// count + throughline color; zoomed in reveals the 135 node chips under their columns
function renderSignpostGrid(){
  const grid = $('#signpostGrid');
  let html = '<div class="sp-corner"></div>';
  DATA.rails.acts.forEach(a => html += `<div class="sp-act-hd">Act ${a} · ${esc((DATA.rails.actMov||{})[a]||'')}</div>`);
  DATA.rails.throughlines.forEach(tl => {
    const anyN = anyActCountFor(tl.id);
    html += `<div class="sp-row-hd t" data-tt="tl" data-id="${tl.id}" tabindex="0" style="--tlc:${TL_COLOR[tl.id]}">${tl.id}<small>${esc(tl.pov)} — ${esc(tl.name)}${anyN ? ' · +' + anyN + ' any-act' : ''}</small></div>`;
    DATA.rails.acts.forEach(a => {
      const key = tl.id + '|' + a;
      const fill = DATA.rails.fill[key];
      const cnt = nodeCountFor(tl.id, a);
      const countTag = `<span class="sig-count" style="--tlc:${TL_COLOR[tl.id]}">${cnt} node${cnt !== 1 ? 's' : ''}</span>`;
      if (fill){
        html += `<button class="sig-cell filled t" data-tt="signpost" data-id="${key}" data-sel-type="signpost" data-sel-id="${key}"><b>${esc(fill.label)}</b>${esc(fill.movement)}<span class="sig-chip">${fill.state==='carded'?'scene carded':'storyform'}</span>${countTag}</button>`;
      } else {
        html += `<div class="sig-cell empty t" data-tt="signpost" data-id="${key}" tabindex="0">no instance found<span class="sig-chip gap">unverified</span>${countTag}</div>`;
      }
    });
  });
  grid.innerHTML = html;
}

function renderNodeColumns(){
  const cols = ['act1','act2','act3','act4','side'];
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
      const col = TL_COLOR[n.throughline] || 'var(--line-2)';
      html += `<button class="node-chip t" data-tt="node" data-id="${n.id}" data-sel-type="node" data-sel-id="${n.id}" style="--tlc:${col}"><span class="tlc">${esc(n.throughline||'')}</span> ${esc(n.name)}</button>`;
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

function setZoom(z){
  state.railsZoom = z;
  $$('#zoomCtl button').forEach(b => b.classList.toggle('on', b.dataset.z === z));
  const sec = $('#nodeSection'); if (sec) sec.style.display = (z === 'in') ? '' : 'none';
}
$('#zoomCtl').addEventListener('click', e => { const b = e.target.closest('button'); if (b) setZoom(b.dataset.z); });

// ==================================================================
// ---- told view: The Arrangement, ported (BOLO 90 × 79, ruled 9/29) ----
// data-driven entirely from DATA.tracking (ShroomsQ/_CANON/_TRACKING/oxo.yaml,
// loaded + validated by tracking.py). A lane with no data draws nothing —
// never a fake line (ruling 3). Edits ride the db and fold in through tracking.py pull (step 6).
// ==================================================================
const TS = DATA.tracking;
const AR_NS = 'http://www.w3.org/2000/svg';
const AR_RULE_H = 30, AR_BAND_H = 22;

// told-order scenes: accumulate beat positions from each scene's own bars × meter
const AR_SCENES = TS.scenes.map(sc => ({ ...sc }));
(function(){ let acc = 0; for (const sc of AR_SCENES) { sc.start = acc; sc.len = sc.num * sc.bars; acc += sc.len; } })();
const AR_TOTAL = Math.max(1, AR_SCENES.reduce((m, sc) => Math.max(m, sc.start + sc.len), 0));
const AR_SCENE_BY_KEY = {}; AR_SCENES.forEach(sc => AR_SCENE_BY_KEY[sc.mv + '|' + sc.q + '|' + sc.s] = sc);
const AR_MOVS = TS.movements.map(m => ({ id: m.id, lbl: m.label }));
const AR_SEQS = TS.sequences.map(s => ({ id: s.id, lbl: s.label }));

function arPos(code){
  const m = (code || '').match(/(M\d+)\s*·\s*(Q\d+)\s*·\s*(S\d+)\s*\|\s*(\d+)\.(\d+)(?:\.(\d+))?/);
  if (!m) return 0;
  const sc = AR_SCENE_BY_KEY[m[1] + '|' + m[2] + '|' + m[3]]; if (!sc) return 0;
  const tick = m[6] ? (+m[6] - 1) * 0.22 : 0;
  return sc.start + (+m[4] - 1) * sc.num + (+m[5] - 1) + Math.min(tick, 0.9);
}
function arCodeAt(p){
  if (!AR_SCENES.length) return null;
  p = Math.max(0, Math.min(AR_TOTAL - 0.001, p));
  const sc = AR_SCENES.find(s => p >= s.start && p < s.start + s.len) || AR_SCENES[AR_SCENES.length - 1];
  const inS = p - sc.start;
  const bar = Math.floor(inS / sc.num) + 1, beat = Math.floor(inS % sc.num) + 1;
  return { sc, text: `${sc.mv} · ${sc.q} · ${sc.s} | ${String(bar).padStart(3, '0')}.${beat}` };
}

// subject "character:victoria_midnight" -> a track id + a display label. No source
// beyond the tracking file + the character block this page already carries.
const AR_SUBJECT_NAME = { victoria_midnight: DATA.character.alias || DATA.character.name, dcus: 'DCUS' };
function arSubjTrack(subject){ if (!subject) return null; return subject.includes(':') ? subject.split(':')[1] : subject; }
function arSubjLabel(subject){
  const id = arSubjTrack(subject); if (!id) return '—';
  return AR_SUBJECT_NAME[id] || id.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
}
function arIsPlace(subject){ return (subject || '').startsWith('place:'); }

// locked lanes — no gesture ever edits these (contract point 4, last bullet)
const AR_TROPE_PTS = TS.tropes.map(t => ({ ...t, tr: 'tropes', p: arPos(t.at) }));
const AR_WORLD = TS.world;
const AR_AUTOMATION = TS.automation.map(a => ({ ...a, points: (a.points || []).map(p => ({ ...p, p: arPos(p.at) })) }));
const AR_TEMPO_MEASURED = TS.tempo.measured.map(p => ({ ...p, p: arPos(p.at) }));
const AR_FREE_IN = TS.theme.in_world.map(p => ({ ...p, p: arPos(p.at) }));
const AR_FREE_AUD = TS.theme.audience.map(p => ({ ...p, p: arPos(p.at) }));

// editable lanes (BOLO 90 step 6, RULED 9/29 · the edit contract): story
// points, cables, planned tempo. Rebuilt by arBuildEditable() from the
// embedded base (TS, untouched) plus every pending edit replayed in seq
// order — never mutated in place. `let`, not `const`: every write recomputes.
let AR_PTS = [], AR_CABLES = [], AR_TEMPO_PLANNED = [];
let AR_SUBJECTS_WITH_POINTS = [];
let AR_TRACKS = [];
// per-lane heights (Chief 9/29: "each of the tools bigger … I want to be able to adjust them"):
// drag a lane header's bottom edge to resize, double-click it to reset; kept per viewer in browser storage
const AR_TRACK_H_KEY = 'ws.told.trackH.v1';
let AR_TRACK_H = {};
try { AR_TRACK_H = JSON.parse(localStorage.getItem(AR_TRACK_H_KEY) || '{}') || {}; } catch (e) { AR_TRACK_H = {}; }
function arSaveTrackH(){ try { localStorage.setItem(AR_TRACK_H_KEY, JSON.stringify(AR_TRACK_H)); } catch (e) {} }
// the told view's full height: ladder + bar ruler + every lane, so nothing is squeezed to fit a fixed box
function arToldNeedH(){ return AR_BAND_H * 2 + AR_RULE_H + AR_TRACKS.reduce((a, t) => a + t.h, 0) + 8; }
function arSizeLane(){
  const need = TS_STATE.view === 'told' ? arToldNeedH() : TS_STATE.view === 'stack' ? Math.max(560, arToldNeedH() * .6 + 300) : 560;
  const hpx = Math.max(420, Math.round(need)) + 'px';
  for (const id of ['arLane', 'arTracks']) { const el = document.getElementById(id); if (el && el.style.height !== hpx) el.style.height = hpx; }
}
let AR_PENDING_COUNT = 0;
let AR_FLAGGED_POINTS = [], AR_FLAGGED_CABLES = [], AR_FLAGGED_TEMPO = null;

// tracks: scenes + tempo always; one per automation lane; one state track per
// subject seen in story points; theme + tropes only if they carry data (ruling 3)
function arBuildTracks(){
  const tracks = [];
  tracks.push({ id: 'scenes', nm: 'Scenes', sub: 'clips · the told order', k: 'var(--accent)', h: 56 });
  tracks.push({
    id: 'tempo', nm: 'Tempo',
    sub: AR_TEMPO_MEASURED.length ? 'planned —  measured - -' : 'planned —  · measured: none until a draft exists',
    k: 'var(--accent)', h: 120, term: 'tempo',
  });
  for (const a of AR_AUTOMATION) {
    if (!a.points.length) continue;
    tracks.push({
      id: 'auto:' + a.id, nm: arSubjLabel(a.subject) + ' · ' + (a.field || '').split('.')[0].replace(/_/g, ' '),
      sub: ((a.field || '').split('.').slice(1).join('.') || 'value') + ' · automation',
      k: arIsPlace(a.subject) ? 'var(--c-place)' : 'var(--c-char)', h: 100, term: 'ramp', auto: a,
    });
  }
  for (const subj of AR_SUBJECTS_WITH_POINTS) {
    const src = (AR_PTS.find(p => p.tr === subj) || {}).subject || '';
    tracks.push({ id: subj, nm: arSubjLabel(src) + ' · state', sub: 'story points', k: arIsPlace(src) ? 'var(--c-place)' : 'var(--c-char)', h: 76 });
  }
  if (AR_FREE_IN.length || AR_FREE_AUD.length) {
    tracks.push({ id: 'theme', nm: 'Theme · ' + (TS.theme.rail || ''), sub: (TS.theme.scale || '') + ' · in-world / audience', k: 'var(--c-theme)', h: 100, term: 'freedom' });
  }
  if (AR_TROPE_PTS.length) {
    tracks.push({ id: 'tropes', nm: 'Tropes', sub: 'from the register', k: 'var(--c-trope)', h: 56 });
  }
  return tracks;
}

// ==================================================================
// ---- the edit layer: db hookup, replay, gestures (BOLO 90 step 6) ----
// ==================================================================
const AR_LEDGER = DATA.ar_ledger || { applied: [], undone: [], flagged: {} };
const AR_EDIT = { db: null, mode: false, cableTool: false, readOnly: true, edits: [] };
let AR_SELECTED_POINT = null, AR_SELECTED_CABLE = null;
let AR_CABLE_DRAG = null;   // { fromPt } while alt-dragging a cable
let AR_TEMPO_DRAFT = null;  // working copy of planned tempo points during a drag

// the playhead inspector's base records (BOLO 90 step 7): parsed at build time
// from canon (character-state-architecture protocol, base -> diffs -> derived
// -> flags); keyed by the same subject id the tracking file's story points use.
const AR_BASES = DATA.bases || {};
// "Who" the inspector is assembled for — clicking a state track header or one
// of its points in the Told view (ruling 6) changes this; default is Tori.
let AR_INSPECT_SUBJECT = 'character:victoria_midnight';
function arSubjectForTrack(trackId){ return (AR_PTS.find(p => p.tr === trackId) || {}).subject || null; }
function arSetInspectSubject(subject){
  if (!subject || subject === AR_INSPECT_SUBJECT) return;
  AR_INSPECT_SUBJECT = subject;
  if (typeof renderDetail === 'function') renderDetail();
}

function arKeyMatch(pt, key){ return !!(pt && key && pt.subject === key.subject && pt.field === key.field && pt.at === key.at); }
function arPKey(p){ return p.subject + '|' + p.field + '|' + p.at; }

function arValidateCode(text){
  const m = (text || '').match(/(M\d+)\s*·\s*(Q\d+)\s*·\s*(S\d+)\s*\|\s*(\d+)\.(\d+)(?:\.(\d+))?/);
  if (!m) return false;
  const sc = AR_SCENE_BY_KEY[m[1] + '|' + m[2] + '|' + m[3]];
  if (!sc) return false;
  const bar = +m[4], beat = +m[5];
  if (!(bar >= 1 && bar <= sc.bars)) return false;
  if (!(beat >= 1 && beat <= sc.num)) return false;
  if (m[6] != null && +m[6] < 1) return false;
  return true;
}
function arCodeForPos(p){
  if (!AR_SCENES.length) return null;
  const rounded = Math.max(0, Math.min(AR_TOTAL - 0.001, Math.round(p)));
  const c = arCodeAt(rounded);
  if (!c) return null;
  const code = c.text + '.1';
  return arValidateCode(code) ? code : null;
}

function arCategorizeEdits(){
  const appliedSet = new Set(AR_LEDGER.applied || []);
  const undoneSet = new Set(AR_LEDGER.undone || []);
  const flaggedMap = AR_LEDGER.flagged || {};
  const all = AR_EDIT.edits.slice().sort((a, b) => ((a.data||{}).seq || 0) - ((b.data||{}).seq || 0) || String(a.id).localeCompare(String(b.id)));
  const cancelled = new Set();
  for (const e of all) {
    const d = e.data || {};
    if (d.op === 'undo' && !appliedSet.has(e.id) && !undoneSet.has(e.id) && !flaggedMap[e.id]) cancelled.add((d.data || {}).ref || d.ref);  // the contract nests ref under data (fixed 9/29: undo never cancelled on the page)
  }
  const pending = [], flagged = [], history = [];
  for (const e of all) {
    const d = e.data || {};
    const reason = flaggedMap[e.id];
    let st;
    if (reason) st = 'flagged';
    else if (appliedSet.has(e.id)) st = 'applied';
    else if (undoneSet.has(e.id)) st = 'undone';
    else if (d.op !== 'undo' && cancelled.has(e.id)) st = 'undone-pending';
    else st = 'pending';
    history.push({ e, state: st, reason });
    if (reason) { flagged.push(e); continue; }
    if (st === 'applied' || st === 'undone' || st === 'undone-pending') continue;
    pending.push(e);
  }
  return { pending, flagged, history };
}

function arReplay(pendingList){
  const points = TS.points.map(p => ({ ...p }));
  const cables = TS.cables.map(c => ({ ...c, setup: { ...c.setup }, payoff: c.payoff ? { ...c.payoff } : null }));
  let tempoPlanned = TS.tempo.planned.map(p => ({ ...p }));
  const pendingPointKeys = new Map(), pendingCableIds = new Map();
  let tempoPendingId = null;
  for (const e of pendingList) {
    const d = e.data || {};
    if (d.op === 'point.move') {
      const idx = points.findIndex(p => arKeyMatch(p, d.key));
      if (idx === -1) continue;
      points[idx] = { ...points[idx], at: d.to };
      pendingPointKeys.set(arPKey(points[idx]), e.id);
    } else if (d.op === 'point.add') {
      const np = { subject: d.subject, field: d.field, value: d.value, at: d.at, origin_event: d.origin_event || null };
      points.push(np);
      pendingPointKeys.set(arPKey(np), e.id);
    } else if (d.op === 'point.remove') {
      const idx = points.findIndex(p => arKeyMatch(p, d.key));
      if (idx !== -1) points.splice(idx, 1);
    } else if (d.op === 'cable.add') {
      const nc = { id: d.id, setup: { ...d.setup }, payoff: d.payoff ? { ...d.payoff } : null, orphan: d.payoff ? 'provisional' : 'setup_no_payoff', why: d.why || '' };
      const already = cables.findIndex(c => c.id === nc.id);
      if (already !== -1) cables[already] = nc; else cables.push(nc);
      pendingCableIds.set(nc.id, e.id);
    } else if (d.op === 'cable.remove') {
      const idx = cables.findIndex(c => c.id === d.id);
      if (idx !== -1) cables.splice(idx, 1);
      pendingCableIds.delete(d.id);
    } else if (d.op === 'tempo.planned') {
      tempoPlanned = (d.points || []).map(p => ({ ...p }));
      tempoPendingId = e.id;
    }
  }
  return { points, cables, tempoPlanned, pendingPointKeys, pendingCableIds, tempoPendingId };
}

function arBuildEditable(){
  const { pending, flagged } = arCategorizeEdits();
  const r = arReplay(pending);
  AR_PTS = r.points.map(p => ({ ...p, tr: arSubjTrack(p.subject), p: arPos(p.at), _pendingEdit: r.pendingPointKeys.get(arPKey(p)) || null }));
  AR_CABLES = r.cables.map(c => ({
    ...c,
    fromTrack: arSubjTrack(c.setup.track), toTrack: c.payoff ? arSubjTrack(c.payoff.track) : null,
    a: arPos(c.setup.at), b: c.payoff ? arPos(c.payoff.at) : null,
    _pendingEdit: r.pendingCableIds.get(c.id) || null,
  }));
  const tempoBase = AR_TEMPO_DRAFT || r.tempoPlanned;
  AR_TEMPO_PLANNED = tempoBase.map(p => ({ ...p, p: arPos(p.at), _pendingEdit: AR_TEMPO_DRAFT ? 'draft' : r.tempoPendingId }));
  AR_SUBJECTS_WITH_POINTS = Array.from(new Set(AR_PTS.map(p => p.tr).filter(Boolean)));
  AR_TRACKS = arBuildTracks();
  for (const t of AR_TRACKS) { t.h0 = t.h; if (AR_TRACK_H[t.id]) t.h = AR_TRACK_H[t.id]; }

  AR_FLAGGED_POINTS = []; AR_FLAGGED_CABLES = []; AR_FLAGGED_TEMPO = null;
  for (const e of flagged) {
    const d = e.data || {}; const reason = (AR_LEDGER.flagged || {})[e.id] || 'flagged';
    if (d.op === 'point.move' && d.key) {
      AR_FLAGGED_POINTS.push({ subject: d.key.subject, field: d.key.field, at: d.to, tr: arSubjTrack(d.key.subject), p: arPos(d.to), editId: e.id, reason });
    } else if (d.op === 'point.add') {
      AR_FLAGGED_POINTS.push({ subject: d.subject, field: d.field, at: d.at, tr: arSubjTrack(d.subject), p: arPos(d.at), editId: e.id, reason });
    } else if (d.op === 'cable.add' && d.setup) {
      AR_FLAGGED_CABLES.push({ id: d.id, fromTrack: arSubjTrack(d.setup.track), toTrack: d.payoff ? arSubjTrack(d.payoff.track) : null, a: arPos(d.setup.at), b: d.payoff ? arPos(d.payoff.at) : null, editId: e.id, reason });
    } else if (d.op === 'tempo.planned') {
      AR_FLAGGED_TEMPO = { editId: e.id, reason };
    }
  }
  AR_PENDING_COUNT = pending.length;
}
arBuildEditable(); // baseline: no edits yet, identical to the old read-only render

function arEditLabel(e){
  const d = e.data || {};
  if (d.op === 'point.move') return `${arSubjLabel(d.key && d.key.subject)} · ${d.key && d.key.field} → ${d.to}`;
  if (d.op === 'point.add') return `${arSubjLabel(d.subject)} · ${d.field} = ${d.value}`;
  if (d.op === 'point.remove') return `${arSubjLabel(d.key && d.key.subject)} · ${d.key && d.key.field} (removed)`;
  if (d.op === 'cable.add') return `cable ${d.id} — ${d.why || ''}`;
  if (d.op === 'cable.remove') return `cable ${d.id} (removed)`;
  if (d.op === 'tempo.planned') return `tempo curve · ${(d.points||[]).length} pts`;
  if (d.op === 'undo') return `undo → ${(d.data || {}).ref || d.ref}`;
  return d.op || 'edit';
}

function arSetMsg(text){
  const el = document.getElementById('toldMsg'); if (!el) return;
  el.hidden = !text; el.textContent = text || '';
  if (text) setTimeout(() => { if (el.textContent === text) { el.hidden = true; el.textContent = ''; } }, 5000);
}
function arSetReadOnly(flag, msg){
  AR_EDIT.readOnly = flag;
  if (flag) AR_EDIT.mode = false;
  if (msg) arSetMsg(msg);
  renderEditToolbar();
}

async function arWriteEdit(op, data){
  if (!AR_EDIT.db || AR_EDIT.readOnly) return false;
  const id = 'e' + Date.now() + '-' + Math.random().toString(36).slice(2, 6);
  const body = { story: 'oxo', seq: Date.now(), op, data };
  AR_EDIT.edits.push({ id, data: body }); // optimistic — a matching id from the next snapshot replaces it wholesale
  arBuildEditable(); toldRender(); renderEditToolbar();
  try {
    await AR_EDIT.db.collection('edits').doc(id).set(body);
    logEvent('told', `edit written · ${op} · ${arEditLabel({ data: body })}`);
    return true;
  } catch (err) {
    AR_EDIT.edits = AR_EDIT.edits.filter(e => e.id !== id);
    const code = err && err.code;
    if (code === 'invalid_argument') arSetReadOnly(true, 'edit rejected — switched to read-only for this visit');
    else if (code === 'quota_exceeded') arSetMsg('storage quota reached — edit not saved');
    else arSetMsg('edit did not save');
    arBuildEditable(); toldRender(); renderEditToolbar();
    return false;
  }
}

function arNewestUndoableId(){
  const { pending } = arCategorizeEdits();
  // skip edits an undo already cancels, including undos written this visit that the snapshot hasn't echoed yet
  // (bug 9/29: three quick Ctrl+Z wrote three undos against the same edit)
  const undoneRefs = new Set(pending.filter(e => (e.data || {}).op === 'undo').map(e => (e.data.data || {}).ref));
  (AR_EDIT.localUndone || []).forEach(r => undoneRefs.add(r));
  const real = pending.filter(e => (e.data || {}).op !== 'undo' && !undoneRefs.has(e.id));
  return real.length ? real[real.length - 1].id : null;
}
function arUndoLast(){
  if (!AR_EDIT.mode || AR_EDIT.readOnly) return;
  const id = arNewestUndoableId();
  if (!id) { arSetMsg('nothing pending to undo'); return; }
  (AR_EDIT.localUndone = AR_EDIT.localUndone || []).push(id);
  arWriteEdit('undo', { ref: id });
}

function cloneEditDoc(d){
  try { return { id: d.id, data: JSON.parse(JSON.stringify(d.data ? d.data() : d)) }; }
  catch (err) { return { id: d.id, data: {} }; }
}

async function arInitDb(){
  let db = null;
  try { if (window.claude && window.claude.use) db = await window.claude.use('db'); }
  catch (err) { db = null; }
  AR_EDIT.db = db || null;
  if (!db) { arSetReadOnly(true); return; }
  AR_EDIT.readOnly = false; AR_EDIT.mode = true; // edit mode on by default once db is up
  try {
    db.collection('edits').onSnapshot(
      snap => {
        const docs = [];
        if (snap && typeof snap.forEach === 'function') snap.forEach(d => docs.push(cloneEditDoc(d)));
        else if (snap && Array.isArray(snap.docs)) snap.docs.forEach(d => docs.push(cloneEditDoc(d)));
        AR_EDIT.edits = docs;
        arBuildEditable(); toldRender(); renderEditToolbar();
      },
      err => { arSetMsg('edit sync lost'); }
    );
  } catch (err) { arSetReadOnly(true); }
  renderEditToolbar();
}
arInitDb(); // never blocks first paint — the view already rendered read-only above

function renderEditToolbar(){
  const seg = document.getElementById('toldEditSeg');
  const pendBtn = document.getElementById('toldPendingBtn');
  const ro = document.getElementById('toldReadonly');
  if (!seg || !pendBtn || !ro) return;
  const dbUp = !!AR_EDIT.db;
  seg.hidden = !dbUp;
  ro.hidden = !AR_EDIT.readOnly;
  if (dbUp) {
    seg.querySelector('[data-e="edit"]').setAttribute('aria-pressed', String(AR_EDIT.mode));
    seg.querySelector('[data-e="cable"]').setAttribute('aria-pressed', String(AR_EDIT.cableTool));
    seg.querySelectorAll('button').forEach(b => { b.disabled = AR_EDIT.readOnly; });
  }
  pendBtn.hidden = AR_PENDING_COUNT === 0;
  pendBtn.textContent = `${AR_PENDING_COUNT} edit${AR_PENDING_COUNT === 1 ? '' : 's'} pending pull`;
}
document.getElementById('toldEditSeg').addEventListener('click', e => {
  const b = e.target.closest('button'); if (!b) return;
  if (b.dataset.e === 'edit') { AR_EDIT.mode = !AR_EDIT.mode; if (!AR_EDIT.mode) { AR_EDIT.cableTool = false; AR_SELECTED_POINT = null; AR_SELECTED_CABLE = null; } renderEditToolbar(); toldRender(); }
  else if (b.dataset.e === 'cable') { AR_EDIT.cableTool = !AR_EDIT.cableTool; renderEditToolbar(); }
  else if (b.dataset.e === 'undo') { arUndoLast(); }
});
document.getElementById('toldPendingBtn').addEventListener('click', arToggleHistory);

function arToggleHistory(){
  const el = document.getElementById('toldHistory');
  if (!el.hidden) { el.hidden = true; return; }
  const { history } = arCategorizeEdits();
  const rows = history.slice().reverse().map(h => `
    <div class="hrow">
      <div><span class="hop">${esc((h.e.data||{}).op||'?')}</span> <span class="htarget">${esc(arEditLabel(h.e))}</span></div>
      <span class="hstate ${h.state}">${esc(h.state)}</span>
      ${h.reason ? `<div class="hreason">${esc(h.reason)}</div>` : ''}
    </div>`).join('') || '<p class="empty-detail">No edits yet.</p>';
  el.innerHTML = `<button class="hclose" id="toldHistoryClose">&times;</button><h4>Edit history</h4>${rows}`;
  const btn = document.getElementById('toldPendingBtn');
  const r = btn.getBoundingClientRect();
  el.style.left = Math.max(12, r.left) + 'px'; el.style.top = (r.bottom + 6) + 'px';
  el.hidden = false;
  document.getElementById('toldHistoryClose').addEventListener('click', () => { el.hidden = true; });
}

const TS_STATE = { view: 'told', ppb: 0, off: 0, ph: AR_SCENES.length ? AR_SCENES[0].start : 0, wph: 0 };
const AR_ZOOMS = [['Story', 1.6], ['Movement', 2.6], ['Sequence', 4], ['Scene', 9], ['Bar', 26], ['Beat', 70], ['Tick', 190]];

function arLaneEl(){ return document.getElementById('arLane'); }
function arSvgEl(){ return document.getElementById('arSvg'); }
function arW(){ const l = arLaneEl(); return l ? l.clientWidth : 0; }
function arH(){ const l = arLaneEl(); return l ? l.clientHeight : 0; }
function arX(p){ return (p - TS_STATE.off) * TS_STATE.ppb; }
function arEl(tag, attrs, parent, text){
  const e = document.createElementNS(AR_NS, tag);
  for (const k in attrs) e.setAttribute(k, attrs[k]);
  if (text != null) e.textContent = text;
  (parent || arSvgEl()).appendChild(e);
  return e;
}
function arStopName(){ let n = AR_ZOOMS[0][0]; for (const [nm, v] of AR_ZOOMS) if (TS_STATE.ppb >= v * .8) n = nm; return n; }
function arFit(){ const w = arW(); if (w <= 0) return; TS_STATE.ppb = Math.max(1, (w - 24) / AR_TOTAL); TS_STATE.off = -8 / TS_STATE.ppb; }
function arClampOff(){ if (!TS_STATE.ppb) return; const w = arW() / TS_STATE.ppb; TS_STATE.off = Math.max(-w * .3, Math.min(AR_TOTAL - w * .7, TS_STATE.off)); }
function arSetZoom(ppb, anchorX){
  if (!TS_STATE.ppb) arFit();
  const ax = anchorX == null ? arW() / 2 : anchorX;
  const p = TS_STATE.off + ax / TS_STATE.ppb;
  TS_STATE.ppb = Math.max(0.6, Math.min(400, ppb));
  TS_STATE.off = p - ax / TS_STATE.ppb; arClampOff(); toldRender();
}

function arHeaders(rows){
  const box = document.getElementById('arTracks'); if (!box) return;
  box.innerHTML = '';
  for (const r of rows) {
    const d = document.createElement('div');
    d.className = 'ar-th' + (r.ruler ? ' ruler' : '');
    d.style.top = r.y + 'px'; d.style.height = r.h + 'px';
    d.style.setProperty('--k', r.k || 'var(--line-2)');
    d.innerHTML = `<span class="nm">${r.term ? `<span class="t" data-tt="gloss" data-id="${r.term}">${esc(r.nm)}</span>` : esc(r.nm)}</span><span class="sub">${esc(r.sub || '')}</span>`;
    // clicking a character/place state track's header selects that subject for
    // the playhead inspector (ruling 6) — works in any ruler view, edit mode or not
    if (!r.ruler && r.id && AR_SUBJECTS_WITH_POINTS.includes(r.id)) {
      const subject = arSubjectForTrack(r.id);
      if (subject) {
        d.classList.add('ar-th-pick');
        if (subject === AR_INSPECT_SUBJECT) d.classList.add('ar-th-sel');
        d.addEventListener('click', () => arSetInspectSubject(subject));
      }
    }
    if (!r.ruler && r.id && TS_STATE.view === 'told') {
      const hd = document.createElement('div');
      hd.className = 'ar-resize'; hd.title = 'Drag to resize this lane · double-click to reset';
      hd.addEventListener('pointerdown', ev => arStartResize(ev, r.id));
      hd.addEventListener('dblclick', ev => { ev.stopPropagation(); const t = AR_TRACKS.find(x => x.id === r.id); if (!t) return; delete AR_TRACK_H[r.id]; t.h = t.h0; arSaveTrackH(); toldRender(); });
      d.appendChild(hd);
    }
    box.appendChild(d);
  }
}

function arStartResize(ev, id){
  const t = AR_TRACKS.find(x => x.id === id); if (!t) return;
  ev.preventDefault(); ev.stopPropagation();
  const y0 = ev.clientY, h0 = t.h, el = ev.currentTarget;
  try { el.setPointerCapture(ev.pointerId); } catch (e) {}
  let raf = 0;
  const move = e => { t.h = Math.max(28, Math.min(480, Math.round(h0 + e.clientY - y0))); if (!raf) raf = requestAnimationFrame(() => { raf = 0; toldRender(); }); };
  const up = () => { el.removeEventListener('pointermove', move); el.removeEventListener('pointerup', up); el.removeEventListener('pointercancel', up); AR_TRACK_H[id] = t.h; arSaveTrackH(); toldRender(); };
  el.addEventListener('pointermove', move); el.addEventListener('pointerup', up); el.addEventListener('pointercancel', up);
}

function arDrawTold(y0, h, compact){
  const w = arW();
  const rows = [];
  arEl('rect', { x: 0, y: y0, width: w, height: AR_BAND_H * 2, class: 'ar-band' });
  for (const mv of AR_MOVS) {
    const sc = AR_SCENES.filter(s => s.mv === mv.id); if (!sc.length) continue;
    const a = arX(sc[0].start), b = arX(sc[sc.length - 1].start + sc[sc.length - 1].len);
    arEl('line', { x1: a, x2: a, y1: y0, y2: y0 + AR_BAND_H * 2, class: 'ar-grid-bar' });
    arEl('text', { x: Math.max(a, 0) + 6, y: y0 + 15, class: 'ar-band-lbl' }, null, `${mv.id} · ${mv.lbl}`);
    const seq = AR_SEQS.find(q => q.id.indexOf(mv.id) === 0);
    if (seq) arEl('text', { x: Math.max(a, 0) + 6, y: y0 + AR_BAND_H + 15 }, null, `${seq.id} · ${seq.lbl}`);
  }
  const ry = y0 + AR_BAND_H * 2;
  arEl('rect', { x: 0, y: ry, width: w, height: AR_RULE_H, fill: 'var(--panel)' });
  arEl('rect', { x: 0, y: y0, width: w, height: AR_BAND_H * 2 + AR_RULE_H, fill: 'transparent', 'data-ruler': '1', style: 'cursor:col-resize' });
  rows.push({ nm: 'Ladder', sub: 'movement · sequence', y: y0, h: AR_BAND_H * 2, ruler: 1, term: 'toldzoom' });
  rows.push({ nm: 'Bars', sub: 'bar ruler · meter', y: ry, h: AR_RULE_H, ruler: 1, term: 'bar' });
  const gy0 = ry + AR_RULE_H, gy1 = y0 + h;
  for (const sc of AR_SCENES) {
    const sx = arX(sc.start);
    if (sx > w + 40 || arX(sc.start + sc.len) < -40) continue;
    arEl('text', { x: sx + 4, y: ry + 12, class: 'ar-sig' }, null, `${sc.num}/${sc.den}`);
    const barPx = sc.num * TS_STATE.ppb, every = barPx > 34 ? 1 : barPx > 16 ? 2 : barPx > 7 ? 4 : 99;
    for (let b = 0; b < sc.bars; b++) {
      const bx = arX(sc.start + b * sc.num);
      if (bx < -2 || bx > w + 2) continue;
      arEl('line', { x1: bx, x2: bx, y1: b === 0 ? y0 : ry + 16, y2: gy1, class: b === 0 ? 'ar-grid-bar' : 'ar-grid-beat', opacity: b === 0 ? 1 : (every < 99 ? .9 : .35) });
      if (every < 99 && b % every === 0) arEl('text', { x: bx + 3, y: ry + 26 }, null, String(b + 1));
      if (TS_STATE.ppb > 18) for (let bt = 1; bt < sc.num; bt++) {
        const tx = arX(sc.start + b * sc.num + bt);
        arEl('line', { x1: tx, x2: tx, y1: ry + 22, y2: gy1, class: 'ar-grid-beat', opacity: .35 });
      }
    }
  }
  let y = gy0;
  const tracks = compact ? AR_TRACKS.filter(t => t.id === 'scenes' || AR_SUBJECTS_WITH_POINTS.includes(t.id)) : AR_TRACKS;
  for (const t of tracks) {
    const th = compact ? 30 : t.h;
    rows.push({ ...t, y, h: th });
    arEl('line', { x1: 0, x2: w, y1: y + th, y2: y + th, class: 'ar-rowline' });
    const mid = y + th / 2;
    if (t.id === 'scenes') {
      for (const sc of AR_SCENES) {
        const a = arX(sc.start) + 1, b = arX(sc.start + sc.len) - 1;
        if (b < 0 || a > w) continue;
        arEl('rect', { x: a, y: y + 4, width: Math.max(2, b - a), height: th - 8, fill: 'var(--accent-soft)', stroke: 'var(--accent)', class: 'ar-clip' });
        if (b - a > 60) arEl('text', { x: Math.max(a, 0) + 6, y: y + th / 2 + 4, class: 'ar-clip-lbl' }, null, (b - a > 170 ? `${sc.s} · ${sc.label}` : sc.s));
      }
    } else if (t.id === 'tempo') {
      arTempoTrack(y, th);
    } else if (t.id.indexOf('auto:') === 0) {
      arAutomationTrack(t.auto, y, th);
    } else if (t.id === 'theme') {
      arCurve(AR_FREE_IN, AR_FREE_AUD, y, th, -3, 1, 'var(--c-theme)', true);
    } else {
      arPoints(t, mid);
    }
    t._y = y; t._h = th;
    y += th;
  }
  arCables(tracks);
  return rows;
}

function arStepPath(arr, y, h, lo, hi, rampAll){
  const Y = v => y + h - 6 - (v - lo) / (hi - lo) * (h - 12);
  let d = `M ${arX(arr[0].p)} ${Y(arr[0].v)}`;
  for (let i = 1; i < arr.length; i++) {
    const ramp = rampAll || arr[i].ramp;
    d += ramp ? ` L ${arX(arr[i].p)} ${Y(arr[i].v)}` : ` L ${arX(arr[i].p)} ${Y(arr[i - 1].v)} L ${arX(arr[i].p)} ${Y(arr[i].v)}`;
  }
  return { d, Y };
}
function arAutomationTrack(a, y, h){
  if (!a.points.length) return; // no data — draw nothing (ruling 3)
  const lo = a.range[0], hi = a.range[1];
  const { d, Y } = arStepPath(a.points, y, h, lo, hi);
  arEl('path', { d: d + ` L ${arX(a.points[a.points.length - 1].p)} ${y + h - 6} L ${arX(a.points[0].p)} ${y + h - 6} Z`, fill: 'var(--c-char)', class: 'ar-auto-fill' });
  arEl('path', { d, fill: 'none', stroke: 'var(--c-char)', 'stroke-width': 2 });
  for (const pt of a.points) arEl('circle', { cx: arX(pt.p), cy: Y(pt.v), r: 3.5, fill: 'var(--c-char)', class: 'ar-pt' });
}
function arTempoTrack(y, h){
  const vals = AR_TEMPO_PLANNED.concat(AR_TEMPO_MEASURED).map(p => p.bpm);
  const lo = vals.length ? Math.min(...vals) - 10 : 60, hi = vals.length ? Math.max(...vals) + 10 : 180;
  TS_STATE._tempoBox = { y, h, lo, hi }; // cached for the click/drag hit-test — planned tempo is the one editable curve here
  if (!AR_TEMPO_PLANNED.length) { arEl('text', { x: 6, y: y + 12 }, null, AR_EDIT.mode ? 'no tempo data — click to add the first point' : 'no tempo data'); return; }
  const planned = AR_TEMPO_PLANNED.map(p => ({ p: p.p, v: p.bpm, ramp: p.ramp }));
  const pa = arStepPath(planned, y, h, lo, hi);
  if (AR_TEMPO_MEASURED.length) {
    const measured = AR_TEMPO_MEASURED.map(p => ({ p: p.p, v: p.bpm, ramp: p.ramp }));
    const pb = arStepPath(measured, y, h, lo, hi);
    const back = [...measured].reverse();
    let g = pa.d; for (const b of back) g += ` L ${arX(b.p)} ${pb.Y(b.v)}`;
    arEl('path', { d: g + ' Z', class: 'ar-gap' });
    arEl('path', { d: pb.d, fill: 'none', stroke: 'var(--accent)', 'stroke-width': 1.6, 'stroke-dasharray': '5 4', opacity: .85 });
    arEl('text', { x: 6, y: y + 12 }, null, 'bpm · planned —  measured - -');
  } else {
    arEl('text', { x: 6, y: y + 12 }, null, 'bpm · planned —  · measured: none until a draft exists');
  }
  arEl('path', { d: pa.d, fill: 'none', stroke: (AR_TEMPO_PLANNED[0] || {})._pendingEdit ? 'var(--accent-ink)' : 'var(--accent)', 'stroke-width': 2, 'stroke-dasharray': (AR_TEMPO_PLANNED[0] || {})._pendingEdit ? '5 4' : 'none' });
  for (const pt of AR_TEMPO_PLANNED) {
    const cx = arX(pt.p), cy = pa.Y(pt.v);
    if (cx < -20 || cx > arW() + 20) continue;
    arEl('circle', { cx, cy, r: 4.5, fill: 'var(--accent)', class: 'ar-pt', 'data-tempoat': pt.at });
  }
  if (AR_FLAGGED_TEMPO) {
    const g = arEl('g', {});
    arEl('text', { x: arW() - 10, y: y + 12, 'text-anchor': 'end', fill: 'var(--bad)', class: 'ar-sig' }, g, '⚑ flagged curve');
    arEl('title', {}, g, `flagged · ${AR_FLAGGED_TEMPO.reason}`);
  }
}
function arCurve(A, B, y, h, lo, hi, col, step){
  if (!A.length && !B.length) return; // no data — draw nothing (ruling 3)
  if (A.length) {
    const pa = arStepPath(A, y, h, lo, hi, !step);
    arEl('path', { d: pa.d, fill: 'none', stroke: col, 'stroke-width': 2 });
    if (B.length) {
      const pb = arStepPath(B, y, h, lo, hi, !step);
      const back = [...B].reverse();
      let g = pa.d; for (const b of back) g += ` L ${arX(b.p)} ${pb.Y(b.v)}`;
      arEl('path', { d: g + ' Z', class: 'ar-gap' });
      arEl('path', { d: pb.d, fill: 'none', stroke: col, 'stroke-width': 1.6, 'stroke-dasharray': '5 4', opacity: .85 });
    }
  } else if (B.length) {
    const pb = arStepPath(B, y, h, lo, hi, !step);
    arEl('path', { d: pb.d, fill: 'none', stroke: col, 'stroke-width': 1.6, 'stroke-dasharray': '5 4', opacity: .85 });
  }
  arEl('text', { x: 6, y: y + 12 }, null, step ? (B.length ? 'in-world —  audience - -' : 'in-world —  · audience: none on record') : '');
}
function arPoints(t, mid){
  const isTropes = t.id === 'tropes';
  const mine = isTropes ? AR_TROPE_PTS : AR_PTS.filter(p => p.tr === t.id);
  const w = arW();
  if (mine.length && TS_STATE.ppb < 6) {
    for (const sc of AR_SCENES) {
      const n = mine.filter(p => p.p >= sc.start && p.p < sc.start + sc.len).length;
      if (!n) continue;
      const cx = arX(sc.start + sc.len / 2);
      arEl('rect', { x: cx - 11, y: mid - 9, width: 22, height: 18, rx: 9, class: 'ar-badge' });
      arEl('text', { x: cx, y: mid + 4, 'text-anchor': 'middle', class: 'ar-badge-t' }, null, String(n));
    }
  } else {
    for (const p of mine) {
      const x = arX(p.p);
      if (x < -20 || x > w + 20) continue;
      const g = arEl('g', {});
      const isSel = !isTropes && AR_SELECTED_POINT && arPKey(AR_SELECTED_POINT) === arPKey(p);
      if (isTropes) arEl('rect', { x: x - 5, y: mid - 5, width: 10, height: 10, fill: t.k, class: 'ar-pt', transform: `rotate(45 ${x} ${mid})` }, g);
      else {
        arEl('circle', { cx: x, cy: mid, r: 5.5, fill: t.k, class: 'ar-pt' + (isSel ? ' selected' : ''), 'data-ptkey': arPKey(p), 'data-track': t.id }, g);
        if (p._pendingEdit) arEl('circle', { cx: x, cy: mid, r: 8.5, class: 'ar-pt-pending-ring' }, g);
      }
      const lbl = isTropes ? p.name : (p.field + (TS_STATE.ppb > 26 ? ' · ' + p.value : ''));
      const show = TS_STATE.ppb > 120 ? lbl : TS_STATE.ppb > 26 ? (isTropes ? p.name : String(p.value)) : '';
      if (show) arEl('text', { x: x + 9, y: mid + 3.5 }, g, show.length > 34 ? show.slice(0, 33) + '…' : show);
    }
  }
  // flagged points on this track are drawn even at low zoom, in red, never hidden
  if (!isTropes) {
    for (const fp of AR_FLAGGED_POINTS.filter(f => f.tr === t.id)) {
      const x = arX(fp.p); if (x < -20 || x > w + 20) continue;
      const g = arEl('g', {});
      arEl('circle', { cx: x, cy: mid, r: 6, class: 'ar-flag-pt', 'data-flag': fp.editId }, g);
      arEl('title', {}, g, `flagged · ${fp.reason}`);
    }
  }
}
function arCables(tracks){
  const ty = id => { const t = tracks.find(t => t.id === id); return t ? t._y + t._h / 2 : null; };
  const w = arW();
  for (const c of AR_CABLES) {
    const y1 = ty(c.fromTrack); if (y1 == null) continue;
    const x1 = arX(c.a);
    const col = c.orphan === 'setup_no_payoff' || c.orphan === 'payoff_no_setup' ? 'var(--bad)' : 'var(--accent)';
    const extra = (c._pendingEdit ? ' pending' : '') + (AR_SELECTED_CABLE && AR_SELECTED_CABLE.id === c.id ? ' selected' : '');
    if (c.b == null) {
      const x2 = x1 + Math.max(40, 18 * Math.sqrt(TS_STATE.ppb));
      arEl('path', { d: `M ${x1} ${y1} C ${x1 + 20} ${y1 + 26}, ${x2 - 10} ${y1 + 30}, ${x2} ${y1 + 22}`, class: 'ar-cable' + extra, stroke: col, 'data-cab': c.id });
      arEl('circle', { cx: x2, cy: y1 + 22, r: 4, class: 'ar-orphan' });
      continue;
    }
    const y2 = ty(c.toTrack); if (y2 == null) continue;
    const x2 = arX(c.b), sag = Math.min(90, Math.abs(x2 - x1) * .18 + 24);
    arEl('path', { d: `M ${x1} ${y1} C ${x1 + (x2 - x1) * .3} ${Math.max(y1, y2) + sag}, ${x1 + (x2 - x1) * .7} ${Math.max(y1, y2) + sag}, ${x2} ${y2}`, class: 'ar-cable' + (c.orphan === 'provisional' ? ' provisional' : '') + extra, stroke: col, 'data-cab': c.id, opacity: .9 });
  }
  // flagged cables — drawn even though never replayed into state, red, never hidden
  for (const fc of AR_FLAGGED_CABLES) {
    const y1 = ty(fc.fromTrack); if (y1 == null) continue;
    const x1 = arX(fc.a);
    const g = arEl('g', {});
    if (fc.b == null) {
      const x2 = x1 + Math.max(40, 18 * Math.sqrt(TS_STATE.ppb));
      arEl('path', { d: `M ${x1} ${y1} C ${x1 + 20} ${y1 + 26}, ${x2 - 10} ${y1 + 30}, ${x2} ${y1 + 22}`, class: 'ar-flag-cable', 'data-flag': fc.editId }, g);
    } else {
      const y2 = ty(fc.toTrack); if (y2 == null) continue;
      const x2 = arX(fc.b), sag = Math.min(90, Math.abs(x2 - x1) * .18 + 24);
      arEl('path', { d: `M ${x1} ${y1} C ${x1 + (x2 - x1) * .3} ${Math.max(y1, y2) + sag}, ${x1 + (x2 - x1) * .7} ${Math.max(y1, y2) + sag}, ${x2} ${y2}`, class: 'ar-flag-cable', 'data-flag': fc.editId }, g);
    }
    arEl('title', {}, g, `flagged · ${fc.reason}`);
  }
  // the cable draw gesture's live ghost line, alt-drag or the Cable tool
  if (AR_CABLE_DRAG && AR_CABLE_DRAG.curX != null) {
    const y1 = ty(AR_CABLE_DRAG.fromPt.tr); const x1 = arX(AR_CABLE_DRAG.fromPt.p);
    if (y1 != null) arEl('line', { x1, y1, x2: AR_CABLE_DRAG.curX, y2: AR_CABLE_DRAG.curY, stroke: 'var(--accent-ink)', 'stroke-width': 2, 'stroke-dasharray': '4 3' });
  }
}

function arDrawWorld(y0, h){
  const w = arW(), n = AR_WORLD.length, rows = [];
  if (!n) { rows.push({ nm: 'World clock', sub: 'no world events on record', y: y0, h, ruler: 1, term: 'world' }); return { rows, evY: y0, cx: () => 0 }; }
  const colW = (w - 24) / n;
  const cx = i => 12 + colW * (i + .5);
  arEl('rect', { x: 0, y: y0, width: w, height: AR_BAND_H * 2, class: 'ar-band' });
  let last = null;
  AR_WORLD.forEach((e, i) => {
    if (e.m !== last) {
      arEl('line', { x1: 12 + colW * i, x2: 12 + colW * i, y1: y0, y2: y0 + h, class: 'ar-grid-bar' });
      arEl('text', { x: 12 + colW * i + 6, y: y0 + 15, class: 'ar-band-lbl' }, null, e.m === 'backstory' ? 'Backstory' : e.m);
      last = e.m;
    }
  });
  arEl('rect', { x: 0, y: y0, width: w, height: AR_BAND_H * 2, fill: 'transparent', 'data-wruler': '1', style: 'cursor:col-resize' });
  rows.push({ nm: 'World clock', sub: 'fabula order · no bars', y: y0, h: AR_BAND_H * 2, ruler: 1, term: 'world' });
  const ey = y0 + AR_BAND_H * 2, eh = 64;
  rows.push({ nm: 'Events', sub: 'the fabula', y: ey, h: eh, k: 'var(--ink-3)' });
  AR_WORLD.forEach((e, i) => {
    const bw = Math.min(colW - 10, 150), x = cx(i) - bw / 2;
    arEl('rect', { x, y: ey + 8, width: bw, height: eh - 16, fill: 'var(--panel-2)', stroke: 'var(--line-2)', class: 'ar-world-ev' });
    arEl('text', { x: x + 6, y: ey + 26, class: 'ar-clip-lbl' }, null, e.label.length * 6.2 > bw - 10 ? e.label.slice(0, Math.max(6, Math.floor((bw - 10) / 6.2))) + '…' : e.label);
    arEl('text', { x: x + 6, y: ey + 42 }, null, e.m);
  });
  arEl('line', { x1: 0, x2: w, y1: ey + eh, y2: ey + eh, class: 'ar-rowline' });
  const ny = ey + eh, nh = 44;
  const cps = AR_WORLD.map((e, i) => ({ e, i })).filter(o => o.e.dcus_name);
  if (cps.length) {
    rows.push({ nm: 'DCUS · name', sub: 'checkpoints · header', y: ny, h: nh, k: 'var(--c-place)', term: 'checkpoint' });
    cps.forEach((o, k) => {
      const a = cx(o.i), b = k < cps.length - 1 ? cx(cps[k + 1].i) : w - 4;
      arEl('rect', { x: a, y: ny + 8, width: b - a - 3, height: nh - 16, fill: 'var(--c-place-soft)', stroke: 'var(--c-place)', class: 'ar-clip' });
      arEl('text', { x: a + 6, y: ny + nh / 2 + 4, class: 'ar-clip-lbl' }, null, o.e.dcus_name);
    });
    arEl('line', { x1: 0, x2: w, y1: ny + nh, y2: ny + nh, class: 'ar-rowline' });
  }
  TS_STATE._wcx = cx; TS_STATE._colW = colW;
  return { rows, evY: ey + 8, cx };
}

function toldRender(){
  if (!TS_STATE.ppb) arFit();
  const svg = arSvgEl(); if (!svg) return;
  svg.innerHTML = '';
  if (!TS_STATE.ppb) return; // lane not visible/sized yet — retried on next resize/switch
  arSizeLane();
  const w = arW(), h = arH();
  let rows = [];
  if (TS_STATE.view === 'told') rows = arDrawTold(0, h, false);
  else if (TS_STATE.view === 'world') rows = arDrawWorld(0, h).rows;
  else {
    const topH = Math.floor(h * .5);
    rows = arDrawTold(0, topH, true);
    const wr = arDrawWorld(topH + 18, h - topH - 18);
    rows = rows.concat(wr.rows);
    let lastWorldIdx = -1;
    for (const sc of AR_SCENES) {
      const i = AR_WORLD.findIndex(e => e.id === sc.event);
      if (i < 0) continue;
      const x1 = arX(sc.start + sc.len / 2), x2 = wr.cx(i);
      const back = lastWorldIdx >= 0 && i < lastWorldIdx;
      arEl('path', { d: `M ${x1} ${topH - 30} C ${x1} ${topH + 20}, ${x2} ${topH - 10}, ${x2} ${wr.evY}`, class: 'ar-link' + (back ? ' back' : '') });
      if (back) arEl('text', { x: (x1 + x2) / 2 - 40, y: topH + 12, class: 'ar-sig' }, null, 'flashback ← runs backward');
      lastWorldIdx = i;
    }
  }
  if (TS_STATE.view !== 'world') {
    const px = arX(TS_STATE.ph);
    if (px >= 0 && px <= w) {
      arEl('line', { x1: px, x2: px, y1: 0, y2: TS_STATE.view === 'stack' ? Math.floor(h * .5) : h, class: 'ar-playhead' });
      arEl('path', { d: `M ${px - 6} 0 L ${px + 6} 0 L ${px} 8 Z`, class: 'ar-ph-cap' });
    }
  } else if (TS_STATE._colW) {
    const px = 12 + TS_STATE._colW * TS_STATE.wph;
    arEl('line', { x1: px, x2: px, y1: 0, y2: h, class: 'ar-playhead' });
    arEl('path', { d: `M ${px - 6} 0 L ${px + 6} 0 L ${px} 8 Z`, class: 'ar-ph-cap' });
  }
  arHeaders(rows);
  const stop = arStopName();
  $$('#toldZoomSeg button').forEach(b => { b.setAttribute('aria-pressed', String(b.dataset.z === stop)); b.disabled = TS_STATE.view === 'world'; });
  $$('#toldRulerSeg button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.v === TS_STATE.view)));
  const tcOut = document.getElementById('toldTcOut');
  if (tcOut) {
    if (TS_STATE.view === 'world') {
      const i = Math.max(0, Math.min(AR_WORLD.length - 1, Math.floor(TS_STATE.wph)));
      tcOut.textContent = AR_WORLD.length ? AR_WORLD[i].m : '—';
    } else {
      const c = arCodeAt(TS_STATE.ph); tcOut.textContent = c ? c.text : '—';
    }
  }
  if (state.lens === 'told' && typeof renderDetail === 'function') renderDetail();
}

// ---- the playhead inspector: state at the playhead, assembled from every
// change up to here (replaces the selection card while Told is open) ----
function arValAt(arr, p, ramp){
  if (!arr.length) return null;
  if (p <= arr[0].p) return arr[0].v;
  for (let i = 1; i < arr.length; i++) if (p < arr[i].p) {
    const r = ramp === true || arr[i].ramp;
    return r ? arr[i - 1].v + (arr[i].v - arr[i - 1].v) * (p - arr[i - 1].p) / (arr[i].p - arr[i - 1].p) : arr[i - 1].v;
  }
  return arr[arr.length - 1].v;
}
const AR_FREE_LBL = { '0': '0 · Neutral', '-1': '− Conformity', '-2': '−− Control', '-3': '−−− Captivity' };

// ---- the assembled record (BOLO 90 step 7): base record + pending-replayed
// diffs, per ssot_02_character_state_architecture.md's query protocol (base ->
// diffs -> derived -> flags) — one subject (ruling 6's "Who"), at the playhead.
const AR_LAYER_CODE_RE = /^([LS]\d+)_/;
function arLayerCode(field){ const m = AR_LAYER_CODE_RE.exec(field || ''); return m ? m[1] : null; }
function arTrim90(s){ s = String(s == null ? '' : s); return s.length > 90 ? s.slice(0, 89) + '…' : s; }
// latest point (base yaml or a replayed pending edit — arBuildEditable already
// folded both into AR_PTS) at or before the playhead, one per exact field
function arSubjPointsAt(subject, ph){
  const byField = new Map();
  for (const p of AR_PTS) {
    if (p.subject !== subject || p.p > ph + 1e-6) continue;
    const cur = byField.get(p.field);
    if (!cur || p.p >= cur.p) byField.set(p.field, p);
  }
  return byField;
}
function arKnownSubjects(){
  const s = new Set();
  for (const id of AR_SUBJECTS_WITH_POINTS) { const full = arSubjectForTrack(id); if (full) s.add(full); }
  for (const k of Object.keys(AR_BASES)) s.add(k);
  return Array.from(s);
}
function arWhoRowHtml(){
  const subs = arKnownSubjects();
  if (subs.length < 2) return '';
  return `<div class="grp" style="margin-bottom:10px"><div class="glbl"><i></i>Who</div>
    <div style="display:flex;flex-wrap:wrap;gap:6px">${subs.map(s => `<button type="button" class="chip who${s === AR_INSPECT_SUBJECT ? ' on' : ''}" data-whosubj="${esc(s)}">${esc(arSubjLabel(s))}</button>`).join('')}</div></div>`;
}
function arAssembledRecordHtml(subject, ph){
  const base = AR_BASES[subject] || null;
  const isPlace = arIsPlace(subject);
  const byField = arSubjPointsAt(subject, ph);
  let html = arWhoRowHtml();
  html += `<div class="grp" style="margin-bottom:10px"><div class="glbl" style="--k:${isPlace ? 'var(--c-place)' : 'var(--c-char)'}"><i></i>${esc(arSubjLabel(subject))}${base ? '' : ' — no base record yet'}</div>`;
  if (base) {
    html += '<dl class="kv">';
    for (const l of base.layers) {
      const disp = isPlace ? arTrim90(l.value) : l.value;
      const title = isPlace ? l.value : (l.fed_by ? `Fed by: ${l.fed_by}` : '');
      const subs = [];
      for (const [field, pt] of byField) { if (arLayerCode(field) === l.code) subs.push({ field, pt }); }
      if (!subs.length) {
        html += `<dt class="base-only" title="${esc(title)}">${esc(l.code)} ${esc(l.name)}</dt><dd title="${esc(title)}">${esc(disp)}</dd>`;
        continue;
      }
      for (const s of subs) {
        const sub = s.field.includes('.') ? s.field.split('.').slice(1).join('.') : s.field;
        const pend = s.pt._pendingEdit ? ' pending' : '';
        html += `<dt title="${esc(title)}">${esc(l.code)} ${esc(l.name)} · ${esc(sub)}</dt>
          <dd class="chg${pend}">${esc(disp)} → ${esc(String(s.pt.value))} <span class="mono" style="font-size:10px;color:var(--ink-3)">${esc(s.pt.at)}</span>${s.pt.origin_event ? ' · ' + esc(s.pt.origin_event) : ''}${s.pt._pendingEdit ? ' <span class="chip prov">pending</span>' : ''}</dd>`;
      }
    }
    html += '</dl>';
  }
  html += '</div>';
  const stateRows = [];
  for (const [field, pt] of byField) { if (!arLayerCode(field)) stateRows.push({ field, pt }); }
  stateRows.sort((a, b) => a.field.localeCompare(b.field));
  html += `<div class="grp" style="margin-bottom:10px"><div class="glbl" style="--k:var(--ink-3)"><i></i>State</div><dl class="kv">`;
  html += stateRows.length
    ? stateRows.map(s => `<dt>${esc(s.field)}</dt><dd class="${s.pt._pendingEdit ? 'chg pending' : ''}">${esc(String(s.pt.value))} <span class="mono" style="font-size:10px;color:var(--ink-3)">${esc(s.pt.at)}</span>${s.pt._pendingEdit ? ' <span class="chip prov">pending</span>' : ''}</dd>`).join('')
    : `<dt>no change yet</dt><dd>—</dd>`;
  html += `</dl></div>`;
  html += `<p class="note" style="font-size:12.5px;color:var(--ink-2)">derived: none ruled yet</p>`;
  if (base && base.flags.length) {
    html += `<div class="grp"><div class="glbl" style="--k:var(--c-char)"><i></i>Flags</div>
      <div style="display:flex;flex-wrap:wrap;gap:6px">${base.flags.map(f => `<span class="chip${f.state === 'active' ? ' ok' : f.state === 'pending' ? ' prov' : ''}" title="${esc(f.state)}">${esc(f.name)}</span>`).join('')}</div></div>`;
  }
  return html;
}
function toldInspectorHtml(){
  if (!AR_SCENES.length) return '<p class="empty-detail">No scenes in the tracking file yet.</p>';
  if (TS_STATE.view === 'world') {
    if (!AR_WORLD.length) return '<p class="empty-detail">No world events on record.</p>';
    const i = Math.max(0, Math.min(AR_WORLD.length - 1, Math.floor(TS_STATE.wph)));
    let name = null;
    for (let k = 0; k <= i; k++) if (AR_WORLD[k].dcus_name) name = AR_WORLD[k].dcus_name;
    const e = AR_WORLD[i];
    return `<h3><small class="lbl">WORLD CLOCK · ${esc((e.m || '').toUpperCase())}</small>${esc(e.label)}</h3>
      <div class="mono" style="font-size:12px;color:var(--ink-3);margin:4px 0 10px">${esc(e.id)}</div>
      <div class="grp"><div class="glbl" style="--k:var(--c-place)"><i></i>DCUS · <span class="t" data-tt="gloss" data-id="checkpoint">checkpoint</span></div>
      <dl class="kv"><dt>header.live_name</dt><dd class="chg">${esc(name || 'no checkpoint yet')}</dd></dl></div>
      <p class="note" style="font-size:12.5px;color:var(--ink-2)">Drag the playhead across the backstory to watch the live name flip at each rename. Flip to <span class="t" data-tt="gloss" data-id="told">told order</span> or <span class="t" data-tt="gloss" data-id="stack">stack</span> for the told-order read.</p>`;
  }
  const c = arCodeAt(TS_STATE.ph);
  let html = `<h3 style="margin:0 0 2px;font-family:var(--display);font-weight:800;font-size:18px;text-transform:uppercase">${esc(c.sc.mv)} · ${esc(c.sc.q)} · ${esc(c.sc.s)} · ${c.sc.num}/${c.sc.den}</h3>
    <div style="font-size:14px;margin-bottom:4px">${esc(c.sc.label)}</div>
    <div class="mono" style="font-size:12.5px;color:var(--ink-3);background:var(--well);border:1px solid var(--line);padding:5px 7px;margin-bottom:10px">${esc(c.text)}</div>`;
  html += arAssembledRecordHtml(AR_INSPECT_SUBJECT, TS_STATE.ph);
  for (const a of AR_AUTOMATION) {
    if (!a.points.length) continue;
    const v = arValAt(a.points, TS_STATE.ph);
    const lo = a.range[0], hi = a.range[1];
    html += `<div class="grp" style="margin-bottom:10px"><div class="glbl" style="--k:var(--c-char)"><i></i>${esc(arSubjLabel(a.subject))} · <span class="t" data-tt="gloss" data-id="ramp">${esc((a.field || '').split('.').pop())}</span></div>
      <dl class="kv"><dt>value</dt><dd>${v == null ? '—' : v.toFixed(2)}</dd></dl>
      <div class="meter"><b style="width:${v == null ? 0 : Math.round((v - lo) / (hi - lo) * 100)}%"></b></div></div>`;
  }
  if (AR_FREE_IN.length || AR_FREE_AUD.length) {
    const fi = arValAt(AR_FREE_IN, TS_STATE.ph, true), fa = arValAt(AR_FREE_AUD, TS_STATE.ph, true);
    html += `<div class="grp" style="margin-bottom:10px"><div class="glbl" style="--k:var(--c-theme)"><i></i>Theme · <span class="t" data-tt="gloss" data-id="freedom">Freedom</span></div>
      <dl class="kv"><dt>in-world</dt><dd>${fi == null ? 'none on record' : esc(AR_FREE_LBL[String(Math.round(fi))] || fi)}</dd><dt>audience</dt><dd class="${fa != null && fa !== fi ? 'chg' : ''}">${fa == null ? 'none on record' : esc(AR_FREE_LBL[String(Math.round(fa))] || fa)}</dd></dl>
      <p class="note" style="font-size:12px;color:var(--ink-2)">${fa != null && fi != null && fa !== fi ? 'The gap is open: the record says one thing, the reader sees another.' : 'No gap on record.'}</p></div>`;
  }
  if (AR_TEMPO_PLANNED.length) {
    const tp = arValAt(AR_TEMPO_PLANNED.map(p => ({ p: p.p, v: p.bpm, ramp: p.ramp })), TS_STATE.ph, true);
    const tm = AR_TEMPO_MEASURED.length ? arValAt(AR_TEMPO_MEASURED.map(p => ({ p: p.p, v: p.bpm, ramp: p.ramp })), TS_STATE.ph, true) : null;
    html += `<div class="grp" style="margin-bottom:10px"><div class="glbl" style="--k:var(--accent)"><i></i><span class="t" data-tt="gloss" data-id="tempo">Tempo</span></div>
      <dl class="kv"><dt>planned</dt><dd>${Math.round(tp)} bpm</dd><dt>measured</dt><dd>${tm == null ? 'none until a draft exists' : Math.round(tm) + ' bpm'}</dd></dl></div>`;
  }
  const live = AR_CABLES.filter(k => k.a <= TS_STATE.ph + 1e-6);
  const chip = orphan => orphan === 'provisional' ? `<span class="chip prov"><span class="t" data-tt="gloss" data-id="provisional">provisional</span></span>`
    : (orphan === 'setup_no_payoff' || orphan === 'payoff_no_setup') ? `<span class="chip orph"><span class="t" data-tt="gloss" data-id="orphan">orphan</span></span>`
    : `<span class="chip ok">paid off</span>`;
  html += `<div class="grp"><div class="glbl" style="--k:var(--accent)"><i></i><span class="t" data-tt="gloss" data-id="cable">Cables</span> set up so far</div>`;
  html += live.length ? live.map(k => `<div class="cab"><div><b>${esc(k.id)}</b> ${chip(k.orphan)}</div><span class="mono">${esc(k.setup.at)}${k.payoff ? ' → ' + esc(k.payoff.at) : ' → (no payoff)'}</span><br><span style="font-size:12px">${esc(k.why)}</span></div>`).join('') : `<p class="note" style="font-size:12.5px;color:var(--ink-2)">None yet. Move the playhead right.</p>`;
  html += `</div>`;
  if (AR_TROPE_PTS.length) {
    const tropes = AR_TROPE_PTS.filter(t => t.p <= TS_STATE.ph).slice(-2).reverse();
    if (tropes.length) html += `<div class="grp" style="margin-top:10px"><div class="glbl" style="--k:var(--c-trope)"><i></i>Tropes in play</div><dl class="kv">${tropes.map(t => `<dt>${esc(t.name)}</dt><dd>${Object.entries(t.keys || {}).map(([d, kk]) => d + ' ' + kk).join(', ') || '—'}</dd>`).join('')}</dl></div>`;
  }
  return html;
}

// ---- Told view controls ----
(function(){
  const zs = document.getElementById('toldZoomSeg');
  if (zs) {
    zs.innerHTML = AR_ZOOMS.map(([nm]) => `<button data-z="${esc(nm)}" aria-pressed="false">${esc(nm)}</button>`).join('');
    zs.addEventListener('click', e => {
      const b = e.target.closest('button'); if (!b) return;
      const z = AR_ZOOMS.find(z => z[0] === b.dataset.z)[1];
      if (b.dataset.z === 'Story') { arFit(); toldRender(); return; }
      if (!TS_STATE.ppb) arFit();
      TS_STATE.off = TS_STATE.ph - (arW() / 2) / z; TS_STATE.ppb = z; arClampOff(); toldRender();
    });
  }
  const rs = document.getElementById('toldRulerSeg');
  if (rs) rs.addEventListener('click', e => {
    const b = e.target.closest('button'); if (!b) return;
    TS_STATE.view = b.dataset.v; if (TS_STATE.view === 'stack') arFit(); toldRender();
  });
  const lane = arLaneEl();
  if (!lane) return;
  lane.addEventListener('wheel', e => {
    e.preventDefault();
    if (TS_STATE.view === 'world') return;
    const r = lane.getBoundingClientRect();
    if (e.shiftKey || Math.abs(e.deltaX) > Math.abs(e.deltaY)) { if (!TS_STATE.ppb) arFit(); TS_STATE.off += (e.deltaX || e.deltaY) / TS_STATE.ppb; arClampOff(); toldRender(); return; }
    arSetZoom((TS_STATE.ppb || 2.2) * Math.exp(-e.deltaY * 0.0015), e.clientX - r.left);
  }, { passive: false });
  let arDrag = null;
  function arMovePH(x){
    if (TS_STATE.view === 'world') { if (AR_WORLD.length) TS_STATE.wph = Math.max(0, Math.min(AR_WORLD.length - .01, (x - 12) / (TS_STATE._colW || 1))); }
    else TS_STATE.ph = Math.max(0, Math.min(AR_TOTAL - .01, TS_STATE.off + x / (TS_STATE.ppb || 1)));
    toldRender();
  }
  const arEditable = () => AR_EDIT.mode && !AR_EDIT.readOnly && TS_STATE.view === 'told';
  function arTrackAtY(y){
    return AR_TRACKS.find(t => AR_SUBJECTS_WITH_POINTS.includes(t.id) && t._y != null && y >= t._y && y < t._y + t._h) || null;
  }
  function arPosFromX(x){ return TS_STATE.off + x / (TS_STATE.ppb || 1); }
  function arBpmFromY(y){
    const box = TS_STATE._tempoBox; if (!box) return 100;
    const frac = 1 - Math.max(0, Math.min(1, (y - box.y - 6) / Math.max(1, box.h - 12)));
    return Math.round(box.lo + frac * (box.hi - box.lo));
  }
  function arCommitTempoDraft(){
    if (!AR_TEMPO_DRAFT) return;
    const pts = AR_TEMPO_DRAFT.slice().sort((a, b) => arPos(a.at) - arPos(b.at)).map(p => ({ at: p.at, bpm: p.bpm, ramp: !!p.ramp }));
    AR_TEMPO_DRAFT = null;
    arWriteEdit('tempo.planned', { points: pts });
  }
  lane.addEventListener('pointerdown', e => {
    const r = lane.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
    // clicking a story point selects its subject for the playhead inspector
    // (ruling 6) whether or not edit mode is on — falls through to the
    // existing edit-mode drag/select logic below unchanged
    const ptElAny = e.target.closest('[data-ptkey]');
    if (ptElAny) {
      const ptAny = AR_PTS.find(p => arPKey(p) === ptElAny.dataset.ptkey);
      if (ptAny && ptAny.subject) arSetInspectSubject(ptAny.subject);
    }
    if (arEditable()) {
      const ptEl = e.target.closest('[data-ptkey]');
      if (ptEl) {
        const pt = AR_PTS.find(p => arPKey(p) === ptEl.dataset.ptkey);
        if (pt) {
          AR_SELECTED_POINT = pt; AR_SELECTED_CABLE = null;
          if (e.altKey || AR_EDIT.cableTool) { arDrag = { mode: 'cable' }; AR_CABLE_DRAG = { fromPt: pt, curX: x, curY: y }; }
          else arDrag = { mode: 'point', target: pt, origKey: { subject: pt.subject, field: pt.field, at: pt.at }, curCode: pt.at };
          toldRender(); lane.setPointerCapture(e.pointerId); return;
        }
      }
      const cabEl = e.target.closest('[data-cab]');
      if (cabEl) {
        AR_SELECTED_CABLE = AR_CABLES.find(c => c.id === cabEl.dataset.cab) || null; AR_SELECTED_POINT = null;
        toldRender(); return;
      }
      const box = TS_STATE._tempoBox;
      if (box && y >= box.y && y < box.y + box.h) {
        if (e.button === 2) return; // right-click delete handled by the 'contextmenu' listener below
        const tEl = e.target.closest('[data-tempoat]');
        if (e.altKey) {
          const at = tEl ? tEl.dataset.tempoat : null;
          if (at) { arWriteEdit('tempo.planned', { points: AR_TEMPO_PLANNED.filter(p => p.at !== at).map(p => ({ at: p.at, bpm: p.bpm, ramp: !!p.ramp })) }); }
          return;
        }
        const draft = AR_TEMPO_PLANNED.map(p => ({ at: p.at, bpm: p.bpm, ramp: !!p.ramp }));
        let idx;
        if (tEl) { idx = draft.findIndex(p => p.at === tEl.dataset.tempoat); }
        else {
          const code = arCodeForPos(arPosFromX(x)); if (!code) return;
          draft.push({ at: code, bpm: arBpmFromY(y), ramp: false });
          idx = draft.length - 1;
        }
        if (idx == null || idx < 0) return;
        AR_TEMPO_DRAFT = draft; arDrag = { mode: 'tempo', idx };
        arBuildEditable(); toldRender(); lane.setPointerCapture(e.pointerId); return;
      }
    }
    const onRuler = y < AR_BAND_H * 2 + AR_RULE_H || (TS_STATE.view === 'stack' && y > arH() * .5 + 18 && y < arH() * .5 + 18 + AR_BAND_H * 2);
    if (TS_STATE.view === 'world' || onRuler) { arDrag = { mode: 'ph' }; arMovePH(x); }
    else arDrag = { mode: 'pan', x, off: TS_STATE.off };
    lane.setPointerCapture(e.pointerId);
  });
  lane.addEventListener('pointermove', e => {
    if (!arDrag) return;
    const r = lane.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
    if (arDrag.mode === 'ph') { arMovePH(x); return; }
    if (arDrag.mode === 'pan') { if (!TS_STATE.ppb) arFit(); TS_STATE.off = arDrag.off - (x - arDrag.x) / TS_STATE.ppb; arClampOff(); toldRender(); return; }
    if (arDrag.mode === 'point') {
      const code = arCodeForPos(arPosFromX(x)); if (!code) return;
      arDrag.curCode = code;
      arDrag.target.at = code; arDrag.target.p = arPos(code);
      toldRender(); return;
    }
    if (arDrag.mode === 'cable') { AR_CABLE_DRAG.curX = x; AR_CABLE_DRAG.curY = y; toldRender(); return; }
    if (arDrag.mode === 'tempo' && AR_TEMPO_DRAFT) {
      const code = arCodeForPos(arPosFromX(x)); if (code) AR_TEMPO_DRAFT[arDrag.idx].at = code;
      AR_TEMPO_DRAFT[arDrag.idx].bpm = arBpmFromY(y);
      arBuildEditable(); toldRender(); return;
    }
  });
  lane.addEventListener('pointerup', e => {
    if (arDrag && arDrag.mode === 'point') {
      if (arDrag.curCode && arDrag.curCode !== arDrag.origKey.at) arWriteEdit('point.move', { key: arDrag.origKey, to: arDrag.curCode });
      else { arBuildEditable(); toldRender(); }
    } else if (arDrag && arDrag.mode === 'cable') {
      const r = lane.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
      const dropEl = document.elementFromPoint(e.clientX, e.clientY);
      const toEl = dropEl && dropEl.closest && dropEl.closest('[data-ptkey]');
      const toPt = toEl ? AR_PTS.find(p => arPKey(p) === toEl.dataset.ptkey) : null;
      const from = AR_CABLE_DRAG.fromPt;
      AR_CABLE_DRAG = null;
      if (!toPt || arPKey(toPt) === arPKey(from)) { toldRender(); }
      else {
        const why = window.prompt('Why does this cable exist? (setup → payoff)', '');
        if (why != null && why.trim()) {
          arWriteEdit('cable.add', { id: 'c' + Date.now(), setup: { track: from.subject, at: from.at }, payoff: { track: toPt.subject, at: toPt.at }, why: why.trim() });
        } else toldRender();
      }
    } else if (arDrag && arDrag.mode === 'tempo') {
      arCommitTempoDraft();
    }
    arDrag = null;
  });
  lane.addEventListener('contextmenu', e => {
    if (!arEditable()) return;
    const tEl = e.target.closest('[data-tempoat]');
    if (!tEl) return;
    e.preventDefault();
    arWriteEdit('tempo.planned', { points: AR_TEMPO_PLANNED.filter(p => p.at !== tEl.dataset.tempoat).map(p => ({ at: p.at, bpm: p.bpm, ramp: !!p.ramp })) });
  });
  lane.addEventListener('dblclick', e => {
    if (!arEditable()) return;
    if (e.target.closest('[data-ptkey], [data-cab], [data-tempoat]')) return;
    const r = lane.getBoundingClientRect(), y = e.clientY - r.top, x = e.clientX - r.left;
    const track = arTrackAtY(y); if (!track) return;
    const code = arCodeForPos(arPosFromX(x)); if (!code) return;
    arOpenAddForm(track.id, code, e.clientX, e.clientY);
  });
  new ResizeObserver(() => { if (!TS_STATE.ppb) arFit(); arClampOff(); toldRender(); }).observe(lane);
})();

function arOpenAddForm(trackId, atCode, clientX, clientY){
  const el = document.getElementById('toldAddForm'); if (!el) return;
  const subject = (AR_PTS.find(p => p.tr === trackId) || {}).subject || trackId;
  el.innerHTML = `
    <div><b class="mono" style="font-size:11px;color:var(--ink-3)">${esc(arSubjLabel(subject))} · ${esc(atCode)}</b></div>
    <div><label>Field</label><input type="text" id="afField" placeholder="e.g. control_state"></div>
    <div><label>Value</label><input type="text" id="afValue" placeholder="e.g. captivity"></div>
    <div><label>Origin event (optional)</label><input type="text" id="afOrigin"></div>
    <div class="row"><button data-a="cancel">Cancel</button><button data-a="add" class="go">Add</button></div>`;
  el.style.left = Math.max(12, Math.min(window.innerWidth - 260, clientX)) + 'px';
  el.style.top = Math.max(12, Math.min(window.innerHeight - 180, clientY)) + 'px';
  el.hidden = false;
  el.querySelector('#afField').focus();
  const close = () => { el.hidden = true; el.innerHTML = ''; };
  el.querySelector('[data-a="cancel"]').addEventListener('click', close);
  el.querySelector('[data-a="add"]').addEventListener('click', () => {
    const field = el.querySelector('#afField').value.trim();
    const value = el.querySelector('#afValue').value.trim();
    const origin = el.querySelector('#afOrigin').value.trim();
    if (!field || !value) { arSetMsg('field and value are both required'); return; }
    arWriteEdit('point.add', { subject, field, value, at: atCode, origin_event: origin || undefined });
    close();
  });
}
function arStepBeat(dir){
  if (!AR_SCENES.length) return;
  TS_STATE.ph = Math.max(0, Math.min(AR_TOTAL - .01, Math.floor(TS_STATE.ph) + dir + .05));
  if (!TS_STATE.ppb) arFit();
  const px = arX(TS_STATE.ph); const w = arW();
  if (px < 20 || px > w - 20) { TS_STATE.off = TS_STATE.ph - w / 2 / TS_STATE.ppb; arClampOff(); }
  toldRender();
}
function arCycleRuler(){
  TS_STATE.view = TS_STATE.view === 'told' ? 'world' : TS_STATE.view === 'world' ? 'stack' : 'told';
  if (TS_STATE.view === 'stack') arFit();
  toldRender();
}

// ---- detail rail: selection-only, 4-6 key fields + a "more" disclosure (call 79-3) ----
let detailTab = 'detail';
function renderDetail(){
  const el = $('#detail');
  const tabs = `<div class="detail-tabs"><button data-t="detail" class="${detailTab==='detail'?'on':''}">Detail</button><button data-t="character" class="${detailTab==='character'?'on':''}">Tori</button></div>`;
  if (detailTab === 'character'){ el.innerHTML = tabs + characterSheetHtml(); wireCharacterSheet(); return; }
  if (state.lens === 'told' && detailTab === 'detail'){ el.innerHTML = tabs + '<div class="told-insp">' + toldInspectorHtml() + '</div>'; return; }
  if (!state.selection){ el.innerHTML = tabs + '<p class="empty-detail">Nothing selected. Click any marker, node, or scene to fill this panel.</p>'; return; }
  el.innerHTML = tabs + detailCardHtml(state.selection.type, state.selection.id);
}
$('#detail').addEventListener('click', e => {
  const t = e.target.closest('.detail-tabs button');
  if (t){ detailTab = t.dataset.t; renderDetail(); return; }
  const who = e.target.closest('[data-whosubj]');
  if (who){ arSetInspectSubject(who.dataset.whosubj); return; }
  const trait = e.target.closest('.trait.linked');
  if (trait){ detailTab = 'detail'; select('event', trait.dataset.event); return; }
});

function detailCardHtml(type, id){
  if (type === 'event'){
    const e = eventsById[id]; if (!e) return '<p class="empty-detail">Unknown event.</p>';
    return `<div class="dcard"><div class="kind">Fabula event · ${esc(e.kernel_satellite)}</div><h3>${esc(e.event_id)}</h3>
      <dl>
        <div><dt>Transition</dt><dd>${esc(e.transition)}</dd></div>
        <div><dt>Movement</dt><dd>${esc(e.time.movement)}</dd></div>
        <div><dt>Actors</dt><dd>${e.actors.map(a=>esc(a.actor)+' ('+esc(a.actant_role)+')').join(', ')}</dd></div>
        <div><dt>Gap / repeat</dt><dd>${esc(e.gap_type)}${e.repeat? ' · repeat (iterative)':''}</dd></div>
      </dl>
      <details class="more-block"><summary>More — reach, location, causal edges</summary>
        <dl>
          <div><dt>Reach / extent</dt><dd>${esc(e.time.reach)}; ${esc(e.time.extent)}</dd></div>
          <div><dt>Location</dt><dd>${esc(e.location)}</dd></div>
          <div><dt>Causal edges</dt><dd>${(e.causal_edges||[]).length? e.causal_edges.map(c=>esc(c.type)+' → '+esc(c.to)).join('; ') : 'none on record'}</dd></div>
        </dl>
      </details>
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
    const hasMore = (n.same_as && n.same_as.length) || n.seat_why;
    return `<div class="dcard"><div class="kind">Rails node · ${esc(n.family)} #${n.n} · ${esc(n.phase)} phase</div><h3>${esc(n.name)}</h3>
      <p style="font-size:13.5px;margin:4px 0 0">${esc(n.def)}</p>
      <dl><div><dt>Tropes keyed (${tropes.length})</dt><dd><ul class="tlist" style="list-style:none;padding:0;margin:6px 0 0">${shown.map(t=>{ const alt = t.alt ? nodesById[t.alt] : null; return `<li style="border-left:2px solid var(--line-2);padding-left:6px;margin-bottom:4px">${esc(t.name)}${alt?`<div class="or-line">or: ${esc(alt.name)}</div>`:''}</li>`; }).join('')}${tropes.length>6?`<li class="more">+ ${tropes.length-6} more — hover the node on the rails for the capped tooltip</li>`:''}</dd></div></dl>
      ${hasMore ? `<details class="more-block"><summary>More — same-as, seat</summary>
        ${n.same_as && n.same_as.length ? `<dl><div><dt>Same as</dt><dd>${n.same_as.map(esc).join(', ')}</dd></div></dl>`:''}
        ${n.seat_why?`<dl><div><dt>Seat</dt><dd>${esc(n.throughline)} · ${n.column==='side'?'any act':esc(n.column.replace('act','Act '))} — ${esc(n.seat_why)}</dd></div></dl>`:''}
      </details>` : ''}
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
      </dl>
      <details class="more-block"><summary>More — collision, told vs happened</summary>
        <dl>
          <div><dt>Collision</dt><dd>${esc(s.collision)}</dd></div>
          <div><dt>Told vs happened</dt><dd>${esc(s.order_told_vs_happened)}</dd></div>
        </dl>
      </details>
      <div class="src">source: ${esc(s.source)}</div></div>`;
  }
  return '<p class="empty-detail">Nothing selected.</p>';
}
$('#detail').addEventListener('click', e => {
  const jb = e.target.closest('[data-jump="told"]');
  if (jb){
    setLens('told');
    // the same beat the Rails signpost cell names (M2 row 9) — move the Arrangement's
    // playhead there so the jump lands on the actual scene, not just the view.
    const sc = AR_SCENES.find(s => s.mv === 'M2' && s.q === 'Q1' && s.s === 'S03');
    if (sc) { TS_STATE.ph = sc.start + 0.05; if (!TS_STATE.ppb) arFit(); TS_STATE.off = TS_STATE.ph - (arW() / 2) / (TS_STATE.ppb || 2.2); arClampOff(); }
    toldRender();
    logEvent('told', "jumped from Rails · M2 · Q1 · S03 (the one carded scene)");
  }
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

// ---- canvas click delegation (fabula/rails/told selection; empty canvas clears it) ----
$('#canvas').addEventListener('click', e => {
  if (state.lens === 'told' && e.target.closest('#arWrap, #toldToolbar')) return;  // the Told view runs its own playhead click model
  const el = e.target.closest('[data-sel-type]');
  if (el) { select(el.dataset.selType, el.dataset.selId); return; }
  if (e.target.closest('button, input, a, .t')) return;  // an interactive control, not "empty canvas"
  clearSelection();
});

// ==================================================================
// ---- Info View strip (Ableton): one line, whatever the pointer is over ----
// ==================================================================
function infoLineFor(el){
  const tt = el.dataset.tt, id = el.dataset.id;
  if (tt === 'node'){ const n = nodesById[id]; return n ? `${n.name} — ${trimJs(n.def, 110)}` : ''; }
  if (tt === 'trope-of'){ const node = nodesById[el.dataset.node]; const t = node && (node.tropes||[]).find(x => x.slug === id); return t ? `${t.name} — ${trimJs(t.def, 110)}` : ''; }
  if (tt === 'event'){ const e = eventsById[id]; return e ? `${e.event_id.replace(/_/g,' ')} — ${trimJs(e.transition, 110)}` : ''; }
  if (tt === 'era'){ const e = erasById[id]; return e ? `${e.label} — ${trimJs(e.detail, 110)}` : ''; }
  if (tt === 'signpost'){ const f = DATA.rails.fill[id]; return f ? `${f.label} — ${trimJs(f.detail, 110)}` : `Signpost ${id.replace('|',' · act ')} — no instance found, unverified.`; }
  if (tt === 'told'){ const s = DATA.told.scene; return `${s.address} — ${s.signpost}`; }
  if (tt === 'tl'){ const t = DATA.rails.throughlines.find(x => x.id === id); return t ? `${t.id} (${t.pov}) — ${t.name}: ${trimJs(t.role, 90)}` : ''; }
  if (tt === 'gloss'){ const g = DATA.glossary[id]; return g ? `${g.t} — ${trimJs(g.d, 110)}` : ''; }
  return '';
}
function setInfoView(text){ const el = $('#ivText'); if (el) el.textContent = text || DEFAULT_INFO; }
document.addEventListener('mouseover', e => {
  const el = e.target.closest('[data-tt]'); if (!el) return;
  state.hoverTarget = el; setInfoView(infoLineFor(el));
});
document.addEventListener('mouseout', e => {
  const el = e.target.closest('[data-tt]'); if (!el) return;
  const to = e.relatedTarget && e.relatedTarget.closest ? e.relatedTarget.closest('[data-tt]') : null;
  if (!to){ state.hoverTarget = null; setInfoView(DEFAULT_INFO); }
});
document.addEventListener('focusin', e => {
  const el = e.target.closest('[data-tt]'); if (el){ state.hoverTarget = el; setInfoView(infoLineFor(el)); }
});
document.addEventListener('focusout', e => {
  const el = e.target.closest('[data-tt]'); if (el){ state.hoverTarget = null; setInfoView(DEFAULT_INFO); }
});

// ==================================================================
// ---- tooltip layer: CK3 nested tooltips, depth<=3 — open on click or Space
// on the hovered/focused term (never on hover alone), nest as before, Esc closes ----
// ==================================================================
let tips = [];

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
    <div class="hint2">Esc or click elsewhere closes</div>`;
}
function nodeTipHtml(node, depth){
  const tropes = (node.tropes||[]).slice(0,6);
  const rest = (node.tropes||[]).length - tropes.length;
  return `<div class="th"><b>${esc(node.name)}</b><span class="k">${esc(node.family)} node</span></div>
    <p>${esc(node.def)}</p>
    <ul class="tlist">${tropes.map(t => `<li><span class="t" data-tt="trope-of" data-node="${node.id}" data-id="${esc(t.slug)}" tabindex="0">${esc(t.name)}</span></li>`).join('')}</ul>
    ${rest > 0 ? `<div class="more">+ ${rest} more</div>` : ''}
    <div class="hint2">click a trope to open it · Esc closes</div>`;
}
function eventTipHtml(ev, depth){
  return `<div class="th"><b>${esc(ev.event_id)}</b><span class="k">fabula event</span></div>
    <p>${esc(ev.transition)}</p>
    <div class="w">${esc(ev.time.movement)} · ${esc(ev.time.reach)}${ev.repeat?' · <span class="t" data-tt="gloss" data-id="repeat" tabindex="0">repeat</span>':''}</div>
    <div class="hint2">Esc or click elsewhere closes</div>`;
}
function eraTipHtml(era){
  return `<div class="th"><b>${esc(era.label)}</b><span class="k">world-clock era</span></div>
    <p>${esc(era.detail)}</p>
    <div class="w">${esc(era.note)}</div>
    <div class="hint2">Esc or click elsewhere closes</div>`;
}
function signpostTipHtml(key){
  const fill = DATA.rails.fill[key];
  if (!fill) return `<div class="th"><b>${esc(key.replace('|',' · act '))}</b><span class="k">signpost</span></div><p>No instance found — rail-required, unverified.</p><div class="hint2">Esc or click elsewhere closes</div>`;
  return `<div class="th"><b>${esc(fill.label)}</b><span class="k">signpost · ${esc(fill.state)}</span></div><p>${esc(fill.detail)}</p>
    <div class="hint2">Esc or click elsewhere closes</div>`;
}
function toldTipHtml(scene){
  return `<div class="th"><b>${esc(scene.address)}</b><span class="k">told scene</span></div><p>${esc(scene.signpost)}</p>
    <div class="w">${esc(scene.order_told_vs_happened)}</div>
    <div class="hint2">Esc or click elsewhere closes</div>`;
}
function throughlineTipHtml(id, depth){
  const tl = DATA.rails.throughlines.find(t => t.id === id); if (!tl) return '';
  const deep = depth >= 3;
  return `<div class="th"><b>${esc(tl.id)}</b><span class="k">throughline · ${esc(tl.pov)}</span></div>
    <p>${esc(tl.name)} — ${esc(tl.role)}</p>
    ${!deep ? `<p><span class="t" data-tt="gloss" data-id="throughline" tabindex="0">what a throughline is →</span></p>` : '<div class="capped">nesting capped at depth 3</div>'}
    <div class="hint2">Esc or click elsewhere closes</div>`;
}
function glossTipHtml(key, depth){
  const g = DATA.glossary[key]; if (!g) return '';
  const deep = depth >= 3;
  return `<div class="th"><b>${esc(g.t)}</b><span class="k">${esc(g.k)}</span></div>
    <p>${esc(g.d)}</p>
    ${!deep ? `<div class="w">${esc(g.w||'')}</div>` : '<div class="capped">nesting capped at depth 3</div>'}
    <div class="hint2">Esc or click elsewhere closes</div>`;
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
  closeTips(depth);  // close any sibling already open at this depth
  const el = document.createElement('div');
  el.className = 'tip locked'; el.dataset.depth = depth;
  el.innerHTML = contentFor(target, depth);
  document.body.appendChild(el);
  const r = target.getBoundingClientRect(); const w = 320, h = el.offsetHeight;
  let x = Math.min(Math.max(12, r.left), window.innerWidth - w - 12);
  let y = r.bottom + 8; if (y + h > window.innerHeight - 12) y = Math.max(12, r.top - h - 8);
  el.style.left = x + 'px'; el.style.top = y + 'px';
  target.classList.add('on');
  const rec = { el, target, depth };
  tips.push(rec);
  return rec;
}
function closeTips(fromDepth){
  tips.filter(t => t.depth >= fromDepth).forEach(t => { t.el.remove(); t.target.classList.remove('on'); });
  tips = tips.filter(t => t.depth < fromDepth);
}
function toggleTip(target){
  const existing = tips.find(t => t.target === target);
  if (existing){ closeTips(existing.depth); return; }
  openTip(target, depthOf(target));
}
document.addEventListener('click', e => {
  const term = e.target.closest('.t');
  if (term){ toggleTip(term); return; }
  if (!e.target.closest('.tip')) closeTips(1);
});

// ---- keyboard: 1/2/3 views+workspace · [ ] L ` panels · - / = rails zoom · Space opens/closes the hovered term · Esc closes ----
document.addEventListener('keydown', e => {
  if (e.target.matches('input')) { if (e.key === 'Escape') e.target.blur(); return; }
  if (e.key === '1') { setLens('fabula'); return; }
  if (e.key === '2') { setLens('rails'); return; }
  if (e.key === '3') { setLens('told'); return; }
  if (e.key === '[') { togglePanel('ol'); return; }
  if (e.key === ']') { togglePanel('det'); return; }
  if (e.key.toLowerCase() === 'l') { togglePanel('log'); return; }
  if (e.key === '`') { toggleMaximize(); return; }
  if (!e.ctrlKey && !e.metaKey && e.key === '-') { setZoom('out'); return; }
  if (!e.ctrlKey && !e.metaKey && e.key === '=') { setZoom('in'); return; }
  if (state.lens === 'told' && e.key.toLowerCase() === 't') { arCycleRuler(); return; }
  if (state.lens === 'told' && (e.key === 'ArrowRight' || e.key === 'ArrowLeft')) { arStepBeat(e.key === 'ArrowRight' ? 1 : -1); e.preventDefault(); return; }
  if (state.lens === 'told' && (e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'z') { arUndoLast(); e.preventDefault(); return; }
  if (state.lens === 'told' && AR_EDIT.mode && !AR_EDIT.readOnly && (e.key === 'Delete' || e.key === 'Backspace')) {
    if (AR_SELECTED_CABLE) { arWriteEdit('cable.remove', { id: AR_SELECTED_CABLE.id }); AR_SELECTED_CABLE = null; e.preventDefault(); return; }
    if (AR_SELECTED_POINT) { arWriteEdit('point.remove', { key: { subject: AR_SELECTED_POINT.subject, field: AR_SELECTED_POINT.field, at: AR_SELECTED_POINT.at } }); AR_SELECTED_POINT = null; e.preventDefault(); return; }
  }
  if (e.key === 'Escape') { if (tips.length) closeTips(1); else clearSelection(); return; }
  if (e.key === ' ') { if (state.hoverTarget){ e.preventDefault(); toggleTip(state.hoverTarget); } return; }
});

// ==================================================================
// ---- boot: a realistic working state, canvas first ----
// ==================================================================
applyLayout();  // outliner / inspector / log all start collapsed
renderOutliner();
renderFabula();
renderTlLegend();
renderSignpostGrid();
renderFamFilter();
renderNodeColumns();
setZoom('out');
// the Told view (The Arrangement) renders lazily on first switch — its lane
// has zero size while hidden; applyLayout()/setLens() trigger toldRender() then.
renderLogFilter();
detailTab = 'detail';
// seed the log with the session's opening moves, then land on the crash event
logEvent('fabula', 'workspace opened · Fabula view (default) · Map workspace');
select('event', 'm1b_crash_jebb_death', { lensLabel: 'fabula' });
logEvent('fabula', "Tori's six fabula events loaded · 3 DCUS eras banded (fuzzy)");
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
