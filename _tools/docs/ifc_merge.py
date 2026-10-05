"""THE INTERFACE FAN-IN (BOLO 102 stage 2 · RANGE, a script).

Usage:  python _tools/docs/ifc_merge.py

Reads every _tools/docs/work/ifc/*.json the extractors wrote, validates the shape, merges them into
_tools/docs/out/ifc_candidates.json (sorted by pair), and prints the digest the CDR designs from:
  - per system pair: DATA · CONTROL · MENTION · proposed counts, both directions
  - one-sided pairs: A says it writes to B but B never says it reads from A (the SE mismatch list)
  - pairs the N² scan found (out/interfaces.json) that no extractor logged at all
  - every proposed entry, in full (the gap list)
"""
import glob
import io
import json
import os
import sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, "work", "ifc")
OUT = os.path.join(HERE, "out")
NAMES = {"00": "Base", "01": "Narrative", "02": "Character", "03": "Setting", "04": "Plot",
         "05": "Worldbuilding", "06": "Theme", "07": "Style", "08": "Tracking", "09": "Operations"}
FIELDS = ["from_sys", "to_sys", "from_doc", "to_doc", "kind", "direction", "payload", "trigger", "where",
          "status", "evidence", "note"]
KINDS = {"DATA", "CONTROL", "MENTION"}
DIRS = {"writes", "reads", "gates", "gated_by"}
STATUS = {"built", "parked", "proposed"}


def main():
    entries, bad = [], []
    for f in sorted(glob.glob(os.path.join(WORK, "*.json"))):
        try:
            data = json.load(io.open(f, encoding="utf-8"))
        except Exception as e:
            bad.append(f"{os.path.basename(f)}: unreadable ({e})")
            continue
        for i, e in enumerate(data):
            miss = [k for k in FIELDS if k not in e]
            if miss:
                bad.append(f"{os.path.basename(f)}[{i}]: missing {miss}")
                continue
            if e["kind"] not in KINDS or e["direction"] not in DIRS or e["status"] not in STATUS \
                    or e["from_sys"] not in NAMES or e["to_sys"] not in NAMES:
                bad.append(f"{os.path.basename(f)}[{i}]: bad enum ({e['kind']}/{e['direction']}/{e['status']}/{e['from_sys']}→{e['to_sys']})")
                continue
            if e["kind"] != "MENTION" and len(e["payload"].strip()) < 8:
                bad.append(f"{os.path.basename(f)}[{i}]: {e['kind']} with no payload")
            e["slice"] = os.path.basename(f)[:-5]
            entries.append(e)
    entries.sort(key=lambda e: (e["from_sys"], e["to_sys"], e["kind"], e["from_doc"]))
    os.makedirs(OUT, exist_ok=True)
    io.open(os.path.join(OUT, "ifc_candidates.json"), "w", encoding="utf-8").write(json.dumps(entries, ensure_ascii=False, indent=1))

    pair = defaultdict(Counter)
    for e in entries:
        key = tuple(sorted((e["from_sys"], e["to_sys"])))
        pair[key][e["kind"] if e["status"] != "proposed" else "proposed"] += 1
    print(f"IFC fan-in · {len(entries)} entries from {len(set(e['slice'] for e in entries))} slices · {len(pair)} pairs")
    for b in bad:
        print("  BAD", b)
    print("\nPAIR          DATA CTRL MENT PROP")
    for (a, b), c in sorted(pair.items()):
        print(f"{a} {NAMES[a][:5]:5}↔{b} {NAMES[b][:5]:5} {c['DATA']:4} {c['CONTROL']:4} {c['MENTION']:4} {c['proposed']:4}")

    # one-sided: writes with no matching read on the other side (same pair, opposite direction)
    wired = [e for e in entries if e["kind"] == "DATA" and e["status"] != "proposed"]
    reads = {(e["to_sys"], e["from_sys"]) for e in wired if e["direction"] == "reads"}
    writes = {(e["from_sys"], e["to_sys"]) for e in wired if e["direction"] == "writes"}
    print("\nONE-SIDED (A writes to B, B logs no read from A):",
          ", ".join(f"{a}→{b}" for a, b in sorted(writes - reads)) or "none")
    print("ONE-SIDED (B reads from A, A logs no write to B):",
          ", ".join(f"{a}→{b}" for a, b in sorted(reads - writes)) or "none")

    scan = os.path.join(OUT, "interfaces.json")
    if os.path.exists(scan):
        seen = {(e["from_sys"], e["to_sys"]) for e in entries} | {(e["to_sys"], e["from_sys"]) for e in entries}
        scanned = {(x["from_sys"], x["to_sys"]) for x in json.load(io.open(scan, encoding="utf-8"))}
        print("N² pairs no extractor logged:", ", ".join(f"{a}→{b}" for a, b in sorted(scanned - seen)) or "none")

    print("\nPROPOSED (the gap list):")
    for e in entries:
        if e["status"] == "proposed":
            print(f"  {e['from_sys']}→{e['to_sys']} {e['direction']:8} {e['from_doc']} :: {e['payload'][:110]}")


if __name__ == "__main__":
    main()
