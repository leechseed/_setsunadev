---
original_path: "/mnt/user-data/outputs/turn-on-tag-board.html"
source_conversation: "Unified profiler UI with markdown export"
created: 2026-07-15
trunk: BOTH
kind: generated-file
---

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Turn-On Tag Board · Industry Pass</title>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=JetBrains+Mono:wght@400;600&family=Spectral:ital,wght@0,400;1,400@display=swap" rel="stylesheet">
<style>
:root{--bg:#0d0a08;--panel:#171210;--panel2:#1f1815;--line:#3a2c22;--ember:#d97b3f;--ember-hot:#f0a05c;--bone:#e8ddd0;--dim:#9a8a78;--faint:#6b5d4f}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--bone);font-family:'JetBrains Mono',monospace;padding:20px 14px 90px;max-width:760px;margin:0 auto}
h1{font-family:'Bebas Neue',sans-serif;font-size:34px;letter-spacing:2px;color:var(--ember-hot)}
.sub{font-family:'Spectral',serif;font-style:italic;color:var(--dim);font-size:15px;margin:4px 0 22px}
.sec{margin:0 0 26px}
.shead{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid var(--line);padding-bottom:6px;margin-bottom:10px}
.st{font-family:'Bebas Neue',sans-serif;font-size:19px;letter-spacing:1.5px;color:var(--bone)}
.sn{font-size:11px;color:var(--faint)}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{font-family:'JetBrains Mono',monospace;font-size:12.5px;line-height:1.35;padding:9px 13px;border-radius:999px;border:1px solid var(--line);background:var(--panel);color:var(--dim);cursor:pointer;transition:all .12s}
.chip:hover{border-color:var(--ember);color:var(--bone)}
.chip.on{background:#2b1c10;border-color:var(--ember);color:var(--ember-hot);font-weight:600}
.bar{position:fixed;left:0;right:0;bottom:0;background:var(--panel2);border-top:1px solid var(--line);padding:12px 14px;display:flex;align-items:center;gap:10px}
.bar-in{max-width:760px;margin:0 auto;display:flex;align-items:center;gap:10px;width:100%}
.total{font-size:14px;font-weight:600;color:var(--ember-hot);flex:1}
button.act{font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600;letter-spacing:.5px;padding:10px 16px;border-radius:6px;border:1px solid var(--ember);background:transparent;color:var(--ember-hot);cursor:pointer}
button.act:hover{background:#2b1c10}
button.ghost{border-color:var(--line);color:var(--faint)}
.note{font-family:'Spectral',serif;font-style:italic;font-size:13.5px;color:var(--faint);margin-top:30px;line-height:1.6}
textarea#out{position:absolute;left:-9999px}
</style>
</head>
<body>
<h1>TURN-ON TAG BOARD</h1>
<div class="sub">Industry pass · 122 tags · 12 lanes · no limit. Tap everything that sparks — even a flicker counts. A tap is data, not a commitment.</div>
<div id="root"></div>
<div class="note">Everything here is 18+ by definition. Fantasy ≠ commitment — mind-only is a valid permanent home for any of it. When done: <b>Copy picks</b>, then paste into your coach chat or the Tool 1 notes field in Mission Control.</div>
<textarea id="out" aria-hidden="true"></textarea>
<div class="bar"><div class="bar-in">
<span class="total" id="total">0 picked</span>
<button class="act ghost" id="clear">CLEAR</button>
<button class="act" id="copy">COPY PICKS</button>
</div></div>
<script>
const DATA=[
["Content lanes",["Straight (M/F)","Lesbian (F/F)","Gay (M/M)","Bisexual / MMF energy","Trans women","Trans men","Trans × trans","Nonbinary / genderqueer","Solo women","Solo men"]],
["Bodies & builds",["Curvy / thick","BBW","Petite / slim (adult)","Athletic / toned","Muscular / jacked","Bears (big, hairy men)","Twinks (slim, smooth men)","Jocks","Big breasts","Small breasts","Big ass","Big dick","Body hair / natural"]],
["Age & archetypes (all 18+)",["MILF","Mature / 50+","Cougar × younger man","Daddy / DILF","Age gap (adults)","College-age (18+)","Girl/boy next door","Married / wedding-ring energy"]],
["Power exchange",["Dominant men","Dominant women (femdom)","Being dominated","Bondage (rope, cuffs)","Discipline / punishment","Top energy","Bottom energy","Verse / switching","Free use (roleplay)","Consensual non-consent (roleplay)"]],
["Rough & edge",["Rough sex","Spanking","Hair pulling","Choking / breath play","Face slapping","Being degraded","Degrading a partner","Humiliation","Gagging / face-fucking","Biting / marking"]],
["Group & sharing",["Threesome (two women)","Threesome (two men)","Foursome / group","Gangbang","Orgy / play party","Double penetration","Cuckolding / being cucked","Hotwife / sharing a partner","Swinging / swaps","Strangers / anonymous"]],
["Watching & showing",["Voyeur (watching others)","Exhibitionist (being watched)","Public / semi-public","Amateur / homemade","POV","Casting / audition setups","Livecam shows","Being filmed","Mirrors"]],
["Scenarios & roleplay",["Step-family roleplay (fictional)","Boss / employee","Teacher / professor (adults)","Doctor / nurse / exam","Massage that escalates","Cheating / affair fantasy","Escort / client roleplay","Uniforms (military, cops)","Maid / service roleplay","Hotel / travel hookup","Office after-hours"]],
["Fetishwear & body focus",["Lingerie","Stockings / pantyhose","High heels","Leather","Latex / PVC","Feet","Armpits / sweat","Jockstraps / underwear","Crossdressing","Cosplay / costumes","Glasses / librarian energy"]],
["Oral & hands",["Giving oral (on him)","Giving oral (on her)","Receiving oral","Deepthroat","Rimming (giving or getting)","Face-sitting","Handjobs / fingering","Mutual masturbation","Edging / orgasm control"]],
["Anal & toys",["Anal (giving)","Anal (receiving)","Pegging","Strap-on","Dildos / vibrators","Plugs","Prostate play","Fisting","Machines"]],
["Finish, fluids & misc kink",["Facials","Creampie","Swallowing","Squirting","Cum play","Breeding / raw (fantasy)","Watersports","Praise kink","Dirty talk","Pet play","Lactation","Sexting / phone sex"]]
];
const KEY="dp:tagboard:v1";
let picked=new Set();
try{const s=localStorage.getItem(KEY);if(s)picked=new Set(JSON.parse(s))}catch(e){}
const root=document.getElementById("root");
DATA.forEach((s,si)=>{
const d=document.createElement("div");d.className="sec";
const h=document.createElement("div");h.className="shead";
const t=document.createElement("span");t.className="st";t.textContent=String(si+1).padStart(2,"0")+" · "+s[0];
const n=document.createElement("span");n.className="sn";n.id="n"+si;
h.append(t,n);d.append(h);
const c=document.createElement("div");c.className="chips";
s[1].forEach(tag=>{
const b=document.createElement("button");b.className="chip";b.type="button";b.textContent=tag;
const k=si+"::"+tag;if(picked.has(k))b.classList.add("on");
b.onclick=()=>{picked.has(k)?(picked.delete(k),b.classList.remove("on")):(picked.add(k),b.classList.add("on"));save();refresh()};
c.append(b)});
d.append(c);root.append(d)});
function save(){try{localStorage.setItem(KEY,JSON.stringify([...picked]))}catch(e){}}
function refresh(){
document.getElementById("total").textContent=picked.size+" picked";
DATA.forEach((s,si)=>{const k=[...picked].filter(p=>p.startsWith(si+"::")).length;
document.getElementById("n"+si).textContent=k+" / "+s[1].length})}
function buildOut(){
let out="Turn-on inventory — industry-tag pass ("+picked.size+" picks):\n";
DATA.forEach((s,si)=>{const items=s[1].filter(t=>picked.has(si+"::"+t));
if(items.length)out+="\n"+s[0]+": "+items.join("; ")});
return out}
document.getElementById("copy").onclick=async()=>{
const txt=buildOut(),btn=document.getElementById("copy");
try{await navigator.clipboard.writeText(txt)}catch(e){
const ta=document.getElementById("out");ta.value=txt;ta.select();document.execCommand("copy")}
btn.textContent="COPIED ✓";setTimeout(()=>btn.textContent="COPY PICKS",1600)};
document.getElementById("clear").onclick=()=>{
if(!picked.size||confirm("Clear all "+picked.size+" picks?")){picked.clear();save();
document.querySelectorAll(".chip.on").forEach(b=>b.classList.remove("on"));refresh()}};
refresh();
</script>
</body>
</html>
