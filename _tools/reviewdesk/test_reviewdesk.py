# -*- coding: utf-8 -*-
"""The review desk's round-trip test (BOLO 125). One review (a comment, a suggestion, two tiny audio blobs) goes in
through POST /review/send and comes back out through the folder, the /review/list route and the CLI.
    python -X utf8 _tools/reviewdesk/test_reviewdesk.py          the Console's own handler on a spare port, REVIEW_DIR in a temp folder
    python -X utf8 _tools/reviewdesk/test_reviewdesk.py --live   the running Console on :8795 (writes to _PRIVATE/reviews, then deletes its test review)
Exit 0 and "PASS" when every check holds.
"""
import base64, importlib.util, json, os, shutil, subprocess, sys, tempfile, threading, urllib.error, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
LIVE = "--live" in sys.argv
AUDIO_A = b"\x1aE\xdf\xa3\x01\x00\x00\x00test-voice-item-one"   # an EBML magic + bytes: the route stores it byte for byte
AUDIO_B = b"\x1aE\xdf\xa3\x01\x00\x00\x00test-voice-overall"
FAILS = []


def check(cond, what):
    print(("  ok    " if cond else "  FAIL  ") + what)
    if not cond:
        FAILS.append(what)


def call(base, path, body=None):
    req = urllib.request.Request(base + path, data=None if body is None else json.dumps(body).encode("utf-8"),
                                 headers={"Content-Type": "application/json"}, method="GET" if body is None else "POST")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode("utf-8") or "{}")


def main():
    tmp = None
    if LIVE:
        base = "http://127.0.0.1:8795"
        rdir = os.path.join(ROOT, "_PRIVATE", "reviews")
    else:
        tmp = tempfile.mkdtemp(prefix="reviewdesk-test-")
        os.environ["REVIEW_DIR"] = rdir = tmp
        spec = importlib.util.spec_from_file_location("console_under_test", os.path.join(ROOT, "_tools", "console", "console.py"))
        con = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(con)
        srv = con.S(("127.0.0.1", 0), con.H)
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        base = "http://127.0.0.1:%d" % srv.server_address[1]
    print("review desk round trip · %s · reviews in %s" % (base, rdir))

    code, d = call(base, "/review/docs")
    paths = [x["path"] for x in d.get("docs", [])]
    check(code == 200 and paths[:3] == ["SOP.md", "STATE.md", "BOLO.md"], "GET /review/docs lists the trunk first (%d docs)" % len(paths))
    check(any(p.startswith("ShroomsQ/_CANON/") for p in paths), "the picker carries the _CANON docs")

    code, doc = call(base, "/review/doc?path=SOP.md")
    check(code == 200 and doc.get("lines", 0) > 10 and len(doc.get("sha1", "")) == 40, "GET /review/doc?path=SOP.md returns the text + sha1")
    for bad in ("../../Windows/win.ini", "_tools/console/console.py", "nope-not-here.md"):
        c, _ = call(base, "/review/doc?path=" + urllib.request.quote(bad))
        check(c == 404, "refuses %s (%d)" % (bad, c))

    lines = doc["text"].split("\n")
    n = next(i for i, l in enumerate(lines) if len(l.strip()) > 30) + 1
    quote = lines[n - 1].strip()[:24]
    body = {"doc": "SOP.md", "sha1": doc["sha1"], "summary": "test review: the overall note", "test": True,
            "voice": {"mime": "audio/webm", "data": base64.b64encode(AUDIO_B).decode()},
            "items": [
                {"kind": "comment", "quote": quote, "line": [n, n], "prefix": "", "suffix": "", "text": "yo what is this",
                 "voice": {"mime": "audio/webm;codecs=opus", "data": base64.b64encode(AUDIO_A).decode()}},
                {"kind": "suggestion", "quote": quote, "line": [n, n], "text": "say it plainer", "replace": "PLAINER WORDS"},
                {"kind": "comment", "quote": "x", "line": [1, 1], "text": "bad audio type",
                 "voice": {"mime": "application/x-msdownload", "data": base64.b64encode(b"MZ").decode()}}]}
    code, r = call(base, "/review/send", body)
    check(code == 200 and r.get("ok"), "POST /review/send -> 200 ok (%s)" % r.get("id"))
    rid = r.get("id", "")
    folder = os.path.join(rdir, rid)
    try:
        check(rid.startswith("sop-") and os.path.isdir(folder), "the folder is <doc-slug>-<timestamp>: %s" % rid)
        check(any("not one of" in e for e in r.get("errors", [])), "a non-audio blob is refused and reported, not written")
        with open(os.path.join(folder, "review.json"), encoding="utf-8") as fh:
            rv = json.load(fh)
        it = rv["items"]
        check(rv["doc"] == "SOP.md" and rv["status"] == "open" and rv["doc_changed_since_open"] is False, "review.json: doc, status open, sha1 matches")
        check([x["kind"] for x in it] == ["comment", "suggestion", "comment"], "three items, kinds in order")
        check(it[0]["text"] == "yo what is this" and it[1]["replace"] == "PLAINER WORDS", "the comment text and the suggested change survive")
        check(it[0]["source"] == lines[n - 1], "each item carries its source markdown line (line %d)" % n)
        check(it[0]["voice"] == "voice-01.webm" and rv["voice"] == "voice-00.webm" and it[2]["voice"] is None, "voice files named, the bad one dropped")
        with open(os.path.join(folder, "voice-01.webm"), "rb") as fh:
            a = fh.read()
        with open(os.path.join(folder, "voice-00.webm"), "rb") as fh:
            b = fh.read()
        check(a == AUDIO_A and b == AUDIO_B, "both audio blobs written byte for byte")
        check(rv["counts"] == {"comments": 2, "suggestions": 1, "voice": 2}, "counts: %s" % rv["counts"])
        check(sorted(os.listdir(folder)) == ["review.json", "voice-00.webm", "voice-01.webm"], "nothing else in the folder")

        code, lst = call(base, "/review/list")
        check(code == 200 and any(x["id"] == rid for x in lst.get("reviews", [])), "GET /review/list shows it")
        env = dict(os.environ, REVIEW_DIR=rdir)
        cli = os.path.join(HERE, "reviewdesk.py")
        out = subprocess.run([sys.executable, "-X", "utf8", cli, "show", rid, "--json"], capture_output=True, text=True, encoding="utf-8", env=env)
        shown = json.loads(out.stdout)
        check(shown.get("id") == rid and len(shown.get("items", [])) == 3, "reviewdesk.py show <id> --json reads it back")
        out = subprocess.run([sys.executable, "-X", "utf8", cli, "done", rid, "--dry-run"], capture_output=True, text=True, encoding="utf-8", env=env)
        check("would mark" in out.stdout, "done --dry-run changes nothing")

        code, r2 = call(base, "/review/send", {"doc": "SOP.md", "items": []})
        check(code == 400, "an empty review is refused (%d)" % code)
        code, r3 = call(base, "/review/send", {"doc": "../outside.md", "items": [{"kind": "comment", "text": "x"}]})
        check(code == 400, "a doc outside the repo is refused (%d)" % code)
    finally:
        if LIVE and rid and os.path.isdir(folder) and json.load(open(os.path.join(folder, "review.json"), encoding="utf-8")).get("test"):
            shutil.rmtree(folder)
            print("  (removed the live test review %s)" % rid)
        if tmp:
            shutil.rmtree(tmp, ignore_errors=True)
    print("FAIL: %d check(s)" % len(FAILS) if FAILS else "PASS")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
