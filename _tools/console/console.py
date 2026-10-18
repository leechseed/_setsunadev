# -*- coding: utf-8 -*-
"""The Console v1 (BOLO 141/142): one app window, console-styled frame, our pages in one iframe pane.
Serves 127.0.0.1:8795 only.  /  the frame · /panes.json · /local/<name> (whitelist) · /status.json · POST /cmd -> cmd.log
Usage: python console.py [--status]   (--status runs pull_queue.py report and caches status.json)
"""
import os, sys, json, time, subprocess, http.server, socketserver

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
PORT = 8795
CMDLOG = os.path.join(HERE, "cmd.log")
STATUS = os.path.join(HERE, "status.json")
PQ = os.path.join(ROOT, "_PRIVATE", "taxonomy_engine", "pull_queue.py")

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
PANES = [
    {"id": "desk", "title": "Desk", "kind": "frame", "url": "/local/desk"},
    {"id": "sitrep", "title": "Sit rep", "kind": "frame", "url": "/local/sitrep"},
    {"id": "pullqueue", "title": "Pull Queue", "kind": "frame", "url": "/local/pullqueue"},
    {"id": "roster", "title": "Roster", "kind": "frame", "url": "/local/roster"},
    {"id": "armory", "title": "Armory", "kind": "frame", "url": "/local/armory"},
    {"id": "traffic", "title": "Traffic", "kind": "frame", "url": "http://127.0.0.1:8787/traffic"},
    {"id": "faces", "title": "Faces", "kind": "frame", "url": "http://127.0.0.1:8787/faces"},
    {"id": "darkroom", "title": "DARKROOM", "kind": "frame", "url": "http://127.0.0.1:8484/"},
    {"id": "stash", "title": "Stash", "kind": "frame", "url": "http://127.0.0.1:9999/"},
    {"id": "fabula", "title": "Fabula graph", "kind": "frame", "url": "/local/fabula-graph"},
    {"id": "stash-erd", "title": "Stash ERD", "kind": "frame", "url": "/local/stash-erd"},
    {"id": "zotero-erd", "title": "Zotero ERD", "kind": "frame", "url": "/local/zotero-erd"},
    {"id": "sitrep-web", "title": "Sit rep (web)", "kind": "tab",
     "url": "https://claude.ai/code/artifact/aebe5f9c-9f2c-4cb8-abbf-714a0a6ea28a"},
    {"id": "soi", "title": "SOI", "kind": "tab",
     "url": "https://claude.ai/code/artifact/4c2fc9c7-e0d2-4626-8142-9740ff8ee0e5"},
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


PAGE = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Console</title>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
:root{--bg:#050608;--fg:#c6cbc8;--dim:#5f6160;--acc:#FF5A1F;--ok:#72c79b;--cy:#79dfff;--vi:#e6a5fb;--am:#ffcf73}
*{box-sizing:border-box}
html,body{margin:0;height:100%;background:var(--bg);color:var(--fg);font:13px/1.45 "IBM Plex Mono",Consolas,monospace}
body{display:grid;grid-template-rows:auto 1fr auto auto;padding:8px 16px;gap:6px;height:100vh;overflow:hidden}
.top{display:flex;justify-content:space-between;color:var(--dim);white-space:pre;overflow:hidden}
.top b{color:var(--acc)}
main{display:grid;grid-template-columns:230px 1fr;gap:8px;min-height:0}
.box{position:relative;border:1px solid var(--dim);padding:14px 10px 8px;overflow:auto;min-height:0}
.box::before{content:"\2524 " attr(data-t) " \251C";position:absolute;top:-.8em;left:10px;background:var(--bg);padding:0 4px;color:var(--dim)}
.box.on{border-color:var(--acc);box-shadow:0 0 0 1px var(--acc) inset}.box.on::before{color:var(--acc)}
#main{padding:0;overflow:hidden;display:flex}
iframe{flex:1;border:0;width:100%;height:100%;background:#fff}
#tabbox{flex:1;display:none;align-items:center;justify-content:center;flex-direction:column;gap:12px}
#tabbox button{font:inherit;color:var(--acc);background:none;border:1px solid var(--acc);padding:6px 14px;cursor:pointer}
#rail div{padding:1px 4px;cursor:pointer;white-space:nowrap}
#rail div.sel{color:var(--acc)}#rail div:hover{background:#10151b}#rail .k{color:var(--dim)}#rail .t{color:var(--cy)}
.status{display:flex;justify-content:space-between;gap:12px;background:#10151b;padding:2px 8px}
.status b{color:var(--acc);font-weight:600}
.cmd{display:flex;gap:8px;border-top:1px solid var(--dim);padding-top:4px}
.cmd span{color:var(--acc)}
.cmd input{flex:1;background:none;border:0;outline:0;color:var(--fg);font:inherit;caret-color:var(--acc)}
#flt{width:100%;background:none;border:0;border-bottom:1px solid var(--dim);outline:0;color:var(--fg);font:inherit;margin-bottom:6px}
.d{color:var(--dim)}
</style></head><body>
<div class="top"><span><b>&#9670; THE CONSOLE</b>  the Command &middot; Chief</span><span id="clk"></span></div>
<main>
 <section class="box on" data-t="PANES" id="railbox"><input id="flt" placeholder="/ filter" autocomplete="off"><div id="rail"></div></section>
 <section class="box" data-t="MAIN" id="main"><iframe id="fr" title="pane"></iframe>
  <div id="tabbox"><div id="tabmsg" class="d"></div><button id="tabbtn">open in a tab &#8599;</button></div></section>
</main>
<div class="status"><span><b id="mode">NORMAL</b>  pane <b id="pn">-</b></span><span id="st" class="d"></span><span class="d">1-9 pane  /  filter  :  command  Esc leave</span></div>
<label class="cmd"><span id="pr">&gt;</span><input id="in" placeholder="press : for a command, / to filter" autocomplete="off"></label>
<script>
(function(){
var panes=[],cur=-1,fr=document.getElementById('fr'),tb=document.getElementById('tabbox'),rail=document.getElementById('rail'),
 flt=document.getElementById('flt'),inp=document.getElementById('in'),st=document.getElementById('st'),pn=document.getElementById('pn');
function draw(){var q=flt.value.toLowerCase();rail.innerHTML='';panes.forEach(function(p,i){
 if(q&&p.title.toLowerCase().indexOf(q)<0)return;var d=document.createElement('div');d.className=i===cur?'sel':'';
 d.innerHTML='<span class="k">'+(i<9?(i+1):'-')+'</span> '+p.title+(p.kind==='tab'?' <span class="t">&#8599;</span>':'');
 d.onclick=function(){pick(i)};rail.appendChild(d)})}
function pick(i){if(i<0||i>=panes.length)return;cur=i;var p=panes[i];pn.textContent=(i+1)+'/'+panes.length;
 if(p.kind==='tab'){fr.style.display='none';fr.removeAttribute('src');tb.style.display='flex';
  document.getElementById('tabmsg').textContent=p.title+' refuses frames; it opens in a tab.';
  document.getElementById('tabbtn').onclick=function(){window.open(p.url,'_blank')}}
 else{tb.style.display='none';fr.style.display='block';fr.src=p.url}
 document.getElementById('main').setAttribute('data-t',p.title.toUpperCase());draw()}
function clk(){var d=new Date(),h=d.getHours()%12||12,m=('0'+d.getMinutes()).slice(-2);
 document.getElementById('clk').textContent=(d.getMonth()+1)+'/'+d.getDate()+'  '+h+':'+m+' '+(d.getHours()<12?'AM':'PM')}
function stat(){fetch('/status.json').then(function(r){return r.json()}).then(function(j){st.textContent=j.pull}).catch(function(){st.textContent='no pull status'})}
fetch('/panes.json').then(function(r){return r.json()}).then(function(j){panes=j.panes;draw();pick(0)});
clk();stat();setInterval(clk,15000);setInterval(stat,60000);
flt.oninput=draw;
flt.addEventListener('keydown',function(e){if(e.key==='Enter'){var q=flt.value.toLowerCase();for(var i=0;i<panes.length;i++){if(panes[i].title.toLowerCase().indexOf(q)>=0){pick(i);break}}flt.blur()}else if(e.key==='Escape'){flt.value='';draw();flt.blur()}});
inp.addEventListener('keydown',function(e){if(e.key==='Escape'){inp.value='';inp.blur();return}
 if(e.key==='Enter'&&inp.value.trim()){var line=inp.value.trim();inp.value='';
  fetch('/cmd',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({line:line})})
  .then(function(){inp.placeholder='logged; JUDY wiring next'}).catch(function(){inp.placeholder='command failed'})}});
document.addEventListener('keydown',function(e){var t=e.target;if(t===inp||t===flt)return;
 if(e.key>='1'&&e.key<='9'){pick(+e.key-1)}
 else if(e.key==='/'){e.preventDefault();document.getElementById('mode').textContent='FILTER';flt.focus()}
 else if(e.key===':'){e.preventDefault();inp.focus()}});
flt.addEventListener('blur',function(){document.getElementById('mode').textContent='NORMAL'});
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
        path = self.path.split("?")[0]
        if path == "/":
            return self._send(200, PAGE, "text/html; charset=utf-8")
        if path == "/panes.json":
            return self._send(200, json.dumps({"panes": PANES}), "application/json; charset=utf-8")
        if path == "/status.json":
            return self._send(200, json.dumps({"pull": read_status()}), "application/json; charset=utf-8")
        if path.startswith("/local/"):
            f = LOCAL.get(path[7:])
            if f and os.path.isfile(f):
                with open(f, "rb") as fh:
                    return self._send(200, fh.read(), "text/html; charset=utf-8")
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


if __name__ == "__main__":
    if "--status" in sys.argv:
        print(write_status())
        sys.exit(0)
    S(("127.0.0.1", PORT), H).serve_forever()
