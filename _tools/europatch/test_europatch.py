# -*- coding: utf-8 -*-
"""EUROPATCH proof (BOLO 173). Zero tokens. Run:  python -X utf8 _tools/europatch/test_europatch.py [--json]

  1 same patch + same seed twice          -> identical instances
  2 a new seed                             -> a different instance, every slider inside its window, every pick a weighted choice;
                                              over 600 seeds a 3:1 weighted list lands near 3:1 and a locked list never strays
  3 a patch cable on vs off                -> the bent dial moves by exactly strength x curve(value) x 100 (add), x(1+s*c) (multiply)
  4 the per-module seed (model doc call 6) -> dropping a module leaves every other module's roll unchanged
  5 a loop                                 -> check refuses it (model doc call 5)
  6 Python vs the page's JS mirror         -> the same instance for every preset and the starter patch, 5 seeds each (needs node)
  7 the catalog rebuilds from LEECHSEED    -> build_catalog.py --dry-run passes
"""
import copy, io, json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import europatch as ep  # noqa: E402

CAT = ep.load_catalog()
PRESETS = ep.load_presets()
RESULTS = []


def ok(name, cond, detail=""):
    RESULTS.append({"test": name, "ok": bool(cond), "detail": detail})


def roll(patch, seed):
    inst, errs = ep.roll(patch, seed, CAT, PRESETS)
    assert not errs, errs
    return inst


def sliders(inst):
    for mk, m in inst["modules"].items():
        for k, d in m["dials"].items():
            if "rolled" in d:
                yield mk + "." + k, d


# 1 repeatable
base = ep.default_patch(CAT)
a, b = roll(base, 48213), roll(copy.deepcopy(base), 48213)
ok("1 same patch + seed = same instance", json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True))

# 2 a new seed: different, same characteristics
c = roll(base, 48214)
diff = sum(1 for (k, d), (_, e) in zip(sliders(a), sliders(c)) if d["rolled"] != e["rolled"])
inside = all(d["window"][0] - 1e-9 <= d["rolled"] <= d["window"][1] + 1e-9 for _, d in sliders(c))
picks_ok = all(d["weights"].get(d["pick"], 0) > 0 for m in c["modules"].values() for d in m["dials"].values() if "pick" in d)
ok("2a a new seed = a new instance", diff >= 20, "%d sliders moved" % diff)
ok("2b every slider rolls inside its window", inside)
ok("2c every pick is a weighted choice", picks_ok)
p = copy.deepcopy(base)
L4 = next(m for m in p["modules"] if m["id"] == "L4")
L4["dials"] = {"system_stance": {"weights": {"cog": 3, "believer": 1, "mask": 0, "bystander": 0, "resister": 0}},
               "coping_strategy": {"pick": "naive"}, "WILL": {"value": 40, "spread": 12}}
p["cables"] = []
counts, strays, out = {}, 0, 0
for s in range(1, 601):
    r = roll(p, s)["modules"]["L4_WILL"]["dials"]
    counts[r["system_stance"]["pick"]] = counts.get(r["system_stance"]["pick"], 0) + 1
    strays += r["coping_strategy"]["pick"] != "naive"
    out += not (28 <= r["WILL"]["rolled"] <= 52)
ratio = counts.get("cog", 0) / max(1, counts.get("believer", 0))
ok("2d 3:1 weights land near 3:1 over 600 seeds", 2.3 <= ratio <= 3.9 and set(counts) <= {"cog", "believer"},
   "cog %d · believer %d (ratio %.2f)" % (counts.get("cog", 0), counts.get("believer", 0), ratio))
ok("2e a locked pick never strays; a 40 +- 12 slider stays in 28..52", strays == 0 and out == 0, "strays %d, out %d" % (strays, out))

# 3 a patch cable on vs off
def cable_patch(cable):
    q = {"europatch": ep.VERSION, "name": "cable-test", "modules": [
        {"id": "L1", "module": "L1", "dials": {"CORE": {"value": 50, "spread": 0}}},
        {"id": "L4", "module": "L4", "dials": {"WILL": {"value": 30, "spread": 0}}}], "cables": [cable] if cable else []}
    return roll(q, 9)["modules"]["L4_WILL"]["dials"]["WILL"]
off = cable_patch(None)
on_add = cable_patch({"from": "L1.CORE", "to": "L4.WILL", "mode": "add", "strength": 0.4, "curve": "linear"})
on_neg = cable_patch({"from": "L1.CORE", "to": "L4.WILL", "mode": "add", "strength": -0.4, "curve": "linear"})
on_mul = cable_patch({"from": "L1.CORE", "to": "L4.WILL", "mode": "multiply", "strength": 0.5, "curve": "linear"})
on_ein = cable_patch({"from": "L1.CORE", "to": "L4.WILL", "mode": "add", "strength": 0.4, "curve": "ease-in"})
on_thr = cable_patch({"from": "L1.CORE", "to": "L4.WILL", "mode": "add", "strength": 0.4, "curve": "threshold-soft",
                      "threshold": 0.7, "soft": 0.1})
ok("3a cable off: the dial rolls its set value (spread 0)", off["rolled"] == 30 and "bent_by" not in off, str(off["rolled"]))
ok("3b add +0.4, source 0.5, linear: moves +20", on_add["rolled"] - off["rolled"] == 20, "%s -> %s" % (off["rolled"], on_add["rolled"]))
ok("3c add -0.4: moves -20", on_neg["rolled"] - off["rolled"] == -20, str(on_neg["rolled"]))
ok("3d multiply +0.5, linear: x1.25", on_mul["rolled"] == 37.5, str(on_mul["rolled"]))
ok("3e ease-in bends less than linear at 0.5 (+10)", on_ein["rolled"] == 40, str(on_ein["rolled"]))
ok("3f threshold-soft at 0.7: a 0.5 source does not bite", on_thr["rolled"] == 30, str(on_thr["rolled"]))
ok("3g the cable never switches: strength 0 = no move",
   cable_patch({"from": "L1.CORE", "to": "L4.WILL", "mode": "add", "strength": 0, "curve": "linear"})["rolled"] == 30)

# 4 per-module seeds
full = copy.deepcopy(base); full["cables"] = []
less = copy.deepcopy(full); less["modules"] = [m for m in less["modules"] if m["id"] != "L9"]
f1, f2 = roll(full, 777), roll(less, 777)
same = all(f1["modules"][k] == f2["modules"][k] for k in f2["modules"])
ok("4 dropping L9 leaves the other 11 modules' rolls unchanged", same and "L9_EROS" not in f2["modules"])

# 5 loops are refused
loop = {"modules": [{"id": "L1", "module": "L1"}, {"id": "L4", "module": "L4"}], "cables": [
    {"from": "L1.CORE", "to": "L4.WILL", "strength": 0.2}, {"from": "L4.WILL", "to": "L1.CORE", "strength": 0.2}]}
errs, _ = ep.check(loop, CAT, PRESETS)
ok("5 a patch cable loop is refused", any("loop" in e for e in errs), "; ".join(errs))
bad = {"modules": [{"id": "L4", "module": "L4", "dials": {"WILL": {"value": 140}, "system_stance": {"pick": "zealot"}}}],
       "cables": [{"from": "L4.nope", "to": "L1.CORE", "curve": "wobble", "strength": 3}]}
errs, _ = ep.check(bad, CAT, PRESETS)
ok("5b check names the bad value, choice, jack, curve and strength", len(errs) >= 5, "%d errors" % len(errs))

# 6 Python vs the JS mirror
node = shutil.which("node")
if not node:
    ok("6 Python = JS mirror", False, "node is not on PATH")
else:
    page = io.open(os.path.join(HERE, "patchbay.html"), encoding="utf-8").read()
    engine = page[page.index("/*ENGINE-START*/"):page.index("/*ENGINE-END*/")]
    cases = []
    patches = [("default", base)] + [("preset:" + n, ep.read_patch("preset:" + n, CAT, PRESETS)) for n in PRESETS]
    patches.append(("cable mix", dict(copy.deepcopy(base), cables=base["cables"] + [
        {"from": "L1.CORE", "to": "L3.SOCIAL", "mode": "multiply", "strength": 0.3, "curve": "s-curve"},
        {"from": "L2.VITAL", "to": "L3.SOCIAL", "mode": "add", "strength": -0.6, "curve": "ease-out"}])))
    for name, pt in patches:
        for sd in (1, 7, 48213, 4294967295, "kenshi"):
            cases.append({"name": name, "patch": pt, "seed": sd})
    d = tempfile.mkdtemp(prefix="europatch-")
    try:
        js = os.path.join(d, "parity.js")
        with io.open(js, "w", encoding="utf-8") as f:
            f.write(engine + "\nvar fs=require('fs');var IN=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));"
                    "var P={};IN.presets.forEach(function(p){P[p.name]=p});"
                    "var out=IN.cases.map(function(c){var r=EP.roll(c.patch,c.seed,IN.catalog,P);return r[0]||{errors:r[1]}});"
                    "fs.writeFileSync(process.argv[3],JSON.stringify(out));\n")
        inp, outp = os.path.join(d, "in.json"), os.path.join(d, "out.json")
        with io.open(inp, "w", encoding="utf-8") as f:
            json.dump({"catalog": CAT, "presets": list(PRESETS.values()), "cases": cases}, f)
        r = subprocess.run([node, js, inp, outp], capture_output=True, text=True)
        if r.returncode:
            ok("6 Python = JS mirror", False, r.stderr[-400:])
        else:
            js_out = json.load(io.open(outp, encoding="utf-8"))
            bad_cases = []
            for case, j in zip(cases, js_out):
                py = roll(case["patch"], case["seed"])
                if json.loads(json.dumps(py)) != j:
                    bad_cases.append("%s seed %s" % (case["name"], case["seed"]))
            ok("6 Python = JS mirror, %d patches x 5 seeds" % len(patches), not bad_cases and len(js_out) == len(cases),
               "; ".join(bad_cases[:5]) or "%d instances identical" % len(cases))
    finally:
        shutil.rmtree(d, ignore_errors=True)

# 7 the catalog rebuilds
r = subprocess.run([sys.executable, "-X", "utf8", os.path.join(HERE, "build_catalog.py"), "--dry-run", "--json"],
                   capture_output=True, text=True, encoding="utf-8")
ok("7 the catalog rebuilds from LEECHSEED", r.returncode == 0, (r.stdout or r.stderr).strip().replace("\n", " ")[:160])

passed = sum(1 for x in RESULTS if x["ok"])
if "--json" in sys.argv:
    print(json.dumps({"passed": passed, "total": len(RESULTS), "results": RESULTS}, indent=1))
else:
    for x in RESULTS:
        print("%s  %s%s" % ("PASS" if x["ok"] else "FAIL", x["test"], ("  · " + x["detail"]) if x["detail"] else ""))
    print("%d/%d passed" % (passed, len(RESULTS)))
sys.exit(0 if passed == len(RESULTS) else 1)
