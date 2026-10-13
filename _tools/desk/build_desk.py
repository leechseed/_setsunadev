# -*- coding: utf-8 -*-
"""Command Desk builder (BOLO 141). Writes _PRIVATE/reference/desk/command-desk.html from live sources.
Every source is optional; an empty one shows the dashed empty state. Stdlib only.
Usage: python -X utf8 _tools/desk/build_desk.py"""
import io, os, re, sys, json, html, datetime as dt, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MOCK = os.path.join(ROOT, "_PRIVATE", "intake-repos", "ruvnet__ruflo", "front-page-mock.html")
OUT = os.path.join(ROOT, "_PRIVATE", "reference", "desk", "command-desk.html")
TE = os.path.join(ROOT, "_PRIVATE", "taxonomy_engine")
NEXT = os.path.join(ROOT, "_tools", "launch", "next.json")
PAGES = os.path.join(ROOT, "_tools", "pages", "pages.json")
STATE = os.path.join(ROOT, "STATE.md")
TRAFFIC = os.path.join(ROOT, "TRAFFIC.md")
JLOG = os.path.join(ROOT, "_tools", "dictation", "judy.session.log")
LAUNCH_POLL = os.path.join(ROOT, "_tools", "launch", "last_poll.json")  # optional; launch.py writes it after the poll

E = html.escape
EMPTY = '<div class="empty">%s</div>'


def t12(d):
    return d.strftime("%I:%M %p").lstrip("0")


def stamp12(s):
    try:
        d = dt.datetime.strptime(s, "%Y-%m-%d %H:%M")
        return "%d/%d %s" % (d.month, d.day, t12(d))
    except Exception:
        return s


def clean(s, n=150):
    s = re.sub(r"[*`]", "", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s).strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + "…"


def rd(p):
    try:
        return io.open(p, encoding="utf-8", errors="replace").read()
    except Exception:
        return ""


def stations():
    try:
        d = json.load(io.open(LAUNCH_POLL, encoding="utf-8"))
        rows = d.get("stations", [])
        if rows:
            when = dt.datetime.fromisoformat(d.get("time", ""))
            stale = (dt.datetime.now() - when).total_seconds() > 6 * 3600
            tiles = "".join('<div class="tile st" data-go="%d" title="%s"><span class="dot%s"></span><div><b>%s</b><small>%s</small></div></div>'
                            % (1 if r.get("go") else 0, E(r.get("detail", "")), "" if r.get("go") else " no", E(r.get("name", "?")),
                               "GO" if r.get("go") else "NO-GO") for r in rows)
            chip = '<span class="chip">stale</span>' if stale else ""
            head = '<div class="mono poll">Polled %d/%d %s%s</div>' % (when.month, when.day, t12(when), chip)
            return head + '<div class="grid">%s</div>' % tiles, 1
    except Exception:
        pass
    try:
        m = dt.datetime.fromtimestamp(os.path.getmtime(JLOG))
        return EMPTY % ("Last launch: see the JUDY session log (log updated %d/%d %s). No poll file yet; the next launch writes one."
                        % (m.month, m.day, t12(m))), 0
    except Exception:
        return EMPTY % "No station poll recorded yet.", 0


def waves():
    try:
        p = subprocess.run([sys.executable, "-X", "utf8", "pull_queue.py", "report"], cwd=TE, capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=60, stdin=subprocess.DEVNULL)
        out = p.stdout
    except Exception:
        out = ""
    cards, q, n = [], "", 0
    for ln in out.splitlines():
        m = re.match(r"wave (\w+):\s*(\d+)/(\d+) boards(.*)", ln)
        if m:
            n += 1
            done, tot = int(m.group(2)), int(m.group(3))
            rest = [x.strip() for x in m.group(4).split("·") if x.strip()]
            pct = 100 * done // max(tot, 1)
            cards.append('<div class="wave"><div class="row"><span>Wave %s</span><span class="mono">%d/%d boards · %d%%</span></div>'
                         '<div class="bar"><div class="fill" style="width:%d%%"></div></div>'
                         '<small class="mono">%s</small></div>' % (E(m.group(1)), done, tot, pct, pct, E(" · ".join(rest))))
        elif ln.startswith("queue:"):
            q = ln[6:].strip()
    if q:
        cards.append('<div class="mono" style="color:var(--mut)">queue: %s</div>' % E(q))
    return ("".join(cards) if cards else EMPTY % "No pull waves running."), n


def calls():
    cards = []
    try:
        nx = json.load(io.open(NEXT, encoding="utf-8"))
    except Exception:
        nx = {}
    if nx.get("leverage"):
        cards.append(("Next pick", clean(nx["leverage"]), "staged " + stamp12(nx.get("staged", ""))))
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
        n = m.group(1)
        sheet = pg.get(n)
        url = sheet or pg.get("sitrep")
        if not url:
            return ""
        return '<a class="crumb mono" href="%s" target="_blank" rel="noopener">Desk › BOLO %s › %s</a>' % (
            E(url), n, "DOPE SHEET" if sheet else "sit rep")
    h = "".join('<div class="card"><b>%s</b><div>%s</div><small class="mono">%s</small>%s</div>' % (E(a), E(b), E(c), crumb(a, b)) for a, b, c in cards)
    return ('<div class="cards">%s</div>' % h if h else EMPTY % "No open calls."), len(cards)


def says():
    items = []
    for part in rd(TRAFFIC).split("<!-- block -->")[1:]:
        first, _, body = part.strip().partition("\n")
        items.append((first.strip("# ").strip(), re.sub(r"\s+", " ", clean(body, 120))))
    items = items[:5]
    if not items:  # fallback: JUDY's spoken lines from her session log
        ls = [m.group(1) for m in (re.match(r"\s*judy > (.*?)\s+\[say-line", l) for l in rd(JLOG).splitlines()) if m]
        items = [("", clean(x, 120)) for x in ls[-5:][::-1]]
    if not items:
        return EMPTY % "No replies recorded yet.", 0
    hist = "".join("<li>%s%s</li>" % (E(a + " · ") if a else "", E(b)) for a, b in items)
    return '<div class="ticker mono"><div>%s</div></div><ul class="hist mono">%s</ul>' % (E(items[0][1]), hist), len(items)


TILES = [("sitrep", "Sit rep", "the board"), ("soi", "SOI", "standing info"), ("pullglass", "Pull queue", "glass"),
         ("roster", "Roster", "agents on call"), ("intake-2026-10-12", "Intake", "10/12 picks"),
         ("intake-report-2026-10-12", "Intake report", "10/12"), ("command-desk-mock", "Desk mock", "the first draft")]


def boards():
    try:
        pg = json.load(io.open(PAGES, encoding="utf-8"))
    except Exception:
        pg = {}
    t = ['<a class="tile" href="%s" target="_blank" rel="noopener"><div><b>%s</b><small>%s</small></div></a>'
         % (E(pg[k]), E(a), E(b)) for k, a, b in TILES if pg.get(k)]
    return (('<div class="grid">%s</div>' % "".join(t)) if t else EMPTY % "No boards in pages.json."), len(t)


EXTRA_CSS = """
.poll{color:var(--mut);margin-bottom:10px}
.chip{display:inline-block;border:1px solid var(--or);color:var(--or);border-radius:10px;padding:0 8px;margin-left:6px;font-size:12px}
.crumb{display:block;margin-top:6px;color:var(--or);text-decoration:none}
.crumb:hover,.crumb:focus-visible{text-decoration:underline;outline:none}
nav a small{display:block;font:11px "IBM Plex Mono",monospace;color:var(--or)}
section.hit{border-color:var(--or)}
.tile.st.boot .dot{background:var(--line);animation:none}
"""

JS = """
var mb=document.getElementById("mb");
mb.onclick=function(){var m=document.getElementById("meta").classList.toggle("on");mb.setAttribute("aria-expanded",m)};
var KEYS={"1":"stations","2":"waves","3":"calls","4":"boards"};
document.addEventListener("keydown",function(e){
 if(e.ctrlKey||e.metaKey||e.altKey||/INPUT|TEXTAREA|SELECT/.test((e.target.tagName||""))||!KEYS[e.key])return;
 var s=document.getElementById(KEYS[e.key]);if(!s)return;
 var o=document.querySelector("section.hit");if(o)o.classList.remove("hit");
 s.classList.add("hit");s.scrollIntoView({behavior:matchMedia("(prefers-reduced-motion:reduce)").matches?"auto":"smooth",block:"start"});
});
(function(){
 var done=false;try{done=sessionStorage.getItem("deskBoot")}catch(x){}
 if(done||matchMedia("(prefers-reduced-motion:reduce)").matches)return;
 try{sessionStorage.setItem("deskBoot","1")}catch(x){}
 var t=[].slice.call(document.querySelectorAll(".tile.st"));if(!t.length)return;
 var step=Math.min(250,1600/t.length);
 t.forEach(function(el,i){var d=el.querySelector(".dot");el.classList.add("boot");
  var sm=el.querySelector("small"),w=sm.textContent;sm.textContent="checking";
  setTimeout(function(){el.classList.remove("boot");sm.textContent=w},(i+1)*step)});
})();
"""


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    src = rd(MOCK)
    if not src:
        print("mock missing: " + MOCK)
        sys.exit(1)
    css = re.search(r"<style>.*?</style>", src, re.S).group(0)
    css = css.replace("</style>", EXTRA_CSS + "</style>")
    stn, ns = stations()
    wv, nw = waves()
    cl, nc = calls()
    sy, nsy = says()
    bd, nb = boards()
    now = dt.datetime.now()
    meta = "Built %d/%d %s from live sources. An empty section means its source had nothing." % (now.month, now.day, t12(now))
    page = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Command Desk</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Barlow+Condensed:wght@600;700&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">
%s
</head>
<body>
<header>
<h1>Command Desk</h1>
<span class="mono">built %s</span>
<span class="sp"></span>
<button id="mb" aria-expanded="false" aria-controls="meta">Info</button>
</header>
<div id="meta" class="mono">%s</div>
<div class="wrap">
<nav aria-label="Sections">
<a href="#stations" title="Key 1">STN<small>1</small></a><a href="#waves" title="Key 2">WAVE<small>2</small></a><a href="#calls" title="Key 3">CALL<small>3</small></a><a href="#says">SAY</a><a href="#boards" title="Key 4">BRD<small>4</small></a>
</nav>
<main>
<section id="stations"><h2>Stations</h2>%s</section>
<section id="waves"><h2><span data-tip="A wave is one detached batch of pulls running in the background." tabindex="0">Pull waves</span></h2>%s</section>
<section id="calls"><h2>Open calls</h2>%s</section>
<section id="says"><h2>Last five replies</h2>%s</section>
<section id="boards"><h2>Boards</h2>%s</section>
</main>
</div>
<script>%s</script>
</body>
</html>
""" % (css, t12(now), E(meta), stn, wv, cl, sy, bd, JS)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    io.open(OUT, "w", encoding="utf-8", newline="\n").write(page)
    print("desk built: %d bytes -> %s" % (len(page.encode("utf-8")), OUT))
    print("stations %s | waves %s | calls %s | replies %s | boards %s" % (
        "filled" if ns else "empty", nw or "empty", nc or "empty", nsy or "empty", nb or "empty"))


if __name__ == "__main__":
    main()
