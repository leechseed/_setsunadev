"""prep_wave.py — 10/30: zero-token prep for a distill wave (README step 8): pdftotext + one brief per book.
Usage: python -X utf8 _tools/zotero/prep_wave.py 0092 0176 ...   (4-digit BVX numbers)
Writes _PRIVATE/distill_wave/BVX.####.txt (book text, never public) and BVX.####.brief.md.
Prints one line per book: ok / no-pdf / pdftotext-failed. Books with no PDF are Chief's to attach in Zotero.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
META = os.path.join(ROOT, "_0.1_BVX_LEARN", "_meta")
OUT = os.path.join(ROOT, "_PRIVATE", "distill_wave")
norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())[:40]


def main(ids):
    cat = {b["id"]: b for b in json.load(open(os.path.join(META, "catalog.json"), encoding="utf8"))}
    inv = json.load(open(os.path.join(META, "inventory-live.json"), encoding="utf8"))
    pdfs = {}
    for r in inv:
        if r.get("pdf_exists"):
            pdfs.setdefault(norm(r["title"]), (r["pdf"], r.get("zkey", "")))
    os.makedirs(OUT, exist_ok=True)
    for i in ids:
        bid = f"BVX.{i}"
        b = cat[bid]
        hit = pdfs.get(norm(b["t"]))
        if not hit:
            print(bid, "no-pdf", b["t"][:60])
            continue
        pdf, zkey = hit
        txt = os.path.join(OUT, f"{bid}.txt")
        r = subprocess.run(["pdftotext", "-layout", pdf, txt], capture_output=True, text=True)
        if r.returncode or not os.path.exists(txt) or os.path.getsize(txt) < 5000:
            print(bid, "pdftotext-failed (scanned image or empty?)", b["t"][:60])
            continue
        pages = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
        m = re.search(r"Pages:\s+(\d+)", pages)
        npg = m.group(1) if m else "unknown"
        brief = (f"JOB: distilling-book\n\nBook: {bid} · {b['t']} · {b.get('a', '')}\n"
                 f"Text (pdftotext, read by section, never whole): _PRIVATE/distill_wave/{bid}.txt\n"
                 f"Template: _0.1_BVX_LEARN/_meta/TEMPLATE.distill.v4.md (sections B and C)\n"
                 f"Write: _0.1_BVX_LEARN/KNOWLEDGE_AREAS/{bid}.md\n"
                 f"Subjects: {', '.join(b.get('subjects', []))} · primary {b.get('primary', '')}\n"
                 f"Frontmatter facts (use exactly, never write 'unknown'): zotero_key {zkey} · pdf_pages {npg} · spine [TEXTURE] unless the book clearly keys elsewhere.\n"
                 f"Coverage rule: read every chapter in runs of 15 to 25 pages. Name any unread chapter in §10 and report DONE_WITH_CONCERNS. "
                 f"Cross-reference only BVX ids you have confirmed exist in KNOWLEDGE_AREAS; never list the book itself.\n"
                 f"Use: craft basis for the OXO script editors (`.claude/agents/editing-*.md`, `reading-cold.md`). "
                 f"Weight §3 framework, §5 heuristics and §7 pitfalls; keep `feeds: []` unless the book is about character psychology.\n")
        open(os.path.join(OUT, f"{bid}.brief.md"), "w", encoding="utf8").write(brief)
        print(bid, "ok", os.path.getsize(txt) // 1000, "KB", b["t"][:60])


if __name__ == "__main__":
    main(sys.argv[1:])
