# -*- coding: utf-8 -*-
"""The review desk's engine (BOLO 125, Chief 11/4 "Go."). Chief highlights a Command doc in the Console's Review pane,
attaches comments, suggested changes and voice notes, and sends it. One review = one folder:
    _PRIVATE/reviews/<doc-slug>-<YYYYMMDD-HHMMSS>/review.json  (+ the audio files it names)
The Console (_tools/console/console.py) calls docs() / read_doc() / save() for its /review/* routes.
`command review` (_tools/cmdtui/review.go) and any session read the folder through this CLI:
    python _tools/reviewdesk/reviewdesk.py list [--all] [--json]       the reviews, newest first (open ones only unless --all)
    python _tools/reviewdesk/reviewdesk.py show <id|N|latest> [--json] one review: every item with its quote and source lines
    python _tools/reviewdesk/reviewdesk.py docs [--json]               the picker's doc list
    python _tools/reviewdesk/reviewdesk.py done <id> [--dry-run]       mark a review read (status: done) once a session has acted on it
REVIEW_DIR in the environment moves the reviews folder (the test uses it).
"""
import base64, hashlib, json, os, re, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
PINNED = ["SOP.md", "STATE.md", "BOLO.md", "PROJECTS.md", "DOCTRINE-0-INVARIANTS.md"]
CANON = os.path.join("ShroomsQ", "_CANON")
AUDIO = {"audio/webm": ".webm", "audio/ogg": ".ogg", "audio/mp4": ".m4a", "audio/mpeg": ".mp3", "audio/wav": ".wav", "audio/x-wav": ".wav"}
MAX_AUDIO = 25 << 20   # one voice note, decoded


def reviews_dir():
    return os.environ.get("REVIEW_DIR") or os.path.join(ROOT, "_PRIVATE", "reviews")


def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, "/")


def safe_doc(path):
    """a repo-relative .md path inside the repo, or None (no traversal, no other file types)"""
    if not isinstance(path, str) or not path.strip():
        return None
    p = os.path.abspath(os.path.join(ROOT, path.strip().replace("\\", "/").lstrip("/")))
    if not p.startswith(ROOT + os.sep) or not p.lower().endswith(".md") or not os.path.isfile(p):
        return None
    return p


def title_of(p):
    try:
        with open(p, encoding="utf-8", errors="replace") as fh:
            for _ in range(12):
                line = fh.readline()
                if not line:
                    break
                m = re.match(r"\s*#{1,3}\s+(.+)", line)
                if m:
                    return re.sub(r"[*_`]", "", m.group(1)).strip()[:90]
    except OSError:
        pass
    return os.path.basename(p)[:-3]


def docs():
    """the picker: the pinned trunk docs, the other root docs, then every _CANON doc"""
    out, seen = [], set()

    def add(p, group):
        r = rel(p)
        if r not in seen and os.path.isfile(p):
            seen.add(r)
            out.append({"path": r, "title": title_of(p) if group != "canon" else os.path.basename(p)[:-3], "group": group})
    for n in PINNED:
        add(os.path.join(ROOT, n), "trunk")
    for n in sorted(os.listdir(ROOT)):
        if n.lower().endswith(".md"):
            add(os.path.join(ROOT, n), "root")
    base = os.path.join(ROOT, CANON)
    for d, subs, files in os.walk(base):
        subs.sort()
        for n in sorted(files):
            if n.lower().endswith(".md"):
                add(os.path.join(d, n), "canon")
    return out


def read_doc(path):
    p = safe_doc(path)
    if not p:
        return None
    with open(p, "rb") as fh:
        b = fh.read()
    text = b.decode("utf-8", errors="replace").replace("\r\n", "\n")
    return {"path": rel(p), "title": title_of(p), "text": text, "lines": text.count("\n") + 1,
            "sha1": hashlib.sha1(b).hexdigest(), "bytes": len(b)}


def slug(path):
    s = re.sub(r"[^a-z0-9]+", "-", path.lower()[:-3] if path.lower().endswith(".md") else path.lower()).strip("-")
    return s[-60:].strip("-") or "doc"


def _audio(blob, name, folder, errors):
    """{mime, data: base64 or data: URL} -> the file name written, or None"""
    if not blob:
        return None
    if not isinstance(blob, dict):
        errors.append(name + ": audio is {mime, data}")
        return None
    mime = str(blob.get("mime", "")).split(";")[0].strip().lower()
    data = str(blob.get("data", ""))
    if data.startswith("data:"):
        head, _, data = data.partition(",")
        mime = mime or head[5:].split(";")[0].lower()
    ext = AUDIO.get(mime)
    if not ext:
        errors.append("%s: audio type %r is not one of %s" % (name, mime, ", ".join(sorted(AUDIO))))
        return None
    try:
        raw = base64.b64decode(data, validate=True)
    except Exception:
        errors.append(name + ": audio is not base64")
        return None
    if not raw or len(raw) > MAX_AUDIO:
        errors.append(name + ": audio is empty or over 25 MB")
        return None
    fn = name + ext
    with open(os.path.join(folder, fn), "wb") as fh:
        fh.write(raw)
    return fn


def save(body):
    """POST /review/send -> (http code, reply). Writes review.json and the audio beside it."""
    if not isinstance(body, dict):
        return 400, {"ok": False, "errors": ["a review is an object"]}
    doc = read_doc(body.get("doc", ""))
    if not doc:
        return 400, {"ok": False, "errors": ["doc must be a .md path inside the repo"]}
    items_in = body.get("items") or []
    summary = str(body.get("summary") or "").strip()
    if not isinstance(items_in, list) or not (items_in or summary or body.get("voice")):
        return 400, {"ok": False, "errors": ["nothing to send: no items, no note, no voice note"]}
    lines = doc["text"].split("\n")
    stamp = time.strftime("%Y%m%d-%H%M%S")
    rid = "%s-%s" % (slug(doc["path"]), stamp)
    folder, k = os.path.join(reviews_dir(), rid), 2
    while os.path.exists(folder):
        rid = "%s-%s-%d" % (slug(doc["path"]), stamp, k)
        folder, k = os.path.join(reviews_dir(), rid), k + 1
    os.makedirs(folder)
    errors, items = [], []
    for i, it in enumerate(items_in[:500], 1):
        if not isinstance(it, dict):
            errors.append("item %d is not an object" % i)
            continue
        kind = "suggestion" if it.get("kind") == "suggestion" else "comment"
        try:
            l0 = max(1, int((it.get("line") or [1])[0]))
            l1 = max(l0, int((it.get("line") or [l0, l0])[-1]))
        except (TypeError, ValueError):
            l0 = l1 = 1
        row = {"n": len(items) + 1, "kind": kind, "quote": str(it.get("quote") or "")[:20000],
               "line": [l0, l1], "prefix": str(it.get("prefix") or "")[:200], "suffix": str(it.get("suffix") or "")[:200],
               "text": str(it.get("text") or "").strip()[:20000]}
        if kind == "suggestion":
            row["replace"] = str(it.get("replace") if it.get("replace") is not None else "")[:20000]
        row["source"] = "\n".join(lines[l0 - 1:l1])[:40000]   # the raw markdown the quote sits in, for the edit
        row["voice"] = _audio(it.get("voice"), "voice-%02d" % row["n"], folder, errors)
        items.append(row)
    review = {"review": 1, "id": rid, "status": "open", "created": time.strftime("%Y-%m-%d %H:%M:%S"),
              "doc": doc["path"], "doc_title": doc["title"], "doc_sha1": doc["sha1"],
              "doc_changed_since_open": bool(body.get("sha1")) and body.get("sha1") != doc["sha1"],
              "summary": summary[:20000], "voice": _audio(body.get("voice"), "voice-00", folder, errors),
              "counts": {"comments": sum(1 for x in items if x["kind"] == "comment"),
                         "suggestions": sum(1 for x in items if x["kind"] == "suggestion"),
                         "voice": sum(1 for x in items if x["voice"]) + (1 if body.get("voice") else 0)},
              "items": items, "errors": errors, "test": bool(body.get("test"))}
    review["counts"]["voice"] = sum(1 for x in items if x["voice"]) + (1 if review["voice"] else 0)
    tmp = os.path.join(folder, "review.json.tmp")
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(review, fh, ensure_ascii=False, indent=1)
    os.replace(tmp, os.path.join(folder, "review.json"))
    return 200, {"ok": True, "id": rid, "dir": rel(folder) if folder.startswith(ROOT) else folder,
                 "counts": review["counts"], "errors": errors}


def load(rid):
    f = os.path.join(reviews_dir(), rid, "review.json")
    try:
        with open(f, encoding="utf-8") as fh:
            r = json.load(fh)
        r["dir"] = os.path.dirname(f)
        return r
    except (OSError, ValueError):
        return None


def all_reviews(include_done=True):
    d = reviews_dir()
    out = []
    for n in sorted(os.listdir(d), reverse=True) if os.path.isdir(d) else []:
        r = load(n)
        if r and (include_done or r.get("status") != "done"):
            out.append(r)
    out.sort(key=lambda r: r.get("created", ""), reverse=True)
    return out


def brief(r):
    return {"id": r["id"], "doc": r["doc"], "created": r["created"], "status": r.get("status", "open"),
            "counts": r.get("counts", {}), "summary": (r.get("summary") or "")[:160], "dir": r["dir"], "test": r.get("test", False)}


def pick(key):
    rs = all_reviews()
    if key in ("latest", "last") and rs:
        return rs[0]
    if key.isdigit() and 1 <= int(key) <= len(rs):
        return rs[int(key) - 1]
    return load(key) if re.match(r"^[a-z0-9-]{1,90}$", key or "") else None


def show_text(r):
    c = r.get("counts", {})
    out = ["%s  [%s]" % (r["id"], r.get("status", "open")),
           "  doc   %s%s" % (r["doc"], "  (changed since Chief opened it)" if r.get("doc_changed_since_open") else ""),
           "  sent  %s  ·  %d comment(s), %d suggestion(s), %d voice note(s)" % (r["created"], c.get("comments", 0), c.get("suggestions", 0), c.get("voice", 0)),
           "  dir   %s" % r["dir"]]
    if r.get("summary") or r.get("voice"):
        out.append("  note  %s%s" % (r.get("summary") or "", ("  [voice: %s]" % r["voice"]) if r.get("voice") else ""))
    for it in r.get("items", []):
        out.append("")
        out.append("  %d. %s · line %s" % (it["n"], it["kind"].upper(), it["line"][0] if it["line"][0] == it["line"][1] else "%d-%d" % tuple(it["line"])))
        out.append("     quote   " + it["quote"].replace("\n", " ")[:300])
        if it["kind"] == "suggestion":
            out.append("     replace " + it.get("replace", "").replace("\n", " ")[:300])
        if it.get("text"):
            out.append("     note    " + it["text"].replace("\n", " ")[:600])
        if it.get("voice"):
            out.append("     voice   " + os.path.join(r["dir"], it["voice"]))
    return "\n".join(out)


def main(argv):
    js = "--json" in argv
    args = [a for a in argv if not a.startswith("--")]
    verb = args[0] if args else "list"
    if verb == "list":
        rs = [brief(r) for r in all_reviews(include_done="--all" in argv)]
        if js:
            print(json.dumps({"dir": reviews_dir(), "reviews": rs}, ensure_ascii=False, indent=1))
        elif not rs:
            print("no open reviews in " + reviews_dir())
        else:
            for i, r in enumerate(rs, 1):
                c = r["counts"]
                print("%2d  %-44s %s  %dc %ds %dv  %s" % (i, r["id"][:44], r["status"][:4], c.get("comments", 0), c.get("suggestions", 0), c.get("voice", 0), r["summary"][:50]))
        return 0
    if verb == "show":
        r = pick(args[1] if len(args) > 1 else "latest")
        if not r:
            print(json.dumps({"ok": False, "error": "no such review"}) if js else "no such review")
            return 1
        print(json.dumps(r, ensure_ascii=False, indent=1) if js else show_text(r))
        return 0
    if verb == "docs":
        ds = docs()
        if js:
            print(json.dumps({"docs": ds}, ensure_ascii=False, indent=1))
        else:
            for d in ds:
                print("%-6s %s" % (d["group"], d["path"]))
        return 0
    if verb == "done":
        r = pick(args[1]) if len(args) > 1 else None
        if not r:
            print("no such review")
            return 1
        if "--dry-run" in argv:
            print("would mark %s done" % r["id"])
            return 0
        f = os.path.join(r["dir"], "review.json")
        r.pop("dir", None)
        r["status"], r["done"] = "done", time.strftime("%Y-%m-%d %H:%M:%S")
        with open(f, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(r, fh, ensure_ascii=False, indent=1)
        print(json.dumps({"ok": True, "id": r["id"], "status": "done"}) if js else "marked %s done" % r["id"])
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
