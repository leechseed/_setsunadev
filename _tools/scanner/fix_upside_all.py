"""fix_upside_all.py - 10/30: a scan where many pages came through the feeder rotated 180 degrees (fix_flipped.py only catches
a few). Every page with text is OCR'd upright and rotated; the orientation with the higher common-word ratio wins.
Writes doc.fixed.pdf + doc.fixed.txt beside the originals (raw.pdf and doc.* untouched).
Usage (Python 3.11):  python -X utf8 fix_upside_all.py <scan folder>
"""
import os
import re
import subprocess
import sys
import tempfile

import pikepdf
from PIL import Image

TESS = r"C:\Program Files\Tesseract-OCR"
STOP = set("the and to of a in is you i it that was for on are with as at be this have from or one had by but not what all were we when your can said there an each which she do how their if will up other about out many then them these so some her would make like him into time has look two more write go see no way could people my than first been who its now find".split())


def score(text):
    toks = re.findall(r"[A-Za-z']+", text)
    if len(toks) < 15:
        return None
    return sum(1 for t in toks if t.lower() in STOP) / len(toks)


def ocr(png):
    r = subprocess.run([os.path.join(TESS, "tesseract.exe"), png, "-", "-l", "eng", "--psm", "6"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.stdout


def main():
    d = sys.argv[1]
    raw = os.path.join(d, "raw.pdf")
    n = len(pikepdf.open(raw).pages)
    flip = []
    with tempfile.TemporaryDirectory() as tmp:
        for i in range(1, n + 1):
            base = os.path.join(tmp, "p")
            subprocess.run(["pdftoppm", "-r", "150", "-f", str(i), "-l", str(i), "-png", "-singlefile", raw, base], check=True)
            im = Image.open(base + ".png").convert("L")
            up = score(ocr(base + ".png"))
            im.rotate(180).save(base + "_r.png")
            dn = score(ocr(base + "_r.png"))
            if (dn or 0) > (up or 0) + 0.05:
                flip.append(i)
            print(f"p.{i}: up={up} rot={dn} {'FLIP' if i in flip else ''}", flush=True)
    print(f"flip {len(flip)} of {n}: {flip}", flush=True)
    rot = os.path.join(d, "_rot.pdf")
    with pikepdf.open(raw) as p:
        for i in flip:
            pg = p.pages[i - 1]
            pg.Rotate = (int(pg.get("/Rotate", 0)) + 180) % 360
        p.save(rot)
    env = dict(os.environ, PATH=TESS + os.pathsep + os.environ.get("PATH", ""))
    o = subprocess.run([sys.executable, "-m", "ocrmypdf", "--force-ocr", "--output-type", "pdfa", "--optimize", "1", "-l", "eng",
                        "--sidecar", os.path.join(d, "doc.fixed.txt"), rot, os.path.join(d, "doc.fixed.pdf")],
                       capture_output=True, text=True, env=env, timeout=3600)
    os.remove(rot)
    print("OCR", "ok" if o.returncode == 0 else o.stderr[-300:], flush=True)


main()
