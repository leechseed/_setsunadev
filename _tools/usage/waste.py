#!/usr/bin/env python3
"""Zero-token session waste pass over local Claude Code transcripts -> glass page.
Counts names and numbers only; no transcript text is written to the page."""
import argparse, html, json, statistics, subprocess, sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TDIR = Path.home() / ".claude/projects/c--Users-U01-LEECHSEED-Desktop--setsunadev"
MIN = datetime.min.replace(tzinfo=timezone.utc)


def blen(x):
    if isinstance(x, str):
        return len(x.encode("utf-8", "ignore"))
    if isinstance(x, list):
        return sum(blen(i) for i in x)
    if isinstance(x, dict):
        return sum(blen(x.get(k)) for k in ("text", "thinking", "content") if k in x)
    return 0


def scan(path):
    s = dict(id=path.stem[:8], start=None, turns=0, tools=Counter(), bytes=0,
             reads=Counter(), skills=Counter(), agents=Counter(), bad=0)
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            if not line.strip():
                continue
            try:
                d = json.loads(line)
            except Exception:
                s["bad"] += 1
                continue
            if not isinstance(d, dict):
                s["bad"] += 1
                continue
            ts = d.get("timestamp")
            if ts and not s["start"]:
                try:
                    s["start"] = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                except Exception:
                    pass
            m = d.get("message")
            if d.get("type") not in ("user", "assistant") or not isinstance(m, dict):
                continue
            c = m.get("content")
            s["bytes"] += blen(c)
            if d["type"] == "user" and not d.get("isMeta"):
                if isinstance(c, str) or (isinstance(c, list) and any(
                        isinstance(b, dict) and b.get("type") == "text" for b in c)):
                    s["turns"] += 1
            if isinstance(c, list):
                for b in c:
                    if not (isinstance(b, dict) and b.get("type") == "tool_use"):
                        continue
                    n = b.get("name") or "?"
                    inp = b.get("input")
                    s["tools"][n] += 1
                    if not isinstance(inp, dict):
                        continue
                    if n == "Read" and inp.get("file_path"):
                        s["reads"][str(inp["file_path"])] += 1
                    if n == "Skill" and inp.get("skill"):
                        s["skills"][str(inp["skill"])] += 1
                    if n in ("Agent", "Task") and inp.get("subagent_type"):
                        s["agents"][str(inp["subagent_type"])] += 1
    s["tokens"] = s["bytes"] // 4
    return s


def tip(term, text):
    return ('<button class="t" type="button">%s<span class="tip">%s</span></button>'
            % (html.escape(term), html.escape(text)))


def rows(items):
    return "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in items)


CSS = """
:root{color-scheme:dark;--bg:#121110;--panel:#1B1A18;--panel-2:#24221F;--line:#34312C;--ink:#ECE7DF;--ink-2:#B7B0A5;--ink-3:#7F786E;--accent:#FF5A1F;--accent-soft:#3A1D10;--warn:#E3B341;
--display:"Barlow Condensed","Arial Narrow",Arial,sans-serif;--body:"Atkinson Hyperlegible","Segoe UI",Verdana,sans-serif;--mono:"IBM Plex Mono",Consolas,monospace}
*{box-sizing:border-box}html,body{background:var(--bg);color:var(--ink)}body{margin:0;font:15px/1.5 var(--body);padding:0 16px 48px}
.strip{position:sticky;top:0;z-index:5;display:flex;align-items:center;gap:14px;height:44px;margin-inline:-16px;padding:0 16px;background:var(--panel);border-bottom:2px solid var(--accent)}
.strip h1{margin:0;font:800 20px/1 var(--display);letter-spacing:.06em;text-transform:uppercase}.strip h1 b{color:var(--accent)}.strip span{font:12px var(--mono);color:var(--ink-2)}
.wrap{max-width:980px;margin:0 auto;display:grid;gap:18px;padding-block:18px}
section{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding-bottom:12px;min-width:0;overflow-x:auto}
h2{margin:0 0 8px;padding:10px 14px;font:700 18px var(--display);letter-spacing:.06em;text-transform:uppercase;border-bottom:1px solid var(--line)}
section>p{margin:0 14px 8px;color:var(--ink-2);font-size:14px}
table{width:calc(100% - 28px);margin:0 14px;border-collapse:collapse;font:13px var(--mono)}th{text-align:left;color:var(--ink-3);font-weight:500;text-transform:uppercase;font-size:11px;letter-spacing:.08em}
th,td{padding:4px 8px 4px 0;border-bottom:1px solid var(--line);vertical-align:top;word-break:break-word}
.kv{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:1px;background:var(--line);margin:0 14px;border:1px solid var(--line)}.kv div{background:var(--panel);padding:8px 10px}
.kv dt{font:500 11px var(--mono);text-transform:uppercase;color:var(--ink-3)}.kv dd{margin:0;font:800 24px var(--display)}.kv dd.w{color:var(--warn)}
.t{position:relative;font:inherit;color:inherit;background:none;border:0;padding:0;border-bottom:1px dotted var(--accent);cursor:help;text-align:left;text-transform:inherit;letter-spacing:inherit}
.tip{display:none;position:absolute;left:0;top:calc(100% + 6px);z-index:20;width:min(300px,80vw);padding:8px 10px;background:var(--panel-2);border:1px solid var(--accent);border-radius:4px;font:400 13px/1.4 var(--body);color:var(--ink);text-transform:none;letter-spacing:0}
.t:hover .tip,.t:focus-visible .tip,.t.pin .tip{display:block}.chips{margin:0 14px;display:flex;flex-wrap:wrap;gap:6px}.chips code{font:12px var(--mono);background:var(--panel-2);border:1px solid var(--line);padding:2px 6px;border-radius:3px}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
"""
JS = ('document.addEventListener("click",e=>{const t=e.target.closest(".t");'
      'document.querySelectorAll(".t.pin").forEach(x=>x!==t&&x.classList.remove("pin"));if(t)t.classList.toggle("pin")});'
      'document.addEventListener("keydown",e=>{if(e.key==="Escape")document.querySelectorAll(".t.pin").forEach(x=>x.classList.remove("pin"))});')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--out", default=str(ROOT / "_PRIVATE/reference/usage/waste.html"))
    a = ap.parse_args()
    sess = [scan(p) for p in sorted(TDIR.glob("*.jsonl"))]
    cutoff = datetime.now(timezone.utc) - timedelta(days=a.days)
    recent = [s for s in sess if s["start"] and s["start"] >= cutoff]
    total = sum(s["tokens"] for s in sess)
    med = statistics.median([s["tokens"] for s in sess]) if sess else 0
    big = [s for s in sess if s["tokens"] > 2 * med]
    reread = Counter()
    for s in sess:
        for f, n in s["reads"].items():
            if n > 1:
                reread[f] += n - 1
    top = reread.most_common(15)
    skills_used, agents_used, tools_all = Counter(), Counter(), Counter()
    for s in recent:
        skills_used.update(s["skills"])
        agents_used.update(s["agents"])
    for s in sess:
        tools_all.update(s["tools"])
    sk = sorted(p.name for p in (ROOT / ".claude/skills").iterdir() if p.is_dir())
    ag = sorted(p.stem for p in (ROOT / ".claude/agents").glob("*.md") if p.stem.lower() != "readme")
    dead_sk = [x for x in sk if x not in skills_used]
    dead_ag = [x for x in ag if x not in agents_used]
    cl = (ROOT / "CLAUDE.md").read_text(encoding="utf-8", errors="replace")
    cl_lines, cl_bytes = len(cl.splitlines()), len(cl.encode("utf-8"))
    try:
        dg = subprocess.run([sys.executable, str(ROOT / "_tools/sitrep/digest.py")],
                            capture_output=True, timeout=60).stdout
        dg_bytes = len(dg)
    except Exception:
        dg_bytes = -1
    bad = sum(s["bad"] for s in sess)
    e = html.escape
    order = sorted(sess, key=lambda s: s["start"] or MIN, reverse=True)
    sess_rows = rows([(s["id"], s["start"].strftime("%m-%d %H:%M") if s["start"] else "?", s["turns"],
                       sum(s["tools"].values()), "{:,}".format(s["tokens"]),
                       sum(1 for n in s["reads"].values() if n > 1),
                       "yes" if s in big else "",
                       e(", ".join("%s %d" % kv for kv in s["tools"].most_common(4)))) for s in order])
    day = datetime.now().strftime("%Y-%m-%d")
    parts = [
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Session Waste</title><style>' + CSS + '</style></head><body>',
        '<header class="strip"><h1>Session <b>Waste</b></h1><span>%d sessions &middot; last %d d: %d &middot; %s</span></header>'
        % (len(sess), a.days, len(recent), day),
        '<main class="wrap">',
        '<section><h2>Totals</h2><dl class="kv">'
        '<div><dt>Sessions</dt><dd>%d</dd></div><div><dt>Tokens est.</dt><dd>%s</dd></div>'
        '<div><dt>Median / session</dt><dd>%s</dd></div>'
        '<div><dt>%s</dt><dd class="w">%d</dd></div>'
        '<div><dt>CLAUDE.md</dt><dd class="%s">%d/200 lines</dd></div>'
        '<div><dt>Digest</dt><dd>%s B</dd></div><div><dt>Skipped lines</dt><dd>%d</dd></div></dl></section>'
        % (len(sess), "{:,}".format(total), "{:,}".format(int(med)),
           tip("Over 2x median", "Sessions whose token estimate is more than twice the median session. Big sessions are where waste hides."),
           len(big), "w" if cl_lines > 200 else "", cl_lines, "{:,}".format(dg_bytes), bad),
        '<section><h2>Most %s files</h2><table><tr><th>Extra reads</th><th>File</th></tr>%s</table></section>'
        % (tip("re-read", "A file the Read tool opened more than once inside one session. The count is extra reads beyond the first, summed over sessions."),
           rows([(n, e(f)) for f, n in top])),
        '<section><h2>Skills %s (%d/%d)</h2><div class="chips">%s</div><p style="margin-top:10px">Fired: %s</p></section>'
        % (tip("never fired", "Not invoked through the Skill tool in the last %d days of transcripts." % a.days),
           len(dead_sk), len(sk), "".join("<code>%s</code>" % e(x) for x in dead_sk) or "none",
           e(", ".join("%s %d" % kv for kv in skills_used.most_common()) or "none")),
        '<section><h2>Agents %s (%d/%d)</h2><div class="chips">%s</div><p style="margin-top:10px">Launched: %s</p></section>'
        % (tip("never fired", "Not launched through the Agent tool in the last %d days of transcripts." % a.days),
           len(dead_ag), len(ag), "".join("<code>%s</code>" % e(x) for x in dead_ag) or "none",
           e(", ".join("%s %d" % kv for kv in agents_used.most_common()) or "none")),
        '<section><h2>Tool calls, all sessions</h2><table><tr><th>Tool</th><th>Calls</th></tr>%s</table></section>'
        % rows([(e(k), v) for k, v in tools_all.most_common(15)]),
        '<section><h2>Sessions</h2><p>Token estimate is message bytes divided by 4. The 2x column marks sessions over twice the median.</p>'
        '<table><tr><th>Id</th><th>Start</th><th>Turns</th><th>Tools</th><th>Tokens</th><th>Re-read</th><th>2x</th><th>Top tools</th></tr>%s</table></section>'
        % sess_rows,
        '</main><script>' + JS + '</script></body></html>',
    ]
    page = "".join(parts)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print("sessions counted: %d (last %dd: %d) | tokens est: %s | median %s | over 2x: %d"
          % (len(sess), a.days, len(recent), "{:,}".format(total), "{:,}".format(int(med)), len(big)))
    print("top re-read: " + "; ".join("%s x%d" % (Path(f).name, n) for f, n in top[:3]))
    print("never-fired skills (%d/%d): %s" % (len(dead_sk), len(sk), ", ".join(dead_sk)))
    print("never-launched agents (%d/%d): %s" % (len(dead_ag), len(ag), ", ".join(dead_ag)))
    print("CLAUDE.md %d/200 lines (%d B) | digest %d B | bad lines %d | page %d KB"
          % (cl_lines, cl_bytes, dg_bytes, bad, len(page.encode()) // 1024))


if __name__ == "__main__":
    main()
