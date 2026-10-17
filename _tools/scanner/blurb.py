"""blurb.py — BOLO 149, 10/17 (Chief: "before every document that I scan ... take that text ... and then attach it to that document").

The voice blurb: Chief says a few words about the next document; Claude cleans them up and queues them here; the next scan
takes the oldest waiting blurb (first in, first out) and carries it three ways:
  context.md beside the scan · the PDF's Subject + Keywords · the blurb embedded inside the PDF as an attached file.
The raw words are kept next to the clean ones (the intake lineage rule, BOLO 107).

Usage (run with Python 3.11, which has pikepdf):
  python blurb.py add --clean "clean text" [--raw "what Chief said"] [--tags a,b]
  python blurb.py list                      # waiting blurbs
  python blurb.py drop B007                 # cancel one
  python blurb.py attach <doc folder>       # scan.py calls this; pairs the oldest waiting blurb
"""
import argparse
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
QDIR = os.path.join(ROOT, "_PRIVATE", "intake", "paper", "_blurbs")
QUEUE = os.path.join(QDIR, "queue.jsonl")


def load():
    if not os.path.exists(QUEUE):
        return []
    return [json.loads(l) for l in open(QUEUE, encoding="utf-8") if l.strip()]


def save(rows):
    os.makedirs(QDIR, exist_ok=True)
    tmp = QUEUE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    os.replace(tmp, QUEUE)


def add(clean, raw="", tags=""):
    rows = load()
    n = 1 + max([int(r["id"][1:]) for r in rows] or [0])
    r = {"id": f"B{n:03d}", "said": time.strftime("%Y-%m-%d %H:%M:%S"), "clean": clean.strip(), "raw": raw.strip(),
         "tags": [t.strip() for t in tags.split(",") if t.strip()], "status": "waiting", "doc": None}
    rows.append(r)
    save(rows)
    return r


def waiting():
    return [r for r in load() if r["status"] == "waiting"]


def attach(doc_dir, blurb_id=None):
    """Pair a blurb with the scanned document in doc_dir; returns the blurb or None when none is waiting."""
    rows = load()
    pick = next((r for r in rows if r["status"] == "waiting" and (blurb_id is None or r["id"] == blurb_id)), None)
    if not pick:
        return None
    md = (f"# Context · {pick['id']}\n\nsaid: {pick['said']}\n"
          + (f"tags: {', '.join(pick['tags'])}\n" if pick["tags"] else "")
          + f"\n{pick['clean']}\n" + (f"\n> raw: {pick['raw']}\n" if pick["raw"] else ""))
    with open(os.path.join(doc_dir, "context.md"), "w", encoding="utf-8") as f:
        f.write(md)
    for name in ("doc.pdf", "raw.pdf"):   # the searchable copy and the untouched scan both carry it
        p = os.path.join(doc_dir, name)
        if os.path.exists(p):
            _embed(p, pick, md)
    pick["status"], pick["doc"], pick["attached"] = "attached", os.path.relpath(doc_dir, ROOT), time.strftime("%Y-%m-%d %H:%M:%S")
    save(rows)
    return pick


def _embed(pdf, pick, md):
    import pikepdf
    with pikepdf.open(pdf, allow_overwriting_input=True) as p:
        p.docinfo["/Subject"] = pick["clean"][:2000]
        p.docinfo["/Keywords"] = ", ".join([pick["id"]] + pick["tags"])
        p.attachments["context.md"] = pikepdf.AttachedFileSpec(p, md.encode("utf-8"), mime_type="text/markdown")
        p.save(pdf)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add"); a.add_argument("--clean", required=True); a.add_argument("--raw", default=""); a.add_argument("--tags", default="")
    sub.add_parser("list")
    d = sub.add_parser("drop"); d.add_argument("id")
    t = sub.add_parser("attach"); t.add_argument("doc_dir"); t.add_argument("--id")
    x = ap.parse_args()
    if x.cmd == "add":
        r = add(x.clean, x.raw, x.tags)
        print(f"BLURB {r['id']} waiting · {len(waiting())} in line · the next scan takes the oldest")
    elif x.cmd == "list":
        w = waiting()
        print(f"{len(w)} waiting" + "".join(f"\n  {r['id']} · {r['said'][11:16]} · {r['clean'][:70]}" for r in w))
    elif x.cmd == "drop":
        rows = load()
        for r in rows:
            if r["id"] == x.id and r["status"] == "waiting":
                r["status"] = "dropped"
        save(rows)
        print(f"BLURB {x.id} dropped")
    else:
        r = attach(x.doc_dir, x.id)
        print(f"BLURB {r['id']} attached -> {r['doc']}" if r else "BLURB none waiting; scanned with no context")


if __name__ == "__main__":
    sys.exit(main())
