"""The intake batches: cut the next reading batches, then check what the Payload Specialists wrote (SOP §9 Lane B, BOLO 107).

Usage:
  python _tools/intake/batch.py make C D E        # cut batches C, D, E from the unread live Joplin notes
  python _tools/intake/batch.py range C D E       # RANGE: prove every note was read and the fields are legal
  python _tools/intake/batch.py demote C D E      # a verbatim not found word for word: direct_quote -> inferred, verbatim null

Zero tokens. `make` writes, per batch, `_PRIVATE/intake/joplin/batch_<L>.txt` (the note bodies, chrome removed,
one block per note) and `batch_<L>.list` (id · path). The read ledger `_PRIVATE/intake/read.json` records every
path handed out, seeded with the pilot's 50. `range` checks `batch_<L>.json` against the list: every id once, legal
bin · system · conf · author · era, and each `verbatim` found word for word in its note (the pilot's 5/10 spot-check,
now a script). The script judges nothing about what is good.
"""
import io, json, os, re, sys

sys.path.insert(0, os.path.dirname(__file__))
from inventory import ROOT, body_of  # noqa: E402

INTAKE = os.path.join(ROOT, "_PRIVATE", "intake")
OUT = os.path.join(INTAKE, "joplin")
LEDGER = os.path.join(INTAKE, "read.json")
SIZE = 50                                   # ruled 10/8, pilot call 5
BINS = {"canon", "method", "inspiration", "dead"}
CONF = {"direct_quote", "inferred", "uncertain"}
AUTHOR = {"chief", "report", "other", "unknown"}
ERA = {"1", "2", "3", "4", "5", "none", "?"}


def norm(s):
    """Words only: case, punctuation, quote and dash styles and markdown never decide a verbatim check."""
    return " ".join(re.findall(r"\w+", s.lower()))


def ledger():
    if os.path.exists(LEDGER):
        return json.load(io.open(LEDGER, encoding="utf-8"))
    pilot = json.load(io.open(os.path.join(INTAKE, "pilot", "pilot50.json"), encoding="utf-8"))
    return {r["path"]: "pilot" for r in pilot}


def make(letters):
    inv = json.load(io.open(os.path.join(INTAKE, "inventory.json"), encoding="utf-8"))["notes"]
    read = ledger()
    todo = sorted((r for r in inv if r["vault"] == "joplin" and not r["empty"] and not r.get("dupe_of")
                   and not r["book"] and r["path"] not in read), key=lambda r: r["path"])
    os.makedirs(OUT, exist_ok=True)
    for L in letters:
        take, todo = todo[:SIZE], todo[SIZE:]
        if not take:
            print("batch %s: nothing left to read" % L)
            break
        txt, lst = [], []
        for n, r in enumerate(take, 1):
            nid = "%s%02d" % (L, n)
            raw = io.open(os.path.join(ROOT, r["path"]), encoding="utf-8", errors="replace").read()
            body, _ = body_of("joplin", raw)
            txt.append("===== %s · %s · year %s · %d chars · lineage: %s\n%s\n" % (
                nid, r["path"], r["year"], r["chars"], ", ".join(r["lineage"]) or "none", body.strip()))
            lst.append("%s\t%s" % (nid, r["path"]))
            read[r["path"]] = L
        io.open(os.path.join(OUT, "batch_%s.txt" % L), "w", encoding="utf-8").write("\n".join(txt))
        io.open(os.path.join(OUT, "batch_%s.list" % L), "w", encoding="utf-8").write("\n".join(lst) + "\n")
        print("batch %s: %d notes · %s chars" % (L, len(take), format(sum(r["chars"] for r in take), ",")))
    io.open(LEDGER, "w", encoding="utf-8").write(json.dumps(read, ensure_ascii=False, indent=0))
    print("unread live Joplin notes after this cut: %d" % len(todo))


def check(L):
    lst = [l.split("\t") for l in io.open(os.path.join(OUT, "batch_%s.list" % L), encoding="utf-8").read().splitlines() if l]
    paths = dict(lst)
    out = os.path.join(OUT, "batch_%s.json" % L)
    if not os.path.exists(out):
        return ["batch %s: no output file" % L], {}
    try:
        recs = json.load(io.open(out, encoding="utf-8"))
    except ValueError as e:
        return ["batch %s: bad JSON (%s)" % (L, e)], {}
    bad, seen = [], {}
    stats = {"notes": 0, "nuggets": 0, "quotes": 0, "found": 0, "bins": {}}
    for r in recs:
        i = r.get("id")
        if i not in paths:
            bad.append("%s: unknown id" % i)
            continue
        if i in seen:
            bad.append("%s: listed twice" % i)
        seen[i] = r
        stats["notes"] += 1
        stats["bins"][r.get("bin")] = stats["bins"].get(r.get("bin"), 0) + 1
        for k, legal in (("bin", BINS), ("author", AUTHOR), ("era", ERA)):
            if str(r.get(k)) not in legal:
                bad.append("%s: %s %r not legal" % (i, k, r.get(k)))
        body = norm(body_of("joplin", io.open(os.path.join(ROOT, paths[i]), encoding="utf-8", errors="replace").read())[0])
        for g in r.get("nuggets", []):
            stats["nuggets"] += 1
            if not re.fullmatch(r"0\d", str(g.get("system", ""))):
                bad.append("%s: system %r not 00-09" % (i, g.get("system")))
            if g.get("conf") not in CONF:
                bad.append("%s: conf %r not legal" % (i, g.get("conf")))
            if g.get("conf") == "direct_quote":
                stats["quotes"] += 1
                v = g.get("verbatim") or ""
                if v and norm(v) in body:
                    stats["found"] += 1
                else:
                    bad.append("%s: verbatim not found in the note: %r" % (i, v[:60]))
    for i in paths:
        if i not in seen:
            bad.append("%s: not read" % i)
    return bad, stats


def demote(letters):
    """A direct_quote whose verbatim is not in the note becomes inferred with verbatim null (the brief's own rule).
    The nugget stays; only the claim that it is word for word goes (10/8 RUN 2: 43/72 found on the first wave)."""
    for L in letters:
        lst = [l.split("\t") for l in io.open(os.path.join(OUT, "batch_%s.list" % L), encoding="utf-8").read().splitlines() if l]
        paths = dict(lst)
        out = os.path.join(OUT, "batch_%s.json" % L)
        recs = json.load(io.open(out, encoding="utf-8"))
        n = 0
        for r in recs:
            if r.get("id") not in paths:
                continue
            body = norm(body_of("joplin", io.open(os.path.join(ROOT, paths[r["id"]]), encoding="utf-8", errors="replace").read())[0])
            for g in r.get("nuggets", []):
                v = g.get("verbatim") or ""
                if g.get("conf") == "direct_quote" and not (v and norm(v) in body):
                    g["conf"], g["verbatim"] = "inferred", None
                    n += 1
        with io.open(out, "w", encoding="utf-8") as f:
            json.dump(recs, f, indent=1, ensure_ascii=False)
        print("DEMOTE batch %s: %d quote(s) not found word for word -> inferred" % (L, n))
    return 0


def rangecheck(letters):
    total = {"notes": 0, "nuggets": 0, "quotes": 0, "found": 0, "bins": {}}
    allbad = []
    for L in letters:
        bad, s = check(L)
        allbad += bad
        for k in ("notes", "nuggets", "quotes", "found"):
            total[k] += s.get(k, 0)
        for b, n in s.get("bins", {}).items():
            total["bins"][b] = total["bins"].get(b, 0) + n
        print("RANGE batch %s: %d notes · %d nuggets · %d finding(s)" % (L, s.get("notes", 0), s.get("nuggets", 0), len(bad)))
    print("bins: " + " · ".join("%d %s" % (n, b) for b, n in sorted(total["bins"].items(), key=lambda x: -x[1])))
    print("verbatim: %d/%d direct quotes found word for word" % (total["found"], total["quotes"]))
    for b in allbad:
        print("  - " + b)
    return 1 if any("not read" in b or "no output" in b or "bad JSON" in b for b in allbad) else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    cmd, letters = sys.argv[1], [a.upper() for a in sys.argv[2:]]
    sys.exit(make(letters) if cmd == "make" else demote(letters) if cmd == "demote" else rangecheck(letters))
