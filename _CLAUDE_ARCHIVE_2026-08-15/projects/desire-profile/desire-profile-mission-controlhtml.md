---
title: "desire-profile-mission-control.html"
project: "DESIRE PROFILE"
trunk: ORANGE
kind: project-knowledge
---

<!-- Desire Profile — Mission Control. Single-file dashboard. Persists via window.storage; embedded coach via Anthropic API. -->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Spectral:ital,wght@0,400;0,500;0,600;1,400&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  :root{
    --bg:#0b0908; --bg2:#0f0c0a; --panel:#151010; --panel2:#1c1512; --raise:#241a15;
    --ink:#ece0cf; --ink2:#cdbfac; --muted:#8a7a68; --faint:#5a4d40;
    --ember:#ff7a2f; --ember-dim:#b8531f; --amber:#f4ad52; --gold:#ffcf7a;
    --blood:#c0392b; --ok:#e08a3c;
    --line:#2b211a; --line2:#3a2c21;
    --glow:0 0 18px rgba(255,122,47,.25);
    --font-disp:"Bebas Neue",sans-serif; --font-body:"Spectral",Georgia,serif; --font-mono:"JetBrains Mono",monospace;
  }
  *{box-sizing:border-box}
  html,body{margin:0}
  body{
    background:
      radial-gradient(1200px 700px at 88% -10%, rgba(255,122,47,.10), transparent 60%),
      radial-gradient(900px 600px at 0% 110%, rgba(192,57,43,.08), transparent 55%),
      var(--bg);
    color:var(--ink); font-family:var(--font-body); line-height:1.5;
    -webkit-font-smoothing:antialiased; min-height:100vh;
  }
  body::before{ /* grain */
    content:""; position:fixed; inset:0; pointer-events:none; opacity:.05; z-index:9999;
    background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  }
  .wrap{max-width:1180px; margin:0 auto; padding:26px 20px 70px}
  a{color:var(--amber); text-decoration:none; border-bottom:1px dotted var(--ember-dim)}
  a:hover{color:var(--gold)}

  /* ---- header ---- */
  .top{display:flex; flex-wrap:wrap; align-items:flex-end; justify-content:space-between; gap:14px; padding-bottom:14px; border-bottom:1px solid var(--line)}
  .brand{display:flex; align-items:center; gap:14px}
  .reticle{width:34px;height:34px;border:1px solid var(--ember-dim);border-radius:50%;position:relative;flex:0 0 auto;box-shadow:var(--glow)}
  .reticle::before,.reticle::after{content:"";position:absolute;background:var(--ember)}
  .reticle::before{left:50%;top:5px;bottom:5px;width:1px;transform:translateX(-.5px)}
  .reticle::after{top:50%;left:5px;right:5px;height:1px;transform:translateY(-.5px)}
  .reticle i{position:absolute;inset:11px;border-radius:50%;background:var(--ember);box-shadow:var(--glow);animation:pulse 3.4s ease-in-out infinite}
  @keyframes pulse{0%,100%{opacity:.55}50%{opacity:1}}
  h1{font-family:var(--font-disp); font-weight:400; font-size:39px; letter-spacing:2px; margin:0; line-height:.92}
  h1 span{color:var(--ember)}
  .sub{font-family:var(--font-mono); font-size:10.5px; letter-spacing:3px; color:var(--muted); text-transform:uppercase; margin-top:3px}
  .meta-r{font-family:var(--font-mono); font-size:10px; letter-spacing:2px; color:var(--faint); text-align:right; text-transform:uppercase}
  .meta-r b{color:var(--ink2);font-weight:500}
  .dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--ember);box-shadow:var(--glow);margin-right:5px;vertical-align:middle}
  .dot.warn{background:var(--amber);box-shadow:0 0 10px rgba(244,173,82,.4)}
  .dot.err{background:var(--blood)}

  /* ---- status strip ---- */
  .status{display:grid; grid-template-columns:1.4fr 1fr; gap:14px; margin:18px 0 22px}
  @media(max-width:740px){.status{grid-template-columns:1fr}}
  .card{background:linear-gradient(180deg,var(--panel2),var(--panel)); border:1px solid var(--line); border-radius:10px; padding:16px 18px; position:relative; overflow:hidden}
  .card::after{content:"";position:absolute;top:8px;right:8px;width:18px;height:18px;border-top:1px solid var(--line2);border-right:1px solid var(--line2);opacity:.7}
  .lbl{font-family:var(--font-mono); font-size:9.5px; letter-spacing:2.5px; color:var(--muted); text-transform:uppercase; margin-bottom:9px}
  .objective .obj-title{font-family:var(--font-disp); font-size:25px; letter-spacing:1px; color:var(--gold); line-height:1.02}
  .objective .obj-detail{color:var(--ink2); font-size:14.5px; margin-top:7px}
  .objective .obj-detail em{color:var(--ember);font-style:normal}
  .gauge-wrap{display:flex; align-items:center; gap:14px}
  .pct{font-family:var(--font-disp); font-size:46px; color:var(--ember); line-height:.8; min-width:96px}
  .pct small{font-family:var(--font-mono);font-size:13px;color:var(--muted);letter-spacing:1px}
  .segs{display:flex; gap:3px; flex:1; height:24px}
  .seg{flex:1; border-radius:2px; background:#241a14; border:1px solid #2e221a; transition:.25s}
  .seg.on{background:linear-gradient(180deg,var(--amber),var(--ember)); border-color:var(--ember); box-shadow:0 0 7px rgba(255,122,47,.5)}
  .gnote{font-family:var(--font-mono); font-size:10px; letter-spacing:1.5px; color:var(--faint); margin-top:10px; text-transform:uppercase}

  /* ---- stations grid ---- */
  .grid{display:grid; grid-template-columns:repeat(2,1fr); gap:16px}
  @media(max-width:740px){.grid{grid-template-columns:1fr}}
  .station{background:linear-gradient(180deg,var(--panel),#120e0c); border:1px solid var(--line); border-radius:11px; padding:0; opacity:0; transform:translateY(8px); animation:rise .5s forwards}
  @keyframes rise{to{opacity:1;transform:none}}
  .st-head{display:flex; align-items:center; justify-content:space-between; padding:13px 16px; border-bottom:1px solid var(--line); background:rgba(255,122,47,.03)}
  .st-name{font-family:var(--font-disp); font-size:21px; letter-spacing:1px; color:var(--ink)}
  .st-name b{color:var(--ember-dim); font-weight:400}
  .led{font-family:var(--font-mono); font-size:9px; letter-spacing:2px; color:var(--muted); display:flex; align-items:center; gap:6px; text-transform:uppercase}
  .led i{width:8px;height:8px;border-radius:50%;background:#3a2c21;display:inline-block}
  .led.part i{background:var(--amber);box-shadow:0 0 7px rgba(244,173,82,.5)}
  .led.full i{background:var(--ember);box-shadow:var(--glow)}
  .st-body{padding:12px 16px 16px}

  .row{display:flex; align-items:center; gap:11px; padding:7px 0}
  .row + .row{border-top:1px dashed #221913}
  .tog{flex:0 0 auto; width:34px; height:20px; border-radius:4px; border:1px solid var(--line2); background:#171010; position:relative; cursor:pointer; transition:.18s}
  .tog::after{content:""; position:absolute; top:2px; left:2px; width:14px; height:14px; border-radius:3px; background:#4a3a2e; transition:.18s}
  .tog.on{background:linear-gradient(180deg,var(--amber),var(--ember-dim)); border-color:var(--ember)}
  .tog.on::after{left:16px; background:#fff3e3; box-shadow:0 0 8px rgba(255,243,227,.7)}
  .row label{flex:1; cursor:pointer; font-size:14.5px; color:var(--ink2)}
  .row.done label{color:var(--faint); text-decoration:line-through; text-decoration-color:var(--ember-dim)}
  .go{font-family:var(--font-mono); font-size:9.5px; letter-spacing:1px; padding:3px 8px; border:1px solid var(--line2); border-radius:4px; color:var(--amber); text-transform:uppercase; white-space:nowrap}
  .go:hover{border-color:var(--ember); color:var(--gold)}

  textarea, input.txt{width:100%; background:#100b09; border:1px solid var(--line2); border-radius:6px; color:var(--ink); font-family:var(--font-body); font-size:14px; padding:9px 11px; resize:vertical; outline:none}
  textarea:focus, input.txt:focus{border-color:var(--ember-dim); box-shadow:0 0 0 2px rgba(255,122,47,.10)}
  textarea::placeholder, input::placeholder{color:#5a4c3f}
  .note-lbl{font-family:var(--font-mono); font-size:9px; letter-spacing:1.5px; color:var(--muted); margin:11px 0 5px; text-transform:uppercase}
  .qrow{display:grid; grid-template-columns:auto 1fr; gap:8px 11px; align-items:center; padding:8px 0}
  .qrow + .qrow{border-top:1px dashed #221913}
  .qrow .qmeta{display:flex; align-items:center; gap:9px; min-width:0}
  .qrow .qmeta label{font-size:13.5px}
  .qrow input.txt{grid-column:2; font-size:13px; padding:6px 9px}
  .synrow{display:flex;align-items:center;gap:9px;padding:5px 0}
  .synrow .n{font-family:var(--font-disp);font-size:18px;color:var(--ember-dim);width:18px;text-align:center}

  /* ---- dock: coach + ideas ---- */
  .dock{display:grid; grid-template-columns:1.25fr 1fr; gap:16px; margin-top:16px}
  @media(max-width:860px){.dock{grid-template-columns:1fr}}
  .coach .st-head{background:linear-gradient(90deg,rgba(192,57,43,.10),rgba(255,122,47,.04))}
  .clog{height:300px; overflow-y:auto; padding:14px 16px; display:flex; flex-direction:column; gap:11px; scrollbar-width:thin}
  .msg{max-width:88%; padding:9px 12px; border-radius:9px; font-size:14px}
  .msg.user{align-self:flex-end; background:#241a14; border:1px solid var(--line2); color:var(--ink)}
  .msg.coach{align-self:flex-start; background:linear-gradient(180deg,#1a1310,#140f0d); border:1px solid var(--line2); border-left:2px solid var(--ember)}
  .msg.sys{align-self:center; font-family:var(--font-mono); font-size:10.5px; letter-spacing:1px; color:var(--amber); background:transparent; border:1px dashed var(--line2)}
  .msg.coach b.name{display:block; font-family:var(--font-mono); font-size:9px; letter-spacing:2px; color:var(--ember); text-transform:uppercase; margin-bottom:4px; font-weight:700}
  .greet{color:var(--muted); font-size:13.5px; text-align:center; padding:18px 10px; line-height:1.6}
  .cinput{display:flex; gap:8px; padding:11px 12px; border-top:1px solid var(--line)}
  .cinput textarea{height:42px; min-height:42px}
  .send{flex:0 0 auto; font-family:var(--font-mono); font-size:11px; letter-spacing:1.5px; text-transform:uppercase; background:linear-gradient(180deg,var(--ember),var(--ember-dim)); color:#1a0e07; border:none; border-radius:6px; padding:0 16px; font-weight:700; cursor:pointer}
  .send:hover{filter:brightness(1.1)} .send:disabled{opacity:.5; cursor:wait}
  .typing{display:inline-flex;gap:4px;align-items:center}
  .typing i{width:5px;height:5px;border-radius:50%;background:var(--ember);animation:blink 1.1s infinite}
  .typing i:nth-child(2){animation-delay:.18s}.typing i:nth-child(3){animation-delay:.36s}
  @keyframes blink{0%,80%,100%{opacity:.25}40%{opacity:1}}

  .ideas .st-body{display:flex;flex-direction:column;gap:10px}
  .idea-add{display:flex;gap:8px}
  .ideic{display:flex;flex-direction:column;gap:7px;max-height:230px;overflow-y:auto;scrollbar-width:thin}
  .idea{display:flex;align-items:flex-start;gap:9px;background:#140f0c;border:1px solid var(--line);border-radius:6px;padding:8px 10px;font-size:13.5px;color:var(--ink2)}
  .idea .x{margin-left:auto;cursor:pointer;color:var(--faint);font-family:var(--font-mono);flex:0 0 auto}
  .idea .x:hover{color:var(--blood)}
  .idea .pin{color:var(--ember-dim);flex:0 0 auto}
  .empty{color:var(--faint);font-size:13px;font-style:italic;padding:6px 2px}

  /* ---- controls ---- */
  .controls{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px;padding-top:18px;border-top:1px solid var(--line)}
  .btn{font-family:var(--font-mono);font-size:10.5px;letter-spacing:1.5px;text-transform:uppercase;background:#191210;color:var(--ink2);border:1px solid var(--line2);border-radius:6px;padding:9px 14px;cursor:pointer;transition:.15s}
  .btn:hover{border-color:var(--ember);color:var(--gold)}
  .btn.danger:hover{border-color:var(--blood);color:#ff6b5c}
  .privacy{font-family:var(--font-mono);font-size:10px;letter-spacing:1px;color:var(--faint);margin-left:auto;align-self:center;text-transform:uppercase}

  .toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(20px);background:#1c1512;border:1px solid var(--ember-dim);color:var(--gold);font-family:var(--font-mono);font-size:12px;letter-spacing:1px;padding:11px 18px;border-radius:8px;opacity:0;transition:.3s;z-index:10000;box-shadow:var(--glow)}
  .toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
  ::-webkit-scrollbar{width:9px}::-webkit-scrollbar-thumb{background:#2e221a;border-radius:5px}
</style>

<div class="wrap">
  <div class="top">
    <div class="brand">
      <div class="reticle"><i></i></div>
      <div>
        <h1>DESIRE PROFILE <span>// MISSION CONTROL</span></h1>
        <div class="sub">Self-Discovery Command Console &nbsp;·&nbsp; Operator Eyes Only</div>
      </div>
    </div>
    <div class="meta-r">
      <div id="sysline"><span class="dot" id="sysdot"></span><b id="systxt">SYSTEM ONLINE</b></div>
      <div style="margin-top:5px">SAVE: <b id="savetxt">—</b></div>
      <div style="margin-top:3px">LAST SYNC: <b id="updtxt">—</b></div>
    </div>
  </div>

  <div class="status">
    <div class="card objective">
      <div class="lbl">▸ Current Objective</div>
      <div class="obj-title" id="objTitle">—</div>
      <div class="obj-detail" id="objDetail"></div>
    </div>
    <div class="card">
      <div class="lbl">▸ Profile Charge</div>
      <div class="gauge-wrap">
        <div class="pct"><span id="pctNum">0</span><small>%</small></div>
        <div class="segs" id="segs"></div>
      </div>
      <div class="gnote" id="chargeNote">0 / 18 OPERATIONAL STEPS COMPLETE</div>
    </div>
  </div>

  <div class="grid" id="stations"></div>

  <div class="dock">
    <section class="station coach">
      <div class="st-head">
        <div class="st-name">COMMS <b>// COACH</b></div>
        <div class="led" id="coachLed"><i></i><span id="coachStat">STANDBY</span></div>
      </div>
      <div class="clog" id="clog"></div>
      <div class="cinput">
        <textarea id="cin" placeholder="Talk to your coach — ask what's next, work a step, get unstuck…"></textarea>
        <button class="send" id="csend">SEND</button>
      </div>
    </section>

    <section class="station ideas">
      <div class="st-head">
        <div class="st-name">PARKING <b>// LOT</b></div>
        <div class="led"><i></i><span>STRAY IDEAS</span></div>
      </div>
      <div class="st-body">
        <div class="idea-add">
          <input class="txt" id="ideaIn" placeholder="Capture a thought to revisit…">
          <button class="send" id="ideaAdd" style="padding:0 14px">PIN</button>
        </div>
        <div class="ideic" id="ideic"></div>
      </div>
    </section>
  </div>

  <div class="controls">
    <button class="btn" id="exp">⤓ Export Markdown Archive</button>
    <button class="btn" id="kick">⎘ Copy Deep-Dive Kickoff Prompt</button>
    <button class="btn danger" id="reset">⟲ Reset Console</button>
    <span class="privacy">🔒 Private to you · stored to your session</span>
  </div>
</div>
<div class="toast" id="toast"></div>

<script>
//=================== STORAGE (with in-memory fallback for plain-browser preview) ===================
const HAS_STORE = (typeof window !== "undefined" && window.storage && typeof window.storage.get === "function");
const _mem = {};
const store = HAS_STORE ? window.storage : {
  async get(k){ if(k in _mem) return {key:k,value:_mem[k]}; throw new Error("nf"); },
  async set(k,v){ _mem[k]=v; return {key:k,value:v}; },
  async delete(k){ delete _mem[k]; return {key:k,deleted:true}; }
};
const KEY = "dp:state";

//=================== CONFIG ===================
const TOOLS = [
  { id:"t1", tag:"TOOL 1", name:"Erotic Journal", note:true, steps:[
    {id:"inventory", label:"Turn-on inventory (no judgment)"},
    {id:"feelings",  label:"Name the feeling under each"},
    {id:"triggers",  label:"Find what triggers the feeling"},
    {id:"delivery",  label:"Other activities + partner qualities"},
    {id:"matrix",    label:"Fill the working matrix"},
  ]},
  { id:"t2", tag:"TOOL 2", name:"Erotic Quizzes", note:true, quizzes:[
    {id:"blueprint",   label:"Jaiya's Erotic Blueprints", url:"https://theblueprintbreakthrough.com/"},
    {id:"bdsmtest",    label:"BDSM Test", url:"https://bdsmtest.org/select-mode"},
    {id:"sexualalpha", label:"Sexual Alpha BDSM Kink Test", url:"https://sexualalpha.com/bdsm-kink-test/"},
    {id:"aellabig",    label:"Aella's Big Kink Survey", url:"https://www.guidedtrack.com/programs/u4m797m/run"},
    {id:"aellaarch",   label:"Aella's BDSM Archetype Survey", url:"https://www.guidedtrack.com/programs/956secf/run"},
  ]},
  { id:"t3", tag:"TOOL 3", name:"Sexual Disclosure", note:true, steps:[
    {id:"person",    label:"Choose a safe person / book a pro"},
    {id:"container", label:"Set the container: confidential, no judgment"},
    {id:"block",     label:"Block an unhurried hour+"},
    {id:"done",      label:"Complete a disclosure"},
    {id:"aftercare", label:"Aftercare + journal the aftermath"},
  ]},
  { id:"t4", tag:"TOOL 4", name:"Sex Menu", note:true, steps:[
    {id:"grab",  label:"Grab the 350+ act template", url:"https://www.brandonthedom.com/resources/sex-menu-template"},
    {id:"fill",  label:"Fill it out honestly"},
    {id:"share", label:"Share + discuss (optional)"},
  ]},
  { id:"syn", tag:"FINAL", name:"Synthesis · Your Profile", synthesis:true },
];
const OBJ_DETAIL = {
  "t1.inventory":"Brain-dump every turn-on — fantasies, favorite experiences, mental images, porn you return to. <em>No editing. No origin-hunting.</em>",
  "t1.feelings":"Take each turn-on and name the <em>feeling</em> it gives you. The feeling is the real target.",
  "t1.triggers":"For each, pin the trigger — setting, partner, act, the thing giving it the charge.",
  "t1.delivery":"List other activities AND partner qualities that hit the <em>same feeling</em>. This is where options open up.",
  "t1.matrix":"Lock it into the matrix: turn-on → feeling → trigger → delivery.",
  "t2.blueprint":"Take the Blueprint quiz — find your arousal type before the rest.",
  "t2.bdsmtest":"Run the classic BDSM Test for your role map.",
  "t2.sexualalpha":"Take Sexual Alpha for deeper archetype explanations.",
  "t2.aellabig":"Aella's Big Kink Survey — a guided tour of everything out there + your kinkiness percentile.",
  "t2.aellaarch":"Aella's Archetype Survey — your preferred dynamic and partner fit.",
  "t3.person":"Pick someone you deeply trust — or a therapist/coach. Conditions matter more than speed.",
  "t3.container":"Name the rules out loud: confidential, no judgment, no fixing — just mirroring.",
  "t3.block":"Carve out an unhurried hour-plus. No clock pressure.",
  "t3.done":"Do the disclosure: history + feelings, desires, and any shame you carry.",
  "t3.aftercare":"Ground yourself after, then journal what surfaced that you didn't expect.",
  "t4.grab":"Pull the 350+ act sex menu template — don't build from scratch.",
  "t4.fill":"Rate every act with notes. Be honest; don't answer to please anyone.",
  "t4.share":"Optional: trade menus with a partner and discuss with curiosity.",
};
const ALL_IDS = []; TOOLS.forEach(t=>{ (t.steps||[]).forEach(s=>ALL_IDS.push(t.id+"."+s.id)); (t.quizzes||[]).forEach(q=>ALL_IDS.push(t.id+"."+q.id)); });

//=================== STATE ===================
function fresh(){ return { done:{}, notes:{t1:"",t2:"",t3:"",t4:""}, quiz:{}, syn:{feel:["","","","",""],delivery:"",limits:""}, ideas:[], coach:[], created:Date.now(), updated:Date.now() }; }
let state = fresh();
let saveTimer=null;
function scheduleSave(){ setSave("saving…"); clearTimeout(saveTimer); saveTimer=setTimeout(saveNow,500); }
async function saveNow(){
  state.updated=Date.now();
  try{ await store.set(KEY, JSON.stringify(state)); setSave("saved ✓"); document.getElementById("updtxt").textContent=fmt(state.updated); }
  catch(e){ setSave("error", true); }
}
function setSave(t,err){ const el=document.getElementById("savetxt"); el.textContent=t; el.style.color = err? "#ff6b5c" : "var(--ink2)"; }
function fmt(ts){ const d=new Date(ts); return d.toLocaleString([], {month:"short",day:"numeric",hour:"2-digit",minute:"2-digit"}); }

//=================== RENDER: stations ===================
function esc(s){ return (s||"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c])); }
function buildStations(){
  const host=document.getElementById("stations");
  host.innerHTML = TOOLS.map((t,i)=>{
    let body="";
    if(t.steps){
      body += t.steps.map(s=>{
        const id=t.id+"."+s.id, on=!!state.done[id];
        const link = s.url? ` <a class="go" href="${s.url}" target="_blank" rel="noopener">OPEN ↗</a>`:"";
        return `<div class="row ${on?'done':''}" data-row="${id}">
          <div class="tog ${on?'on':''}" data-tog="${id}" role="checkbox" aria-checked="${on}"></div>
          <label data-tog="${id}">${esc(s.label)}</label>${link}</div>`;
      }).join("");
    }
    if(t.quizzes){
      body += t.quizzes.map(q=>{
        const id=t.id+"."+q.id, on=!!state.done[id];
        return `<div class="qrow" data-row="${id}">
          <div class="qmeta">
            <div class="tog ${on?'on':''}" data-tog="${id}"></div>
            <label data-tog="${id}" class="${on?'':''}">${esc(q.label)}</label>
            <a class="go" href="${q.url}" target="_blank" rel="noopener">TAKE ↗</a>
          </div>
          <input class="txt" data-quiz="${q.id}" placeholder="result / key takeaways…" value="${esc(state.quiz[q.id]||"")}">
        </div>`;
      }).join("");
    }
    if(t.note){
      body += `<div class="note-lbl">▸ Findings / notes</div>
        <textarea data-note="${t.id}" rows="3" placeholder="capture what you found here…">${esc(state.notes[t.id]||"")}</textarea>`;
    }
    if(t.synthesis){
      body += `<div class="note-lbl">▸ Core feelings (ranked)</div>` +
        state.syn.feel.map((v,k)=>`<div class="synrow"><span class="n">${k+1}</span><input class="txt" data-feel="${k}" placeholder="${k===0?'the feeling you chase most…':'…'}" value="${esc(v)}"></div>`).join("") +
        `<div class="note-lbl">▸ Feeling → delivery map</div><textarea data-syn="delivery" rows="3" placeholder="for each core feeling: triggers · green-light activities · partner qualities…">${esc(state.syn.delivery)}</textarea>` +
        `<div class="note-lbl">▸ Limits & edges</div><textarea data-syn="limits" rows="2" placeholder="hard limits · soft limits (conditions) · curiosities · mind-only…">${esc(state.syn.limits)}</textarea>`;
    }
    return `<section class="station" style="animation-delay:${i*70}ms">
      <div class="st-head">
        <div class="st-name"><b>${t.tag} //</b> ${esc(t.name)}</div>
        <div class="led" data-led="${t.id}"><i></i><span>—</span></div>
      </div>
      <div class="st-body">${body}</div>
    </section>`;
  }).join("");

  // wire (event delegation)
  host.addEventListener("click", e=>{
    const tg=e.target.closest("[data-tog]"); if(tg && !e.target.closest("a")){ toggle(tg.getAttribute("data-tog")); }
  });
  host.addEventListener("input", e=>{
    const el=e.target;
    if(el.dataset.note!==undefined){ state.notes[el.dataset.note]=el.value; scheduleSave(); }
    else if(el.dataset.quiz!==undefined){ state.quiz[el.dataset.quiz]=el.value; scheduleSave(); }
    else if(el.dataset.feel!==undefined){ state.syn.feel[+el.dataset.feel]=el.value; scheduleSave(); updateHeader(); }
    else if(el.dataset.syn!==undefined){ state.syn[el.dataset.syn]=el.value; scheduleSave(); }
  });
  refreshLeds();
}
function toggle(id){
  state.done[id]=!state.done[id];
  document.querySelectorAll(`[data-row="${CSS.escape(id)}"]`).forEach(r=>r.classList.toggle("done", !!state.done[id]));
  document.querySelectorAll(`[data-tog="${CSS.escape(id)}"]`).forEach(t=>{ if(t.classList.contains("tog")) t.classList.toggle("on", !!state.done[id]); });
  scheduleSave(); updateHeader(); refreshLeds();
}
function refreshLeds(){
  TOOLS.forEach(t=>{
    const led=document.querySelector(`[data-led="${t.id}"]`); if(!led) return;
    let total=0, dn=0;
    (t.steps||[]).forEach(s=>{ total++; if(state.done[t.id+"."+s.id]) dn++; });
    (t.quizzes||[]).forEach(q=>{ total++; if(state.done[t.id+"."+q.id]) dn++; });
    if(t.synthesis){ total=3; dn=(state.syn.feel.filter(Boolean).length>=3?1:0)+(state.syn.delivery.trim()?1:0)+(state.syn.limits.trim()?1:0); }
    led.classList.remove("part","full");
    if(dn>=total && total>0) led.classList.add("full");
    else if(dn>0) led.classList.add("part");
    led.querySelector("span").textContent = dn>=total&&total>0 ? "COMPLETE" : dn>0 ? dn+"/"+total : "STANDBY";
  });
}

//=================== HEADER: progress + objective ===================
function doneCount(){ return ALL_IDS.filter(id=>state.done[id]).length; }
function updateHeader(){
  const dn=doneCount(), total=ALL_IDS.length, pct=Math.round(dn/total*100);
  document.getElementById("pctNum").textContent=pct;
  document.getElementById("chargeNote").textContent=`${dn} / ${total} OPERATIONAL STEPS COMPLETE`;
  // segments
  const segs=document.getElementById("segs"); if(segs.children.length!==total){ segs.innerHTML=Array.from({length:total},()=>'<div class="seg"></div>').join(""); }
  Array.from(segs.children).forEach((s,i)=>s.classList.toggle("on", i<dn));
  // objective
  let obj=null;
  for(const t of TOOLS){
    for(const s of (t.steps||[])){ const id=t.id+"."+s.id; if(!state.done[id]){ obj={id,label:s.label,tag:t.tag}; break; } }
    if(obj) break;
    for(const q of (t.quizzes||[])){ const id=t.id+"."+q.id; if(!state.done[id]){ obj={id,label:q.label,tag:t.tag}; break; } }
    if(obj) break;
  }
  const synReady=state.syn.feel.filter(Boolean).length>=3 && state.syn.delivery.trim();
  if(!obj && !synReady){ document.getElementById("objTitle").textContent="Assemble your profile"; document.getElementById("objDetail").innerHTML="All 18 steps done. Drop into <em>Synthesis</em> — rank your core feelings and map each to its triggers, activities, and partner qualities."; }
  else if(!obj && synReady){ document.getElementById("objTitle").textContent="Maintain & deepen"; document.getElementById("objDetail").innerHTML="Profile is built. Revisit in <em>~6 months</em>, or deepen any single tool. Nice work, Operator."; }
  else { document.getElementById("objTitle").textContent=obj.label; document.getElementById("objDetail").innerHTML=(OBJ_DETAIL[obj.id]||"Next step in your sequence."); }
}

//=================== IDEAS ===================
function renderIdeas(){
  const host=document.getElementById("ideic");
  if(!state.ideas.length){ host.innerHTML='<div class="empty">Nothing parked yet. Drop stray thoughts here so they don\'t derail the work.</div>'; return; }
  host.innerHTML=state.ideas.map(it=>`<div class="idea"><span class="pin">▹</span><span>${esc(it.text)}</span><span class="x" data-x="${it.id}">✕</span></div>`).join("");
  host.querySelectorAll("[data-x]").forEach(x=>x.onclick=()=>{ state.ideas=state.ideas.filter(i=>i.id!==x.dataset.x); renderIdeas(); scheduleSave(); });
}
function addIdea(){
  const inp=document.getElementById("ideaIn"); const v=inp.value.trim(); if(!v) return;
  state.ideas.unshift({id:"i"+Date.now(),text:v}); inp.value=""; renderIdeas(); scheduleSave();
}

//=================== COACH (Anthropic API) ===================
function coachSystem(){
  let s = `You are the embedded coach inside a private "Desire Profile" self-discovery dashboard, working with one adult user.

VOICE: Blunt, no-bullshit, and warm. Frank and sex-positive like a seasoned, unembarrassed sex educator — confident, knowing, a little dry humor and swagger (the Nina Hartley register). You name sexual things plainly, never clinically stiff, never squeamish, never preachy. You don't shame, moralize, or coddle. You're direct: name the next move and why it matters.

SCOPE: You are a self-discovery COACH, not an erotica writer or roleplay partner. Guide the user to do their own introspective work — do NOT produce explicit/pornographic content or sexual roleplay. Keep replies SHORT: 2-5 sentences, ONE step at a time, at most one question per reply.

CORE METHOD — feelings first: every turn-on decodes to a FEELING; the feeling is the real target, and acts/partners are interchangeable ways to reach it. Chain: turn-on -> feeling -> trigger -> delivery (activities + partner qualities).

THE 4 TOOLS (freeform — read the STATE below, then pick the single highest-leverage next move):
1) Erotic Journal: list turn-ons (no judgment) -> name the feeling each gives -> find the trigger -> list other activities + partner qualities that hit the same feeling -> fill the matrix.
2) Erotic Quizzes (outside lenses): Jaiya's Erotic Blueprints, BDSM Test, Sexual Alpha BDSM test, Aella's Big Kink Survey, Aella's BDSM Archetype Survey. Take them, then find patterns.
3) Sexual Disclosure: with a deeply trusted person or a therapist/coach — disclose history+feelings, desires/kinks, and any shame. It builds a reference experience that dissolves shame.
4) Sex Menu (Yes/No/Maybe): rate 350+ acts with notes — the communication capstone.
Then SYNTHESIS: rank core feelings, map each to triggers/activities/partner qualities, set limits.

PRINCIPLES: no judgment, no origin-hunting; a fantasy is never a commitment (mind-only is valid); don't go zero-to-100 (approach intense feelings via milder acts first); consent + safety for anything acted on; observer stance toward shame; self-compassion.

When the user finishes something, tell them to check it off in the dashboard. Use the STATE so they never repeat themselves.

CURRENT STATE:\n`;
  TOOLS.forEach(t=>{
    if(t.synthesis){ s+=`- Synthesis: ${state.syn.feel.filter(Boolean).length} core feelings named; delivery map ${state.syn.delivery.trim()?"started":"empty"}; limits ${state.syn.limits.trim()?"started":"empty"}.\n`; return; }
    const items=(t.steps||t.quizzes||[]); const dn=items.filter(x=>state.done[t.id+"."+x.id]).length;
    s+=`- ${t.tag} ${t.name}: ${dn}/${items.length} done.\n`;
  });
  const dn=doneCount();
  s+=`Overall: ${dn}/${ALL_IDS.length} steps. `;
  if(state.ideas.length) s+=`Parked ideas: ${state.ideas.map(i=>i.text).join("; ")}. `;
  return s;
}
let coaching=false;
function renderCoach(){
  const log=document.getElementById("clog");
  if(!state.coach.length){
    log.innerHTML=`<div class="greet">No transmissions yet.<br>Ask <b style="color:var(--ember)">"where do I start?"</b> — or just start talking. I'll meet you wherever you are and we'll take it one step at a time.</div>`;
    return;
  }
  log.innerHTML=state.coach.map(m=>{
    if(m.role==="sys") return `<div class="msg sys">${esc(m.content)}</div>`;
    if(m.role==="user") return `<div class="msg user">${esc(m.content)}</div>`;
    return `<div class="msg coach"><b class="name">COACH</b>${esc(m.content)}</div>`;
  }).join("");
  log.scrollTop=log.scrollHeight;
}
function setCoachLed(on){ const l=document.getElementById("coachLed"); l.classList.toggle("part",on); document.getElementById("coachStat").textContent=on?"TRANSMITTING":"STANDBY"; }
async function sendCoach(){
  if(coaching) return;
  const inp=document.getElementById("cin"); const text=inp.value.trim(); if(!text) return;
  inp.value=""; state.coach.push({role:"user",content:text}); renderCoach(); scheduleSave();
  coaching=true; document.getElementById("csend").disabled=true; setCoachLed(true);
  const log=document.getElementById("clog");
  const t=document.createElement("div"); t.className="msg coach"; t.innerHTML='<b class="name">COACH</b><span class="typing"><i></i><i></i><i></i></span>'; log.appendChild(t); log.scrollTop=log.scrollHeight;
  try{
    const hist=state.coach.filter(m=>m.role!=="sys").slice(-16).map(m=>({role:m.role,content:m.content}));
    const res=await fetch("https://api.anthropic.com/v1/messages",{
      method:"POST", headers:{"Content-Type":"application/json"},
      body:JSON.stringify({ model:"claude-sonnet-4-20250514", max_tokens:1000, system:coachSystem(), messages:hist })
    });
    if(!res.ok) throw new Error("HTTP "+res.status);
    const data=await res.json();
    const reply=(data.content||[]).filter(b=>b.type==="text").map(b=>b.text).join("\n").trim() || "(no reply)";
    t.remove(); state.coach.push({role:"coach",content:reply}); renderCoach(); saveNow();
  }catch(err){
    t.remove();
    state.coach.push({role:"sys",content:"⚠ Coach link offline. The tracker, notes, ideas & export all still work — and you can run a full deep-dive in a Claude Project chat. ("+err.message+")"});
    renderCoach(); saveNow();
  }finally{ coaching=false; document.getElementById("csend").disabled=false; setCoachLed(false); }
}

//=================== EXPORT / KICKOFF / RESET ===================
function buildMarkdown(){
  const L=[]; L.push("# Desire Profile — Snapshot"); L.push("");
  L.push("> Exported "+new Date().toLocaleString()+" · charge "+Math.round(doneCount()/ALL_IDS.length*100)+"%"); L.push("");
  TOOLS.forEach(t=>{
    L.push("## "+t.tag+" — "+t.name);
    (t.steps||[]).forEach(s=>L.push(`- [${state.done[t.id+"."+s.id]?"x":" "}] ${s.label}`));
    (t.quizzes||[]).forEach(q=>{ L.push(`- [${state.done[t.id+"."+q.id]?"x":" "}] ${q.label}${state.quiz[q.id]?" — "+state.quiz[q.id]:""}`); });
    if(t.note && state.notes[t.id]&&state.notes[t.id].trim()){ L.push(""); L.push("**Notes:** "+state.notes[t.id]); }
    if(t.synthesis){
      const f=state.syn.feel.filter(Boolean); if(f.length){ L.push("**Core feelings (ranked):**"); f.forEach((x,i)=>L.push(`${i+1}. ${x}`)); }
      if(state.syn.delivery.trim()){ L.push(""); L.push("**Feeling → delivery:** "+state.syn.delivery); }
      if(state.syn.limits.trim()){ L.push(""); L.push("**Limits & edges:** "+state.syn.limits); }
    }
    L.push("");
  });
  if(state.ideas.length){ L.push("## Parking Lot"); state.ideas.forEach(i=>L.push("- "+i.text)); }
  return L.join("\n");
}
function download(){
  const blob=new Blob([buildMarkdown()],{type:"text/markdown"}); const url=URL.createObjectURL(blob);
  const a=document.createElement("a"); a.href=url; a.download="desire-profile-snapshot.md"; a.click(); URL.revokeObjectURL(url); toast("Markdown archive exported");
}
function kickoff(){
  const dn=doneCount(); let next=document.getElementById("objTitle").textContent;
  const txt=`I'm working through my Desire Profile and want a deep-dive coaching session. Here's where I am:\n\n`+
    buildMarkdown().replace(/^# .*\n/,"")+`\n\nMy current objective is: "${next}". Coach me through it one step at a time — blunt, warm, frank, no hand-holding. Start by orienting me, then give me the first concrete move.`;
  (navigator.clipboard?navigator.clipboard.writeText(txt):Promise.reject()).then(()=>toast("Kickoff prompt copied — paste it into a Project chat")).catch(()=>{ window.prompt("Copy this kickoff prompt:",txt); });
}
async function resetAll(){
  if(!confirm("Wipe the console? This clears all progress, notes, ideas and coach history. Export first if you want a copy.")) return;
  try{ await store.delete(KEY); }catch(e){}
  state=fresh(); buildStations(); renderIdeas(); renderCoach(); updateHeader(); refreshLeds(); saveNow(); toast("Console reset");
}
function toast(msg){ const el=document.getElementById("toast"); el.textContent=msg; el.classList.add("show"); clearTimeout(el._t); el._t=setTimeout(()=>el.classList.remove("show"),2600); }

//=================== INIT ===================
async function init(){
  // system status line
  const dot=document.getElementById("sysdot"), txt=document.getElementById("systxt");
  if(!HAS_STORE){ dot.className="dot warn"; txt.textContent="SESSION-ONLY (NO PERSISTENCE)"; }
  let loaded=null;
  try{ const r=await store.get(KEY); if(r&&r.value) loaded=JSON.parse(r.value); }catch(e){}
  if(loaded){ state=Object.assign(fresh(),loaded); state.notes=Object.assign({t1:"",t2:"",t3:"",t4:""},loaded.notes||{}); state.syn=Object.assign({feel:["","","","",""],delivery:"",limits:""},loaded.syn||{}); document.getElementById("updtxt").textContent=fmt(state.updated); setSave("loaded ✓"); }
  else { await saveNow(); }

  buildStations(); renderIdeas(); renderCoach(); updateHeader(); refreshLeds();

  document.getElementById("csend").onclick=sendCoach;
  document.getElementById("cin").addEventListener("keydown",e=>{ if(e.key==="Enter"&&!e.shiftKey){ e.preventDefault(); sendCoach(); } });
  document.getElementById("ideaAdd").onclick=addIdea;
  document.getElementById("ideaIn").addEventListener("keydown",e=>{ if(e.key==="Enter"){ e.preventDefault(); addIdea(); } });
  document.getElementById("exp").onclick=download;
  document.getElementById("kick").onclick=kickoff;
  document.getElementById("reset").onclick=resetAll;
}
init();
</script>
