"""scan.py — BOLO 149, 10/17: one command scans the next document off the ES-590W feeder and files it.

Chief loads the pages and says the kind; Claude runs this. NAPS2's console drives the scanner over TWAIN (USB; NAPS2
does not see the ES-590W over ESCL/Wi-Fi). Each document gets its own folder:
  _PRIVATE/intake/paper/scans/<YYYY-MM-DD>_<NNN>_<kind>/
    raw.pdf      the untouched scan (never rewritten except to carry the blurb)
    doc.pdf      searchable copy (OCRmyPDF; typed and receipt only)
    doc.txt      the OCR text sidecar
    context.md   Chief's voice blurb (blurb.py), if one was waiting
Handwriting skips Tesseract: scan-reader reads raw.pdf and writes transcript.md.

Usage (Python 3.11, which has pikepdf + ocrmypdf):
  python scan.py typed | hand | photo | receipt [--simplex]
"""
import argparse
import os
import shutil
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import blurb  # noqa: E402

ROOT = blurb.ROOT
OUT = os.path.join(ROOT, "_PRIVATE", "intake", "paper", "scans")
NAPS2 = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\WindowsApps\NAPS2.Console.exe")
TESS = r"C:\Program Files\Tesseract-OCR"
DEVICE = "EPSON ES-590W"
# the settings table on the glass (research recs, 10/17): dpi · bit depth · both sides · OCR
KINDS = {"typed": (300, "gray", True, True), "hand": (300, "color", True, False),
         "photo": (600, "color", False, False), "receipt": (300, "gray", False, True)}


def next_dir(kind):
    day = time.strftime("%Y-%m-%d")
    os.makedirs(OUT, exist_ok=True)
    n = 1 + sum(1 for d in os.listdir(OUT) if d.startswith(day))
    d = os.path.join(OUT, f"{day}_{n:03d}_{kind}")
    os.makedirs(d)
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=list(KINDS))
    ap.add_argument("--simplex", action="store_true", help="one side only")
    a = ap.parse_args()
    dpi, depth, duplex, ocr = KINDS[a.kind]
    d = next_dir(a.kind)
    raw = os.path.join(d, "raw.pdf")
    cmd = [NAPS2, "--driver", "twain", "--device", DEVICE, "--source", "duplex" if duplex and not a.simplex else "feeder",
           "--dpi", str(dpi), "--bitdepth", depth, "--jpegquality", "95", "-o", raw, "--force"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    if r.returncode or not os.path.exists(raw):
        shutil.rmtree(d, ignore_errors=True)
        sys.exit(f"SCAN failed (exit {r.returncode}): {(r.stdout + r.stderr).strip()[-400:] or 'no output; is paper in the feeder?'}")
    if ocr:
        env = dict(os.environ, PATH=TESS + os.pathsep + os.environ.get("PATH", ""))
        o = subprocess.run([sys.executable, "-m", "ocrmypdf", "--deskew", "--rotate-pages", "--clean", "--output-type", "pdfa",
                            "--optimize", "1", "-l", "eng", "--sidecar", os.path.join(d, "doc.txt"), raw, os.path.join(d, "doc.pdf")],
                           capture_output=True, text=True, env=env, timeout=1800)
        note = "OCR ok" if o.returncode == 0 else f"OCR failed (exit {o.returncode}): {o.stderr.strip()[-200:]}"
    else:
        note = "no OCR (scan-reader reads it)" if a.kind == "hand" else "no OCR"
    b = blurb.attach(d)
    import pikepdf
    with pikepdf.open(raw) as p:
        pages = len(p.pages)
    print(f"SCAN {os.path.basename(d)} · {pages} page(s) · {dpi} dpi {depth} · {note} · "
          + (f"blurb {b['id']} attached" if b else "no blurb waiting"))


if __name__ == "__main__":
    main()
