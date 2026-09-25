"""
stashgrade.py - the grading pass (BOLO 28, Chief 9/24: "I just imported a whole bunch of new videos into Stash ...
a playlist where I can enter tags and ratings, five star ... maybe 30 minutes at a time").

Queues about N minutes of the UNRATED scenes, newest imports first, in VLC (windowed, VLC's web remote on), and serves
a grading panel on http://127.0.0.1:8485/ that follows whatever VLC is playing - skip in VLC and the panel follows.
Stars and tags write straight to Stash (GraphQL on :9999). New tag names are created on the spot.

    python stashgrade.py            # 30 minutes
    python stashgrade.py 45         # 45 minutes
    python stashgrade.py 30 --full  # VLC fullscreen (the panel on the other screen)
    python stashgrade.py --panel    # the panel only, over a VLC this script already started

Panel keys: 1-5 stars (0 clears) · N next · P previous · Space pause · T the tag box · Enter adds the tag.
Run it from the Bash tool in the background; Ctrl+C or closing the terminal stops the panel, VLC keeps playing.
"""
import base64
import io
import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stashplay import FIELDS, VLC, gql, label, stop, up  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
PANEL_PORT, VLC_PORT, VLC_PASS = 8485, 8486, "grade"
STATE = os.path.join(HERE, "_stashgrade_queue.json")
M3U = os.path.join(HERE, "_stashgrade_queue.m3u")
SKIP_TAGS = ("dupe:cut",)
GFIELDS = FIELDS.replace("tags { name }", "tags { id name }") + " created_at"


def norm(p):
    return os.path.normcase(os.path.normpath(p or ""))


def skip_ids():
    ids = []
    for name in SKIP_TAGS:
        t = gql('query($n:String!){ findTags(tag_filter:{name:{value:$n, modifier:EQUALS}}) { tags { id } } }', {"n": name})["findTags"]["tags"]
        ids += [x["id"] for x in t]
    return ids


def build(minutes):
    """Unrated scenes, newest import first, until the set reaches about `minutes`."""
    f = {"rating100": {"value": 0, "modifier": "IS_NULL"}}
    ids = skip_ids()
    if ids:
        f["tags"] = {"value": ids, "modifier": "EXCLUDES"}
    d = gql('query($f:SceneFilterType){ findScenes(scene_filter:$f, filter:{per_page:300, sort:"created_at", direction:DESC}) { count scenes { %s } } }' % GFIELDS, {"f": f})["findScenes"]
    want, picked, total = minutes * 60, [], 0.0
    for s in d["scenes"]:
        if not s.get("files"):
            continue
        dur = s["files"][0].get("duration") or 0
        if picked and total + dur > want * 1.25:   # would overshoot by more than a quarter: try a shorter one
            continue
        picked.append(s)
        total += dur
        if total >= want:
            break
    return picked, total, d["count"]


def launch_vlc(picked, full):
    io.open(M3U, "w", encoding="utf-8").write("#EXTM3U\n" + "".join(
        "#EXTINF:%d,%s\n%s\n" % (s["files"][0]["duration"] or 0, label(s), s["files"][0]["path"]) for s in picked))
    stop()
    args = [VLC, "--extraintf=http", "--http-host=127.0.0.1", "--http-port=%d" % VLC_PORT, "--http-password=" + VLC_PASS,
            "--no-video-title-show", "--no-random", "--no-loop", "--no-repeat", M3U]
    if full:
        args.insert(1, "--fullscreen")
    subprocess.Popen(args, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# ---- VLC's web remote ----
AUTH = "Basic " + base64.b64encode((":" + VLC_PASS).encode()).decode()


def vlc(path, **q):
    url = "http://127.0.0.1:%d/requests/%s" % (VLC_PORT, path) + ("?" + urllib.parse.urlencode(q) if q else "")
    r = urllib.request.urlopen(urllib.request.Request(url, headers={"Authorization": AUTH}), timeout=2)
    return json.load(r)


def vlc_now():
    """(path of the playing item or None, status dict) - the panel's only link to VLC."""
    st = vlc("status.json")
    cur = st.get("currentplid")
    if cur is None or cur < 0:
        return None, st

    def walk(n):
        if n.get("type") == "leaf" and str(n.get("id")) == str(cur):
            return n.get("uri")
        for c in n.get("children") or []:
            u = walk(c)
            if u:
                return u
    uri = walk(vlc("playlist.json"))
    if not uri:
        return None, st
    p = urllib.parse.unquote(urllib.parse.urlparse(uri).path)
    if len(p) > 2 and p[0] == "/" and p[2] == ":":
        p = p[1:]
    return p, st


# ---- Stash writes ----
def scene(sid):
    return gql('query($id:ID!){ findScene(id:$id) { %s } }' % GFIELDS, {"id": sid})["findScene"]


def set_rating(sid, stars):
    gql('mutation($i:SceneUpdateInput!){ sceneUpdate(input:$i) { id } }',
        {"i": {"id": sid, "rating100": int(stars) * 20 if int(stars) else None}})


def tag_id(name):
    t = gql('query($n:String!){ findTags(tag_filter:{name:{value:$n, modifier:EQUALS}}) { tags { id } } }', {"n": name})["findTags"]["tags"]
    if t:
        return t[0]["id"]
    return gql('mutation($n:String!){ tagCreate(input:{name:$n}) { id } }', {"n": name})["tagCreate"]["id"]


def set_tags(sid, ids):
    gql('mutation($i:SceneUpdateInput!){ sceneUpdate(input:$i) { id } }', {"i": {"id": sid, "tag_ids": sorted(set(ids))}})


def tag_search(q):
    return [t["name"] for t in gql('query($q:String){ findTags(filter:{q:$q, per_page:12, sort:"scenes_count", direction:DESC}) { tags { name } } }', {"q": q})["findTags"]["tags"]]


# ---- the panel ----
def queue_state():
    return json.load(io.open(STATE, encoding="utf-8"))


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send(self, obj, code=200, ctype="application/json"):
        body = obj if isinstance(obj, bytes) else json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        try:
            if u.path == "/":
                return self.send(PAGE.encode("utf-8"), ctype="text/html; charset=utf-8")
            if u.path == "/now":
                q = queue_state()
                try:
                    path, st = vlc_now()
                except Exception:
                    return self.send({"vlc": False, "queue": q["items"]})
                idx = next((i for i, it in enumerate(q["items"]) if norm(it["path"]) == norm(path)), -1)
                sc = scene(q["items"][idx]["id"]) if idx >= 0 else None
                return self.send({"vlc": True, "state": st.get("state"), "time": st.get("time"), "length": st.get("length"),
                                  "idx": idx, "path": path, "scene": sc, "queue": q["items"]})
            if u.path == "/tags":
                return self.send(tag_search(urllib.parse.parse_qs(u.query).get("q", [""])[0]))
            self.send({"error": "not found"}, 404)
        except Exception as e:
            self.send({"error": str(e)[:200]}, 500)

    def do_POST(self):
        try:
            n = int(self.headers.get("Content-Length") or 0)
            b = json.loads(self.rfile.read(n) or b"{}")
            if self.path == "/rate":
                set_rating(b["id"], b["stars"])
                q = queue_state()
                for it in q["items"]:
                    if it["id"] == b["id"]:
                        it["stars"] = int(b["stars"])
                io.open(STATE, "w", encoding="utf-8").write(json.dumps(q))
            elif self.path == "/tag":
                sc = scene(b["id"])
                set_tags(b["id"], [t["id"] for t in sc["tags"]] + [tag_id(b["name"].strip())])
            elif self.path == "/untag":
                sc = scene(b["id"])
                set_tags(b["id"], [t["id"] for t in sc["tags"] if t["id"] != b["tag"]])
            elif self.path == "/vlc":
                cmd = {"next": "pl_next", "prev": "pl_previous", "pause": "pl_pause"}[b["cmd"]]
                vlc("status.json", command=cmd)
            else:
                return self.send({"error": "not found"}, 404)
            self.send({"ok": True})
        except Exception as e:
            self.send({"error": str(e)[:200]}, 500)


PAGE = r"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Stash Grading</title>
<style>
:root{--bg:#0F1216;--panel:#171B21;--panel2:#1F242C;--ink:#E8EAEE;--ink2:#A9B0BC;--ink3:#7B8492;--acc:#FF6B35;--good:#5CC48A;--line:#2B313B;color-scheme:dark}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.45 "Segoe UI",system-ui,sans-serif}
header{height:44px;display:flex;align-items:center;gap:14px;padding:0 16px;border-bottom:1px solid var(--line);background:var(--panel)}
header b{font:800 20px "Arial Narrow",sans-serif;letter-spacing:.04em;text-transform:uppercase}header b i{display:inline-block;width:9px;height:9px;background:var(--acc);margin-right:8px}
header span{font:12px Consolas,monospace;color:var(--ink3)}header .r{margin-left:auto}
main{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:0;height:calc(100vh - 44px)}
.now{padding:22px 26px;overflow:auto}.side{border-left:1px solid var(--line);overflow:auto;background:var(--panel)}
h1{margin:0 0 6px;font:700 26px/1.2 "Segoe UI",sans-serif;overflow-wrap:anywhere}
.meta{color:var(--ink2);font-size:14px;margin-bottom:18px}.meta a{color:var(--acc)}
.bar{height:4px;background:var(--panel2);margin:0 0 22px}.bar i{display:block;height:100%;background:var(--acc);width:0}
.lbl{font:11px Consolas,monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--ink3);margin:0 0 8px}
.stars{display:flex;gap:6px;margin-bottom:24px}.stars button{font-size:40px;line-height:1;background:none;border:0;color:var(--ink3);cursor:pointer;padding:0 2px}
.stars button.on{color:var(--acc)}.stars button:hover{color:var(--ink)}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:10px}.chip{font:13px Consolas,monospace;padding:3px 8px;border:1px solid var(--line);background:var(--panel2)}
.chip button{background:none;border:0;color:var(--ink3);cursor:pointer;margin-left:6px}.chip button:hover{color:var(--acc)}
input{width:100%;max-width:420px;font:16px "Segoe UI",sans-serif;padding:9px 11px;background:var(--panel);color:var(--ink);border:1px solid var(--line)}
input:focus{outline:2px solid var(--acc)}
.ctl{display:flex;gap:8px;margin-top:26px}.ctl button{font:700 13px Consolas,monospace;letter-spacing:.08em;text-transform:uppercase;padding:8px 14px;border:1px solid var(--line);background:var(--panel2);color:var(--ink);cursor:pointer}
.ctl button:hover{border-color:var(--acc)}
.keys{margin-top:18px;font:12px Consolas,monospace;color:var(--ink3)}
.q{list-style:none;margin:0;padding:0}.q li{display:grid;grid-template-columns:22px 1fr auto;gap:8px;padding:9px 14px;border-bottom:1px solid var(--line);font-size:13.5px;color:var(--ink2)}
.q li.cur{background:var(--panel2);color:var(--ink);border-left:3px solid var(--acc)}.q li .s{color:var(--acc);font-size:12px;white-space:nowrap}
.q li .n{color:var(--ink3);font:12px Consolas,monospace}.q li span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.off{padding:40px 26px;color:var(--ink2)}.err{color:#E9788A;font:12px Consolas,monospace;min-height:16px}
@media(max-width:760px){main{grid-template-columns:1fr;height:auto}.side{border-left:0;border-top:1px solid var(--line)}}
</style></head><body>
<header><b><i></i>Grading</b><span id="pos"></span><span class="r" id="sum"></span></header>
<main><section class="now" id="now"><div class="off">Waiting for VLC...</div></section><aside class="side"><ul class="q" id="q"></ul></aside></main>
<datalist id="tl"></datalist>
<script>
const $=s=>document.querySelector(s);let cur=null,lastId=null,err='';
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const mmss=t=>{t=Math.round(t||0);return Math.floor(t/60)+':'+String(t%60).padStart(2,'0')};
async function post(p,b){const r=await fetch(p,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b)});const j=await r.json();err=j.error||'';if($('#err'))$('#err').textContent=err;return j}
function name(s){return s.title||(s.files&&s.files[0]?s.files[0].basename:'(untitled)')}
function renderQueue(q,idx){$('#q').innerHTML=q.map((it,i)=>`<li class="${i===idx?'cur':''}"><span class="n">${i+1}</span><span title="${esc(it.label)}">${esc(it.label)}</span><span class="s">${it.stars?'&#9733;'.repeat(it.stars):''}</span></li>`).join('');
  const done=q.filter(x=>x.stars).length;$('#sum').textContent=`${done} / ${q.length} rated`}
function renderNow(d){const s=d.scene;cur=s;
  if(!s){$('#now').innerHTML=`<div class="off">${d.vlc?'VLC is playing something outside this set.':'VLC is not answering. Start the set with stashgrade.py.'}</div>`;return}
  const stars=s.rating100?Math.round(s.rating100/20):0,f=s.files[0]||{},who=(s.performers||[]).map(p=>p.name).join(', ');
  $('#pos').textContent=`${d.idx+1} of ${d.queue.length}`;
  if(lastId!==s.id||!$('#tagIn')){lastId=s.id;
  $('#now').innerHTML=`<h1>${esc(name(s))}</h1>
   <div class="meta">${who?esc(who)+' · ':''}${s.studio?esc(s.studio.name)+' · ':''}${mmss(f.duration)} · <a href="http://127.0.0.1:9999/scenes/${s.id}" target="_blank">open in Stash</a></div>
   <div class="bar"><i id="prog"></i></div>
   <p class="lbl">Rating</p><div class="stars" id="stars">${[1,2,3,4,5].map(n=>`<button data-n="${n}" title="${n}">&#9733;</button>`).join('')}</div>
   <p class="lbl">Tags</p><div class="chips" id="chips"></div>
   <input id="tagIn" list="tl" placeholder="Add a tag and press Enter (new names are created)" autocomplete="off">
   <div class="ctl"><button data-c="prev">&larr; Prev</button><button data-c="pause">Pause</button><button data-c="next">Next &rarr;</button></div>
   <div class="err" id="err">${esc(err)}</div>
   <div class="keys">1-5 stars · 0 clears · N next · P prev · Space pause · T tags</div>`}
  $('#stars').querySelectorAll('button').forEach(b=>b.classList.toggle('on',+b.dataset.n<=stars));
  $('#chips').innerHTML=(s.tags||[]).map(t=>`<span class="chip">${esc(t.name)}<button data-t="${t.id}" title="remove">&times;</button></span>`).join('')||'<span class="meta">no tags yet</span>';
  $('#prog').style.width=d.length?(100*d.time/d.length)+'%':'0'}
async function tick(){try{const d=await (await fetch('/now')).json();renderQueue(d.queue||[],d.idx);renderNow(d)}catch(e){}}
async function rate(n){if(!cur)return;await post('/rate',{id:cur.id,stars:n});tick()}
async function addTag(v){v=v.trim();if(!cur||!v)return;await post('/tag',{id:cur.id,name:v});$('#tagIn').value='';tick()}
document.addEventListener('click',async e=>{const b=e.target.closest('button');if(!b)return;
  if(b.dataset.n)rate(+b.dataset.n);else if(b.dataset.t){await post('/untag',{id:cur.id,tag:b.dataset.t});tick()}else if(b.dataset.c){await post('/vlc',{cmd:b.dataset.c});setTimeout(tick,300)}});
document.addEventListener('keydown',async e=>{if(e.target.id==='tagIn'){if(e.key==='Enter')addTag(e.target.value);if(e.key==='Escape')e.target.blur();return}
  if(/^[0-5]$/.test(e.key))rate(+e.key);else if(e.key==='n'||e.key==='N'){await post('/vlc',{cmd:'next'});setTimeout(tick,300)}
  else if(e.key==='p'||e.key==='P'){await post('/vlc',{cmd:'prev'});setTimeout(tick,300)}
  else if(e.key===' '){e.preventDefault();post('/vlc',{cmd:'pause'})}else if(e.key==='t'||e.key==='T'){e.preventDefault();$('#tagIn')&&$('#tagIn').focus()}});
let tq;document.addEventListener('input',e=>{if(e.target.id!=='tagIn')return;clearTimeout(tq);const v=e.target.value;if(v.length<2)return;
  tq=setTimeout(async()=>{const l=await (await fetch('/tags?q='+encodeURIComponent(v))).json();$('#tl').innerHTML=(l||[]).map(n=>`<option value="${esc(n)}">`).join('')},200)});
tick();setInterval(tick,1000);
</script></body></html>"""


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not up():
        print("Stash isn't answering on :9999.")
        sys.exit(1)
    if "--panel" not in sys.argv:
        if not VLC:
            print("VLC not found.")
            sys.exit(1)
        minutes = int(args[0]) if args else 30
        picked, total, left = build(minutes)
        if not picked:
            print("No unrated scenes. Everything has stars.")
            sys.exit(0)
        io.open(STATE, "w", encoding="utf-8").write(json.dumps({"items": [
            {"id": s["id"], "path": s["files"][0]["path"], "label": label(s), "stars": 0} for s in picked]}))
        launch_vlc(picked, "--full" in sys.argv)
        print("GRADING SET · %d scenes · %d min · %d unrated in Stash" % (len(picked), round(total / 60), left))
    srv = ThreadingHTTPServer(("127.0.0.1", PANEL_PORT), H)
    print("panel http://127.0.0.1:%d/" % PANEL_PORT, flush=True)
    webbrowser.open("http://127.0.0.1:%d/" % PANEL_PORT)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
