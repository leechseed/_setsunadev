#!/usr/bin/env python3
"""Local Review: read the uncommitted diff, comment on lines, send the batch back as a file.

python _tools/review/localpr.py [--base HEAD] [--port 8790]
Serves one page on 127.0.0.1 only. "Send to Claude" POSTs the comments; the server writes
_tools/review/out/<timestamp>.json and .md, prints the path, and keeps serving.
Read-only on the repo: only git diff / ls-files / show-style reads are run.
"""
import argparse, json, re, subprocess, sys, time
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "out"
ROOT = HERE.parent.parent
MAX_UNTRACKED = 400_000


def git(*args):
    r = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True)
    return r.stdout.decode("utf-8", "replace")


def parse_diff(text):
    files, cur, hunk = [], None, None
    for line in text.split("\n"):
        if line.startswith("diff --git "):
            m = re.match(r"diff --git a/(.*) b/(.*)$", line)
            cur = {"path": m.group(2) if m else line[11:], "hunks": [], "note": ""}
            files.append(cur); hunk = None
        elif cur is None:
            continue
        elif line.startswith("Binary files") or line.startswith("GIT binary patch"):
            cur["note"] = "binary file"
        elif line.startswith("rename to "):
            cur["note"] = "renamed from " + cur.get("from", "?")
        elif line.startswith("rename from "):
            cur["from"] = line[12:]
        elif line.startswith("new file"):
            cur["note"] = "new file"
        elif line.startswith("deleted file"):
            cur["note"] = "deleted"
        elif line.startswith("@@"):
            m = re.match(r"@@ -(\d+)(?:,\d+)? \+(\d+)", line)
            o, n = int(m.group(1)), int(m.group(2))
            hunk = {"head": line, "lines": []}
            cur["hunks"].append(hunk)
        elif hunk is not None and line[:1] in (" ", "+", "-"):
            t = line[0]
            if t == " ":
                hunk["lines"].append([" ", o, n, line[1:]]); o += 1; n += 1
            elif t == "+":
                hunk["lines"].append(["+", None, n, line[1:]]); n += 1
            else:
                hunk["lines"].append(["-", o, None, line[1:]]); o += 1
    return files


def untracked():
    out = []
    for p in git("ls-files", "--others", "--exclude-standard").split("\n"):
        p = p.strip()
        if not p or p.startswith("_tools/review/out/"):
            continue
        f = ROOT / p
        try:
            data = f.read_bytes()
        except OSError:
            continue
        if b"\0" in data[:4096]:
            out.append({"path": p, "hunks": [], "note": "new untracked binary file"}); continue
        if len(data) > MAX_UNTRACKED:
            out.append({"path": p, "hunks": [], "note": "new untracked file, too large to show"}); continue
        lines = data.decode("utf-8", "replace").split("\n")
        if lines and lines[-1] == "":
            lines.pop()
        out.append({"path": p, "note": "untracked (all additions)",
                    "hunks": [{"head": "@@ -0,0 +1,%d @@" % len(lines),
                               "lines": [["+", None, i + 1, s] for i, s in enumerate(lines)]}]})
    return out


def build(base):
    files = parse_diff(git("diff", "--no-color", "-U3", base, "--"))
    return files + untracked()


PAGE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Local Review</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Barlow+Condensed:wght@600;700&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">
<style>
:root{--bg:#121110;--panel:#1B1A18;--line:#2c2a27;--ink:#e9e5df;--mute:#8d867c;--acc:#FF5A1F;--add:#12301c;--del:#3a1816}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 'Atkinson Hyperlegible',system-ui,sans-serif}
header{position:sticky;top:0;z-index:5;height:44px;background:var(--panel);border-bottom:1px solid var(--line);display:flex;align-items:center;gap:12px;padding:0 16px}
h1{font:700 20px 'Barlow Condensed',sans-serif;letter-spacing:.06em;text-transform:uppercase;margin:0;color:var(--acc)}
.sp{flex:1}.cnt{color:var(--mute);font-size:14px}
button{font:inherit;background:var(--bg);color:var(--ink);border:1px solid var(--line);border-radius:4px;padding:3px 10px;cursor:pointer}
button:hover,button:focus-visible{border-color:var(--acc)}
button.go{background:var(--acc);color:#121110;border-color:var(--acc);font-weight:700}
main{max-width:1200px;margin:0 auto;padding:16px}
.gen{width:100%;background:var(--panel);color:var(--ink);border:1px solid var(--line);border-radius:4px;padding:8px;font:inherit;min-height:60px}
.file{background:var(--panel);border:1px solid var(--line);border-radius:4px;margin:16px 0;overflow:hidden}
.fh{padding:8px 12px;font:600 17px 'Barlow Condensed',sans-serif;letter-spacing:.04em;border-bottom:1px solid var(--line)}
.fh small{color:var(--mute);font:14px 'Atkinson Hyperlegible',sans-serif;margin-left:8px}
.hh{color:var(--mute);font:13px 'IBM Plex Mono',monospace;padding:2px 12px;background:#161513}
table{border-collapse:collapse;width:100%;font:13px/1.45 'IBM Plex Mono',monospace}
td{padding:0 6px;vertical-align:top}
td.n{width:48px;text-align:right;color:var(--mute);user-select:none;border-right:1px solid var(--line)}
td.c{white-space:pre-wrap;word-break:break-all;width:100%}
tr.add td.c{background:var(--add)}tr.del td.c{background:var(--del)}
td.b{width:28px;text-align:center}
td.b button{padding:0 6px;font-size:13px;opacity:.35}tr:hover td.b button{opacity:1;border-color:var(--acc)}
tr.cm td{background:#201e1b;padding:8px 12px}
tr.cm textarea{width:100%;background:var(--bg);color:var(--ink);border:1px solid var(--acc);border-radius:4px;padding:6px;font:15px 'Atkinson Hyperlegible',sans-serif;min-height:54px}
.empty{color:var(--mute);padding:40px 0;text-align:center}
#msg{color:var(--acc);font-size:14px}
</style></head><body>
<header><h1>Local Review</h1><span class="cnt" id="cnt"></span><span class="sp"></span><span id="msg" role="status"></span><button class="go" id="send">Send to Claude</button></header>
<main><label for="gen" class="cnt">General comment</label><textarea class="gen" id="gen" placeholder="Overall notes for the CDR"></textarea><div id="root"></div></main>
<script>
const FILES=__DATA__;
const cm={};// key "path\x00line" -> text
const root=document.getElementById('root');
function upd(){const n=Object.values(cm).filter(v=>v.trim()).length;document.getElementById('cnt').textContent=FILES.length+' files · '+n+' comments'}
function el(t,c,x){const e=document.createElement(t);if(c)e.className=c;if(x!==undefined)e.textContent=x;return e}
if(!FILES.length)root.appendChild(el('div','empty','No changes against the base.'));
FILES.forEach(f=>{
 const box=el('section','file');const h=el('div','fh',f.path);if(f.note)h.appendChild(el('small','',f.note));box.appendChild(h);
 f.hunks.forEach(hk=>{
  box.appendChild(el('div','hh',hk.head));const t=el('table');
  hk.lines.forEach(l=>{
   const ln=l[2]!==null?l[2]:l[1];const tr=el('tr',l[0]=='+'?'add':l[0]=='-'?'del':'');
   tr.appendChild(el('td','n',l[1]===null?'':l[1]));tr.appendChild(el('td','n',l[2]===null?'':l[2]));
   tr.appendChild(el('td','c',l[0]+l[3]));
   const b=el('td','b');const btn=el('button','','+');btn.title='Comment on line '+ln;btn.setAttribute('aria-label','Comment on '+f.path+' line '+ln);
   const key=f.path+'\u0000'+(l[0]=='-'?'-':'')+ln;
   btn.onclick=()=>{let nx=tr.nextSibling;if(nx&&nx.dataset&&nx.dataset.k===key){nx.querySelector('textarea').focus();return}
    const r=el('tr','cm');r.dataset.k=key;const c=el('td');c.colSpan=4;const ta=el('textarea');ta.value=cm[key]||'';
    ta.oninput=()=>{cm[key]=ta.value;upd()};c.appendChild(ta);r.appendChild(c);tr.after(r);ta.focus()};
   b.appendChild(btn);tr.appendChild(b);t.appendChild(tr)});
  box.appendChild(t)});
 root.appendChild(box)});
upd();
document.getElementById('send').onclick=async()=>{
 const items=Object.entries(cm).filter(([k,v])=>v.trim()).map(([k,v])=>{const [p,l]=k.split('\u0000');return {file:p,line:l,comment:v.trim()}});
 const general=document.getElementById('gen').value.trim();
 if(!items.length&&!general){msg('Nothing to send');return}
 try{const r=await fetch('/send',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({general,comments:items})});
  const j=await r.json();msg(r.ok?'Sent: '+j.path:'Failed')}catch(e){msg('Failed: '+e)}};
function msg(s){document.getElementById('msg').textContent=s}
</script></body></html>
"""


def write_batch(base, payload):
    OUT.mkdir(exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    comments = payload.get("comments", [])
    general = payload.get("general", "")
    data = {"base": base, "created": stamp, "general": general, "comments": comments}
    (OUT / f"{stamp}.json").write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    md = [f"# Local Review {stamp} (base {base})", ""]
    if general:
        md += ["## General", "", general, ""]
    md += ["## Line comments", ""]
    for c in comments:
        md.append(f"- {c['file']} · line {c['line']} · {c['comment']}")
    if not comments:
        md.append("(none)")
    (OUT / f"{stamp}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    return OUT / f"{stamp}.md"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="HEAD")
    ap.add_argument("--port", type=int, default=8790)
    a = ap.parse_args()

    class H(BaseHTTPRequestHandler):
        def log_message(self, *x):
            pass

        def _send(self, code, body, ctype):
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            if self.path.split("?")[0] != "/":
                return self._send(404, b"not found", "text/plain")
            data = json.dumps(build(a.base)).replace("</", "<\\/")
            self._send(200, PAGE.replace("__DATA__", data).encode("utf-8"), "text/html; charset=utf-8")

        def do_POST(self):
            if self.path != "/send":
                return self._send(404, b"not found", "text/plain")
            try:
                n = int(self.headers.get("Content-Length", 0))
                payload = json.loads(self.rfile.read(n).decode("utf-8"))
                p = write_batch(a.base, payload)
            except Exception as e:
                return self._send(400, json.dumps({"error": str(e)}).encode(), "application/json")
            print(f"comments written: {p}", flush=True)
            self._send(200, json.dumps({"path": str(p)}).encode(), "application/json")

    srv = HTTPServer(("127.0.0.1", a.port), H)
    print(f"Local Review on http://127.0.0.1:{a.port}/  (base {a.base})", flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()

# in the spirit of gilles-g/localpr (MIT), rewritten stdlib-only · BOLO 140 · 2026-10-13
