#!/usr/bin/env python3
"""Pick a route for turning a PDF into text (stdlib only, no installs).

Tries pdftotext (Poppler, installed on the box) first, with and without -layout, and judges
the result by characters per page. If the text layer is missing or poor, it prints a plain-text
note of what else would be needed (OCR, a layout-aware converter); it installs and runs nothing else.

Usage: python _tools/ingest/pdf_route.py <file.pdf> [out.txt]
Exit 0 text written, 3 poor or empty text layer (note printed), 2 usage or tool missing.
"""
import re
import shutil
import subprocess
import sys

MIN_CHARS_PER_PAGE = 200  # below this the page is treated as scanned or image-only


def run(args):
    r = subprocess.run(args, capture_output=True, timeout=300)
    return r.stdout.decode("utf-8", "replace") if r.returncode == 0 else ""


def pages(pdf):
    info = run(["pdfinfo", pdf]) if shutil.which("pdfinfo") else ""
    m = re.search(r"^Pages:\s+(\d+)", info, re.M)
    return int(m.group(1)) if m else 0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    pdf = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    if not shutil.which("pdftotext"):
        print("NOTE · pdftotext is not on PATH. Needed: Poppler (pdftotext, pdfinfo). Nothing was installed.")
        return 2
    n = pages(pdf) or 1
    best, mode = "", ""
    for label, flags in (("layout", ["-layout"]), ("raw", [])):
        txt = run(["pdftotext", *flags, pdf, "-"])
        if len(txt.strip()) > len(best.strip()):
            best, mode = txt, label
    per = len(best.strip()) / n
    print(f"ROUTE · pdftotext ({mode}) · {n} page(s) · {per:.0f} chars/page")
    if per < MIN_CHARS_PER_PAGE:
        print("NOTE · the text layer is missing or poor (likely a scan). Still needed, not installed here:")
        print("  - an OCR step (for example ocrmypdf with Tesseract) to add a text layer, then rerun this script")
        print("  - for tables or slide decks, a layout-aware converter if pdftotext -layout flattens them")
        if out and best.strip():
            open(out, "w", encoding="utf-8", newline="\n").write(best)
            print(f"  partial text written to {out}")
        return 3
    if out:
        open(out, "w", encoding="utf-8", newline="\n").write(best)
        print(f"WROTE · {out}")
    else:
        sys.stdout.write(best)
    print("CHECK · read one early and one hard section before trusting the text (tables and columns break first).")
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    sys.exit(main())

# idea from sickn33/agentic-awesome-skills skills/pdf-conversion-router (community; license not stated in file; classify, route, validate) · own code, pdftotext only · BOLO 140 · 2026-10-13
