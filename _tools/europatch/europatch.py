# -*- coding: utf-8 -*-
"""EUROPATCH (BOLO 173): the roll engine. A patch (modules + dials + patch cables) + a seed -> one instance, as JSON.
Zero tokens: no model call anywhere in the roll. The model doc: ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_europatch.md

Usage:  python -X utf8 _tools/europatch/europatch.py roll <patch.json | - | preset:NAME | default> [--seed N] [--json] [--out F]
        python -X utf8 _tools/europatch/europatch.py modules [--json]     the module catalog (modules/leechseed.json)
        python -X utf8 _tools/europatch/europatch.py presets [--json]     the starter presets (presets/*.json)
        python -X utf8 _tools/europatch/europatch.py check <patch.json | -> [--json]
        python -X utf8 _tools/europatch/europatch.py default [--json]     the starter patch (12 modules, the doc's cables)
        python -X utf8 _tools/europatch/europatch.py build [--json] [--dry-run]  rebuild the catalog from LEECHSEED + refresh the page

The roll, in the doc's stacked order: the preset sets the dials, the patch's own values nudge them, the patch cables
bend each dial's centre, then the seed rolls inside the window (centre +- spread). Modules roll in cable order: a
module rolls after every module cabled into it, and its out-jacks pass the rolled values on. A loop is an error.
  add:       centre += strength x curve(value) x 100          (value = the source dial's rolled value / 100)
  multiply:  centre *= 1 + strength x curve(value)
  curves:    linear · ease-in · ease-out · s-curve · threshold-soft (a soft step around `threshold`, width `soft`)
Seeds: each module's seed = fnv1a(seed|module id); each dial draws from fnv1a(module seed|dial key) through xorshift32,
so adding a module never reshuffles the others. The page carries the same engine in JS (patchbay.html, between the
ENGINE markers); test_europatch.py proves both give the same instance.
"""
import io, json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CATALOG = os.path.join(HERE, "modules", "leechseed.json")
PRESETS = os.path.join(HERE, "presets")
PAGE = os.path.join(HERE, "patchbay.html")
VERSION = "0.1.0"
M32 = 0xFFFFFFFF
CURVES = ("linear", "ease-in", "ease-out", "s-curve", "threshold-soft")
MODES = ("add", "multiply")
CONF = {"high": 3, "medium": 2, "low": 1}   # model doc open call 7: trope-register conf -> default weight
NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 _.-]{0,63}$")
SEED_RE = re.compile(r"^[A-Za-z0-9_-]{1,64}$")
SET_PIECE_TENSION = 0.5      # provisional: tension at or above this flags a set-piece candidate
REFLECTIVE_PULL = 0.5        # provisional: 2+ cables, tension under 0.05, total pull at or above this


# ---------- the portable core (mirrored line for line in patchbay.html) ----------
def fnv1a(s):
    h = 2166136261
    for ch in s:
        h ^= ord(ch)
        h = (h * 16777619) & M32
    return h


class Rng(object):
    def __init__(self, state):
        self.x = state & M32 or 0x9E3779B9
        for _ in range(3):
            self.next()

    def next(self):
        x = self.x
        x ^= (x << 13) & M32
        x ^= x >> 17
        x ^= (x << 5) & M32
        self.x = x & M32
        return self.x / 4294967296.0


def rnd(x, n):
    p = 10 ** n
    return math.floor(x * p + 0.5) / p


def clamp(x, lo, hi):
    return lo if x < lo else hi if x > hi else x


def curve(x, c):
    x = clamp(x, 0.0, 1.0)
    k = c.get("curve") or "linear"
    if k == "ease-in":
        return x * x
    if k == "ease-out":
        return 1 - (1 - x) * (1 - x)
    if k == "s-curve":
        return x * x * (3 - 2 * x)
    if k == "threshold-soft":
        t = c.get("threshold", 0.5)
        w = c.get("soft", 0.15)
        if w < 0.001:
            w = 0.001
        y = clamp((x - (t - w)) / (2 * w), 0.0, 1.0)
        return y * y * (3 - 2 * y)
    return x


def weight(w):
    if isinstance(w, str):
        return CONF.get(w.lower(), 0)
    return w if isinstance(w, (int, float)) and w > 0 else 0


def fmt(x):
    if isinstance(x, float) and x == math.floor(x) and abs(x) < 1e15:
        return str(int(x))
    return repr(x) if isinstance(x, float) else str(x)


def band(v):
    return 0 if v < 34 else 1 if v < 67 else 2


def human(s):
    return str(s).replace("_", " ")


def resolve(patch, cat, presets):
    """the stack: catalog defaults -> patch preset -> module preset -> the module's own dials. Returns (mods, cables)."""
    defs = {}
    for m in cat["modules"]:
        defs[m["id"]] = m
    mods = []
    plist = patch.get("modules")
    if not plist:
        plist = [{"id": m["id"], "module": m["id"]} for m in cat["modules"]]
    for pm in plist:
        mid = pm.get("module") or pm.get("id")
        cm = defs.get(mid)
        if cm is None:
            continue
        iid = pm.get("id") or mid
        dials = {}
        for d in cm["dials"]:
            if d["kind"] == "slider":
                dials[d["key"]] = {"value": d["default"], "spread": d["spread"]}
            else:
                ws = {}
                for ch in d["choices"]:
                    ws[ch] = 1
                dials[d["key"]] = {"weights": ws}
        layers = []
        if patch.get("preset") and patch["preset"] in presets:
            layers.append((presets[patch["preset"]].get("dials") or {}).get(mid) or {})
        if pm.get("preset") and pm["preset"] in presets:
            layers.append((presets[pm["preset"]].get("dials") or {}).get(mid) or {})
        layers.append(pm.get("dials") or {})
        for lay in layers:
            for key in lay:
                if key not in dials:
                    continue
                src = lay[key]
                cur = dials[key]
                if "weights" in cur:
                    if src.get("pick") is not None:
                        ws = {}
                        for ch in cur["weights"]:
                            ws[ch] = 1 if ch == src["pick"] else 0
                        cur["weights"] = ws
                    if src.get("weights"):
                        ws = {}
                        for ch in cur["weights"]:
                            ws[ch] = cur["weights"][ch]
                        for ch in src["weights"]:
                            if ch in ws:
                                ws[ch] = weight(src["weights"][ch])
                        cur["weights"] = ws
                else:
                    if src.get("value") is not None:
                        cur["value"] = src["value"]
                    if src.get("spread") is not None:
                        cur["spread"] = src["spread"]
        mods.append({"id": iid, "module": mid, "code": cm["code"], "dials": dials, "cat": cm})
    if "cables" in patch:
        cables = patch.get("cables") or []
    elif patch.get("preset") and patch["preset"] in presets and "cables" in presets[patch["preset"]]:
        cables = presets[patch["preset"]]["cables"]
    else:
        cables = []
    return mods, cables


def roll_order(mods, cables):
    """Kahn's sort over modules, ties broken by patch order. Returns (order, loop_ids)."""
    idx = {}
    for i, m in enumerate(mods):
        idx[m["id"]] = i
    deps = [set() for _ in mods]
    for c in cables:
        a = idx.get(str(c.get("from", "")).split(".")[0])
        b = idx.get(str(c.get("to", "")).split(".")[0])
        if a is not None and b is not None and a != b:
            deps[b].add(a)
    done, order = set(), []
    while len(order) < len(mods):
        nxt = -1
        for i in range(len(mods)):
            if i not in done and all(d in done for d in deps[i]):
                nxt = i
                break
        if nxt < 0:
            return order, [mods[i]["id"] for i in range(len(mods)) if i not in done]
        done.add(nxt)
        order.append(nxt)
    return order, []


def roll_core(patch, seed, cat, presets):
    mods, cables = resolve(patch, cat, presets)
    order, loop = roll_order(mods, cables)
    sseed = str(seed)
    out_mods = {}
    rolled = {}
    warnings = []
    if loop:
        return None, ["patch cable loop through: " + ", ".join(loop)]
    cab_out = []
    into = {}
    for i, c in enumerate(cables):
        cid = c.get("id") or ("c" + str(i + 1))
        cab_out.append({"id": cid, "from": c["from"], "to": c["to"], "mode": c.get("mode") or "add",
                        "strength": c.get("strength", 0), "curve": c.get("curve") or "linear", "value": None, "pull": 0})
        into.setdefault(c["to"], []).append(i)
    tension = {}
    patterns = []
    for oi in order:
        m = mods[oi]
        mseed = fnv1a(sseed + "|" + m["id"])
        dout = {}
        rl = {}
        for d in m["cat"]["dials"]:
            key = d["key"]
            spec = m["dials"][key]
            rng = Rng(fnv1a(str(mseed) + "|" + key))
            u = rng.next()
            if d["kind"] == "slider":
                centre = clamp(spec["value"], 0, 100)
                spread = clamp(spec["spread"], 0, 50)
                bent = []
                pulls = []
                for ci in into.get(m["id"] + "." + key, []):
                    c = cables[ci]
                    co = cab_out[ci]
                    src = rolled.get(c["from"])
                    if src is None:
                        warnings.append(co["id"] + ": no rolled value at " + c["from"])
                        continue
                    x = src / 100.0
                    f = curve(x, c)
                    s = c.get("strength", 0)
                    if (c.get("mode") or "add") == "multiply":
                        nc = centre * (1 + s * f)
                    else:
                        nc = centre + s * f * 100
                    p = (nc - centre) / 100.0
                    centre = nc
                    co["value"] = rnd(x, 4)
                    co["pull"] = rnd(p, 4)
                    pulls.append(p)
                    bent.append(co["id"])
                centre = clamp(centre, 0, 100)
                val = clamp(centre + (2 * u - 1) * spread, 0, 100)
                val = rnd(val, 2)
                lo, hi = d["native"]
                dd = {"set": spec["value"], "spread": spread, "centre": rnd(centre, 2),
                      "window": [rnd(clamp(centre - spread, 0, 100), 2), rnd(clamp(centre + spread, 0, 100), 2)],
                      "rolled": val, "native": rnd(lo + val * (hi - lo) / 100.0, 1)}
                if bent:
                    dd["bent_by"] = bent
                    tot = 0
                    mag = 0
                    for p in pulls:
                        tot += p
                        mag += abs(p)
                    t = rnd(mag - abs(tot), 4)
                    tk = m["id"] + "_" + m["code"] + "." + key
                    tension[tk] = t
                    if t >= SET_PIECE_TENSION:
                        patterns.append({"kind": "set_piece", "dial": tk, "tension": t, "total_pull": rnd(tot, 4)})
                    elif len(pulls) >= 2 and t < 0.05 and abs(tot) >= REFLECTIVE_PULL:
                        patterns.append({"kind": "reflective", "dial": tk, "tension": t, "total_pull": rnd(tot, 4)})
                dout[key] = dd
                rl[key] = val
                rolled[m["id"] + "." + key] = val
            else:
                ws = spec["weights"]
                total = 0
                for ch in d["choices"]:
                    total += weight(ws.get(ch, 0))
                pick = None
                if total > 0:
                    r = u * total
                    acc = 0
                    for ch in d["choices"]:
                        acc += weight(ws.get(ch, 0))
                        if r < acc:
                            pick = ch
                            break
                    if pick is None:
                        pick = d["choices"][len(d["choices"]) - 1]
                wout = {}
                for ch in d["choices"]:
                    wout[ch] = weight(ws.get(ch, 0))
                dout[key] = {"weights": wout, "pick": pick}
                rl[key] = pick
        out_mods[m["id"] + "_" + m["code"]] = {"id": m["id"], "module": m["module"], "seed": mseed,
                                               "dials": dout, "rolled": rl}
    ordered = {}
    for m in mods:
        k = m["id"] + "_" + m["code"]
        if k in out_mods:
            ordered[k] = out_mods[k]
    out_mods = ordered
    inst = {"europatch": VERSION, "kind": "instance", "catalog": cat.get("catalog"),
            "patch": patch.get("name") or "untitled", "preset": patch.get("preset") or None, "seed": seed,
            "modules": out_mods, "cables": cab_out, "tension": tension, "patterns": patterns,
            "warnings": warnings}
    inst["summary"] = summarize(inst, cat)
    return inst, []


def summarize(inst, cat):
    """plain words from the values, no model: one headline, then one line per module"""
    by = {}
    for m in cat["modules"]:
        by[m["id"]] = m
    r = {}
    for k in inst["modules"]:
        mm = inst["modules"][k]
        r[mm["module"]] = mm["rolled"]
    lines = []
    head = []
    f = r.get("L12") or {}
    if f.get("dramatica_archetype"):
        a = f["dramatica_archetype"]
        head.append(("An " if a[0] in "AEIOU" else "A ") + a + (" who must " + ("change" if f.get("resolve") == "Change" else "hold steady") if f.get("resolve") else ""))
    d = r.get("L11") or {}
    if d.get("arc_type"):
        head.append("a " + human(d["arc_type"]) + " arc" + (", moved by " + human(d["change_cause"]) if d.get("change_cause") else ""))
    w = r.get("L5") or {}
    if w.get("wound_kind") and w.get("severity") is not None:
        lo, hi = by["L5"]["dials"][0]["native"] if "L5" in by else (0, 10)
        head.append("wound: " + human(w["wound_kind"]) + " at " + fmt(rnd(lo + w["severity"] * (hi - lo) / 100.0, 1)) + "/" + fmt(hi))
    im = r.get("L8") or {}
    if im.get("attachment_style"):
        head.append(human(im["attachment_style"]) + " attachment")
    if head:
        lines.append("; ".join(head) + ".")
    for k in inst["modules"]:
        mm = inst["modules"][k]
        cm = by.get(mm["module"])
        if not cm:
            continue
        parts = []
        for dd in cm["dials"]:
            v = mm["rolled"].get(dd["key"])
            if v is None:
                continue
            if dd["kind"] == "slider":
                parts.append(dd["words"][band(v)] + " (" + fmt(mm["dials"][dd["key"]]["native"]) + "/" + fmt(dd["native"][1]) + ")")
            else:
                parts.append(dd.get("label", dd["key"]) + ": " + human(v))
        lines.append(cm["code"] + ": " + "; ".join(parts) + ".")
    return lines
# ---------- end of the portable core ----------


def load_json(path):
    with io.open(path, encoding="utf-8") as f:
        return json.load(f)


def load_catalog():
    return load_json(CATALOG)


def load_presets():
    out = {}
    if os.path.isdir(PRESETS):
        for fn in sorted(os.listdir(PRESETS)):
            if fn.endswith(".json"):
                p = load_json(os.path.join(PRESETS, fn))
                out[p.get("name") or fn[:-5]] = p
    return out


def default_patch(cat):
    """all 12 modules (the page lays them out by the doc's tier groups), the doc's suggested patch cables"""
    mods = [{"id": m["id"], "module": m["id"], "dials": {}} for m in cat["modules"]]
    cables = []
    for i, c in enumerate(cat.get("suggested_cables", [])):
        cc = {k: v for k, v in c.items() if k in ("from", "to", "mode", "strength", "curve", "threshold", "soft")}
        cc["id"] = "c%d" % (i + 1)
        cables.append(cc)
    return {"europatch": VERSION, "kind": "patch", "name": "leechseed-default", "catalog": "leechseed",
            "preset": None, "seed": 48213, "modules": mods, "cables": cables,
            "groups": [dict(g) for g in cat.get("groups", [])]}


def check(patch, cat, presets):
    errs, warns = [], []
    if not isinstance(patch, dict):
        return ["a patch is a JSON object"], []
    if patch.get("name") and not NAME_RE.match(str(patch["name"])):
        errs.append("name: letters, digits, space, _ . - only (64 max)")
    if patch.get("catalog") not in (None, cat.get("catalog")):
        errs.append("catalog: only '%s' exists in v1" % cat.get("catalog"))
    if patch.get("preset") and patch["preset"] not in presets:
        errs.append("preset: no preset named %r" % patch["preset"])
    if patch.get("seed") is not None and not SEED_RE.match(str(patch["seed"])):
        errs.append("seed: a whole number (or a short word of letters, digits, _ -)")
    defs = {m["id"]: m for m in cat["modules"]}
    ids = {}
    for i, pm in enumerate(patch.get("modules") or []):
        mid = pm.get("module") or pm.get("id")
        if mid not in defs:
            errs.append("modules[%d]: no module %r in the catalog" % (i, mid)); continue
        iid = pm.get("id") or mid
        if iid in ids:
            errs.append("modules[%d]: id %r used twice" % (i, iid))
        ids[iid] = defs[mid]
        if pm.get("preset") and pm["preset"] not in presets:
            errs.append("%s.preset: no preset named %r" % (iid, pm["preset"]))
        dk = {d["key"]: d for d in defs[mid]["dials"]}
        for key, v in (pm.get("dials") or {}).items():
            d = dk.get(key)
            if not d:
                errs.append("%s.%s: no such dial" % (iid, key)); continue
            if not isinstance(v, dict):
                errs.append("%s.%s: a dial setting is an object" % (iid, key)); continue
            if d["kind"] == "slider":
                if "value" in v and not (isinstance(v["value"], (int, float)) and 0 <= v["value"] <= 100):
                    errs.append("%s.%s: value 0..100" % (iid, key))
                if "spread" in v and not (isinstance(v["spread"], (int, float)) and 0 <= v["spread"] <= 50):
                    errs.append("%s.%s: spread 0..50" % (iid, key))
            else:
                if v.get("pick") is not None and v["pick"] not in d["choices"]:
                    errs.append("%s.%s: %r is not a choice" % (iid, key, v["pick"]))
                ws = v.get("weights") or {}
                for ch, w in ws.items():
                    if ch not in d["choices"]:
                        errs.append("%s.%s: %r is not a choice" % (iid, key, ch))
                    if not (isinstance(w, (int, float)) and w >= 0) and str(w).lower() not in CONF:
                        errs.append("%s.%s.%s: a weight is a number >= 0 or high/medium/low" % (iid, key, ch))
                if ws and v.get("pick") is None:
                    merged = {ch: 1 for ch in d["choices"]}
                    merged.update({c: weight(w) for c, w in ws.items() if c in merged})
                    if sum(merged.values()) <= 0:
                        errs.append("%s.%s: every weight is 0" % (iid, key))
    if not patch.get("modules"):
        ids = {m["id"]: m for m in cat["modules"]}
    for i, c in enumerate(patch.get("cables") or []):
        tag = c.get("id") or "cables[%d]" % i
        for end in ("from", "to"):
            ref = str(c.get(end, ""))
            mid, _, key = ref.partition(".")
            if mid not in ids or key not in ids[mid].get("jacks_out", []):
                errs.append("%s.%s: no slider jack %r" % (tag, end, ref))
        if str(c.get("from", "")).split(".")[0] == str(c.get("to", "")).split(".")[0]:
            errs.append("%s: a patch cable inside one module is not in v1" % tag)
        if (c.get("mode") or "add") not in MODES:
            errs.append("%s.mode: add or multiply" % tag)
        if (c.get("curve") or "linear") not in CURVES:
            errs.append("%s.curve: one of %s" % (tag, ", ".join(CURVES)))
        s = c.get("strength", 0)
        if not (isinstance(s, (int, float)) and -1 <= s <= 1):
            errs.append("%s.strength: -1 to +1" % tag)
    if not errs:
        mods, cables = resolve(patch, cat, presets)
        _, loop = roll_order(mods, cables)
        if loop:
            errs.append("patch cable loop through: " + ", ".join(loop) + " (no roll order; model doc open call 5)")
    return errs, warns


def roll(patch, seed=None, cat=None, presets=None):
    cat = cat or load_catalog()
    presets = load_presets() if presets is None else presets
    if seed is None:
        seed = patch.get("seed", 1)
    if isinstance(seed, str) and re.match(r"^\d{1,15}$", seed):
        seed = int(seed)
    errs, _ = check(dict(patch, seed=seed), cat, presets)
    if errs:
        return None, errs
    return roll_core(patch, seed, cat, presets)


def read_patch(arg, cat, presets):
    if arg == "-":
        return json.loads(sys.stdin.read())
    if arg == "default":
        return default_patch(cat)
    if arg.startswith("preset:"):
        p = default_patch(cat)
        name = arg[7:]
        p["name"], p["preset"] = "preset-" + name, name
        if "cables" in presets.get(name, {}):
            p.pop("cables")
        return p
    return load_json(arg)


def build(js):
    import subprocess
    r = subprocess.run([sys.executable, "-X", "utf8", os.path.join(HERE, "build_catalog.py"), "--json"],
                       capture_output=True, text=True, encoding="utf-8")
    res = json.loads(r.stdout or "{}") if r.stdout.strip().startswith("{") else {"ok": False, "errors": [r.stderr]}
    if r.returncode:
        return res, 1
    res["page"] = embed_page()
    return res, 0


def embed_page():
    """write catalog + presets + the starter patch into the page's data block, then the Command theme"""
    if not os.path.exists(PAGE):
        return "no page"
    cat = load_catalog()
    data = {"catalog": cat, "presets": list(load_presets().values()), "default": default_patch(cat)}
    s = io.open(PAGE, encoding="utf-8").read()
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    s2 = re.sub(r'(<script type="application/json" id="ep-data">).*?(</script>)',
                lambda m: m.group(1) + blob + m.group(2), s, count=1, flags=re.S)
    sys.path.insert(0, os.path.join(ROOT, "_tools", "brand"))
    try:
        from theme import apply
        s2 = apply(s2, "europatch")
    except Exception:
        pass
    if s2 != s:
        with io.open(PAGE, "w", encoding="utf-8", newline="\n") as f:
            f.write(s2)
    return "refreshed" if s2 != s else "same"


def main(argv):
    js = "--json" in argv
    args = [a for a in argv if a != "--json"]
    def opt(name):
        if name in args:
            i = args.index(name)
            v = args[i + 1] if i + 1 < len(args) else None
            del args[i:i + 2]
            return v
        return None
    seed, out = opt("--seed"), opt("--out")
    if not args or args[0] in ("-h", "--help", "help"):
        print(__doc__); return 0
    verb = args[0]
    if verb == "build" and "--dry-run" in args:
        import subprocess
        r = subprocess.run([sys.executable, "-X", "utf8", os.path.join(HERE, "build_catalog.py"), "--dry-run", "--json"],
                           capture_output=True, text=True, encoding="utf-8")
        res = json.loads(r.stdout) if r.stdout.strip().startswith("{") else {"ok": False, "errors": [r.stderr]}
        res["page"] = "would refresh " + os.path.relpath(PAGE, ROOT).replace("\\", "/")
        print(json.dumps(res, indent=1) if js else "dry run: catalog %s modules, %s dials · %s" % (res.get("modules"), res.get("dials"), res["page"]))
        return r.returncode
    if verb == "build":
        res, code = build(js)
        print(json.dumps(res, indent=1) if js else "catalog %s · page %s" % (res.get("out", "?"), res.get("page", "?")))
        return code
    cat = load_catalog()
    presets = load_presets()
    if verb == "modules":
        if js:
            print(json.dumps(cat, ensure_ascii=False, indent=1)); return 0
        for m in cat["modules"]:
            print("%-4s %-9s %s" % (m["id"], m["code"], " · ".join(
                d["key"] + ("" if d["kind"] == "slider" else "[%d]" % len(d["choices"])) for d in m["dials"])))
        return 0
    if verb == "presets":
        if js:
            print(json.dumps({"presets": list(presets.values())}, ensure_ascii=False, indent=1)); return 0
        for n, p in presets.items():
            print("%-16s %s%s" % (n, p.get("title", ""), "  (provisional)" if p.get("provisional") else ""))
        return 0
    if verb == "default":
        print(json.dumps(default_patch(cat), ensure_ascii=False, indent=1)); return 0
    if verb in ("roll", "check"):
        if len(args) < 2:
            print("which patch? a path, -, default or preset:NAME"); return 2
        try:
            patch = read_patch(args[1], cat, presets)
        except (OSError, ValueError) as e:
            print(json.dumps({"ok": False, "errors": [str(e)]}) if js else "cannot read the patch: %s" % e); return 2
        if verb == "check":
            errs, warns = check(patch, cat, presets)
            if js:
                print(json.dumps({"ok": not errs, "errors": errs, "warnings": warns}, indent=1))
            else:
                print("ok" if not errs else "\n".join(errs))
            return 0 if not errs else 1
        inst, errs = roll(patch, seed, cat, presets)
        if errs:
            print(json.dumps({"ok": False, "errors": errs}, indent=1) if js else "\n".join(errs)); return 1
        body = json.dumps(inst, ensure_ascii=False, indent=1)
        if out:
            with io.open(out, "w", encoding="utf-8", newline="\n") as f:
                f.write(body + "\n")
        if js:
            print(body)
        else:
            print("seed %s · %s" % (inst["seed"], inst["patch"]))
            for line in inst["summary"]:
                print("  " + line)
            for p in inst["patterns"]:
                print("  %s at %s (tension %s)" % (p["kind"].replace("_", "-"), p["dial"], p["tension"]))
            if out:
                print("  instance -> " + out)
        return 0
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
