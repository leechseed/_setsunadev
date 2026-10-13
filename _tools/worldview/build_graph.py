#!/usr/bin/env python3
"""Build _PRIVATE/reference/fabula/fabula-graph.html from _tools/worldview/fabula.json.
Stdlib only. d3 7.9.0 from cdnjs. Three views (keys 1-3), properties sidebar, highlight-path mode."""
import json, sys, datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "_tools/worldview/fabula.json"
OUT = ROOT / "_PRIVATE/reference/fabula/fabula-graph.html"

TEMPLATE = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Fabula Graph</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Barlow+Condensed:wght@600;700&family=IBM+Plex+Mono:wght@400&display=swap">
<style>
:root{--bg:#121110;--panel:#1B1A18;--line:#34312d;--tx:#ECE7DF;--mut:#A39C91;--acc:#FF5A1F;
--system:#FF5A1F;--era:#F2C94C;--character:#6FB7E9;--perspective:#B999EE;--place:#62C48A;--faction:#EE82A5;--event:#9A9488;--layer:#7d776d}
*{box-sizing:border-box}
html,body{margin:0;height:100%;background:var(--bg);color:var(--tx);font-family:'Atkinson Hyperlegible',system-ui,sans-serif;overflow:hidden}
#bar{height:44px;display:flex;align-items:center;gap:10px;padding:0 12px;background:var(--panel);border-bottom:1px solid var(--line)}
#bar h1{font:700 20px 'Barlow Condensed',sans-serif;letter-spacing:.04em;text-transform:uppercase;margin:0;color:var(--acc);white-space:nowrap}
#types{display:flex;gap:5px;overflow-x:auto;flex:1;scrollbar-width:none}
.chip{font:400 11px 'IBM Plex Mono',monospace;color:var(--mut);background:none;border:1px solid var(--line);border-radius:14px;padding:3px 8px;cursor:pointer;white-space:nowrap}
.chip i{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:5px;background:var(--c)}
.chip[aria-pressed=true]{color:var(--tx);border-color:var(--c)}
button:focus-visible,select:focus-visible,#q:focus-visible,.nd:focus-visible{outline:2px solid var(--acc);outline-offset:2px}
#q,#path{background:var(--bg);color:var(--tx);border:1px solid var(--line);border-radius:6px;padding:4px 8px;font:13px 'Atkinson Hyperlegible',sans-serif}
#q{width:140px}#path{max-width:150px}
#rail{position:absolute;top:44px;left:0;bottom:28px;width:58px;background:var(--panel);border-right:1px solid var(--line);display:flex;flex-direction:column;gap:6px;padding:8px 5px}
#rail button{background:none;border:1px solid var(--line);border-radius:8px;color:var(--mut);padding:6px 2px;cursor:pointer;font:400 10px 'IBM Plex Mono',monospace;line-height:1.3}
#rail button b{display:block;font:700 18px 'Barlow Condensed',sans-serif;color:var(--tx)}
#rail button[aria-pressed=true]{border-color:var(--acc);color:var(--acc)}
#rail button[aria-pressed=true] b{color:var(--acc)}
#stage{position:absolute;top:44px;left:58px;right:0;bottom:28px}
svg{width:100%;height:100%;display:block;position:absolute;inset:0}
svg.off{display:none}
.lk{stroke:#5a554e;stroke-opacity:.55}
.lk.hi{stroke:var(--acc);stroke-opacity:1}
.pth{stroke:var(--acc);stroke-width:3;fill:none;stroke-linecap:round;stroke-linejoin:round}
.nd{cursor:pointer}
.nd .sh{stroke:var(--bg);stroke-width:1.5}
.nd.sel .sh{stroke:#fff;stroke-width:2.5}
.nd text{font:12px 'Atkinson Hyperlegible',sans-serif;fill:var(--tx);paint-order:stroke;stroke:var(--bg);stroke-width:3px;pointer-events:none}
.nd.onpath .sh{stroke:var(--acc);stroke-width:3}
.dim{opacity:.1}
.band rect{fill:#171614;stroke:var(--line)}
.band text.bt{font:700 15px 'Barlow Condensed',sans-serif;fill:var(--era);letter-spacing:.04em}
.band text.bs{font:400 10px 'IBM Plex Mono',monospace;fill:var(--mut)}
.band line{stroke:var(--line);stroke-dasharray:4 4}
.tl text.nm{font:11px 'Atkinson Hyperlegible',sans-serif}
.tree .tl{stroke:#5a554e;fill:none}
.tree text{font:12px 'Atkinson Hyperlegible',sans-serif;fill:var(--tx)}
.tree .tg{cursor:pointer}
#tip{position:fixed;pointer-events:none;background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:8px 10px;max-width:300px;font-size:13px;line-height:1.35;display:none;z-index:5}
#tip b{font:700 15px 'Barlow Condensed',sans-serif;letter-spacing:.03em}
#tip em{display:block;font:400 11px 'IBM Plex Mono',monospace;color:var(--mut);font-style:normal;margin-bottom:3px}
#side{position:absolute;top:8px;right:10px;width:310px;max-height:calc(100% - 16px);overflow:auto;background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:12px;display:none;font-size:14px;line-height:1.4;z-index:4}
#side h2{font:700 21px 'Barlow Condensed',sans-serif;margin:0 0 6px}
#side .x{position:absolute;top:6px;right:8px;background:none;border:0;color:var(--mut);font-size:20px;cursor:pointer}
#side dl{margin:8px 0;display:grid;grid-template-columns:62px 1fr;gap:3px 8px}
#side dt{font:400 11px 'IBM Plex Mono',monospace;color:var(--mut)}
#side dd{margin:0;word-break:break-word}
#side dd.mono{font:400 11px 'IBM Plex Mono',monospace}
#side ul{margin:6px 0 0;padding:0;list-style:none}
#side li{padding:2px 0}
#side li a{color:var(--tx);cursor:pointer;text-decoration:underline;text-decoration-color:var(--line)}
#side li small{color:var(--mut);font:400 10px 'IBM Plex Mono',monospace}
#side .go{margin-top:8px;background:var(--acc);color:#121110;border:0;border-radius:6px;padding:5px 10px;font:700 13px 'Atkinson Hyperlegible',sans-serif;cursor:pointer}
#foot{position:absolute;bottom:0;left:0;right:0;height:28px;line-height:28px;padding:0 14px;border-top:1px solid var(--line);background:var(--panel);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font:400 11px 'IBM Plex Mono',monospace;color:var(--mut)}
@media(max-width:700px){#q{width:90px}#path{max-width:90px}#bar h1{font-size:16px}#side{width:calc(100% - 20px)}}
</style>
</head>
<body>
<div id="bar"><h1>Fabula Graph</h1><div id="types" role="group" aria-label="Filter by type"></div>
<select id="path" aria-label="Highlight path of a character"></select>
<input id="q" type="search" placeholder="Search ( / )" aria-label="Search nodes"></div>
<div id="rail" role="group" aria-label="Views"></div>
<div id="stage"><svg id="v1"></svg><svg id="v2" class="off"></svg><svg id="v3" class="off tree"></svg>
<aside id="side" aria-live="polite"></aside></div>
<div id="tip"></div>
<div id="foot"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js"></script>
<script>
const DATA=__DATA__;
const BUILT="__BUILT__";
const TYPES=['system','era','character','perspective','place','faction','event'];
const COL=t=>getComputedStyle(document.documentElement).getPropertyValue('--'+t).trim()||'#888';
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const on=new Set(TYPES);let sel=null,pathChar=null,query='',view=1;
const nodes=DATA.nodes.map(d=>({...d})),byId=new Map(nodes.map(d=>[d.id,d]));
const layerNodes=DATA.layers.map(l=>({id:l.id,label:l.label,type:'layer',desc:l.desc,source:l.source,line:l.line,era:null,year:null}));
const lookup=id=>byId.get(id)||layerNodes.find(l=>l.id===id);
const links=DATA.links.map(d=>({source:d.a,target:d.b,kind:d.kind,w:d.w,src:d.src}));
const nb=new Map(nodes.map(d=>[d.id,new Set()]));
links.forEach(l=>{nb.get(l.source).add(l.target);nb.get(l.target).add(l.source)});
nodes.forEach(d=>d.deg=nb.get(d.id).size);
const sid=x=>typeof x==='object'?x.id:x;
const eraName=id=>id?(byId.get(id)||{}).label:'';
const fmtSrc=d=>d.source?d.source+':'+d.line:'(no source)';
const matches=d=>!query||(d.label+' '+(d.desc||'')).toLowerCase().includes(query);
const vis=d=>on.has(d.type)&&matches(d);
// ---- highlight path: a character's events, in year then clock order
function pathList(cid){
  if(!cid)return[];
  const ev=links.filter(l=>l.kind==='involves'&&(sid(l.target)===cid||sid(l.source)===cid)).map(l=>byId.get(sid(l.target)===cid?sid(l.source):sid(l.target))).filter(n=>n&&n.type==='event');
  const u=[...new Map(ev.map(n=>[n.id,n])).values()];
  u.sort((a,b)=>(a.year??1e9)-(b.year??1e9)||(a.ord??0)-(b.ord??0));
  return[byId.get(cid),...u];
}
let P=[],PS=new Set();
// ---- chrome
const bar=document.getElementById('types');
TYPES.forEach(t=>{const b=document.createElement('button');b.className='chip';b.style.setProperty('--c',COL(t));b.setAttribute('aria-pressed','true');
 b.innerHTML='<i></i>'+t+' '+nodes.filter(n=>n.type===t).length;b.onclick=()=>{on.has(t)?on.delete(t):on.add(t);b.setAttribute('aria-pressed',on.has(t));refresh()};bar.appendChild(b)});
const ps=document.getElementById('path');
ps.innerHTML='<option value="">Path: none</option>'+nodes.filter(n=>n.type==='character').map(n=>'<option value="'+n.id+'">Path: '+esc(n.label)+' ('+(pathList(n.id).length-1)+')</option>').join('');
ps.onchange=()=>setPath(ps.value||null);
function setPath(id){pathChar=id;ps.value=id||'';P=pathList(id);PS=new Set(P.map(n=>n.id));refresh()}
const rail=document.getElementById('rail');
[['1','Force'],['2','Eras'],['3','DCUS']].forEach(([k,n])=>{const b=document.createElement('button');b.id='rb'+k;b.innerHTML='<b>'+k+'</b>'+n;b.onclick=()=>setView(+k);rail.appendChild(b)});
function setView(v){view=v;[1,2,3].forEach(k=>{document.getElementById('v'+k).classList.toggle('off',k!==v);document.getElementById('rb'+k).setAttribute('aria-pressed',k===v)});
 if(v===2)drawTimeline();if(v===3)drawTree();refresh()}
document.getElementById('foot').textContent='Source: fabula.json built '+DATA.built+' from '+DATA.sources.map(s=>s.split('/').pop()).join(', ')+'. Page built '+BUILT+'. '+nodes.length+' nodes, '+links.length+' links.';
document.getElementById('foot').title=DATA.sources.join('\n');
const tip=document.getElementById('tip');
function tipOn(e,d){tip.innerHTML='<em>'+d.type+(d.year?' · '+d.year:'')+(d.deg!=null?' · '+d.deg+' links':'')+'</em><b>'+esc(d.label)+'</b><br>'+esc((d.desc||'').slice(0,220));tip.style.display='block'}
function tipMove(e){tip.style.left=Math.min(e.clientX+14,innerWidth-320)+'px';tip.style.top=Math.min(e.clientY+14,innerHeight-120)+'px'}
function tipOff(){tip.style.display='none'}
function bindNode(s){s.on('mouseenter focus',tipOn).on('mousemove',tipMove).on('mouseleave blur',tipOff)
 .on('click',(e,d)=>{e.stopPropagation();select(d.id)}).on('keydown',(e,d)=>{if(e.key==='Enter')select(d.id)})}
// ---- properties sidebar (netron-04)
const side=document.getElementById('side');
function select(id){sel=id;refresh()}
function drawSide(){
  if(!sel){side.style.display='none';return}
  const d=lookup(sel);if(!d){side.style.display='none';return}
  const rel=links.filter(l=>sid(l.source)===sel||sid(l.target)===sel).map(l=>{const o=byId.get(sid(l.source)===sel?sid(l.target):sid(l.source));return '<li><a data-id="'+o.id+'" tabindex="0">'+esc(o.label)+'</a> <small>'+o.type+' · '+esc(l.kind)+'</small></li>'});
  const f=(k,v,c)=>v==null||v===''?'':'<dt>'+k+'</dt><dd class="'+(c||'')+'">'+v+'</dd>';
  side.innerHTML='<button class="x" aria-label="Close">×</button><small style="color:'+COL(d.type)+';font:11px IBM Plex Mono,monospace">'+d.type+'</small><h2>'+esc(d.label)+'</h2><dl>'+
   f('id',esc(d.id),'mono')+f('era',esc(eraName(d.era)))+f('year',d.year)+f('source',esc(fmtSrc(d)),'mono')+f('about',esc(d.desc))+'</dl>'+
   (d.type==='character'?'<button class="go">Highlight path</button>':'')+(rel.length?'<small style="font:11px IBM Plex Mono,monospace;color:var(--mut)">'+rel.length+' links</small><ul>'+rel.join('')+'</ul>':'');
  side.style.display='block';
  side.querySelector('.x').onclick=()=>select(null);
  const g=side.querySelector('.go');if(g)g.onclick=()=>setPath(pathChar===d.id?null:d.id);
  side.querySelectorAll('li a').forEach(a=>{a.onclick=()=>select(a.dataset.id);a.onkeydown=e=>{if(e.key==='Enter')select(a.dataset.id)}});
}
// ---- view 1: force graph
const svg1=d3.select('#v1'),g1=svg1.append('g');
svg1.call(d3.zoom().scaleExtent([.3,4]).on('zoom',e=>g1.attr('transform',e.transform))).on('click',()=>select(null));
const lk=g1.append('g').selectAll('line').data(links).join('line').attr('class','lk');
const ptl=g1.append('g').append('path').attr('class','pth');
const nd1=g1.append('g').selectAll('g').data(nodes).join('g').attr('class','nd').attr('tabindex',0);
nd1.append('circle').attr('class','sh').attr('r',d=>5+Math.sqrt(d.deg)*2.6).attr('fill',d=>COL(d.type));
nd1.append('text').attr('x',d=>9+Math.sqrt(d.deg)*2.6).attr('y',4).text(d=>d.label);
bindNode(nd1);
const sim=d3.forceSimulation(nodes).force('link',d3.forceLink(links).id(d=>d.id).distance(60).strength(.5))
 .force('charge',d3.forceManyBody().strength(-260)).force('collide',d3.forceCollide(d=>10+d.deg))
 .force('x',d3.forceX().strength(.04)).force('y',d3.forceY().strength(.06));
function fit(){const r=document.getElementById('stage').getBoundingClientRect();sim.force('center',d3.forceCenter(r.width/2,r.height/2));sim.force('x').x(r.width/2);sim.force('y').y(r.height/2)}
fit();addEventListener('resize',()=>{fit();sim.alpha(.3).restart()});
nd1.call(d3.drag().on('start',(e,d)=>{if(!e.active)sim.alphaTarget(.3).restart();d.fx=d.x;d.fy=d.y}).on('drag',(e,d)=>{d.fx=e.x;d.fy=e.y}).on('end',(e,d)=>{if(!e.active)sim.alphaTarget(0);d.fx=d.fy=null}));
function tick(){lk.attr('x1',d=>d.source.x).attr('y1',d=>d.source.y).attr('x2',d=>d.target.x).attr('y2',d=>d.target.y);nd1.attr('transform',d=>'translate('+d.x+','+d.y+')');
 ptl.attr('d',P.length>1?d3.line()(P.map(n=>[n.x,n.y])):null)}
sim.on('tick',tick);
// ---- view 2: era timeline
const svg2=d3.select('#v2'),g2=svg2.append('g');
const zoom2=d3.zoom().scaleExtent([.2,4]).on('zoom',e=>g2.attr('transform',e.transform));
svg2.call(zoom2).on('click',()=>select(null));
const BANDS=[['era1','Skeeter Creek'],['era2','DCUS'],['era3','LAKAD'],['era5','Beyond'],['none','No era']];
let tlItems=[];
function drawTimeline(){
  g2.selectAll('*').remove();
  const H=240,STEP=74;
  const items=nodes.filter(n=>(n.type==='event'||n.type==='character')&&vis(n));
  const lanes={};
  const bandOf=n=>n.era||'none';
  ['era1','era2','era3','era4','era5','none'].forEach(b=>lanes[b]={dated:[],und:[]});
  items.forEach(n=>(n.year?lanes[bandOf(n)].dated:lanes[bandOf(n)].und).push(n));
  const key=(a,b)=>(a.year??0)-(b.year??0)||(a.ord??1e5)-(b.ord??1e5)||a.label.localeCompare(b.label);
  Object.values(lanes).forEach(l=>{l.dated.sort(key);l.und.sort(key)});
  const wOf=b=>Math.max(230,STEP*Math.max(lanes[b].dated.length,lanes[b].und.length)+50);
  const w={era1:wOf('era1'),era2:Math.max(wOf('era2'),wOf('era4')),era3:wOf('era3'),era5:wOf('era5'),none:wOf('none')};
  const x0={};let x=20;BANDS.forEach(([b])=>{x0[b]=x;x+=w[b]+14});x0.era4=x0.era2;w.era4=w.era2;
  const total=x;tlItems=[];
  const bands=[...BANDS.map(([b,n])=>[b,n,0]),['era4','ASTRO7EX (runs alongside era 2)',H+24]];
  bands.forEach(([b,name,y0])=>{
    const bg=g2.append('g').attr('class','band').attr('transform','translate('+x0[b]+','+y0+')');
    bg.append('rect').attr('width',w[b]).attr('height',H).attr('rx',8);
    bg.append('text').attr('class','bt').attr('x',10).attr('y',20).text(b==='none'?name:(b.slice(3)+' · '+name));
    bg.append('text').attr('class','bs').attr('x',10).attr('y',34).text(lanes[b].dated.length+' dated');
    bg.append('line').attr('x1',8).attr('x2',w[b]-8).attr('y1',140).attr('y2',140);
    bg.append('text').attr('class','bs').attr('x',10).attr('y',154).text('undated ('+lanes[b].und.length+')');
    [['dated',lanes[b].dated,48],['und',lanes[b].und,166]].forEach(([k,arr,ly])=>{
      const st=Math.max(STEP,(w[b]-50)/Math.max(arr.length,1));
      arr.forEach((n,i)=>{const px=x0[b]+24+i*Math.min(st,STEP*1.6),py=y0+ly+(i%4)*20;n._tx=px;n._ty=py;tlItems.push(n)})});
  });
  const nd=g2.append('g').selectAll('g').data(tlItems,d=>d.id).join('g').attr('class','nd tl').attr('tabindex',0).attr('transform',d=>'translate('+d._tx+','+d._ty+')');
  nd.append('path').attr('class','sh').attr('d',d=>d3.symbol().type(d.type==='character'?d3.symbolDiamond:d3.symbolCircle).size(d.type==='character'?170:90)()).attr('fill',d=>COL(d.type));
  nd.append('text').attr('class','nm').attr('x',9).attr('y',4).text(d=>(d.label.length>20?d.label.slice(0,19)+'…':d.label)+(d.year?' '+d.year:''));
  bindNode(nd);
  g2.append('path').attr('class','pth').attr('id','tlpath');
  svg2.call(zoom2.transform,d3.zoomIdentity);
  const r=document.getElementById('stage').getBoundingClientRect();const k=Math.min(1,(r.width-20)/total);
  svg2.call(zoom2.transform,d3.zoomIdentity.translate(10,10).scale(k));
}
// ---- view 3: DCUS hierarchy
const svg3=d3.select('#v3'),g3=svg3.append('g');
const zoom3=d3.zoom().scaleExtent([.4,3]).on('zoom',e=>g3.attr('transform',e.transform));
svg3.call(zoom3).on('click',()=>select(null));
let root3=null;
function buildTree(){
  const T=DATA.tree,rootN=byId.get(T.root);
  const kids=T.groups.map(gr=>({name:gr.label,type:'group',children:gr.ids.filter(i=>i!==T.root&&byId.get(i)).map(i=>({name:byId.get(i).label,id:i,type:byId.get(i).type}))}));
  kids.push({name:'Setting layers S1-S12',type:'group',children:DATA.layers.map(l=>({name:l.label,id:l.id,type:'layer'}))});
  const h=d3.hierarchy({name:rootN.label,id:T.root,type:rootN.type,children:kids});
  h.children[h.children.length-1]._children=h.children[h.children.length-1].children;h.children[h.children.length-1].children=null;
  return h;
}
function drawTree(){
  if(!root3)root3=buildTree();
  g3.selectAll('*').remove();
  d3.tree().nodeSize([26,250])(root3);
  g3.append('g').selectAll('path').data(root3.links()).join('path').attr('class','tl').attr('d',d3.linkHorizontal().x(d=>d.y).y(d=>d.x));
  const n=g3.append('g').selectAll('g').data(root3.descendants()).join('g').attr('class','nd tg').attr('transform',d=>'translate('+d.y+','+d.x+')').attr('tabindex',0);
  n.append('circle').attr('class','sh').attr('r',d=>d.data.type==='group'?5:6).attr('fill',d=>d.data.type==='group'?'#34312d':COL(d.data.type)).attr('stroke',d=>d._children?'var(--acc)':'var(--bg)');
  n.append('text').attr('x',11).attr('y',4).text(d=>d.data.name+(d._children?' (+'+d._children.length+')':''));
  n.on('click',(e,d)=>{e.stopPropagation();if(d.data.type==='group'||d.depth===0){if(d.children){d._children=d.children;d.children=null}else if(d._children){d.children=d._children;d._children=null}}
    if(d.data.id)sel=d.data.id;drawTree();refresh()})
   .on('keydown',(e,d)=>{if(e.key==='Enter')n.on('click')(e,d)})
   .on('mouseenter focus',(e,d)=>{const x=d.data.id&&lookup(d.data.id);if(x)tipOn(e,x)}).on('mousemove',tipMove).on('mouseleave blur',tipOff);
  const r=document.getElementById('stage').getBoundingClientRect();
  if(!drawTree.done){svg3.call(zoom3.transform,d3.zoomIdentity.translate(40,r.height/2));drawTree.done=1}
}
// ---- refresh all
function refresh(){
  P=pathList(pathChar);PS=new Set(P.map(n=>n.id));
  const hl=sel&&view===1?new Set([sel,...(nb.get(sel)||[])]):null;
  const dimN=d=>!vis(d)||(hl&&!hl.has(d.id))||(PS.size&&!PS.has(d.id));
  nd1.style('display',d=>on.has(d.type)?null:'none').classed('dim',dimN).classed('sel',d=>d.id===sel).classed('onpath',d=>PS.has(d.id)&&PS.size>0);
  lk.style('display',l=>on.has(l.source.type)&&on.has(l.target.type)?null:'none')
    .classed('hi',l=>sel&&(l.source.id===sel||l.target.id===sel)).classed('dim',l=>(hl&&!(l.source.id===sel||l.target.id===sel))||(PS.size&&!(PS.has(l.source.id)&&PS.has(l.target.id))));
  tick();
  if(view===2){
    g2.selectAll('.tl').classed('dim',d=>dimOther(d)).classed('sel',d=>d.id===sel).classed('onpath',d=>PS.has(d.id)&&PS.size>0);
    const pts=P.filter(n=>n._tx!=null&&vis(n));
    g2.select('#tlpath').attr('d',pts.length>1?d3.line()(pts.map(n=>[n._tx,n._ty])):null);
  }
  if(view===3)g3.selectAll('.tg').classed('sel',d=>d.data.id===sel);
  drawSide();
}
function dimOther(d){return PS.size?!PS.has(d.id):false}
addEventListener('keydown',e=>{
  if(e.target.tagName==='INPUT'||e.target.tagName==='SELECT')return;
  if(e.key==='1'||e.key==='2'||e.key==='3')setView(+e.key);
  else if(e.key==='/'){e.preventDefault();document.getElementById('q').focus()}
  else if(e.key==='Escape'){sel=null;setPath(null)}
});
document.getElementById('q').addEventListener('input',e=>{query=e.target.value.trim().toLowerCase();if(view===2)drawTimeline();refresh()});
on.forEach(()=>{});
// the type chips and search redraw the timeline too
document.getElementById('types').addEventListener('click',()=>{if(view===2){drawTimeline();refresh()}});
setView(1);
</script>
</body>
</html>
'''

def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    built = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    html = TEMPLATE.replace("__DATA__", blob).replace("__BUILT__", built)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    size = OUT.stat().st_size
    print("wrote", OUT, size, "bytes", "OK" if size < 400_000 else "OVER 400 KB")

main()
