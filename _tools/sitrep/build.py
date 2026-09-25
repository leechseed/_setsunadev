"""SITREP front page — build.

Usage:  python _tools/sitrep/build.py [YYYY-MM-DD]
        (defaults to the newest board in _tools/sitrep/boards/)

Inputs : _tools/sitrep/boards/<date>.json   one board per sit rep (the data)
         _tools/sitrep/glossary.json        the term register (grows; every [[key]] must exist here)
         _tools/sitrep/template.html        the page (artifact fragment: <title> + <style> + markup + <script>)
Outputs: SITREP.html                        full document at the repo root, sibling of MCDP-CODEX.html
         <scratch>/SITREP.fragment.html     the fragment the Artifact tool publishes (path printed)

The build is deterministic: the JSON is injected at /*__DATA__*/null and nothing else changes.
"""
import glob, io, json, os, re, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
BOARDS = os.path.join(HERE, "boards")

def load(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()

def main():
    date = sys.argv[1] if len(sys.argv) > 1 else sorted(f[:-5] for f in os.listdir(BOARDS) if f.endswith(".json"))[-1]
    board = json.loads(load(os.path.join(BOARDS, date + ".json")))
    glossary = json.loads(load(os.path.join(HERE, "glossary.json")))

    # every [[key]] in the board must resolve
    text = json.dumps(board, ensure_ascii=False)
    missing = sorted({k for k in re.findall(r"\[\[([^\]|]+)", text) if k not in glossary})
    if missing:
        print("MISSING GLOSSARY KEYS:", ", ".join(missing))
        sys.exit(1)

    # BREVITY (BOLO 37, ruled 9/23): the selection panel's slots. Front five of each bench only; the back five stay on disk.
    bp = os.path.join(ROOT, "_tools", "soi", "benches.json")
    brevity = {"slots": []}
    if os.path.exists(bp):
        for s in json.loads(load(bp))["slots"]:
            brevity["slots"].append({"id": s["id"], "thing": s["thing"], "since": s.get("since", ""), "front": s["bench"][:5],
                                     "sealed": s["sealed"][:3], "status": s.get("status", "open"), "ruling": s.get("ruling")})
    # QUOTES (9/24, Chief): with no open slot, the panel carries a quote from the quote book, rotating by board.
    qp = os.path.join(ROOT, "QUOTES.md")
    if os.path.exists(qp):
        rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in load(qp).splitlines()
                if re.match(r"^\|\s*\d+\s*\|", l)]
        if rows:
            r = rows[len(glob.glob(os.path.join(HERE, "boards", "*.json"))) % len(rows)]
            brevity["quote"] = {"n": r[0], "words": r[1], "source": r[2], "met": r[3], "for": r[4]}
    data = json.dumps({"board": board, "glossary": glossary, "brevity": brevity}, ensure_ascii=False)
    data = data.replace("</script", "<\\/script")
    tpl = load(os.path.join(HERE, "template.html"))
    assert tpl.count("/*__DATA__*/null") == 1
    frag = tpl.replace("/*__DATA__*/null", data)

    full = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1">\n</head>\n<body>\n'
            + frag + '\n</body>\n</html>\n')
    out = os.path.join(ROOT, "SITREP.html")
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(full)

    scratch = os.environ.get("SITREP_SCRATCH") or tempfile.gettempdir()
    fp = os.path.join(scratch, "SITREP.fragment.html")
    with io.open(fp, "w", encoding="utf-8", newline="\n") as f:
        f.write(frag)

    print(f"board {date}: {len(board['blocks'])} blocks · {len(glossary)} terms")
    print("wrote", out, f"({os.path.getsize(out)//1024} KB)")
    print("fragment", fp)

if __name__ == "__main__":
    main()
