# -*- coding: utf-8 -*-
"""EUROPATCH module catalog builder (BOLO 173): LEECHSEED's 12 layers -> modules/leechseed.json.

Reads the SSOT, never edits it:
  ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/📐 ssot_02_character_systems_vertical_slice.md
    Part A table      -> each layer's code, name, question, tier and the fields it writes
    Structured block  -> the instance's numbers (the observed value of each numeric field)
    every doc in 02   -> pick-list vocab, read from "a | b | c" or "(a · b · c)" runs after the field's name
The DIALS spec below says which fields become dials (only SFW keys: L9's explicit keys stay in _PRIVATE and link
by key). A pick's vocab comes from the doc when the doc spells it; else from the spec's cited list (vocab_src says
which). A spec field the doc no longer names fails the build (LEECHSEED changed: update the spec).

Usage:  python -X utf8 _tools/europatch/build_catalog.py [--json] [--dry-run]
"""
import io, json, os, re, sys, glob, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SSOT = os.path.join(ROOT, "ShroomsQ", "_CANON", "_SSOT", "02_CHARACTER_SYSTEMS")
SLICE = os.path.join(SSOT, "\U0001F4D0 ssot_02_character_systems_vertical_slice.md")
OUT = os.path.join(HERE, "modules", "leechseed.json")

LOW_MID_HIGH = ("low", "mid", "high")


def S(key, lo, hi, default, words, label=None, help=None):
    """a slider dial: native scale lo..hi, default in native units, words = the low/mid/high phrases"""
    return {"key": key, "kind": "slider", "native": [lo, hi], "default_native": default, "words": list(words),
            "label": label or key, "help": help or ""}


def P(key, vocab, src, label=None, help=None):
    """a pick dial: vocab = the cited fallback list; the doc's own run wins when the build finds one"""
    return {"key": key, "kind": "pick", "fallback": list(vocab), "src": src, "label": label or key, "help": help or ""}


# which fields become dials. Scales from the slice doc (Domain Declarations, Structured Data Block, Derived Statistics).
DIALS = {
    "L1": [S("CORE", 0, 20, 10, ["a light, practical mind", "an ordinary working mind", "a heavy, sharp mind"],
             help="Cognitive and ideological mass (IQ equivalent; default 10)."),
           P("psychology_stack.extrovert_introvert", ["extrovert", "introvert"], "BVX.1123 Egri psychology checklist",
             label="extro/intro", help="Egri's psychology third names extrovert/introvert on the checklist.")],
    "L2": [S("VITAL", 0, 20, 10, ["a slight, low-energy body", "a steady body", "a strong, high-energy presence"],
             help="Physical and energetic presence (DX equivalent; default 10).")],
    "L3": [S("SOCIAL", 0, 20, 10, ["hard to read and easy to miss", "socially ordinary", "reads a room and fills it"],
             help="Projection into and reading of the social world (default 10)."),
           S("circumplex.agency", -5, 5, 0, ["yielding", "even in a room", "dominant"], label="agency",
             help="Interpersonal circumplex, yielding to dominant (-5..+5)."),
           S("circumplex.communion", -5, 5, 0, ["cold", "neutral", "warm"], label="communion",
             help="Interpersonal circumplex, cold to warm (-5..+5).")],
    "L4": [S("WILL", 0, 20, 10, ["bends under pressure", "holds under ordinary pressure", "decides under any pressure"],
             help="The capacity to decide under pressure. Derives from CORE by default (WILL = CORE)."),
           S("locus_of_control", -5, 5, 0, ["owns the outcome", "a mixed locus", "puts the outcome on the world"],
             label="locus", help="Internal (-5) to external (+5)."),
           P("coping_strategy", ["naive", "cinderella", "exceptional", "pleasing", "disappointed"],
             "BVX.0045 Schmidt's five coping strategies", label="coping"),
           P("system_stance", ["cog", "believer", "mask", "bystander", "resister"], "slice doc CL25", label="stance")],
    "L5": [S("severity", 0, 10, 3, ["lightly marked", "carries real damage", "near the collapse line"],
             label="severity", help="WOUND, 0 undamaged to 10 functional collapse (Puglisi & Ackerman's severity)."),
           P("wound_kind", ["injury_suffered", "error_committed", "loss_unrecognized"], "slice doc CL22", label="kind"),
           P("relational_refs.kind", ["ghost", "revenant", "mentor", "shapeshifter"], "slice doc, BVX.0196",
             label="tie", help="The kind of character the wound keys to.")],
    "L6": [S("DRIVE", 0, 20, 10, ["running on fumes", "steady fuel", "a burning drive"],
             help="Narrative motivation fuel. Derives from VITAL by default (DRIVE = VITAL)."),
           P("futurity_stance", ["planned", "hoped", "foreclosed", "none", "refused", "horizon"], "slice doc 3.0.0",
             label="future"),
           P("drive_texture", ["more", "risk", "novelty", "abundance"], "slice doc 2.5.0 (prose list)", label="texture"),
           P("want_need.need_kind", ["psychological", "moral"], "slice doc CL16", label="need")],
    "L7": [S("origin_stability", 0, 10, 5, ["an unstable start", "an uneven start", "a stable start"], label="stability"),
           S("family_coherence", 0, 10, 5, ["a broken family", "a strained family", "a tight family"], label="family"),
           S("origin_wound_seed", 0, 10, 3, ["little early harm", "some early harm", "deep early harm"], label="wound seed",
             help="Feeds the WOUND base."),
           S("tech_level", 0, 10, 5, ["low tech", "mid tech", "high tech"], label="tech")],
    "L8": [S("attachment_style_score", 0, 10, 5, ["a faint attachment pull", "a middling attachment pull",
                                                   "a strong attachment pull"], label="attach score"),
           S("emotional_range", 0, 10, 5, ["a narrow emotional range", "a middling emotional range",
                                            "a wide emotional range"], label="range"),
           S("imprint_flexibility", 0, 10, 5, ["locked-in conditioning", "partly flexible conditioning",
                                                "flexible conditioning"], label="flexibility"),
           P("attachment_style", ["secure", "anxious", "avoidant", "fearful_avoidant"], "slice doc, BVX.1127 Attached",
             label="attachment")],
    "L9": [S("armor_index", 0, 12, 6, ["unarmored", "guarded", "heavily armored"], label="armor",
             help="Body armor; Expressive Range = 12 - armor."),
           S("exposure_shame", 0, 10, 5, ["unbothered by exposure", "some exposure shame", "exposure-shamed"],
             label="exposure shame", help="Shame under public exposure (read alias shame_index)."),
           P("intimacy_mode", ["partnered_merge", "parallel_presence", "solo_directed", "bounded_no_strings"],
             "slice doc CL2", label="intimacy"),
           P("signal_fluency", ["fluent", "functional", "illiterate"], "slice doc L9 (prose list)", label="signals")],
    "L10": [S("shadow_density", 0, 10, 5, ["a thin shadow", "a working shadow", "a dense shadow"], label="density"),
            S("projection_tendency", 0, 10, 5, ["owns what it carries", "projects at times", "projects hard"],
              label="projection"),
            P("shadow_content.kind", ["denied_wish", "assigned_by_world", "feared_double", "standing_alarm",
                                      "scrubbed_bond", "imposed_self_image"], "slice doc CL9", label="content")],
    "L11": [S("resistance_index", 0, 10, 5, ["open to change", "resists change", "fights change hard"],
              label="resistance"),
            P("arc_type", ["growth", "transformation", "hybrid"], "BVX.0196 growth vs transformation", label="arc"),
            P("change_cause", ["unmasking", "external_force", "will", "uncaused"], "BVX.0061 the four causes",
              label="cause")],
    "L12": [P("dramatica_archetype", ["Protagonist", "Antagonist", "Guardian", "Contagonist", "Reason", "Emotion",
                                      "Sidekick", "Skeptic"], "BVX.0089 the eight archetypes", label="archetype"),
            P("resolve", ["Change", "Steadfast"], "Dramatica protocol, storyform dynamics"),
            P("story_outcome", ["Success", "Failure"], "Dramatica protocol, storyform dynamics", label="outcome"),
            P("story_judgement", ["Good", "Bad"], "Dramatica protocol, storyform dynamics", label="judgement"),
            P("limit_type", ["Timelock", "Optionlock"], "Dramatica protocol, storyform dynamics", label="limit"),
            P("convention_role.actant_slot", ["subject", "object", "sender", "receiver", "helper", "opponent"],
              "Dramatica protocol CL15", label="actant")],
}

# the cables the doc itself names (Domain Declarations, Derived Statistics); "provisional" ones are the CDR's call
SUGGESTED = [
    {"from": "L1.CORE", "to": "L4.WILL", "mode": "add", "strength": 0.2, "curve": "linear",
     "why": "L4: WILL derives from CORE by default (WILL = CORE)", "src": "doc"},
    {"from": "L2.VITAL", "to": "L6.DRIVE", "mode": "add", "strength": 0.2, "curve": "linear",
     "why": "L6: DRIVE derives from VITAL by default (DRIVE = VITAL)", "src": "doc"},
    {"from": "L5.severity", "to": "L4.WILL", "mode": "add", "strength": -0.3, "curve": "threshold-soft",
     "threshold": 0.5, "soft": 0.2, "why": "L5: high WOUND reduces effective WILL under trigger conditions", "src": "doc"},
    {"from": "L5.severity", "to": "L3.SOCIAL", "mode": "add", "strength": -0.2, "curve": "threshold-soft",
     "threshold": 0.5, "soft": 0.2, "why": "L5: high WOUND reduces effective SOCIAL under trigger conditions", "src": "doc"},
    {"from": "L7.origin_wound_seed", "to": "L5.severity", "mode": "add", "strength": 0.3, "curve": "s-curve",
     "why": "L7: ORIGIN's numbers feed the WOUND base", "src": "doc"},
    {"from": "L7.origin_stability", "to": "L3.SOCIAL", "mode": "add", "strength": 0.15, "curve": "linear",
     "why": "L7: ORIGIN's numbers feed SOCIAL defaults", "src": "doc"},
    {"from": "L10.projection_tendency", "to": "L3.SOCIAL", "mode": "add", "strength": -0.1, "curve": "linear",
     "why": "Derived: Social Legibility = SOCIAL - projection/3", "src": "doc"},
    {"from": "L8.imprint_flexibility", "to": "L11.resistance_index", "mode": "multiply", "strength": -0.4,
     "curve": "ease-in", "why": "a flexible imprint lowers resistance to change", "src": "provisional"},
]

GROUPS = [   # the doc's own three tiers, as the starter sub-patches
    {"title": "Tier 1 · surface", "modules": ["L1", "L2", "L3"]},
    {"title": "Tier 2 · pressure", "modules": ["L4", "L5", "L6"]},
    {"title": "Tier 3 · depth", "modules": ["L7", "L8", "L9", "L10", "L11", "L12"]},
]

PRIVATE_NOTE = ("L9 EROS: only SFW keys are dials here. The explicit keys stay in _PRIVATE/ and link by key "
                "(a private patch can carry them under dials with the same key names).")


def read(path):
    return io.open(path, encoding="utf-8").read()


def parse_part_a(text):
    """the Part A table: | **L1** | **CORE** | question | source | fields | tier |"""
    layers = {}
    for line in text.splitlines():
        m = re.match(r"\|\s*\*\*(L\d+)\*\*\s*\|\s*\*\*([A-Z]+)\*\*\s*\|(.*)$", line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(3).split("|")]
        if len(cells) < 4:
            continue
        question, fields, tier = cells[0], cells[2], cells[3]
        layers[m.group(1)] = {"code": m.group(2), "question": question, "tier": tier,
                              "fields": re.findall(r"`([A-Za-z_]+)`", fields)}
    return layers


def parse_block(text):
    """the instance's Structured Data Block: the first `key: <int>` per key"""
    i = text.find("### Structured Data Block")
    j = text.find("```", i)
    k = text.find("```", j + 3)
    nums = {}
    keys = set()
    for line in text[j + 3:k].splitlines():
        m = re.match(r"\s+([A-Za-z_]+):\s*(-?\d+)\s*(#.*)?$", line)
        if m:
            nums.setdefault(m.group(1), int(m.group(2)))
        m2 = re.match(r"\s+([A-Za-z_]+):", line)
        if m2:
            keys.add(m2.group(1))
    return nums, keys


RUN = re.compile(r"([A-Za-z_]+(?:\s*(?:\||·)\s*[A-Za-z_]+)+)")


def doc_vocab(corpus, key, fallback):
    """the doc's own a|b|c or (a · b · c) run within 200 chars after the field's name (its root or its leaf),
    anywhere in the 02 docs. A run counts only when half or more of it is the cited list (same list, maybe grown)."""
    names = [key.split(".")[-1], key.split(".")[0]] if "." in key else [key]
    fb = set(fallback)
    best = None
    for name in names:
        for m in re.finditer(r"`?" + re.escape(name) + r"`?", corpus):
            window = corpus[m.end():m.end() + 200]
            for r in RUN.finditer(window):
                toks = [t.strip() for t in re.split(r"\||·", r.group(1)) if t.strip()]
                if len(toks) < 2 or any(len(t) > 40 for t in toks):
                    continue
                if len(fb & set(toks)) * 2 >= len(toks) and (best is None or len(toks) > len(best)):
                    best = toks
    return best


def build():
    text = read(SLICE)
    layers = parse_part_a(text)
    nums, block_keys = parse_block(text)
    corpus = "\n".join(read(p) for p in sorted(glob.glob(os.path.join(SSOT, "*.md")))).replace("\\|", "|")
    errors, drift, modules = [], [], []
    for lid in sorted(DIALS, key=lambda s: int(s[1:])):
        lay = layers.get(lid)
        if not lay:
            errors.append("%s: not in the slice doc's Part A table" % lid)
            continue
        named = set(lay["fields"]) | block_keys | {lay["code"]}
        dials = []
        for d in DIALS[lid]:
            d = dict(d)
            root = d["key"].split(".")[0]
            if root not in named and root not in text:
                errors.append("%s.%s: the doc no longer names %s" % (lid, d["key"], root))
            if d["kind"] == "slider":
                lo, hi = d["native"]
                d["default"] = round((d["default_native"] - lo) * 100.0 / (hi - lo))
                d["spread"] = 10
                obs = nums.get(root)
                if obs is not None:
                    d["observed_native"] = obs   # the locked instance's value (Victoria Midnight), for reference
            else:
                fb = d.pop("fallback")
                found = doc_vocab(corpus, d["key"], fb)
                if found:
                    d["choices"], d["vocab_src"] = found, "doc: " + d["src"]
                    if set(found) != set(fb):
                        drift.append("%s.%s: doc %s vs spec %s" % (lid, d["key"], found, fb))
                else:
                    d["choices"], d["vocab_src"] = fb, "cited: " + d["src"]
                d.pop("src", None)
            dials.append(d)
        jacks = [d["key"] for d in dials if d["kind"] == "slider"]
        modules.append({"id": lid, "code": lay["code"], "name": lay["code"].title(), "tier": lay["tier"],
                        "question": lay["question"], "fields": lay["fields"], "dials": dials,
                        "jacks_in": jacks, "jacks_out": jacks})
    for c in SUGGESTED:
        for end in (c["from"], c["to"]):
            mid, key = end.split(".", 1)
            mod = next((m for m in modules if m["id"] == mid), None)
            if not mod or key not in mod["jacks_out"]:
                errors.append("suggested cable %s: no jack %s" % (c["why"], end))
    cat = {"europatch": 1, "catalog": "leechseed", "system": "LEECHSEED (the character system)",
           "built": time.strftime("%Y-%m-%d %H:%M"), "generator": "_tools/europatch/build_catalog.py",
           "source": os.path.relpath(SLICE, ROOT).replace("\\", "/"),
           "scale": "every slider is 0..100 on the bay; native = the doc's own scale (shown beside it)",
           "private": PRIVATE_NOTE, "modules": modules, "suggested_cables": SUGGESTED, "groups": GROUPS}
    return cat, errors, drift


def main(argv):
    cat, errors, drift = build()
    if errors:
        print(json.dumps({"ok": False, "errors": errors}, indent=1) if "--json" in argv else "\n".join(errors))
        return 1
    if "--dry-run" not in argv:
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
            json.dump(cat, f, ensure_ascii=False, indent=1)
            f.write("\n")
    n_dials = sum(len(m["dials"]) for m in cat["modules"])
    doc_picks = sum(1 for m in cat["modules"] for d in m["dials"] if d.get("vocab_src", "").startswith("doc"))
    res = {"ok": True, "out": os.path.relpath(OUT, ROOT).replace("\\", "/"), "modules": len(cat["modules"]),
           "dials": n_dials, "picks_from_doc": doc_picks, "drift": drift, "written": "--dry-run" not in argv}
    if "--json" in argv:
        print(json.dumps(res, indent=1))
    else:
        print("catalog: %(modules)d modules, %(dials)d dials, %(picks_from_doc)d pick lists read from the doc -> %(out)s" % res)
        for d in drift:
            print("  drift: " + d)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
