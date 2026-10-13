"""erd.py v2 (cdb-03 right rail: tables list + relationships list; cdb-04 one metadata query) - build an ERD glass from a SQLite COPY (BOLO 140).

Usage: python -X utf8 _tools/mcp/erd.py stash [zotero ...]
Reads _PRIVATE/dbcopies/<db>.sqlite read-only (mode=ro, query_only). Row counts only,
never row contents. Writes _PRIVATE/reference/erd/<db>-erd.html. Stdlib only.
"""
import html
import os
import sqlite3
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
COPIES = os.path.join(ROOT, "_PRIVATE", "dbcopies")
OUT = os.path.join(ROOT, "_PRIVATE", "reference", "erd")
W, HEAD, ROW, GAPX, GAPY, PAD = 270, 46, 19, 70, 40, 30


def q(name):
    return '"' + name.replace('"', '""') + '"'


def read(db):
    path = os.path.join(COPIES, db + ".sqlite")
    c = sqlite3.connect("file:" + path.replace("\\", "/") + "?mode=ro", uri=True)
    c.execute("PRAGMA query_only=1")
    tabs, fks = {}, []
    META = ("SELECT 'c', m.name, p.cid, p.name, p.type, p.pk FROM sqlite_master m, pragma_table_info(m.name) p "
            "WHERE m.type='table' AND m.name NOT LIKE 'sqlite_%' "
            "UNION ALL SELECT 'f', m.name, f.id, f.\"from\", f.\"table\", f.\"to\" FROM sqlite_master m, "
            "pragma_foreign_key_list(m.name) f WHERE m.type='table' AND m.name NOT LIKE 'sqlite_%' ORDER BY 2, 1, 3")
    try:  # cdb-04: one metadata query for the whole database
        for kind, t, _i, a, b, c5 in c.execute(META):
            tabs.setdefault(t, {"rows": None, "cols": []})
            if kind == "c":
                tabs[t]["cols"].append((a, b or "", c5 > 0))
            else:
                fks.append((t, a, b, c5))
        tabs = {n: tabs[n] for n in sorted(tabs)}
    except sqlite3.Error:  # fallback: per-table pragmas (older SQLite or a virtual table that will not load)
        tabs, fks = {}, []
        for n in [r[0] for r in c.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")]:
            tabs[n] = {"rows": None, "cols": [(r[1], r[2] or "", r[5] > 0) for r in c.execute("PRAGMA table_info(%s)" % q(n))]}
            for r in c.execute("PRAGMA foreign_key_list(%s)" % q(n)):
                fks.append((n, r[3], r[2], r[4]))
    for n in tabs:
        try:
            tabs[n]["rows"] = c.execute("SELECT COUNT(*) FROM %s" % q(n)).fetchone()[0]
        except sqlite3.Error:
            pass  # virtual table whose module is missing
    c.close()
    return tabs, [f for f in fks if f[2] in tabs]


def curve(x1, y1, x2, y2, dx1, dx2):
    return "M%d %.1f C%.0f %.1f %.0f %.1f %d %.1f" % (x1, y1, x1 + dx1, y1, x2 + dx2, y2, x2, y2)


def build(db):
    tabs, fks = read(db)
    names = list(tabs)
    deg = {n: 0 for n in names}
    for a, _, b, _ in fks:
        deg[a] += 1
        deg[b] += 1
    names.sort(key=lambda n: (-deg[n], n))
    ncols = max(3, round(len(names) ** 0.5 * 1.1))
    pos, y = {}, PAD + 6
    for i in range(0, len(names), ncols):
        grp = names[i:i + ncols]
        hs = [HEAD + ROW * len(tabs[n]["cols"]) + 8 for n in grp]
        for j, n in enumerate(grp):
            pos[n] = (PAD + j * (W + GAPX), y, hs[j])
        y += max(hs) + GAPY
    width = PAD * 2 + min(ncols, len(names)) * (W + GAPX) - GAPX
    height = y

    cards = []
    for n in names:
        x, yy, _ = pos[n]
        fkc = {ac for a, ac, _, _ in fks if a == n}
        rows = []
        for cn, ct, pk in tabs[n]["cols"]:
            tag = '<b class="pk">PK</b>' if pk else ('<b class="fkt">FK</b>' if cn in fkc else "<b></b>")
            rows.append('<div class="c">%s<span>%s</span><i>%s</i></div>'
                        % (tag, html.escape(cn), html.escape(ct.lower())))
        rc = "?" if tabs[n]["rows"] is None else "{:,}".format(tabs[n]["rows"])
        cards.append('<div class="card" data-n="%s" style="left:%dpx;top:%dpx;width:%dpx"><h3><span>%s</span><em>%s rows</em></h3>%s</div>'
                     % (html.escape(n.lower()), x, yy, W, html.escape(n), rc, "".join(rows)))

    lines = []
    for a, ac, b, bc in fks:
        ax, ay, _ = pos[a]
        bx, by, _ = pos[b]
        ci = next((i for i, c in enumerate(tabs[a]["cols"]) if c[0] == ac), 0)
        if not bc:
            pk = [c[0] for c in tabs[b]["cols"] if c[2]]
            bc = pk[0] if pk else tabs[b]["cols"][0][0]
        cj = next((i for i, c in enumerate(tabs[b]["cols"]) if c[0] == bc), 0)
        y1 = ay + HEAD + ROW * ci + ROW / 2
        y2 = by + HEAD + ROW * cj + ROW / 2
        if bx == ax:
            d = curve(ax + W, y1, bx + W, y2, 50, 50)
        elif bx > ax:
            m = max(30, (bx - ax - W) / 2)
            d = curve(ax + W, y1, bx, y2, m, -m)
        else:
            m = max(30, (ax - bx - W) / 2)
            d = curve(ax, y1, bx + W, y2, -m, m)
        tip = "%s.%s → %s.%s" % (a, ac, b, bc)
        lines.append('<g class="fk" data-a="%s" data-b="%s"><path class="hit" d="%s" data-t="%s"/><path class="ln" d="%s"/></g>'
                     % (html.escape(a.lower()), html.escape(b.lower()), d, html.escape(tip), d))

    tl = "".join('<li data-n="%s"><span>%s</span><em>%s</em></li>' % (html.escape(n.lower()), html.escape(n),
                 "?" if tabs[n]["rows"] is None else "{:,}".format(tabs[n]["rows"])) for n in sorted(tabs))
    rl = "".join('<li data-a="%s" data-b="%s"><span>%s.%s</span> &rarr; <span>%s.%s</span></li>'
                 % (html.escape(a.lower()), html.escape(b.lower()), html.escape(a), html.escape(ac), html.escape(b), html.escape(bc or "pk"))
                 for a, ac, b, bc in fks) or "<li><em>no foreign keys declared</em></li>"
    title = db.capitalize() + " ERD"
    page = (PAGE.replace("{{TITLE}}", title).replace("{{W}}", str(width)).replace("{{H}}", str(height))
            .replace("{{CARDS}}", "".join(cards)).replace("{{LINES}}", "".join(lines))
            .replace("{{TL}}", tl).replace("{{RL}}", rl).replace("{{NT}}", str(len(tabs))).replace("{{NF}}", str(len(fks))))
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, db + "-erd.html")
    with open(p, "w", encoding="utf-8") as f:
        f.write(page)
    return p, len(tabs), len(fks), len(page.encode("utf-8"))


PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{{TITLE}}</title>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Atkinson+Hyperlegible:wght@400;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{--bg:#121110;--pan:#1B1A18;--ac:#FF5A1F;--tx:#E9E6E1;--mu:#8C877F;--ln:#2C2A27}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--tx);font:14px 'Atkinson Hyperlegible',sans-serif}
header{position:sticky;top:0;z-index:5;height:44px;display:flex;align-items:center;gap:16px;padding:0 16px;background:var(--pan);border-bottom:1px solid var(--ln)}
header h1{margin:0;font:700 20px 'Barlow Condensed',sans-serif;letter-spacing:.04em;color:var(--ac);text-transform:uppercase}
header span{font:12px 'IBM Plex Mono',monospace;color:var(--mu)}
input{margin-left:auto;width:min(260px,40vw);background:var(--bg);color:var(--tx);border:1px solid var(--ln);border-radius:4px;padding:5px 8px;font:13px 'IBM Plex Mono',monospace}
input:focus{outline:2px solid var(--ac)}
main{display:flex;height:calc(100vh - 44px)}#wrap{flex:1;overflow:auto}
aside{width:300px;flex:none;overflow:auto;background:var(--pan);border-left:1px solid var(--ln);padding:8px 0}
aside h2{margin:8px 12px 4px;font:700 14px 'Barlow Condensed',sans-serif;letter-spacing:.08em;color:var(--ac);text-transform:uppercase}
aside ul{list-style:none;margin:0 0 8px;padding:0}aside li{display:flex;justify-content:space-between;gap:8px;padding:3px 12px;font:12px 'IBM Plex Mono',monospace;cursor:pointer}
aside li:hover{background:var(--ln)}aside li em{color:var(--mu);font-style:normal}.sel{outline:2px solid var(--ac)}
@media(max-width:700px){main{flex-direction:column;height:auto}aside{width:auto;max-height:40vh}#wrap{height:60vh}}
#cv{position:relative;width:{{W}}px;height:{{H}}px}
svg{position:absolute;left:0;top:0}
.card{position:absolute;background:var(--pan);border:1px solid var(--ln);border-radius:6px;overflow:hidden;transition:opacity .15s}
.card h3{margin:0;height:46px;padding:6px 10px;border-bottom:2px solid var(--ac);display:flex;flex-direction:column;justify-content:center}
.card h3 span{font:700 16px 'Barlow Condensed',sans-serif;letter-spacing:.03em;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.card h3 em{font:11px 'IBM Plex Mono',monospace;color:var(--mu);font-style:normal}
.c{height:19px;display:flex;align-items:center;gap:6px;padding:0 10px;font:12px 'IBM Plex Mono',monospace}
.c span{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.c i{color:var(--mu);font-style:normal;font-size:11px}
.c b{width:20px;font-size:10px}.pk{background:var(--ac);color:var(--bg);text-align:center;border-radius:2px}.fkt{color:var(--ac)}
.dim{opacity:.12}
.ln{fill:none;stroke:#7a4a35;stroke-width:1.3;pointer-events:none}.hit{fill:none;stroke:transparent;stroke-width:12;cursor:help;pointer-events:stroke}
g.fk:hover .ln{stroke:var(--ac);stroke-width:2.4}
#tip{position:fixed;display:none;z-index:9;background:var(--pan);border:1px solid var(--ac);padding:4px 8px;border-radius:4px;font:12px 'IBM Plex Mono',monospace;pointer-events:none}
</style></head><body>
<header><h1>{{TITLE}}</h1><span>{{NT}} tables &middot; {{NF}} foreign keys</span><input id="q" type="search" placeholder="search tables" aria-label="Search tables"></header>
<main><div id="wrap"><div id="cv"><svg width="{{W}}" height="{{H}}">{{LINES}}</svg>{{CARDS}}</div></div>
<aside><h2>Tables</h2><ul id="tl">{{TL}}</ul><h2>Relationships</h2><ul id="rl">{{RL}}</ul></aside></main>
<div id="tip"></div>
<script>
var q=document.getElementById('q'),cs=[].slice.call(document.querySelectorAll('.card')),gs=[].slice.call(document.querySelectorAll('g.fk'));
q.addEventListener('input',function(){var v=q.value.trim().toLowerCase(),on={};
cs.forEach(function(c){var m=!v||c.dataset.n.indexOf(v)>-1;on[c.dataset.n]=m;c.classList.toggle('dim',!m)});
gs.forEach(function(g){g.style.opacity=(!v||on[g.dataset.a]||on[g.dataset.b])?1:.08})});
var wrap=document.getElementById('wrap');
function pick(n){cs.forEach(function(c){c.classList.remove('sel');if(c.dataset.n===n){c.classList.add('sel');wrap.scrollTo({left:c.offsetLeft-20,top:c.offsetTop-20,behavior:'smooth'})}})}
document.querySelectorAll('#tl li').forEach(function(li){li.addEventListener('click',function(){pick(li.dataset.n)})});
document.querySelectorAll('#rl li').forEach(function(li){li.addEventListener('click',function(){pick(li.dataset.a)})});
var t=document.getElementById('tip');
document.querySelectorAll('.hit').forEach(function(h){h.addEventListener('mousemove',function(e){t.textContent=h.dataset.t;t.style.display='block';t.style.left=(e.clientX+12)+'px';t.style.top=(e.clientY+12)+'px'});h.addEventListener('mouseleave',function(){t.style.display='none'})});
</script></body></html>"""

if __name__ == "__main__":
    for d in sys.argv[1:] or ["stash", "zotero"]:
        p, nt, nf, sz = build(d)
        print("%s: %d tables, %d FKs, %d bytes -> %s" % (d, nt, nf, sz, p))
