"""RANGE · the core-docs check (BOLO 102 stage 1, "core first").

Usage:  python _tools/docs/docs_check.py

Reads _tools/docs/out/components.json (run components.py first) and the written pages under
ShroomsQ/_CANON/_DOCS/<system>/<stem>/. For every core doc it checks:
  - the four pages exist (1-concept · 2-reference · 3-how-to · 4-tutorial), unless the
    reference page says state: retired, or the doc has zero components (reference only)
  - front matter carries title · type · for · does · owner · state · reviewed · source
  - the thin strip (Who it's for · What it does · Type) is the first body line
  - the reference page has an H2 for every component and an H3 for every part (exact names)
Advisory: sentences over 20 words (DOC-SOP 3.2), OPEN lines (gaps the writers found).
"""
import io
import json
import os
import re
import sys

import yaml

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DOCS = os.path.join(ROOT, "ShroomsQ", "_CANON", "_DOCS")
INV = os.path.join(HERE, "out", "components.json")

PAGES = ["1-concept.md", "2-reference.md", "3-how-to.md", "4-tutorial.md"]
FIELDS = ["title", "type", "for", "does", "owner", "state", "reviewed", "source"]


def stem(fname):
    return re.sub(r"^[^\w]+", "", fname)[:-3].strip()


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[*_`]", "", s)).strip().lower()


def split_front(text):
    m = re.match(r"\A﻿?---\n(.*?)\n---\s*\n(.*)\Z", text, re.S)
    if not m:
        return None, text
    try:
        return yaml.safe_load(m.group(1)) or {}, m.group(2)
    except yaml.YAMLError:
        return None, m.group(2)


def long_sentences(body):
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    n = 0
    for line in body.splitlines():
        if line.startswith(("#", "|", ">")) or not line.strip():
            continue
        line = re.sub(r"\"[^\"]*\"|“[^”]*”", "Q", line)
        for s in re.split(r"(?<=[.!?])\s+|\s·\s", line):
            if len(re.findall(r"[\w'’-]+", s)) > 20:
                n += 1
    return n


def main():
    inv = json.load(io.open(INV, encoding="utf-8"))
    blocking, docs_ok, pages, longs, opens = [], 0, 0, 0, 0
    for sysdir, docs in inv.items():
        for fname, comps in docs.items():
            folder = os.path.join(DOCS, sysdir, stem(fname))
            tag = f"{sysdir}/{stem(fname)}"
            if not os.path.isdir(folder):
                blocking.append(f"{tag}: no folder")
                continue
            ref = os.path.join(folder, "2-reference.md")
            if not os.path.exists(ref):
                blocking.append(f"{tag}: no 2-reference.md")
                continue
            rfm, _ = split_front(io.open(ref, encoding="utf-8").read())
            retired = bool(rfm) and str(rfm.get("state", "")).lower() == "retired"
            need = ["2-reference.md"] if (retired or not comps) else PAGES
            bad = False
            for p in need:
                path = os.path.join(folder, p)
                if not os.path.exists(path):
                    blocking.append(f"{tag}: missing {p}")
                    bad = True
                    continue
                pages += 1
                text = io.open(path, encoding="utf-8").read()
                fm, body = split_front(text)
                if fm is None:
                    blocking.append(f"{tag}/{p}: front matter missing or broken")
                    bad = True
                    continue
                miss = [f for f in FIELDS if not fm.get(f)]
                if miss:
                    blocking.append(f"{tag}/{p}: front matter lacks {', '.join(miss)}")
                    bad = True
                first = next((l for l in body.splitlines() if l.strip()), "")
                if "Who it's for" not in first or "Type:" not in first:
                    blocking.append(f"{tag}/{p}: thin strip is not the first body line")
                    bad = True
                longs += long_sentences(body)
                opens += len(re.findall(r"\*\*OPEN:\*\*", body))
                if p == "2-reference.md" and not retired:
                    h2 = {norm(h) for h in re.findall(r"^##\s+(.+?)\s*$", body, re.M)}
                    h3 = {norm(h) for h in re.findall(r"^###\s+(.+?)\s*$", body, re.M)}
                    for c in comps:
                        if norm(c["name"]) not in h2:
                            blocking.append(f"{tag}: reference lacks component '{c['name']}'")
                            bad = True
                        for part in c["parts"]:
                            if norm(part) not in h3:
                                blocking.append(f"{tag}: reference lacks part '{part}'")
                                bad = True
            docs_ok += not bad
    total = sum(len(v) for v in inv.values())
    print(f"RANGE core docs · {docs_ok}/{total} docs clean · {pages} pages · "
          f"{opens} OPEN gaps · {longs} sentences over 20 words (advisory)")
    for b in blocking:
        print("  -", b)
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
