"""evernote_pull.py — 10/30 (Chief: "pull the Mx86 stuff ... we also have it in Evernote"): export notes by tag from a COPY of the
Evernote 6 database (read-only), as plain-text Markdown plus an index. The live database is never opened here.

Usage (Python 3.11):  python -X utf8 evernote_pull.py <copy of x.exb> <out dir> <tag> [<tag> ...]
  e.g. ... ever.exb _PRIVATE/evernote "mx86" "Over Exit Out"
Each tag gets <out dir>/<tag slug>/NNNNN-title.md and index.md. Text is Evernote's own search text (plain; no images or layout).
Evernote's search index does not use note ids: each row is "title NUL body", so a note is matched to its text by TITLE. Notes that
share a title are marked AMBIGUOUS and show every candidate text. Attachments (images, audio) are saved beside their note.
Dates are the database's day numbers (counted from 0001-01-01).
"""
import datetime
import os
import re
import sqlite3
import sys

NUL = chr(0)
NL = chr(10)


def day(n):
    try:
        return datetime.date.fromordinal(int(float(n))).strftime("%Y-%m-%d")
    except (TypeError, ValueError):
        return ""


def norm(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def slug(s, n=60):
    return re.sub(r"[^A-Za-z0-9._ -]+", "", s).strip().replace(" ", "-")[:n] or "untitled"


def split(t):
    head, _, body = t.partition(NUL)
    return head, body


def main():
    db, out, tags = sys.argv[1], sys.argv[2], sys.argv[3:]
    con = sqlite3.connect("file:" + db.replace(chr(92), "/") + "?mode=ro", uri=True)
    con.create_collation("NOCASEUTF8", lambda a, b: (a.lower() > b.lower()) - (a.lower() < b.lower()))
    cur = con.cursor()
    nb = {r[0]: r[1] for r in cur.execute("select uid,name from notebook_attr")}
    index = {}
    for docid, raw in cur.execute("select docid,c0text from fts_content"):
        t = raw.decode("utf-8", "replace") if isinstance(raw, bytes) else (raw or "")
        index.setdefault(norm(split(t)[0])[:40], []).append(t)
    ext = {"image/jpeg": ".jpg", "image/png": ".png", "audio/amr": ".amr", "application/pdf": ".pdf", "image/gif": ".gif"}
    for tag in tags:
        d = os.path.join(out, slug(tag))
        os.makedirs(d, exist_ok=True)
        rows = []
        for uid, title, tg, nbid, created, updated, deleted in cur.execute(
                "select uid,title,tags,notebook_uid,date_created,date_updated,date_deleted from note_attr"):
            toks = [t.strip().lower() for t in (tg or "").split(",")]
            if tag.lower() in toks and not deleted:
                rows.append((created or 0, uid, title or "", tg, nbid, created, updated))
        rows.sort()
        idx = ["# Evernote export: tag \"%s\" (%d notes)" % (tag, len(rows)), "", "Sorted by created date. Plain text from Evernote's search index, matched to notes by title.", ""]
        for _, uid, title, tg, nbid, created, updated in rows:
            cands = [t2 for t2 in index.get(norm(title)[:40], []) if norm(split(t2)[0]) == norm(title)]
            if len(cands) == 1:
                flag, txt = "", split(cands[0])[1]
            elif len(cands) > 1:
                flag = "AMBIGUOUS: %d notes share this title; the texts below may belong to the other notes." % len(cands) + NL + NL
                txt = (NL + NL + "---" + NL + NL).join(split(t2)[1] for t2 in cands)
            else:
                flag, txt = "No matching text found in the search index (title not found)." + NL + NL, ""
            txt = flag + txt.replace(NUL, NL).strip()
            name = "%05d-%s.md" % (uid, slug(title))
            with open(os.path.join(d, name), "w", encoding="utf-8") as f:
                f.write("# %s%s%screated: %s · updated: %s · notebook: %s · tags: %s%s%s%s" % (
                    title, NL, NL, day(created), day(updated), nb.get(nbid, ""), tg, NL, NL, txt + NL))
            for ruid, mime, fname in cur.execute("select uid,mime,file_name from resource_attr where note=?", (uid,)).fetchall():
                blob = cur.execute("select data from resources where uid=?", (ruid,)).fetchone()
                if blob and blob[0]:
                    an = "%05d-att%s%s" % (uid, ruid, os.path.splitext(fname)[1] if fname else ext.get(mime, ".bin"))
                    open(os.path.join(d, an), "wb").write(blob[0])
                    with open(os.path.join(d, name), "a", encoding="utf-8") as f:
                        f.write(NL + "Attachment: [%s](%s) (%s)" % (an, an, mime) + NL)
            idx.append("- %s · %s · %d words%s · [%s](%s)" % (day(created), title or "(untitled)", len(txt.split()), " · AMBIGUOUS" if flag.startswith("AMB") else "", name, name))
        with open(os.path.join(d, "index.md"), "w", encoding="utf-8") as f:
            f.write(NL.join(idx) + NL)
        print(tag, len(rows), "notes ->", d)


main()
