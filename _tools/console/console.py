# -*- coding: utf-8 -*-
"""The Console v2 (BOLO 141/142 · BOLO 153 ONE WINDOW, Chief 10/18): the one window the launch opens.
The boot sequence plays inside it, then the workspace: a rail of panes, a rail of the recent glasses, one main pane.
Everything wears the boot screen's look. The window snaps to the right half of the screen, top to taskbar.
Serves 127.0.0.1:8795 only.
  /  the frame · /panes.json · /glasses.json · /boot.json · /local/<name> (whitelist) · /glass/<id>/<file>
  /status.json · POST /cmd -> cmd.log
Usage: python console.py              serve
       python console.py --open       open the window (or focus the open one) and snap it to the right half
       python console.py --status     run pull_queue.py report and cache status.json
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
]


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


def page_bytes(path):
    """a page as the browser should get it: artifact fragments carry no skeleton, so give them one"""
    with open(path, "rb") as fh:
        b = fh.read()
    if path.lower().endswith((".html", ".htm")) and not b.lstrip()[:15].lower().startswith(b"<!doctype"):
        b = (b'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" '
             b'content="width=device-width,initial-scale=1"></head><body>' + b + b"</body></html>")
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
.box{position:relative;border:1px solid var(--dim);padding:14px 8px 8px;overflow:auto;min-height:0}
.box::before{content:"\2524 " attr(data-t) " \251C";position:absolute;top:-.8em;left:10px;background:var(--bg);padding:0 4px;color:var(--dim)}
.box.on{border-color:var(--acc)}.box.on::before{color:var(--acc)}
#main{padding:0;overflow:hidden;display:flex;margin-top:.8em}
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
.cmd{display:flex;gap:8px;border-top:1px solid var(--dim);padding-top:4px}
.cmd span{color:var(--acc)}
.cmd input{flex:1;background:none;border:0;outline:0;color:var(--fg);font:inherit;caret-color:var(--acc)}
#flt{width:100%;background:none;border:0;border-bottom:1px solid var(--dim);outline:0;color:var(--fg);font:inherit;margin-bottom:6px}
.d{color:var(--dim)}
/* the boot overlay: the same sequence boot.py draws, inside the window */
#boot{position:fixed;inset:0;z-index:50;background:var(--bg);padding:14px 18px;overflow:hidden;cursor:pointer;transition:opacity .5s}
#boot.gone{opacity:0;pointer-events:none}
#boot pre{margin:0;white-space:pre;font:inherit}
#logo{line-height:1;letter-spacing:0}
#logo .a{color:var(--accd)}#logo .b{color:var(--accm)}#logo .c{color:var(--acc)}#logo .e{color:var(--acch);font-weight:600}
.bv{color:var(--acc);font-weight:600}.o{color:var(--acc)}.g{color:var(--ok);font-weight:600}.r{color:var(--bad);font-weight:600}.y{color:var(--am);font-weight:600}.w{color:#fff;font-weight:600}
#bskip{position:fixed;right:18px;bottom:10px;color:var(--dim)}
</style></head><body>
<div id="boot"><pre id="logo"></pre><pre id="blines"></pre><span id="bskip">any key · skip</span></div>
<div class="top"><span><b>&#9670; THE CONSOLE</b>  the Command &middot; Chief</span><span id="clk"></span></div>
<main>
 <div class="col">
  <section class="box on" data-t="PANES" id="pbox"><input id="flt" placeholder="/ filter" autocomplete="off"><div id="panes" class="rail"></div></section>
  <section class="box" data-t="GLASSES" id="gbox"><div id="glasses" class="rail"></div></section>
 </div>
 <section class="box" data-t="MAIN" id="main"><iframe id="fr" title="pane"></iframe></section>
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
   function(){if(g.local)open(u,g.title,'glass');else window.open(g.url,'_blank')}));n++});
 $('gbox').setAttribute('data-t','GLASSES · '+n)}
function open(u,title,kind){cur={u:u,t:title};fr.src=u;$('main').setAttribute('data-t',title.toUpperCase());$('pn').textContent=title;
 $('pbox').classList.toggle('on',kind!=='glass');$('gbox').classList.toggle('on',kind==='glass');draw()}
function clk(){var d=new Date();$('clk').textContent=(d.getMonth()+1)+'/'+d.getDate()+'  '+hm(d)}
function stat(){fetch('/status.json').then(function(r){return r.json()}).then(function(j){$('st').textContent=j.pull}).catch(function(){})}
function gl(){fetch('/glasses.json').then(function(r){return r.json()}).then(function(j){glasses=j.glasses||[];draw()}).catch(function(){})}
fetch('/panes.json').then(function(r){return r.json()}).then(function(j){panes=j.panes;open(panes[0].url,panes[0].title)});
clk();stat();gl();setInterval(clk,15000);setInterval(stat,60000);setInterval(gl,60000);
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
document.addEventListener('keydown',function(e){var t=e.target;if(t===inp||t===flt)return;if(booting){skip();return}
 if(e.key>='1'&&e.key<='6'){var p=panes[+e.key-1];if(p)open(p.url,p.title)}
 else if(e.key==='/'){e.preventDefault();flt.focus()}
 else if(e.key===':'){e.preventDefault();inp.focus()}
 else if(e.key==='b'){boot(true)}});

/* ---- the boot sequence: the launch writes boot.jsonl; the window draws it like boot.py does ---- */
var booting=false,timer=null;
var EARLY=[[':: running early hook','[udev]'],[':: running hook','[keymap]'],[':: mounting',"'/dev/q' on real root"],
 [':: loading','the Command · SOP · BOLO · STATE'],[':: starting','systemd-launch (BOLO 58)']];
function pad(s,n){s=String(s);while(s.length<n)s+=' ';return s}
function stamp(s){var t=s.toFixed(3);while(t.length<8)t=' '+t;return '<span class="d">['+t+']</span>'}
function logoHTML(rows){var C={'.':'a','-':'b','+':'c','#':'e'};return rows.map(function(l){var o='';for(var i=0;i<l.length;i++){var c=l[i];
 o+=C[c]?'<span class="'+C[c]+'">'+esc(c)+'</span>':esc(c)}return o}).join('\n')}
function stationLine(ev,t){var go=ev.go,note=(ev.note||'').slice(0,52);
 if(ev.waves&&ev.waves.length)note=ev.waves.length+' waves open';
 var o=stamp(t)+' '+(go?'<span class="g">[  OK  ]</span>':'<span class="r">[FAILED]</span>')+' <span class="w">'+esc(pad(ev.station,10))+'</span> '+
  '<span class="d">'+Array(31).join('.')+'</span> '+(go?'<span class="g">GO    </span>':'<span class="r">NO-GO </span>')+' <span class="d">'+esc(note)+'</span>';
 (ev.sub||[]).forEach(function(s){o+='\n           <span class="d">&#9492;&#9472; '+esc(s.slice(0,92))+'</span>'});
 (ev.waves||[]).forEach(function(w){o+='\n           <span class="d">&#9492;&#9472; </span><span class="'+(w.indexOf('STALLED')>=0?'r':'g')+'">'+esc(w.slice(0,90))+'</span>'});
 return o}
function skip(){booting=false;clearTimeout(timer);$('boot').classList.add('gone')}
function boot(replay){booting=true;$('boot').classList.remove('gone');
 fetch('/boot.json').then(function(r){return r.json()}).then(function(b){
  var lg=$('logo');lg.innerHTML=logoHTML(b.logo)+'\n\n<span class="bv">        B  O  L  D  V  E  N  T  U  R  E</span>\n<span class="d">   &#9472;&#9472; the Command · launch sequence &#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;</span>';
  var cols=Math.max.apply(null,b.logo.map(function(l){return l.length}).concat([60])),fs=Math.max(5,Math.min(12,Math.floor(innerWidth/(cols*0.62))));lg.style.fontSize=fs+'px';
  var ev=b.events,ended=ev.some(function(e){return e.state==='end'}),old=ended&&ev.length&&(b.now-ev[ev.length-1].t>120);
  var fast=replay||old,t0=ev.length?ev[0].t:b.now,lines=[],i=0,shown=0,start=Date.now(),pos=0,running=null,frame=0;
  EARLY.forEach(function(x,j){lines.push(stamp(0.12*(j+1))+' <span class="o">'+x[0]+'</span> '+esc(x[1]))});lines.push('');
  function paint(extra){$('blines').innerHTML=lines.slice(0,shown).join('\n')+(extra?'\n'+extra:'')}
  function step(){if(!booting)return;
   if(shown<lines.length){shown++;paint();timer=setTimeout(step,fast?25:110);return}
   var evs=ev.slice(pos);pos=ev.length;
   evs.forEach(function(e){if(e.state==='start'){running=e.station;frame=0}
    else if(e.state==='done'){lines.push(stationLine(e,e.t-t0));running=null}
    else if(e.state==='end'){var ok=ev.filter(function(x){return x.state==='done'&&x.go}).length,bad=ev.filter(function(x){return x.state==='done'&&!x.go}).length;
     lines.push('');lines.push(bad?'<span class="r">  '+bad+' NO-GO</span> · <span class="g">'+ok+' GO</span> · the sit rep carries the details'
      :'<span class="g">  Reached target </span><span class="bv">The Command</span><span class="g">.  ALL GO ('+ok+')</span>');ended=true}});
   if(shown<lines.length){timer=setTimeout(step,fast?25:60);return}
   if(ended){paint();timer=setTimeout(skip,fast?900:2500);return}
   frame++;paint(running?stamp((Date.now()/1000)-t0)+' <span class="y">[  '+'|/-\\'[frame%4]+'   ]</span> <span class="w">'+esc(pad(running,10))+'</span> <span class="d">'+Array(Math.min(frame,30)+1).join('.')+'</span>':'');
   timer=setTimeout(function(){fetch('/boot.json').then(function(r){return r.json()}).then(function(n){ev=n.events;step()}).catch(step)},250)}
  if(!ev.length){lines.push('<span class="d">  no launch on record · the workspace is ready</span>');ended=true}
  step()}).catch(skip)}
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
            return self._send(200, PAGE, "text/html; charset=utf-8")
        if path in ("/favicon.svg", "/favicon.ico") and os.path.isfile(MARK):   # the BoldVenture bunny bandit (Chief 10/18)
            with open(MARK, "rb") as fh:
                return self._send(200, fh.read(), "image/svg+xml")
        if path == "/panes.json":
            return self._send(200, json.dumps({"panes": PANES}), "application/json; charset=utf-8")
        if path == "/glasses.json":
            return self._send(200, json.dumps({"glasses": read_glasses()}, ensure_ascii=False), "application/json; charset=utf-8")
        if path == "/boot.json":
            return self._send(200, json.dumps(read_boot(), ensure_ascii=False), "application/json; charset=utf-8")
        if path == "/status.json":
            return self._send(200, json.dumps({"pull": read_status()}), "application/json; charset=utf-8")
        if path.startswith("/local/"):
            f = LOCAL.get(path[7:])
            if f and os.path.isfile(f):
                return self._send(200, page_bytes(f), "text/html; charset=utf-8")
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
                    return self._send(200, page_bytes(f), ctype)
        self._send(404, "not found", "text/plain")

    def do_POST(self):
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
    if "--status" in sys.argv:
        print(write_status())
        sys.exit(0)
    if "--open" in sys.argv:
        print(open_window())
        sys.exit(0)
    threading.Thread(target=glasses_loop, daemon=True).start()
    S(("127.0.0.1", PORT), H).serve_forever()
