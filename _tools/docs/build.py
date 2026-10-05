"""THE REFERENCE — build (BOLO 100, ruled 10/4 "Rick").

Usage:  python _tools/docs/build.py

One docs site, the reference type (DOC-SOP 1.2): a side panel down the left, one doc in the
center, its contents on the right. Nothing on the page is hand-typed except the landing page
(_tools/docs/landing.md, the one concept page). Every doc is rendered from disk at build time.

Inputs : ShroomsQ/_CANON/_SSOT/0*/**/*.md     the systems (top-level docs + their shelves)
         ShroomsQ/_CANON/_AUTHORITATIVE/**/*.md the authoritative story docs
         _CANON_NODES/*.md                      the story canon nodes
         ShroomsQ/_CANON/_DOCS/<system>/<doc>/*.md the core docs, four types each (BOLO 102, 10/5)
         _tools/docs/landing.md                 the concept landing page
         _tools/tm/terms.json                   the hover-term register (shared with TM + review)
         _tools/tm/template.html                the Command's color tokens (copied, never forked)
Outputs: _tools/docs/out/REFERENCE.html         an artifact fragment (no doctype/html/head/body)

RANGE (the check, at the end): every .md found is in the side panel exactly once; prints counts.
"""
import html
import io
import json
import os
import re
import sys

import markdown
import yaml

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SSOT = os.path.join(ROOT, "ShroomsQ", "_CANON", "_SSOT")
AUTH = os.path.join(ROOT, "ShroomsQ", "_CANON", "_AUTHORITATIVE")
NODES = os.path.join(ROOT, "_CANON_NODES")
DOCS = os.path.join(ROOT, "ShroomsQ", "_CANON", "_DOCS")
TM = os.path.join(ROOT, "_tools", "tm")
OUT = os.path.join(HERE, "out", "REFERENCE.html")

TERMS = json.load(io.open(os.path.join(TM, "terms.json"), encoding="utf-8"))

# the reading order of the systems (Touchstones first: built last, read first)
SYSTEM_NAMES = {
    "00": "Base", "01": "Narrative frameworks", "02": "Character", "03": "Setting", "04": "Plot",
    "05": "Worldbuilding", "06": "Theme", "07": "Style", "08": "Tracking", "09": "Operations",
}
TYPE_LABEL = {"concept": "Concept", "reference": "Reference", "how-to": "How-to", "tutorial": "Tutorial"}
SYSTEM_ORDER = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]   # the numbers ARE the reading order (BOLO 103, 10/5)


def read(p):
    return io.open(p, encoding="utf-8", errors="replace").read()


def split_front(text):
    t = text.lstrip("﻿")
    m = re.match(r"\s*---\n(.*?)\n---\s*\n", t, re.S)
    if not m:
        return {}, t
    try:
        fm = yaml.safe_load(m.group(1)) or {}
        if not isinstance(fm, dict):
            fm = {}
    except Exception:
        fm = {}
    return fm, t[m.end():]


def clean_title(s):
    s = re.sub(r"[\U0001F000-\U0001FFFF☀-➿️]", "", s or "")
    s = re.sub(r"[*_`#]", "", s).strip()
    return s


def title_of(fm, body, path):
    if fm.get("title"):
        return clean_title(str(fm["title"]))
    m = re.search(r"^#\s+(.+)$", body, re.M)
    if m:
        return clean_title(m.group(1))[:120]
    return clean_title(os.path.splitext(os.path.basename(path))[0].replace("_", " "))


def slug(s, used):
    b = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60] or "doc"
    k, i = b, 2
    while k in used:
        k, i = f"{b}-{i}", i + 1
    used.add(k)
    return k


# ---------------------------------------------------------------- hover terms

TERM_KEYS = sorted(((k, v.get("t", "")) for k, v in TERMS.items() if len(v.get("t", "")) >= 4),
                   key=lambda kv: -len(kv[1]))


def autolink(md):
    """First mention of each register term per doc becomes [[key|text]]; code and links are protected."""
    store = []

    def protect(pat, s, fl=0):
        def r(m):
            store.append(m.group(0))
            return f"\x00{len(store) - 1}\x00"
        return re.sub(pat, r, s, flags=fl)

    t = protect(r"```.*?```", md, re.S)
    t = protect(r"`[^`\n]+`", t)
    t = protect(r"\[\[[^\]]*\]\]", t)
    t = protect(r"\[[^\]]*\]\([^)]*\)", t)
    t = protect(r"<[^>\n]+>", t)
    t = protect(r"^#+ .*$", t, re.M)                    # headings stay plain
    for key, disp in TERM_KEYS:
        m = re.search(r"(?<![\w.-])" + re.escape(disp) + r"(?![\w-])", t, flags=re.I)
        if m:
            store.append(f"[[{key}|{m.group(0)}]]")
            t = t[:m.start()] + f"\x00{len(store) - 1}\x00" + t[m.end():]
    while "\x00" in t:
        t = re.sub(r"\x00(\d+)\x00", lambda m: store[int(m.group(1))], t)
    return t


def wiki(s):
    def r(m):
        k, label = m.group(1).strip(), m.group(2)
        g = TERMS.get(k)
        shown = html.escape(label or (g["t"] if g else k))
        return f'<a class="t" data-t="{html.escape(k)}" tabindex="0">{shown}</a>' if g else shown
    return re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", r, s)


# ---------------------------------------------------------------- render one doc

MD = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])


def render(body, doc_id, by_stem, live_mermaid=True, here=None, by_path=None):
    body = re.sub(r"(?is)<script.*?</script>", "", body)
    body = autolink(body)

    def link(m):
        txt, url = m.group(1), m.group(2).strip()
        if re.match(r"^https?://", url):
            return m.group(0)
        rel = url.split("#")[0].replace("%20", " ")
        if by_path and rel:
            for base in ([here] if here else []) + [ROOT]:
                tgt = by_path.get(os.path.abspath(os.path.join(base, rel)))
                if tgt:
                    return f"[{txt}](#{tgt})"
        stem = os.path.splitext(os.path.basename(rel))[0]
        stem = re.sub(r"^[^\w]+\s*", "", stem)
        tgt = by_stem.get(stem.lower())
        if tgt:
            return f"[{txt}](#{tgt})"
        return f"[{txt}](#nolink)"
    body = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)", link, body)

    MD.reset()
    h = MD.convert(body)
    h = wiki(h)
    if live_mermaid:   # the shelves hold ~1,560 diagrams; drawing them all would stall the page, so they stay as source
        h = re.sub(r'<pre><code class="language-mermaid">(.*?)</code></pre>',
                   lambda m: f'<pre class="mermaid">{m.group(1)}</pre>', h, flags=re.S)
    h = re.sub(r'<a href="#nolink">(.*?)</a>', r'<span class="pathref">\1</span>', h, flags=re.S)
    h = h.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")
    h = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', h)

    toc, n = [], [0]

    def head(m):
        lvl, inner = m.group(1), m.group(2)
        n[0] += 1
        hid = f"{doc_id}~{n[0]}"
        if lvl in ("2", "3"):
            toc.append((int(lvl), re.sub(r"<[^>]+>", "", inner)[:90], hid))
        return f'<h{lvl} id="{hid}">{inner}</h{lvl}>'
    h = re.sub(r"<h([1-6])>(.*?)</h\1>", head, h, flags=re.S)
    return h, toc


# ---------------------------------------------------------------- gather

def gather():
    docs, groups, used = [], [], set()

    def add(group, path, kind):
        fm, body = split_front(read(path))
        d = {"path": path, "rel": os.path.relpath(path, ROOT).replace("\\", "/"), "fm": fm, "body": body,
             "title": title_of(fm, body, path), "kind": kind, "shelf": bool(group.get("shelf")),
             "core": bool(group.get("core"))}
        d["id"] = slug(d["title"], used)
        docs.append(d)
        group["docs"].append(d)

    landing = os.path.join(HERE, "landing.md")
    start = {"name": "Start here", "key": "start", "docs": [], "open": True, "top": "start", "toptitle": "Start here"}
    groups.append(start)
    if os.path.exists(landing):
        add(start, landing, "concept")
    folders = {re.match(r"(\d\d)_", f).group(1): os.path.join(SSOT, f)
               for f in os.listdir(SSOT) if re.match(r"\d\d_", f)}
    ts = os.path.join(folders["01"], "📐 ssot_01_touchstones_register.md")
    if os.path.exists(ts):
        add(start, ts, "reference")

    for nn in SYSTEM_ORDER:
        base = folders[nn]
        top = {"top": nn, "toptitle": f"{nn} · {SYSTEM_NAMES[nn]}"}
        dsys = os.path.join(DOCS, os.path.basename(base))
        if os.path.isdir(dsys):
            cg = {"name": "The docs", "key": f"{nn}-docs", "docs": [], "open": False, "core": True, "bydoc": [], **top}
            groups.append(cg)
            for stem_dir in sorted(os.listdir(dsys), key=str.lower):
                sd = os.path.join(dsys, stem_dir)
                if not os.path.isdir(sd):
                    continue
                n0 = len(cg["docs"])
                for f in sorted(x for x in os.listdir(sd) if x.lower().endswith(".md")):
                    fm, _ = split_front(read(os.path.join(sd, f)))
                    add(cg, os.path.join(sd, f), str((fm or {}).get("type") or "reference"))
                pages = cg["docs"][n0:]
                for d in pages:
                    d["navlabel"] = TYPE_LABEL.get(d["kind"], d["kind"])
                if pages:
                    label = re.sub(r"\s*:\s*(concept|reference|how-to|tutorial)\s*$", "", pages[0]["title"], flags=re.I)
                    cg["bydoc"].append((label, pages))
        g = {"name": "Source docs", "key": nn, "docs": [], "open": False, **top}
        groups.append(g)
        for f in sorted(os.listdir(base), key=str.lower):
            p = os.path.join(base, f)
            if f.lower().endswith(".md") and os.path.isfile(p) and os.path.abspath(p) != os.path.abspath(ts):
                add(g, p, "reference")
        for dp, dns, fns in sorted(os.walk(base)):
            dns.sort(key=str.lower)
            if dp == base or "_ARCHIVE" in dp:
                continue
            mds = sorted(f for f in fns if f.lower().endswith(".md"))
            if not mds:
                continue
            sub = os.path.relpath(dp, base).replace("\\", " / ")
            sg = {"name": f"Shelf · {sub}", "key": f"{nn}-shelf", "docs": [], "open": False, "shelf": True, **top}
            groups.append(sg)
            for f in mds:
                add(sg, os.path.join(dp, f), "reference")

    for dp, dns, fns in sorted(os.walk(AUTH)):
        mds = sorted(f for f in fns if f.lower().endswith(".md"))
        if mds:
            g = {"name": os.path.relpath(dp, AUTH).replace("\\", " / "), "key": "story", "docs": [], "open": False,
                 "top": "stories", "toptitle": "Stories"}
            groups.append(g)
            for f in mds:
                add(g, os.path.join(dp, f), "reference")

    node_files = sorted(f for f in os.listdir(NODES) if f.lower().endswith(".md"))
    buckets = {}
    for f in node_files:
        pre = f.split("-")[0].lower()
        buckets.setdefault(pre, []).append(f)
    big = {k: v for k, v in buckets.items() if len(v) >= 3}
    misc = sorted(f for k, v in buckets.items() if len(v) < 3 for f in v)
    for k in sorted(big):
        g = {"name": f"Canon nodes · {k}", "key": "story", "docs": [], "open": False, "top": "stories", "toptitle": "Stories"}
        groups.append(g)
        for f in big[k]:
            add(g, os.path.join(NODES, f), "reference")
    if misc:
        g = {"name": "Canon nodes · other", "key": "story", "docs": [], "open": False, "top": "stories", "toptitle": "Stories"}
        groups.append(g)
        for f in misc:
            add(g, os.path.join(NODES, f), "reference")
    return docs, groups


# ---------------------------------------------------------------- page

def tokens_from_tm():
    t = read(os.path.join(TM, "template.html"))
    m = re.search(r"<style>(.*?)\n\s*\* \{ box-sizing", t, re.S)
    css = m.group(1)
    css = re.sub(r"/\*.*?\*/", "", css, count=1, flags=re.S)
    return css


def meta_line(d):
    fm = d["fm"]
    bits = []
    if fm.get("version"):
        bits.append(f'<span><i>version</i>{html.escape(str(fm["version"]))}</span>')
    if fm.get("state"):
        bits.append(f'<span><i>state</i>{html.escape(str(fm["state"]))}</span>')
    lu = fm.get("last_updated") or fm.get("updated") or fm.get("reviewed")
    if lu:
        bits.append(f'<span><i>reviewed</i>{html.escape(str(lu))}</span>')
    if fm.get("trunk"):
        bits.append(f'<span><i>trunk</i>{html.escape(str(fm["trunk"]))}</span>')
    if fm.get("module_of"):
        bits.append(f'<span><i>module of</i>{html.escape(str(fm["module_of"]))}</span>')
    return "".join(bits)


def header(d):
    fm = d["fm"]
    if d.get("core"):
        who, what = str(fm.get("for") or ""), str(fm.get("does") or "")
    elif d["kind"] == "concept":
        who, what = "Chief, before phase 2, reading the whole stack", "Explains how the pieces fit, so every other page makes sense."
    else:
        story = d["rel"].startswith("_CANON_NODES") or "_AUTHORITATIVE" in d["rel"]
        who = "Chief and the writers, on the story" if story else "Chief and the writers, mid-build"
        what = str(fm.get("purpose") or "").strip() or "No purpose line yet."
        what = re.sub(r"\s+", " ", what)
    return (f'<header class="dh"><div class="eyebrow">{d["kind"]}</div><h1>{html.escape(d["title"])}</h1>'
            f'<dl class="three"><div><dt>Who it\'s for</dt><dd>{html.escape(who)}</dd></div>'
            f'<div><dt>What it does</dt><dd>{wiki(html.escape(what))}</dd></div>'
            f'<div><dt>Type</dt><dd>{d["kind"]}</dd></div></dl>'
            f'<div class="meta">{meta_line(d)}<span class="path">{html.escape(d["rel"])}</span></div></header>')


def main():
    docs, groups = gather()
    by_stem, by_path = {}, {os.path.abspath(d["path"]): d["id"] for d in docs}
    for d in docs:
        if d.get("core"):
            continue
        st = re.sub(r"^[^\w]+\s*", "", os.path.splitext(os.path.basename(d["path"]))[0]).lower()
        by_stem.setdefault(st, d["id"])

    arts, tocs = [], {}
    for d in docs:
        body = d["body"]
        body = re.sub(r"^\s*#\s+.+\n", "", body, count=1)      # the header carries the title
        body = re.sub(r"^\*\*Who it's for:\*\*.*\n", "", body, count=1, flags=re.M)   # the header carries the three
        h, toc = render(body, d["id"], by_stem, live_mermaid=not d["shelf"],
                        here=os.path.dirname(d["path"]), by_path=by_path)
        tocs[d["id"]] = toc
        arts.append(f'<article id="{d["id"]}" class="doc" hidden>{header(d)}<div class="body">{h}</div>'
                    f'<footer class="df"><button type="button" class="mark" data-mark="{d["id"]}">Mark read</button>'
                    f'<span class="nx"></span></footer></article>')

    def item(d):
        return (f'<a class="ni" href="#{d["id"]}" data-id="{d["id"]}"><b class="dot"></b>'
                f'<span>{html.escape(d.get("navlabel") or d["title"])}</span>'
                f'<em>{html.escape(str(d["fm"].get("version") or ""))}</em></a>')

    def sub(g):
        if g.get("bydoc"):   # the docs: one row per doc, its four pages inside
            body = "".join(f'<details class="grp doc"><summary><span>{html.escape(lbl)}</span><small>{len(ps)}</small></summary>'
                           f'{"".join(item(d) for d in ps)}</details>' for lbl, ps in g["bydoc"])
        else:
            body = "".join(item(d) for d in g["docs"])
        cls = "grp sub" + (" shelf" if g.get("shelf") else "")
        return (f'<details class="{cls}" data-key="{g["key"]}"><summary><span>{html.escape(g["name"])}</span>'
                f'<small>{len(g["docs"])}</small></summary>{body}</details>')

    nav, tops = [], {}
    for g in groups:
        if g["docs"]:
            tops.setdefault(g["top"], []).append(g)
    for key, gs in tops.items():
        if key == "start":
            g = gs[0]
            nav.append(f'<details class="grp sys" data-key="start" open><summary><span>{html.escape(g["name"])}</span>'
                       f'<small>{len(g["docs"])}</small></summary>{"".join(item(d) for d in g["docs"])}</details>')
            continue
        n = sum(len(g["docs"]) for g in gs)
        main = "".join(sub(g) for g in gs if not g.get("shelf"))
        shelves = [g for g in gs if g.get("shelf")]
        if shelves:   # STOWAGE (provisional 10/5): every shelf of the system stowed under one subheading
            rows = "".join(f'<details class="grp doc shelf" data-key="{g["key"]}"><summary><span>{html.escape(g["name"].replace("Shelf · ", ""))}</span>'
                           f'<small>{len(g["docs"])}</small></summary>{"".join(item(d) for d in g["docs"])}</details>' for g in shelves)
            main += (f'<details class="grp sub shelf" data-key="{key}-stowage"><summary><span>Stowage</span>'
                     f'<small>{sum(len(g["docs"]) for g in shelves)}</small></summary>{rows}</details>')
        nav.append(f'<details class="sys" data-key="{key}"><summary><span>{html.escape(gs[0]["toptitle"])}</span>'
                   f'<small>{n}</small></summary>{main}</details>')

    used_terms = set(re.findall(r'data-t="([^"]+)"', "".join(arts)))
    G = {k: TERMS[k] for k in used_terms if k in TERMS}
    order = [d["id"] for d in docs]

    page = PAGE
    page = page.replace("/*TOKENS*/", tokens_from_tm())
    page = page.replace("<!--NAV-->", "".join(nav))
    page = page.replace("<!--ARTICLES-->", "\n".join(arts))
    page = page.replace("/*DATA*/", "const G=" + json.dumps(G, ensure_ascii=False) + ";const TOC=" +
                        json.dumps(tocs, ensure_ascii=False) + ";const ORDER=" + json.dumps(order) + ";")
    page = page.replace("<!--COUNT-->", str(len(docs)))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    io.open(OUT, "w", encoding="utf-8").write(page)

    # RANGE: every .md on disk is in the side panel exactly once
    found = set()
    for base in (SSOT, AUTH, DOCS):
        if not os.path.isdir(base):
            continue
        for dp, _, fns in os.walk(base):
            if "_ARCHIVE" in dp:
                continue
            found |= {os.path.abspath(os.path.join(dp, f)) for f in fns if f.lower().endswith(".md")}
    found |= {os.path.abspath(os.path.join(NODES, f)) for f in os.listdir(NODES) if f.lower().endswith(".md")}
    listed = [os.path.abspath(d["path"]) for d in docs if d["kind"] != "concept" or d.get("core")]
    missing = found - set(listed)
    dupes = len(listed) - len(set(listed))
    print(f"docs {len(docs)} · groups {sum(1 for g in groups if g['docs'])} · terms wired {len(G)} · "
          f"{os.path.getsize(OUT) // 1024} KB → {os.path.relpath(OUT, ROOT)}")
    print(f"RANGE: on disk {len(found)} · in panel {len(set(listed))} · missing {len(missing)} · dupes {dupes}"
          f" · landing {'yes' if any(d['kind'] == 'concept' for d in docs) else 'NO'}")
    for m in sorted(missing)[:10]:
        print("  missing:", os.path.relpath(m, ROOT))
    if missing or dupes:
        sys.exit(1)


PAGE = r"""<title>Command Reference</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* THE REFERENCE · layout: one 44px strip, the side panel left (300px), the doc center (~70ch), its contents right (220px).
   Tokens copied from the TM page at build time (DARK first, light face E-INK gray). */
/*TOKENS*/
* { box-sizing: border-box; }
html, body { height: 100%; }
body { margin: 0; background: var(--bg); color: var(--ink); font-family: var(--body); font-size: 16px; line-height: 1.55; -webkit-font-smoothing: antialiased; overflow: hidden; }
a { color: var(--link); }
button { font: inherit; color: inherit; }
button:focus-visible, a:focus-visible, input:focus-visible, summary:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.strip { height: calc(44px + env(safe-area-inset-top, 0px)); padding: env(safe-area-inset-top, 0px) 16px 0; display: flex; align-items: center; gap: 14px; border-bottom: 1px solid var(--line); background: var(--panel); }
.strip h1 { margin: 0; font-family: var(--display); font-weight: 800; font-size: 20px; letter-spacing: .04em; text-transform: uppercase; white-space: nowrap; }
.strip h1 b { color: var(--accent); }
.strip .sp { flex: 1; }
.strip .count { font-family: var(--mono); font-size: 12px; color: var(--ink-2); font-variant-numeric: tabular-nums; white-space: nowrap; }
.strip .count b { color: var(--accent); }
.strip .bar { width: 120px; height: 4px; background: var(--line); position: relative; }
.strip .bar i { position: absolute; inset: 0 auto 0 0; background: var(--accent); width: 0; }
#menu { display: none; background: none; border: 1px solid var(--line-2); padding: 4px 10px; font-family: var(--mono); font-size: 12px; cursor: pointer; }
.shell { display: grid; grid-template-columns: 300px minmax(0, 1fr) 220px; height: calc(100% - 44px - env(safe-area-inset-top, 0px)); }
.side { border-right: 1px solid var(--line); overflow-y: auto; background: var(--panel); padding-block: 10px 40px; }
.side .search { padding: 0 12px 10px; position: sticky; top: -10px; background: var(--panel); padding-top: 10px; z-index: 2; }
.side input { width: 100%; background: var(--bg); border: 1px solid var(--line-2); color: var(--ink); padding: 7px 10px; font-family: var(--mono); font-size: 13px; }
.side .filters { display: flex; gap: 6px; margin-top: 8px; flex-wrap: wrap; }
.side .filters button { background: none; border: 1px solid var(--line-2); font-family: var(--mono); font-size: 11px; padding: 2px 8px; cursor: pointer; color: var(--ink-2); }
.side .filters button[aria-pressed="true"] { border-color: var(--accent); color: var(--accent); }
.grp { border-top: 1px solid var(--line); }
.grp summary { list-style: none; cursor: pointer; display: flex; align-items: baseline; gap: 8px; padding: 9px 14px 7px; font-family: var(--display); font-weight: 700; font-size: 15.5px; letter-spacing: .05em; text-transform: uppercase; color: var(--ink); }
.grp summary::-webkit-details-marker { display: none; }
.grp summary::before { content: "▸"; color: var(--ink-3); font-size: 11px; width: 10px; }
.grp[open] summary::before { content: "▾"; }
.grp summary span { flex: 1; min-width: 0; }
.grp summary small { font-family: var(--mono); font-size: 11px; color: var(--ink-3); font-weight: 400; }
.sys { border-top: 1px solid var(--line); }
.sys > summary { list-style: none; cursor: pointer; display: flex; align-items: baseline; gap: 8px; padding: 9px 14px 7px; font-family: var(--display); font-weight: 700; font-size: 15.5px; letter-spacing: .02em; }
.sys > summary::-webkit-details-marker { display: none; }
.sys > summary::before { content: "\25B8"; color: var(--ink-3); font-size: 11px; width: 10px; }
.sys[open] > summary::before { content: "\25BE"; }
.sys > summary span { flex: 1; min-width: 0; }
.sys > summary small { font-family: var(--mono); font-size: 11px; color: var(--ink-3); font-weight: 400; }
.grp.sub, .grp.doc { border-top: 0; }
.grp.sub > summary { font-size: 13.5px; color: var(--ink-2); padding: 6px 14px 5px 26px; }
.grp.sub[open] > summary::before, .grp.doc[open] > summary::before { content: "\25BE"; }
.grp.doc > summary { font-family: inherit; font-weight: 400; font-size: 13px; color: var(--ink-2); padding: 4px 14px 4px 38px; letter-spacing: 0; }
.grp.sub .ni { padding-left: 40px; }
.grp.doc .ni { padding-left: 52px; }
.ni { display: grid; grid-template-columns: 10px minmax(0, 1fr) auto; gap: 8px; align-items: baseline; padding: 4px 14px 4px 26px; text-decoration: none; color: var(--ink-2); font-size: 14px; line-height: 1.35; }
.ni:hover { background: var(--panel-2); color: var(--ink); }
.ni.cur { background: var(--accent-soft); color: var(--ink); box-shadow: inset 3px 0 0 var(--accent); }
.ni em { font-style: normal; font-family: var(--mono); font-size: 10.5px; color: var(--ink-3); }
.ni .dot { width: 7px; height: 7px; border: 1px solid var(--line-2); border-radius: 50%; transform: translateY(-1px); }
.ni.read .dot { background: var(--good); border-color: var(--good); }
.ni[hidden] { display: none; }
main { overflow-y: auto; padding-block: 28px 80px; padding-inline: 40px; min-width: 0; }
.doc { max-width: 76ch; margin: 0 auto; }
.dh .eyebrow { font-family: var(--mono); font-size: 11px; letter-spacing: .14em; text-transform: uppercase; color: var(--accent); }
.dh h1 { font-family: var(--display); font-weight: 800; font-size: 40px; line-height: 1.05; margin: 6px 0 16px; text-wrap: balance; text-transform: uppercase; letter-spacing: .01em; }
.three { display: grid; grid-template-columns: 9.5em minmax(0, 1fr); gap: 4px 14px; margin: 0 0 12px; padding: 12px 14px; border: 1px solid var(--line); background: var(--panel); }
.three div { display: contents; }
.three dt { font-family: var(--mono); font-size: 11px; letter-spacing: .1em; text-transform: uppercase; color: var(--ink-3); padding-top: 3px; }
.three dd { margin: 0; font-size: 15px; color: var(--ink); }
.meta { display: flex; flex-wrap: wrap; gap: 6px 16px; font-family: var(--mono); font-size: 11.5px; color: var(--ink-2); padding-bottom: 18px; border-bottom: 1px solid var(--line); margin-bottom: 22px; }
.meta i { font-style: normal; color: var(--ink-3); margin-right: 6px; text-transform: uppercase; letter-spacing: .08em; font-size: 10px; }
.meta .path { color: var(--ink-3); overflow-wrap: anywhere; }
.body { overflow-wrap: break-word; }
.body h1, .body h2, .body h3, .body h4 { font-family: var(--display); text-transform: uppercase; letter-spacing: .03em; line-height: 1.15; text-wrap: balance; scroll-margin-top: 16px; }
.body h1 { font-size: 30px; margin: 34px 0 10px; }
.body h2 { font-size: 26px; margin: 34px 0 10px; padding-top: 14px; border-top: 1px solid var(--line); }
.body h3 { font-size: 20px; margin: 24px 0 8px; color: var(--ink); }
.body h4 { font-size: 16.5px; margin: 18px 0 6px; color: var(--ink-2); }
.body p, .body li { max-width: 70ch; }
.body code { font-family: var(--mono); font-size: .88em; background: var(--panel-2); padding: 1px 4px; overflow-wrap: anywhere; }
.body pre { background: var(--panel); border: 1px solid var(--line); padding: 12px 14px; overflow-x: auto; font-size: 13px; line-height: 1.45; }
.body pre code { background: none; padding: 0; overflow-wrap: normal; }
.body pre.mermaid { background: var(--panel); }
.body blockquote { margin: 14px 0; padding: 4px 16px; border-left: 3px solid var(--accent); color: var(--ink-2); background: var(--panel); }
.body hr { border: 0; border-top: 1px solid var(--line); margin: 26px 0; }
.tw { overflow-x: auto; margin: 14px 0; border: 1px solid var(--line); }
.body table { border-collapse: collapse; font-size: 14px; width: 100%; }
.body th, .body td { border-bottom: 1px solid var(--line); padding: 6px 10px; text-align: left; vertical-align: top; min-width: 7em; }
.body th { background: var(--panel); font-family: var(--mono); font-size: 11.5px; letter-spacing: .06em; text-transform: uppercase; color: var(--ink-2); position: sticky; top: 0; }
.pathref { border-bottom: 1px dashed var(--line-2); color: var(--ink-2); }
.df { display: flex; align-items: center; gap: 14px; margin-top: 40px; padding-top: 16px; border-top: 1px solid var(--line); flex-wrap: wrap; }
.mark { background: var(--accent); color: var(--bg); border: 0; padding: 8px 16px; font-family: var(--display); font-weight: 700; font-size: 16px; letter-spacing: .06em; text-transform: uppercase; cursor: pointer; }
.mark.done { background: var(--good-soft); color: var(--good); }
.df .nx a { font-family: var(--mono); font-size: 13px; }
.rail { border-left: 1px solid var(--line); overflow-y: auto; padding: 24px 14px 40px; font-size: 13px; }
.rail h4 { margin: 0 0 8px; font-family: var(--mono); font-size: 10.5px; letter-spacing: .14em; text-transform: uppercase; color: var(--ink-3); font-weight: 500; }
.rail a { display: block; text-decoration: none; color: var(--ink-2); padding: 3px 0; line-height: 1.3; }
.rail a.l3 { padding-left: 12px; font-size: 12.5px; color: var(--ink-3); }
.rail a:hover { color: var(--accent); }
.rail .keys { margin-top: 22px; font-family: var(--mono); font-size: 11px; color: var(--ink-3); line-height: 1.8; }
kbd { font-family: var(--mono); font-size: 10.5px; border: 1px solid var(--line-2); padding: 0 4px; color: var(--ink-2); }
.t { color: var(--link); text-decoration: none; border-bottom: 1px dotted color-mix(in srgb, var(--link) 55%, transparent); cursor: help; }
.t:hover, .t.on { border-bottom-style: solid; }
.tip { position: fixed; z-index: 50; width: 340px; max-width: calc(100vw - 24px); background: var(--panel); border: 1px solid var(--line-2); border-top: 3px solid var(--accent); box-shadow: var(--shadow); padding: 12px 14px 10px; font-size: 14.5px; line-height: 1.45; }
.tip .th { display: flex; align-items: baseline; gap: 10px; margin-bottom: 4px; }
.tip .th b { font-family: var(--display); font-weight: 700; font-size: 19px; text-transform: uppercase; }
.tip .th .k { font-family: var(--mono); font-size: 10px; letter-spacing: .12em; text-transform: uppercase; color: var(--ink-3); }
.tip p { margin: 0; }
.tip .w { margin-top: 8px; font-family: var(--mono); font-size: 11px; color: var(--ink-3); overflow-wrap: anywhere; }
.tip .lock { height: 2px; background: var(--line); margin-top: 10px; position: relative; }
.tip .lock b { position: absolute; left: 0; top: 0; bottom: 0; width: 0; background: var(--accent); }
.tip.locked { border-top-color: var(--ink); }
.tip.locked .lock b { width: 100%; }
.tip .hint { font-family: var(--mono); font-size: 10px; color: var(--ink-3); margin-top: 4px; }
.pins { margin-top: 18px; display: grid; gap: 8px; }
.pins .pin { border: 1px solid var(--line-2); background: var(--panel); padding: 8px 10px; position: relative; }
.pins .pin b { font-family: var(--display); text-transform: uppercase; font-size: 15px; display: block; padding-right: 18px; }
.pins .pin p { margin: 4px 0 0; color: var(--ink-2); font-size: 12.5px; }
.pins .pin button { position: absolute; top: 4px; right: 6px; background: none; border: 0; cursor: pointer; color: var(--ink-3); }
@media (max-width: 1100px) { .shell { grid-template-columns: 280px minmax(0, 1fr); } .rail { display: none; } }
@media (max-width: 760px) {
  #menu { display: inline-block; }
  .strip .bar { display: none; }
  .shell { grid-template-columns: minmax(0, 1fr); }
  .side { position: fixed; z-index: 20; top: calc(44px + env(safe-area-inset-top, 0px)); bottom: 0; left: 0; width: min(320px, 88vw); transform: translateX(-100%); transition: transform .2s; box-shadow: var(--shadow); }
  .side.show { transform: none; }
  main { padding-inline: 16px; }
  .dh h1 { font-size: 30px; }
  .three { grid-template-columns: minmax(0, 1fr); }
}
@media (prefers-reduced-motion: reduce) { .side { transition: none; } }
</style>

<div class="strip">
  <button type="button" id="menu" aria-controls="side">Docs</button>
  <h1><b>Command</b> Reference</h1>
  <span class="sp"></span>
  <span class="count"><b id="nRead">0</b> / <!--COUNT--> read</span>
  <span class="bar" aria-hidden="true"><i id="barFill"></i></span>
</div>
<div class="shell">
  <nav class="side" id="side" aria-label="All docs">
    <div class="search">
      <input id="q" type="search" placeholder="Search titles and text  ( / )" aria-label="Search the docs">
      <div class="filters">
        <button type="button" id="fUnread" aria-pressed="false">Unread only</button>
        <button type="button" id="fShelf" aria-pressed="false">Hide shelves</button>
        <button type="button" id="fOpen">Collapse all</button>
      </div>
    </div>
    <!--NAV-->
  </nav>
  <main id="main">
<!--ARTICLES-->
  </main>
  <aside class="rail" aria-label="On this page">
    <h4>On this page</h4>
    <div id="toc"></div>
    <div class="pins" id="pins"></div>
    <div class="keys"><kbd>/</kbd> search · <kbd>J</kbd> <kbd>K</kbd> next / prev<br><kbd>M</kbd> mark read · <kbd>Space</kbd> lock a card<br><kbd>Esc</kbd> close · click a term to pin it</div>
  </aside>
</div>

<script>
/*DATA*/
const $ = (s, el = document) => el.querySelector(s), $$ = (s, el = document) => [...el.querySelectorAll(s)];
const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const store = { get(k, d) { try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (_) { return d; } },
                set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (_) {} } };
let READ = new Set(store.get('ref.read', []));
let cur = null;

function paintRead() {
  $$('.ni').forEach(a => a.classList.toggle('read', READ.has(a.dataset.id)));
  const n = ORDER.filter(id => READ.has(id)).length;
  $('#nRead').textContent = n; $('#barFill').style.width = (100 * n / ORDER.length) + '%';
  if (cur) { const b = $('.mark', $('#' + CSS.escape(cur))); b.classList.toggle('done', READ.has(cur)); b.textContent = READ.has(cur) ? 'Read ✓ (undo)' : 'Mark read'; }
  if ($('#fUnread').getAttribute('aria-pressed') === 'true') filter();
}
function toggleRead(id) { READ.has(id) ? READ.delete(id) : READ.add(id); store.set('ref.read', [...READ]); paintRead(); }

function show(id, anchor) {
  if (!id || !document.getElementById(id) || !ORDER.includes(id)) id = ORDER[0];
  if (cur && cur !== id) $('#' + CSS.escape(cur)).hidden = true;
  const art = $('#' + CSS.escape(id)); art.hidden = false; cur = id;
  $$('.ni.cur').forEach(a => a.classList.remove('cur'));
  const ni = $(`.ni[data-id="${CSS.escape(id)}"]`);
  if (ni) { ni.classList.add('cur'); let g = ni.closest('details'); while (g) { g.open = true; g = g.parentElement.closest('details'); } ni.scrollIntoView({ block: 'nearest' }); }
  $('#toc').innerHTML = (TOC[id] || []).map(([l, t, h]) => `<a class="l${l}" href="#" data-h="${esc(h)}">${esc(t)}</a>`).join('') || '<span style="color:var(--ink-3)">No sections.</span>';
  const i = ORDER.indexOf(id), nx = ORDER[i + 1];
  $('.nx', art).innerHTML = nx ? `Next: <a href="#${nx}">${esc($('#' + CSS.escape(nx) + ' h1').textContent)}</a>` : 'Last page.';
  closeTips(1); paintRead(); store.set('ref.last', id);
  const m = $('#main');
  if (anchor) { const h = document.getElementById(anchor); if (h) { h.scrollIntoView(); return; } }
  m.scrollTop = 0;
  $('#side').classList.remove('show');
}
function route() { const h = decodeURIComponent(location.hash.slice(1)); show(h || store.get('ref.last', ORDER[0])); }
window.addEventListener('hashchange', route);
$('#toc').addEventListener('click', e => { const a = e.target.closest('a'); if (!a) return; e.preventDefault(); const h = document.getElementById(a.dataset.h); if (h) h.scrollIntoView({ behavior: 'smooth' }); });
document.addEventListener('click', e => { const b = e.target.closest('[data-mark]'); if (b) toggleRead(b.dataset.mark); });
$('#menu').addEventListener('click', () => $('#side').classList.toggle('show'));

/* search: titles first, then full text (built lazily) */
let TEXT = null;
function filter() {
  const q = $('#q').value.trim().toLowerCase(), unread = $('#fUnread').getAttribute('aria-pressed') === 'true';
  if (q && !TEXT) { TEXT = {}; $$('article.doc').forEach(a => TEXT[a.id] = a.textContent.toLowerCase()); }
  $$('.grp').forEach(g => {
    let any = 0;
    $$('.ni', g).forEach(a => { const ok = (!q || a.textContent.toLowerCase().includes(q) || TEXT[a.dataset.id].includes(q)) && (!unread || !READ.has(a.dataset.id)); a.hidden = !ok; any += ok; });
    const shelfHide = g.classList.contains('shelf') && $('#fShelf').getAttribute('aria-pressed') === 'true';
    g.hidden = !any || shelfHide; if (q && any) g.open = true;
  });
  $$('.sys:not(.grp)').forEach(s => { s.hidden = false; const vis = $$('.ni', s).some(a => !a.closest('[hidden]')); s.hidden = !vis; if (q && vis) s.open = true; });
}
$('#q').addEventListener('input', filter);
['fUnread', 'fShelf'].forEach(id => $('#' + id).addEventListener('click', e => { const b = e.currentTarget; b.setAttribute('aria-pressed', b.getAttribute('aria-pressed') === 'true' ? 'false' : 'true'); filter(); }));
$('#fOpen').addEventListener('click', () => $$('.grp, .sys').forEach(g => g.open = false));

/* hover cards: hover opens · 1.5 s or Space locks · nested to depth 3 · Esc closes · click pins */
let tips = [], openTimer = null, closeTimer = null;
function mdInline(s) { return esc(s).replace(/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g, (m, k, l) => { const g = G[k]; const label = l || (g ? g.t : k); return g ? `<a class="t" data-t="${esc(k)}" tabindex="0">${label}</a>` : label; }); }
function tipFor(target, depth) {
  const k = target.dataset.t, g = G[k]; if (!g) return null;
  const el = document.createElement('div'); el.className = 'tip'; el.dataset.depth = depth;
  const deep = depth >= 3, plain = s => esc(String(s || '').replace(/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g, (m, kk, l) => l || (G[kk] ? G[kk].t : kk)));
  el.innerHTML = `<div class="th"><b>${esc(g.t)}</b><span class="k">${esc(g.k)}</span></div><p>${deep ? plain(g.d) : mdInline(g.d)}</p><div class="w">${esc(g.w || '')}</div><div class="lock"><b></b></div><div class="hint">hold 1.5 s or Space to lock · Esc closes · click pins</div>`;
  document.body.appendChild(el);
  const r = target.getBoundingClientRect(), w = el.offsetWidth, h = el.offsetHeight;
  let x = Math.min(Math.max(12, r.left), innerWidth - w - 12), y = r.bottom + 8; if (y + h > innerHeight - 12) y = Math.max(12, r.top - h - 8);
  el.style.left = x + 'px'; el.style.top = y + 'px';
  const rec = { el, target, depth, locked: false, timer: null };
  const bar = $('.lock b', el); requestAnimationFrame(() => { bar.style.transition = 'width 1.5s linear'; bar.style.width = '100%'; });
  rec.timer = setTimeout(() => lock(rec), 1500);
  el.addEventListener('mouseenter', () => clearTimeout(closeTimer));
  el.addEventListener('mouseleave', () => scheduleClose(depth));
  target.classList.add('on'); tips.push(rec); return rec;
}
function lock(rec) { rec.locked = true; rec.el.classList.add('locked'); }
function closeTips(d) { tips.filter(t => t.depth >= d).forEach(t => { clearTimeout(t.timer); t.el.remove(); t.target.classList.remove('on'); }); tips = tips.filter(t => t.depth < d); }
function scheduleClose(depth) { clearTimeout(closeTimer); closeTimer = setTimeout(() => { const un = tips.filter(t => t.depth >= depth && !t.locked); if (un.length) closeTips(Math.min(...un.map(t => t.depth))); }, 220); }
function depthOf(t) { const p = t.closest('.tip'); return p ? +p.dataset.depth + 1 : 1; }
function onEnter(t) { clearTimeout(openTimer); clearTimeout(closeTimer); const d = depthOf(t); openTimer = setTimeout(() => { closeTips(d); tipFor(t, d); }, 120); }
document.addEventListener('mouseover', e => { const t = e.target.closest('.t'); if (t) onEnter(t); });
document.addEventListener('mouseout', e => { const t = e.target.closest('.t'); if (t) { clearTimeout(openTimer); scheduleClose(depthOf(t)); } });
document.addEventListener('focusin', e => { const t = e.target.closest('.t'); if (t) onEnter(t); });
document.addEventListener('focusout', e => { const t = e.target.closest('.t'); if (t) scheduleClose(depthOf(t)); });
document.addEventListener('click', e => {
  const t = e.target.closest('.t');
  if (t && t.dataset.t) { e.preventDefault(); pin(t.dataset.t); return; }
  if (!e.target.closest('.tip')) closeTips(1);
});
let PINS = [];
function pin(k) { if (!G[k] || PINS.includes(k)) return; PINS.unshift(k); PINS = PINS.slice(0, 6); paintPins(); closeTips(1); }
function paintPins() { $('#pins').innerHTML = PINS.map(k => `<div class="pin"><b>${esc(G[k].t)}</b><p>${mdInline(G[k].d)}</p><button type="button" data-unpin="${esc(k)}" aria-label="Unpin">×</button></div>`).join(''); }
$('#pins').addEventListener('click', e => { const b = e.target.closest('[data-unpin]'); if (b) { PINS = PINS.filter(k => k !== b.dataset.unpin); paintPins(); } });

document.addEventListener('keydown', e => {
  if (e.target.matches('input, textarea')) { if (e.key === 'Escape') e.target.blur(); return; }
  if (e.metaKey || e.ctrlKey || e.altKey) return;
  const k = e.key.toLowerCase(), i = ORDER.indexOf(cur);
  if (e.key === '/') { e.preventDefault(); $('#q').focus(); return; }
  if (k === 'j' && ORDER[i + 1]) { location.hash = ORDER[i + 1]; return; }
  if (k === 'k' && i > 0) { location.hash = ORDER[i - 1]; return; }
  if (k === 'm' && cur) { toggleRead(cur); return; }
  if (e.key === 'Escape') { if (tips.length) closeTips(1); else $('#side').classList.remove('show'); return; }
  if (e.key === ' ' && tips.length) { e.preventDefault(); lock(tips[tips.length - 1]); }
});
route();
</script>
"""

if __name__ == "__main__":
    main()
