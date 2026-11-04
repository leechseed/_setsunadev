# -*- coding: utf-8 -*-
"""The Console v2 (BOLO 141/142 · BOLO 153 ONE WINDOW, Chief 10/18): the one window the launch opens.
The boot sequence plays inside it, then the workspace: a rail of panes, a rail of the recent glasses, one main pane.
Everything wears the boot screen's look. The window snaps to the right half of the screen, top to taskbar.
Serves 127.0.0.1:8795 only.
  /  the frame · /panes.json · /glasses.json · /boot.json · /desk.json · /local/<name> (whitelist) · /glass/<id>/<file>
  /status.json · POST /cmd -> cmd.log · POST /show + /show.json (command glass hands the frame a glass)
  /review/docs · /review/doc?path= · /review/list · POST /review/send (BOLO 125, the review desk; engine _tools/reviewdesk)
Usage: python console.py              serve
       python console.py --open       open the window (or focus the open one) and snap it to the right half
       python console.py --status     run pull_queue.py report and cache status.json
       python console.py --store [key]  what glasses saved while open in the Console (_PRIVATE/console-stores/)
  /store/<key>/<collection>[/<doc>]  GET · PUT · PATCH · DELETE: the stand-in for a glass's claude.use("db")
"""
import os, sys, json, time, subprocess, threading, mimetypes, http.server, socketserver

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
PORT = 8795
URL = "http://127.0.0.1:%d/" % PORT
TITLE = "The Console"
CMDLOG = os.path.join(HERE, "cmd.log")
STATUS = os.path.join(HERE, "status.json")
GLASSES = os.path.join(HERE, "glasses.json")
BOOT = os.path.join(ROOT, "_tools", "launch", "boot.jsonl")
ART = os.path.join(ROOT, "_tools", "brand", "boldventure-ascii.txt")
MARK = os.path.join(ROOT, "_tools", "brand", "boldventure-mark.svg")   # the favicon and the window's icon
BOUNCE = os.path.join(ROOT, "_PRIVATE", "console")   # Chief 10/31: bounce.gif (or .webp/.png) here bounces on the boot; else the mark


def bounce_file():
    for ext in ("gif", "webp", "apng", "png", "jpg"):
        p = os.path.join(BOUNCE, "bounce." + ext)
        if os.path.isfile(p):
            return p
    return MARK


MUSIC = os.path.join(ROOT, "_PRIVATE", "audio", "boot-music.wav")   # Chief 10/19: the boot screen's idle music, looped until Space (a PCM copy; game audio stays out of the public repo)


def music(on):
    """the server plays it (winsound, async loop), so the browser's autoplay rule never mutes it"""
    try:
        import winsound
        if on and os.path.isfile(MUSIC):
            winsound.PlaySound(MUSIC, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        else:
            winsound.PlaySound(None, winsound.SND_PURGE)
    except Exception:
        pass
PQ = os.path.join(ROOT, "_PRIVATE", "taxonomy_engine", "pull_queue.py")
SNAP = "right"   # Chief 10/18: half the screen, top edge to the taskbar; the right half keeps VS Code on the left (provisional)

LOCAL = {   # the whitelist: name -> file
    "desk": os.path.join(ROOT, "_PRIVATE", "reference", "desk", "command-desk.html"),
    "pullqueue": os.path.join(ROOT, "_PRIVATE", "reference", "pullqueue", "pull-queue.html"),
    "roster": os.path.join(ROOT, "_tools", "roster", "roster.html"),
    "sitrep": os.path.join(ROOT, "SITREP.html"),
    "armory": os.path.join(ROOT, "_PRIVATE", "reference", "armory", "armory.html"),
    "fabula-graph": os.path.join(ROOT, "_PRIVATE", "intake-repos", "d3__d3", "fabula-graph.html"),
    "stash-erd": os.path.join(ROOT, "_PRIVATE", "reference", "erd", "stash-erd.html"),
    "zotero-erd": os.path.join(ROOT, "_PRIVATE", "reference", "erd", "zotero-erd.html"),
    "tropes": os.path.join(ROOT, "_tools", "tropes", "glass", "tropes.html"),   # BOLO 89, _tools/tropes/build_glass.py
    "europatch": os.path.join(ROOT, "_tools", "europatch", "patchbay.html"),   # BOLO 173, the patch bay (europatch.py build)
    "review": os.path.join(ROOT, "_tools", "reviewdesk", "review-desk.html"),   # BOLO 125, the review desk (11/4)
}
PANES = [   # the rail: six up front (Chief 10/18, rec taken), the rest behind "more"
    {"id": "desk", "title": "Desk", "url": "/local/desk"},
    {"id": "sitrep", "title": "Sit rep", "url": "/local/sitrep"},
    {"id": "stash", "title": "Stash", "url": "http://127.0.0.1:9999/"},
    {"id": "darkroom", "title": "DARKROOM", "url": "http://127.0.0.1:8484/"},
    {"id": "pullqueue", "title": "Pull Queue", "url": "/local/pullqueue"},
    {"id": "faces", "title": "Faces", "url": "http://127.0.0.1:8787/faces"},
    {"id": "roster", "title": "Roster", "url": "/local/roster", "more": True},
    {"id": "armory", "title": "Armory", "url": "/local/armory", "more": True},
    {"id": "traffic", "title": "Traffic", "url": "http://127.0.0.1:8787/traffic", "more": True},
    {"id": "fabula", "title": "Fabula graph", "url": "/local/fabula-graph", "more": True},
    {"id": "stash-erd", "title": "Stash ERD", "url": "/local/stash-erd", "more": True},
    {"id": "zotero-erd", "title": "Zotero ERD", "url": "/local/zotero-erd", "more": True},
    {"id": "tropes", "title": "Tropes", "url": "/local/tropes", "more": True},
    {"id": "europatch", "title": "Patch bay", "url": "/local/europatch", "more": True},
    {"id": "review", "title": "Review desk", "url": "/local/review", "more": True},   # BOLO 125 (provisional: behind "more")
]
REVIEWDESK = os.path.join(ROOT, "_tools", "reviewdesk", "reviewdesk.py")   # BOLO 125: the review desk's engine
_RD = []


def rd():
    """the review desk's engine, loaded once from its file (docs · read_doc · save · all_reviews)"""
    if not _RD:
        import importlib.util
        spec = importlib.util.spec_from_file_location("reviewdesk", REVIEWDESK)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _RD.append(mod)
    return _RD[0]
EUROPATCH = os.path.join(ROOT, "_tools", "europatch", "europatch.py")   # BOLO 173: the roll engine
EP_PATCHES = os.path.join(ROOT, "_PRIVATE", "europatch", "patches")      # saved patches (whitelisted names only)
EP_NAME = __import__("re").compile(r"^[a-z0-9][a-z0-9_-]{0,47}$")


def ep_roll(body):
    """POST /europatch/roll {patch, seed}: python europatch.py roll - --seed S --json; the patch goes in on stdin"""
    patch, seed = body.get("patch"), str(body.get("seed", "1"))
    if not isinstance(patch, dict) or not __import__("re").match(r"^[A-Za-z0-9_-]{1,64}$", seed):
        return 400, {"ok": False, "errors": ["a patch object and a seed (letters, digits, _ -)"]}
    try:
        r = subprocess.run([sys.executable, "-X", "utf8", EUROPATCH, "roll", "-", "--seed", seed, "--json"],
                           input=json.dumps(patch), capture_output=True, text=True, encoding="utf-8", timeout=30, cwd=ROOT)
        out = json.loads(r.stdout)
    except Exception as e:
        return 500, {"ok": False, "errors": ["europatch.py roll failed: %s" % e]}
    return 200, out


def ep_list():
    if not os.path.isdir(EP_PATCHES):
        return []
    return sorted(f[:-5] for f in os.listdir(EP_PATCHES) if f.endswith(".json") and EP_NAME.match(f[:-5]))


def write_status():
    line = "no pull status"
    try:
        r = subprocess.run([sys.executable, "-X", "utf8", PQ, "report"], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=60, cwd=ROOT)
        txt = [l.strip() for l in (r.stdout or "").splitlines() if l.strip()]
        if txt:
            line = " | ".join(txt[:3])[:200]
    except Exception:
        pass
    with open(STATUS, "w", encoding="utf-8") as f:
        json.dump({"pull": line, "at": time.strftime("%Y-%m-%d %H:%M")}, f)
    return line


def read_status():
    try:
        with open(STATUS, encoding="utf-8") as f:
            return json.load(f).get("pull") or "no pull status"
    except Exception:
        return "no pull status"


# ---- the recent glasses: glasses.py scans the transcripts; a thread keeps the list fresh ----
def glasses_loop():
    sys.path.insert(0, HERE)
    import glasses
    while True:
        try:
            glasses.write()
        except Exception:
            pass
        time.sleep(120)


def read_glasses():
    try:
        with open(GLASSES, encoding="utf-8") as f:
            return json.load(f).get("glasses") or []
    except Exception:
        return []


# ---- the desk's live data (BOLO 141, 10/31): the desk pane polls /desk.json every 60 s; build_desk.py --json, cached 30 s ----
DESK = os.path.join(ROOT, "_tools", "desk", "build_desk.py")
DESK_CACHE = {"at": 0.0, "body": None}
DESK_LOCK = threading.Lock()   # one build at a time; a second poll waits and takes the fresh copy


def desk_json():
    with DESK_LOCK:
        if DESK_CACHE["body"] is None or time.time() - DESK_CACHE["at"] > 30:
            try:
                r = subprocess.run([sys.executable, "-X", "utf8", DESK, "--json"], capture_output=True, timeout=30,
                                   cwd=ROOT, stdin=subprocess.DEVNULL)
                json.loads(r.stdout.decode("utf-8"))   # only good JSON replaces the cache
                DESK_CACHE.update(at=time.time(), body=r.stdout)
            except Exception:
                if DESK_CACHE["body"] is None:
                    return None
        return DESK_CACHE["body"]


# ---- the hand-off (command glass, 10/19): POST /show bumps seq; the frame polls /show.json and opens the glass ----
SHOW = {"seq": 0, "id": "", "url": "", "title": "", "boot": 0}   # memory only: a restart forgets the last pick
# boot: bumped by POST /boot (launch.py, when the Console was already up) so the open window replays the bounce;
# a window that stays open never reloads, so it never saw a launch's boot (Chief 10/31: "doesn't have the bouncing gif")
SHOW_LOCK = threading.Lock()


def show(gid, url, title):
    with SHOW_LOCK:
        SHOW.update(seq=SHOW["seq"] + 1, id=gid, url=url, title=title)


def bring():
    """the window to the front; a window opened just now only records seq on load, so the pick goes over again"""
    if open_window().startswith("opened"):
        time.sleep(2)
        show(SHOW["id"], SHOW["url"], SHOW["title"])


# ---- the boot sequence, for the window to draw: the launch's events plus the BoldVenture mark ----
def logo(scale=2):
    """boot.py's shrink: each scale x scale block keeps its densest character"""
    ramp = " .-+#"
    try:
        rows = [l.rstrip() for l in open(ART, encoding="utf-8").read().splitlines() if l.strip()]
    except OSError:
        return []
    ind = min(len(l) - len(l.lstrip()) for l in rows)
    rows = [l[ind:] for l in rows]
    w = max(len(l) for l in rows)
    rows = [l.ljust(w) for l in rows]
    out = []
    for y in range(0, len(rows), scale):
        line = ""
        for x in range(0, w, scale):
            block = [rows[yy][xx] for yy in range(y, min(y + scale, len(rows))) for xx in range(x, min(x + scale, w))]
            line += max(block, key=lambda c: ramp.index(c) if c in ramp else 0)
        out.append(line.rstrip())
    return out


LOGO = logo()


def read_boot():
    evs = []
    try:
        with open(BOOT, encoding="utf-8") as f:
            for l in f:
                try:
                    evs.append(json.loads(l))
                except ValueError:
                    pass
    except OSError:
        pass
    return {"logo": LOGO, "events": evs, "now": time.time()}


# ---- the fetch panel (Chief 10/18): neofetch-style numbers beside the spinning mark, for showing the Command off ----
_FETCH = {"at": 0, "rows": []}


def fetch_info():
    if time.time() - _FETCH["at"] < 60:
        return _FETCH["rows"]

    def git(*a):
        try:
            return subprocess.run(["git"] + list(a), cwd=ROOT, capture_output=True, text=True, timeout=10).stdout.strip()
        except Exception:
            return ""
    import glob, datetime as dt
    rows = []
    first = (git("log", "--reverse", "--format=%cs").splitlines() or [""])[0]
    try:
        days = (dt.date.today() - dt.date.fromisoformat(first)).days
        up = "%d days (since %s)" % (days, first)
    except ValueError:
        up = "?"
    try:
        with open(os.path.join(ROOT, "BOLO.md"), encoding="utf-8") as f:
            bolos = sum(1 for l in f if l[:2] == "| " and l[2:3].isdigit())
    except OSError:
        bolos = 0
    try:
        with open(os.path.join(ROOT, "_tools", "launch", "last_poll.json"), encoding="utf-8") as f:
            st = json.load(f)["stations"]
        stations = "%d/%d GO" % (sum(1 for s in st if s["go"]), len(st))
    except Exception:
        stations = "?"
    rows = [
        ("OS", "The Command · BoldVenture"),
        ("Kernel", "Claude Code · Opus 5.5 (CDR)"),
        ("Uptime", up),
        ("Commits", "{:,}".format(int(git("rev-list", "--count", "HEAD") or 0))),
        ("Stations", stations),
        ("BOLOs", "%d on the board" % bolos),
        ("Agents", "%d on call" % len(glob.glob(os.path.join(ROOT, ".claude", "agents", "*.md")))),
        ("Skills", "%d" % len(glob.glob(os.path.join(ROOT, ".claude", "skills", "*", "")))),
        ("Glasses", "%d published" % len(read_glasses())),
        ("Shell", "bash 5 · PowerShell 7"),
        ("Terminal", "The Console"),
        ("Voice", "JUDY"),
        ("Theme", "BoldVenture orange #FF5A1F"),
        ("Font", "IBM Plex Mono"),
    ]
    _FETCH.update(at=time.time(), rows=rows)
    return rows


def aliases():
    """a web URL the Command published -> the local page that holds the same thing (pages.json names; the pull glass is the pull queue)"""
    out = {}
    try:
        with open(os.path.join(ROOT, "_tools", "pages", "pages.json"), encoding="utf-8") as f:
            pages = json.load(f)
    except Exception:
        return out
    for name, url in pages.items():
        local = {"pullglass": "pullqueue"}.get(name, name)
        if local in LOCAL and isinstance(url, str):
            out[url] = "/local/" + local
        elif isinstance(url, str):   # else a local glass with the same title (the SOI lives at two web addresses)
            g = next((x for x in read_glasses() if x.get("local") and x.get("title", "").lower() == name.lower()), None)
            if g:
                out[url] = "/glass/%s/%s" % (g["id"], os.path.basename(g["file"]))
    return out


_FRAME = {}


def frameable(url):
    """does the site let another page frame it? X-Frame-Options or a CSP frame-ancestors rule says no; cached per host"""
    from urllib.parse import urlsplit
    import urllib.request
    host = urlsplit(url).netloc
    if host.startswith(("127.0.0.1", "localhost")):
        return True
    if host in _FRAME:
        return _FRAME[host]
    ok = False
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 the-console"}), timeout=6)
        xfo = (r.headers.get("X-Frame-Options") or "").strip()
        csp = (r.headers.get("Content-Security-Policy") or "").lower()
        fa = csp.split("frame-ancestors", 1)[1].split(";", 1)[0] if "frame-ancestors" in csp else None
        ok = not xfo and (fa is None or "*" in fa.split())
    except Exception:
        ok = False
    _FRAME[host] = ok
    return ok


STORES = os.path.join(ROOT, "_PRIVATE", "console-stores")   # 10/30: a glass's calls when it runs in the Console (private)
STORE_LOCK = threading.Lock()
# 10/30 (Chief: "Calls are not saving: the page could not reach its store"): a page opened from its local file has no
# claude.ai host, so window.claude is missing. The Console hands it a small stand-in for claude.use("db") that keeps the
# docs in _PRIVATE/console-stores/<key>.json, where the CDR reads them (python console.py --store <key>).
SHIM = r'''<script>(function(){if(window.claude&&window.claude.use)return;var K=%s,B="/store/"+encodeURIComponent(K)+"/";
function req(m,c,d,body){return fetch(B+encodeURIComponent(c)+(d!=null?"/"+encodeURIComponent(d):""),{method:m,headers:{"Content-Type":"application/json"},body:body==null?undefined:JSON.stringify(body)}).then(function(r){if(!r.ok)throw{code:"store-"+r.status};return r.json()})}
function snap(o){var docs=Object.keys(o).map(function(id){return{id:id,exists:true,data:function(){return o[id]}}});return{docs:docs,size:docs.length,empty:!docs.length,forEach:function(f){docs.forEach(f)}}}
function coll(c){return{doc:function(id){return{id:id,set:function(v){return req("PUT",c,id,v)},update:function(v){return req("PATCH",c,id,v)},delete:function(){return req("DELETE",c,id)},
get:function(){return req("GET",c).then(function(o){return{id:id,exists:id in o,data:function(){return o[id]}}})}}},
get:function(){return req("GET",c).then(snap)},
onSnapshot:function(ok,bad){var last=null,live=true;function tick(){if(!live)return;req("GET",c).then(function(o){var s=JSON.stringify(o);if(s!==last){last=s;ok(snap(o))}},function(e){if(bad)bad(e)}).then(function(){setTimeout(tick,3000)})}tick();return function(){live=false}}}}
var db={collection:coll,console:true};window.claude=window.claude||{};window.claude.use=function(n){return Promise.resolve(n==="db"?db:null)};})();</script>'''


def store_path(key):
    safe = "".join(ch if ch.isalnum() or ch in "-_." else "_" for ch in key)[:80] or "page"
    return os.path.join(STORES, safe + ".json")


def store_read(key):
    try:
        with open(store_path(key), encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


def page_bytes(path, key=None):
    """a page as the browser should get it: artifact fragments carry no skeleton, so give them one; with a key, the db stand-in"""
    with open(path, "rb") as fh:
        b = fh.read()
    html = path.lower().endswith((".html", ".htm"))
    if html and not b.lstrip()[:15].lower().startswith(b"<!doctype"):
        b = (b'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" '
             b'content="width=device-width,initial-scale=1"></head><body>' + b + b"</body></html>")
    if html and key:
        shim = (SHIM % json.dumps(key)).encode("utf-8")
        i = b.lower().find(b"<head>")
        b = b[:i + 6] + shim + b[i + 6:] if i >= 0 else shim + b
    return b


PAGE = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Console</title>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
/* the boot screen's look, everywhere (Chief 10/18): black ground, BoldVenture orange, mono, box lines, [  OK  ] tags */
:root{--bg:#050608;--fg:#c6cbc8;--dim:#5f6160;--acc:#FF5A1F;--accd:#6e280e;--accm:#be4216;--acch:#FFB08F;--ok:#4ec96f;--bad:#e5604d;--am:#e3b341;--hl:#10151b}
*{box-sizing:border-box}
html,body{margin:0;height:100%;background:var(--bg);color:var(--fg);font:13px/1.45 "IBM Plex Mono",Consolas,monospace}
body{display:grid;grid-template-rows:auto 1fr auto auto;padding:8px 12px;gap:6px;height:100vh;overflow:hidden}
.top{display:flex;justify-content:space-between;color:var(--dim);white-space:pre;overflow:hidden}
.top b{color:var(--acc)}
main{display:grid;grid-template-columns:250px 1fr;gap:8px;min-height:0}
.col{display:grid;grid-template-rows:auto 1fr;gap:16px;min-height:0;padding-top:.8em}
.box{position:relative;border:1px solid var(--dim);padding:14px 8px 8px;min-height:0;display:flex;flex-direction:column}
/* the label rides on the border, so the box itself never clips; the rail inside it scrolls (Chief 10/18: the cut-off labels) */
.box::before{content:"\2524 " attr(data-t) " \251C";position:absolute;top:-.8em;left:10px;background:var(--bg);padding:0 4px;color:var(--dim)}
.box.on{border-color:var(--acc)}.box.on::before{color:var(--acc)}
#main{padding:12px 0 0;flex-direction:row;margin-top:.8em}
.rail{flex:1;min-height:0;overflow:auto}
iframe{flex:1;border:0;width:100%;height:100%;background:var(--bg)}
.rail div{padding:1px 4px;cursor:pointer;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.rail div.sel{color:var(--bg);background:var(--acc)}.rail div:not(.sel):hover{background:var(--hl)}
.rail .k{color:var(--dim)}.rail div.sel .k{color:var(--bg)}
.rail .more{color:var(--dim)}
.rail .day{color:var(--acc);cursor:default;margin-top:6px}.rail .day:hover{background:none}
.rail .tm{color:var(--dim)}.rail div.sel .tm{color:var(--bg)}
.rail .web{color:var(--dim)}
.status{display:flex;justify-content:space-between;gap:12px;background:var(--hl);padding:2px 8px;white-space:nowrap;overflow:hidden}
.status b{color:var(--acc);font-weight:600}
.status>span{flex:none}.status>#st{flex:1 1 auto;min-width:0;overflow:hidden;text-overflow:ellipsis;text-align:center}/* 11/4: a long pull line ellipsizes, the key hints stay on screen (agent-browser check, BOLO 160) */
.cmd{display:flex;gap:8px;border-top:1px solid var(--dim);padding-top:4px}
.cmd span{color:var(--acc)}
.cmd input{flex:1;background:none;border:0;outline:0;color:var(--fg);font:inherit;caret-color:var(--acc)}
#flt{width:100%;background:none;border:0;border-bottom:1px solid var(--dim);outline:0;color:var(--fg);font:inherit;margin-bottom:6px}
.d{color:var(--dim)}
/* the boot overlay (Chief 10/31): the terminal already plays the full boot, so the window bounces the mark like a DVD
   screensaver while the launch runs; one status line at the bottom. The mark is /bounce (Chief's gif when it lands). */
#boot{position:fixed;inset:0;z-index:50;background:#000;overflow:hidden;cursor:pointer;transition:opacity .5s,background .3s}
#boot.gone{opacity:0;pointer-events:none}
#boot.corner{background:#1a0d07}
#dvd{position:absolute;left:0;top:0;width:min(24vw,280px);height:auto;will-change:transform;user-select:none;-webkit-user-drag:none}
.bv{color:var(--acc);font-weight:600}.g{color:var(--ok);font-weight:600}.r{color:var(--bad);font-weight:600}.y{color:var(--am);font-weight:600}.w{color:#fff;font-weight:600}
#bstat{position:fixed;left:18px;bottom:10px;color:var(--dim)}
#bskip{position:fixed;right:18px;bottom:10px;color:var(--dim)}
.blink{color:var(--acc);font-weight:600;animation:blink 1.1s steps(1) infinite}@keyframes blink{50%{opacity:0}}
</style></head><body>
<div id="boot"><img id="dvd" src="/bounce" alt="" draggable="false" data-tint=""><span id="bstat"></span><span id="bskip">SPACE · skip</span></div>
<div class="top"><span><b>&#9670; THE CONSOLE</b>  the Command &middot; Chief</span><span id="clk"></span></div>
<main>
 <div class="col">
  <section class="box on" data-t="PANES" id="pbox"><input id="flt" placeholder="/ filter" autocomplete="off"><div id="panes" class="rail"></div></section>
  <section class="box" data-t="GLASSES" id="gbox"><div id="glasses" class="rail"></div></section>
 </div>
 <section class="box" data-t="MAIN" id="main"><iframe id="fr" title="pane" allow="microphone"></iframe></section>
</main>
<div class="status"><span><b id="mode">NORMAL</b>  <b id="pn">-</b></span><span id="st" class="d"></span><span class="d">1-6 pane · / filter · : command · b boot</span></div>
<label class="cmd"><span>&gt;</span><input id="in" placeholder="press : for a command, / to filter" autocomplete="off"></label>
<script>
(function(){
var $=function(i){return document.getElementById(i)};
var panes=[],glasses=[],cur=null,more=false,fr=$('fr'),flt=$('flt'),inp=$('in');
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function hm(d){var h=d.getHours()%12||12;return h+':'+('0'+d.getMinutes()).slice(-2)+' '+(d.getHours()<12?'AM':'PM')}
function day(d){var t=new Date();t.setHours(0,0,0,0);var x=new Date(d);x.setHours(0,0,0,0);var n=Math.round((t-x)/864e5);
 return n===0?'TODAY':n===1?'YESTERDAY':['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'][x.getMonth()]+' '+x.getDate()}
function row(html,sel,fn,cls){var d=document.createElement('div');d.className=(sel?'sel ':'')+(cls||'');d.innerHTML=html;if(fn)d.onclick=fn;return d}
function draw(){var q=flt.value.toLowerCase(),P=$('panes'),G=$('glasses'),n=0;P.innerHTML='';G.innerHTML='';
 panes.forEach(function(p,i){if(p.more&&!more&&!q)return;if(q&&p.title.toLowerCase().indexOf(q)<0)return;
  P.appendChild(row('<span class="k">'+(p.more?'·':(i+1))+'</span> '+esc(p.title),cur&&cur.u===p.url,function(){open(p.url,p.title)}))});
 if(!q)P.appendChild(row(more?'&#9652; less':'&#9662; more ('+panes.filter(function(p){return p.more}).length+')',false,function(){more=!more;draw()},'more'));
 var last='';glasses.forEach(function(g){if(q&&g.title.toLowerCase().indexOf(q)<0)return;var d=new Date(g.when),k=day(d);
  if(k!==last){G.appendChild(row('&#9472;&#9472; '+k,false,null,'day'));last=k}
  var u=g.local?'/glass/'+g.id+'/'+encodeURIComponent(g.file.split(/[\\/]/).pop()):g.url;
  G.appendChild(row('<span class="tm">'+hm(d)+'</span> '+esc(g.title)+(g.local?'':' <span class="web">&#8599; web</span>'),cur&&cur.u===u,
   function(){if(g.local)open(u,g.title,'glass');else route(g.url,g.title)}));n++});
 $('gbox').setAttribute('data-t','GLASSES · '+n)}
/* links never leave for Firefox (Chief 10/19): a link inside a pane opens in the pane when it can (our own pages,
   a glass with a local copy, any site that allows frames); a site that refuses frames gets its own app window from
   the same Edge process the Console already runs. */
function route(href,label){var u,b=location.href;try{b=fr.contentWindow.location.href}catch(e){}try{u=new URL(href,b)}catch(e){return}
 if(!/^https?:$/.test(u.protocol))return;
 if(u.origin===location.origin){open(u.pathname+u.search,label||u.pathname,u.pathname.indexOf('/glass/')===0?'glass':'');return}
 if(alias[u.href]){open(alias[u.href],label||u.href);return}
 var g=glasses.find(function(g){return g.local&&g.url===u.href});
 if(g){open('/glass/'+g.id+'/'+encodeURIComponent(g.file.split(/[\\/]/).pop()),g.title,'glass');return}
 fetch('/open',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({url:u.href})})
 .then(function(r){return r.json()}).then(function(j){if(j.pane)open(u.href,label||u.hostname);else $('st').textContent='opened in its own window: '+u.hostname})}
function hook(){try{var w=fr.contentWindow,d=fr.contentDocument;if(!d||w.__routed)return;w.__routed=true;
 d.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(!a||e.defaultPrevented)return;
  var h=a.getAttribute('href');if(!h||h.charAt(0)==='#'||/^(javascript|mailto):/i.test(h))return;
  e.preventDefault();route(a.href,(a.textContent||'').trim().slice(0,40))},true);
 w.open=function(h){route(h);return null}}catch(e){}}   /* other ports (Stash, DARKROOM, JUDY) are cross-origin: their links stay theirs */
fr.addEventListener('load',hook);
function open(u,title,kind){cur={u:u,t:title};fr.src=u;$('main').setAttribute('data-t',title.toUpperCase());$('pn').textContent=title;
 $('pbox').classList.toggle('on',kind!=='glass');$('gbox').classList.toggle('on',kind==='glass');draw()}
function clk(){var d=new Date();$('clk').textContent=(d.getMonth()+1)+'/'+d.getDate()+'  '+hm(d)}
function stat(){fetch('/status.json').then(function(r){return r.json()}).then(function(j){$('st').textContent=j.pull}).catch(function(){})}
function gl(){fetch('/glasses.json').then(function(r){return r.json()}).then(function(j){glasses=j.glasses||[];draw()}).catch(function(){})}
/* command glass hands over a pick (POST /show bumps seq); a fresh load only records seq, so a reload never replays one */
var seq=-1,bootN=-1;function show(){fetch('/show.json').then(function(r){return r.json()}).then(function(j){
 if(seq>=0&&j.seq!==seq&&j.url){if(booting)skip();if(j.url.charAt(0)==='/')open(j.url,j.title,'glass');else route(j.url,j.title)}seq=j.seq;
 if(bootN>=0&&j.boot!==bootN&&!booting){$('dvd').src='/bounce?'+j.boot;boot(true)}bootN=j.boot}).catch(function(){})}   /* a new launch: the bounce again */
var alias={};
fetch('/panes.json').then(function(r){return r.json()}).then(function(j){panes=j.panes;alias=j.aliases||{};open(panes[0].url,panes[0].title)});
clk();stat();gl();show();setInterval(clk,15000);setInterval(stat,60000);setInterval(gl,60000);setInterval(show,1500);
flt.oninput=draw;
flt.addEventListener('keydown',function(e){if(e.key==='Escape'){flt.value='';draw();flt.blur()}
 else if(e.key==='Enter'){var q=flt.value.toLowerCase(),p=panes.find(function(p){return p.title.toLowerCase().indexOf(q)>=0}),
  g=glasses.find(function(g){return g.local&&g.title.toLowerCase().indexOf(q)>=0});
  if(p)open(p.url,p.title);else if(g)open('/glass/'+g.id+'/'+encodeURIComponent(g.file.split(/[\\/]/).pop()),g.title,'glass');flt.blur()}});
flt.addEventListener('focus',function(){$('mode').textContent='FILTER'});flt.addEventListener('blur',function(){$('mode').textContent='NORMAL'});
inp.addEventListener('keydown',function(e){if(e.key==='Escape'){inp.value='';inp.blur();return}
 if(e.key==='Enter'&&inp.value.trim()){var line=inp.value.trim();inp.value='';
  fetch('/cmd',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({line:line})})
  .then(function(){inp.placeholder='logged; JUDY wiring next'}).catch(function(){inp.placeholder='command failed'})}});
document.addEventListener('keydown',function(e){var t=e.target;if(t===inp||t===flt)return;if(booting){if(e.key===' '||e.key==='Enter'){e.preventDefault();skip()}return}
 if(e.key>='1'&&e.key<='6'){var p=panes[+e.key-1];if(p)open(p.url,p.title)}
 else if(e.key==='/'){e.preventDefault();flt.focus()}
 else if(e.key===':'){e.preventDefault();inp.focus()}
 else if(e.key==='b'){boot(true)}});

/* ---- the boot: the mark bounces like a DVD screensaver (Chief 10/31) while the launch writes boot.jsonl ---- */
var booting=false,timer=null,BX=null;
/* each wall hit shifts the hue, the way the DVD logo changed color; a corner hit flashes the screen */
function bounce(){var el=$('dvd'),tok={},red=matchMedia('(prefers-reduced-motion: reduce)').matches,
  x=Math.random()*Math.max(0,innerWidth-300),y=Math.random()*Math.max(0,innerHeight-300),
  vx=(Math.random()<.5?-1:1)*150,vy=(Math.random()<.5?-1:1)*115,hue=0,last=performance.now();
 BX=tok;
 function f(now){if(!booting||BX!==tok)return;
  var dt=Math.min(.05,(now-last)/1000),W=Math.max(0,innerWidth-el.offsetWidth),H=Math.max(0,innerHeight-el.offsetHeight),hx=false,hy=false;
  last=now;if(!red){x+=vx*dt;y+=vy*dt}
  if(x<=0){x=0;vx=Math.abs(vx);hx=true}else if(x>=W){x=W;vx=-Math.abs(vx);hx=true}
  if(y<=0){y=0;vy=Math.abs(vy);hy=true}else if(y>=H){y=H;vy=-Math.abs(vy);hy=true}
  if(!red&&(hx||hy)){if(el.dataset.tint){hue=(hue+60+Math.random()*120)%360;el.style.filter='hue-rotate('+Math.round(hue)+'deg)'}   /* the mark only; a picture keeps its colors */
   if(hx&&hy){$('boot').classList.add('corner');setTimeout(function(){$('boot').classList.remove('corner')},600)}}
  el.style.transform='translate('+Math.round(x)+'px,'+Math.round(y)+'px)';requestAnimationFrame(f)}
 requestAnimationFrame(f)}
/* one status line from boot.json: the station running now and the GO count; it holds on Space when the launch ends */
function poll(){if(!booting)return;
 fetch('/boot.json').then(function(r){return r.json()}).then(function(b){if(!booting)return;
  var ev=b.events||[],ok=0,bad=0,end=false,run=null;
  ev.forEach(function(e){if(e.state==='start')run=e.station;else if(e.state==='done'){run=null;if(e.go)ok++;else bad++}else if(e.state==='end')end=true});
  var done=end||!ev.length,s;
  if(!ev.length)s='<span class="d">no launch on record · the workspace is ready</span>';
  else if(end)s=bad?'<span class="r">'+bad+' NO-GO</span> · <span class="g">'+ok+' GO</span> <span class="d">· the sit rep carries the details</span>'
   :'<span class="g">Reached target </span><span class="bv">The Command</span><span class="g">.  ALL GO ('+ok+')</span>';
  else s='<span class="y">loading</span> <span class="w">'+esc(run||'...')+'</span> <span class="d">· '+ok+' GO'+(bad?' · '+bad+' NO-GO':'')+'</span>';
  $('bstat').innerHTML=s;
  $('bskip').className=done?'blink':'';$('bskip').textContent=done?'press SPACE to continue':'SPACE · skip';   /* Chief 10/18: the boot holds until Space */
  if(!done)timer=setTimeout(poll,500)}).catch(function(){timer=setTimeout(poll,1500)})}
/* no music on the boot (Chief 10/31: "remove the bg music") */
function skip(){booting=false;clearTimeout(timer);$('boot').classList.add('gone')}
function boot(replay){booting=true;$('boot').classList.remove('gone');bounce();poll()}
$('boot').onclick=skip;
boot(false);
})();
</script></body></html>
'''


class H(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, body, ctype):
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        from urllib.parse import unquote
        path = unquote(self.path.split("?")[0])
        if path == "/":
            page = PAGE.replace('data-tint=""', 'data-tint="1"') if bounce_file() == MARK else PAGE
            return self._send(200, page, "text/html; charset=utf-8")
        if path in ("/favicon.svg", "/favicon.ico") and os.path.isfile(MARK):   # the BoldVenture bunny bandit (Chief 10/18)
            with open(MARK, "rb") as fh:
                return self._send(200, fh.read(), "image/svg+xml")
        if path == "/bounce":   # the boot's bouncing mark (Chief 10/31)
            f = bounce_file()
            if os.path.isfile(f):
                with open(f, "rb") as fh:
                    return self._send(200, fh.read(), "image/svg+xml" if f.endswith(".svg") else mimetypes.guess_type(f)[0] or "image/gif")
        if path == "/panes.json":
            return self._send(200, json.dumps({"panes": PANES, "aliases": aliases()}), "application/json; charset=utf-8")
        if path == "/glasses.json":
            return self._send(200, json.dumps({"glasses": read_glasses()}, ensure_ascii=False), "application/json; charset=utf-8")
        if path == "/desk.json":
            body = desk_json()
            if body is None:
                return self._send(503, '{"error":"build_desk.py --json failed"}', "application/json; charset=utf-8")
            return self._send(200, body, "application/json; charset=utf-8")
        if path == "/boot.json":
            b = read_boot()
            b["fetch"] = fetch_info()
            return self._send(200, json.dumps(b, ensure_ascii=False), "application/json; charset=utf-8")
        if path == "/status.json":
            return self._send(200, json.dumps({"pull": read_status()}), "application/json; charset=utf-8")
        if path == "/show.json":
            with SHOW_LOCK:
                s = {"seq": SHOW["seq"], "url": SHOW["url"], "title": SHOW["title"], "boot": SHOW["boot"]}
            return self._send(200, json.dumps(s, ensure_ascii=False), "application/json; charset=utf-8")
        if path == "/europatch/patches":
            return self._send(200, json.dumps({"patches": ep_list()}), "application/json; charset=utf-8")
        if path.startswith("/europatch/patches/"):
            name = path[19:]
            f = os.path.join(EP_PATCHES, name + ".json")
            if EP_NAME.match(name) and os.path.isfile(f):
                with open(f, "rb") as fh:
                    return self._send(200, fh.read(), "application/json; charset=utf-8")
            return self._send(404, '{"error":"no such patch"}', "application/json")
        if path in ("/review/docs", "/review/doc", "/review/list"):   # BOLO 125, the review desk
            from urllib.parse import urlparse, parse_qs
            try:
                if path == "/review/docs":
                    out = {"docs": rd().docs()}
                elif path == "/review/list":
                    out = {"reviews": [rd().brief(r) for r in rd().all_reviews()][:50]}
                else:
                    out = rd().read_doc((parse_qs(urlparse(self.path).query).get("path") or [""])[0])
                    if out is None:
                        return self._send(404, '{"ok":false,"errors":["no such .md doc in the repo"]}', "application/json")
            except Exception as e:
                return self._send(500, json.dumps({"ok": False, "errors": [str(e)]}), "application/json")
            return self._send(200, json.dumps(out, ensure_ascii=False), "application/json; charset=utf-8")
        if path.startswith("/local/"):
            f = LOCAL.get(path[7:])
            if f and os.path.isfile(f):
                return self._send(200, page_bytes(f, "local-" + path[7:]), "text/html; charset=utf-8")
        if path.startswith("/store/"):   # the db stand-in: GET /store/<key>/<collection> -> {doc id: data}
            parts = path[7:].split("/")
            if len(parts) == 2:
                with STORE_LOCK:
                    data = store_read(parts[0]).get("collections", {}).get(parts[1], {})
                return self._send(200, json.dumps(data, ensure_ascii=False), "application/json; charset=utf-8")
        if path.startswith("/glass/"):   # /glass/<id>/<file>: only files a publish named, and their own folder's assets
            parts = path[7:].split("/", 1)
            g = next((x for x in read_glasses() if x.get("id") == parts[0] and x.get("local")), None)
            if g and len(parts) == 2:
                base = os.path.dirname(os.path.abspath(g["file"]))
                f = os.path.abspath(os.path.join(base, parts[1]))
                if f.startswith(base + os.sep) and os.path.isfile(f):
                    ctype = mimetypes.guess_type(f)[0] or "application/octet-stream"
                    if ctype.startswith("text/") or ctype.endswith(("json", "javascript")):
                        ctype += "; charset=utf-8"
                    return self._send(200, page_bytes(f, g["id"]), ctype)
        self._send(404, "not found", "text/plain")

    def _store(self, method):
        """the db stand-in's writes: PUT sets a doc, PATCH merges into it, DELETE removes it"""
        from urllib.parse import unquote
        parts = [unquote(p) for p in self.path.split("?")[0][7:].split("/")]
        if not self.path.startswith("/store/") or len(parts) != 3:
            return self._send(404, "not found", "text/plain")
        key, coll, doc = parts
        body = None
        if method != "DELETE":
            n = min(int(self.headers.get("Content-Length") or 0), 1 << 20)
            try:
                body = json.loads(self.rfile.read(n) or b"null")
            except ValueError:
                return self._send(400, '{"error":"bad json"}', "application/json")
            if not isinstance(body, dict):
                return self._send(400, '{"error":"a doc is an object"}', "application/json")
        with STORE_LOCK:
            s = store_read(key)
            if not s:
                g = next((x for x in read_glasses() if x.get("id") == key), {})
                s = {"key": key, "url": g.get("url", ""), "title": g.get("title", key), "collections": {}}
            c = s["collections"].setdefault(coll, {})
            if method == "PUT":
                c[doc] = body
            elif method == "PATCH":
                c[doc] = dict(c.get(doc) or {}, **body)
            else:
                c.pop(doc, None)
            s["updated"] = time.strftime("%Y-%m-%d %H:%M:%S")
            os.makedirs(STORES, exist_ok=True)
            tmp = store_path(key) + ".tmp"
            with open(tmp, "w", encoding="utf-8") as fh:
                json.dump(s, fh, ensure_ascii=False, indent=1)
            os.replace(tmp, store_path(key))
        return self._send(200, '{"ok":true}', "application/json")

    def do_PUT(self):
        return self._store("PUT")

    def do_PATCH(self):
        return self._store("PATCH")

    def do_DELETE(self):
        return self._store("DELETE")

    def do_POST(self):
        if self.path == "/review/send":   # BOLO 125: one review.json + its audio -> _PRIVATE/reviews/<doc-slug>-<ts>/
            try:
                n = int(self.headers.get("Content-Length") or 0)
                if n > (96 << 20):
                    return self._send(413, '{"ok":false,"errors":["a review is under 96 MB"]}', "application/json")
                body = json.loads(self.rfile.read(n).decode("utf-8"))
            except Exception:
                return self._send(400, '{"ok":false,"errors":["bad json"]}', "application/json")
            try:
                code, out = rd().save(body)
            except Exception as e:
                code, out = 500, {"ok": False, "errors": ["save failed: %s" % e]}
            return self._send(code, json.dumps(out, ensure_ascii=False), "application/json; charset=utf-8")
        if self.path == "/europatch/roll" or self.path.startswith("/europatch/patches/"):   # BOLO 173, the patch bay
            try:
                n = int(self.headers.get("Content-Length") or 0)
                if n > (1 << 20):
                    return self._send(413, '{"ok":false,"errors":["a patch is under 1 MB"]}', "application/json")
                body = json.loads(self.rfile.read(n).decode("utf-8"))
            except Exception:
                return self._send(400, '{"ok":false,"errors":["bad json"]}', "application/json")
            if self.path == "/europatch/roll":
                code, out = ep_roll(body if isinstance(body, dict) else {})
                return self._send(code, json.dumps(out, ensure_ascii=False), "application/json; charset=utf-8")
            name = self.path[19:]
            if not EP_NAME.match(name) or not isinstance(body, dict) or not body.get("europatch"):
                return self._send(400, '{"ok":false,"errors":["a whitelisted name (a-z 0-9 _ -) and a patch object"]}', "application/json")
            os.makedirs(EP_PATCHES, exist_ok=True)
            tmp = os.path.join(EP_PATCHES, name + ".json.tmp")
            with open(tmp, "w", encoding="utf-8", newline=chr(10)) as fh:
                json.dump(body, fh, ensure_ascii=False, indent=1)
            os.replace(tmp, os.path.join(EP_PATCHES, name + ".json"))
            return self._send(200, json.dumps({"ok": True, "name": name}), "application/json")
        if self.path == "/open":   # a link from a pane: in the pane if the site allows frames, else its own app window
            try:
                n = min(int(self.headers.get("Content-Length") or 0), 8192)
                url = str(json.loads(self.rfile.read(n).decode("utf-8")).get("url", ""))
            except Exception:
                return self._send(400, json.dumps({"ok": False}), "application/json")
            if not url.startswith(("http://", "https://")):
                return self._send(400, json.dumps({"ok": False}), "application/json")
            if frameable(url):
                return self._send(200, json.dumps({"pane": True}), "application/json")
            exe = app_exe()
            if exe:
                subprocess.Popen([exe, "--app=" + url], cwd=ROOT, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return self._send(200, json.dumps({"pane": False, "window": bool(exe)}), "application/json")
        if self.path == "/show":   # command glass: only an id comes in, checked against the list
            from urllib.parse import quote
            try:
                n = min(int(self.headers.get("Content-Length") or 0), 1024)
                body = json.loads(self.rfile.read(n).decode("utf-8"))
                gid = str(body.get("glass", ""))
                pid = str(body.get("pane", ""))
            except Exception:
                return self._send(400, json.dumps({"ok": False}), "application/json")
            if pid:   # command tropes (BOLO 89): a /local/ pane by id, checked against PANES
                p = next((x for x in PANES if x["id"] == pid and x["url"].startswith("/local/")), None)
                if not p:
                    return self._send(400, json.dumps({"ok": False, "error": "unknown pane"}), "application/json")
                show(pid, p["url"], p["title"])
                threading.Thread(target=bring, daemon=True).start()
                return self._send(200, json.dumps({"ok": True, "seq": SHOW["seq"], "url": p["url"]}), "application/json")
            g = next((x for x in read_glasses() if gid and x.get("id") == gid), None) or {}
            url = str(g.get("url", ""))
            if g.get("local"):   # the same path the rail builds, encodeURIComponent's safe set
                url = "/glass/%s/%s" % (gid, quote(os.path.basename(g.get("file", "")), safe="!*'()"))
            if not g or not url.startswith(("/glass/", "https://")):
                return self._send(400, json.dumps({"ok": False, "error": "unknown glass"}), "application/json")
            show(gid, url, str(g.get("title") or gid))
            threading.Thread(target=bring, daemon=True).start()
            return self._send(200, json.dumps({"ok": True, "seq": SHOW["seq"], "url": url}), "application/json")
        if self.path == "/boot":   # replay the bounce in the open window (the launch found the Console already up)
            with SHOW_LOCK:
                SHOW["boot"] += 1
            return self._send(200, json.dumps({"ok": True, "boot": SHOW["boot"]}), "application/json")
        if self.path in ("/music/start", "/music/stop"):
            music(self.path.endswith("start"))
            return self._send(200, "ok", "text/plain")
        if self.path == "/quit":   # console.py --restart asks the old server to step down (no port scan needed)
            self._send(200, "bye", "text/plain")
            threading.Thread(target=lambda: (time.sleep(0.3), os._exit(0)), daemon=True).start()
            return
        if self.path != "/cmd":
            return self._send(404, "not found", "text/plain")
        try:
            n = min(int(self.headers.get("Content-Length") or 0), 4096)
            line = str(json.loads(self.rfile.read(n).decode("utf-8")).get("line", "")).replace("\n", " ")[:500]
            with open(CMDLOG, "a", encoding="utf-8") as f:
                f.write("%s\t%s\n" % (time.strftime("%Y-%m-%d %H:%M:%S"), line))
            self._send(200, json.dumps({"ok": True, "note": "logged; JUDY wiring next"}), "application/json")
        except Exception as e:
            self._send(400, json.dumps({"ok": False, "error": str(e)}), "application/json")


class S(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


# ---- the window: one Chromium app window, found by title, snapped to half the work area ----
def app_exe():
    for exe in (os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
                os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
                os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe"),
                os.path.expandvars(r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"),
                os.path.expandvars(r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe")):
        if os.path.exists(exe):
            return exe
    return None


def find_windows(title):
    import ctypes
    from ctypes import wintypes
    u = ctypes.windll.user32
    found = []

    @ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
    def cb(h, _):
        if u.IsWindowVisible(h):
            n = u.GetWindowTextLengthW(h)
            if n:
                b = ctypes.create_unicode_buffer(n + 1)
                u.GetWindowTextW(h, b, n + 1)
                if b.value == title or b.value.startswith(title + " -"):
                    found.append(h)
        return True
    u.EnumWindows(cb, 0)
    return found


def snap(h, side=SNAP):
    """half the work area, top edge at the top, bottom edge on the taskbar; the invisible resize border is paid back"""
    import ctypes
    from ctypes import wintypes
    u, dwm = ctypes.windll.user32, ctypes.windll.dwmapi
    wa = wintypes.RECT()
    u.SystemParametersInfoW(0x0030, 0, ctypes.byref(wa), 0)   # SPI_GETWORKAREA: the screen minus the taskbar
    half = (wa.right - wa.left) // 2
    x = wa.left + (half if side == "right" else 0)
    u.ShowWindow(h, 9)   # SW_RESTORE: a maximized window ignores a move
    u.SetWindowPos(h, 0, x, wa.top, half, wa.bottom - wa.top, 0x0004 | 0x0010)
    time.sleep(0.15)
    wr, fr = wintypes.RECT(), wintypes.RECT()
    u.GetWindowRect(h, ctypes.byref(wr))
    if dwm.DwmGetWindowAttribute(h, 9, ctypes.byref(fr), ctypes.sizeof(fr)) == 0:   # DWMWA_EXTENDED_FRAME_BOUNDS: the visible frame
        l, t = fr.left - wr.left, fr.top - wr.top
        r, b = wr.right - fr.right, wr.bottom - fr.bottom
        u.SetWindowPos(h, 0, x - l, wa.top - t, half + l + r, wa.bottom - wa.top + t + b, 0x0004 | 0x0010)
    u.SetForegroundWindow(h)


def open_window():
    """focus the one Console window if it is up, else open it; either way snap it. Returns a note for the launch."""
    import ctypes
    try:
        ctypes.windll.user32.SetProcessDpiAwarenessContext(ctypes.c_void_p(-4))   # per-monitor v2: real pixels in and out
    except Exception:
        pass
    hs = find_windows(TITLE)
    if hs:
        snap(hs[0])
        return "focused the open window" + (" (%d more open)" % (len(hs) - 1) if len(hs) > 1 else "")
    exe = app_exe()
    if not exe:
        return "no Chrome or Edge for the app window"
    subprocess.Popen([exe, "--app=" + URL], cwd=ROOT, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(60):
        time.sleep(0.25)
        hs = find_windows(TITLE)
        if hs:
            snap(hs[0])
            return "opened · snapped %s" % SNAP
    return "opened · window not found to snap"


if __name__ == "__main__":
    if "--store" in sys.argv:   # what a glass saved in the Console: --store lists them, --store <key> prints one
        i = sys.argv.index("--store")
        if i + 1 < len(sys.argv):
            print(json.dumps(store_read(sys.argv[i + 1]), ensure_ascii=False, indent=1))
        else:
            for f in sorted(os.listdir(STORES)) if os.path.isdir(STORES) else []:
                s = store_read(f[:-5])
                n = sum(len(v) for v in s.get("collections", {}).values())
                print(f"{f[:-5]:<24} {n:>4} doc(s)  {s.get('updated', '')}  {s.get('title', '')}")
        sys.exit(0)
    if "--status" in sys.argv:
        print(write_status())
        sys.exit(0)
    if "--open" in sys.argv:
        print(open_window())
        sys.exit(0)
    if "--restart" in sys.argv:   # new code live: the old server quits, a fresh one starts detached, the window reloads
        import urllib.request
        try:
            urllib.request.urlopen(urllib.request.Request(URL + "quit", data=b"", method="POST"), timeout=3)
            time.sleep(1.0)
        except Exception:
            pass
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        si.wShowWindow = 7
        subprocess.Popen([sys.executable, "-u", os.path.abspath(__file__)], cwd=ROOT, startupinfo=si,
                         creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.CREATE_NEW_PROCESS_GROUP,
                         stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for _ in range(20):
            time.sleep(0.5)
            try:
                urllib.request.urlopen(URL, timeout=2)
                break
            except Exception:
                pass
        import ctypes
        for h in find_windows(TITLE):
            ctypes.windll.user32.PostMessageW(h, 0x0010, 0, 0)
        time.sleep(1.5)
        print("restarted · " + open_window())
        sys.exit(0)
    threading.Thread(target=glasses_loop, daemon=True).start()
    S(("127.0.0.1", PORT), H).serve_forever()
