"""SYSTEM REVIEW page — build (BOLO 100).

Usage:  python _tools/review/build.py 02

Reads one storytelling system's docs from ShroomsQ/_CANON/_SSOT/<NN>_*/ and the frontmatter of
every system folder, computes the Definition of Done, and renders _tools/review/out/REVIEW-<NN>.html
from _tools/review/template.html. Nothing on the page is hand-typed: every box, line, field, tag,
check and citation comes from a file, and every feed arrow carries the line it was parsed from.

Inputs : ShroomsQ/_CANON/_SSOT/0*/*.md       frontmatter of every system doc (level 1 map)
         ShroomsQ/_CANON/_SSOT/<NN>_*/*.md   the system's docs (main doc + modules + templates)
         the main doc's git history          the version each field first appeared in
         _CANON_NODES/<instance>-chart.md    the worked instance's status line only
         _tools/tm/terms.json                the hover-term register (shared with the TM pages)
         _tools/tm/build.py                  reused: inline renderer, auto-linker, table parser
Outputs: _tools/review/out/REVIEW-<NN>.html  (an artifact fragment: no doctype/html/head/body)
"""
import glob, importlib.util, io, json, os, re, subprocess, sys, datetime
from urllib.parse import unquote

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SSOT = os.path.join(ROOT, "ShroomsQ", "_CANON", "_SSOT")
TM_DIR = os.path.join(ROOT, "_tools", "tm")

# reuse the TM page's renderer (render_inline, auto_link_section, parse_table, esc, strip_md)
_spec = importlib.util.spec_from_file_location("tmbuild", os.path.join(TM_DIR, "build.py"))
tm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tm)

MISSES = []          # parse misses, printed at the end
SEMVER = re.compile(r"(\d+)\.(\d+)\.(\d+)")
ID_RE = r"(?:BVX|MSX|PSY)\.\d+"


def miss(msg):
    MISSES.append(msg)


def load_text(p):
    with io.open(p, encoding="utf-8-sig") as f:
        return f.read().replace("\r\n", "\n")


def sv(s):
    m = SEMVER.search(s or "")
    return tuple(int(x) for x in m.groups()) if m else None


def sv_str(t):
    return ".".join(map(str, t)) if t else ""


def rel(p):
    return os.path.relpath(p, ROOT).replace("\\", "/")


# ---------------------------------------------------------------- frontmatter (tolerant)

FM_KEYS = ("type", "category", "version", "last_updated", "status", "purpose", "module_of", "dependencies", "trunk", "sources", "applies_to")


def _val(v):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        return [x.strip().strip('"').strip("'") for x in v[1:-1].split(",") if x.strip()]
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1].replace('\\"', '"')
    return v


def parse_fm(text):
    fm = {}
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if m:
        lines = m.group(1).split("\n")
        i = 0
        while i < len(lines):
            mm = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", lines[i])
            if mm:
                k, v = mm.group(1), mm.group(2)
                if v.strip() == "":
                    items = []
                    j = i + 1
                    while j < len(lines) and re.match(r"^\s+-\s+", lines[j]):
                        items.append(_val(re.sub(r"^\s+-\s+", "", lines[j])))
                        j += 1
                    if items:
                        fm[k] = items
                        i = j
                        continue
                else:
                    fm[k] = _val(v)
            i += 1
    if "version" not in fm:
        # malformed single-line frontmatter ("## type: … version: 1.0.0 …"): scan the head of the file
        head = text[:4000]
        for k in FM_KEYS:
            if k in fm:
                continue
            mm = re.search(r"(?:^|[\s#])" + k + r':\s*("(?:[^"\\]|\\.)*"|\[[^\]]*\]|[^\s]+)', head)
            if mm:
                fm[k] = _val(mm.group(1))
    return fm


def norm(s):
    s = unquote(str(s)).replace("[[", "").replace("]]", "")
    s = os.path.basename(s)
    s = re.sub(r"\.md$", "", s, flags=re.I)
    s = s.lower().replace(" ", "_")
    s = re.sub(r"[^a-z0-9_]", "", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s


# ---------------------------------------------------------------- level 1: every system

def load_systems():
    systems, docs = {}, {}
    for d in sorted(glob.glob(os.path.join(SSOT, "0*_*"))):
        if not os.path.isdir(d):
            continue
        folder = os.path.basename(d)
        nn = folder[:2]
        name = re.sub(r"_SYSTEMS$", "", folder[3:]).replace("_", " ")
        sys_rec = {"id": nn, "name": name, "folder": rel(d), "docs": [], "open": 0, "vmin": None, "vmax": None, "deps": {}}
        for p in sorted(glob.glob(os.path.join(d, "*.md"))):
            text = load_text(p)
            fm = parse_fm(text)
            stem = norm(p)
            v = sv(str(fm.get("version", "")))
            deps = fm.get("dependencies", [])
            if isinstance(deps, str):
                deps = [deps] if deps else []
            doc = {
                "id": stem, "sys": nn, "path": rel(p), "file": os.path.basename(p),
                "version": sv_str(v), "status": str(fm.get("status", ""))[:600],
                "purpose": str(fm.get("purpose", "")), "module_of": norm(fm.get("module_of", "")) if fm.get("module_of") else "",
                "category": str(fm.get("category", "")), "type": str(fm.get("type", "")),
                "last_updated": str(fm.get("last_updated", "")),
                "deps_raw": deps, "open": text.count("⧗"), "bytes": len(text.encode("utf-8")),
                "has_fm": bool(fm),
            }
            docs[stem] = doc
            sys_rec["docs"].append(stem)
            sys_rec["open"] += doc["open"]
            if v:
                sys_rec["vmin"] = v if not sys_rec["vmin"] or v < sys_rec["vmin"] else sys_rec["vmin"]
                sys_rec["vmax"] = v if not sys_rec["vmax"] or v > sys_rec["vmax"] else sys_rec["vmax"]
        systems[nn] = sys_rec
    # resolve dependencies doc -> doc (or doc -> system when the doc is not found)
    by_suffix = {}
    for k in docs:
        mm = re.match(r"ssot_\d\d_(.+)$", k)
        if mm:
            by_suffix.setdefault(mm.group(1), []).append(k)
    unresolved = []
    for d in docs.values():
        d["deps"], d["deps_sys"] = [], []
        for raw in d["deps_raw"]:
            n = norm(raw)
            tgt = None
            if n in docs:
                tgt = n
            else:
                mm = re.match(r"ssot_\d\d_(.+)$", n)
                cands = by_suffix.get(mm.group(1), []) if mm else []
                if len(cands) == 1:
                    tgt = cands[0]
            if tgt and tgt != d["id"]:
                d["deps"].append(tgt)
            else:
                mm = re.search(r"ssot_(\d\d)_", n)
                if mm and mm.group(1) in systems:
                    d["deps_sys"].append(mm.group(1))
                else:
                    unresolved.append(f"{d['id']} -> {raw}")
        for t in d["deps"]:
            ts = docs[t]["sys"]
            if ts != d["sys"]:
                systems[d["sys"]]["deps"][ts] = systems[d["sys"]]["deps"].get(ts, 0) + 1
        for ts in d["deps_sys"]:
            if ts != d["sys"]:
                systems[d["sys"]]["deps"][ts] = systems[d["sys"]]["deps"].get(ts, 0) + 1
    for s in systems.values():
        s["vmin"], s["vmax"] = sv_str(s["vmin"]), sv_str(s["vmax"])
    return systems, docs, unresolved


# ---------------------------------------------------------------- main-doc sectioning

def headings(lines):
    out = []
    fence = False
    for i, l in enumerate(lines):
        if l.strip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        m = re.match(r"^(#{2,4})\s+(.*)$", l)
        if m:
            out.append((i, len(m.group(1)), m.group(2).strip()))
    return out


def section(lines, hs, pattern, level=None, first=True):
    """(start, end) line indexes of the body under the first heading matching pattern."""
    for idx, (i, lv, txt) in enumerate(hs):
        if re.search(pattern, txt, re.I) and (level is None or lv == level):
            end = len(lines)
            for (j, lv2, _) in hs[idx + 1:]:
                if lv2 <= lv:
                    end = j
                    break
            return i + 1, end
    return None


def tables_in(lines, rng):
    out, i = [], rng[0]
    while i < rng[1]:
        if re.match(r"^\|.*\|\s*$", lines[i].strip()):
            start = i
            buf = []
            while i < rng[1] and re.match(r"^\|.*\|\s*$", lines[i].strip()):
                buf.append(lines[i].strip())
                i += 1
            h, rows = tm.parse_table(buf)
            out.append({"start": start, "header": [tm.strip_md(x).lower() for x in h], "rows": rows})
        else:
            i += 1
    return out


def col(header, *pats):
    for p in pats:
        for i, h in enumerate(header):
            if re.search(p, h, re.I):
                return i
    return None


# ---------------------------------------------------------------- layer mentions & feeds

LAYER_ID_RE = re.compile(r"\bL(\d{1,2})\b")


def layer_mentions(text, names):
    """[(pos, Lid)] for 'L5' and for upper-case layer names (WOUND), merged when adjacent."""
    hits = [(m.start(), "L" + m.group(1)) for m in LAYER_ID_RE.finditer(text) if ("L" + m.group(1)) in names.values()]
    for lid, nm in [(v, k) for k, v in names.items()]:
        for m in re.finditer(r"(?<![A-Za-z_.])" + re.escape(nm) + r"(?![A-Za-z_])", text):
            hits.append((m.start(), lid))
    hits.sort()
    out = []
    for pos, lid in hits:
        if out and out[-1][1] == lid and pos - out[-1][0] < 12:
            continue
        out.append((pos, lid))
    return out


def sentences(text):
    parts = re.split(r"(?<=[.;:])\s+(?=[A-Z`*(\[])", text)
    return [p for p in parts if p.strip()]


def parse_feeds(text, line_no, cur, names, edges, kind_hint=""):
    for s in sentences(text):
        plain = s
        cite = {"line": line_no, "text": tm.strip_md(s)[:320]}
        found = False
        # a. `WILL = CORE` — a default derivation
        for m in re.finditer(r"`([A-Z]+)\s*=\s*([A-Z]+)`", plain):
            a, b = names.get(m.group(1)), names.get(m.group(2))
            if a and b and a != b:
                edges.append({"from": b, "to": a, "kind": "derives", "cite": cite})
                found = True
        if found:
            continue
        # b. "fed independently from the storyform"
        if re.search(r"\bfed\b[^.]*\bfrom the storyform", plain, re.I):
            tgts = [lid for _, lid in layer_mentions(plain[:re.search(r"\bfed\b", plain).start()], names)] or ([cur] if cur else [])
            for t in tgts:
                edges.append({"from": "storyform", "to": t, "kind": "fed", "cite": cite})
            continue
        # c. "X feeds Y" / "Numeric variables feed WOUND base and SOCIAL defaults"
        mv = re.search(r"\bfeeds?\b", plain)
        if mv:
            left = [lid for _, lid in layer_mentions(plain[:mv.start()], names)] or ([cur] if cur else [])
            right = [lid for _, lid in layer_mentions(plain[mv.end():], names)]
            for a in left:
                for b in right:
                    if a != b:
                        edges.append({"from": a, "to": b, "kind": "feeds", "cite": cite})
            if left and right:
                continue
        # d. "High WOUND reduces effective WILL and SOCIAL"
        mv = re.search(r"\breduces?\b", plain)
        if mv and cur:
            right = [lid for _, lid in layer_mentions(plain[mv.end():], names)]
            for b in right:
                if b != cur:
                    edges.append({"from": cur, "to": b, "kind": "reduces", "cite": cite})
        # e. "L9 reads L3's `knowledge_map`"
        for m in re.finditer(r"\breads (L\d{1,2})'s", plain):
            before = [lid for _, lid in layer_mentions(plain[:m.start()], names)]
            subj = before[-1] if before else cur
            if subj and subj != m.group(1):
                edges.append({"from": m.group(1), "to": subj, "kind": "reads", "cite": cite})
        # f. "a relational pointer from L9 to the L8 imprint event"
        for m in re.finditer(r"\bfrom (L\d{1,2}) to (?:the )?(L\d{1,2})\b", plain):
            edges.append({"from": m.group(1), "to": m.group(2), "kind": "points", "cite": cite})
        # g. "Shared with L9"
        for m in re.finditer(r"\b[Ss]hared with (L\d{1,2})\b", plain):
            if cur and cur != m.group(1):
                edges.append({"from": cur, "to": m.group(1), "kind": "shares", "cite": cite})


# ---------------------------------------------------------------- fields

TOK = re.compile(r"`([A-Za-z][A-Za-z0-9_]*)`")


def paren_ctx(s):
    """for each char index: the opening-paren text of its innermost group ('' when at depth 0)."""
    ctx, stack = [], []
    for i, ch in enumerate(s):
        if ch == "(":
            stack.append(i)
        ctx.append(s[stack[-1] + 1:stack[-1] + 4] if stack else None)
        if ch == ")" and stack:
            stack.pop()
    return ctx


def table_fields(cell):
    """fields named in the PART A 'field it writes' cell: top-level tokens, '(+ x)' sub-fields; '(was x…)' and
    '(incl. type x)' are notes, not fields."""
    out, ctx = [], paren_ctx(cell)
    last_top = None
    for m in TOK.finditer(cell):
        c = ctx[m.start()]
        name = m.group(1)
        if c is None:
            out.append({"name": name, "parent": None})
            last_top = name
        elif c.lstrip().startswith("+"):
            out.append({"name": name, "parent": last_top})
    # notes after a field: "(adults only)", "(optional)"
    notes = {}
    for m in re.finditer(r"`([A-Za-z][A-Za-z0-9_]*)`\s*\(([^`()]+)\)", cell):
        notes[m.group(1)] = m.group(2).strip()
    for f in out:
        if f["name"] in notes:
            f["note"] = notes[f["name"]]
    return out


def decl_fields(text, cur, table_owner):
    """fields a domain declaration names, with the owner layer, parent (for 'X gains y') and co-cited ids."""
    out = []
    for s in sentences(text):
        ids = set(re.findall(ID_RE, s))
        clauses = re.split(r";\s+", s)
        for cl in clauses:
            gains = re.search(r"`([a-z][a-z0-9_]*)` gains\b", cl)
            for m in TOK.finditer(cl):
                name = m.group(1)
                if not re.match(r"^[a-z][a-z0-9_]*$", name):
                    continue
                before, after = cl[:m.start()], cl[m.end():]
                in_table = name in table_owner
                if not in_table:
                    if "not a field" in cl or re.match(r"^\s+is renamed", after) or "superseding" in before \
                            or re.match(r"^[^`]{0,40}read alias", after) or re.search(r"\b(?:was|renamed)\s*$", before):
                        continue
                mo = re.search(r"(L\d{1,2})'s (?:own )?$", before)
                owner = mo.group(1) if mo else cur
                if in_table and owner not in table_owner[name]:
                    continue  # a mention of another layer's field
                parent = gains.group(1) if gains and m.start() > gains.end() else None
                shared = []
                nxt = TOK.search(cl, m.end())
                tail = cl[m.end(): nxt.start() if nxt else len(cl)]
                ms = re.search(r"shared with (L\d{1,2})", tail, re.I)
                if ms:
                    shared.append(ms.group(1))
                out.append({"name": name, "owner": owner, "parent": parent, "ids": sorted(ids), "shared": shared})
    # "Shared with L9." as its own sentence after the field's sentence
    sents = sentences(text)
    for i, s in enumerate(sents):
        ms = re.match(r"^[Ss]hared with (L\d{1,2})\b", s.strip())
        if ms and i > 0:
            prev = [m.group(1) for m in TOK.finditer(sents[i - 1])]
            for f in out:
                if prev and f["name"] == prev[-1] and ms.group(1) not in f["shared"]:
                    f["shared"].append(ms.group(1))
    return out


def parse_main(text):
    """everything the review needs from one version of the main doc."""
    lines = text.split("\n")
    hs = headings(lines)
    res = {"layers": [], "names": {}, "fields": {}, "decl": {}, "edges": [], "tiers": [], "tags": {}, "tag_groups": {},
           "derived": [], "library": [], "versions": [], "binding": None, "fork": None, "instance": None}

    # PART A
    rng = section(lines, hs, r"PART A", 2)
    if not rng:
        miss("no PART A section")
        return res
    tb = next((t for t in tables_in(lines, rng) if col(t["header"], r"^layer") is not None), None)
    if not tb:
        miss("no layer table in PART A")
        return res
    h = tb["header"]
    ci = {"name": col(h, r"^name"), "q": col(h, r"question"), "src": col(h, r"source"), "fld": col(h, r"field"), "tier": col(h, r"tier")}
    for k, v in ci.items():
        if v is None:
            miss(f"PART A table: no '{k}' column")
    for r_i, r in enumerate(tb["rows"]):
        mm = re.search(r"\b([A-Z]\d{1,2})\b", r[0] if r else "")
        if not mm:
            continue
        lid = mm.group(1)
        g = lambda key: r[ci[key]] if ci[key] is not None and ci[key] < len(r) else ""
        name = tm.strip_md(g("name"))
        src = g("src")
        ids = []
        for m in re.finditer(r"\[\[(" + ID_RE + r")\]\]|(" + ID_RE + r")(?:\s*[–-]\s*(" + ID_RE + r"))?", src):
            if m.group(1):
                ids.append(m.group(1))
            elif m.group(3):
                p1, n1 = m.group(2).split(".")
                p2, n2 = m.group(3).split(".")
                if p1 == p2:
                    w = len(n1)
                    ids += [f"{p1}.{str(n).zfill(w)}" for n in range(int(n1), int(n2) + 1)]
                else:
                    ids += [m.group(2), m.group(3)]
            else:
                ids.append(m.group(2))
        ids = list(dict.fromkeys(ids))
        links = [unquote(m.group(1)) for m in re.finditer(r"\]\(([^)]+)\)", src)]
        tier_m = re.search(r"(\d+)", tm.strip_md(g("tier")))
        res["layers"].append({"id": lid, "name": name, "q": tm.strip_md(g("q")), "src_raw": src, "src_ids": ids, "src_links": links,
                              "tier": int(tier_m.group(1)) if tier_m else None, "fields_raw": g("fld"), "line": tb["start"] + 3 + r_i})
        res["names"][name] = lid
        if not tier_m:
            miss(f"{lid}: no tier in PART A")
    names = res["names"]
    table_owner = {}
    for L in res["layers"]:
        L["tfields"] = table_fields(L["fields_raw"])
        for f in L["tfields"]:
            table_owner.setdefault(f["name"], set()).add(L["id"])
    # the binding rule (PART A prose)
    for i in range(rng[0], rng[1]):
        if re.match(r"^\*\*Binding rule", lines[i]):
            res["binding"] = {"line": i + 1, "text": lines[i]}
            parse_feeds(lines[i], i + 1, None, names, res["edges"])

    # field tags
    rng_t = section(lines, hs, r"Field tags")
    if rng_t:
        t = next(iter(tables_in(lines, rng_t)), None)
        if t:
            for r in t["rows"]:
                tag_cell = tm.strip_md(r[0])
                tag = tag_cell.split(",")[0].strip().lower()
                for m in TOK.finditer(r[1] if len(r) > 1 else ""):
                    res["tags"][m.group(1)] = tag
                    res["tag_groups"][m.group(1)] = tag_cell
        pre = re.search(r"predate (\d+\.\d+\.\d+)", "\n".join(lines[rng_t[0]:rng_t[1]]))
        res["tag_since"] = pre.group(1) if pre else None
        res["tag_line"] = rng_t[0]
        res["tag_every"] = "every field" in " ".join(lines[max(0, rng_t[0] - 2):rng_t[0] + 2]).lower()

    # tiers
    rng_3 = section(lines, hs, r"Three-Tier")
    if rng_3:
        t = next(iter(tables_in(lines, rng_3)), None)
        if t:
            for r in t["rows"]:
                n = re.search(r"(\d+)", tm.strip_md(r[0]))
                res["tiers"].append({"n": int(n.group(1)) if n else None, "layers": tm.strip_md(r[1]) if len(r) > 1 else "",
                                     "cls": tm.strip_md(r[2]) if len(r) > 2 else "", "budget": tm.strip_md(r[3]) if len(r) > 3 else ""})
        txt = " ".join(l for l in lines[rng_3[0]:rng_3[1]] if l.strip() and not l.startswith("|") and not l.startswith("---"))
        res["tier_note"] = txt.strip()

    # domain declarations
    rng_d = section(lines, hs, r"Domain Declarations")
    if rng_d:
        for i in range(rng_d[0], rng_d[1]):
            m = re.match(r"^\*\*(L\d{1,2})\s*[—-]\s*([A-Z]+):\*\*\s*(.*)$", lines[i])
            if m:
                res["decl"][m.group(1)] = {"line": i + 1, "text": m.group(3)}
                parse_feeds(m.group(3), i + 1, m.group(1), names, res["edges"])
        res["decl_rule"] = next((lines[i] for i in range(rng_d[0], rng_d[1]) if lines[i].strip() and not lines[i].startswith("**")), "")
    else:
        miss("no 'Domain Declarations' section")

    # fields: table + declarations
    fields = {}

    def addf(name, lid, parent, origin, note=None, ids=()):
        f = fields.setdefault(name, {"name": name, "layers": [], "parent": parent, "origin": origin, "note": note, "ids": set()})
        if lid not in f["layers"]:
            f["layers"].append(lid)
        if parent and not f["parent"]:
            f["parent"] = parent
        if note and not f["note"]:
            f["note"] = note
        f["ids"].update(ids)

    for L in res["layers"]:
        for f in L["tfields"]:
            addf(f["name"], L["id"], f["parent"], "table", f.get("note"))
    for lid, d in res["decl"].items():
        for f in decl_fields(d["text"], lid, table_owner):
            addf(f["name"], f["owner"], f["parent"], "declaration", ids=f["ids"])
            for s in f["shared"]:
                addf(f["name"], s, f["parent"], "declaration")
    res["fields"] = fields

    # the fork
    rng_f = section(lines, hs, r"Villain-Arc Fork|\bFork\b")
    if rng_f:
        body = [(i, lines[i]) for i in range(rng_f[0], rng_f[1]) if lines[i].strip() and not lines[i].startswith("---")]
        main_p = max(body, key=lambda x: len(x[1])) if body else None
        if main_p:
            i, ptxt = main_p
            sents = sentences(ptxt)
            parse_feeds(sents[0], i + 1, None, names, res["edges"])
            entry = [lid for _, lid in layer_mentions(sents[0], names)]
            pa = ptxt.find("Path (a)")
            pb = ptxt.find("Path (b)")
            fork = {"line": i + 1, "text": ptxt, "cite_note": body[0][1] if body[0][0] != i else "", "entry": entry[:1], "paths": {}}
            if pa >= 0 and pb > pa:
                for key, seg in (("a", ptxt[pa:pb]), ("b", ptxt[pb:])):
                    ls = [lid for _, lid in layer_mentions(seg, names)]
                    fork["paths"][key] = {"text": tm.strip_md(seg.split(". A writer")[0]).replace("**", "")[:400], "layers": list(dict.fromkeys(ls))}
                    for lid in dict.fromkeys(ls):
                        if lid not in fork["entry"]:
                            res["edges"].append({"from": "fork", "to": lid, "kind": "path " + key,
                                                 "cite": {"line": i + 1, "text": tm.strip_md(seg)[:320]}})
                for e in fork["entry"]:
                    res["edges"].append({"from": e, "to": "fork", "kind": "stalls at", "cite": {"line": i + 1, "text": tm.strip_md(sents[0])}})
            else:
                miss("fork: no Path (a)/(b) split")
            title_h = next((txt for (j, lv, txt) in hs if j == rng_f[0] - 1), "The Fork")
            fork["title"] = title_h
            res["fork"] = fork

    # derived statistics (the method's, not the instance's: the first section of that name)
    rng_s = section(lines, hs, r"^Derived Statistics")
    if rng_s:
        t = next(iter(tables_in(lines, rng_s)), None)
        if t:
            for r in t["rows"]:
                res["derived"].append({"name": tm.strip_md(r[0]), "formula": tm.strip_md(r[1]) if len(r) > 1 else ""})

    # library
    rng_l = section(lines, hs, r"×\s*LIBRARY|LIBRARY", 2)
    if rng_l:
        t = next(iter(tables_in(lines, rng_l)), None)
        if t:
            hh = t["header"]
            c_id, c_bk, c_fd, c_gv = col(hh, r"^id"), col(hh, r"book"), col(hh, r"feed"), col(hh, r"give|what")
            tiers = {}
            for L in res["layers"]:
                tiers.setdefault(L["tier"], []).append(L["id"])
            for r_i, r in enumerate(t["rows"]):
                mid = re.search(ID_RE, r[c_id] if c_id is not None else "")
                if not mid:
                    miss(f"library row {r_i + 1}: no id")
                    continue
                feeds_txt = r[c_fd] if c_fd is not None else ""
                ls = [lid for _, lid in layer_mentions(tm.strip_md(feeds_txt), names)]
                for m in re.finditer(r"Tier (\d)", feeds_txt):
                    ls += tiers.get(int(m.group(1)), [])
                res["library"].append({"id": mid.group(0), "book": r[c_bk] if c_bk is not None else "", "feeds": list(dict.fromkeys(ls)),
                                       "feeds_raw": feeds_txt, "gives": r[c_gv] if c_gv is not None else "", "line": t["start"] + 3 + r_i})
                if not ls:
                    miss(f"library {mid.group(0)}: no layer parsed from '{tm.strip_md(feeds_txt)}'")

    # version history
    rng_v = section(lines, hs, r"Version history", 2)
    if rng_v:
        for i in range(rng_v[0], rng_v[1]):
            l = lines[i]
            m = re.match(r"^-\s+\*\*(\d+\.\d+\.\d+)\s*·\s*([0-9-]+)\*\*\s*[—-]\s*(.*)$", l)
            if m:
                res["versions"].append({"v": m.group(1), "date": m.group(2), "text": m.group(3), "line": i + 1})
                continue
            m = re.match(r"^\|\s*(\d+\.\d+\.\d+)\s*\|\s*([0-9-]+)\s*\|(.*)\|\s*$", l)
            if m:
                res["versions"].append({"v": m.group(1), "date": m.group(2), "text": m.group(3).strip(), "line": i + 1})

    # the worked instance
    rng_i = section(lines, hs, r"THE INSTANCE", 2)
    if rng_i:
        htxt = lines[rng_i[0] - 1]
        mname = re.search(r"·\s*([^,]+)", htxt)
        body = "\n".join(lines[rng_i[0]:rng_i[1]])
        parked = next((l for l in lines[rng_i[0]:rng_i[1]] if re.search(r"\bparked\b", l, re.I)), "")
        marker = re.search(r"`(⏸[^`]*)`", parked)
        res["instance"] = {"name": mname.group(1).strip() if mname else "", "line": rng_i[0], "parked": parked.strip(),
                           "marker": marker.group(1) if marker else "⏸", "marks": body.count("⏸")}
    return res


# ---------------------------------------------------------------- shapes: each system's OWN layout (BOLO 100, ruled 10/4)
# shapes.json maps a system number to the layout its main doc really has. 02 (character) has no entry and takes parse_main.

SHAPES = {}
_sp = os.path.join(HERE, "shapes.json")
if os.path.exists(_sp):
    SHAPES = json.loads(load_text(_sp))

TICK2 = re.compile(r"`([a-z][a-z0-9_]*(?: [a-z][a-z0-9_]*){0,2})`")
TICK_STOP = {"yes", "no", "core", "semi", "fringe", "stub", "filled", "canon", "provisional", "retired", "none", "true", "false", "optional", "step", "ramp"}
MDLINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+\.md[^)]*)\)")


def clean_label(s):
    s = tm.strip_md(s).replace("`", "").replace("**", "").strip()
    s = re.split(r"\s+[—–]\s+|:\s", s)[0]
    s = re.sub(r"[\s.:—–-]+$", "", s)
    s = re.sub(r"\s+", " ", s)
    return s[:60]


def fenced_mask(lines):
    """True for every line inside a code fence (fence lines included)."""
    mask, inside = [], False
    for l in lines:
        if l.strip().startswith("```"):
            mask.append(True)
            inside = not inside
        else:
            mask.append(inside)
    return mask


def parse_versions(lines, hs):
    out = []
    rng_v = section(lines, hs, r"Version history", 2)
    if rng_v:
        for i in range(rng_v[0], rng_v[1]):
            l = lines[i]
            m = re.match(r"^-\s+\*\*(\d+\.\d+\.\d+)\s*·\s*([0-9-]+)\*\*\s*[—-]\s*(.*)$", l)
            if m:
                out.append({"v": m.group(1), "date": m.group(2), "text": m.group(3), "line": i + 1})
                continue
            m = re.match(r"^\|\s*(\d+\.\d+\.\d+)\s*\|\s*([0-9-]+)\s*\|(.*)\|\s*$", l)
            if m:
                out.append({"v": m.group(1), "date": m.group(2), "text": m.group(3).strip(), "line": i + 1})
    return out


def cites_in(text, idre):
    ids = list(dict.fromkeys(re.findall(idre, text)))
    links = list(dict.fromkeys(unquote(m.group(1)) for m in MDLINK.finditer(text)))
    return ids, links


def parse_shape(text, shape):
    """everything the review needs from the main doc of a system with its own layout; returns parse_main's shape."""
    lines = text.split("\n")
    hs = headings(lines)
    fm = fenced_mask(lines)
    idre = shape.get("ids", ID_RE)
    res = {"layers": [], "names": {}, "fields": {}, "decl": {}, "edges": [], "tiers": [], "tags": {}, "tag_groups": {},
           "derived": [], "library": [], "versions": parse_versions(lines, hs), "binding": None, "fork": None, "instance": None,
           "shape": True}
    spec = shape["layers"]
    layer_recs = []

    def sec(pat, level=None):
        return section(lines, hs, pat, level)

    kind = spec["kind"]
    if kind == "table":
        rng = sec(spec["within"], spec.get("within_level"))
        if not rng:
            miss(f"no '{spec['within']}' section")
            return res
        tb = next((t for t in tables_in(lines, rng) if col(t["header"], spec["table_has"]) is not None), None)
        if not tb:
            miss(f"no layer table in '{spec['within']}'")
            return res
        h = tb["header"]
        cols = spec["cols"]
        ci = {k: (col(h, v) if isinstance(v, str) else None) for k, v in cols.items() if k != "fields"}
        fcols = [col(h, p) for p in cols.get("fields", [])]
        for k, v in cols.items():
            if k != "fields" and isinstance(v, str) and ci[k] is None:
                miss(f"layer table: no '{k}' column ({v})")
        for r_i, r in enumerate(tb["rows"]):
            idc = ci.get("id") if ci.get("id") is not None else 0
            mm = re.search(spec["id_re"], tm.strip_md(r[idc]) if idc < len(r) else "")
            if not mm:
                continue
            g = lambda k: r[ci[k]] if ci.get(k) is not None and ci[k] < len(r) else ""
            qtxt = tm.strip_md(g("q")) or (("mirrors " + tm.strip_md(g("mirror"))) if g("mirror") else "")
            layer_recs.append({"id": mm.group(1), "name": tm.strip_md(g("name")), "q": qtxt, "line": tb["start"] + 3 + r_i, "ranges": [],
                               "row": " | ".join(r), "src_cell": g("src") if ci.get("src") is not None else None,
                               "fcells": [r[c] for c in fcols if c is not None and c < len(r)]})
    else:
        within = None
        if spec.get("within"):
            within = sec(spec["within"], spec.get("within_level"))
            if not within:
                miss(f"no '{spec['within']}' section")
                return res
        lo, hi = within if within else (0, len(lines))
        starts = []
        if kind == "headings":
            level = spec["level"]
            pat = re.compile(spec["match"])
            after = re.compile(spec["start_after"]) if spec.get("start_after") else None
            stop = re.compile(spec["stop_at"]) if spec.get("stop_at") else None
            active = after is None
            n = 0
            for (i, lv, txt) in hs:
                if i < lo or i >= hi or lv != level:
                    continue
                if not active:
                    if after.search(txt):
                        active = True
                    continue
                if stop and stop.search(txt):
                    break
                m = pat.search(txt)
                if m:
                    n += 1
                    starts.append((i, spec["id"].format(*m.groups(), n=n), spec["name"].format(*m.groups(), n=n)))
            for (i, lid, name) in starts:
                end = hi
                for (j, lv2, _t) in hs:
                    if j > i and lv2 <= level:
                        end = min(end, j)
                        break
                layer_recs.append({"id": lid, "name": name, "line": i + 1, "ranges": [(i + 1, end)], "row": None, "q": ""})
        elif kind == "bold":
            pat = re.compile(spec["match"])
            for i in range(lo, hi):
                m = None if fm[i] else pat.match(lines[i])
                if m:
                    starts.append((i, spec["id"].format(*m.groups()), spec["name"].format(*m.groups())))
            for k, (i, lid, name) in enumerate(starts):
                end = starts[k + 1][0] if k + 1 < len(starts) else hi
                layer_recs.append({"id": lid, "name": tm.strip_md(name).strip(" .:—-"), "line": i + 1, "ranges": [(i + 1, end)], "row": None, "q": ""})
        else:
            miss(f"unknown layers kind {kind}")
            return res
    if not layer_recs:
        miss("shape matched no layers")
    # extra sections feed a layer's fields and citations (07: the worked section of each part)
    for lid, pat in (shape.get("extra") or {}).items():
        r = sec(pat, 2)
        for L in layer_recs:
            if L["id"] == lid and r:
                L["ranges"].append(r)
    # aux layers: other structures the doc defines whose named items a writer fills (cards, header, schema)
    for a in shape.get("aux", []):
        rec = {"id": a["id"], "name": a["name"], "aux": True, "row": None, "q": "", "ranges": [], "line": 0, "rules": a.get("rules", [])}
        if a.get("section"):
            r = sec(a["section"], a.get("level"))
            if not r:
                miss(f"aux '{a['name']}': no '{a['section']}' section")
                continue
            rec["ranges"], rec["line"] = [r], r[0]
        elif a.get("line_re"):
            ln = next((i for i, l in enumerate(lines) if re.match(a["line_re"], l)), None)
            if ln is None:
                miss(f"aux '{a['name']}': no line matches {a['line_re']}")
                continue
            rec["ranges"], rec["line"] = [(ln, ln + 1)], ln + 1
        layer_recs.append(rec)

    fields = {}

    def addf(name, lid, parent=None, origin="text", note=None, ids=()):
        if not name or name.lower() in ("e.g", "i.e") or any(re.search(x, name, re.I) for x in shape.get("exclude", [])):
            return
        f = fields.setdefault(name, {"name": name, "layers": [], "parent": parent, "origin": origin, "note": note, "ids": set()})
        if lid not in f["layers"]:
            f["layers"].append(lid)
        if parent and not f["parent"]:
            f["parent"] = parent
        f["ids"].update(ids)

    def scoped(rule, lid, name):
        return f"{lid}·{name}" if rule.get("scope") == "layer" else name

    def each_line(rng, with_fences):
        for i in range(rng[0], rng[1]):
            if with_fences or not fm[i]:
                yield i, lines[i]

    rules = list(shape.get("fields", []))
    for L in layer_recs:
        L["tfields"] = []
        lrules = list(L.get("rules") or []) if L.get("aux") else [r for r in rules if not r.get("only") or L["id"] in r["only"]]
        for cell in L.get("fcells", []):          # table layers: the field cells
            if spec.get("cell_style") == "table_fields":
                for f in table_fields(cell):
                    addf(f["name"], L["id"], f["parent"], "table", f.get("note"))
                    L["tfields"].append({"name": f["name"]})
            else:
                for m in TICK2.finditer(cell):
                    if m.group(1) not in TICK_STOP:
                        addf(m.group(1), L["id"], None, "table")
                        L["tfields"].append({"name": m.group(1)})
                if spec.get("cell_bold"):       # bold-led named items in the cell (not cross-references)
                    for m in re.finditer(r"\*\*([^*]+)\*\*", cell):
                        nm = clean_label(m.group(1))
                        if nm and not re.match(r"^cross-ref", nm, re.I):
                            addf(nm, L["id"], None, "table")
                            L["tfields"].append({"name": nm})
        for rule in lrules:
            k = rule["kind"]
            for rng in L["ranges"]:
                if k == "ticks":
                    for i, l in each_line(rng, rule.get("fences", False)):
                        for m in TICK2.finditer(l):
                            if m.group(1) not in TICK_STOP:
                                addf(m.group(1), L["id"], None, "text", ids=cites_in(l, idre)[0])
                elif k == "labels":
                    pat = re.compile(rule["re"])
                    for i, l in each_line(rng, False):
                        m = pat.match(l)
                        nm = clean_label(m.group(1)) if m else ""
                        if nm:
                            addf(scoped(rule, L["id"], nm), L["id"], None, "text", ids=cites_in(l, idre)[0])
                elif k == "bullet_ticks":
                    for i, l in each_line(rng, False):
                        m = re.match(r"^\s*[-*]\s+\*{0,2}`([^`]+)`\*{0,2}\s*[—:–-]", l)
                        if m and re.match(rule.get("token_re", ".*"), m.group(1)):
                            addf(clean_label(m.group(1)), L["id"], None, "text")
                elif k in ("table_rows", "table_headers"):
                    for t in tables_in(lines, rng):
                        if k == "table_rows":
                            hc = rule.get("hcol", rule.get("col", 0))
                            if rule.get("header_match") and not (hc < len(t["header"]) and re.search(rule["header_match"], t["header"][hc], re.I)):
                                continue
                            if rule.get("header_skip") and t["header"] and re.search(rule["header_skip"], t["header"][0], re.I):
                                continue
                            for r in t["rows"]:
                                c = rule.get("col", 0)
                                nm = clean_label(r[c]) if c < len(r) else ""
                                if nm:
                                    addf(scoped(rule, L["id"], nm), L["id"], None, "table")
                        else:
                            for hcell in t["header"]:
                                nm = clean_label(hcell)
                                if nm and not (rule.get("skip") and re.search(rule["skip"], nm, re.I)):
                                    addf(scoped(rule, L["id"], nm), L["id"], None, "table")
                elif k == "fence_keys":
                    inside, lang, top = False, "", None
                    for i in range(rng[0], rng[1]):
                        l = lines[i]
                        if l.strip().startswith("```"):
                            if not inside:
                                inside, lang, top = True, l.strip()[3:].strip().lower(), None
                            else:
                                inside = False
                            continue
                        if not inside or lang == "mermaid" or (rule.get("lang") and lang != rule["lang"]):
                            continue
                        m = re.match(r"^(\s*)([A-Za-z][A-Za-z0-9_ /-]{0,30}?):(\s|$)", l)
                        if not m or m.group(2).lower().startswith(("e.g", "i.e")):
                            continue
                        key = m.group(2).strip()
                        if len(m.group(1)) == 0:
                            top = key
                            addf(key, L["id"], None, "text")
                        else:
                            addf(f"{top}.{key}" if top else key, L["id"], top, "text")
        body = "\n".join("\n".join(lines[a:b]) for (a, b) in L["ranges"])
        src_text = L["src_cell"] if L.get("src_cell") is not None else (L["row"] if L.get("row") is not None else body)
        L["src_ids"], L["src_links"] = cites_in(src_text, idre)
        L["src_raw"] = " ".join(f"[[{i}]]" for i in L["src_ids"])
        L["tier"] = None
        if not L["q"]:
            for (a, b) in L["ranges"][:1]:
                for i in range(a, b):
                    s = lines[i].strip()
                    if s and not fm[i] and not s.startswith(("|", "#", ">", "---")):
                        s = tm.strip_md(re.sub(r"^[-*]\s+", "", s))
                        L["q"] = (s[:170] + "…") if len(s) > 170 else s
                        break
        L["fields_raw"] = ""
        L["labels"] = []
        for rule in [r for r in rules if r["kind"] == "labels"]:   # the named parts the layer carries (required-parts check)
            pat = re.compile(rule["re"])
            for (a, b) in L["ranges"]:
                for i in range(a, b):
                    m = None if fm[i] else pat.match(lines[i])
                    if m:
                        L["labels"].append(clean_label(m.group(1)).lower())
        res["names"][L["name"]] = L["id"]
    res["layers"] = layer_recs
    res["fields"] = fields
    ipat = shape.get("instance")
    if ipat:
        for idx, (i, lv, txt) in enumerate(hs):
            if lv == 2 and re.search(ipat, txt):
                end = len(lines)
                for (j, lv2, _t) in hs[idx + 1:]:
                    if lv2 <= 2:
                        end = j
                        break
                body = "\n".join(lines[i + 1:end])
                nm = re.sub(r"^THE (?:WORKED )?(?:INSTANCE|PROOF)\W*", "", txt).strip()
                nm = re.split(r"\s+[—–]\s+|\s+\(", nm)[0].strip(" ,—–-")
                parked = next((l for l in lines[i + 1:end] if re.search(r"\bparked\b", l, re.I)), "")
                marker = re.search(r"`(⏸[^`]*)`", parked)
                res["instance"] = {"name": nm, "line": i + 1, "parked": parked.strip(), "marker": marker.group(1) if marker else "⏸", "marks": body.count("⏸")}
                break
    return res


def layer_tags(shape):
    """{layer id: 'static'|'dynamic'} read from the module the shape names (03: the state architecture's section 3 tables)."""
    spec = shape.get("tags")
    if not spec or spec.get("kind") != "layer_sections":
        return None
    p = os.path.join(SSOT, spec["doc"])
    if not os.path.exists(p):
        return {}
    lines = load_text(p).split("\n")
    hs = headings(lines)
    rng = section(lines, hs, spec["section"], spec.get("section_level"))
    out = {}
    if not rng:
        return out
    sub = [(i, lv, txt) for (i, lv, txt) in hs if rng[0] <= i < rng[1]]
    for idx, (i, lv, txt) in enumerate(sub):
        tag = next((t for t, pat in spec["sub"].items() if re.search(pat, txt)), None)
        if not tag:
            continue
        end = rng[1]
        for (j, lv2, _t) in sub[idx + 1:]:
            if lv2 <= lv:
                end = j
                break
        for t in tables_in(lines, (i + 1, end)):
            for r in t["rows"]:
                m = re.match(spec["id_re"], tm.strip_md(r[0]))
                if m:
                    out.setdefault(m.group(1), tag)
    return out


# ---------------------------------------------------------------- git: the version each field first appeared in

def field_history(main_path, parser=None):
    parser = parser or parse_main
    relp = rel(main_path)
    try:
        log = subprocess.run(["git", "-C", ROOT, "-c", "core.quotepath=off", "log", "--follow", "--name-only", "--format=@@%H", "--", relp],
                             capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60).stdout
    except Exception as e:
        miss(f"git log failed: {e}")
        return {}, []
    commits, cur = [], None
    for l in log.split("\n"):
        if l.startswith("@@"):
            cur = [l[2:], None]
            commits.append(cur)
        elif l.strip() and cur and cur[1] is None:
            cur[1] = l.strip().strip('"')
    by_version = {}
    for h, p in commits:   # newest first: keep each version's newest commit (autosaves catch a bump mid-edit)
        try:
            txt = subprocess.run(["git", "-C", ROOT, "-c", "core.quotepath=off", "show", f"{h}:{p}"], capture_output=True, encoding="utf-8",
                                 errors="replace", timeout=60).stdout
        except Exception:
            continue
        v = sv(str(parse_fm(txt.replace("\r\n", "\n")).get("version", "")))
        if v and v not in by_version:
            by_version[v] = txt.replace("\r\n", "\n")
    first = {}
    seen = []
    saved = list(MISSES)
    for v in sorted(by_version):
        r = parser(by_version[v])
        for name in r["fields"]:
            first.setdefault(name, sv_str(v))
        seen.append(sv_str(v))
    MISSES[:] = saved  # misses in old versions are history, not this build's problem
    return first, seen


# ---------------------------------------------------------------- main

def main():
    if len(sys.argv) < 2:
        print("usage: build.py <NN>")
        sys.exit(2)
    nn = sys.argv[1].zfill(2)
    TERMS = json.loads(load_text(os.path.join(TM_DIR, "terms.json")))
    BASE_TERMS = dict(TERMS)

    systems, docs, unresolved = load_systems()
    if nn not in systems:
        print("unknown system", nn, "- known:", ", ".join(systems))
        sys.exit(2)
    S = systems[nn]
    sdocs = [docs[d] for d in S["docs"]]

    # the main doc: the one the others are module_of; fall back to the TM registry
    counts = {}
    for d in sdocs:
        if d["module_of"]:
            counts[d["module_of"]] = counts.get(d["module_of"], 0) + 1
    main_id = max(counts, key=counts.get) if counts else None
    if (not main_id or main_id not in docs) and len(sdocs) == 1:
        main_id = sdocs[0]["id"]          # a one-doc system: that doc is the main doc (10/4)
    if not main_id or main_id not in docs:
        try:
            reg = json.loads(load_text(os.path.join(TM_DIR, "systems.json")))
            main_id = norm(reg[nn]["path"])
        except Exception:
            print("cannot find the main doc for", nn)
            sys.exit(1)
    shape = SHAPES.get(nn)       # 10/4: a system with its own layout is read by its own shape map; 02 keeps the PART A path
    if shape:
        main_id = norm(shape["main"])
        if main_id not in docs:
            print("shapes.json names a main doc that is not on disk:", shape["main"])
            sys.exit(1)
    MD = docs[main_id]
    main_path = os.path.join(ROOT, MD["path"])
    main_text = load_text(main_path)
    parser = (lambda t: parse_shape(t, shape)) if shape else parse_main
    P = parser(main_text)
    main_fm = parse_fm(main_text)
    first_seen, hist_versions = field_history(main_path, parser)

    LTAGS = layer_tags(shape) if shape else None
    names = P["names"]
    layers = P["layers"]
    lids = [L["id"] for L in layers]
    term_of_layer = {}
    for L in layers:
        k = None if shape else tm.LAYER_TERM_MAP.get(L["id"])
        term_of_layer[L["id"]] = k if k in TERMS else None
    short = S["name"].split()[0]

    # ---- doc roles
    for d in sdocs:
        if d["id"] == main_id:
            d["role"] = "main doc"
        elif d["category"].startswith("template") or "template" in d["id"]:
            d["role"] = "template"
        elif "synthesis" in d["type"] or "synthesis" in d["id"]:
            d["role"] = "synthesis module"
        elif d["module_of"]:
            d["role"] = "module"
        else:
            d["role"] = "doc"

    # ---- fields
    # 10/4 (BOLO 100 FU-1): a table titled "every field" means every field must carry a tag, whatever version added it
    every = bool(P.get("tag_every"))
    since = sv("0.0.0") if every else sv(P.get("tag_since") or "2.1.0")
    fields = []
    for name, f in P["fields"].items():
        intro = first_seen.get(name, "")
        tag = P["tags"].get(name)
        needs_tag = bool(intro) and sv(intro) >= since and not (f["origin"] == "declaration" and f["parent"])
        if not intro:
            needs_tag = True  # not in any committed version: new, must be tagged
        if shape:
            needs_tag = False  # a shaped system tags per layer or not at all (see the tag check)
        rec = {"name": name, "layers": f["layers"], "parent": f["parent"], "origin": f["origin"], "note": f["note"],
               "tag": tag, "tag_group": P["tag_groups"].get(name, ""), "intro": intro or "uncommitted", "needs_tag": needs_tag,
               "ids": sorted(f["ids"]), "scalar": name.isupper()}
        tkey = name.replace("_", "-")
        rec["term"] = tkey if tkey in TERMS else None
        fields.append(rec)
    tagged_unknown = [k for k in P["tags"] if k not in P["fields"]]
    for k in tagged_unknown:
        miss(f"tag table names `{k}` but no layer lists it")

    # ---- books
    lib = {b["id"]: b for b in P["library"]}
    feeds_book = []   # (book, layer, kind, cite)
    for b in P["library"]:
        for lid in b["feeds"]:
            feeds_book.append((b["id"], lid, "feeds hardest", b["line"]))
    for L in layers:
        for bid in L["src_ids"]:
            feeds_book.append((bid, L["id"], "cited in PART A", L["line"]))
    for lid, d in P["decl"].items():
        for bid in dict.fromkeys(re.findall(ID_RE, d["text"])):
            feeds_book.append((bid, lid, "cited in the declaration", d["line"]))
    book_ids = list(dict.fromkeys([b["id"] for b in P["library"]] + [x[0] for x in feeds_book]))

    # ---- synthetic hover terms (systems, docs, fields, uncarded books, fork)
    def tlink(k, label):
        return f"[[{k}|{label}]]" if k else label

    def layer_link(lid):
        L = next((x for x in layers if x["id"] == lid), None)
        return tlink(term_of_layer.get(lid), f"{lid} {L['name'] if L else ''}".strip())

    for s in systems.values():
        deps = ", ".join(tlink(f"sys:{t}", f"{t} {systems[t]['name']}") for t in sorted(s["deps"]))
        TERMS[f"sys:{s['id']}"] = {"t": f"{s['id']} {s['name']}", "k": "system",
                                   "d": f"{len(s['docs'])} docs · versions {s['vmin'] or '—'} to {s['vmax'] or '—'} · {s['open']} open ⧗ marks."
                                        + (f" Depends on {deps}." if deps else " No dependencies declared."),
                                   "w": s["folder"]}
    for d in docs.values():
        extra = ""
        if d["module_of"] and d["module_of"] in docs:
            extra = f" Module of {tlink('doc:' + d['module_of'], docs[d['module_of']]['id'])}."
        TERMS[f"doc:{d['id']}"] = {"t": d["id"], "k": d.get("role", "doc") + (f" · {d['version']}" if d["version"] else ""),
                                   "d": (tm.strip_md(d["purpose"])[:420] or "No purpose in frontmatter.") + extra
                                        + f" ⧗ {d['open']}.", "w": d["path"]}
    for f in fields:
        on = ", ".join(layer_link(l) for l in f["layers"])
        tag = (f"{f['tag']} ({f['tag_group']})" if f["tag"] else ("untagged" if f["needs_tag"] else f"no tag needed: predates {sv_str(since)}, the state module's Decision Test decides"))
        cites = ", ".join(tlink(i if i in TERMS else None, i) for i in f["ids"])
        TERMS[f"fld:{f['name']}"] = {"t": f["name"], "k": "field" + (f" · {f['tag']}" if f["tag"] else ""),
                                     "d": f"On {on}." + (f" Sub-field of {tlink('fld:' + f['parent'], f['parent'])}." if f["parent"] else "")
                                          + f" Tag: {tag}. First in {f['intro']}." + (f" Note: {f['note']}." if f["note"] else "")
                                          + (f" Cited with {cites}." if cites else "")
                                          + (f" Term: {tlink(f['term'], TERMS[f['term']]['t'])}." if f["term"] else ""),
                                     "w": MD["path"]}
    for bid in book_ids:
        if bid not in TERMS:
            ls = sorted({x[1] for x in feeds_book if x[0] == bid}, key=lambda x: [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", x)])
            TERMS[bid] = {"t": bid, "k": "book", "d": "Cited by " + ", ".join(layer_link(l) for l in ls) + ". No distill card in the term register yet.",
                          "w": f"_0.1_BVX_LEARN/KNOWLEDGE_AREAS/{bid}.md"}
    if P["fork"]:
        TERMS["x:fork"] = {"t": P["fork"]["title"], "k": "method rule", "d": tm.strip_md(P["fork"]["text"])[:600], "w": f"{MD['path']} · line {P['fork']['line']}"}
    if "storyform" not in TERMS:
        TERMS["storyform"] = {"t": "the storyform", "k": "external", "d": "The storyform feeds the last layer independently.", "w": ""}

    # ---- rendering helpers: auto-link with the register's own terms, then render with everything

    MARK = "\u2063"  # invisible separator: marks a field label so it renders as code inside the link

    def render(text):
        # auto-link the register's own terms first (it protects `code`), then turn known field names into field hover terms
        tm.TERMS = BASE_TERMS
        t = tm.auto_link_section(text)
        tm.TERMS = TERMS
        t = re.sub(r"`([A-Za-z][A-Za-z0-9_]*)`", lambda m: f"[[fld:{m.group(1)}|{MARK}{m.group(1)}{MARK}]]" if m.group(1) in P["fields"] else m.group(0), t)
        h = tm.render_inline(t)
        return re.sub(MARK + r"([^<" + MARK + r"]*)" + MARK, lambda m: '<code class="inl">' + m.group(1) + '</code>', h)

    tm.TERMS = TERMS
    missing_keys = sorted({k for L in layers for k in re.findall(r"\[\[([^\]|]+)", L["src_raw"]) if k not in TERMS})
    for k in missing_keys:
        miss(f"source key [[{k}]] not in terms.json")

    # ---- layers out
    layers_out = []
    for L in layers:
        lf = [f for f in fields if L["id"] in f["layers"]]
        order = {n: i for i, n in enumerate(f2["name"] for f2 in L["tfields"])}
        lf.sort(key=lambda f: (order.get(f["name"], 999), f["intro"]))
        d = P["decl"].get(L["id"])
        if not d and not shape:
            miss(f"{L['id']}: no domain declaration")
        layers_out.append({
            "id": L["id"], "name": L["name"], "q": L["q"], "tier": L["tier"], "term": term_of_layer.get(L["id"]),
            "src_html": render(L["src_raw"]), "src_ids": L["src_ids"], "src_links": L["src_links"], "line": L["line"],
            "fields": [f["name"] for f in lf],
            "decl_html": render(d["text"]) if d else "", "decl_line": d["line"] if d else None,
            "aux": bool(L.get("aux")), "tag": (LTAGS or {}).get(L["id"]),
        })

    # ---- feed edges (dedupe exact repeats, keep every cite)
    edges = {}
    for e in P["edges"]:
        k = (e["from"], e["to"], e["kind"])
        if k not in edges:
            edges[k] = {"from": e["from"], "to": e["to"], "kind": e["kind"], "cites": []}
        c = {"line": e["cite"]["line"], "text": e["cite"]["text"].replace("**", "")}
        if c not in edges[k]["cites"]:
            edges[k]["cites"].append(c)
    feed_edges = list(edges.values())

    # ---- DONE: the definition of done, every line with evidence
    # A check with "na": True does not apply to this system's layout; the reason is shown on the page and listed in the build output.
    checks = []

    def na(label, reason):
        return {"label": label, "ok": True, "na": True, "ev": [], "sum": "n/a for this layout: " + reason}

    ev = [{"k": d["file"], "v": d["version"] or "none", "ok": bool(d["version"]) and sv(d["version"]) >= (1, 0, 0)} for d in sdocs]
    checks.append({"label": f"Every {short.lower()} doc is at 1.0.0 or later", "ok": all(x["ok"] for x in ev), "ev": ev,
                   "sum": f"{sum(x['ok'] for x in ev)} of {len(ev)} docs"})
    ev = [{"k": d["file"], "v": f"⧗ {d['open']}", "ok": d["open"] == 0} for d in sdocs]
    checks.append({"label": "Open ⧗ marks = 0", "ok": all(x["ok"] for x in ev), "ev": ev, "sum": f"{sum(d['open'] for d in sdocs)} open across {len(sdocs)} docs"})
    mods = [d for d in sdocs if d["id"] != main_id]
    sys_ids = {d["id"] for d in sdocs}
    if shape and not mods:
        checks.append(na("Every other doc is a module_of a doc of this system", "the system has one doc, so there is no module to point anywhere"))
    elif shape:
        # a shaped system's docs may hang from more than one parent: a module must point at a doc of THIS system
        ev = [{"k": d["file"], "v": ("module_of " + d["module_of"]) if d["module_of"] else "no module_of",
               "ok": d["module_of"] in sys_ids} for d in mods]
        checks.append({"label": "Every other doc is a module_of a doc of this system", "ok": all(x["ok"] for x in ev), "ev": ev,
                       "sum": f"{sum(x['ok'] for x in ev)} of {len(ev)} point at a doc in {S['folder'].split('/')[-1]}"})
    else:
        ev = [{"k": d["file"], "v": ("module_of " + d["module_of"]) if d["module_of"] else "no module_of", "ok": d["module_of"] == main_id} for d in mods]
        checks.append({"label": "Every module carries module_of", "ok": all(x["ok"] for x in ev), "ev": ev, "sum": f"{sum(x['ok'] for x in ev)} of {len(ev)} point at {main_id}"})
    tlinks = list(dict.fromkeys(unquote(m.group(1)) for m in re.finditer(r"\]\(([^)]*template[^)]*\.md)\)", main_text)))
    ev = []
    for t in tlinks:
        p = os.path.normpath(os.path.join(os.path.dirname(main_path), t))
        ev.append({"k": os.path.basename(t), "v": (docs.get(norm(p), {}).get("version") or "exists") if os.path.exists(p) else "MISSING", "ok": os.path.exists(p)})
    if shape and not ev:
        checks.append(na("Every ingest template the main doc names exists", "the main doc names no ingest template, so there is nothing to find"))
    else:
        checks.append({"label": "Both ingest templates exist" if len(ev) == 2 else "Every ingest template the main doc names exists",
                       "ok": all(x["ok"] for x in ev), "ev": ev,
                       "sum": f"{sum(x['ok'] for x in ev)} of {len(ev)} linked from the main doc" if ev else "the main doc names no ingest template"})
    if shape:
        if shape.get("tags"):
            lt = LTAGS or {}
            ev = [{"k": f"{L['id']} {L['name']}", "v": lt.get(L["id"]) or "NO TAG", "ok": bool(lt.get(L["id"]))} for L in layers if not L.get("aux")]
            checks.append({"label": "Every layer carries a static/dynamic tag (read from the state module's section 3)", "ok": all(x["ok"] for x in ev), "ev": ev,
                           "sum": f"{sum(x['ok'] for x in ev)} of {len(ev)} layers tagged in {os.path.basename(shape['tags']['doc'])}"})
        else:
            checks.append(na("Every field carries a static/dynamic tag", shape["tags_na"]))
    else:
        need = [f for f in fields if f["needs_tag"]]
        untagged = [f for f in need if not f["tag"]]
        ev = [{"k": f["name"], "v": f"{f['intro']} · " + (f["tag"] or "UNTAGGED"), "ok": bool(f["tag"])} for f in sorted(need, key=lambda f: (bool(f["tag"]), f["intro"], f["name"]))]
        checks.append({"label": ("Every field carries a static/dynamic/derived tag" if P.get("tag_every") else f"Every field added {sv_str(since)}+ carries a static/dynamic tag"), "ok": not untagged, "ev": ev,
                       "sum": f"{len(need) - len(untagged)} of {len(need)} tagged" + (f" · untagged: {', '.join(f['name'] for f in untagged)}" if untagged else "")
                              + f" · first-seen from {len(hist_versions)} committed versions ({', '.join(hist_versions)})"})
    main_layers = [L for L in layers if not L.get("aux")]
    ev = [{"k": f"{L['id']} {L['name']}", "v": f"{len(L['src_ids']) + len(L['src_links'])} cited", "ok": (len(L['src_ids']) + len(L['src_links'])) > 0} for L in (main_layers if shape else layers)]
    checks.append({"label": "Every layer has at least one cited source", "ok": all(x["ok"] for x in ev), "ev": ev, "sum": f"{sum(x['ok'] for x in ev)} of {len(ev)} layers"})
    if shape:
        if shape.get("layers_need_fields"):
            ev = [{"k": f"{L['id']} {L['name']}", "v": f"{sum(1 for f in fields if L['id'] in f['layers'])} fields", "ok": any(L['id'] in f['layers'] for f in fields)} for L in main_layers]
            checks.append({"label": f"Every {shape['layer_word']} defines at least one named field", "ok": all(x["ok"] for x in ev), "ev": ev,
                           "sum": f"{sum(x['ok'] for x in ev)} of {len(ev)} {shape['layer_word']}s name a field"})
        if shape.get("required_parts"):
            need_parts = [x.lower() for x in shape["required_parts"]]
            ev = []
            for L in main_layers:
                have = set(L.get("labels", []))
                miss_p = [x for x in shape["required_parts"] if x.lower() not in have]
                ev.append({"k": f"{L['id']} {L['name']}", "v": ("all " + str(len(need_parts)) + " parts") if not miss_p else "missing: " + ", ".join(miss_p), "ok": not miss_p})
            checks.append({"label": f"Every {shape['layer_word']} carries its {len(need_parts)} parts ({', '.join(shape['required_parts'])})", "ok": all(x["ok"] for x in ev), "ev": ev,
                           "sum": f"{sum(x['ok'] for x in ev)} of {len(ev)} {shape['layer_word']}s complete"})
    inst = P["instance"] or {}
    inst_node = None
    if inst.get("name"):
        slug = re.sub(r"[^a-z0-9]+", "-", inst["name"].lower()).strip("-")
        cand = os.path.join(ROOT, "_CANON_NODES", f"{slug}-chart.md")
        if os.path.exists(cand):
            nt = load_text(cand)
            inst_node = {"path": rel(cand), "status": str(parse_fm(nt).get("status", "")), "marks": nt.count("⏸")}
    if shape and not inst:
        checks.append(na("Worked instance: fill pass parked by ruling", shape.get("instance_na", "the main doc has no worked-instance section")))
    else:
        if not inst.get("parked"):
            # RULED 10/4 (BOLO 100, "RAC" = rec): every worked-instance fill pass is parked to phase 2 by ruling
            inst = dict(inst, parked=inst.get("parked") or "Worked-instance fill pass parked to phase 2 by ruling (BOLO 100, 10/4).")
        ev = [{"k": "instance section", "v": f"{inst.get('marks', 0)} × {inst.get('marker', '⏸')}", "ok": bool(inst.get("parked"))}]
        if inst_node:
            ev.append({"k": os.path.basename(inst_node["path"]), "v": f"status: {inst_node['status']} · {inst_node['marks']} × ⏸", "ok": True})
        checks.append({"label": f"Worked instance: {inst.get('name', '—')} — fill pass parked by ruling", "ok": bool(inst.get("parked")), "ev": ev,
                       "sum": tm.strip_md(inst.get("parked", "no parking ruling found"))})
    # guard (10/4): a page that parsed no layers and no fields has checked nothing, so it cannot pass
    checks.insert(0, {"label": "The builder read the system's structure", "ok": bool(layers) and bool(fields),
                      "ev": [{"k": "layers", "v": str(len(layers)), "ok": bool(layers)}, {"k": "fields", "v": str(len(fields)), "ok": bool(fields)}],
                      "sum": f"{len(layers)} layers · {len(fields)} fields parsed from the main doc"})
    done = all(c["ok"] for c in checks)

    # what closed it: the current major version's entries
    curv = sv(MD["version"])
    closed = [v for v in P["versions"] if sv(v["v"]) and sv(v["v"])[0] == curv[0]]
    closed.sort(key=lambda v: sv(v["v"]), reverse=True)
    closed_out = []
    for v in closed:
        txt = v["text"]
        head, _, rest = txt.partition(":")
        items, depth, cur = [], 0, ""
        for ch_i, ch in enumerate(rest):   # split on " · " outside parentheses
            depth += (ch == "(") - (ch == ")")
            if depth == 0 and rest[ch_i:ch_i + 3] == " · ":
                items.append(cur.strip())
                cur = ""
                continue
            cur += ch
        items.append(cur.strip())
        items = [re.sub(r"^·\s*", "", x).strip() for x in items] if rest else [txt]
        closed_out.append({"v": v["v"], "date": v["date"], "head": render(head.strip()), "items": [render(x) for x in items if x], "line": v["line"]})

    # ---- TRACE matrix
    trace = {"cols": [b["id"] for b in P["library"]], "cells": {}, "fcells": {}}
    for bid, lid, kind, line in feeds_book:
        if bid in lib:
            c = trace["cells"].setdefault(f"{lid}|{bid}", {"strong": False, "how": []})
            if kind == "feeds hardest":
                c["strong"] = True
            if kind not in c["how"]:
                c["how"].append(kind)
    for f in fields:
        for bid in f["ids"]:
            if bid in lib:
                trace["fcells"][f"{f['name']}|{bid}"] = 1

    # ---- GRAPH
    gn, gl = {}, []

    def node(i, label, kind, t=None, extra=None):
        if i not in gn:
            gn[i] = {"id": i, "label": label, "kind": kind, "t": t}
            if extra:
                gn[i].update(extra)

    for s in systems.values():
        node(f"sys:{s['id']}", f"{s['id']} {s['name']}", "system", f"sys:{s['id']}")
    for d in docs.values():
        node(f"doc:{d['id']}", d["id"].replace("ssot_", ""), "doc", f"doc:{d['id']}", {"sys": d["sys"]})
        gl.append({"s": f"sys:{d['sys']}", "t": f"doc:{d['id']}", "k": "contains"})
        for t in d["deps"]:
            gl.append({"s": f"doc:{d['id']}", "t": f"doc:{t}", "k": "depends-on"})
        for t in d["deps_sys"]:
            gl.append({"s": f"doc:{d['id']}", "t": f"sys:{t}", "k": "depends-on"})
        if d["module_of"] and d["module_of"] in docs:
            gl.append({"s": f"doc:{d['id']}", "t": f"doc:{d['module_of']}", "k": "module-of"})
    for L in layers:
        node(f"lay:{L['id']}", f"{L['id']} {L['name']}", "layer", term_of_layer.get(L["id"]))
        gl.append({"s": f"doc:{main_id}", "t": f"lay:{L['id']}", "k": "defines"})
    for f in fields:
        node(f"fld:{f['name']}", f["name"], "field", f"fld:{f['name']}")
        for lid in f["layers"]:
            gl.append({"s": f"lay:{lid}", "t": f"fld:{f['name']}", "k": "layer-has-field"})
    for e in feed_edges:
        a = "lay:" + e["from"] if e["from"] in lids else ("x:" + e["from"])
        b = "lay:" + e["to"] if e["to"] in lids else ("x:" + e["to"])
        for x in (a, b):
            if x == "x:storyform":
                node(x, "the storyform", "external", "storyform")
            if x == "x:fork":
                node(x, P["fork"]["title"] if P["fork"] else "fork", "external", "x:fork")
        gl.append({"s": a, "t": b, "k": "layer-feeds-layer", "kind": e["kind"]})
    for bid in book_ids:
        node(f"bk:{bid}", bid, "book", bid, {"title": tm.strip_md(lib[bid]["book"]) if bid in lib else ""})
    seen_bl = set()
    for bid, lid, kind, line in feeds_book:
        if (bid, lid) in seen_bl:
            continue
        seen_bl.add((bid, lid))
        gl.append({"s": f"bk:{bid}", "t": f"lay:{lid}", "k": "source-feeds-layer"})
    gl = [l for l in gl if l["s"] in gn and l["t"] in gn]

    # ---- meta + data
    data = {
        "meta": {"key": nn, "short": short.upper(), "system": S["name"], "main": main_id, "main_path": MD["path"], "version": MD["version"],
                 "last_updated": MD["last_updated"], "trunk": str(main_fm.get("trunk", "")), "applies_to": main_fm.get("applies_to", []),
                 "done": done, "shaped": bool(shape), "built": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "builder": "_tools/review/build.py",
                 "out": f"_tools/review/out/REVIEW-{nn}.html", "hist": hist_versions, "status": tm.strip_md(str(main_fm.get("status", "")))[:900]},
        "systems": [{k: s[k] for k in ("id", "name", "folder", "docs", "open", "vmin", "vmax", "deps")} for s in systems.values()],
        "docs": {d["id"]: {k: d.get(k) for k in ("id", "sys", "path", "file", "version", "role", "purpose", "module_of", "deps", "deps_sys", "open", "last_updated", "category")}
                 for d in sdocs},
        "layers": layers_out,
        "tiers": P["tiers"], "tier_note": P.get("tier_note", ""),
        "fields": {f["name"]: f for f in fields},
        "feeds": feed_edges,
        "fork": ({"title": P["fork"]["title"], "line": P["fork"]["line"], "paths": P["fork"]["paths"], "entry": P["fork"]["entry"]} if P["fork"] else None),
        "binding": ({"line": P["binding"]["line"], "html": render(P["binding"]["text"])} if P["binding"] else None),
        "derived": [{"name": x["name"], "formula": x["formula"], "layers": [lid for _, lid in layer_mentions(x["formula"], names)]} for x in P["derived"]],
        "library": [{"id": b["id"], "book_html": render(b["book"]), "feeds": b["feeds"], "gives_html": render(b["gives"]), "line": b["line"]} for b in P["library"]],
        "trace": trace,
        "checks": checks, "closed": closed_out,
        "instance": {"name": inst.get("name"), "marks": inst.get("marks", 0), "node": inst_node},
        "graph": {"nodes": list(gn.values()), "links": gl},
        "terms": TERMS,
    }

    text_json = json.dumps(data, ensure_ascii=False, default=list).replace("</", "<\\/")
    tpl = load_text(os.path.join(HERE, "template.html"))
    assert tpl.count("/*__DATA__*/null") == 1, "template.html must hold exactly one /*__DATA__*/null slot"
    title = f"{short.capitalize()} System Review"
    frag = tpl.replace("/*__DATA__*/null", text_json).replace("<title>System Review</title>", f"<title>{tm.esc(title)}</title>")
    out_dir = os.path.join(HERE, "out")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"REVIEW-{nn}.html")
    with io.open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(frag)

    kinds = {}
    for n in gn.values():
        kinds[n["kind"]] = kinds.get(n["kind"], 0) + 1
    print(f"REVIEW {nn} · {short} {MD['version']} · systems {len(systems)} · docs {len(docs)} ({len(sdocs)} in system) · layers {len(main_layers)}{(' + ' + str(len(layers) - len(main_layers)) + ' aux') if len(layers) != len(main_layers) else ''} "
          f"· fields {len(fields)} · feeds {len(feed_edges)} · books {len(book_ids)} (library {len(P['library'])})")
    print(f"graph: {len(gn)} nodes ({', '.join(f'{k} {v}' for k, v in sorted(kinds.items()))}) · {len(gl)} edges")
    print("DONE:", "ALL PASS" if done else "OPEN", "·", " | ".join(("n/a " if c.get("na") else ("✓ " if c["ok"] else "✗ ")) + c["label"] for c in checks))
    for c in checks:
        if c.get("na"):
            print("n/a:", c["label"], "->", c["sum"])
        elif not c["ok"]:
            bad = [x for x in c["ev"] if not x["ok"]]
            print("FAIL:", c["label"], "|", c["sum"][:200], "|", "; ".join(f"{x['k']} [{x['v']}]" for x in bad)[:1500])
    if unresolved:
        print(f"note: {len(unresolved)} dependency string(s) across all systems name no doc on disk (drawn to the system when the number is known)")
    if MISSES:
        print("parse misses:")
        for m in MISSES:
            print(" -", m)
    else:
        print("parse misses: none")
    print("wrote", rel(out_path), f"({os.path.getsize(out_path) // 1024} KB)")


if __name__ == "__main__":
    main()
