"""glass_extend.py - 10/30 (BOLO 170): add scan folders to the sorter glass (_PRIVATE/intake/paper/scans/_glass): thumbnails + manifest rows.
Reads each scan's context.md blurb and its best PDF (doc.ordered > doc.fixed > doc.pdf > raw.pdf). Skips ids already in manifest.js.
Usage (Python 3.11):  python -X utf8 glass_extend.py <id> [<id> ...]
"""
import json, os, subprocess, sys
import pikepdf

SCANS = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_PRIVATE", "intake", "paper", "scans")
G = os.path.join(SCANS, "_glass")
MAN = os.path.join(G, "manifest.js")


def blurb(d):
    out = []
    for ln in open(os.path.join(d, "context.md"), encoding="utf-8").read().splitlines()[1:]:
        if ln.startswith(("said:", "tags:", "> raw")):
            if ln.startswith("> raw"):
                break
            continue
        if ln.strip():
            out.append(ln.strip())
    return " ".join(out)[:300]


def main():
    man = open(MAN, encoding="utf-8").read()
    rows = []
    for sid in sys.argv[1:]:
        if sid in man:
            print("skip", sid); continue
        d = os.path.join(SCANS, sid)
        src = next(f for f in ("doc.ordered.pdf", "doc.fixed.pdf", "doc.pdf", "raw.pdf") if os.path.exists(os.path.join(d, f)))
        pdf = os.path.join(d, src)
        n = len(pikepdf.open(pdf).pages)
        shown = n if n <= 60 else 6
        pad = max(2, len(str(n)))
        td = os.path.join(G, "thumbs", sid)
        os.makedirs(td, exist_ok=True)
        subprocess.run(["pdftoppm", "-r", "40", "-f", "1", "-l", str(shown), "-jpeg", "-scale-to-x", "272", "-scale-to-y", "-1", pdf, os.path.join(td, "p")], check=True)
        for f in os.listdir(td):                      # pdftoppm pads to the page count's width; the glass wants pad above
            num = f.split("-")[-1].split(".")[0]
            new = f"p-{int(num):0{pad}d}.jpg"
            if f != new:
                os.replace(os.path.join(td, f), os.path.join(td, new))
        rows.append(f'{{id:"{sid}",pages:{n},shown:{shown},src:"{sid}/{src}",blurb:{json.dumps(blurb(d), ensure_ascii=False)}}},')
        print(sid, n, "pages,", shown, "shown,", src)
    if rows:
        man = man.rstrip()
        assert man.endswith("];")
        man = man[:-2] + "\n".join(rows) + "\n];\n"
        open(MAN, "w", encoding="utf-8").write(man)


main()
