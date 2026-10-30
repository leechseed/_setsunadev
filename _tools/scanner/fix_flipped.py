"""fix_flipped.py — 10/30 (BOLO 169): find script pages whose OCR text came out upside down and re-OCR them rotated.
A page is suspect when few of its words are common English words. Each suspect page is rendered, OCR'd as-is and rotated
180 degrees, and the orientation with the higher stopword ratio wins. Writes <txt>.fixed.txt and a report; never touches the original.
Usage (Python 3.11):  python -X utf8 fix_flipped.py <script.txt> <script.pdf> [--score-only]
"""
import os
import re
import subprocess
import sys
import tempfile

from PIL import Image

STOP = set("the and to of a in is you i it that was for on are with as at be this have from or one had by but not what all were we when your can said there use an each which she do how their if will up other about out many then them these so some her would make like him into time has look two more go see no way could my than first been who its now people did my over down only".split())
TESS = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def score(text):
    toks = re.findall(r"[A-Za-z']+", text)
    if len(toks) < 15:
        return None
    return sum(1 for t in toks if t.lower() in STOP) / len(toks)


def ocr(png):
    r = subprocess.run([TESS, png, "-", "-l", "eng", "--psm", "6"], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.stdout


def main():
    txt, pdf = sys.argv[1], sys.argv[2]
    pages = open(txt, encoding="utf-8", errors="replace").read().split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    sc = [score(p) for p in pages]
    good = sorted(s for s in sc if s is not None)
    med = good[len(good) // 2]
    thr = min(0.10, med * 0.4)
    sus = [i for i, s in enumerate(sc) if s is not None and s < thr]
    sus += [i for i, s in enumerate(sc) if s is None and len(pages[i].strip()) < 40 and False]
    print(f"{len(pages)} pages · median stopword ratio {med:.2f} · threshold {thr:.2f} · {len(sus)} suspect: {[i + 1 for i in sus]}")
    if "--score-only" in sys.argv:
        return
    fixed = list(pages)
    rows = []
    with tempfile.TemporaryDirectory() as tmp:
        for i in sus:
            base = os.path.join(tmp, f"p{i + 1}")
            subprocess.run(["pdftoppm", "-r", "200", "-f", str(i + 1), "-l", str(i + 1), "-png", "-singlefile", pdf, base], check=True)
            png = base + ".png"
            best = (sc[i] or 0, pages[i], 0)
            for rot in (180, 90, 270):
                out = base + f"_{rot}.png"
                Image.open(png).rotate(rot, expand=True).save(out)
                t = ocr(out)
                s = score(t)
                if s is not None and s > best[0]:
                    best = (s, t, rot)
            fixed[i] = best[1]
            rows.append((i + 1, sc[i], best[0], best[2]))
            print(f"p.{i + 1}: {sc[i]} -> {best[0]:.2f} (rotate {best[2]})", flush=True)
    open(txt[:-4] + ".fixed.txt", "w", encoding="utf-8").write("\f".join(fixed) + "\f")
    still = [r[0] for r in rows if r[2] < thr]
    print(f"fixed {sum(1 for r in rows if r[3])} pages by rotating; still low after rotation: {still}")


main()
