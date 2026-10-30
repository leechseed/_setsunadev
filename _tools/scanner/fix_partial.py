"""fix_partial.py — 10/30 (BOLO 169): second repair for script pages whose OCR is partly scrambled (not wholly upside down).
Picks pages whose common-word ratio is low or that the caller names, then re-OCRs each at 300 dpi over several settings
(page-segmentation modes 3, 4, 6, 11; plain, mirrored, rotated 180) and keeps the text with the best ratio.
Writes <txt> in place (the pre-run copy is saved as <txt>.before-partial.txt). Prints one line per page.
Usage (Python 3.11):  python -X utf8 fix_partial.py <script.txt> <script.pdf> [--thr 0.25] [--pages 2,26,91]
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

from PIL import Image, ImageOps

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
STOP = set("the and to of a in is you i it that was for on are with as at be this have from or one had by but not what all were we when your can said there use an each which she do how their if will up other about out many then them these so some her would make like him into time has look two more go see no way could my than first been who its now people did my over down only".split())
TESS = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def score(text):
    toks = re.findall(r"[A-Za-z']+", text)
    if len(toks) < 15:
        return None
    return sum(1 for t in toks if t.lower() in STOP) / len(toks)


def ocr(png, psm):
    r = subprocess.run([TESS, png, "-", "-l", "eng", "--psm", str(psm)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.stdout


def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


def main():
    txt, pdf = sys.argv[1], sys.argv[2]
    thr = float(arg("--thr", "0.25"))
    named = [int(x) for x in arg("--pages", "").split(",") if x]
    raw = open(txt, encoding="utf-8", errors="replace").read()
    pages = raw.split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    sc = [score(p) for p in pages]
    cand = sorted(set(named) | {i + 1 for i, s in enumerate(sc) if s is not None and s < thr})
    print(f"{len(pages)} pages · candidates: {cand}")
    shutil.copy(txt, txt[:-4] + ".before-partial.txt")
    changed = []
    with tempfile.TemporaryDirectory() as tmp:
        for n in cand:
            base = os.path.join(tmp, f"p{n}")
            subprocess.run(["pdftoppm", "-r", "300", "-f", str(n), "-l", str(n), "-png", "-singlefile", pdf, base], check=True)
            im = Image.open(base + ".png").convert("L")
            variants = {"plain": im, "mirror": ImageOps.mirror(im), "rot180": im.rotate(180), "autocontrast": ImageOps.autocontrast(im, cutoff=2)}
            old = sc[n - 1] or 0.0
            best = (old, None, "keep")
            for vname, v in variants.items():
                p = os.path.join(tmp, f"p{n}_{vname}.png")
                v.save(p)
                for psm in (3, 4, 6, 11):
                    t = ocr(p, psm)
                    s = score(t)
                    if s is not None and s > best[0] + 0.02:
                        best = (s, t, f"{vname}/psm{psm}")
            if best[1] is not None and best[0] > old + 0.05:
                pages[n - 1] = best[1]
                changed.append(n)
            print(f"p.{n}: {old:.2f} -> {best[0]:.2f} via {best[2]}", flush=True)
    open(txt, "w", encoding="utf-8").write("\f".join(pages) + "\f")
    print(f"updated {len(changed)} pages: {changed}")


main()
