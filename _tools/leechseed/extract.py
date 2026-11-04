"""LEECHSEED character extract (BOLO 176, 11/4): one JSON per character for the character console and the patch bay.

    python -X utf8 _tools/leechseed/extract.py            write _tools/leechseed/characters/<id>.json, print a summary
    python -X utf8 _tools/leechseed/extract.py --json     the same, and print the summary as JSON
    python -X utf8 _tools/leechseed/extract.py --dry-run  parse and report, write nothing

Sources (read only):
  the vertical slice, its "THE INSTANCE" sections and their Structured Data Blocks (values, fill tags, the parked marker)
  _CANON_NODES/<node>.md                     name, and Jebb's card (he has no slice record yet: a stub, card fields only)
  _tools/bolostatus/work/176/<x>-fill.md     the fill lists: the confidence and the source looked at, for every row

THE CONTRACT (BAY's europatch.py reads it; do not change it):
  {"id","name","node","fields":{key:{"layer","value","native_scale","source","confidence","status":"filled|parked|held"}},
   "numbers":{"CORE":n,...},"gates":{"step1":"pass|red","step3":"pass|fail"},"counts":{"filled","parked"}}

Provisional calls (CONSOLE, 11/4):
  - counts.filled includes "held" fields, the way anna-fill.md tallies them ("19 filled (17 sourced + 2 held by rule)").
  - Tori's L9 disclosure_posture (the sexual-health register) is keyed disclosure_posture_L9; L3 keeps the plain key.
  - native_scale is {"code","range":[min,max],"default"} from the slice's scale column, or null for text, enum and list fields.
  - gates.step1 is "pass" only for a block whose STATUS is locked; step3 is "pass" when want_need.need is non-empty.
  - ORANGE (L9) values are only what the slice block itself states.
"""
import json
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SLICE_REL = "ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/\U0001F4D0 ssot_02_character_systems_vertical_slice.md"
SLICE = os.path.join(ROOT, *SLICE_REL.split("/"))
WORK = os.path.join(ROOT, "_tools", "bolostatus", "work", "176")
OUT = os.path.join(HERE, "characters")

CHARS = [   # id, node, fill list (None: card only)
    ("victoria_midnight", "_CANON_NODES/victoria-midnight.md", "tori-fill.md"),
    ("anna_colson_conway", "_CANON_NODES/anna-colson-conway.md", "anna-fill.md"),
    ("jebb_midnight", "_CANON_NODES/jebb-midnight.md", None),
]

SECTION_LAYER = {"L5_WOUND": "L5", "L7_ORIGIN": "L7", "L8_IMPRINT": "L8", "L9_EROS": "L9", "L10_SHADOW": "L10",
                 "L11_DESTINY": "L11", "L12_FUNCTION": "L12", "L12_DRAMATICA_EXTENDED": "L12"}
TIER_LAYER = {   # TIER_1 and TIER_2 fields by the slice's PART A table (fields column)
    "CORE": "L1", "psychology_stack": "L1", "assigned_labels": "L1", "neurotype": "L1",
    "VITAL": "L2", "physiology_stack": "L2", "body_capital": "L2",
    "SOCIAL": "L3", "sociology_stack": "L3", "circumplex": "L3", "pair_register": "L3", "standing": "L3",
    "civic_standing": "L3", "disclosure_posture": "L3", "voice_sheet": "L3", "community_membership": "L3",
    "WILL": "L4", "coping_strategy": "L4", "locus_of_control": "L4", "system_stance": "L4",
    "WOUND": "L5", "DRIVE": "L6", "futurity_stance": "L6", "want_need": "L6",
}


def _sc(code, lo, hi, default, note=None):
    d = {"code": code, "range": [lo, hi], "default": default}
    if note:
        d["note"] = note
    return d


SC20 = _sc("SC-20", 0, 20, 10)
SCALES = {   # the slice's scale column (PART A, RULED 11/4)
    "CORE": SC20, "VITAL": SC20, "SOCIAL": SC20,
    "WILL": _sc("SC-20", 0, 20, "= CORE"), "DRIVE": _sc("SC-20", 0, 20, "= VITAL"),
    "WOUND": _sc("SC-12", 0, 12, 0, "even values"), "severity": _sc("SC-12", 0, 12, 0, "even values"),
    "circumplex": _sc("SC-10 two-sided", -5, 5, None), "locus_of_control": _sc("SC-10 two-sided", -5, 5, None),
    "dark_triad": _sc("SC-10", 0, 10, None), "light_triad": _sc("SC-10", 0, 10, None),
    "arousal_curve": _sc("SC-10", 0, 10, None, "amplitude, spasm size"), "compersion": _sc("SC-10", 0, 10, None, "level"),
    "attraction_channels": _sc("SC-10", 0, 10, None), "dissolution": _sc("SC-10", 0, 10, None, "depth"),
    "orientation_dimensions": _sc("SC-6", 0, 6, None, "Kinsey score"),
    "group_size": {"code": "unscaled", "range": None, "default": None, "note": "a count"},
}
for _k in ("origin_stability", "family_coherence", "origin_wound_seed", "tech_level", "attachment_style_score",
           "attachment_dimensions", "emotional_range", "imprint_flexibility", "shame_index", "exposure_shame",
           "role_shame", "armor_index", "shadow_density", "projection_tendency", "resistance_index"):
    SCALES[_k] = _sc("SC-12", 0, 12, None)

FILL_TAG = re.compile(r"\((?:fill|derived) 11/4")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def frontmatter(text):
    """title and entity from a node's front matter, by line (some nodes' front matter is not strict YAML)"""
    m = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.S)
    out = {}
    for line in (m.group(1) if m else "").splitlines():
        k = re.match(r"^(title|entity):\s*(.+?)\s*$", line)
        if k and k.group(1) not in out:
            v = k.group(2)
            if len(v) > 1 and v[0] == v[-1] and v[0] in "\"'":
                v = v[1:-1]
            out[k.group(1)] = v
    return out


def comment_of(line):
    """the comment on a block line: text after the first # outside quotes"""
    q = None
    for i, c in enumerate(line):
        if q:
            if c == q:
                q = None
        elif c in "\"'" and (i == 0 or line[i - 1] in " :[{,"):
            q = c
        elif c == "#" and (i == 0 or line[i - 1] == " "):
            return line[i + 1:].strip()
    return ""


def balanced(text, start):
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "(":
            depth += 1
        elif text[i] == ")":
            depth -= 1
            if depth == 0:
                return text[start + 1:i]
    return text[start + 1:]


def tag_of(comment):
    m = FILL_TAG.search(comment)
    return balanced(comment, m.start()) if m else None


def source_of(tag):
    m = re.search(r"\bsource:?\s+(.*)", tag, re.S)
    if m:
        return m.group(1).strip()
    m = re.search(r"\brule:\s+(.*)", tag, re.S)
    if m:
        return "rule: " + m.group(1).strip()
    return tag.strip()


def empty(v):
    if v is None:
        return True
    if isinstance(v, str):
        return v.strip() == ""
    if isinstance(v, (list, tuple)):
        return len(v) == 0
    if isinstance(v, dict):
        return all(empty(x) for x in v.values())
    return False


def instance_blocks(slice_text):
    """{character_id: (instance prose, block text)} for every '## THE INSTANCE' section"""
    out = {}
    parts = re.split(r"^## THE INSTANCE · ", slice_text, flags=re.M)[1:]
    for p in parts:
        p = re.split(r"^## (?!#)", p, flags=re.M)[0]   # stop at the next H2
        i = p.find("### Structured Data Block")
        if i < 0:
            continue
        m = re.search(r"```\n(.*?)\n```", p[i:], re.S)
        if not m:
            continue
        block = m.group(1)
        cid = re.search(r"^CHARACTER_ID:\s*(\S+)", block, re.M)
        if cid:
            out[cid.group(1)] = (p[:i], block)
    return out


def block_fields(block):
    """[(section, key, comments)] in order, the comments of the field's own line and its nested lines"""
    rows, sec, cur = [], None, None
    for line in block.splitlines():
        if not line.strip():
            continue
        m = re.match(r"^([A-Z][A-Z0-9_]*):", line)
        if m:
            sec, cur = m.group(1), None
            continue
        m = re.match(r"^  ([A-Za-z_][A-Za-z0-9_]*):", line)
        if m and sec:
            cur = [sec, m.group(1), [comment_of(line)]]
            rows.append(cur)
            continue
        if cur and re.match(r"^   +\S", line):
            cur[2].append(comment_of(line))
    return [(s, k, " · ".join(c for c in cs if c)) for s, k, cs in rows]


def fill_rows(path):
    """the fill list's field table: [{names, layer, source, conf, value}]"""
    rows = []
    if not path or not os.path.isfile(path):
        return rows
    for line in read(path).splitlines():
        if not re.match(r"^\| \d+(?:[–-]\d+)? \|", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 7:   # Tori: # | Field | Layer | Scale | Proposed | Source | Conf
            _, field, layer, _scale, value, src, conf = cells
        elif len(cells) == 6:  # Anna: # | Field | Layer | Proposed | Source | Conf
            _, field, layer, value, src, conf = cells
        else:
            continue
        names = re.findall(r"`([A-Za-z_][A-Za-z0-9_]*)`", field)
        if not names and "L9 EROS" in field:
            names = ["status"]
        rows.append({"names": names, "layer": layer, "source": src, "conf": conf, "value": value})
    return rows


def conf_word(conf):
    c = conf.replace("*", "")
    if "RULED" in c:
        return "med (ruled 11/4)"
    for w in ("high", "med", "low"):
        if re.match(r"\s*" + w, c):
            return w
    if "high" in c:
        return "high"
    if "NO SOURCE" in c:
        return "none"
    return c[:40]


def classify(cid, sec, key, value, comment, status_line, fill):
    """status, source, confidence for one block field"""
    tag = tag_of(comment)
    held = ("held open by rule" in comment or value == "n_a_by_design" or "held by rule" in comment)
    if held:
        return "held", source_of(tag) if tag else comment, "held by rule"
    if tag and (not empty(value) or "ruled null" in comment):
        conf = "derived (provisional)" if tag.startswith("derived") else (
            "med (ruled 11/4)" if re.search(r"\bmed\b", tag.split("source")[0]) or "ruled Chief" in tag else "high")
        if fill and fill["conf"]:
            fc = conf_word(fill["conf"])
            if conf == "high" and fc.startswith("med"):
                conf = fc
        return "filled", source_of(tag), conf
    if not empty(value):
        src = "slice instance block (%s)" % status_line
        if comment:
            src += " · " + comment
        if fill and fill["source"] and conf_word(fill["conf"]) in ("high", "med (ruled 11/4)"):
            src = fill["source"] + " · " + src
        return "filled", src, "canon (%s)" % status_line
    # parked: the marker, or a null with no tag
    src = fill["source"] if fill else (comment or "no source documented")
    conf = conf_word(fill["conf"]) if fill else ("none" if "⏸" in comment else "none")
    return "parked", src, conf


def build_slice_record(cid, node_rel, fill_name, prose, block):
    data = yaml.safe_load(block)
    status_line = "%s %s" % (data.get("STATUS", "?"), data.get("VERSION", "?"))
    rows = fill_rows(os.path.join(WORK, fill_name)) if fill_name else []
    fields, numbers, seen = {}, {}, set()
    for sec, key, comment in block_fields(block):
        layer = SECTION_LAYER.get(sec) or TIER_LAYER.get(key)
        if layer is None:
            continue   # DERIVED and FLAGS are computed, never stored (the stats engine's job)
        value = (data.get(sec) or {}).get(key)
        fkey = key if key not in seen else "%s_%s" % (key, layer)
        seen.add(key)
        fill = next((r for r in rows if key in r["names"] and r["layer"] == layer), None) or \
            next((r for r in rows if key in r["names"]), None)
        st, src, conf = classify(cid, sec, key, value, comment, status_line, fill)
        if layer == "L9" and key == "status" and value == "n_a_by_design":
            fkey = "L9_EROS"
        fields[fkey] = {"layer": layer, "value": value, "native_scale": SCALES.get(key), "source": src,
                        "confidence": conf, "status": st}
        if isinstance(value, int) and not isinstance(value, bool):
            numbers[fkey] = value
    need = ((data.get("TIER_2") or {}).get("want_need") or {}).get("need")
    gates = {"step1": "pass" if str(data.get("STATUS", "")).lower() == "locked" and "gate: red" not in prose.lower()
             else "red",
             "step3": "pass" if not empty(need) else "fail"}
    counts = {"filled": sum(1 for f in fields.values() if f["status"] in ("filled", "held")),
              "parked": sum(1 for f in fields.values() if f["status"] == "parked")}
    return fields, numbers, gates, counts


def build_card_record(node_text):
    """a stub with no slice record: the node's Structure table, one field per row, layer 'card'"""
    fields = {}
    m = re.search(r"^## Structure\n(.*?)(?=^## )", node_text, re.S | re.M)
    for line in (m.group(1) if m else "").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 3 or cells[0] in ("Field", "") or set(cells[0]) <= set("-"):
            continue
        key = re.sub(r"[^a-z0-9]+", "_", cells[0].strip("`").lower()).strip("_")
        fields[key] = {"layer": "card", "value": cells[1].replace("`", ""), "native_scale": None,
                       "source": cells[2], "confidence": "canon (card, stub)", "status": "filled"}
    return fields, {}, {"step1": "red", "step3": "fail"}, {"filled": len(fields), "parked": 0}


def extract():
    blocks = instance_blocks(read(SLICE))
    out = []
    for cid, node_rel, fill_name in CHARS:
        node_path = os.path.join(ROOT, *node_rel.split("/"))
        node_text = read(node_path) if os.path.isfile(node_path) else ""
        fm = frontmatter(node_text)
        name = fm.get("title") or fm.get("entity") or cid   # title first: Anna's is the hyphenated form
        if cid in blocks:
            fields, numbers, gates, counts = build_slice_record(cid, node_rel, fill_name, *blocks[cid])
        else:
            fields, numbers, gates, counts = build_card_record(node_text)
        out.append({"id": cid, "name": name, "node": node_rel, "fields": fields, "numbers": numbers,
                    "gates": gates, "counts": counts})
    return out


def main(argv):
    recs = extract()
    if "--dry-run" not in argv:
        os.makedirs(OUT, exist_ok=True)
        for r in recs:
            with open(os.path.join(OUT, r["id"] + ".json"), "w", encoding="utf-8", newline="\n") as f:
                json.dump(r, f, ensure_ascii=False, indent=1)
                f.write("\n")
    summary = [{"id": r["id"], "name": r["name"], "counts": r["counts"], "gates": r["gates"],
                "fields": len(r["fields"]), "numbers": len(r["numbers"])} for r in recs]
    if "--json" in argv:
        print(json.dumps({"characters": summary, "wrote": "--dry-run" not in argv, "out": rel(OUT)}, ensure_ascii=False))
    else:
        for s in summary:
            print("%-20s filled %3d  parked %3d  step1 %-4s step3 %-4s  (%d fields, %d numbers)" % (
                s["id"], s["counts"]["filled"], s["counts"]["parked"], s["gates"]["step1"], s["gates"]["step3"],
                s["fields"], s["numbers"]))
        print(("dry run, nothing written" if "--dry-run" in argv else "wrote " + rel(OUT)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
