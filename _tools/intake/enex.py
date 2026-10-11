"""The Evernote lane: turn an ENEX export into intake notes the batches can cut (BOLO 107, Chief 10/11: "go Evernote and voice memos").

Usage:
  python _tools/intake/enex.py convert   # every .enex in _PRIVATE/intake/evernote/ -> notes/<year>/*.md + media/
  python _tools/intake/enex.py memos     # faster-whisper on the 3090: every voice memo -> its note gets the transcript
  python _tools/intake/enex.py index     # write the evernote rows into inventory.json (memo notes join once transcribed)

Zero tokens. The export carries bare HTML entities that break XML parsers, so the notes are cut by regex.
Each note becomes one markdown file: title, created date, tags, the text, and a line per attachment
([image: media/…] · [voice memo: media/…] · [pdf: media/…]). Notes that hold a voice memo stay out of the index
until `memos` writes the transcript into them. Exact copies (same text) are marked dupe_of. The script judges nothing.
"""
import base64, glob, hashlib, html, io, json, os, re, sys

sys.path.insert(0, os.path.dirname(__file__))
from inventory import ROOT, LINEAGE  # noqa: E402

LANE = os.path.join(ROOT, "_PRIVATE", "intake", "evernote")
NOTES, MEDIA = os.path.join(LANE, "notes"), os.path.join(LANE, "media")
MANIFEST = os.path.join(LANE, "manifest.json")
EXT = {"image/jpeg": "jpg", "image/jpg": "jpg", "image/png": "png", "image/gif": "gif", "audio/amr": "amr",
       "audio/wav": "wav", "application/pdf": "pdf"}
KIND = {"image": "image", "audio": "voice memo", "application/pdf": "pdf"}


def one(tag, s):
    m = re.search(r"<%s>(.*?)</%s>" % (tag, tag), s, re.S)
    return html.unescape(m.group(1)).strip() if m else ""


def enml_text(enml, media):
    s = re.sub(r"<!\[CDATA\[|\]\]>", "", enml)
    s = re.sub(r"<\?xml.*?\?>|<!DOCTYPE.*?>", "", s, flags=re.S)
    s = re.sub(r'<en-media[^>]*hash="([0-9a-f]+)"[^>]*/?>', lambda m: "\n%s\n" % media.get(m.group(1), "[attachment]"), s)
    s = re.sub(r"<en-todo[^>]*checked=\"true\"[^>]*/?>", "[x] ", s)
    s = re.sub(r"<en-todo[^>]*/?>", "[ ] ", s)
    s = re.sub(r"<li[^>]*>", "\n- ", s)
    s = re.sub(r"<(br|/div|/p|/h\d|/tr|/li)[^>]*>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    return re.sub(r"\n\s*\n\s*\n+", "\n\n", s).strip()


def slug(t):
    return (re.sub(r"[^\w\- ]+", "", t).strip()[:60] or "untitled").replace(" ", "_")


def convert():
    os.makedirs(NOTES, exist_ok=True)
    os.makedirs(MEDIA, exist_ok=True)
    rows, n = [], 0
    for f in sorted(glob.glob(os.path.join(LANE, "*.enex"))):
        src = os.path.basename(f)
        data = io.open(f, encoding="utf-8", errors="replace").read()
        for s in re.findall(r"<note>(.*?)</note>", data, re.S):
            n += 1
            nid = "EN%04d" % n
            created = one("created", s)
            year = created[:4] if re.match(r"20\d\d", created) else "????"
            media, files = {}, []
            for k, r in enumerate(re.findall(r"<resource>(.*?)</resource>", s, re.S), 1):
                mime = one("mime", r)
                b64 = re.search(r"<data[^>]*>(.*?)</data>", r, re.S)
                if not b64:
                    continue
                raw = base64.b64decode(re.sub(r"\s+", "", b64.group(1)))
                name = "%s_%02d.%s" % (nid, k, EXT.get(mime, "bin"))
                io.open(os.path.join(MEDIA, name), "wb").write(raw)
                kind = KIND.get(mime, KIND.get(mime.split("/")[0], "attachment"))
                tag = "[%s: media/%s]" % (kind, name)
                media[hashlib.md5(raw).hexdigest()] = tag
                files.append({"file": name, "kind": kind})
            title = one("title", s) or "untitled"
            tags = [html.unescape(t).strip() for t in re.findall(r"<tag>(.*?)</tag>", s, re.S)]
            text = enml_text(one("content", s) if "<content>" in s else "", media)
            for m in media.values():                     # attachments the body never placed still get a line
                if m not in text:
                    text += "\n" + m
            head = "# %s\n\ncreated: %s · tags: %s · source: %s\n\n" % (title, created or "?", ", ".join(tags) or "none", src)
            path = os.path.join(NOTES, year, "%s %s.md" % (nid, slug(title)))
            os.makedirs(os.path.dirname(path), exist_ok=True)
            io.open(path, "w", encoding="utf-8").write(head + text + "\n")
            plain = re.sub(r"\[(image|voice memo|pdf|attachment)[^\]]*\]", "", text).strip()
            rows.append({"id": nid, "path": os.path.relpath(path, ROOT).replace("\\", "/"), "title": title, "year": year,
                         "tags": tags, "chars": len(head + text), "text_chars": len(plain), "files": files,
                         "audio": [x["file"] for x in files if x["kind"] == "voice memo"], "transcribed": False,
                         "hash": hashlib.md5(re.sub(r"\s+", " ", plain).lower().encode()).hexdigest()[:16]})
    json.dump(rows, io.open(MANIFEST, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    aud = sum(1 for r in rows if r["audio"])
    print("CONVERT: %d notes · %d media files · %d notes hold a voice memo -> %s" % (
        len(rows), sum(len(r["files"]) for r in rows), aud, os.path.relpath(NOTES, ROOT)))


def memos():
    import subprocess, tempfile
    from faster_whisper import WhisperModel
    rows = json.load(io.open(MANIFEST, encoding="utf-8"))
    todo = [r for r in rows if r["audio"] and not r["transcribed"]]
    model = WhisperModel("distil-large-v3", device="cuda", compute_type="float16")
    tmp = tempfile.mkdtemp()
    done = 0
    for r in todo:
        parts = []
        for a in r["audio"]:
            wav = os.path.join(tmp, a + ".wav")
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", os.path.join(MEDIA, a), "-ar", "16000", "-ac", "1", wav], check=False)
            if not os.path.exists(wav):
                parts.append((a, "[transcription failed: ffmpeg could not read the file]"))
                continue
            segs, _ = model.transcribe(wav, language="en", vad_filter=True)
            parts.append((a, " ".join(x.text.strip() for x in segs).strip() or "[no speech heard]"))
            os.remove(wav)
        p = os.path.join(ROOT, r["path"])
        body = io.open(p, encoding="utf-8").read()
        for a, t in parts:
            body = body.replace("[voice memo: media/%s]" % a, "[voice memo: media/%s]\nTRANSCRIPT (whisper, machine-made): %s" % (a, t))
        io.open(p, "w", encoding="utf-8").write(body)
        r["transcribed"] = True
        r["chars"] = len(body)
        r["text_chars"] += sum(len(t) for _, t in parts)
        done += 1
        if done % 25 == 0:
            json.dump(rows, io.open(MANIFEST, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
            print("MEMOS: %d/%d notes" % (done, len(todo)), flush=True)
    json.dump(rows, io.open(MANIFEST, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("MEMOS: done · %d notes transcribed" % done)


def index():
    rows = json.load(io.open(MANIFEST, encoding="utf-8"))
    invp = os.path.join(ROOT, "_PRIVATE", "intake", "inventory.json")
    inv = json.load(io.open(invp, encoding="utf-8"))
    inv["notes"] = [r for r in inv["notes"] if r["vault"] != "evernote"]
    first, added, held = {}, 0, 0
    for r in rows:
        if r["audio"] and not r["transcribed"]:
            held += 1
            continue
        body = io.open(os.path.join(ROOT, r["path"]), encoding="utf-8").read()
        rec = {"vault": "evernote", "path": r["path"], "chars": r["chars"], "year": r["year"], "hash": r["hash"],
               "empty": r["text_chars"] < 20 and not r["files"], "title": r["title"], "book": False,
               "lineage": [w for w in LINEAGE if re.search(r"\b%s\b" % re.escape(w), body, re.I)]}
        if not rec["empty"] and r["text_chars"] >= 20:
            if r["hash"] in first:
                rec["dupe_of"] = first[r["hash"]]
            else:
                first[r["hash"]] = r["path"]
        inv["notes"].append(rec)
        added += 1
    json.dump(inv, io.open(invp, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    ev = [r for r in inv["notes"] if r["vault"] == "evernote"]
    print("INDEX: %d evernote rows · %d empty · %d exact copies · %d memo notes held for transcripts" % (
        added, sum(r["empty"] for r in ev), sum(1 for r in ev if r.get("dupe_of")), held))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    {"convert": convert, "memos": memos, "index": index}[sys.argv[1]]()
