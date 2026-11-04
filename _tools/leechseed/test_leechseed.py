"""LEECHSEED character console tests (BOLO 176, 11/4).

    python -X utf8 _tools/leechseed/test_leechseed.py

1 extraction finds Tori and Anna (and Jebb's card stub)
2 their counts match the fill lists (anna-fill.md's round-2 tally; tori-fill.md's rows still waiting)
3 every filled field has a source
4 the JSON follows the contract BAY reads, and the files on disk are current
5 the routes answer (console.py's handler, served in-process on a free port; the live Console is not touched)
6 the display name stays out of the public files (read from _PRIVATE, never spelled here)
"""
import importlib.util
import json
import os
import re
import sys
import threading
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import extract  # noqa: E402

WORK = os.path.join(ROOT, "_tools", "bolostatus", "work", "176")
RECS = {r["id"]: r for r in extract.extract()}
FAILS = []


def check(name, ok, detail=""):
    print(("  ok    " if ok else "  FAIL  ") + name + ("" if ok else "  -> " + detail))
    if not ok:
        FAILS.append(name)


def t1_found():
    check("extraction finds Tori", "victoria_midnight" in RECS)
    check("extraction finds Anna", "anna_colson_conway" in RECS)
    check("Jebb is a card-only stub", RECS.get("jebb_midnight", {}).get("counts", {}).get("parked") == 0
          and all(f["layer"] == "card" for f in RECS.get("jebb_midnight", {}).get("fields", {}).values()))


def t2_counts():
    anna = RECS["anna_colson_conway"]["counts"]
    txt = extract.read(os.path.join(WORK, "anna-fill.md"))
    m = re.search(r"(\d+) of (\d+) layer fields filled, (\d+) parked", txt)
    check("anna-fill.md states a round-2 tally", bool(m))
    if m:
        f, total, p = map(int, m.groups())
        check("Anna filled = %d (fill list)" % f, anna["filled"] == f, str(anna))
        check("Anna parked = %d (fill list)" % p, anna["parked"] == p, str(anna))
        check("Anna fields = %d (fill list)" % total, len(RECS["anna_colson_conway"]["fields"]) == total,
              str(len(RECS["anna_colson_conway"]["fields"])))
    # Tori: the rows still waiting (low and NO SOURCE, not RULED, not high) are her parked fields
    rows = extract.fill_rows(os.path.join(WORK, "tori-fill.md"))
    waiting = [(n, r["layer"]) for r in rows for n in r["names"]
               if "high" not in r["conf"] and "RULED" not in r["conf"]]
    tori = RECS["victoria_midnight"]
    check("Tori parked = %d (fill list rows waiting)" % len(waiting), tori["counts"]["parked"] == len(waiting),
          str(tori["counts"]))
    fields = tori["fields"]

    def status(name, layer):
        f = fields.get("%s_%s" % (name, layer)) if layer == "L9" and name == "disclosure_posture" else fields.get(name)
        return f and f["status"]
    bad = [n for n, l in waiting if status(n, l) != "parked"]
    check("every waiting Tori row is parked in the record", not bad, ", ".join(bad))
    done = [(n, r["layer"]) for r in rows for n in r["names"] if "high" in r["conf"] or "RULED" in r["conf"]]
    bad = [n for n, l in done if status(n, l) not in ("filled", "held")]
    check("every high or RULED Tori row is filled in the record", not bad, ", ".join(bad))


def t3_sources():
    for cid, r in RECS.items():
        bad = [k for k, f in r["fields"].items() if f["status"] in ("filled", "held") and not str(f["source"] or "").strip()]
        check("%s: every filled field has a source" % cid, not bad, ", ".join(bad))


def t4_contract():
    for cid, r in RECS.items():
        check("%s: top-level keys" % cid, set(r) == {"id", "name", "node", "fields", "numbers", "gates", "counts"},
              str(sorted(r)))
        fk = {"layer", "value", "native_scale", "source", "confidence", "status"}
        bad = [k for k, f in r["fields"].items() if set(f) != fk or f["status"] not in ("filled", "parked", "held")]
        check("%s: every field has the six keys and a known status" % cid, not bad, ", ".join(bad[:5]))
        check("%s: gates" % cid, r["gates"].get("step1") in ("pass", "red") and r["gates"].get("step3") in ("pass", "fail")
              and set(r["gates"]) == {"step1", "step3"}, str(r["gates"]))
        check("%s: counts add up" % cid, set(r["counts"]) == {"filled", "parked"}
              and r["counts"]["filled"] + r["counts"]["parked"] == len(r["fields"]), str(r["counts"]))
        check("%s: numbers are integers that match their fields" % cid,
              all(isinstance(v, int) and not isinstance(v, bool) and r["fields"][k]["value"] == v
                  for k, v in r["numbers"].items()))
        p = os.path.join(extract.OUT, cid + ".json")
        disk = json.load(open(p, encoding="utf-8")) if os.path.isfile(p) else None
        check("%s: the file on disk is current (re-run extract.py if not)" % cid, disk == json.loads(json.dumps(r)))
    tori, anna = RECS["victoria_midnight"]["numbers"], RECS["anna_colson_conway"]["numbers"]
    check("Tori's stat inputs are in numbers", all(k in tori for k in (
        "WILL", "WOUND", "SOCIAL", "DRIVE", "projection_tendency", "shadow_density", "resistance_index", "shame_index",
        "armor_index")), str(sorted(tori)))
    check("Anna's numbers pass values", {k: anna.get(k) for k in ("CORE", "VITAL", "SOCIAL", "WILL", "WOUND", "DRIVE")}
          == {"CORE": 10, "VITAL": 10, "SOCIAL": 10, "WILL": 11, "WOUND": 0, "DRIVE": 10}, str(anna))
    check("Anna's L9 is held, not filled with values", RECS["anna_colson_conway"]["fields"].get("L9_EROS", {})
          .get("status") == "held")


def t5_routes():
    spec = importlib.util.spec_from_file_location("console_ut", os.path.join(ROOT, "_tools", "console", "console.py"))
    con = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(con)
    srv = con.S(("127.0.0.1", 0), con.H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = "http://127.0.0.1:%d" % srv.server_address[1]

    def get(path):
        try:
            with urllib.request.urlopen(base + path, timeout=60) as r:
                return r.status, r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            return e.code, e.read().decode("utf-8")
    try:
        code, body = get("/leechseed/characters")
        j = json.loads(body) if code == 200 else {}
        check("GET /leechseed/characters answers with Tori and Anna",
              code == 200 and {"victoria_midnight", "anna_colson_conway"} <= {c["id"] for c in j.get("characters", [])},
              str(code))
        code, body = get("/leechseed/char?id=victoria_midnight")
        j = json.loads(body) if code == 200 else {}
        check("GET /leechseed/char?id= answers with fields and the card", code == 200 and j.get("fields") and j.get("card_md"))
        check("GET /leechseed/char rejects a bad id", get("/leechseed/char?id=../x")[0] == 404)
        code, body = get("/leechseed/stats?char=victoria_midnight")
        j = json.loads(body) if code == 200 else {}
        honest = (j.get("built") is False and j.get("error") == "stats engine not built yet" and "stats" not in j) or \
            (j.get("built") is True and isinstance(j.get("stats"), dict))
        check("GET /leechseed/stats?char= answers (engine output, or 'not built yet' with no numbers)", code == 200 and honest,
              body[:200])
        check("GET /leechseed/distill answers", get("/leechseed/distill")[0] == 200)
        code, body = get("/local/leechseed")
        check("GET /local/leechseed serves the page", code == 200 and "Roll in the patch bay" in body)
        code, body = get("/panes.json")
        check("the leechseed pane is on the rail", code == 200 and any(p["id"] == "leechseed" for p in json.loads(body)["panes"]))
    finally:
        srv.shutdown()


def t6_private_name():
    p = os.path.join(ROOT, "_PRIVATE", "leechseed", "console.json")
    if not os.path.isfile(p):
        check("the display-name file exists in _PRIVATE", False, p)
        return
    name = str(json.load(open(p, encoding="utf-8")).get("title") or "").lower()
    pub = [os.path.join(HERE, f) for f in ("console.html", "extract.py", "test_leechseed.py")] + \
        [os.path.join(ROOT, "_tools", "console", "console.py")] + \
        [os.path.join(extract.OUT, f) for f in os.listdir(extract.OUT) if f.endswith(".json")]
    leaks = [os.path.relpath(f, ROOT) for f in pub if name and name in open(f, encoding="utf-8").read().lower()]
    check("the display name appears in no public leechseed or console file", not leaks, ", ".join(leaks))


def t7_draft_roundtrip():
    """POST /leechseed/draft -> the JSON + card land (in a temp folder, not _PRIVATE) -> the list and GET read them back"""
    import shutil, tempfile
    spec = importlib.util.spec_from_file_location("console_ut7", os.path.join(ROOT, "_tools", "console", "console.py"))
    con = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(con)
    tmp = tempfile.mkdtemp(prefix="leechseed-drafts-")
    con.LS_DRAFTS = tmp
    srv = con.S(("127.0.0.1", 0), con.H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = "http://127.0.0.1:%d" % srv.server_address[1]

    def call(path, body=None):
        data = json.dumps(body).encode("utf-8") if body is not None else None
        req = urllib.request.Request(base + path, data=data, headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.status, json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read().decode("utf-8") or "{}")
    draft = {"name": "Test Draft (round trip)", "seed": 48213, "instance_id": "char-victoria-midnight@48213#1a2b3c",
             "patch": {"europatch": "0.2.0", "kind": "patch", "name": "char-victoria-midnight", "modules": [], "cables": []},
             "kept": [{"module": "L4", "code": "WILL", "key": "WILL", "kind": "slider", "native": 14, "scale": [0, 20]},
                      {"module": "L5", "code": "WOUND", "key": "severity", "kind": "slider", "native": 8, "scale": [0, 10]},
                      {"module": "L12", "code": "FUNCTION", "key": "dramatica_archetype", "kind": "list", "pick": "Protagonist"}]}
    try:
        code, out = call("/leechseed/draft", draft)
        sid = out.get("id")
        check("POST /leechseed/draft saves a draft", code == 200 and out.get("ok") and sid == "test-draft-round-trip", str(out)[:200])
        jp, mp = os.path.join(tmp, "%s.json" % sid), os.path.join(tmp, "%s.md" % sid)
        rec = json.load(open(jp, encoding="utf-8")) if os.path.isfile(jp) else {}
        card = open(mp, encoding="utf-8").read() if os.path.isfile(mp) else ""
        check("the draft JSON holds the kept natives, the patch, the seed and the instance id",
              rec.get("numbers") == {"WILL": 14, "severity": 8} and rec["fields"]["dramatica_archetype"]["value"] == "Protagonist"
              and rec.get("seed") == "48213" and rec.get("instance_id") == draft["instance_id"] and rec.get("patch", {}).get("name")
              == "char-victoria-midnight" and rec.get("status") == "DRAFT" and rec.get("canon") is False, json.dumps(rec)[:200])
        check("the draft card lists every kept field, marked DRAFT, rolled from <patch> seed <n>",
              "DRAFT" in card and "never canon" in card and card.count("rolled from char-victoria-midnight seed 48213") == 3
              and all(k in card for k in ("WILL", "severity", "dramatica_archetype")), card[:160])
        code, lst = call("/leechseed/characters")
        check("GET /leechseed/characters lists it under drafts", code == 200 and any(d["id"] == sid for d in lst.get("drafts", [])))
        code, back = call("/leechseed/draft?id=" + str(sid))
        check("GET /leechseed/draft?id= reads it back with its card", code == 200 and back.get("fields", {}).get("WILL", {}).get("value") == 14
              and "DRAFT" in (back.get("card_md") or ""))
        code, again = call("/leechseed/draft", draft)
        check("a second draft with the same name gets its own file", code == 200 and again.get("id") == sid + "-2")
        bad = dict(draft, name="<script>x</script>", kept=[{"module": "L4", "code": "WILL", "key": "WILL", "kind": "slider", "native": "x"}])
        code, out = call("/leechseed/draft", bad)
        check("a bad name or value is refused, nothing written", code == 400 and len(os.listdir(tmp)) == 4, str(out)[:160])
        check("GET /leechseed/draft refuses a path", call("/leechseed/draft?id=../x")[0] == 404)
    finally:
        srv.shutdown()
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    for name, fn in [("1 found", t1_found), ("2 counts", t2_counts), ("3 sources", t3_sources), ("4 contract", t4_contract),
                     ("5 routes", t5_routes), ("6 private name", t6_private_name), ("7 draft round trip", t7_draft_roundtrip)]:
        print(name)
        fn()
    print("PASS" if not FAILS else "FAIL (%d): %s" % (len(FAILS), "; ".join(FAILS)))
    sys.exit(1 if FAILS else 0)
