# -*- coding: utf-8 -*-
"""LOCI check — the reviewer at the fan-in: every fetched link is covered by the register (script, zero tokens).

Usage:  python _tools/loci/check.py <name> <register.md>
"""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

def main():
    name, reg = sys.argv[1], sys.argv[2]
    man = json.load(io.open(os.path.join(HERE, "work", name, "manifest.json"), encoding="utf-8"))
    text = io.open(reg, encoding="utf-8").read()
    norm = lambda u: re.sub(r"^https?://(www\.)?", "", u).rstrip("/").lower()
    body = norm(text)
    fetched = [m for m in man if m["status"] == 200]
    missing = [m["url"] for m in fetched if norm(m["url"]) not in body and (m["title"] and m["title"].lower()[:40] not in body)]
    dead = [m["url"] for m in man if m["status"] != 200]
    ext = sorted(f for f in os.listdir(os.path.join(HERE, "work", name)) if f.startswith("extract.") and f.endswith(".json"))
    items = 0
    for f in ext:
        try: items += sum(len(x.get("items", [])) for x in json.load(io.open(os.path.join(HERE, "work", name, f), encoding="utf-8")))
        except Exception: print("  note  unreadable " + f)
    print(f"CHECK · {name} · {len(fetched)} fetched · {len(missing)} not covered · {len(dead)} dead links · {items} extracted item(s) in {len(ext)} batch file(s)")
    for u in missing: print("  MISSING " + u)
    for u in dead: print("  dead    " + u)
    sys.exit(1 if missing else 0)

if __name__ == "__main__":
    main()
