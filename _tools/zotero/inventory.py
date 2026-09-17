# -*- coding: utf-8 -*-
"""Zotero live-DB inventory (BOLO 18 stage 2, step 1). Reads a COPY of the live zotero.sqlite,
writes _0.1_BVX_LEARN/_meta/inventory-live.json + INVENTORY-LIVE.md, imports Chief's 0N_ tag scheme as spine keys,
and diffs against catalog.json (title-normalised). Nothing in the repo is a PDF; only paths are recorded.

Usage: python _tools/zotero/inventory.py [path-to-zotero.sqlite]
"""
import io, os, re, sys, json, shutil, sqlite3, collections, datetime
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
META = os.path.join(ROOT, "_0.1_BVX_LEARN", "_meta")
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.expanduser("~"), "Zotero", "zotero.sqlite")
STORAGES = [os.path.join(os.path.dirname(SRC), "storage"),
            r"D:\My Google Drive\ZOTERO_DATA_DIRECTORY\storage",  # live first, the Dec-2023 Drive copy as fallback
            r"C:/Users/U01_LEECHSEED/Desktop/_PDF_DROP"]  # the drop folder (9/16): acquisitions land here, no Zotero filing; drop_scan() below picks them up

# Chief's 2023 tag scheme (00_ .. 09_) -> the story spine (ssot_01_story_spine_comparative_tree) - provisional 9/16
TAG2SPINE = {"00_THEORY OF COMPOSITION": "L0", "01_THEME": "L6", "02_PLOT": "L4", "02_PLOT SYUHZET": "L4",
             "03_CHARACTER": "L5", "CHARACTER": "L5", "04_SETTING": "SETTING", "05_SEQUENCE FABULA": "L4",
             "06_NARRATOR": "TEXTURE", "07_DIEGESIS": "TEXTURE", "08_FUZZ INTERTEXT AND GENRE": "L7",
             "09_PUBLICATION": "L7", "PLOT & STORY": "L4", "NARRATIVE": "L0", "PLOT": "L4"}


def norm(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()[:80]


def drop_scan(cat_by_title, today):
    """The drop folder (9/16): every PDF under STORAGES[2] becomes an item with no Zotero record, src "drop".
    Title/author/year are guessed from the filename (Zotero export 'Author - Year - Title.pdf' or 'Title (Author).pdf' or
    z-lib 'Title (Author)ISBN (Z-Library).pdf'); the sweep keys them like any other row (bvx NEW until cataloged)."""
    root = STORAGES[2]; out = []
    cat_by_file = {c["drop_file"]: c for c in cat_by_title.values() if c.get("drop_file")}
    if not os.path.isdir(root):
        return out
    for dp, _, fs in os.walk(root):
        for f in sorted(fs):
            if not f.lower().endswith(".pdf") or f.startswith("._") or os.path.getsize(os.path.join(dp, f)) < 2048:
                continue  # AppleDouble resource forks and empty files are not books
            stem = re.sub(r"\s*\(Z-Library\)|\s*\(z-lib\.org\)|\s*9\d{12}|\s*\d{13}", "", f[:-4]).strip()
            stem = re.sub(r"^\d{6,}-", "", stem)  # a Scribd numeric prefix
            if "-" in stem and " " not in stem:
                stem = stem.replace("-", " ")  # hyphenated Scribd names
            year = (re.search(r"(1[89]\d\d|20\d\d)", stem) or [None, ""])[1] if re.search(r"(1[89]\d\d|20\d\d)", stem) else ""
            m = re.match(r"^(.+?) - (\d{4}) - (.+)$", stem)
            if m:
                authors, title = [a.strip() for a in re.split(r",| and | & ", m.group(1)) if a.strip()], m.group(3).strip()
            else:
                m2 = re.match(r"^(.+?)\s*\(([^()]+)\)\s*$", stem)
                if m2:
                    title, authors = m2.group(1).strip(), [a.strip() for a in re.split(r",| and | & ", m2.group(2)) if a.strip()]
                else:
                    title, authors = stem, []
            c = cat_by_file.get(f) or cat_by_title.get(norm(title))
            if c and c.get("drop_file") == f:
                title, authors, year = c["t"], [x.strip() for x in re.split(r",| & ", c["a"]) if x.strip()], str(c.get("year") or "")
            out.append({"zid": None, "zkey": "", "type": "drop", "title": title, "authors": authors[:4], "year": year,
                        "publisher": "", "isbn": "", "pages": "", "abstract": False, "tags": [], "collections": [], "spine": [],
                        "has_pdf": True, "pdf_exists": True, "pdf": os.path.join(dp, f), "annotations": 0, "notes": [],
                        "bvx": c["id"] if c else None, "subject": c["primary"] if c else None,
                        "added": today, "modified": today, "src": "drop"})
    return out


def main():
    tmp = os.path.join(os.environ.get("TEMP", "."), "zotero-inventory-copy.sqlite")
    shutil.copy(SRC, tmp)
    db = sqlite3.connect(tmp); db.row_factory = sqlite3.Row
    q = lambda s, *a: db.execute(s, a).fetchall()
    types = {r["itemTypeID"]: r["typeName"] for r in q("select * from itemTypes")}
    fields = {r["fieldID"]: r["fieldName"] for r in q("select * from fields")}
    deleted = {r["itemID"] for r in q("select itemID from deletedItems")}
    data = collections.defaultdict(dict)
    for r in q("select d.itemID, d.fieldID, v.value from itemData d join itemDataValues v on v.valueID=d.valueID"):
        data[r["itemID"]][fields[r["fieldID"]]] = r["value"]
    authors = collections.defaultdict(list)
    for r in q("select ic.itemID, c.lastName, c.firstName from itemCreators ic join creators c on c.creatorID=ic.creatorID order by ic.orderIndex"):
        authors[r["itemID"]].append(r["lastName"] or r["firstName"] or "")
    tags = collections.defaultdict(list)
    for r in q("select it.itemID, t.name from itemTags it join tags t on t.tagID=it.tagID"):
        tags[r["itemID"]].append(r["name"])
    colls = collections.defaultdict(list)
    for r in q("select ci.itemID, c.collectionName from collectionItems ci join collections c on c.collectionID=ci.collectionID"):
        colls[r["itemID"]].append(r["collectionName"])
    atts = collections.defaultdict(list)
    for r in q("select a.itemID, a.parentItemID, a.contentType, a.path, i.key from itemAttachments a join items i on i.itemID=a.itemID"):
        if r["itemID"] not in deleted:
            atts[r["parentItemID"]].append(dict(r))
    notes = collections.defaultdict(list)
    for r in q("select parentItemID, note from itemNotes"):
        notes[r["parentItemID"]].append(re.sub("<[^>]+>", " ", r["note"] or "").strip())
    ann = collections.Counter()
    for r in q("select att.parentItemID as p, count(*) as n from itemAnnotations a join itemAttachments att on att.itemID=a.parentItemID group by att.parentItemID"):
        ann[r["p"]] = r["n"]
    zkey = {r["itemID"]: r["key"] for r in q("select itemID, key from items")}

    cat = json.load(io.open(os.path.join(META, "catalog.json"), encoding="utf-8"))
    cat_by_title = {norm(c["t"]): c for c in cat}

    items = []
    for r in q("select itemID, itemTypeID, dateAdded, dateModified from items"):
        iid = r["itemID"]; tn = types[r["itemTypeID"]]
        if iid in deleted or tn in ("attachment", "note", "annotation"):
            continue
        d = data[iid]; title = d.get("title", "")
        pdfs = [a for a in atts[iid] if (a["contentType"] or "").endswith("pdf")]
        pdf_path = None
        for a in pdfs:
            p = a["path"] or ""
            if p.startswith("storage:"):
                cands = [os.path.join(s, a["key"], p[8:]) for s in STORAGES]
                pdf_path = next((c for c in cands if os.path.exists(c)), cands[0])
            elif p:
                pdf_path = p
            if pdf_path and os.path.exists(pdf_path):
                break
        spine = sorted({TAG2SPINE[t] for t in tags[iid] if t in TAG2SPINE})
        c = cat_by_title.get(norm(title))
        items.append({"zid": iid, "zkey": zkey[iid], "type": tn, "title": title, "authors": authors[iid][:4],
                      "year": (d.get("date") or "")[:4], "publisher": d.get("publisher", ""), "isbn": d.get("ISBN", ""),
                      "pages": d.get("numPages", ""), "abstract": bool(d.get("abstractNote")),
                      "tags": tags[iid], "collections": colls[iid], "spine": spine,
                      "has_pdf": bool(pdfs), "pdf_exists": bool(pdf_path and os.path.exists(pdf_path)), "pdf": pdf_path,
                      "annotations": ann.get(iid, 0), "notes": notes[iid],
                      "bvx": c["id"] if c else None, "subject": c["primary"] if c else None,
                      "added": r["dateAdded"][:10], "modified": r["dateModified"][:10]})
    drops = drop_scan(cat_by_title, str(datetime.date.today()))
    items += drops
    # carry the sweep's own fields across regenerations (9/16 finding: the PS TOC keys and repaired titles lived only in
    # this file; regenerating from the DB silently dropped them). Matched by zkey; the DB never wins over a sweep field.
    prev_p = os.path.join(META, "inventory-live.json")
    if os.path.exists(prev_p):
        prev = {i.get("zkey") or i.get("pdf"): i for i in json.load(io.open(prev_p, encoding="utf-8"))}
        carried = 0
        for i in items:
            o = prev.get(i["zkey"] or i.get("pdf"))  # drop rows have no zkey; they carry by path
            if not o:
                continue
            for k in ("spine", "spine_src", "subject", "subject_src", "junk_title", "rot"):
                if k in o:
                    i[k] = o[k]
            if o.get("spine_src") in ("toc", "toc-off") and o.get("title") and o["title"] != i["title"]:
                i["title"] = o["title"]  # a PS-repaired boilerplate title
            carried += 1
        print(f"carried sweep fields for {carried} items from the previous inventory")
    # rot notes live in _meta/rot.json (9/16) so they survive every regeneration of this file
    rp = os.path.join(META, "rot.json")
    if os.path.exists(rp):
        rot = json.load(io.open(rp, encoding="utf-8"))
        for i in items:
            if i.get("bvx") in rot:
                i["rot"] = rot[i["bvx"]]
    items.sort(key=lambda x: (x["bvx"] is None, x["title"].lower()))
    io.open(os.path.join(META, "inventory-live.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(items, ensure_ascii=False, indent=1))

    n = len(items); withpdf = sum(i["has_pdf"] for i in items); on_disk = sum(i["pdf_exists"] for i in items)
    new = [i for i in items if i["bvx"] is None]; keyed = [i for i in items if i["spine"]]
    story = [i for i in items if i["subject"] in ("CRE", "LIT")]
    tagc = collections.Counter(t for i in items for t in i["tags"])
    spc = collections.Counter(s for i in items for s in i["spine"])
    subj = collections.Counter(i["subject"] or "NEW" for i in items)
    L = ["---", "id: BVX-LEARN.inventory-live", "title: \"Zotero live-library inventory\"", "type: report",
         f"generated: {datetime.date.today()}", f"source: \"{SRC}\"", "status: BOLO 18 stage 2 - step 1", "---", "",
         "# Zotero live-library inventory", "",
         "Read from a copy of the live `zotero.sqlite`. Data written to `inventory-live.json` (paths only, no PDFs).", "",
         "| | |", "|---|---|", f"| Top-level items | **{n}** |", f"| With a PDF attachment | {withpdf} |",
         f"| PDF present on disk | {on_disk} |", f"| Already in catalog.json (BVX id) | {n - len(new)} |",
         f"| **New since the Dec-2023 catalog** | **{len(new)}** |", f"| Story-side (CRE + LIT by catalog) | {len(story)} |",
         f"| **Spine-keyed from Chief's tags** | **{len(keyed)}** |",
         f"| With PDF annotations | {sum(1 for i in items if i['annotations'])} ({sum(i['annotations'] for i in items)} highlights) |",
         f"| With notes | {sum(1 for i in items if i['notes'])} |", "",
         "## Spine keys imported (tag to level, provisional 9/16)", "", "| Level | Items |", "|---|---|"]
    L += [f"| {k} | {v} |" for k, v in spc.most_common()]
    L += ["", "## By catalog subject", "", "| Subject | Items |", "|---|---|"] + [f"| {k} | {v} |" for k, v in subj.most_common()]
    L += ["", "## All tags", "", "| Tag | Items |", "|---|---|"] + [f"| {k} | {v} |" for k, v in tagc.most_common()]
    L += ["", f"## New since the catalog ({len(new)})", "", "| Year | Title | Author | Tags |", "|---|---|---|---|"]
    L += [f"| {i['year']} | {i['title'][:70]} | {', '.join(i['authors'])[:30]} | {', '.join(i['tags'])[:40]} |" for i in new]
    io.open(os.path.join(META, "INVENTORY-LIVE.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    print(f"items {n} - pdf {withpdf} (on disk {on_disk}) - new {len(new)} - spine-keyed {len(keyed)} - story-side {len(story)} - drop folder {len(drops)}")
    print("spine:", dict(spc))
    print("0N_ tags:", {k: v for k, v in tagc.items() if re.match(r"^0\d", k)})


if __name__ == "__main__":
    main()
