#!/usr/bin/env python3
"""Build _tools/worldview/fabula.json from the SSOT / canon files (read-only)
plus the hand-kept fabula_links.json (non-event nodes, links, years, DCUS tree).
Stdlib only. Prints counts per type and the unsourced nodes."""
import json, re, sys, datetime
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
FAB = "ShroomsQ/_CANON/_SSOT/04_PLOT_SYSTEMS/📐 ssot_04_fabula.md"
SET = "ShroomsQ/_CANON/_SSOT/03_SETTING_SYSTEMS/📐 ssot_03_setting_system.md"
OXO = "ShroomsQ/_CANON/_TRACKING/oxo.yaml"

_cache = {}
def lines(rel):
    if rel not in _cache:
        p = ROOT / rel
        _cache[rel] = p.read_text(encoding="utf-8").split("\n") if p.exists() else None
    return _cache[rel]

def first_match(cands):
    """cands: [[file, regex], ...] -> (file, line) or (None, None)."""
    for rel, rx in cands:
        L = lines(rel)
        if not L:
            continue
        for i, l in enumerate(L):
            if re.search(rx, l):
                return rel, i + 1
    return None, None

def humanize(eid):
    s = re.sub(r"^(skeeter_creek|astro7ex|lakad|beyond|backstory|unplaced)_", "", eid)
    s = re.sub(r"^(backstory|narco_republic)_", "", s)
    return s.replace("_", " ").capitalize()

def era_of_event(eid):
    for pre, e in (("skeeter_creek_", "era1"), ("lakad_", "era3"), ("beyond_", "era5"), ("astro7ex_", "era4")):
        if eid.startswith(pre):
            return e
    if re.match(r"m\d", eid):
        return "era2"
    return None

def parse_fabula_events():
    L = lines(FAB)
    out = {}
    for i, l in enumerate(L):
        m = re.match(r"\s*event_id:\s*\"?(\w+)", l)
        if not m:
            continue
        blk = L[i:i + 45]
        ev = {"line": i + 1, "edges": []}
        for b in blk[1:]:
            if re.match(r"\s*event_id:", b) or b.startswith("```"):
                break
            t = re.match(r'\s*transition:\s*"(.*)"', b)
            if t: ev["transition"] = t.group(1)
            t = re.match(r'\s*calendar_year:\s*"?(\d{3,4})', b)
            if t: ev["year"] = int(t.group(1))
            t = re.match(r'\s*movement:\s*"?(\w[\w ,.-]*)', b)
            if t and "movement" not in ev: ev["movement"] = t.group(1).strip()
        k = i
        while k < len(L) and not L[k].startswith("```"):
            k += 1
        ce = "\n".join(L[i:k])
        for t, to in re.findall(r"-\s*type:\s*(\w+)\s*\n\s*to:\s*\"(\w+)\"", ce):
            ev["edges"].append((t, to))
        out[m.group(1)] = ev
    return out

def parse_oxo_world():
    L = lines(OXO)
    out, order = {}, []
    inw = False
    for i, l in enumerate(L):
        if l.startswith("world:"):
            inw = True; continue
        if inw:
            m = re.match(r"\s*- \{id: (\w+), m: (\w+), label: (.*?)(?:, dcus_name:.*)?\}\s*$", l)
            if m:
                lab = m.group(3).strip().strip('"')
                out[m.group(1)] = {"line": i + 1, "m": m.group(2), "label": lab}
                order.append(m.group(1))
    return out, order

def parse_slayers():
    L = lines(SET)
    out = []
    for i, l in enumerate(L):
        m = re.match(r"\|\s*(S\d+) ([A-Z]+)\s*\|\s*(.*?)\s*\|\s*$", l)
        if m and i > 320:
            out.append({"id": m.group(1), "label": m.group(1) + " " + m.group(2).title(),
                        "desc": m.group(3)[:220], "source": SET, "line": i + 1})
    return out

def main():
    hand = json.loads((HERE / "fabula_links.json").read_text(encoding="utf-8"))
    nodes, unsourced = [], []
    byid = {}

    def add(n):
        byid[n["id"]] = n
        nodes.append(n)
        if not n.get("source"):
            unsourced.append(n["id"])

    for h in hand["nodes"]:
        f, ln = first_match(h["find"])
        n = {"id": h["id"], "label": h["label"], "type": h["type"], "era": None, "year": None,
             "desc": h["desc"], "source": f, "line": ln}
        add(n)

    fev = parse_fabula_events()
    oxo, oxo_order = parse_oxo_world()
    amap = {"backstory_skeeter_creek_founding": "skeeter_creek_backstory_skeeter_creek_founding",
            "backstory_red_hills_rename": "skeeter_creek_backstory_red_hills_rename"}
    oxo2 = {amap.get(k, k): v for k, v in oxo.items()}
    ids = list(oxo2.keys()) + [k for k in fev if k not in oxo2]
    for ord_, eid in enumerate(ids):
        fe, ox = fev.get(eid), oxo2.get(eid)
        label = (ox or {}).get("label") or humanize(eid)
        if len(label) > 48 and ":" in label:
            label = label.split(":")[0]
        mv = (fe or {}).get("movement") or (ox or {}).get("m")
        year = (fe or {}).get("year")
        if year is None and re.match(r"m\d", eid):
            year = hand["years"]["m1_to_m6"][0]
        desc = (fe or {}).get("transition") or ((ox or {}).get("label") or "")
        if mv: desc = (desc + " [" + mv + "]").strip()
        src, ln = (FAB, fe["line"]) if fe else (OXO, ox["line"])
        n = {"id": eid, "label": label[:60], "type": "event", "era": era_of_event(eid), "year": year,
             "desc": desc, "source": src, "line": ln, "ord": ord_}
        add(n)

    links = []
    for l in hand["links"]:
        if l["a"] not in byid or l["b"] not in byid:
            print("LINK TO MISSING NODE:", l); continue
        links.append({"a": l["a"], "b": l["b"], "kind": l["kind"], "w": l["w"], "src": l["src"]})
    for eid, fe in fev.items():
        for t, to in fe["edges"]:
            if to in byid:
                links.append({"a": eid, "b": to, "kind": "causal-" + t, "w": t + " (causal edge)",
                              "src": FAB + ":" + str(fe["line"])})
    have = {(l["a"], l["b"]) for l in links if l["kind"] == "placed"}
    for n in nodes:
        if n["type"] == "event" and n["era"] and (n["id"], n["era"]) not in have:
            links.append({"a": n["id"], "b": n["era"], "kind": "placed", "w": "placed on the world clock",
                          "src": "id prefix rule"})
    # era for non-events: year hint, direct era link, then majority of linked events/perspectives
    for l in links:
        if l["kind"] == "placed" and byid[l["a"]]["type"] == "event" and not byid[l["a"]]["era"]:
            byid[l["a"]]["era"] = l["b"]
    for n in nodes:
        if n["type"] == "event" and n["era"] is None:
            n["era"] = None
    nb = {n["id"]: [] for n in nodes}
    for l in links:
        nb[l["a"]].append(l["b"]); nb[l["b"]].append(l["a"])
    for n in nodes:
        if n["type"] == "era":
            n["era"] = n["id"]
        elif n["type"] in ("character", "perspective", "place", "faction"):
            direct = [x for x in nb[n["id"]] if byid[x]["type"] == "era"]
            if direct:
                n["era"] = direct[0]
            else:
                c = Counter(byid[x]["era"] for x in nb[n["id"]] if byid[x]["type"] == "event" and byid[x]["era"])
                if c: n["era"] = c.most_common(1)[0][0]
    for n in nodes:  # characters/places with no era: take the era of their linked place/perspective
        if n["era"] is None and n["type"] in ("character", "faction"):
            c = Counter(byid[x]["era"] for x in nb[n["id"]] if byid[x]["era"])
            if c: n["era"] = c.most_common(1)[0][0]
        if n["year"] is None and n["type"] != "system":
            m = re.search(r"\b(2[0-2]\d\d)(?:-\d\d-\d\d)?\b", n["label"] + " " + n["desc"])
            if m and 2090 <= int(m.group(1)) <= 2299:
                n["year"] = int(m.group(1))

    out = {"built": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "nodes": nodes, "links": links,
           "layers": parse_slayers(), "tree": hand["tree"],
           "sources": sorted({n["source"] for n in nodes if n["source"]})}
    (HERE / "fabula.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    ct = Counter(n["type"] for n in nodes)
    lk = Counter(l["kind"] for l in links)
    print("nodes", len(nodes), dict(ct))
    print("links", len(links), dict(lk))
    print("layers", len(out["layers"]))
    print("dated", sum(1 for n in nodes if n["year"]), "undated events", sum(1 for n in nodes if n["type"] == "event" and not n["year"]))
    print("no era", [n["id"] for n in nodes if not n["era"] and n["type"] != "system"])
    print("UNSOURCED", unsourced)

main()
