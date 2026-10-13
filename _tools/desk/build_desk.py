# -*- coding: utf-8 -*-
"""The Command Desk builder (BOLO 141). Live sources -> _PRIVATE/reference/desk/command-desk.html.

v2, 10/13 (Chief: "the command deck UI dashboard ... hackerpunk console vibe ... the same font, the same
look as Caves of Qud, an old-school Dwarf Fortress"): the page is a terminal roguelike. Double-line box
frames, a tile font (VT323) for the big glyphs, IBM Plex Mono for the data, ASCII meters for the waves,
a glyph map of the stations, the last replies as a game message log. The orange trunk stays. DARK only.

Sources: _tools/launch/last_poll.json (stations) · pull_queue.py report (waves) · _tools/launch/next.json +
STATE.md Blocked + pages.json (calls) · TRAFFIC.md or judy.session.log (replies) · pages.json (boards).
Usage: python _tools/desk/build_desk.py          (the Console serves it at /local/desk)
"""
import io, os, re, sys, json, html, datetime as dt, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "_PRIVATE", "reference", "desk", "command-desk.html")
TE = os.path.join(ROOT, "_PRIVATE", "taxonomy_engine")
NEXT = os.path.join(ROOT, "_tools", "launch", "next.json")
PAGES = os.path.join(ROOT, "_tools", "pages", "pages.json")
STATE = os.path.join(ROOT, "STATE.md")
TRAFFIC = os.path.join(ROOT, "TRAFFIC.md")
JLOG = os.path.join(ROOT, "_tools", "dictation", "judy.session.log")
LAUNCH_POLL = os.path.join(ROOT, "_tools", "launch", "last_poll.json")  # launch.py writes it after the poll

E = html.escape
EMPTY = '<div class="empty">%s</div>'
METER = 24  # cells in an ASCII meter


def t12(d):
    return d.strftime("%I:%M %p").lstrip("0")


def stamp12(s):
    try:
        d = dt.datetime.fromisoformat(s)
        return "%d/%d %s" % (d.month, d.day, t12(d))
    except Exception:
        return s or "?"


def clean(s, n=150):
    s = re.sub(r"\s+", " ", (s or "")).strip()
    s = re.sub(r"[*_`]+", "", s)
    return s if len(s) <= n else s[:n - 1].rstrip() + "…"


def rd(p):
    try:
        return io.open(p, encoding="utf-8", errors="replace").read()
    except Exception:
        return ""


def meter(done, tot, cells=METER):
    f = int(round(cells * done / max(tot, 1)))
    return '<span class="meter" aria-hidden="true">[<i>%s</i>%s]</span>' % ("█" * f, "░" * (cells - f))


# ---------- sections ----------

def stations():
    try:
        d = json.load(io.open(LAUNCH_POLL, encoding="utf-8"))
        rows = d.get("stations", [])
        if rows:
            when = dt.datetime.fromisoformat(d.get("time", ""))
            stale = (dt.datetime.now() - when).total_seconds() > 6 * 3600
            ngo = sum(1 for r in rows if r.get("go"))
            cells = "".join('<a class="cell%s" href="#st-%s" title="%s · %s">%s</a>'
                            % ("" if r.get("go") else " no", E(r.get("name", "?")).lower(), E(r.get("name", "?")),
                               "GO" if r.get("go") else "NO-GO", E((r.get("name") or "?")[0])) for r in rows)
            lines = "".join('<li id="st-%s" class="st%s"><span class="g">%s</span><b>%s</b><span class="s">%s</span><small>%s</small></li>'
                            % (E(r.get("name", "?")).lower(), "" if r.get("go") else " no", "■" if r.get("go") else "×",
                               E(r.get("name", "?")), "GO" if r.get("go") else "NO-GO", E(clean(r.get("detail", ""), 110))) for r in rows)
            head = ('<div class="poll"><span class="map">%s</span><span class="sum">%d/%d GO · polled %d/%d %s%s</span></div>'
                    % (cells, ngo, len(rows), when.month, when.day, t12(when), ' <span class="chip">stale</span>' if stale else ""))
            return head + '<ul class="stl">%s</ul>' % lines, 1
    except Exception:
        pass
    try:
        m = dt.datetime.fromtimestamp(os.path.getmtime(JLOG))
        return EMPTY % ("No station poll on file. JUDY's log last moved %d/%d %s. The next launch writes the poll." % (m.month, m.day, t12(m))), 0
    except Exception:
        return EMPTY % "No station poll recorded yet.", 0


def waves():
    try:
        p = subprocess.run([sys.executable, "-X", "utf8", "pull_queue.py", "report"], cwd=TE, capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=60, stdin=subprocess.DEVNULL)
        out = p.stdout
    except Exception:
        out = ""
    rows, q, n = [], "", 0
    for ln in out.splitlines():
        m = re.match(r"wave (\w+):\s*(\d+)/(\d+) boards(.*)", ln)
        if m:
            n += 1
            done, tot = int(m.group(2)), int(m.group(3))
            rest = [x.strip() for x in m.group(4).split("·") if x.strip()]
            landed = any("LANDED" in x for x in rest)
            on = next((x for x in rest if x.startswith("on ")), "")
            eta = next((x for x in rest if x.startswith("ETA")), "")
            img = next((x for x in rest if "image" in x), "")
            tail = "LANDED" if landed else " · ".join(x for x in (on, eta) if x)
            rows.append('<li class="wv%s"><span class="k">wave %s</span>%s<span class="n">%d/%d</span><span class="d">%s</span><span class="t">%s</span></li>'
                        % (" landed" if landed else "", E(m.group(1)), meter(done, tot), done, tot, E(img), E(tail)))
        elif ln.startswith("queue:"):
            q = ln[6:].strip()
        elif ln.startswith("disk:"):
            q += " · " + ln[5:].strip()
    body = ('<ul class="wvl">%s</ul>' % "".join(rows)) if rows else EMPTY % "No pull waves running."
    if q:
        body += '<div class="qline">%s</div>' % E(q)
    return body, n


def calls():
    cards = []
    try:
        nx = json.load(io.open(NEXT, encoding="utf-8"))
    except Exception:
        nx = {}
    lev = nx.get("leverage")
    if isinstance(lev, dict):          # since 10/13 next.json carries {line, why, board}
        lev = lev.get("line", "")
    if lev:
        cards.append(("Next pick", clean(lev), "staged " + stamp12(nx.get("staged", ""))))
    for it in nx.get("open_at_close", []):
        cards.append(("Open at close", clean(it), "from the last Oscar Mike"))
    try:
        pg = json.load(io.open(PAGES, encoding="utf-8"))
    except Exception:
        pg = {}
    on = False
    for ln in rd(STATE).splitlines():
        if ln.startswith("## ") and "Blocked" in ln:
            on = True
            continue
        if on and ln.startswith("## "):
            break
        if on and ln.startswith("|") and not re.match(r"^\|\s*(#|-)", ln):
            c = [x.strip() for x in ln.strip("|").split("|")]
            if len(c) >= 2 and c[0]:
                cards.insert(0, ("Blocked #" + clean(c[0], 10), clean(c[1]), "unblocks: " + clean(c[2] if len(c) > 2 else "", 60)))

    def crumb(a, b):
        m = re.search(r"#(\d+)", a) or re.search(r"BOLO\s*(\d+)", b, re.I)
        if not m:
            return ""
        num = m.group(1)
        sheet = pg.get(num)
        url = sheet or pg.get("sitrep")
        if not url:
            return ""
        return '<a class="crumb" href="%s" target="_blank" rel="noopener">» BOLO %s › %s</a>' % (E(url), num, "DOPE SHEET" if sheet else "sit rep")
    h = "".join('<div class="card"><b>%s</b><p>%s</p><small>%s</small>%s</div>' % (E(a), E(b), E(c), crumb(a, b)) for a, b, c in cards)
    return ('<div class="cards">%s</div>' % h if h else EMPTY % "No open calls. Nothing waits on you."), len(cards)


def says():
    items = []
    for part in rd(TRAFFIC).split("<!-- block -->")[1:]:
        first, _, body = part.strip().partition("\n")
        items.append((first.strip("# ").strip(), re.sub(r"\s+", " ", clean(body, 140))))
    items = items[:5]
    if not items:  # fallback: JUDY's spoken lines from her session log
        ls = [m.group(1) for m in (re.match(r"\s*judy > (.*?)\s+\[say-line", l) for l in rd(JLOG).splitlines()) if m]
        items = [("", clean(x, 140)) for x in ls[-5:][::-1]]
    if not items:
        return EMPTY % "No replies recorded yet.", 0
    # a game log: oldest at the top and dim, the newest last with a cursor
    rows = list(reversed(items))
    lines = "".join('<li class="l%d">&gt; %s%s</li>' % (len(rows) - i, E(a + " · ") if a else "", E(b)) for i, (a, b) in enumerate(rows))
    return '<ol class="log">%s<li class="cur" aria-hidden="true">&gt; <span class="blink">_</span></li></ol>' % lines, len(items)


TILES = [("sitrep", "Sit rep", "the board"), ("soi", "SOI", "standing info"), ("pullglass", "Pull queue", "the glass"),
         ("roster", "Roster", "agents on call"), ("event-scorer", "Event scorer", "langextract step 2"),
         ("intake-2026-10-12", "Intake", "10/12 picks"), ("intake-report-2026-10-12", "Intake report", "10/12"),
         ("command-desk-mock", "Desk mock", "the first draft")]


def boards():
    try:
        pg = json.load(io.open(PAGES, encoding="utf-8"))
    except Exception:
        pg = {}
    t = ['<li><a href="%s" target="_blank" rel="noopener"><span class="k">%s</span><b>%s</b><small>%s</small></a></li>'
         % (E(pg[k]), "abcdefghijklmnop"[i], E(a), E(b)) for i, (k, a, b) in enumerate(x for x in TILES if pg.get(x[0]))]
    return (('<ol class="brd">%s</ol>' % "".join(t)) if t else EMPTY % "No boards in pages.json."), len(t)


# ---------- the page ----------

CSS = """
/* the Command Desk, DARK only (ruled 9/11). A terminal roguelike (Chief 10/13: Caves of Qud, old-school Dwarf
   Fortress): phosphor cream on near-black, double-line frames, one tile font for glyphs, one mono for data. */
:root{color-scheme:dark;
  --bg:#0A0C10;--pan:#0F1218;--pan2:#161A22;--line:#3B4150;--line2:#5A6274;--tx:#D9DBC9;--mut:#8A9080;--dim:#5C6258;
  --or:#FF5A1F;--or2:#FFB08F;--go:#5FBF8A;--no:#E9788A;--cyan:#5CC8D0;
  --tile:"VT323","Courier New",monospace;--mono:"IBM Plex Mono",Consolas,monospace}
*{box-sizing:border-box}
html,body{background:var(--bg);color:var(--tx)}
body{margin:0;font:14px/1.5 var(--mono);padding-inline:16px;padding-block:0 48px}
a{color:var(--cyan)} a:hover,a:focus-visible{color:var(--or2);outline:none}
:focus-visible{outline:1px solid var(--or);outline-offset:2px}
header{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;min-height:44px;display:flex;align-items:center;gap:14px;margin-inline:-16px;padding:4px 16px;background:var(--pan);border-bottom:1px solid var(--line)}
header h1{margin:0;font:400 30px/1 var(--tile);color:var(--or);letter-spacing:.04em;text-transform:uppercase}
header h1 i{font-style:normal;color:var(--tx)}
header .built{color:var(--mut);font-size:12px}
header .sp{flex:1}
button{font:inherit;font-size:12px;background:var(--pan2);color:var(--tx);border:1px solid var(--line);padding:3px 9px;cursor:pointer}
button:hover,button:focus-visible{border-color:var(--or);color:var(--or2)}
#meta{display:none;margin-inline:-16px;padding:6px 16px;background:var(--pan);border-bottom:1px solid var(--line);color:var(--mut);font-size:12px}
#meta.on{display:block}
.wrap{display:grid;grid-template-columns:60px minmax(0,1fr);gap:0 14px;padding-top:14px}
nav{display:flex;flex-direction:column;gap:4px;position:sticky;top:calc(env(safe-area-inset-top,0px) + 58px);align-self:start}
nav a{display:block;padding:6px 0 4px;text-align:center;text-decoration:none;color:var(--mut);border:1px solid var(--line);font:400 20px/1 var(--tile);letter-spacing:.04em}
nav a small{display:block;font:11px var(--mono);color:var(--or)}
nav a:hover,nav a:focus-visible{border-color:var(--or);color:var(--tx)}
main{display:grid;gap:22px;min-width:0}
section{position:relative;border:3px double var(--line);padding:18px 14px 12px;min-width:0;background:var(--pan)}
section.hit{border-color:var(--or)}
section h2{position:absolute;top:-15px;left:12px;margin:0;padding:0 8px;background:var(--pan);font:400 24px/1 var(--tile);letter-spacing:.06em;text-transform:uppercase;color:var(--or)}
section h2 small{font:11px var(--mono);color:var(--mut);letter-spacing:.08em;margin-left:8px;vertical-align:middle}
.empty{border:1px dashed var(--line);padding:10px 12px;color:var(--mut)}
/* stations: the glyph map, then the list */
.poll{display:flex;flex-wrap:wrap;align-items:center;gap:10px 16px;margin-bottom:10px}
.map{display:inline-flex;gap:2px;border:1px solid var(--line);padding:3px}
.cell{display:inline-block;width:22px;height:22px;line-height:22px;text-align:center;text-decoration:none;font:400 20px/22px var(--tile);background:#163322;color:var(--go)}
.cell.no{background:#3A1B20;color:var(--no)}
.cell:hover,.cell:focus-visible{outline:1px solid var(--or2)}
.sum{color:var(--mut);font-size:12px}
.chip{border:1px solid var(--or);color:var(--or);padding:0 6px;font-size:11px}
.stl{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:2px 18px}
.stl li{display:grid;grid-template-columns:18px 92px 52px minmax(0,1fr);gap:6px;align-items:baseline;padding:2px 0;border-top:1px dotted var(--line)}
.stl .g{font:400 18px/1 var(--tile);color:var(--go)} .stl li.no .g{color:var(--no)}
.stl b{font-weight:500;color:var(--tx)} .stl .s{font-size:11px;letter-spacing:.08em;color:var(--go)} .stl li.no .s{color:var(--no)}
.stl small{color:var(--dim);font-size:11px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.stl li.boot .g{color:var(--dim)}
/* waves: ascii meters */
.wvl{list-style:none;margin:0;padding:0;display:grid;gap:4px}
.wvl li{display:grid;grid-template-columns:64px auto 56px minmax(0,1fr);gap:0 10px;align-items:baseline;font-variant-numeric:tabular-nums}
.wvl .k{color:var(--or2)} .wvl .n{text-align:right} .wvl .d{color:var(--mut)} .wvl .t{grid-column:2/-1;color:var(--mut);font-size:12px}
.wvl li.landed .t{color:var(--go)}
.meter{letter-spacing:-1px;color:var(--line2)} .meter i{font-style:normal;color:var(--or)}
.qline{margin-top:10px;padding-top:8px;border-top:1px dotted var(--line);color:var(--mut);font-size:12px}
/* calls: announcement cards */
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:10px}
.card{border:1px solid var(--line);padding:8px 10px;background:var(--pan2);min-width:0}
.card b{display:block;font:400 20px/1.1 var(--tile);color:var(--or);letter-spacing:.03em}
.card p{margin:4px 0 6px;overflow-wrap:anywhere} .card small{color:var(--dim);font-size:11px}
.crumb{display:block;margin-top:4px;font-size:12px;text-decoration:none}
/* the message log */
.log{list-style:none;margin:0;padding:0}
.log li{padding:1px 0;overflow-wrap:anywhere}
.log .l5{color:var(--dim)} .log .l4{color:var(--dim)} .log .l3{color:var(--mut)} .log .l2{color:var(--mut)} .log .l1{color:var(--tx)}
.log .cur{color:var(--or)}
.blink{animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
/* boards */
.brd{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:4px 16px}
.brd a{display:grid;grid-template-columns:22px minmax(0,1fr);gap:0 8px;align-items:baseline;padding:4px 0;text-decoration:none;border-top:1px dotted var(--line);color:var(--tx)}
.brd .k{color:var(--or);font:400 18px/1 var(--tile)} .brd b{font-weight:500} .brd small{grid-column:2;color:var(--dim);font-size:11px}
.brd a:hover b,.brd a:focus-visible b{color:var(--or2)}
@media(max-width:560px){.wrap{grid-template-columns:44px minmax(0,1fr)} nav a{font-size:16px} .stl li{grid-template-columns:18px 80px 50px minmax(0,1fr)} .wvl li{grid-template-columns:56px auto 50px minmax(0,1fr)}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""

JS = """
var mb=document.getElementById("mb");
mb.onclick=function(){var m=document.getElementById("meta").classList.toggle("on");mb.setAttribute("aria-expanded",m)};
var KEYS={"1":"stations","2":"waves","3":"calls","4":"says","5":"boards"};
document.addEventListener("keydown",function(e){
 if(e.ctrlKey||e.metaKey||e.altKey||/INPUT|TEXTAREA|SELECT/.test((e.target.tagName||"")))return;
 var b=document.querySelector('.brd a[data-key="'+e.key+'"]');
 if(b){b.focus();return;}
 if(!KEYS[e.key])return;
 var s=document.getElementById(KEYS[e.key]);if(!s)return;
 var o=document.querySelector("section.hit");if(o)o.classList.remove("hit");
 s.classList.add("hit");s.scrollIntoView({behavior:matchMedia("(prefers-reduced-motion:reduce)").matches?"auto":"smooth",block:"start"});
});
[].slice.call(document.querySelectorAll(".brd a")).forEach(function(a){a.setAttribute("data-key",a.querySelector(".k").textContent);});
(function(){
 var done=false;try{done=sessionStorage.getItem("deskBoot")}catch(x){}
 if(done||matchMedia("(prefers-reduced-motion:reduce)").matches)return;
 try{sessionStorage.setItem("deskBoot","1")}catch(x){}
 var t=[].slice.call(document.querySelectorAll(".stl li"));if(!t.length)return;
 var step=Math.min(140,1400/t.length);
 t.forEach(function(el,i){var g=el.querySelector(".g"),w=g.textContent;el.classList.add("boot");g.textContent="·";
  setTimeout(function(){el.classList.remove("boot");g.textContent=w},(i+1)*step)});
})();
"""


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    stn, ns = stations()
    wv, nw = waves()
    cl, nc = calls()
    sy, nsy = says()
    bd, nb = boards()
    now = dt.datetime.now()
    meta = ("Built %d/%d %s from live sources: the launch poll, the pull report, next.json and STATE's Blocked table, "
            "TRAFFIC.md or JUDY's log, pages.json. An empty frame means its source had nothing. Keys 1-5 jump frames; "
            "a letter opens that board." % (now.month, now.day, t12(now)))
    page = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Command Desk</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=VT323&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>%s</style>
</head>
<body>
<header>
<h1>Command <i>Desk</i></h1>
<span class="built">built %s</span>
<span class="sp"></span>
<button id="mb" aria-expanded="false" aria-controls="meta">Info</button>
</header>
<div id="meta">%s</div>
<div class="wrap">
<nav aria-label="Frames">
<a href="#stations" title="Key 1">STN<small>1</small></a><a href="#waves" title="Key 2">WAVE<small>2</small></a><a href="#calls" title="Key 3">CALL<small>3</small></a><a href="#says" title="Key 4">LOG<small>4</small></a><a href="#boards" title="Key 5">BRD<small>5</small></a>
</nav>
<main>
<section id="stations"><h2>Stations<small>the launch poll</small></h2>%s</section>
<section id="waves"><h2>Pull waves<small>BOLO 137</small></h2>%s</section>
<section id="calls"><h2>Open calls<small>waiting on you</small></h2>%s</section>
<section id="says"><h2>Message log<small>JUDY's last five</small></h2>%s</section>
<section id="boards"><h2>Boards<small>press a letter</small></h2>%s</section>
</main>
</div>
<script>%s</script>
</body>
</html>
""" % (CSS, t12(now), E(meta), stn, wv, cl, sy, bd, JS)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    io.open(OUT, "w", encoding="utf-8", newline="\n").write(page)
    print("desk built: %d bytes -> %s" % (len(page.encode("utf-8")), OUT))
    print("stations %s | waves %s | calls %s | replies %s | boards %s" % (
        "filled" if ns else "empty", nw or "empty", nc or "empty", nsy or "empty", nb or "empty"))


if __name__ == "__main__":
    main()
