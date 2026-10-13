"""build_report.py — BOLO 140: one glass for every intake deliverable (10/12).

Reads each note.md under _PRIVATE/intake-repos/ (repos and articles) and renders them as one DARK page with a
left rail: one section per item, the Markdown turned to HTML by a small converter (headings, lists, tables,
bold, code, links). The picks counts per item come from picks.json beside each note.

    python _tools/intake/build_report.py [--out _PRIVATE/intake-repos/intake-report.html]
"""
import argparse
import html
import io
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass
ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "_PRIVATE" / "intake-repos"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_picker import LABELS  # noqa: E402

ORDER = ["articles/context-engineering", "articles/multi-agent-research", "articles/steering", "anthropics__skills",
         "ThibautMelen__agentic-ai-systems", "thedotmack__claude-mem", "articles/mcp-addons", "HKUDS__ClawTeam",
         "hesreallyhim__awesome-claude-code", "BehiSecc__awesome-claude-skills", "hluaguo__learn-faster-kit",
         "Leonxlnx__taste-skill", "ruvnet__ruflo", "Mudlet__Mudlet", "LukeRenton__explore-claude-code"]


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 <code>\2</code>", s)
    return s


def md_to_html(text):
    out, lines, i = [], text.splitlines(), 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        if ln.startswith("```"):
            buf = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(lines[i])
                i += 1
            out.append("<pre>" + html.escape("\n".join(buf)) + "</pre>")
            i += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)", ln)
        if m:
            lvl = min(len(m.group(1)) + 1, 4)
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
            i += 1
            continue
        if ln.lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]):
            head = [c.strip() for c in ln.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            t = "<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
            for r in rows:
                t += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
            out.append(t + "</tbody></table>")
            continue
        if re.match(r"^\s*([-*+]|\d+[.)])\s+", ln):
            ordered = bool(re.match(r"^\s*\d+[.)]\s+", ln))
            tag = "ol" if ordered else "ul"
            items = []
            while i < len(lines) and re.match(r"^\s*([-*+]|\d+[.)])\s+", lines[i]):
                item = re.sub(r"^\s*([-*+]|\d+[.)])\s+", "", lines[i])
                i += 1
                while i < len(lines) and lines[i].startswith(("  ", "\t")) and not re.match(r"^\s*([-*+]|\d+[.)])\s+", lines[i]):
                    item += " " + lines[i].strip()
                    i += 1
                items.append(f"<li>{inline(item)}</li>")
            out.append(f"<{tag}>" + "".join(items) + f"</{tag}>")
            continue
        if ln.startswith(">"):
            out.append(f"<blockquote>{inline(ln.lstrip('> '))}</blockquote>")
            i += 1
            continue
        para = [ln.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,6}\s|```|\s*([-*+]|\d+[.)])\s|\s*\||>)", lines[i]):
            para.append(lines[i].strip())
            i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(out)


def counts(folder):
    f = folder / "picks.json"
    if not f.exists():
        return ""
    try:
        d = json.loads(f.read_text(encoding="utf-8-sig"))
    except Exception:  # noqa: BLE001
        return ""
    if isinstance(d, dict):
        d = d.get("picks") or d.get("rows") or list(d.values())
    recs = [str(r.get("rec", "")).lower() for r in d]
    return f"{len(d)} picks · {recs.count('yes')} yes · {recs.count('maybe')} maybe · {recs.count('no')} no"


CSS = """
:root{color-scheme:dark;--bg:#121110;--panel:#1B1A18;--panel-2:#24221F;--line:#34312C;--ink:#ECE7DF;--ink-2:#B7B0A5;--ink-3:#7F786E;
--accent:#FF5A1F;--accent-soft:#3A1D10;--accent-ink:#FFB08F;--good:#5FBF8A;--warn:#E3B341;
--display:"Barlow Condensed","Arial Narrow",Arial,sans-serif;--body:"Atkinson Hyperlegible","Segoe UI",Verdana,sans-serif;--mono:"IBM Plex Mono",Consolas,monospace}
*{box-sizing:border-box}html,body{background:var(--bg);color:var(--ink);margin:0}
body{font:15px/1.55 var(--body);padding-inline:16px;padding-block:0 48px}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.strip{position:sticky;top:0;z-index:5;display:flex;align-items:center;gap:12px;flex-wrap:wrap;min-height:44px;margin-inline:-16px;padding:6px 16px;background:var(--panel);border-bottom:1px solid var(--line)}
.strip h1{margin:0;font:800 20px/1 var(--display);letter-spacing:.06em;text-transform:uppercase}.strip h1 b{color:var(--accent)}
.chip{font:500 11px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase;padding:4px 7px;border:1px solid var(--line);border-radius:3px;color:var(--ink-2)}
.spacer{flex:1}.strip a{color:var(--accent-ink)}
.wrap{max-width:1180px;margin:0 auto;display:grid;grid-template-columns:230px minmax(0,1fr);gap:18px;padding-block:18px}
nav{position:sticky;top:60px;align-self:start;display:grid;gap:2px;max-height:calc(100vh - 80px);overflow:auto}
nav a{display:block;padding:7px 10px;border-radius:4px;color:var(--ink-2);text-decoration:none;font:500 13px var(--mono);border-left:2px solid transparent}
nav a:hover,nav a:focus-visible{background:var(--panel);color:var(--ink)}nav a.on{border-left-color:var(--accent);color:var(--ink);background:var(--panel)}
nav a small{display:block;color:var(--ink-3);font-size:11px}
main{min-width:0;display:grid;gap:18px}
section{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:0 16px 14px;min-width:0}
section>h2{margin:0 -16px 12px;padding:10px 16px;font:700 20px var(--display);letter-spacing:.06em;text-transform:uppercase;border-bottom:1px solid var(--line);display:flex;gap:10px;align-items:center;flex-wrap:wrap}
section>h2 .s{margin-left:auto;font:400 12px var(--mono);color:var(--ink-2);letter-spacing:0;text-transform:none}
section>h2 .s a{color:var(--accent-ink)}
.body h2,.body h3,.body h4{font-family:var(--display);letter-spacing:.04em;text-transform:uppercase;margin:16px 0 6px}
.body h2{font-size:18px;color:var(--accent-ink)}.body h3{font-size:16px}.body h4{font-size:14px;color:var(--ink-2)}
.body p{margin:6px 0}.body ul,.body ol{margin:6px 0;padding-left:22px}.body li{margin:3px 0}
.body code{font:13px var(--mono);background:var(--panel-2);padding:1px 4px;border-radius:3px}
.body pre{font:12.5px/1.45 var(--mono);background:var(--bg);border:1px solid var(--line);border-radius:4px;padding:10px;overflow:auto}
.body table{border-collapse:collapse;width:100%;margin:8px 0;font-size:13.5px}.body th,.body td{border:1px solid var(--line);padding:5px 8px;text-align:left;vertical-align:top}
.body th{background:var(--panel-2);font:500 11px var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--ink-2)}
.body blockquote{margin:8px 0;padding:6px 12px;border-left:3px solid var(--accent);color:var(--ink-2)}
.body a{color:var(--accent-ink)}.body b{color:var(--ink)}
@media (max-width:760px){.wrap{grid-template-columns:minmax(0,1fr)}nav{position:static;max-height:none;grid-template-columns:repeat(auto-fill,minmax(150px,1fr))}}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(SRC / "intake-report.html"))
    ap.add_argument("--picker", default="")
    a = ap.parse_args()
    keys = [k for k in ORDER if (SRC / k / "note.md").exists()]
    keys += sorted(p.parent.relative_to(SRC).as_posix() for p in SRC.rglob("note.md") if p.parent.relative_to(SRC).as_posix() not in keys)
    nav, secs = [], []
    for n, k in enumerate(keys, 1):
        label, line = LABELS.get(k, (k, ""))
        folder = SRC / k
        body = md_to_html(folder.joinpath("note.md").read_text(encoding="utf-8-sig"))
        c = counts(folder)
        repo = "" if k.startswith("articles/") else f'<a href="https://github.com/{k.replace("__", "/")}" target="_blank" rel="noopener">repo</a>'
        sid = re.sub(r"[^a-z0-9]+", "-", k.lower()).strip("-")
        nav.append(f'<a href="#{sid}">{n:02d} {html.escape(label)}<small>{html.escape(c)}</small></a>')
        secs.append(f'<section id="{sid}"><h2>{n:02d} · {html.escape(label)}<span class="s">{html.escape(c)} {repo}</span></h2>'
                    f'<p class="chip" style="display:inline-block;margin:0 0 8px">{html.escape(line)}</p><div class="body">{body}</div></section>')
    picker = f' · <a href="{a.picker}" target="_blank" rel="noopener">the picker</a>' if a.picker else ""
    page = f"""<title>Intake Report</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Atkinson+Hyperlegible:wght@400;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>{CSS}</style>
<header class="strip"><h1><b>Intake</b> Report</h1><span class="chip">BOLO 140</span><span class="spacer"></span>
<span class="chip">{len(keys)} items · 10/12</span><span class="chip">15 specialists, one each{picker}</span></header>
<div class="wrap"><nav aria-label="Items">{''.join(nav)}</nav><main>{''.join(secs)}</main></div>
<script>
const links=[...document.querySelectorAll('nav a')];const secs=links.map(a=>document.querySelector(a.getAttribute('href')));
const io=new IntersectionObserver(es=>{{es.forEach(e=>{{if(e.isIntersecting){{links.forEach(l=>l.classList.toggle('on',l.getAttribute('href')==='#'+e.target.id));}}}});}},{{rootMargin:'-40% 0px -55% 0px'}});
secs.forEach(s=>s&&io.observe(s));
</script>
"""
    Path(a.out).write_text(page, encoding="utf-8")
    print(f"{len(keys)} items → {a.out} ({Path(a.out).stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
