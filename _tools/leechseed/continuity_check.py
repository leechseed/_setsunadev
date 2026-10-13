#!/usr/bin/env python3
"""LEECHSEED continuity keeper (BOLO 140 -> BOLO 100). A script, no model judges prose.

Usage:
    python _tools/leechseed/continuity_check.py <draft.md> [--ssot ShroomsQ/_CANON/_SSOT] [--json] [--rebuild]

Builds _tools/leechseed/registry.json from the SSOT (fabula, setting, character slice),
the tracking file and _CANON_NODES/*.md (rebuilt with --rebuild or when missing; nothing
from _PRIVATE/ is ever read). Then checks the draft for:
  retired    Outsiders, Ariel, Barnes, Red Stick Creek, Quinton, Inner Spiral -> their rulings
  era/year   a year named with an era that does not hold it; a character acting before birth
  name       capitalised two-word names not in the registry (advisory)
  place      "in/at/from the Xxx Yyy" places not in the registry (advisory)
Output: one line per finding: line | kind | text | rule. Exit 1 on any conflict
(retired, era, birth); unknown names and places are advisory (exit 0).
A retired word on a line that says lineage/legacy/formerly/etc. is a note, not a conflict.
"""
import argparse, json, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
REG = HERE / "registry.json"
NODES = ROOT / "_CANON_NODES"
TRACK = ROOT / "ShroomsQ/_CANON/_TRACKING/oxo.yaml"

RETIRED = [
    (r"\bOutsiders\b", "series is 'The Outliers', never 'The Out' + 'siders' (standing ruling)"),
    (r"\bAriel\b", "Ariel is Tori's earlier name: lineage, not canon (ruled 9/29); use Tori / Victoria Midnight"),
    (r"\bBarnes\b", "no character named Barnes exists (standing ruling)"),
    (r"\bRed Stick Creek\b", "renamed Skeeter Creek (era 1; legacy vocab, 2022-23 lineage)"),
    (r"\bQuinton\b", "'Quinton' means Quinn Bishop (standing ruling)"),
    (r"\bInner Spiral\b", "school is Delta Coast Ultra School (DCUS), ruled 8/24; Inner Spiral is legacy vocab"),
]
LINEAGE = re.compile(r"lineage|legacy|formerly|earlier name|retired|superseded|renamed|history|never|alias|"
                     r"pre-ruling|was |not canon|ruling|ruled|vocab", re.I)
ERAS = {1: "Skeeter Creek", 2: "DCUS", 3: "LAKAD", 4: "ASTRO7EX", 5: "beyond"}
ERA_NAME = {"skeeter creek": 1, "dcus": 2, "lakad": 3, "astro7ex": 4, "beyond": 5}
# anchors stated in the fabula world clock: Moon Severance 2099 in era 1; OXO present 2199, shared by eras 2 and 4
ERA_YEARS_SEED = {2099: [1], 2199: [2, 4]}
STOP = set("""The A An In On At To Of For And But Or If When While After Before Then There This That These Those It
He She They We You I His Her Their Our My Your As By With From Into Over Under Not No Yes So Is Are Was Were Be
Monday Tuesday Wednesday Thursday Friday Saturday Sunday January February March April May June July August
September October November December One Two Three Four Five Six Seven Eight Nine Ten Part Era Movement Scene
Chief Layer Rule Open Note See Status""".split())
NAME_RE = re.compile(r"\b([A-Z][a-z]{2,}(?:\s+[A-Z][a-z]{2,}){1,2})\b")
PLACE_RE = re.compile(r"\b(?:in|at|from|to|into|near|across|through)\s+(?:the\s+)?([A-Z][a-z]{2,}(?:\s+[A-Z][a-z]{2,})+)")
YEAR_RE = re.compile(r"\b(2[0-3]\d\d|1[5-9]\d\d)\b")


def clean(text):
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", " ", text)
    text = re.sub(r"\[\[([^\]|]*)(?:\|[^\]]*)?\]\]", r"\1", text)
    text = re.sub(r"\]\([^)]*\)", "]", text)
    return text.replace("*", "").replace("_", " ") if False else re.sub(r"[*]", "", text)


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    out = {}
    if m:
        for ln in m.group(1).splitlines():
            k, _, v = ln.partition(":")
            if _ and not ln.startswith(" "):
                out[k.strip()] = v.strip()
    return out


def aliases_of(v):
    v = v.strip().strip("[]")
    res = []
    for a in re.findall(r'"([^"]+)"|([^,]+)', v):
        a = (a[0] or a[1]).strip().strip('"')
        a = re.sub(r"\s*\(.*?\)", "", a).strip()
        if a:
            res.append(a)
    return res


def ssot_files(ssot):
    for sub in ("02_CHARACTER_SYSTEMS", "03_SETTING_SYSTEMS", "04_PLOT_SYSTEMS"):
        for p in sorted((ssot / sub).glob("*.md")):
            yield p


def build(ssot):
    reg = {"characters": {}, "places": {}, "factions": {}, "terms": [], "eras": {}, "era_years": {},
           "births": {}, "school": "Delta Coast Ultra School (DCUS)", "series": "The Outliers", "sources": []}
    def add(bucket, name, canon=None):
        reg[bucket].setdefault(name, canon or name)
    # nodes
    for p in sorted(NODES.glob("*.md")):
        if "_PRIVATE" in str(p):
            continue
        txt = p.read_text(encoding="utf-8", errors="replace")
        fm = frontmatter(txt)
        kind = (fm.get("type") or fm.get("kind") or "").lower()
        ent = fm.get("entity") or fm.get("title") or ""
        bucket = "characters" if "character" in kind else "places" if kind in ("place", "school", "setting", "location") \
            else "factions" if kind in ("faction", "nation", "org") else None
        if p.stem in ("delta-coast-ultra-school",):
            bucket = "places"
        if bucket and ent:
            add(bucket, ent)
            for a in aliases_of(fm.get("aliases", "")):
                add(bucket, a, ent)
            reg["sources"].append(f"_CANON_NODES/{p.name}")
        for m in re.finditer(r"(?:born|birth(?:\s+year)?)\D{0,12}(\d{4})", txt[:6000], re.I):
            if ent and bucket == "characters":
                reg["births"].setdefault(ent, int(m.group(1)))
    # tracking subjects
    if TRACK.exists():
        for kind, slug in re.findall(r"subject:\s*(character|place|faction):([a-z_]+)", TRACK.read_text(encoding="utf-8")):
            add({"character": "characters", "place": "places", "faction": "factions"}[kind], slug.replace("_", " ").title())
        reg["sources"].append("ShroomsQ/_CANON/_TRACKING/oxo.yaml")
    # SSOT: actors, terms, birth, era-year
    cnt = Counter()
    for p in ssot_files(ssot):
        t = p.read_text(encoding="utf-8", errors="replace")
        reg["sources"].append(str(p.relative_to(ROOT)).replace("\\", "/") if ROOT in p.parents else str(p))
        for a in re.findall(r'^\s*-\s*actor:\s*"([^"]+)"', t, re.M):
            if re.match(r"^[A-Z][a-z]+(?:\s[A-Z][a-z]+)*$", a) or a.isupper():
                add("characters", a)
        for m in re.finditer(r"(?:^|\n)[^\n]*\bborn\b[^\n]*", t):
            pass
        for m in re.finditer(r"([A-Z][a-z]+)'s (\d{4}) birth|([A-Z][a-z]+)[^.\n]{0,40}\bborn in (\d{4})|\b(\d{4}) birth", t):
            if m.group(1):
                reg["births"].setdefault(m.group(1), int(m.group(2)))
        for line in clean(t).splitlines():
            for ph in NAME_RE.findall(line):
                w = ph.split()
                while w and w[0] in STOP:
                    w = w[1:]
                if len(w) >= 2:
                    cnt[" ".join(w)] += 1
    reg["births"].setdefault("Vivian", 2091)  # fabula: Vivian's 2091 stands alone (2090s births are ancestors)
    reg["terms"] = sorted(n for n, c in cnt.items() if c >= 2)
    # standing names
    for n in ("Tori Midnight", "Victoria Midnight", "Quinn Bishop", "Jebb Midnight", "Riley Moss",
              "Anna Colson Conway", "Vivian", "Myrtle", "Tori", "Victoria", "Quinn"):
        add("characters", n)
    reg["characters"]["Tori"] = reg["characters"]["Victoria"] = "Tori Midnight"
    reg["characters"]["Quinn"] = "Quinn Bishop"
    for n in ("Delta Coast", "Skeeter Creek", "Red Hills", "Deep Meridian", "Narco Republic", "Aldrin Sector",
              "Delta Coast Ultra School", "DCUS"):
        add("places", n)
    reg["eras"] = {str(k): v for k, v in ERAS.items()}
    reg["era_years"] = {str(y): e for y, e in ERA_YEARS_SEED.items()}
    return reg


def load(args):
    if args.rebuild or not REG.exists():
        reg = build(Path(args.ssot))
        REG.write_text(json.dumps(reg, ensure_ascii=False, indent=1), encoding="utf-8")
    return json.loads(REG.read_text(encoding="utf-8"))


def sentences(line):
    return [s for s in re.split(r"(?<=[.;!?])\s+", line) if s]


def check(draft_path, reg):
    raw = Path(draft_path).read_text(encoding="utf-8", errors="replace")
    body_start = 0
    m = re.match(r"---\n.*?\n---\n", raw, re.S)
    if m:
        body_start = raw[:m.end()].count("\n")
    lines = clean(raw).splitlines()
    # clean() strips frontmatter via regex, so re-add offset
    lines = ["" ] * body_start + lines
    known = set(reg["characters"]) | set(reg["places"]) | set(reg["factions"]) | set(reg["terms"])
    known_l = {k.lower() for k in known}
    known_words = set()
    for k in known:
        known_words.update(k.lower().split())
    findings = []
    seen = set()
    def add(n, kind, text, rule, conflict):
        key = (n, kind, text)
        if key not in seen:
            seen.add(key)
            findings.append({"line": n, "kind": kind, "text": text, "rule": rule, "conflict": conflict})
    chars = sorted(reg["characters"], key=len, reverse=True)
    for n, line in enumerate(lines, 1):
        if not line.strip():
            continue
        lin = bool(LINEAGE.search(line))
        for pat, rule in RETIRED:
            for m in re.finditer(pat, line):
                add(n, "retired" if not lin else "retired-note", m.group(0), rule, not lin)
        for s in sentences(line):
            years = [int(y) for y in YEAR_RE.findall(s)]
            eras = set(int(x) for x in re.findall(r"\bera\s+([1-5])\b", s, re.I))
            for nm, num in ERA_NAME.items():
                if re.search(rf"\b{re.escape(nm)}\s+era\b", s, re.I):
                    eras.add(num)
            for y in years:
                held = reg["era_years"].get(str(y))
                if held and eras and not (eras & set(held)):
                    add(n, "era", f"{y} named with era {sorted(eras)}",
                        f"SSOT fabula world clock: {y} sits in era {'/'.join(map(str, held))}", True)
            if years:
                for who, by in reg["births"].items():
                    if re.search(rf"\b{re.escape(who)}\b", s) and not re.search(r"born|birth|ancest|lineage|descend", s, re.I):
                        early = [y for y in years if y < by]
                        if early:
                            add(n, "birth", f"{who} acts in {early[0]}", f"{who} born {by} (SSOT fabula)", True)
        for m in PLACE_RE.finditer(line):
            ph = m.group(1)
            if ph.lower() not in known_l and not any(ph.lower() in k for k in known_l) and ph.split()[0] not in STOP:
                add(n, "place", ph, "place not in registry: add or fix", False)
        for m in NAME_RE.finditer(line):
            w = m.group(1).split()
            while w and w[0] in STOP:
                w = w[1:]
            if len(w) < 2:
                continue
            ph = " ".join(w)
            if ph.lower() in known_l or any(ph.lower() in k or k in ph.lower() for k in known_l if len(k) > 3):
                continue
            if all(x.lower() in known_words for x in w):
                continue
            if any(re.search(pat, ph) for pat, _ in RETIRED):
                continue
            add(n, "name", ph, "unknown name, add or fix", False)
    return findings


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("draft")
    ap.add_argument("--ssot", default=str(ROOT / "ShroomsQ/_CANON/_SSOT"))
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--rebuild", action="store_true")
    a = ap.parse_args()
    if "_PRIVATE" in a.ssot:
        sys.exit("refusing: _PRIVATE is not a source")
    reg = load(a)
    f = check(a.draft, reg)
    conflicts = [x for x in f if x["conflict"]]
    adv = [x for x in f if not x["conflict"]]
    if a.json:
        print(json.dumps({"findings": f, "conflicts": len(conflicts), "advisory": len(adv)}, ensure_ascii=False, indent=1))
    else:
        for x in f:
            print(f"{x['line']} | {x['kind']} | {x['text']} | {x['rule']}")
        print(f"SUMMARY {a.draft}: {len(conflicts)} conflict(s), {len(adv)} advisory "
              f"({sum(1 for x in adv if x['kind']=='name')} unknown names, "
              f"{sum(1 for x in adv if x['kind']=='place')} places, "
              f"{sum(1 for x in adv if x['kind']=='retired-note')} lineage notes)")
    sys.exit(1 if conflicts else 0)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
