"""The intake inventory: count and clean the note vaults on disk (INTEL CYCLE Lane B, SOP §9, BOLO 107).

Usage:  python _tools/intake/inventory.py

Zero tokens. Reads the four vaults, keeps text notes only, and finds:
  exact duplicates (same body after cleanup) · the Obsidian copies of Joplin notes (by title) ·
  book dumps (Lane A, out of the packet) · empty notes ·
  lineage words (old names, SOP §9 CLEAN) · notes per year.
Joplin's sync folder holds folders, tags and resources too; only type_ 1 (a note) counts.
The script judges nothing. Reading and binning is the Payload Specialists' job.

Outputs (git-ignored): _PRIVATE/intake/inventory.json · _PRIVATE/intake/inventory.md
"""
import hashlib, io, json, os, re, sys, time
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "_PRIVATE", "intake")
VAULTS = [
    ("obsidian", "OVER_EXIT_OUT_OBSIDIAN"),
    ("joplin", ".ASTRO7EX.SYNC.JOPLIN"),
    ("logseq", "logseq_2023_journals_notes"),
    ("devlog", "_devlog"),
]
TEXT = {".md", ".txt"}
SKIP_DIRS = {".git", ".obsidian", ".trash", "node_modules", "assets", ".recycle", "pyscripts_backup"}
SKIP_PATHS = ("/logseq/bak",)   # Logseq's own backup copies of every page
BOOK_ISBN = re.compile(r"97[89]\d{10}")
BOOK_CHARS = 200_000            # a note this long is a pasted book or a merged export, not Chief's writing
LINEAGE = ["Inner Spiral", "Red Hills", "Skeeter Creek", "Red Stick Creek", "Ariel"]
EMPTY_CHARS = 40
JOPLIN_META = re.compile(r"^[a-z_]+:.*$")
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)


def body_of(vault, raw):
    """The note's text with vault chrome removed. Returns (body, is_note)."""
    text = raw.replace("\r\n", "\n")
    if vault == "joplin":
        lines = text.rstrip("\n").split("\n")
        meta = {}
        while lines and JOPLIN_META.match(lines[-1]):
            k, _, v = lines.pop().partition(":")
            meta[k] = v.strip()
        if meta.get("type_") not in (None, "1"):
            return "", False
        text = "\n".join(lines)
    return FRONTMATTER.sub("", text), True


def norm(body):
    return re.sub(r"\s+", " ", body).strip().lower()


def year_of(path, body, mtime):
    m = re.search(r"(20[0-2]\d)[-_.]?(0[1-9]|1[0-2])", os.path.basename(path))
    if m:
        return m.group(1)
    m = re.search(r"\b(20[0-2]\d)-(0[1-9]|1[0-2])-\d\d\b", body[:400])
    if m:
        return m.group(1)
    return time.strftime("%Y", time.localtime(mtime)) + "~"   # ~ = file date, not the note's own


def walk(vault, rel):
    base = os.path.join(ROOT, rel)
    for dp, dns, fns in os.walk(base):
        dns[:] = [d for d in dns if d not in SKIP_DIRS and not any(
            s in os.path.join(dp, d).replace("\\", "/") for s in SKIP_PATHS)]
        for fn in fns:
            if os.path.splitext(fn)[1].lower() in TEXT:
                yield os.path.join(dp, fn)


def main():
    notes, by_hash = [], defaultdict(list)
    skipped = Counter()
    for vault, rel in VAULTS:
        for p in walk(vault, rel):
            try:
                raw = io.open(p, encoding="utf-8", errors="replace").read()
            except OSError:
                skipped[vault] += 1
                continue
            body, is_note = body_of(vault, raw)
            if not is_note:
                skipped[vault] += 1
                continue
            n = norm(body)
            h = hashlib.sha1(n.encode("utf-8")).hexdigest()[:16]
            hits = [w for w in LINEAGE if re.search(r"\b%s\b" % re.escape(w), body, re.I)]
            rec = {
                "vault": vault,
                "path": os.path.relpath(p, ROOT).replace("\\", "/"),
                "chars": len(n),
                "year": year_of(p, body, os.path.getmtime(p)),
                "hash": h,
                "empty": len(n) < EMPTY_CHARS,
                "lineage": hits,
                "title": (body.strip().split("\n", 1)[0].lstrip("# ").strip().lower() if vault == "joplin"
                          else os.path.splitext(os.path.basename(p))[0].strip().lower()),
                "book": bool(BOOK_ISBN.search(os.path.basename(p))) or len(n) > BOOK_CHARS,
            }
            notes.append(rec)
            if not rec["empty"]:
                by_hash[h].append(rec)

    dupes = {h: rs for h, rs in by_hash.items() if len(rs) > 1}
    for rs in dupes.values():   # keep one: the longest path is usually the import copy, so keep the shortest
        keep = min(rs, key=lambda r: (len(r["path"]), r["path"]))
        for r in rs:
            r["dupe_of"] = None if r is keep else keep["path"]
    # Obsidian holds a Joplin import (00_IMPORTED_JOPLIN): the converter changed the formatting,
    # so exact hashes miss it. A title match marks the import copy as the duplicate; Joplin is the source.
    jtitle = {r["title"]: r["path"] for r in notes if r["vault"] == "joplin" and not r["empty"]}
    for r in notes:
        if r["vault"] == "obsidian" and "00_IMPORTED_JOPLIN" in r["path"] and not r.get("dupe_of")                 and r["title"] in jtitle:
            r["dupe_of"] = jtitle[r["title"]]
    live = [r for r in notes if not r["empty"] and not r.get("dupe_of") and not r["book"]]
    books = [r for r in notes if r["book"] and not r["empty"] and not r.get("dupe_of")]

    per_vault = Counter(r["vault"] for r in notes)
    live_vault = Counter(r["vault"] for r in live)
    empty_vault = Counter(r["vault"] for r in notes if r["empty"])
    dupe_vault = Counter(r["vault"] for r in notes if r.get("dupe_of"))
    book_vault = Counter(r["vault"] for r in books)
    cross = Counter()
    for rs in dupes.values():
        vs = sorted({r["vault"] for r in rs})
        if len(vs) > 1:
            cross[" + ".join(vs)] += 1
    years = Counter(r["year"] for r in live)
    lineage = Counter(w for r in live for w in r["lineage"])
    chars = sum(r["chars"] for r in live)

    os.makedirs(OUT, exist_ok=True)
    io.open(os.path.join(OUT, "inventory.json"), "w", encoding="utf-8").write(
        json.dumps({"built": time.strftime("%Y-%m-%d %H:%M"), "notes": notes}, ensure_ascii=False, indent=0))

    L = ["# The intake inventory", "", "Built %s by `_tools/intake/inventory.py` (SOP §9, BOLO 107). Counts only; nothing judged." % time.strftime("%Y-%m-%d %H:%M"), ""]
    L += ["## Per vault", "", "| Vault | Notes | Empty | Duplicates | Book dumps | Live |", "|---|---|---|---|---|---|"]
    for v, _ in VAULTS:
        L.append("| %s | %d | %d | %d | %d | %d |" % (v, per_vault[v], empty_vault[v], dupe_vault[v], book_vault[v], live_vault[v]))
    L.append("| **all** | **%d** | **%d** | **%d** | **%d** | **%d** |" % (len(notes), sum(empty_vault.values()), sum(dupe_vault.values()), len(books), len(live)))
    L += ["", "Book dumps routed to Lane A (an ISBN in the name, or over %s characters): %d notes, about %s characters." % (
        format(BOOK_CHARS, ","), len(books), format(sum(r["chars"] for r in books), ",")), ""]
    L += ["Live text: about %s characters (~%s tokens at 4 chars a token)." % (format(chars, ","), format(chars // 4, ",")), ""]
    L += ["## Overlap between vaults", ""] + (["- %s: %d shared notes" % (k, n) for k, n in cross.most_common()] or ["- none"]) + [""]
    L += ["## Live notes per year", "", "A year with ~ is the file's date, not the note's own.", ""]
    L += ["- %s: %d" % (y, n) for y, n in sorted(years.items())] + [""]
    L += ["## Lineage words in live notes", ""] + ["- %s: %d notes" % (w, lineage[w]) for w in LINEAGE] + [""]
    if any(skipped.values()):
        L += ["## Not notes (skipped)", ""] + ["- %s: %d" % (v, n) for v, n in skipped.items()] + [""]
    io.open(os.path.join(OUT, "inventory.md"), "w", encoding="utf-8").write("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
