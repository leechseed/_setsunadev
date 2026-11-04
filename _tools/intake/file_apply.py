# -*- coding: utf-8 -*-
"""file_apply.py: apply an approved scan filing (BOLO 149/170, 11/4: Chief "take every rec" on tonight's filing).

Usage:  python _tools/intake/file_apply.py <filing.json> [--apply] [--json]

Reads a scan-filer filing.json ({"docs": [{id, title, date, bin, tags, ties, private, why, folders?}]}). Each doc's scan
folder(s) under _PRIVATE/intake/paper/scans/ move to _PRIVATE/intake/<bin>/<folder name>/ (the name is kept, so the scan
date and kind stay readable). A filing.md beside the scan carries the title, date, tags, ties and the why.
Folders: the doc's "folders" list if it has one, else the scan folder whose number matches the id (d007 -> <date>_007_*);
the date comes from the filing's file name. Every .md/.json/.html under the repo that cites a moved folder is rewritten
to the new path (the logs, git and the big vault folders are skipped). A ledger line per move goes to
_PRIVATE/intake/filed.jsonl. Without --apply it is a dry run: it prints the moves and the files it would rewrite.
"""
import io, json, os, re, shutil, sys, time
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
INTAKE = os.path.join(ROOT, "_PRIVATE", "intake")
SCANS = os.path.join(INTAKE, "paper", "scans")
BINS = ("paper", "scripts", "shelf", "receipts", "photos", "other")
SKIP = {".git", "_LOG", "node_modules", ".venv", ".venv-gpu", "logseq_2023_journals_notes", "_CLAUDE_ARCHIVE_2026-08-15",
        "scans", "pages", "_pages"}
EXT = (".md", ".json", ".html")


def plan(filing_path):
    day = re.match(r"(\d{4}-\d{2}-\d{2})", os.path.basename(filing_path))
    day = day.group(1) if day else None
    docs = json.load(io.open(filing_path, encoding="utf-8"))["docs"]
    names = sorted(os.listdir(SCANS))
    moves = []
    for d in docs:
        if d.get("bin") not in BINS:
            raise SystemExit("doc %s: bin %r is not one of %s" % (d.get("id"), d.get("bin"), ", ".join(BINS)))
        want = d.get("folders") or [day + "_" + d["id"][1:].zfill(3)]
        for w in want:
            hit = [n for n in names if n == w or n.startswith(w + "_")]
            if len(hit) != 1:
                raise SystemExit("doc %s: no single scan folder for %r (found %s)" % (d["id"], w, hit))
            src = os.path.join(SCANS, hit[0])
            dst = os.path.join(INTAKE, d["bin"], hit[0])
            moves.append({"doc": d, "folder": hit[0], "src": src, "dst": dst})
    return moves


def citing_files(folders):
    pats = [("intake/paper/scans/" + f, "intake\\paper\\scans\\" + f) for f in folders]
    out = []
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [x for x in dn if x not in SKIP]
        for f in fn:
            if not f.endswith(EXT):
                continue
            p = os.path.join(dp, f)
            try:
                t = io.open(p, encoding="utf-8").read()
            except (UnicodeDecodeError, OSError):
                continue
            if any(a in t or b in t for a, b in pats):
                out.append(p)
    return out


def main():
    a = sys.argv[1:]
    if not a or a[0].startswith("-"):
        print(__doc__); return 2
    filing, do, as_json = a[0], "--apply" in a, "--json" in a
    moves = plan(filing)
    for m in moves:
        if os.path.exists(m["dst"]):
            raise SystemExit("already filed: " + m["dst"])
    cites = citing_files([m["folder"] for m in moves])
    rep = {"apply": do, "moves": [{"doc": m["doc"]["id"], "title": m["doc"]["title"], "bin": m["doc"]["bin"],
                                   "from": os.path.relpath(m["src"], ROOT), "to": os.path.relpath(m["dst"], ROOT)} for m in moves],
           "rewrites": [os.path.relpath(p, ROOT) for p in cites]}
    if do:
        for m in moves:
            os.makedirs(os.path.dirname(m["dst"]), exist_ok=True)
            shutil.move(m["src"], m["dst"])
            d = m["doc"]
            io.open(os.path.join(m["dst"], "filing.md"), "w", encoding="utf-8").write(
                "# %s\n\n- **Date:** %s\n- **Bin:** %s\n- **Tags:** %s\n- **Ties:** %s\n- **Private:** %s\n- **Why:** %s\n- **Filed:** %s from %s\n"
                % (d["title"], d.get("date") or "unknown", d["bin"], ", ".join(d.get("tags") or []), ", ".join(d.get("ties") or []) or "none",
                   "yes" if d.get("private") else "no", d.get("why", ""), time.strftime("%Y-%m-%d %H:%M"), os.path.basename(filing)))
            with io.open(os.path.join(INTAKE, "filed.jsonl"), "a", encoding="utf-8") as L:
                L.write(json.dumps({"at": time.strftime("%Y-%m-%d %H:%M"), "doc": d["id"], "title": d["title"], "bin": d["bin"],
                                    "from": os.path.relpath(m["src"], ROOT), "to": os.path.relpath(m["dst"], ROOT)}, ensure_ascii=False) + "\n")
        for p in cites:
            raw = io.open(p, encoding="utf-8", newline="").read()
            new = raw
            for m in moves:
                rel_new = os.path.relpath(m["dst"], os.path.join(ROOT, "_PRIVATE")).replace("\\", "/")
                new = new.replace("intake/paper/scans/" + m["folder"], rel_new)
                new = new.replace("intake\\paper\\scans\\" + m["folder"], rel_new.replace("/", "\\"))
            if new != raw:
                io.open(p, "w", encoding="utf-8", newline="").write(new)
    if as_json:
        print(json.dumps(rep, indent=1, ensure_ascii=False)); return 0
    print(("FILED" if do else "DRY RUN") + " · %d folder(s) · %d citing file(s)" % (len(moves), len(cites)))
    for r in rep["moves"]:
        print("  %s  %-8s %s  ->  %s" % (r["doc"], r["bin"], r["from"].replace("\\", "/").split("/")[-1], r["to"].replace("\\", "/")))
    for p in rep["rewrites"]:
        print("  rewrite " + p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
