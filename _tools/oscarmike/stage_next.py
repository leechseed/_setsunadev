# -*- coding: utf-8 -*-
"""Oscar Mike H4 (BOLO 86): stage the next launch. Zero tokens.

Writes _tools/launch/next.json: the leverage line (newest board, Block VI), every DOPE SHEET
touched today (boards/N.json modified today), and the newest note's "Open at close" bullets.
launch.py reads it and FRAGOs each named sheet before the boards open.

Usage:  python _tools/oscarmike/stage_next.py
"""
import io, os, re, json, sys, glob, datetime
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
today = datetime.date.today()


def key(f):   # 2026-10-12.session.md < 2026-10-12-2.session.md < ...-3
    m = re.match(r"(\d{4}-\d{2}-\d{2})(?:-(\d+))?\.session\.md$", os.path.basename(f))
    return (m.group(1), int(m.group(2) or 1)) if m else ("", 0)


def main():
    out = {"staged": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "leverage": {}, "sheets": [], "open_at_close": [], "note": ""}
    boards = sorted(glob.glob(os.path.join(ROOT, "_tools", "sitrep", "boards", "*.json")))
    if boards:
        b = json.load(io.open(boards[-1], encoding="utf-8"))
        vi = next((x for x in b["blocks"] if x["id"] == "VI"), {})
        out["leverage"] = {"line": vi.get("line", ""), "why": vi.get("why", ""), "board": os.path.basename(boards[-1])}
    for f in glob.glob(os.path.join(ROOT, "_tools", "bolostatus", "boards", "*.json")):
        n = os.path.basename(f)[:-5]
        if n.isdigit() and datetime.date.fromtimestamp(os.path.getmtime(f)) == today:
            out["sheets"].append(int(n))
    out["sheets"].sort()
    notes = sorted(glob.glob(os.path.join(ROOT, "_CACHE", "*.session.md")), key=key)
    if notes:
        out["note"] = os.path.basename(notes[-1])
        txt = io.open(notes[-1], encoding="utf-8").read()
        m = re.search(r"\*\*Open at close:?\*\*:?\s*\n((?:[ \t]+[-*].*\n?|\s*\n)+)", txt)
        if m:
            out["open_at_close"] = [re.sub(r"^[-*]\s*", "", l.strip()) for l in m.group(1).splitlines() if l.strip()]
        else:   # inline form: "**Open at close:** a · b · c"
            m = re.search(r"\*\*Open at close:?\*\*:?[ \t]*(\S.*)", txt)
            if m:
                out["open_at_close"] = [x.strip() for x in m.group(1).split(" · ") if x.strip()]
    dst = os.path.join(ROOT, "_tools", "launch", "next.json")
    io.open(dst, "w", encoding="utf-8", newline="\n").write(json.dumps(out, ensure_ascii=False, indent=1))
    print("staged -> _tools/launch/next.json | sheets %s | %d open item(s) | leverage: %s"
          % (out["sheets"], len(out["open_at_close"]), out["leverage"].get("line", "")[:80]))


if __name__ == "__main__":
    main()
