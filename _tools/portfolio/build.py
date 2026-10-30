# -*- coding: utf-8 -*-
"""build.py - the portfolio glass (10/30): one local viewer page for Chief's past video and audio work.

Reads   Q:\\_Final_Media_Products\\1keep_copy2 (video + audio only; stock packs, lessons and installers are skipped)
Writes  _PRIVATE/portfolio/portfolio.html + thumbs/*.jpg + catalog.json   (private, local; file:// links, no copies)
Zero tokens. Usage: python -X utf8 build.py [--root PATH] [--no-thumbs]
"""
import argparse, concurrent.futures as cf, hashlib, html, json, os, re, subprocess, sys, time
from urllib.parse import quote

ROOT_DEFAULT = r"Q:\_Final_Media_Products\1keep_copy2"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "..", "_PRIVATE", "portfolio"))
VIDEO = {".mp4", ".mov", ".wmv", ".m4v", ".avi", ".mkv", ".webm"}
AUDIO = {".mp3", ".wav", ".m4a", ".flac", ".ogg", ".aac"}
# not Chief's works: stock packs, lessons, installers, class files, game folders
SKIP = {"Light Leaks Pack", "AE2", "Vocal Coach.com - Voice Singing Lessons [Complete mp3]", "Toontrack",
        "Toontrack_Product_Manager_WIN", "Auto-Tune Artist v9.0.0 Windows (4)", "Cyberpunk 2077",
        "Blender Class Dillongoo", "VASHI VISUALS EXTREME WIDESCREEN", "Clonehires_512kb.mp4"}
SKIP_NAMES = re.compile(r"^(Together - Pegboard Nerds)", re.I)   # a bought track, not a work
# folders shown as their own shelf; loose top-level files go on "Films and videos" / "Music and audio"
SHELF = {"finals": "Finals (episodes)", "pbp": "PBP", "jsoc": "JSOC", "Disarmed": "Disarmed",
         "Where the fuck is Tom": "Where the F is Tom", "TikTok Drops": "TikTok drops", "vtuber": "VTuber",
         "Birddog Music": "Birddog music", "cllankers spotify": "Spotify uploads", "sound": "Sound",
         "SMM-Salon1-all-audio-files": "SMM salon audio", "C2C VOICE OVER AND B ROLL": "C2C voice-over and b-roll",
         "readthroughs": "Readthroughs (2012-13)"}


def probe(path):
    try:
        r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_name,width,height",
                            "-of", "json", path], capture_output=True, text=True, timeout=60)
        j = json.loads(r.stdout or "{}")
        dur = float(j.get("format", {}).get("duration") or 0)
        st = j.get("streams") or []
        v = next((s for s in st if s.get("width")), {})
        return dur, v.get("width", 0), v.get("height", 0), v.get("codec_name", "")
    except Exception:
        return 0.0, 0, 0, ""


def thumb(path, dur, dest):
    if os.path.exists(dest):
        return True
    t = max(0.0, min(dur * 0.1, 30.0)) if dur else 0
    try:
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{t:.2f}", "-i", path, "-frames:v", "1",
                        "-vf", "scale=320:-2", "-q:v", "5", dest], capture_output=True, timeout=90)
    except Exception:
        return False
    return os.path.exists(dest)


def walk(root):
    items = []
    for dp, dn, fn in os.walk(root):
        rel = os.path.relpath(dp, root)
        top = "" if rel == "." else rel.split(os.sep)[0]
        if top in SKIP:
            dn[:] = []
            continue
        for f in fn:
            ext = os.path.splitext(f)[1].lower()
            if ext not in VIDEO | AUDIO or f in SKIP or SKIP_NAMES.match(f):
                continue
            items.append((os.path.join(dp, f), top, "video" if ext in VIDEO else "audio"))
    return items


def mins(s):
    s = int(s)
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}" if s >= 3600 else f"{s // 60}:{s % 60:02d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=ROOT_DEFAULT)
    ap.add_argument("--no-thumbs", action="store_true")
    a = ap.parse_args()
    os.makedirs(os.path.join(OUT, "thumbs"), exist_ok=True)
    items = walk(a.root)
    print(f"{len(items)} media files", flush=True)

    def work(it):
        p, top, kind = it
        st = os.stat(p)
        dur, w, h, codec = probe(p)
        key = hashlib.md5(p.encode("utf-8")).hexdigest()[:12]
        th = ""
        if kind == "video" and not a.no_thumbs:
            d = os.path.join(OUT, "thumbs", key + ".jpg")
            if thumb(p, dur, d):
                th = "thumbs/" + key + ".jpg"
        shelf = SHELF.get(top) or ("Films and videos" if kind == "video" else "Music and audio")
        return {"path": p, "name": os.path.splitext(os.path.basename(p))[0], "ext": os.path.splitext(p)[1].lower()[1:],
                "kind": kind, "shelf": shelf, "dur": dur, "w": w, "h": h, "codec": codec, "mb": round(st.st_size / 1048576, 1),
                "year": time.strftime("%Y", time.localtime(st.st_mtime)), "thumb": th}

    with cf.ThreadPoolExecutor(6) as ex:
        cat = list(ex.map(work, items))
    cat.sort(key=lambda c: (c["shelf"], c["name"].lower()))
    with open(os.path.join(OUT, "catalog.json"), "w", encoding="utf-8") as f:
        json.dump(cat, f, indent=1, ensure_ascii=False)
    with open(os.path.join(OUT, "portfolio.html"), "w", encoding="utf-8") as f:
        f.write(page(cat))
    v = sum(c["kind"] == "video" for c in cat)
    print(f"wrote {OUT}\\portfolio.html  ({v} video, {len(cat) - v} audio)")


def url(p):
    return "file:///" + quote(p.replace("\\", "/"), safe="/:")


def card(c):
    u = html.escape(url(c["path"]))
    name = html.escape(c["name"])
    meta = f'{mins(c["dur"])} · {c["ext"].upper()} · {c["mb"]:.0f} MB' + (f' · {c["w"]}×{c["h"]}' if c["w"] else "")
    data = f'data-n="{html.escape(c["name"].lower())}" data-k="{c["kind"]}" data-y="{c["year"]}"'
    if c["kind"] == "video":
        img = f'<img loading="lazy" src="{html.escape(c["thumb"])}" alt="">' if c["thumb"] else '<div class="nothumb">VIDEO</div>'
        return (f'<article class="card" {data}><button class="play" data-src="{u}" data-name="{name}" aria-label="Play {name}">{img}'
                f'<span class="dur">{mins(c["dur"])}</span></button><h3>{name}</h3><p class="meta">{html.escape(meta)} · {c["year"]}</p>'
                f'<a href="{u}" target="_blank">open file</a></article>')
    return (f'<article class="card audio" {data}><h3>{name}</h3><p class="meta">{html.escape(meta)} · {c["year"]}</p>'
            f'<audio controls preload="none" src="{u}"></audio></article>')


def page(cat):
    shelves = {}
    for c in cat:
        shelves.setdefault(c["shelf"], []).append(c)
    order = sorted(shelves, key=lambda s: (s not in ("Films and videos", "Music and audio"), s))
    nv = sum(c["kind"] == "video" for c in cat)
    secs = "".join(
        f'<section id="s{i}"><h2>{html.escape(s)} <small>{len(shelves[s])}</small></h2><div class="grid">'
        + "".join(card(c) for c in shelves[s]) + "</div></section>" for i, s in enumerate(order))
    nav = "".join(f'<a href="#s{i}">{html.escape(s)}</a>' for i, s in enumerate(order))
    return PAGE.replace("@@SECS@@", secs).replace("@@NAV@@", nav).replace("@@NV@@", str(nv)).replace("@@NA@@", str(len(cat) - nv))


PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Portfolio Glass</title>
<style>
:root{color-scheme:dark;--bg:#121110;--panel:#1B1A18;--panel-2:#24221F;--line:#34312C;--ink:#ECE7DF;--ink-2:#B7B0A5;--ink-3:#8A8378;--accent:#FF5A1F;--accent-ink:#FFB08F;
--display:"Barlow Condensed","Arial Narrow",Arial,sans-serif;--body:"Atkinson Hyperlegible","Segoe UI",Verdana,sans-serif;--mono:"IBM Plex Mono",Consolas,monospace}
*{box-sizing:border-box}html,body{background:var(--bg);color:var(--ink)}body{margin:0;font:15px/1.5 var(--body);padding:0 16px 60px}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.strip{position:sticky;top:0;z-index:5;display:flex;align-items:center;gap:12px;flex-wrap:wrap;min-height:44px;margin:0 -16px;padding:6px 16px;background:var(--panel);border-bottom:1px solid var(--line)}
.strip h1{margin:0;font:800 20px/1 var(--display);letter-spacing:.06em;text-transform:uppercase}.strip h1 b{color:var(--accent)}
.chip{font:500 11px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase;padding:4px 7px;border:1px solid var(--line);border-radius:3px;color:var(--ink-2)}
input[type=search]{flex:1;min-width:160px;max-width:320px;background:var(--panel-2);border:1px solid var(--line);color:var(--ink);padding:7px 10px;border-radius:4px;font:inherit}
.tabs button{background:none;border:1px solid var(--line);color:var(--ink-2);padding:6px 10px;border-radius:4px;font:500 12px var(--mono);cursor:pointer;text-transform:uppercase}
.tabs button[aria-pressed=true]{border-color:var(--accent);color:var(--accent-ink)}
nav{display:flex;gap:6px;flex-wrap:wrap;max-width:1200px;margin:14px auto 0}nav a{font:500 12px var(--mono);color:var(--ink-2);text-decoration:none;border:1px solid var(--line);padding:4px 8px;border-radius:3px}nav a:hover{color:var(--accent-ink);border-color:var(--accent)}
main{max-width:1200px;margin:0 auto;display:grid;gap:22px;padding-top:18px}
section{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding-bottom:16px}
h2{margin:0 0 12px;padding:10px 16px;font:700 19px var(--display);letter-spacing:.06em;text-transform:uppercase;border-bottom:1px solid var(--line)}h2 small{font:400 12px var(--mono);color:var(--ink-3);margin-left:8px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px;padding:0 16px}
.card{background:var(--panel-2);border:1px solid var(--line);border-radius:5px;padding:8px;min-width:0}
.card h3{margin:8px 0 2px;font:700 15px/1.2 var(--display);letter-spacing:.03em;overflow-wrap:anywhere}.meta{margin:0 0 4px;font:11px var(--mono);color:var(--ink-3)}
.card a{font:11px var(--mono);color:var(--accent-ink)}
.play{position:relative;display:block;width:100%;aspect-ratio:16/9;padding:0;border:0;background:#000;cursor:pointer;border-radius:3px;overflow:hidden}
.play img{width:100%;height:100%;object-fit:cover;display:block}.play:hover{outline:2px solid var(--accent)}
.nothumb{display:grid;place-items:center;height:100%;color:var(--ink-3);font:12px var(--mono)}
.dur{position:absolute;right:6px;bottom:6px;background:#000c;color:#fff;font:11px var(--mono);padding:2px 5px;border-radius:3px}
.audio audio{width:100%;margin-top:4px;height:34px}
dialog{width:min(960px,96vw);background:var(--panel);color:var(--ink);border:1px solid var(--accent);border-radius:6px;padding:12px}dialog::backdrop{background:#000d}
dialog video{width:100%;max-height:75vh;background:#000}dialog header{display:flex;justify-content:space-between;gap:10px;margin-bottom:8px;font:700 18px var(--display)}
dialog button{background:var(--accent);color:#000;border:0;padding:6px 14px;border-radius:4px;font:700 13px var(--mono);cursor:pointer}
.hide{display:none!important}
</style></head><body>
<div class="strip"><h1>The <b>Portfolio</b> Glass</h1><span class="chip">@@NV@@ video</span><span class="chip">@@NA@@ audio</span><span class="chip">private · local</span>
<input type="search" id="q" placeholder="search title" aria-label="search"><span class="tabs"><button data-k="all" aria-pressed="true">All</button><button data-k="video" aria-pressed="false">Video</button><button data-k="audio" aria-pressed="false">Audio</button></span></div>
<nav>@@NAV@@</nav><main>@@SECS@@</main>
<dialog id="dlg"><header><span id="dt"></span><button id="dc">Close</button></header><video id="dv" controls></video></dialog>
<script>
const q=document.getElementById('q'),cards=[...document.querySelectorAll('.card')],tabs=[...document.querySelectorAll('.tabs button')];let kind='all';
function filt(){const s=q.value.trim().toLowerCase();cards.forEach(c=>c.classList.toggle('hide',!(c.dataset.n.includes(s)&&(kind==='all'||c.dataset.k===kind))));
document.querySelectorAll('section').forEach(sec=>sec.classList.toggle('hide',!sec.querySelector('.card:not(.hide)')))}
q.oninput=filt;tabs.forEach(b=>b.onclick=()=>{kind=b.dataset.k;tabs.forEach(x=>x.setAttribute('aria-pressed',x===b));filt()});
const dlg=document.getElementById('dlg'),dv=document.getElementById('dv');
document.addEventListener('click',e=>{const p=e.target.closest('.play');if(!p)return;document.getElementById('dt').textContent=p.dataset.name;dv.src=p.dataset.src;dlg.showModal();dv.play().catch(()=>{})});
function shut(){dv.pause();dv.removeAttribute('src');dv.load();dlg.close()}document.getElementById('dc').onclick=shut;dlg.addEventListener('cancel',()=>{dv.pause()});
</script></body></html>
"""

if __name__ == "__main__":
    main()
