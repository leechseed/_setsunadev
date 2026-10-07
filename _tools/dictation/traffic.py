"""
traffic.py — the Traffic Panel (BOLO 115). Parsing + page for JUDY's console.

    /traffic       the page
    /traffic.json  ?scope=session|3d  &ids=<comma ids of pinned replies>

Reuses reader.py's project_dir / newest_transcript / parse. A "turn" starts at a genuine
user message (reader.parse -> "user") and holds every assistant text block until the next one.
"""

import glob
import io
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)

SAY = re.compile(r"<!--\s*say:\s*(.*?)\s*-->", re.S | re.I)
BOLO_RE = re.compile(r"\bBOLO\s*#?(\d{1,3})\b|\bgo\s+(\d{2,3})\b", re.I)
WAIT_RE = re.compile(r"on go\b|\bgo 1\d\d\b|Rec:|\?|waits on you", re.I)
DONE_RE = re.compile(r"\bbuilt\b|\bdone\b|\bpublished\b|\blive\b", re.I)
_cache = {}          # path -> (mtime, size, turns)
_bolo = {"m": None, "titles": {}}


def _reader():
    import reader  # imported lazily: it pulls speak/squelch
    return reader


def _ts(d):
    return d.get("timestamp") or ""


def parse_file(path):
    """-> list of turns {id, ts, user, text} for one transcript, cached by mtime+size."""
    try:
        st = os.stat(path)
    except OSError:
        return []
    key = (st.st_mtime, st.st_size)
    hit = _cache.get(path)
    if hit and hit[0] == key:
        return hit[1]
    rd = _reader()
    turns, cur = [], None
    with io.open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            r = rd.parse(line)
            if not r:
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            if r[0] == "user":
                cur = {"id": d.get("uuid") or _ts(d), "ts": _ts(d), "user": r[1], "parts": []}
                turns.append(cur)
            else:
                if cur is None:
                    cur = {"id": d.get("uuid") or _ts(d), "ts": _ts(d), "user": "", "parts": []}
                    turns.append(cur)
                cur["parts"].append(r[1])
    for t in turns:
        t["text"] = "\n\n".join(t.pop("parts"))
    _cache[path] = (key, turns)
    if len(_cache) > 40:
        _cache.pop(next(iter(_cache)))
    return turns


def bolo_titles():
    p = os.path.join(ROOT, "BOLO.md")
    try:
        m = os.path.getmtime(p)
    except OSError:
        return {}
    if _bolo["m"] == m:
        return _bolo["titles"]
    t = {}
    try:
        for line in io.open(p, encoding="utf-8", errors="replace"):
            mm = re.match(r"\|\s*(\d+)\s*\|\s*\*\*(.+?)\*\*", line)
            if mm:
                t[int(mm.group(1))] = mm.group(2).strip()[:60]
    except Exception:
        pass
    _bolo.update(m=m, titles=t)
    return t


def mentions(text):
    return {int(a or b) for a, b in BOLO_RE.findall(text or "")}


def lanes_for(turns, cap=20):
    titles = bolo_titles()
    ticks, last_reply = {}, {}
    for i, t in enumerate(turns):
        for n in mentions(t["user"]) | mentions(t["text"]):
            ticks.setdefault(n, []).append(i)
        for n in mentions(t["text"]):
            last_reply[n] = t["text"]
    out = []
    for n, tk in ticks.items():
        txt = last_reply.get(n, "")
        color = "gray"
        if txt:
            win = ""
            for m in BOLO_RE.finditer(txt):
                if int(m.group(1) or m.group(2)) == n:
                    win += txt[max(0, m.start() - 160): m.end() + 160] + "\n"
            if WAIT_RE.search(win):
                color = "orange"
            elif DONE_RE.search(win):
                color = "green"
        out.append({"n": n, "title": titles.get(n, ""), "ticks": tk, "color": color})
    out.sort(key=lambda l: l["ticks"][-1], reverse=True)
    return out[:cap]


def split_say(text):
    m = SAY.search(text)
    say = m.group(1).strip() if m else ""
    body = SAY.sub("", text, count=1).lstrip("\n") if m else text
    return say, body


def open_calls(body):
    out, seen, fence = [], set(), False
    for ln in body.splitlines():
        if ln.strip().startswith("```"):
            fence = not fence
            continue
        s = ln.strip()
        if fence or not s:
            continue
        if s.endswith("?") or "Rec:" in s:
            c = re.sub(r"^[-*+>#\s]+|^\d+\.\s+", "", s)
            c = re.sub(r"[*_`]", "", c).strip()
            if c and c not in seen:
                seen.add(c)
                out.append(c[:300])
    return out


def reply(t):
    say, body = split_say(t["text"])
    return {"id": t["id"], "ts": t["ts"], "say": say, "text": body, "calls": open_calls(body)}


def transcripts(scope):
    rd = _reader()
    folder = rd.project_dir()
    if scope == "3d":
        cut = time.time() - 72 * 3600
        fs = [f for f in glob.glob(os.path.join(folder, "*.jsonl")) if os.path.getmtime(f) >= cut]
        return sorted(fs, key=os.path.getmtime)
    p = rd.newest_transcript(folder)
    return [p] if p else []


def build_payload(scope="session", ids=()):
    cur = transcripts("session")
    sess = parse_file(cur[0]) if cur else []
    withtext = [t for t in sess if t["text"].strip()]
    last5 = withtext[-5:]
    want = {t["id"] for t in last5}
    pinned = [t for t in withtext if t["id"] in set(ids) and t["id"] not in want]
    if scope == "3d":
        turns = []
        for f in transcripts("3d"):
            turns += parse_file(f)
        turns.sort(key=lambda t: t["ts"])
    else:
        turns = sess
    return {
        "updated": time.strftime("%H:%M:%S"),
        "scope": scope,
        "turns": len(turns),
        "replies": [reply(t) for t in reversed(last5)],
        "pinned": [reply(t) for t in pinned],
        "lanes": lanes_for(turns),
    }


PAGE = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Traffic</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Atkinson+Hyperlegible:wght@400;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root{--bg:#121110;--panel:#1B1A18;--line:#34312C;--ink:#ECE7DF;--ink2:#B7B0A5;--ink3:#7F786E;--acc:#FF5A1F;--green:#5FBF8A;
--disp:"Barlow Condensed","Arial Narrow",sans-serif;--body:"Atkinson Hyperlegible",system-ui,sans-serif;--mono:"IBM Plex Mono",Consolas,monospace}
*{box-sizing:border-box}html,body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 var(--body)}
header{height:44px;display:flex;align-items:center;gap:14px;padding:0 16px;border-bottom:1px solid var(--line);background:var(--panel);position:sticky;top:0;z-index:5}
h1{font:800 22px var(--disp);letter-spacing:.08em;margin:0;text-transform:uppercase}h1 b{color:var(--acc)}
.chip{font:500 12px var(--mono);border:1px solid var(--line);border-radius:99px;padding:2px 10px;color:var(--ink2)}
.sp{flex:1}.upd{font:400 12px var(--mono);color:var(--ink3)}header a{color:var(--ink2);font-size:13px;text-decoration:none}
main{display:grid;grid-template-columns:minmax(0,3fr) minmax(0,2fr);gap:16px;padding:16px;max-width:1500px;margin:0 auto}
@media(max-width:900px){main{grid-template-columns:1fr}}
.card{background:var(--panel);border:1px solid var(--line);border-radius:8px;min-width:0}
.tabs{display:flex;flex-wrap:wrap;gap:4px;padding:8px 8px 0;border-bottom:1px solid var(--line)}
.tab{font:500 12px var(--mono);color:var(--ink2);background:none;border:1px solid transparent;border-bottom:0;border-radius:6px 6px 0 0;padding:6px 10px;cursor:pointer;max-width:210px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.tab.on{background:var(--bg);border-color:var(--line);color:var(--ink)}.tab.pin::before{content:"\25CF ";color:var(--acc)}
.bar{display:flex;align-items:center;gap:10px;padding:10px 16px 0}
.btn{font:500 12px var(--mono);color:var(--ink2);background:none;border:1px solid var(--line);border-radius:6px;padding:4px 10px;cursor:pointer}
.btn:hover,.btn.on{border-color:var(--acc);color:var(--ink)}
.say{font-style:italic;color:var(--ink3);font-size:13px;margin:0}
.calls{margin:12px 16px 0;border:1px solid var(--acc);background:rgba(255,90,31,.08);border-radius:6px;padding:8px 12px}
.calls h3{font:700 13px var(--disp);letter-spacing:.1em;text-transform:uppercase;color:var(--acc);margin:0 0 4px}
.calls ul{margin:0;padding-left:18px;font-size:14px}
.md{padding:8px 16px 18px;overflow-wrap:anywhere}
.md h1,.md h2,.md h3,.md h4{font-family:var(--disp);letter-spacing:.04em;margin:1em 0 .3em;line-height:1.15}
.md h1{font-size:26px}.md h2{font-size:22px}.md h3{font-size:18px}.md h4{font-size:16px;color:var(--ink2)}
.md p{margin:.5em 0}.md code{font:400 .88em var(--mono);background:var(--bg);border:1px solid var(--line);border-radius:4px;padding:1px 5px}
.md pre{background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:10px;overflow:auto}.md pre code{border:0;padding:0}
.md a{color:var(--acc)}.md table{border-collapse:collapse;display:block;overflow:auto;font-size:14px}
.md th,.md td{border:1px solid var(--line);padding:4px 8px;text-align:left}.md th{background:var(--bg)}
.md ul,.md ol{padding-left:22px;margin:.4em 0}
.net{padding:12px}.net h2{font:700 14px var(--disp);letter-spacing:.12em;text-transform:uppercase;color:var(--ink2);margin:0}
.nh{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px}
.leg{font:400 11px var(--mono);color:var(--ink3);margin-top:6px}.leg i{display:inline-block;width:9px;height:9px;border-radius:2px;margin:0 4px 0 10px}
.cl{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:6px 0}.cl .t{flex:1 1 100%;font-size:14px}.cl input{flex:1 1 160px;min-width:0;background:var(--bg);color:var(--ink);border:1px solid var(--line);border-radius:6px;padding:4px 8px;font:400 13px var(--body)}.btn.ok{border-color:var(--green);color:var(--green)}
.empty{color:var(--ink3);padding:16px}
</style></head><body>
<header><h1>Traffic <b>Panel</b></h1><span class="chip">BOLO 115</span><span class="sp"></span><button class="btn" id="allrec">Take all recs</button><span class="upd" id="upd">--</span><a href="/">console</a><a href="/faces">faces</a></header>
<main>
<section class="card"><div class="tabs" id="tabs"></div><div id="view"><div class="empty">loading</div></div></section>
<section class="card net"><div class="nh"><h2>Net</h2><span><button class="btn on" id="s1">This session</button> <button class="btn" id="s3">3 days</button></span></div><div id="net"></div>
<div class="leg"><i style="background:#FF5A1F"></i>waits on Chief<i style="background:#5FBF8A"></i>done<i style="background:#7F786E"></i>waits on JUDY</div></section>
</main>
<script>
var scope="session",active=null,data=null,PK="traffic.pins";
function pins(){try{return JSON.parse(localStorage.getItem(PK)||"[]")}catch(e){return[]}}
function setPins(a){try{localStorage.setItem(PK,JSON.stringify(a))}catch(e){}}
function esc(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;")}
function inl(s){var codes=[];
 s=esc(s).replace(/`([^`]+)`/g,function(_,c){codes.push(c);return "\u0001"+(codes.length-1)+"\u0001"});
 s=s.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g,function(_,t,u){return /^(https?:|\/|\.|#|[\w-]+\/)/i.test(u)&&!/^javascript:/i.test(u)?'<a href="'+u+'" target="_blank" rel="noopener">'+t+'</a>':t});
 s=s.replace(/\*\*([^*]+)\*\*/g,"<strong>$1</strong>").replace(/(^|[^\w*])\*([^*\s][^*]*)\*(?!\w)/g,"$1<em>$2</em>").replace(/(^|[^\w])_([^_\s][^_]*)_(?!\w)/g,"$1<em>$2</em>");
 return s.replace(/\u0001(\d+)\u0001/g,function(_,i){return "<code>"+codes[+i]+"</code>"})}
function cells(l){return l.trim().replace(/^\||\|$/g,"").split("|").map(function(c){return c.trim()})}
function md(src){var L=src.replace(/\r/g,"").split("\n"),o=[],i=0,m;
 while(i<L.length){var l=L[i];
  if(/^\s*```/.test(l)){var b=[];i++;while(i<L.length&&!/^\s*```/.test(L[i]))b.push(L[i++]);i++;o.push("<pre><code>"+esc(b.join("\n"))+"</code></pre>");continue}
  if(!l.trim()){i++;continue}
  if((m=l.match(/^(#{1,4})\s+(.*)/))){o.push("<h"+m[1].length+">"+inl(m[2])+"</h"+m[1].length+">");i++;continue}
  if(/^\s*\|/.test(l)&&i+1<L.length&&/^\s*\|?[\s:|-]+\|[\s:|-]*$/.test(L[i+1])){var h=cells(l);i+=2;var t="<table><tr>"+h.map(function(c){return"<th>"+inl(c)+"</th>"}).join("")+"</tr>";
   while(i<L.length&&/^\s*\|/.test(L[i]))t+="<tr>"+cells(L[i++]).map(function(c){return"<td>"+inl(c)+"</td>"}).join("")+"</tr>";o.push(t+"</table>");continue}
  if(/^\s*([-*+]|\d+\.)\s+/.test(l)){var ord=/^\s*\d+\./.test(l),it=[];
   while(i<L.length&&/^\s*([-*+]|\d+\.)\s+/.test(L[i]))it.push("<li>"+inl(L[i++].replace(/^\s*([-*+]|\d+\.)\s+/,""))+"</li>");
   o.push((ord?"<ol>":"<ul>")+it.join("")+(ord?"</ol>":"</ul>"));continue}
  var p=[];while(i<L.length&&L[i].trim()&&!/^\s*(```|#{1,4}\s|\||([-*+]|\d+\.)\s)/.test(L[i]))p.push(L[i++]);
  if(!p.length){p.push(L[i++])}o.push("<p>"+p.map(inl).join("<br>")+"</p>")}
 return o.join("\n")}
function hm(ts){try{var d=new Date(ts);return ("0"+d.getHours()).slice(-2)+":"+("0"+d.getMinutes()).slice(-2)}catch(e){return"--:--"}}
function label(r){var t=r.text,m=t.match(/^#{1,4}\s+(.+)$/m)||t.match(/\*\*([^*]+)\*\*/)||[0,t.replace(/[#*`|]/g," ").trim()];
 var w=m[1].replace(/[*_`\[\]]/g,"").trim().split(/\s+/).slice(0,4).join(" ");return hm(r.ts)+" "+w}
function tabsList(){var all=[],seen={};(data.replies||[]).forEach(function(r){all.push(r);seen[r.id]=1});
 var P=pins();(data.pinned||[]).forEach(function(r){if(!seen[r.id]){all.push(r);seen[r.id]=1}});return all}
var lastSig="";
function render(){var all=tabsList(),P=pins(),sig=JSON.stringify([all,P,active]);
 if(sig===lastSig)return;lastSig=sig;
 var ae=document.activeElement,keep=null;if(ae&&ae.tagName==="INPUT"&&ae.dataset.k!==undefined)keep={k:ae.dataset.k,v:ae.value,s:ae.selectionStart,e:ae.selectionEnd};
 var vals={};document.querySelectorAll("#view input[data-k]").forEach(function(i){if(i.value)vals[i.dataset.k]=i.value});
 draw(all,P);
 document.querySelectorAll("#view input[data-k]").forEach(function(i){if(vals[i.dataset.k])i.value=vals[i.dataset.k]});
 if(keep){var n=document.querySelector('#view input[data-k="'+keep.k+'"]');if(n){n.value=keep.v;n.focus();try{n.setSelectionRange(keep.s,keep.e)}catch(e){}}}}
function draw(all,P){if(!all.length){document.getElementById("view").innerHTML='<div class="empty">no replies yet</div>';document.getElementById("tabs").innerHTML="";return}
 if(!all.some(function(r){return r.id===active}))active=all[0].id;
 document.getElementById("tabs").innerHTML=all.map(function(r){return '<button class="tab'+(r.id===active?" on":"")+(P.indexOf(r.id)>=0?" pin":"")+'" data-id="'+esc(r.id)+'" title="'+esc(label(r))+'">'+esc(label(r))+"</button>"}).join("");
 var r=all.filter(function(x){return x.id===active})[0],pinned=P.indexOf(r.id)>=0;
 var h='<div class="bar"><button class="btn'+(pinned?" on":"")+'" id="pin">'+(pinned?"Unpin":"Pin")+'</button>'+(r.say?'<p class="say">spoken line: '+esc(r.say)+"</p>":"")+"</div>";
 if(r.calls.length)h+='<div class="calls"><h3>Open calls</h3>'+r.calls.map(function(c,k){return '<div class="cl"><span class="t">'+esc(c)+'</span>'+(c.indexOf("Rec:")>=0?'<button class="btn" data-act="rec" data-k="'+k+'">Take rec</button>':"")+'<input data-k="'+k+'" placeholder="answer"><button class="btn" data-act="ans" data-k="'+k+'">Send</button></div>'}).join("")+"</div>";
 document.getElementById("view").innerHTML=h+'<div class="md">'+md(r.text)+"</div>"}
document.getElementById("tabs").onclick=function(e){var b=e.target.closest(".tab");if(b){active=b.dataset.id;render()}};
var busy=0;
function send(text,btn){if(Date.now()-busy<1200)return;busy=Date.now();var o=btn.textContent;
 fetch("/traffic/send",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({text:text})}).then(function(r){return r.json()}).then(function(d){btn.textContent=d.ok?"sent":"failed";if(d.ok)btn.classList.add("ok");setTimeout(function(){btn.textContent=o;btn.classList.remove("ok")},1500)}).catch(function(){btn.textContent="failed";setTimeout(function(){btn.textContent=o},1500)})}
function callText(k){var r=tabsList().filter(function(x){return x.id===active})[0];return r&&r.calls[k]||""}
document.getElementById("allrec").onclick=function(){send("take all recs",this)};
document.getElementById("view").onclick=function(e){var b=e.target.closest("button[data-act]");
 if(b){var k=+b.dataset.k,c=callText(k);if(b.dataset.act==="rec")send("rec: "+c.slice(0,140),b);
  else{var i=document.querySelector('#view input[data-k="'+k+'"]'),v=i&&i.value.trim();if(!v)return;send("answer: "+c.slice(0,80)+" → "+v,b);i.value=""}return}
 if(e.target.id!=="pin")return;var P=pins(),i=P.indexOf(active);
 if(i>=0)P.splice(i,1);else{if(P.length>=3){alert("Max 3 pins");return}P.push(active)}setPins(P);poll()};
function color(c){return c==="orange"?"#FF5A1F":c==="green"?"#5FBF8A":"#7F786E"}
function net(){var Ls=data.lanes||[],el=document.getElementById("net");if(!Ls.length){el.innerHTML='<div class="empty">no BOLO traffic</div>';return}
 var LW=170,RH=24,W=560,PW=W-LW-12,N=Math.max(data.turns-1,1),H=Ls.length*RH+8,s='<svg viewBox="0 0 '+W+" "+H+'" width="100%" role="img" aria-label="Net chart">';
 Ls.forEach(function(l,k){var y=k*RH+4,c=color(l.color),x0=LW+l.ticks[0]/N*PW,x1=LW+l.ticks[l.ticks.length-1]/N*PW;
  var t=("BOLO "+l.n+(l.title?" "+l.title:""));if(t.length>26)t=t.slice(0,25)+"…";
  s+='<line x1="'+LW+'" x2="'+(LW+PW)+'" y1="'+(y+12)+'" y2="'+(y+12)+'" stroke="#34312C"/>';
  s+='<line x1="'+x0+'" x2="'+x1+'" y1="'+(y+12)+'" y2="'+(y+12)+'" stroke="'+c+'" stroke-width="2" opacity=".5"/>';
  s+='<text x="0" y="'+(y+16)+'" fill="'+(l.color==="gray"?"#B7B0A5":c)+'" font-family="IBM Plex Mono,monospace" font-size="11"><title>'+esc("BOLO "+l.n+" "+l.title)+"</title>"+esc(t)+"</text>";
  l.ticks.forEach(function(i){s+='<rect x="'+(LW+i/N*PW-1.5)+'" y="'+(y+5)+'" width="3" height="14" fill="'+c+'"/>'})});
 el.innerHTML=s+"</svg>"}
function poll(){var q="/traffic.json?scope="+scope+"&ids="+encodeURIComponent(pins().join(","));
 fetch(q).then(function(r){return r.json()}).then(function(d){data=d;document.getElementById("upd").textContent="updated "+d.updated;render();net()}).catch(function(){document.getElementById("upd").textContent="offline"})}
function sc(s){scope=s;document.getElementById("s1").className="btn"+(s==="session"?" on":"");document.getElementById("s3").className="btn"+(s==="3d"?" on":"");poll()}
document.getElementById("s1").onclick=function(){sc("session")};document.getElementById("s3").onclick=function(){sc("3d")};
poll();setInterval(poll,5000);
</script></body></html>
'''
