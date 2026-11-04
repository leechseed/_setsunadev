"""sources.py: the Engine Room's shared reader (BOLO 180, phase 1). Reads the Venture Engine live from the repo; copies nothing.

The gate meter (BOLO 100, systems first): for each of the ten SSOT systems, count
  open     a formal OPEN marker: a page line '> **OPEN:** ...' under _DOCS/<system>/, or '**OPEN:**' in an _SSOT doc
  parked   a line carrying the parked marker U+23F8 in an _SSOT doc
  unmarked a loose upper-case OPEN word in an _SSOT doc (shown apart; ruled 11/4, call 2: it does not count toward the gate)
  waived   a row whose id is in waivers.json (Chief's per-row waiver; phase 1 only reads it)
The scrub drops, from parked and unmarked: template files · version-history sections · inline-code markers (`...`) ·
mermaid fences · legend lines that define the marker. YAML and other code fences stay counted: a parked field there is real.
The CCC imports this module; this module never imports the CCC.
"""
import hashlib
import io
import json
import os
import re
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CANON = os.path.join(ROOT, "ShroomsQ", "_CANON")
WAIVERS = os.path.join(HERE, "waivers.json")

PARK = "⏸"
NAMES = {
    "00": "Epistemology", "01": "Narrative", "02": "Character", "03": "Setting", "04": "Plot",
    "05": "Worldbuilding", "06": "Theme", "07": "Style", "08": "Tracking", "09": "Operations",
}
RE_PAGE_OPEN = re.compile(r"^\s*>\s*\*\*OPEN:\*\*")
RE_SSOT_OPEN = re.compile(r"\*\*OPEN:\*\*")
RE_LOOSE_OPEN = re.compile(r"\bOPEN\b")
RE_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
RE_HISTORY = re.compile(r"history|changelog|change log|version log", re.I)
RE_HISTORY_ROW = re.compile(r"^\s*(\|\s*\d+\.\d+\.\d+\s*\||[-*]\s+\*\*\d+\.\d+\.\d+)")
RE_INLINE_MARK = re.compile(r"`\s*" + PARK + r"\s*`")   # the bare symbol in backticks names the marker; `⏸ row 9 fill pass` is a real parked item
RE_LEGEND = re.compile(PARK + r"\s+(means|marks)\b|\b(the|a|this|parked)\s+marker\b|\blegend\b", re.I)   # a line that defines the marker


def rel(p):
    return os.path.relpath(p, ROOT).replace("\\", "/")


def row_id(path, text):
    return rel(path) + "#" + hashlib.sha1(text.strip().encode("utf-8")).hexdigest()[:10]


def load_waivers(path=WAIVERS):
    try:
        data = json.load(io.open(path, encoding="utf-8"))
        return {w["row_id"]: w for w in data if isinstance(w, dict) and w.get("row_id")}
    except (OSError, ValueError):
        return {}


def systems(canon=CANON):
    """[(id, folder)] for the ten system folders under _SSOT, in reading order."""
    ssot = os.path.join(canon, "_SSOT")
    out = []
    for name in sorted(os.listdir(ssot)):
        m = re.match(r"^(\d\d)_", name)
        if m and os.path.isdir(os.path.join(ssot, name)):
            out.append((m.group(1), name))
    return out


def md_files(folder):
    for dp, dn, fn in os.walk(folder):
        dn[:] = [d for d in dn if not d.startswith((".", "_history"))]
        for f in sorted(fn):
            if f.endswith(".md"):
                yield os.path.join(dp, f)


def scan_lines(path):
    """Yield (line_no, text, context) where context is 'history', 'mermaid', 'fence' or ''."""
    try:
        lines = io.open(path, encoding="utf-8", errors="replace").read().split("\n")
    except OSError:
        return
    hist_level = 0
    fence = None
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith("```"):
            if fence is None:
                fence = "mermaid" if s[3:].strip().lower().startswith("mermaid") else "fence"
            else:
                fence = None
            continue
        if fence is None:
            h = RE_HEADING.match(line)
            if h:
                lvl = len(h.group(1))
                if hist_level and lvl <= hist_level:
                    hist_level = 0
                if RE_HISTORY.search(h.group(2)):
                    hist_level = lvl
                continue
        ctx = fence or ("history" if hist_level else "")
        yield i, line, ctx


def classify_ssot(path, line, ctx):
    """Return (kind, dropped_reason) for one _SSOT line; kind is 'parked', 'open', 'unmarked' or None."""
    is_template = "template" in os.path.basename(path).lower()
    if RE_SSOT_OPEN.search(line):
        kind = "open"
    elif PARK in line:
        kind = "parked"
    elif RE_LOOSE_OPEN.search(line):
        kind = "unmarked"
    else:
        return None, None
    if is_template:
        return kind, "template file"
    if ctx == "history" or RE_HISTORY_ROW.match(line):
        return kind, "version history"
    if ctx == "mermaid":
        return kind, "mermaid diagram"
    if kind == "parked":
        if RE_INLINE_MARK.search(line) and PARK not in RE_INLINE_MARK.sub("", line):
            return kind, "inline code (names the marker)"
        if RE_LEGEND.search(line):
            return kind, "legend line"
    return kind, None


def gate(canon=CANON, waivers=None, with_rows=True):
    """The gate meter: per system counts plus every counted and dropped row."""
    waivers = load_waivers() if waivers is None else waivers
    root_for_rel = ROOT
    out = []
    tot = {"open": 0, "parked": 0, "unmarked": 0, "waived": 0, "dropped": 0, "raw_open": 0, "raw_parked": 0}
    for sid, folder in systems(canon):
        c = {"open": 0, "parked": 0, "unmarked": 0, "waived": 0, "dropped": 0, "raw_open": 0, "raw_parked": 0}
        rows = []
        ssot_dir = os.path.join(canon, "_SSOT", folder)
        for p in md_files(ssot_dir):
            for ln, line, ctx in scan_lines(p):
                kind, drop = classify_ssot(p, line, ctx)
                if not kind:
                    continue
                if kind in ("open", "parked"):
                    c["raw_" + kind] += 1
                rid = row_id(p, line)
                if drop:
                    c["dropped"] += 1
                elif rid in waivers:
                    c["waived"] += 1
                else:
                    c[kind] += 1
                rows.append({"kind": kind, "file": rel(p), "line": ln, "text": line.strip()[:200], "row_id": rid,
                             "dropped": drop, "waived": rid in waivers})
        docs_dir = os.path.join(canon, "_DOCS", folder)
        if os.path.isdir(docs_dir):
            for p in md_files(docs_dir):
                for ln, line, ctx in scan_lines(p):
                    if ctx in ("history", "mermaid") or not RE_PAGE_OPEN.match(line):
                        continue
                    c["raw_open"] += 1
                    rid = row_id(p, line)
                    if rid in waivers:
                        c["waived"] += 1
                    else:
                        c["open"] += 1
                    rows.append({"kind": "open", "file": rel(p), "line": ln, "text": line.strip()[:200], "row_id": rid,
                                 "dropped": None, "waived": rid in waivers})
        for k in tot:
            tot[k] += c[k]
        item = {"id": sid, "name": NAMES.get(sid, folder), "folder": folder, **c, "gate": c["open"] + c["parked"]}
        if with_rows:
            item["rows"] = rows
        out.append(item)
    tot["gate"] = tot["open"] + tot["parked"]
    return {"counted_at": time.strftime("%Y-%m-%dT%H:%M:%S"), "rule": "gate = open + parked (scrubbed, waivers out); "
            "unmarked is shown apart and does not count (ruled 11/4)", "totals": tot, "systems": out,
            "plotting_unlocked": tot["gate"] == 0}
