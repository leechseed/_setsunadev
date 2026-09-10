"""SOI — the house tongue's book. Build.

Usage:  python _tools/soi/build.py

Inputs : _tools/sitrep/glossary.json   the shared term register (every ruled word lands here the same turn)
         _tools/soi/soi.json           edition · sections · authentication · changes
         SOP.md §8                     the dictation codebook table, parsed live so the page never drifts from the SOP
         _tools/soi/template.html
Outputs: SOI.html at the repo root · <scratch>/SOI.fragment.html for the Artifact tool
"""
import io, json, os, re, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

def load(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()

def codebook():
    sop = load(os.path.join(ROOT, "SOP.md"))
    sec = sop.split("## 8 ·", 1)[1]
    rows = []
    for line in sec.splitlines():
        if not line.startswith("|"): continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0].lower() in ("heard", "---") or set(cells[0]) <= set("-: "): continue
        rows.append({"heard": cells[0], "read": cells[1]})
    return rows

def main():
    glossary = json.loads(load(os.path.join(ROOT, "_tools", "sitrep", "glossary.json")))
    soi = json.loads(load(os.path.join(HERE, "soi.json")))
    soi["codebook"] = codebook()
    # every [[key]] inside definitions and changes must resolve
    text = json.dumps(glossary, ensure_ascii=False) + json.dumps(soi, ensure_ascii=False)
    missing = sorted({k for k in re.findall(r"\[\[([^\]|]+)", text) if k not in glossary})
    if missing:
        print("MISSING GLOSSARY KEYS:", ", ".join(missing)); sys.exit(1)
    data = json.dumps({"soi": soi, "glossary": glossary}, ensure_ascii=False).replace("</script", "<\\/script")
    tpl = load(os.path.join(HERE, "template.html"))
    assert tpl.count("/*__DATA__*/null") == 1
    frag = tpl.replace("/*__DATA__*/null", data)
    out = os.path.join(ROOT, "SOI.html")
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n</head>\n<body>\n' + frag + '\n</body>\n</html>\n')
    scratch = os.environ.get("SITREP_SCRATCH") or tempfile.gettempdir()
    fp = os.path.join(scratch, "SOI.fragment.html")
    with io.open(fp, "w", encoding="utf-8", newline="\n") as f:
        f.write(frag)
    print(f"SOI edition {soi['edition']}: {len(glossary)} terms · {sum(1 for g in glossary.values() if g['k']=='proword')} prowords · {len(soi['codebook'])} codebook rows · {len(soi['changes'])} changes")
    print("wrote", out, f"({os.path.getsize(out)//1024} KB)")
    print("fragment", fp)

if __name__ == "__main__":
    main()
