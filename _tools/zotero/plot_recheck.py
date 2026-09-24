# -*- coding: utf-8 -*-
"""The plot-shelf re-check (BOLO 77) — run after Chief drops more books. Zero tokens.
  python _tools/zotero/plot_recheck.py
1. snapshots inventory-live.json, re-runs inventory.py (Zotero records + loose Zotero files + the drop folder)
2. lists every file that is new since the snapshot and samples its text (PDF page 30, or EPUB words) so summary spam shows
3. matches the still-needed list (upload rows + unheld canon) against everything held, flips what landed
4. rebuilds the page and prints the remaining need list, one block per lane (tier 1 + the classics)"""
import io, json, os, re, subprocess, sys, zipfile, collections, shutil
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
META = os.path.join(ROOT, "_0.1_BVX_LEARN", "_meta")
INV, SP = os.path.join(META, "inventory-live.json"), os.path.join(META, "plot_sweep.json")
JUNK = re.compile(r"scan to download|bookey|book summary|download link", re.I)


def load(p):
    return json.load(io.open(p, encoding="utf-8"))


def sample(path):
    try:
        if path.lower().endswith(".epub"):
            z = zipfile.ZipFile(path)
            t = " ".join(re.sub(r"<[^>]+>", " ", z.read(n).decode("utf-8", "ignore")) for n in z.namelist() if n.endswith(("html", "htm", "xhtml")))
            w = t.split(); return f"epub {len(w)} words", " ".join(w[2000:2020])
        pages = re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", path], capture_output=True, text=True, errors="replace").stdout)
        n = int(pages.group(1)) if pages else 0
        pg = str(min(30, max(1, n // 3)))
        t = subprocess.run(["pdftotext", "-f", pg, "-l", pg, path, "-"], capture_output=True, text=True, errors="replace").stdout
        head = subprocess.run(["pdftotext", "-l", "2", path, "-"], capture_output=True, text=True, errors="replace").stdout
        return f"{n} pp" + (" · SPAM?" if JUNK.search(head) else "") + ("" if t.strip() else " · no text layer"), " ".join(t.split())[:110]
    except Exception as e:
        return "unreadable", str(e)[:60]


full = lambda s: " ".join(re.sub(r"[^a-z0-9 ]", " ", re.sub(r"\(.*?\)|\[.*?\]", " ", (s or "").lower())).split())


def main():
    snap = os.path.join(os.environ.get("TEMP", "."), "inv_snapshot.json")
    shutil.copy(INV, snap)
    subprocess.run([sys.executable, os.path.join(HERE, "inventory.py")], capture_output=True)
    before = {i.get("pdf") for i in load(snap)}
    inv = load(INV)
    new = [i for i in inv if i.get("pdf") not in before and i.get("pdf_exists")]
    print(f"NEW FILES · {len(new)}")
    for i in new:
        tag, txt = sample(i["pdf"])
        print(f"  [{tag}] {i['title'][:70]} | {', '.join(i['authors'][:2])[:30]}\n      “{txt}”")
    held = [(full(i["title"]) + " " + " ".join(i.get("authors") or []).lower(), i) for i in inv
            if i.get("pdf_exists") and not re.search(r"SYD.?Screenplay.?PDF|Booth.The.Rhetoric.Of.Fiction", i.get("pdf") or "", re.I)]

    def have(title, author):
        f = full(re.split(r"[:;]| - ", title)[0]); sur = [w for w in re.split(r"[ ,;.]+", (author or "").lower()) if len(w) > 3]
        if len(f) < 10:  # short generic titles ("Narrative", "Genre") false-match too easily
            return None
        return next((i for h, i in held if f in h and (not sur or any(s in h for s in sur))), None)
    d = load(SP); flipped = []
    for k in d["keep"]:
        if k["src"] == "zlib-gap":
            i = have(k["clean"], k["author"])
            if i:
                k["src"] = "drop" if i.get("src") == "drop" else "zotero"; k["why"] += " · landed " + os.path.basename(i["pdf"])[:40]
                flipped.append(k["clean"])
    for c in d["canon"]:
        if not c["held"]:
            i = have(c["title"], c["author"])
            if i:
                c["held"] = True; c["match"] = i["title"][:70]; flipped.append("CANON " + c["title"])
    json.dump(d, io.open(SP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nLANDED ON THE LIST · {len(flipped)}")
    for f in flipped:
        print("  " + f[:90])
    subprocess.run([sys.executable, os.path.join(HERE, "plot_sweep_page.py")])
    gap = [k for k in d["keep"] if k["src"] == "zlib-gap"]
    print(f"\nSTILL TO GET · {len(gap)} (tier {dict(collections.Counter(k['tier'] for k in gap))})")
    seen = set()
    for lane in ["RAILS", "THEORY", "GAME-RAILS", "SERIES", "TROPES", "FABULA", "SCENE", "AI-PLANNING", "COUNTER"]:
        rows = [k for k in sorted(gap, key=lambda k: k["clean"]) if k["tier"] == 1 and k["lane"] == lane]
        rows = [k for k in rows if not (full(k["clean"])[:30] in seen or seen.add(full(k["clean"])[:30]))]
        if rows:
            print(f"## {lane} ({len(rows)})")
            for k in rows:
                print(f"  {re.sub(r'[;]', ',', k['author']).strip(' ,')[:40]} — {k['clean'][:100]}")
    cn = [c for c in d["canon"] if not c["held"]]
    print(f"## CLASSICS ({len(cn)})")
    for c in cn:
        print(f"  {c['author']} — {c['title']}")


if __name__ == "__main__":
    main()
