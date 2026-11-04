"""gatepage.py: the Engine Room's gate page, written for a person (Chief 11/4: "I don't even know what I'm looking at").
Plain words first, the picture second, the detail last. engineroom.py reloads this module on every request, so a change
here shows on the next refresh without restarting the server."""
import html
import math
import os
import re
import time

ABOUT = {
    "00": "The ground rules: how the engine decides what is true, the patch bay, the module registry.",
    "01": "Story shape: genre, the collision engine, the scale ladder, the story registry.",
    "02": "Characters: LEECHSEED, the twelve layers, Tori's and Anna's records.",
    "03": "Places: the setting system and how a place changes over time.",
    "04": "What happens: the fabula (the world clock), the plot system, the trope graph.",
    "05": "The world's parts: the worldbuilding system and its catalog.",
    "06": "What it means: the theme system.",
    "07": "How it reads: prose, document and page style.",
    "08": "Keeping track: the tracking files (OXO's lives here).",
    "09": "Running the work: project flow and the house standards.",
}
PARK = "⏸"


def esc(s):
    return html.escape(str(s))


def json_script(obj):
    import json
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


def clock12(iso):
    t = time.strptime(iso, "%Y-%m-%dT%H:%M:%S")
    return time.strftime("%I:%M %p", t).lstrip("0")


def doc_name(path):
    base = os.path.basename(path)
    folder = os.path.basename(os.path.dirname(path))
    page = ""
    m = re.match(r"^\d-(\w[\w-]*)\.md$", base)
    if m:  # a doc page: _DOCS/<sys>/<doc>/2-reference.md
        page = " (" + m.group(1).replace("-", " ") + " page)"
        base = folder
    base = re.sub(r"\.md$", "", base)
    base = re.sub(r"^[^\w]+", "", base).strip()
    base = re.sub(r"^ssot[_ ]+\d\d[_ ]*", "", base, flags=re.I)
    base = base.replace("_", " ").strip()
    return (base[:1].upper() + base[1:] if base else os.path.basename(path)) + page


def plain(text, kind):
    """Turn one markdown / YAML line into a plain sentence: (title, note)."""
    t = text.strip()
    m = re.match(r"^[-*]?\s*([\w.\-\[\]]+):\s*(null|~|\"\"|''|\[\]|\{\})?\s*#\s*" + PARK + r"?\s*(.*)$", t)
    if m:  # a YAML field left empty
        note = m.group(3).strip()
        note = re.sub(r"\s*→\s*see\s+\S+", "", note)
        return m.group(1).replace("_", " "), "Empty, waiting on: " + (note or "a fill pass")
    m = re.match(r"^>\s*\*\*OPEN:\*\*\s*(.*)$", t)
    if m:
        return "Unanswered", clean(m.group(1))
    if t.startswith("|"):  # a table row
        cells = [clean(c) for c in t.strip("|").split("|")]
        cells = [c for c in cells if c and not set(c) <= set("-: ")]
        if cells:
            return cells[0][:80], " · ".join(cells[1:])[:240]
    return "", clean(t)[:280]


def clean(s):
    s = re.sub(r"\[\[[^\]]+\]\]", "", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = s.replace("**", "").replace("`", "").replace(PARK, "")
    s = re.sub(r"^#+\s*", "", s.strip())
    s = re.sub(r"^[-*]\s+", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip(" ·|")


def ring(systems):
    """The Ninestar ring as a small SVG: 00 in the middle, 01-09 around, each dot sized and lit by what is left."""
    S, C, R = 300, 150, 112
    mx = max([s["gate"] for s in systems] + [1])
    parts = ["<svg viewBox='0 0 300 300' role='img' aria-label='The ten systems, sized by how much is left'>",
             "<circle cx='150' cy='150' r='112' fill='none' stroke='var(--line)'/>"]
    pos = {}
    for s in systems:
        if s["id"] == "00":
            pos["00"] = (C, C)
        else:
            a = (-90 + (int(s["id"]) - 1) * 40) * math.pi / 180
            pos[s["id"]] = (C + R * math.cos(a), C + R * math.sin(a))
    for s in systems:
        if s["id"] != "00":
            x, y = pos[s["id"]]
            parts.append("<line x1='150' y1='150' x2='%.1f' y2='%.1f' stroke='var(--line)'/>" % (x, y))
    for s in systems:
        x, y = pos[s["id"]]
        r = 11 + 15 * math.sqrt(s["gate"] / mx)
        done = s["gate"] == 0
        parts.append("<a href='#s%s'><g class='dot'><title>%s %s: %d left</title>"
                     "<circle cx='%.1f' cy='%.1f' r='%.1f' fill='%s' stroke='%s' stroke-width='2'/>"
                     "<text x='%.1f' y='%.1f' text-anchor='middle' dominant-baseline='central' font-size='11' font-weight='700' fill='%s'>%s</text></g></a>" % (
                         s["id"], s["id"], esc(s["name"]), s["gate"], x, y, r,
                         "var(--okbg)" if done else "rgba(255,90,31,%.2f)" % (0.15 + 0.6 * s["gate"] / mx),
                         "var(--ok)" if done else "var(--accent)", x, y,
                         "var(--ink)", s["gate"] if not done else "✓"))
    parts.append("</svg>")
    return "".join(parts)


CSS = """
:root{--bg:#121315;--plate:#1a1c1f;--plate2:#202327;--line:#2c2f34;--ink:#ece9e4;--dim:#a29e98;--faint:#66625c;
--accent:#FF5A1F;--ok:#7fbf8e;--okbg:rgba(127,191,142,.18);color-scheme:dark}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 "Segoe UI",system-ui,sans-serif}
a{color:inherit}
.strip{display:flex;align-items:center;gap:12px;min-height:44px;padding:8px 20px;border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--bg);z-index:5}
.strip b{color:var(--accent)}.strip .t{font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:14px}
.strip .m{color:var(--dim);font-size:13px;margin-left:auto}
main{max-width:1100px;margin:0 auto;padding:22px 20px 60px;display:grid;gap:22px}
.hero{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(220px,300px);gap:24px;align-items:center}
@media(max-width:760px){.hero{grid-template-columns:1fr}}
.hero h1{font-size:30px;line-height:1.2;margin:0 0 10px;font-weight:600;text-wrap:balance}.hero h1 span{color:var(--accent)}
.hero p{margin:0 0 10px;color:var(--dim);max-width:60ch}.hero p strong{color:var(--ink)}
.lock{display:inline-flex;gap:8px;align-items:center;font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
padding:4px 12px;border-radius:999px;border:1px solid var(--accent);color:var(--accent)}.lock.open{border-color:var(--ok);color:var(--ok)}
.ring svg{width:100%;height:auto;display:block}.dot circle{transition:stroke-width .15s}.dot:hover circle{stroke-width:4}
.boxes{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:14px}
.box{background:var(--plate);border:1px solid var(--line);border-radius:8px;padding:14px 16px}
.box h2{margin:0 0 6px;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--dim);font-weight:600}
.box p{margin:0}.box.next{border-color:var(--accent)}.box.next h2{color:var(--accent)}
.legend{display:grid;gap:6px;margin:0;padding:0;list-style:none}.legend li{display:flex;gap:10px;align-items:baseline}
.chip{display:inline-block;font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:1px 8px;border-radius:999px;white-space:nowrap}
.chip.q{background:rgba(255,90,31,.15);color:var(--accent)}.chip.f{background:rgba(255,255,255,.07);color:var(--ink)}
h2.sec{font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:var(--dim);margin:6px 0 -8px;font-weight:600}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:12px}
details.card{background:var(--plate);border:1px solid var(--line);border-radius:8px}
details.card[open]{grid-column:1/-1;border-color:var(--faint)}
details.card>summary{list-style:none;cursor:pointer;padding:14px 16px;display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:4px 12px;align-items:center}
details.card>summary::-webkit-details-marker{display:none}
.num{font-size:12px;font-weight:700;color:var(--dim);font-family:Consolas,monospace}
.nm{font-weight:600;font-size:16px}.left{font-size:26px;font-weight:600;font-variant-numeric:tabular-nums;color:var(--accent);text-align:right;line-height:1}
.left small{display:block;font-size:11px;color:var(--dim);font-weight:500;letter-spacing:.06em;text-transform:uppercase}
.left.done{color:var(--ok)}.about{grid-column:2/4;color:var(--dim);font-size:13px}
.split{grid-column:2/4;display:flex;gap:8px;flex-wrap:wrap}
.bar{grid-column:1/-1;height:4px;background:var(--line);border-radius:2px;overflow:hidden}.bar i{display:block;height:4px;background:var(--accent)}
.inside{padding:0 16px 16px;display:grid;gap:12px}
.file{background:var(--plate2);border-radius:6px;padding:10px 12px}
.file h3{margin:0 0 6px;font-size:14px;font-weight:600;display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
.file h3 span{color:var(--dim);font-weight:400;font-size:12px}
.items{margin:0;padding:0;list-style:none;display:grid;gap:6px}
.items li{display:grid;grid-template-columns:auto minmax(0,1fr);gap:10px;align-items:baseline;font-size:14px}
.items .w{color:var(--faint);font-size:12px;font-family:Consolas,monospace}
.items .ti{font-weight:600}.more{color:var(--dim);font-size:13px}
details.behind{background:transparent;border:1px dashed var(--line);border-radius:8px;padding:10px 16px;color:var(--dim)}
details.behind summary{cursor:pointer}details.behind table{width:100%;border-collapse:collapse;margin-top:10px;font-size:13px;font-variant-numeric:tabular-nums}
details.behind td,details.behind th{padding:5px 8px;border-bottom:1px solid var(--line);text-align:right}
details.behind td:first-child,details.behind th:first-child{text-align:left}
"""


def card(s, maxgate, answers=None, recs=None, data=None):
    answers = answers or {}
    recs = recs or {}
    rows = [r for r in s.get("rows", []) if not r["dropped"] and not r["waived"] and r["kind"] in ("open", "parked")]
    by_file = {}
    for r in rows:
        by_file.setdefault(r["file"], []).append(r)
    files = sorted(by_file.items(), key=lambda kv: -len(kv[1]))
    inner = []
    for f, items in files:
        q = sum(1 for r in items if r["kind"] == "open")
        e = len(items) - q
        li = []
        for r in items:
            title, note = plain(r["text"], r["kind"])
            rid = r["row_id"]
            if data is not None:
                data[rid] = {"sys": s["id"], "sysname": s["name"], "file": r["file"], "doc": doc_name(r["file"]), "line": r["line"],
                             "kind": r["kind"], "text": r["text"], "title": title, "note": note}
            chip = "<span class='chip q'>question</span>" if r["kind"] == "open" else "<span class='chip f'>empty</span>"
            a = answers.get(rid)
            state = ""
            if a and a.get("status") == "answered":
                state = "<span class='chip ok'>answered · waiting to be written</span> "
            rc = recs.get(rid)
            what = ("<span class='what'>%s</span>" % esc(rc["what"])) if rc and rc.get("what") else ""
            li.append("<li data-row='%s' class='%s'>%s<span>%s%s%s <span class='w'>line %d</span>%s</span>"
                      "<span class='acts'><button class='b ans' data-act='answer'>Answer</button>"
                      "<button class='b' data-act='copy' title='Copy this blank for chat in VS Code'>Copy</button></span></li>" % (
                          esc(rid), "is-ans" if state else "", chip, state, ("<span class='ti'>%s</span> · " % esc(title)) if title else "",
                          esc(note), r["line"], what))
        more = ""
        parts = []
        if q:
            parts.append("%d question%s" % (q, "" if q == 1 else "s"))
        if e:
            parts.append("%d empty field%s" % (e, "" if e == 1 else "s"))
        inner.append("<div class='file'><h3>%s <span>%s · %s</span><button class='b copyall' data-file='%s'>Copy all %d for chat</button></h3>"
                     "<ul class='items'>%s</ul>%s</div>" % (esc(doc_name(f)), " · ".join(parts), esc(f), esc(f), len(items), "".join(li), more))
    w = int(100 * s["gate"] / maxgate) if maxgate else 0
    done = s["gate"] == 0
    return ("<details class='card' id='s%s'><summary><span class='num'>%s</span><span class='nm'>%s</span>"
            "<span class='left%s'>%s<small>%s</small></span><span class='about'>%s</span>"
            "<span class='split'><span class='chip q'>%d questions</span><span class='chip f'>%d empty fields</span></span>"
            "<span class='bar'><i style='width:%d%%'></i></span></summary><div class='inside'>%s</div></details>") % (
        s["id"], s["id"], esc(s["name"]), " done" if done else "", "✓" if done else s["gate"], "all clear" if done else "left",
        esc(ABOUT.get(s["id"], "")), s["open"], s["parked"], w,
        "".join(inner) or "<p class='more'>Nothing left here.</p>")


MODAL_CSS = """
.b{background:var(--plate2);color:var(--ink);border:1px solid var(--line);border-radius:5px;padding:3px 10px;font:inherit;font-size:12px;cursor:pointer}
.b:hover{border-color:var(--accent)}.b.ans{border-color:var(--accent);color:var(--accent)}.b.copyall{margin-left:auto}
.items li{grid-template-columns:auto minmax(0,1fr) auto}.items li .acts{display:flex;gap:6px}
.items li.is-ans{opacity:.75}.chip.ok{background:var(--okbg);color:var(--ok)}
.what{display:block;color:var(--dim);font-size:13px;margin-top:2px}
.file h3{align-items:center}
#modal{position:fixed;inset:0;background:rgba(0,0,0,.6);display:flex;align-items:flex-start;justify-content:center;padding:40px 16px;z-index:20;overflow:auto}
#modal .win{background:var(--plate);border:1px solid var(--accent);border-radius:10px;width:min(760px,100%);padding:18px 20px;display:grid;gap:12px}
#modal .hd{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}#modal .hd b{font-size:17px}#modal .hd span{color:var(--dim);font-size:13px}
#modal .x{margin-left:auto}
#modal .ask{font-size:16px}#modal .raw{background:var(--bg);border-radius:6px;padding:8px 10px;font:12px/1.5 Consolas,monospace;color:var(--dim);white-space:pre-wrap;word-break:break-word}
#modal .rec{border-left:3px solid var(--accent);background:var(--plate2);padding:8px 12px;border-radius:0 6px 6px 0}
#modal .rec .rt{font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}
#modal .rec .rv{font-size:15px;font-weight:600;margin:2px 0}#modal .rec .ry{color:var(--dim);font-size:13px}
#modal textarea,#modal input{width:100%;background:var(--bg);color:var(--ink);border:1px solid var(--line);border-radius:6px;padding:8px 10px;font:inherit}
#modal textarea{min-height:110px;resize:vertical}#modal label{font-size:12px;color:var(--dim);letter-spacing:.06em;text-transform:uppercase}
#modal .row{display:flex;gap:8px;flex-wrap:wrap}#modal .go{background:var(--accent);color:#111;border-color:var(--accent);font-weight:700;padding:6px 16px;font-size:14px}
#modal .b{padding:6px 14px;font-size:14px}#modal .msg{color:var(--dim);font-size:13px;min-height:1.2em}
#toast{position:fixed;bottom:18px;left:50%;transform:translateX(-50%);background:var(--plate2);border:1px solid var(--accent);padding:8px 16px;border-radius:999px;z-index:30}
"""

MODAL_JS = r"""
const DATA = JSON.parse(document.getElementById('er-data').textContent);
const RECS = JSON.parse(document.getElementById('er-recs').textContent);
const modal = document.getElementById('modal'); let cur = null;
const $ = (s) => modal.querySelector(s);
function toast(t){const el=document.getElementById('toast');el.textContent=t;el.hidden=false;clearTimeout(toast.h);toast.h=setTimeout(()=>el.hidden=true,2200);}
function block(id){const d=DATA[id];if(!d)return'';const r=RECS[id];
  let s='Engine Room blank · '+d.sys+' '+d.sysname+' · '+(d.kind==='open'?'question':'empty field')+'\nWhere: '+d.file+':'+d.line+'\nText: '+d.text;
  if(r){s+='\nWhat it asks (draft): '+(r.what||'')+'\nRec ('+(r.rec_type||'')+'): '+(r.rec||'')+(r.why?'\nWhy: '+r.why:'')+(r.source?'\nSource: '+r.source:'');}
  return s;}
async function copy(t){try{await navigator.clipboard.writeText(t);toast('Copied. Paste it into chat in VS Code.');}
  catch(e){const ta=document.createElement('textarea');ta.value=t;document.body.appendChild(ta);ta.select();document.execCommand('copy');ta.remove();toast('Copied.');}}
function open(id){const d=DATA[id];if(!d)return;cur=id;const r=RECS[id];
  $('.hd b').textContent=d.sys+' '+d.sysname+' · '+(d.kind==='open'?'A question':'An empty field');
  $('.hd span').textContent=d.doc+' · line '+d.line;
  $('.ask').textContent=(r&&r.what)?r.what:((d.title?d.title+' · ':'')+d.note);
  $('.raw').textContent=d.text;
  const rb=$('.rec');if(r&&r.rec){rb.hidden=false;$('.rt').textContent='Rec · '+(r.rec_type||'')+(r.confidence?' · '+r.confidence+' confidence':'');
    $('.rv').textContent=r.rec;$('.ry').textContent=(r.why||'')+(r.source?'  Source: '+r.source:'')+(r.options&&r.options.length?'  Options: '+r.options.join(' / '):'');
    $('#take').hidden=false;}else{rb.hidden=true;$('#take').hidden=true;}
  $('#ans').value='';$('#src').value='';$('.msg').textContent=r?'':'No rec drafted for this one yet. Copy it to chat if it makes no sense.';
  modal.hidden=false;setTimeout(()=>$('#ans').focus(),30);}
function close(){modal.hidden=true;cur=null;}
async function save(mode){if(!cur)return;const d=DATA[cur],r=RECS[cur];
  const body={row_id:cur,sys:d.sys,file:d.file,line:d.line,kind:d.kind,text:d.text,mode:mode,
    answer:mode==='rec'?(r?r.rec:''):$('#ans').value,source_note:$('#src').value,rec:r?r.rec:''};
  if(mode==='answer'&&!body.answer.trim()){$('.msg').textContent='Write an answer first, or take the rec, or skip.';return;}
  const res=await fetch('/api/answer',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
  const j=await res.json();if(!j.ok){$('.msg').textContent=j.error||'Not saved.';return;}
  const li=document.querySelector('li[data-row="'+CSS.escape(cur)+'"]');
  if(li){if(mode==='skip'){li.remove();}else{li.classList.add('is-ans');if(!li.querySelector('.chip.ok')){const c=document.createElement('span');c.className='chip ok';c.textContent='answered · waiting to be written';li.children[1].prepend(c,document.createTextNode(' '));}}}
  const q=document.getElementById('qcount');if(q)q.textContent=j.queue;
  toast(mode==='skip'?'Skipped. It leaves the count now.':'Saved. '+j.queue+' answers waiting: say "apply answers" in chat.');close();}
document.addEventListener('click',(e)=>{const b=e.target.closest('button');if(!b)return;
  const li=b.closest('li[data-row]');
  if(b.dataset.act==='answer'&&li){e.preventDefault();open(li.dataset.row);}
  else if(b.dataset.act==='copy'&&li){e.preventDefault();copy(block(li.dataset.row)+'\n\nExplain what this blank is asking and give me your rec.');}
  else if(b.classList.contains('copyall')){e.preventDefault();const f=b.dataset.file;
    const ids=Object.keys(DATA).filter(k=>DATA[k].file===f&&document.querySelector('li[data-row="'+CSS.escape(k)+'"]'));
    copy(ids.map(block).join('\n\n---\n\n')+'\n\nWalk me through these blanks one at a time: what each asks and your rec.');}});
$('.x').onclick=close;$('#save').onclick=()=>save('answer');$('#take').onclick=()=>save('rec');$('#skip').onclick=()=>save('skip');
$('#copy1').onclick=()=>copy(block(cur)+'\n\nExplain what this blank is asking and give me your rec.');
modal.addEventListener('click',(e)=>{if(e.target===modal)close();});
document.addEventListener('keydown',(e)=>{if(modal.hidden)return;if(e.key==='Escape')close();if(e.key==='Enter'&&(e.ctrlKey||e.metaKey))save('answer');});
"""

BOOT_CSS = """
#boot{position:fixed;inset:0;z-index:50;background:#000;overflow:hidden;cursor:pointer;transition:opacity .5s,background .3s;font:14px/1.6 Consolas,"Cascadia Mono",monospace}
#boot.gone{opacity:0;pointer-events:none}#boot.corner{background:#1a0d07}
#dvd{position:absolute;left:0;top:0;width:min(24vw,280px);height:auto;will-change:transform;user-select:none}
#dvd.vid{width:auto;height:min(46vh,420px);mix-blend-mode:screen;filter:contrast(1.45) brightness(.92);-webkit-mask-image:radial-gradient(ellipse 50% 50% at 50% 50%,#000 62%,transparent 100%);mask-image:radial-gradient(ellipse 50% 50% at 50% 50%,#000 62%,transparent 100%)}/* Chief 11/4: transparent. The clip's dark backdrop is crushed to black and screened out; the edges feather away */
#blog{position:fixed;left:18px;bottom:34px;color:#cfcac3;white-space:pre;max-width:calc(100vw - 36px);overflow:hidden}
#blog .okt{color:#7fbf8e;font-weight:600}#blog .bv{color:#FF5A1F;font-weight:600}
#bskip{position:fixed;right:18px;bottom:10px;color:#9a9690}#bstat{position:fixed;left:18px;bottom:10px;color:#9a9690}
.blink{color:#FF5A1F!important;font-weight:600;animation:blink 1.1s steps(1) infinite}@keyframes blink{50%{opacity:0}}
"""

BOOT_JS = r"""
(function(){const B=document.getElementById('boot'),el=document.getElementById('dvd'),log=document.getElementById('blog'),
 sk=document.getElementById('bskip'),st=document.getElementById('bstat'),LINES=JSON.parse(document.getElementById('er-boot').textContent);
 let on=false,tok=null,timer=null;
 function bounce(){const t={},red=matchMedia('(prefers-reduced-motion: reduce)').matches;tok=t;
  let x=Math.random()*Math.max(0,innerWidth-300),y=Math.random()*Math.max(0,innerHeight-300),vx=(Math.random()<.5?-1:1)*150,vy=(Math.random()<.5?-1:1)*115,last=performance.now();
  function f(now){if(!on||tok!==t)return;const dt=Math.min(.05,(now-last)/1000),W=Math.max(0,innerWidth-el.offsetWidth),H=Math.max(0,innerHeight-el.offsetHeight);let hx=false,hy=false;last=now;
   if(!red){x+=vx*dt;y+=vy*dt}if(x<=0){x=0;vx=Math.abs(vx);hx=true}else if(x>=W){x=W;vx=-Math.abs(vx);hx=true}
   if(y<=0){y=0;vy=Math.abs(vy);hy=true}else if(y>=H){y=H;vy=-Math.abs(vy);hy=true}
   if(hx&&hy){B.classList.add('corner');setTimeout(()=>B.classList.remove('corner'),600)}
   el.style.transform='translate('+Math.round(x)+'px,'+Math.round(y)+'px)';requestAnimationFrame(f)}requestAnimationFrame(f)}
 function lines(){log.innerHTML='';let i=0;st.textContent='';sk.className='';sk.textContent='SPACE · skip';
  (function next(){if(!on)return;if(i<LINES.length){const d=document.createElement('div');d.innerHTML=LINES[i++];log.appendChild(d);
    while(log.children.length>7)log.removeChild(log.firstChild);timer=setTimeout(next,380);}
   else{sk.className='blink';sk.textContent='press SPACE to continue';}})();}
 function skip(){on=false;clearTimeout(timer);B.classList.add('gone');try{sessionStorage.setItem('er-booted','1')}catch(e){}}
 function boot(){on=true;B.classList.remove('gone');bounce();lines();}
 B.onclick=skip;
 document.addEventListener('keydown',(e)=>{const m=document.getElementById('modal');if(m&&!m.hidden)return;
  if(on&&(e.key===' '||e.key==='Enter')){e.preventDefault();skip();}else if(!on&&e.key==='b'&&!/INPUT|TEXTAREA/.test(document.activeElement.tagName)){boot();}});
 let seen=false;try{seen=sessionStorage.getItem('er-booted')==='1'}catch(e){}
 if(seen)B.classList.add('gone');else boot();})();
"""

BOOT_HTML = """<div id="boot">%s<div id="blog"></div><span id="bstat"></span><span id="bskip">SPACE · skip</span></div>"""


def bounce_tag():
    """A video clip (Chief 11/4: the Engine Room's .webm) bounces as a muted looping video; a picture as an img."""
    here = os.path.dirname(os.path.abspath(__file__))
    own = os.path.join(here, "..", "..", "_PRIVATE", "engineroom")
    for ext in ("webm", "mp4"):
        if os.path.isfile(os.path.join(own, "bounce." + ext)):
            return '<video id="dvd" class="vid" src="/bounce" autoplay muted loop playsinline></video>'
    return '<img id="dvd" src="/bounce" alt="" draggable="false">'


def boot_lines(g, answers, recs):
    t = g["totals"]
    ok = "<span class='okt'>[  OK  ]</span> "
    docs = sum(1 for s in g["systems"] for r in s.get("rows", []))
    q = sum(1 for a in answers.values() if a.get("status") == "answered")
    out = [ok + "Started the Engine Room on 127.0.0.1:8796",
           ok + "Read the ten Venture Engine systems, 00 Epistemology to 09 Operations",
           ok + "Scanned %d marked lines across the system docs" % docs,
           ok + "Cleaned out %d notes, templates and history lines" % t["dropped"],
           ok + "Counted %d questions and %d empty fields" % (t["open"], t["parked"]),
           ok + "Loaded %d drafted recs" % len(recs),
           ok + "Found %d answers waiting to be written" % q,
           "<span class='okt'>Reached target</span> <span class='bv'>The Engine Room</span><span class='okt'>.  %d blanks left.</span>" % t["gate"]]
    return out


MODAL_HTML = """<div id="modal" hidden><div class="win" role="dialog" aria-modal="true" aria-label="Answer a blank">
<div class="hd"><b></b><span></span><button class="b x" title="Close (Esc)">Close</button></div>
<div class="ask"></div>
<div class="raw"></div>
<div class="rec" hidden><div class="rt"></div><div class="rv"></div><div class="ry"></div></div>
<div><label for="ans">Your answer</label><textarea id="ans" placeholder="Write the answer or the value. Ctrl+Enter saves."></textarea></div>
<div><label for="src">Where it comes from (optional)</label><input id="src" placeholder="e.g. my head, the 2013 notes, a book"></div>
<div class="row"><button class="b go" id="take">Take the rec</button><button class="b go" id="save">Save my answer</button>
<button class="b" id="skip" title="Waive it: it leaves the count now">Skip</button><button class="b" id="copy1">Copy for chat</button></div>
<div class="msg"></div></div></div><div id="toast" hidden></div>"""


def page(g, answers=None, recs=None):
    answers = answers or {}
    recs = recs or {}
    data = {}
    queued = sum(1 for a in answers.values() if a.get("status") == "answered")
    t = g["totals"]
    systems = g["systems"]
    order = sorted(systems, key=lambda s: -s["gate"])
    top = order[0] if order and order[0]["gate"] else None
    maxgate = max([s["gate"] for s in systems] + [1])
    clear = sum(1 for s in systems if s["gate"] == 0)
    lock = "<span class='lock open'>Plotting unlocked</span>" if g["plotting_unlocked"] else "<span class='lock'>Plotting locked</span>"
    nxt = ("Start with <strong>%s</strong>: %d left. Open its card below; each line says what is missing and where it lives." % (
        esc(top["name"]), top["gate"])) if top else "Everything is answered. Plotting can start."
    cards_html = "".join(card(s, maxgate, answers, recs, data) for s in order)
    behind = "".join("<tr><td>%s %s</td><td>%d</td><td>%d</td><td>%d</td><td>%d</td></tr>" % (
        s["id"], esc(s["name"]), s["unmarked"], s["dropped"], s["waived"], s["raw_open"] + s["raw_parked"]) for s in systems)
    return """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Engine Room</title><style>%s</style></head><body>
<header class="strip"><span class="t">The <b>Engine Room</b></span><span class="m">Counted at %s · refresh to recount</span></header>
<main>
<section class="hero">
  <div>
    %s
    <h1><span>%d</span> blanks left before you can plot OXO</h1>
    <p>The Venture Engine is your ten story systems. This page counts every blank still in them: a <strong>question</strong> nobody has answered yet, or an <strong>empty field</strong> left for later. You set the rule on 10/4: every system done before any plotting (BOLO 100).</p>
    <p><strong>%d of 10</strong> systems are clear. The biggest dot on the ring has the most left.</p>
  </div>
  <div class="ring">%s</div>
</section>

<section class="boxes">
  <div class="box next"><h2>What to do next</h2><p>%s</p></div>
  <div class="box"><h2>How to read a card</h2><ul class="legend">
    <li><span class="chip q">question</span><span>A decision only you can make. Usually one line.</span></li>
    <li><span class="chip f">empty</span><span>A field on a character, place or event that has no value yet.</span></li>
    <li><span style="color:var(--accent);font-weight:700">129</span><span>How many blanks that system still has.</span></li>
  </ul></div>
  <div class="box"><h2>How a blank goes away</h2><p>Click <strong>Answer</strong> on any line: take the rec, write your own, or skip it. Confused? <strong>Copy</strong> it and paste it to me in VS Code. <strong id="qcount">%d</strong> answers are waiting; say <strong>"apply answers"</strong> in chat and agents write them into the docs.</p></div>
</section>

<h2 class="sec">The ten systems, most left first</h2>
<section class="cards">%s</section>

<details class="behind"><summary>Behind the scenes: what the count leaves out</summary>
<p>Loose mentions use the word OPEN without the formal marker; you ruled they don't count (11/4). Ignored lines are templates, version history, marker legends and diagrams. Skipped means you waived it. Raw is everything before that cleanup.</p>
<table><thead><tr><th>System</th><th>Loose mentions</th><th>Ignored</th><th>Skipped</th><th>Raw</th></tr></thead><tbody>%s</tbody></table>
</details>
</main>%s%s
<script type="application/json" id="er-data">%s</script>
<script type="application/json" id="er-recs">%s</script>
<script type="application/json" id="er-boot">%s</script>
<script>%s</script><script>%s</script></body></html>""" % (CSS + MODAL_CSS + BOOT_CSS, clock12(g["counted_at"]), lock, t["gate"], clear, ring(systems), nxt, queued,
                             cards_html, behind, MODAL_HTML, BOOT_HTML % bounce_tag(), json_script(data), json_script(recs),
                             json_script(boot_lines(g, answers, recs)), MODAL_JS, BOOT_JS)
