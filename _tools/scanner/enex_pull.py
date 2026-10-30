"""enex_pull.py — 10/30 (BOLO 169): read a big Evernote export (.enex) in one streaming pass, without loading it all.

Usage (Python 3.11):  python -X utf8 enex_pull.py <file.enex> <out dir> <tag> [<tag> ...]
Writes, under <out dir>:
  all-notes-index.csv        every note: created, updated, title, tags, word count, attachment count
  keyword-hits.md            notes (any tag) whose text or title hits the OXO sequel words, with the matching line
  <tag slug>/NNNN-title.md   the full plain text of every note carrying that tag, plus index.md
Attachments are not written (the export is 360 MB mostly of pictures); the count is in the index.
"""
import csv
import html
import html.entities
import os
import re
import sys
import xml.etree.ElementTree as ET

NL = chr(10)
KEYS = re.compile(r"\b(tori|tyson|ariel|troupe|ivy|shane|flynn|riley|colson|lucina|sabine|oxo|over[ .]?exit|outliers?|red hills|caliphate|mass effect|sequel|crew|ship|band back|super.?(soldier|agent)|bourne|arbiter|dcus)\b", re.I)


def plain(enml):
    t = re.sub(r"<(br|/div|/p|/li|/tr|/h\d)[^>]*>", NL, enml or "", flags=re.I)
    t = re.sub(r"<li[^>]*>", "- ", t, flags=re.I)
    t = re.sub(r"<en-media[^>]*>", "[attachment]", t, flags=re.I)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t).replace(chr(160), " ")
    return re.sub(r"[ \t]*" + NL + r"(\s*" + NL + r")+", NL + NL, t).strip()


def slug(s, n=60):
    return re.sub(r"[^A-Za-z0-9._ -]+", "", s or "").strip().replace(" ", "-")[:n] or "untitled"


def stamp(s):
    return (s or "")[:8] and "%s-%s-%s" % (s[:4], s[4:6], s[6:8])


def main():
    src, out, tags = sys.argv[1], sys.argv[2], [t.lower() for t in sys.argv[3:]]
    os.makedirs(out, exist_ok=True)
    tagdirs = {}
    for t in tags:
        d = os.path.join(out, slug(t))
        os.makedirs(d, exist_ok=True)
        tagdirs[t] = (d, [])
    csvf = open(os.path.join(out, "all-notes-index.csv"), "w", encoding="utf-8", newline="")
    cw = csv.writer(csvf)
    cw.writerow(["created", "updated", "title", "tags", "words", "attachments"])
    hits = []
    n = 0
    parser = ET.XMLParser()   # ENEX bodies use HTML entities (&nbsp; and friends) that plain XML does not define
    for name, cp in html.entities.name2codepoint.items():
        if name not in ("lt", "gt", "amp", "quot", "apos"):
            parser.entity[name] = chr(cp)
    ctx = ET.iterparse(src, events=("end",), parser=parser)
    for ev, el in ctx:
        if el.tag != "note":
            continue
        n += 1
        title = el.findtext("title") or ""
        tg = [t.text or "" for t in el.findall("tag")]
        created, updated = stamp(el.findtext("created")), stamp(el.findtext("updated"))
        body = plain(el.findtext("content"))
        natt = len(el.findall("resource"))
        cw.writerow([created, updated, title, "; ".join(tg), len(body.split()), natt])
        low = [t.lower() for t in tg]
        for t, (d, idx) in tagdirs.items():
            if t in low:
                name = "%04d-%s.md" % (n, slug(title))
                with open(os.path.join(d, name), "w", encoding="utf-8") as f:
                    f.write("# %s%s%screated: %s · updated: %s · tags: %s · attachments: %d%s%s%s" % (title, NL, NL, created, updated, "; ".join(tg), natt, NL, NL, body + NL))
                idx.append((created, title, len(body.split()), natt, name))
        m = KEYS.search(title + NL + body)
        if m and not any(t in low for t in tagdirs):
            line = next((l for l in (title + NL + body).split(NL) if KEYS.search(l)), "")
            hits.append((created, title, "; ".join(tg), m.group(0).lower(), line.strip()[:160]))
        el.clear()
    csvf.close()
    for t, (d, idx) in tagdirs.items():
        idx.sort()
        with open(os.path.join(d, "index.md"), "w", encoding="utf-8") as f:
            f.write("# Evernote export: tag \"%s\" (%d notes)%s%s" % (t, len(idx), NL, NL))
            for created, title, w, a, name in idx:
                f.write("- %s · %s · %d words · %d attachments · [%s](%s)%s" % (created, title or "(untitled)", w, a, name, name, NL))
    with open(os.path.join(out, "keyword-hits.md"), "w", encoding="utf-8") as f:
        f.write("# Notes outside the exported tags that hit the OXO words (%d)%s%s" % (len(hits), NL, NL))
        for h in sorted(hits):
            f.write("- %s · %s · [%s] · %s: %s%s" % (h + (NL,)))
    print(n, "notes read;", {t: len(v[1]) for t, v in tagdirs.items()}, "tag notes;", len(hits), "other keyword hits")


main()
