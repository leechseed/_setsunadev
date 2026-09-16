"""BOLO status page — build.

Usage:  python _tools/bolostatus/build.py 45

Inputs : _tools/bolostatus/boards/<n>.json   one board per BOLO (the five-paragraph order as data)
         _tools/sitrep/glossary.json          the shared term register (every [[key]] must exist here)
         _tools/bolostatus/template.html      the page (artifact fragment)
Outputs: _tools/bolostatus/out/BOLO-<n>.html  full document, tracked
         <scratch>/BOLO-<n>.fragment.html     the fragment the Artifact tool publishes (path printed)
"""
import io, json, os, re, sys, tempfile
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
GLOSS = os.path.join(ROOT, "_tools", "sitrep", "glossary.json")

def load(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("usage: build.py <bolo number>"); sys.exit(2)
    n = sys.argv[1]
    board = json.loads(load(os.path.join(HERE, "boards", n + ".json")))
    glossary = json.loads(load(GLOSS))

    text = json.dumps(board, ensure_ascii=False)
    missing = sorted({k for k in re.findall(r"\[\[([^\]|]+)", text) if k not in glossary})
    if missing:
        print("MISSING GLOSSARY KEYS:", ", ".join(missing)); sys.exit(1)

    data = json.dumps({"board": board, "glossary": glossary}, ensure_ascii=False).replace("</script", "<\\/script")
    tpl = load(os.path.join(HERE, "template.html"))
    assert tpl.count("/*__DATA__*/null") == 1
    frag = tpl.replace("/*__DATA__*/null", data).replace("<title>BOLO</title>", f"<title>DOPE SHEET {n}</title>")

    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    out = os.path.join(HERE, "out", f"BOLO-{n}.html")
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n</head>\n<body>\n' + frag + '\n</body>\n</html>\n')

    scratch = os.environ.get("SITREP_SCRATCH") or tempfile.gettempdir()
    fp = os.path.join(scratch, f"BOLO-{n}.fragment.html")
    with io.open(fp, "w", encoding="utf-8", newline="\n") as f:
        f.write(frag)

    print(f"BOLO {n}: {len(board['paragraphs'])} paragraphs · {len(glossary)} terms")
    print("wrote", out, f"({os.path.getsize(out)//1024} KB)")
    print("fragment", fp)

if __name__ == "__main__":
    main()
