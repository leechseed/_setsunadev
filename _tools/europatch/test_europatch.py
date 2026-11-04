# -*- coding: utf-8 -*-
"""EUROPATCH proof (BOLO 173). Zero tokens. Run:  python -X utf8 _tools/europatch/test_europatch.py [--json]

  1 same patch + same seed twice          -> identical instances
  2 a new seed                             -> a different instance, every slider inside its window, every pick a weighted choice;
                                              over 600 seeds a 3:1 weighted list lands near 3:1 and a locked list never strays
  3 a patch cable on vs off                -> the bent dial moves by the 0.2 log-odds formula (add: logit + s*K*c; multiply: logit x (1+s*c))
  8 the edge                               -> twelve +1 cables into one dial never reach 100
  9 cancel + order                         -> two opposite equal cables cancel; cable order never changes the roll
 10 stats                                  -> the derived stats engine (Python vs JS mirror; Tori and Anna when their JSON exists)
  4 the per-module seed (model doc call 6) -> dropping a module leaves every other module's roll unchanged
  5 a loop                                 -> check refuses it (model doc call 5)
  6 Python vs the page's JS mirror         -> the same instance for every preset and the starter patch, 5 seeds each (needs node)
  7 the catalog rebuilds from LEECHSEED    -> build_catalog.py --dry-run passes
"""
import copy, io, json, math, os, re, shutil, subprocess, sys, tempfile

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
def bent(setv, adds=(), muls=()):
    """the 0.2 log-odds formula, re-derived here from the doc block, not imported"""
    p = min(max(setv / 100.0, 0.005), 0.995)
    z = math.log(p / (1 - p))
    for sf in muls:
        z *= 1 + sf
    z += sum(4 * math.log(3) * sf for sf in adds)
    return ep.rnd(100 * min(max(1 / (1 + math.exp(-z)), 0.005), 0.995), 2)
ok("3a cable off: the dial rolls its set value (spread 0)", off["rolled"] == 30 and "bent_by" not in off, str(off["rolled"]))
ok("3b add +0.4, source 0.5, linear: logit + 0.2K", on_add["rolled"] == bent(30, adds=[0.2]) and on_add["rolled"] > 30,
   "%s -> %s" % (off["rolled"], on_add["rolled"]))
ok("3c add -0.4: logit - 0.2K", on_neg["rolled"] == bent(30, adds=[-0.2]) and on_neg["rolled"] < 30, str(on_neg["rolled"]))
ok("3d multiply +0.5, linear: the logit distance from 0 x1.25 (30 moves away from the middle)",
   on_mul["rolled"] == bent(30, muls=[0.25]) and on_mul["rolled"] < 30, str(on_mul["rolled"]))
ok("3e ease-in bends less than linear at 0.5", on_ein["rolled"] == bent(30, adds=[0.1]) and 30 < on_ein["rolled"] < on_add["rolled"],
   str(on_ein["rolled"]))
mid = {"europatch": ep.VERSION, "name": "k-test", "modules": [
    {"id": "L1", "module": "L1", "dials": {"CORE": {"value": 100, "spread": 0}}},
    {"id": "L4", "module": "L4", "dials": {"WILL": {"value": 50, "spread": 0}}}],
    "cables": [{"from": "L1.CORE", "to": "L4.WILL", "mode": "add", "strength": 0.25, "curve": "linear"}]}
ok("3h K: a +0.25 cable at full source moves a mid dial 50 -> 75, as in 0.1",
   roll(mid, 3)["modules"]["L4_WILL"]["dials"]["WILL"]["rolled"] == 75)
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

# 8 diminishing returns at the edge: 12 strong cables pushing one dial up never reach 100
srcs = [(m["id"], j) for m in CAT["modules"] if m["id"] != "L4" for j in m.get("jacks_out", [])][:12]
mods8 = {}
for mid8, j in srcs:
    mods8.setdefault(mid8, {"id": mid8, "module": mid8, "dials": {}})["dials"][j] = {"value": 100, "spread": 0}
mods8["L4"] = {"id": "L4", "module": "L4", "dials": {"WILL": {"value": 90, "spread": 0}}}
steps = []
for n in range(1, len(srcs) + 1):
    q = {"europatch": ep.VERSION, "name": "edge-test", "modules": list(mods8.values()),
         "cables": [{"from": a + "." + j, "to": "L4.WILL", "mode": "add", "strength": 1, "curve": "linear"} for a, j in srcs[:n]]}
    steps.append(roll(q, 5)["modules"]["L4_WILL"]["dials"]["WILL"])
ok("8a twelve +1 cables into one dial never reach 100",
   len(srcs) == 12 and all(d["rolled"] < 100 and d["centre"] < 100 for d in steps) and steps[0]["rolled"] > 90,
   "%d cables: %s" % (len(srcs), " ".join(str(d["rolled"]) for d in steps)))
mods8["L4"]["dials"]["WILL"]["value"] = 50
soft = [50.0]
for n in range(1, 7):
    q = {"europatch": ep.VERSION, "name": "edge-test", "modules": list(mods8.values()),
         "cables": [{"from": a + "." + j, "to": "L4.WILL", "mode": "add", "strength": 0.25, "curve": "linear"} for a, j in srcs[:n]]}
    soft.append(roll(q, 5)["modules"]["L4_WILL"]["dials"]["WILL"]["rolled"])
gains = [soft[i + 1] - soft[i] for i in range(len(soft) - 1)]
ok("8b past the middle each +0.25 cable adds less than the one before",
   all(g > 0 for g in gains[:-1]) and all(gains[i + 1] < gains[i] for i in range(len(gains) - 1)),
   " -> ".join(str(v) for v in soft))

# 9 two opposite cables of equal strength cancel; cable order does not matter
def two(cables):
    q = {"europatch": ep.VERSION, "name": "cancel-test", "modules": [
        {"id": "L1", "module": "L1", "dials": {"CORE": {"value": 60, "spread": 0}}},
        {"id": "L2", "module": "L2", "dials": {"VITAL": {"value": 60, "spread": 0}}},
        {"id": "L4", "module": "L4", "dials": {"WILL": {"value": 30, "spread": 0}}}], "cables": cables}
    return roll(q, 11)["modules"]["L4_WILL"]["dials"]["WILL"]
up = {"from": "L1.CORE", "to": "L4.WILL", "mode": "add", "strength": 0.7, "curve": "s-curve"}
down = {"from": "L2.VITAL", "to": "L4.WILL", "mode": "add", "strength": -0.7, "curve": "s-curve"}
mul = {"from": "L2.VITAL", "to": "L4.WILL", "mode": "multiply", "strength": 0.4, "curve": "linear"}
cx = two([up, down])
ok("9a two opposite cables of equal strength cancel", cx["rolled"] == 30 and cx["centre"] == 30, str(cx["rolled"]))
ok("9b cable order does not matter (add + multiply, both orders)", two([up, mul])["rolled"] == two([mul, up])["rolled"],
   "%s / %s" % (two([up, mul])["rolled"], two([mul, up])["rolled"]))

# 10 the stats engine
SKIPS = []
TORI_SLICE = {"id": "tori-slice", "numbers": {"SOCIAL": 10, "WILL": 14, "WOUND": 8, "DRIVE": 12, "resistance_index": 8,
              "projection_tendency": 6, "shadow_density": 7, "shame_index": 2, "armor_index": 8, "attachment_style_score": 7},
              "fields": {"conditional_patterns": {"value": ["merit_earns_freedom"], "status": "filled"},
                         "mc_problem_element": {"value": "Equity", "status": "filled"},
                         "limit_type": {"value": "Optionlock", "status": "filled"},
                         "dramatica_archetype": {"value": "Protagonist", "status": "filled"},
                         "story_outcome": {"value": "Failure", "status": "filled"},
                         "secure_base_object": {"value": "deceased", "status": "filled"}}}
ANNA_SLICE = {"id": "anna-slice", "numbers": {"SOCIAL": 10, "WILL": 11, "WOUND": 0, "DRIVE": 10, "resistance_index": 0},
              "fields": {"shame_index": {"value": "n/a", "status": "held"}, "armor_index": {"value": None, "status": "held"},
                         "dramatica_archetype": {"value": "Guardian", "status": "filled"}}}
ts = ep.stats_core(ep.inputs_from_char(TORI_SLICE), "tori-slice")
an = ep.stats_core(ep.inputs_from_char(ANNA_SLICE), "anna-slice")
ok("10a the slice's Tori table: TEI 20 · ER 4 · DR 10 · SL 8 · NM 16 · ST 6 · CR 7, all five flags' conditions met",
   ts["stats"] == {"truth_exposure": 20, "expressive_range": 4, "stress_threshold": 6, "damage_resistance": 10,
                   "narrative_momentum": 16, "social_legibility": 8, "collapse_risk": 7}
   and set(ts["flags"].values()) == {"ACTIVE"}, json.dumps(ts["stats"]))
ok("10b the slice's Anna table: DR 11 · NM 10 · ST 11; TEI, ER, SL, CR null with inputs listed; every flag INACTIVE or UNKNOWN, never guessed",
   an["stats"]["damage_resistance"] == 11 and an["stats"]["narrative_momentum"] == 10 and an["stats"]["stress_threshold"] == 11
   and an["stats"]["truth_exposure"] is None and an["stats"]["expressive_range"] is None
   and an["stats"]["social_legibility"] is None and an["stats"]["collapse_risk"] is None
   and {"shame_index", "armor_index", "projection_tendency", "shadow_density"} <= set(an["inputs_missing"])
   and an["flags"]["EARNED_JUDGEMENT"] == "INACTIVE" and an["flags"]["OPTIONLOCK_PROGRESSION"] == "INACTIVE",
   json.dumps(an["flags"]))
for cid, want in (("victoria_midnight", {"truth_exposure": 20, "expressive_range": 4}),
                  ("anna_colson_conway", {"damage_resistance": 11, "narrative_momentum": 10, "stress_threshold": 11,
                                          "truth_exposure": None, "expressive_range": None})):
    res = ep.char_stats(cid)
    if res.get("errors"):
        SKIPS.append("10c %s: %s" % (cid, res["errors"][0]))
        continue
    got = {k: res["stats"][k] for k in want}
    ok("10c %s's record (CONSOLE's JSON) gives the known values" % cid, got == want, json.dumps(got))
if node:
    d = tempfile.mkdtemp(prefix="europatch-stats-")
    try:
        insts = [roll(c["patch"], c["seed"]) for c in cases[:20]] if "cases" in dir() else [roll(base, 1)]
        recs = [TORI_SLICE, ANNA_SLICE]
        if os.path.isdir(ep.CHARS):
            recs += [ep.load_json(os.path.join(ep.CHARS, f)) for f in sorted(os.listdir(ep.CHARS)) if f.endswith(".json")]
        js = os.path.join(d, "stats.js")
        with io.open(js, "w", encoding="utf-8") as f:
            f.write(engine + "\nvar fs=require('fs');var IN=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));"
                    "var out=IN.insts.map(function(i){return EP.statsCore(EP.inputsFromInstance(i),'x')})"
                    ".concat(IN.recs.map(function(r){return EP.statsCore(EP.inputsFromChar(r),'x')}));"
                    "fs.writeFileSync(process.argv[3],JSON.stringify(out));\n")
        inp, outp = os.path.join(d, "in.json"), os.path.join(d, "out.json")
        with io.open(inp, "w", encoding="utf-8") as f:
            json.dump({"insts": insts, "recs": recs}, f)
        r = subprocess.run([node, js, inp, outp], capture_output=True, text=True)
        if r.returncode:
            ok("10d stats: Python = JS mirror", False, r.stderr[-400:])
        else:
            jo = json.load(io.open(outp, encoding="utf-8"))
            po = [ep.stats_core(ep.inputs_from_instance(i), "x") for i in insts] + [ep.stats_core(ep.inputs_from_char(x), "x") for x in recs]
            bad = [i for i, (a1, b1) in enumerate(zip(po, jo)) if json.loads(json.dumps(a1)) != b1]
            ok("10d stats: Python = JS mirror, %d instances + %d records" % (len(insts), len(recs)), not bad and len(jo) == len(po),
               "mismatch at %s" % bad[:5] if bad else "%d identical" % len(po))
    finally:
        shutil.rmtree(d, ignore_errors=True)

# 7 the catalog rebuilds
r = subprocess.run([sys.executable, "-X", "utf8", os.path.join(HERE, "build_catalog.py"), "--dry-run", "--json"],
                   capture_output=True, text=True, encoding="utf-8")
ok("7 the catalog rebuilds from LEECHSEED", r.returncode == 0, (r.stdout or r.stderr).strip().replace("\n", " ")[:160])

passed = sum(1 for x in RESULTS if x["ok"])
if "--json" in sys.argv:
    print(json.dumps({"passed": passed, "total": len(RESULTS), "results": RESULTS, "skipped": SKIPS}, indent=1))
else:
    for x in RESULTS:
        print("%s  %s%s" % ("PASS" if x["ok"] else "FAIL", x["test"], ("  · " + x["detail"]) if x["detail"] else ""))
    for sk in SKIPS:
        print("SKIP  " + sk)
    print("%d/%d passed" % (passed, len(RESULTS)))
sys.exit(0 if passed == len(RESULTS) else 1)
