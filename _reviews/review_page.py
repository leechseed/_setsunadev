"""review_page.py <reviewed.md> : build one self-contained dark HTML review page (BOLO 125).
Output: <name>.review.html beside the input. Marks: ==span==[^cN]  ~~old~~ ++new++[^cN]  comments at [^cN]: **cN** . text
Choices live in localStorage; Export decisions downloads JSON for apply_review.py. Publishes nothing."""
import html
import io
import json
import os
import re
import sys


def parse(md):
    comments = {}
    for m in re.finditer(r"^\[\^(c\d+)\]:\s*\*\*c\d+\*\*\s*·\s*(.+)$", md, re.M):
        comments[m.group(1)] = {"id": m.group(1), "text": m.group(2).strip(), "span": "", "old": None, "new": None}
    body = md.split("\n## Comments")[0].replace("\r\n", "\n")
    k = body.find("> **REVIEWED COPY.**")
    if k >= 0:  # skip the legend so its sample marks are not read as edits
        body = body[body.find("\n", k):]
    for m in re.finditer(r"==(.+?)==\[\^(c\d+)\]", body, re.S):
        if m.group(2) in comments:
            comments[m.group(2)]["span"] = m.group(1)
    for m in re.finditer(r"~~([^\n]+?)~~[ ]*\+\+([^\n]+?)\+\+\[\^(c\d+)\]", body):
        c = comments.get(m.group(3))
        if c:
            c["old"], c["new"] = m.group(1), m.group(2)
            c["span"] = c["span"] or m.group(1)
    return body, comments


def render_block(blk):
    out = html.escape(blk)
    out = re.sub(r"==(.+?)==\[\^(c\d+)\]", r'<mark data-c="\2">\1</mark><sup>\2</sup>', out, flags=re.S)
    out = re.sub(r"~~([^\n]+?)~~[ ]*\+\+([^\n]+?)\+\+\[\^(c\d+)\]", r"<del>\1</del> <ins>\2</ins><sup>\3</sup>", out)
    out = re.sub(r"\[\^(c\d+)\]", r"<sup>\1</sup>", out)
    out = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", out)
    return out


def main():
    src = sys.argv[1]
    md = io.open(src, encoding="utf-8").read()
    body, comments = parse(md)
    blocks = []
    for blk in re.split(r"\n\s*\n", body.strip()):
        ids = re.findall(r"\[\^(c\d+)\]", blk)
        blocks.append({"html": render_block(blk), "ids": ids, "table": blk.lstrip().startswith("|")})
    name = os.path.basename(src).replace(".reviewed.md", "").replace(".md", "")
    page = (TPL.replace("__NAME__", html.escape(name))
            .replace("__BLOCKS__", json.dumps(blocks).replace("</", "<\\/"))
            .replace("__COMMENTS__", json.dumps(comments).replace("</", "<\\/")))
    out = os.path.join(os.path.dirname(os.path.abspath(src)), name + ".review.html")
    io.open(out, "w", encoding="utf-8", newline="\n").write(page)
    print("wrote", out, "-", len(comments), "comments -", sum(1 for c in comments.values() if c["old"]), "with a suggested edit")


TPL = r"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Review Desk</title>
<style>
:root{--bg:#141016;--card:#1d1721;--line:#33283a;--tx:#e9e2ec;--mu:#9a8fa3;--or:#FF5A1F;--ok:#3fbf7f;--no:#e0455a}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--tx);font:16px/1.5 system-ui,sans-serif}
header{position:sticky;top:0;height:44px;display:flex;align-items:center;gap:12px;padding:0 16px;background:#0f0b11;border-bottom:2px solid var(--or);z-index:2}
header b{color:var(--or)}header span{color:var(--mu);font-size:14px;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
button{background:var(--or);color:#141016;border:0;border-radius:6px;padding:8px 12px;font-weight:700;cursor:pointer}
main{max-width:1100px;margin:0 auto;padding:16px}
.row{display:grid;grid-template-columns:minmax(0,3fr) minmax(0,2fr);gap:16px;margin-bottom:6px}
@media(max-width:760px){.row{grid-template-columns:1fr}}
.p{white-space:pre-wrap;word-wrap:break-word;padding:4px 0}.p.tb{font:13px/1.4 ui-monospace,Consolas,monospace;overflow-x:auto;white-space:pre;color:var(--mu)}
mark{background:#FF5A1F33;color:var(--tx);border-bottom:2px solid var(--or);padding:0 2px}
del{color:var(--no)}ins{color:var(--ok);text-decoration:none}sup{color:var(--or);font-weight:700}
.card{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--or);border-radius:8px;padding:12px;margin-bottom:10px}
.card.accept{border-left-color:var(--ok)}.card.reject{border-left-color:var(--no)}
.id{color:var(--or);font-weight:700;font-size:13px}.q{color:var(--mu);font-size:13px;margin:4px 0}
.ed{font-size:14px;margin:6px 0}.btns{display:flex;gap:8px;margin-top:8px}
.btns button{flex:1;min-height:40px;background:#2a2030;color:var(--tx);border:1px solid var(--line)}
.btns .a.on{background:var(--ok);color:#0b1a12}.btns .r.on{background:var(--no);color:#fff}
</style></head><body>
<header><b>REVIEW DESK</b><span id="n">__NAME__</span><button id="x">Export decisions</button></header>
<main id="m"></main>
<script>
var B=__BLOCKS__,C=__COMMENTS__,NAME="__NAME__",K="reviewdesk:"+NAME,S={};
try{S=JSON.parse(localStorage.getItem(K)||"{}")}catch(e){}
function save(){try{localStorage.setItem(K,JSON.stringify(S))}catch(e){}}
function esc(s){var d=document.createElement("div");d.textContent=s;return d.innerHTML}
function card(id){var c=C[id],v=S[id]||"";
return '<div class="card '+v+'" id="k'+id+'"><div class="id">'+id+(v?' - '+v:'')+'</div>'+(c.span?'<div class="q">"'+esc(c.span.slice(0,140))+'"</div>':'')+'<div>'+esc(c.text)+'</div>'+
(c.old?'<div class="ed"><del>'+esc(c.old)+'</del> <ins>'+esc(c.new)+'</ins></div>':'')+
'<div class="btns"><button class="a'+(v=="accept"?" on":"")+'" data-i="'+id+'" data-v="accept">Accept</button><button class="r'+(v=="reject"?" on":"")+'" data-i="'+id+'" data-v="reject">Reject</button></div></div>'}
function draw(){var n=0,t=Object.keys(C).length;for(var k in S)if(C[k])n++;
document.getElementById("n").textContent=NAME+" - "+n+" of "+t+" decided";
document.getElementById("m").innerHTML=B.map(function(b){return '<div class="row"><div class="p'+(b.table?' tb':'')+'">'+b.html+'</div><div>'+b.ids.map(card).join("")+'</div></div>'}).join("")}
document.getElementById("m").addEventListener("click",function(e){var b=e.target.closest("button");if(!b)return;var i=b.dataset.i;if(S[i]==b.dataset.v)delete S[i];else S[i]=b.dataset.v;save();draw()});
document.getElementById("x").onclick=function(){var o={document:NAME,exported:new Date().toISOString(),decisions:Object.keys(C).map(function(i){return{id:i,decision:S[i]||"undecided"}})};
var a=document.createElement("a");a.href=URL.createObjectURL(new Blob([JSON.stringify(o,null,1)],{type:"application/json"}));a.download=NAME+".decisions.json";a.click()};
draw();
</script></body></html>"""

if __name__ == "__main__":
    main()
