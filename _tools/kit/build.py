"""kit/build.py — THE KIT (10/13): every skill, agent, hook and workflow the Command runs, on one glass, with what each
does, how it fires, where it came from (organic or adopted from a GitHub repo) and which BOLOs name it.

Chief, 10/13: "give me a fucking glass of all the skills that we use and all the agents that we use with the description",
the first step of wiring the GitHub-sourced agents and workflows into every live BOLO.

Reads .claude/skills/*/SKILL.md, .claude/agents/*.md, .claude/settings.local.json (hooks), .claude/workflows/*.js,
BOLO.md (mentions) and _tools/bolocheck/live.json (live vs cosmoline). Zero tokens. Writes _tools/kit/kit.html.
Usage: python _tools/kit/build.py
"""
import glob
import html
import json
import os
import re
import sys
import time

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(os.path.dirname(__file__), "kit.html")
sys.path.insert(0, os.path.join(ROOT, "_tools", "roster"))
try:
    from build import GROUPS  # the Roster's agent groups (BOLO 139)
except Exception:
    GROUPS = []
e = lambda s: html.escape(str(s or ""), quote=True)

HOOKS = {   # what each hook script does, in plain words
    "digest.py": "Prints the session-open digest, so the session never reads the five big files.",
    "autocommit.sh": "Commits the tree locally at the end of every turn. Never pushes.",
    "no_probe.py": "Blocks commands that scan the box unless the order names it (ruled 9/19).",
    "order_hint.py": "Spots the proword in Chief's message and names the order before the turn starts.",
    "precompact_backup.py": "Saves the transcript before the context gets compacted.",
}


def front(path):
    t = open(path, encoding="utf-8", errors="replace").read()
    m = re.match(r"---\n(.*?)\n---\n", t, re.S)
    fm = {}
    if m:
        for ln in m.group(1).splitlines():
            mm = re.match(r"^(\w[\w-]*):\s*(.*)$", ln)
            if mm:
                fm[mm.group(1)] = mm.group(2).strip().strip('"')
    src = re.findall(r"<!--\s*adapted from (.*?)-->", t)
    return fm, t, (src[-1].strip() if src else "")


def plain(desc):
    d = re.sub(r"\s*Use when the CDR needs this:.*$", "", desc or "")
    return d.strip()


def repo_of(src):
    m = re.search(r"github\.com/([\w.-]+/[\w.-]+)", src or "")
    if m:
        return m.group(1)
    m = re.match(r"(\w[\w-]*)\s", src or "")
    return m.group(1) if m else ""


def main():
    bolo = open(os.path.join(ROOT, "BOLO.md"), encoding="utf-8", errors="replace").read().split("\n")
    rows = [(int(m.group(1)), l) for l in bolo for m in [re.match(r"^\| *(\d+) *\|", l)] if m]
    try:
        live = set(json.load(open(os.path.join(ROOT, "_tools", "bolocheck", "live.json"), encoding="utf-8"))["live"])
    except Exception:
        live = set()

    def bolos_naming(name):
        rx = re.compile(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])", re.I)
        return sorted({n for n, l in rows if rx.search(l)})

    def bchips(ns):
        if not ns:
            return '<span class="none">no BOLO names it yet</span>'
        return "".join(f'<span class="b{" lv" if n in live else ""}" title="{"live BOLO" if n in live else "BOLO"} {n}">{n}</span>' for n in ns[:14]) + \
               (f'<span class="more">+{len(ns) - 14}</span>' if len(ns) > 14 else "")

    items = []
    # skills
    for p in sorted(glob.glob(os.path.join(ROOT, ".claude", "skills", "*", "SKILL.md"))):
        fm, t, src = front(p)
        name = fm.get("name") or os.path.basename(os.path.dirname(p))
        d = fm.get("description", "")
        says = re.findall(r'"([^"]{2,40})"', d)[:6]
        items.append(dict(kind="skill", name=name, desc=plain(d), says=says, src=src, repo=repo_of(src), meta="",
                          path=os.path.relpath(p, ROOT).replace("\\", "/"), bolos=bolos_naming(name)))
    # agents
    grp = {n: g for g, _, names in GROUPS for n in names}
    for p in sorted(glob.glob(os.path.join(ROOT, ".claude", "agents", "*.md"))):
        if os.path.basename(p).lower() == "readme.md":
            continue
        fm, t, src = front(p)
        name = fm.get("name") or os.path.splitext(os.path.basename(p))[0]
        items.append(dict(kind="agent", name=name, desc=plain(fm.get("description", "")), says=[], src=src, repo=repo_of(src),
                          meta=f'{fm.get("model", "inherits")} · {fm.get("tools", "all tools")}', group=grp.get(name, ""),
                          path=os.path.relpath(p, ROOT).replace("\\", "/"), bolos=bolos_naming(name)))
    # hooks
    try:
        hk = json.load(open(os.path.join(ROOT, ".claude", "settings.local.json"), encoding="utf-8")).get("hooks", {})
    except Exception:
        hk = {}
    for event, lst in hk.items():
        for h in lst:
            for c in h.get("hooks", []):
                script = os.path.basename(re.findall(r'[\w.-]+\.(?:py|sh)', c.get("command", ""))[-1]) if re.findall(r'[\w.-]+\.(?:py|sh)', c.get("command", "")) else c.get("command", "")
                items.append(dict(kind="hook", name=script, desc=HOOKS.get(script, "A hook script."), says=[], src="", repo="",
                                  meta=f"fires on {event}" + (f" · {h.get('matcher')}" if h.get("matcher") else ""), path=".claude/settings.local.json",
                                  bolos=bolos_naming(script.rsplit(".", 1)[0])))
    # workflows
    for p in sorted(glob.glob(os.path.join(ROOT, ".claude", "workflows", "*.js"))):
        t = open(p, encoding="utf-8", errors="replace").read()
        m = re.search(r"description:\s*'([^']*)'", t)
        name = os.path.splitext(os.path.basename(p))[0]
        items.append(dict(kind="workflow", name=name, desc=m.group(1) if m else "", says=[], src="", repo="", meta="a Workflow script",
                          path=os.path.relpath(p, ROOT).replace("\\", "/"), bolos=bolos_naming(name + ".js")))

    counts = {k: sum(1 for i in items if i["kind"] == k) for k in ("skill", "agent", "hook", "workflow")}
    adopted = sum(1 for i in items if i["repo"])
    repos = sorted({i["repo"] for i in items if i["repo"]})
    cards = []
    for i in items:
        says = "".join(f'<span class="say">{e(s)}</span>' for s in i["says"])
        src = (f'<span class="src gh" title="{e(i["src"])}">from {e(i["repo"])}</span>' if i["repo"]
               else '<span class="src org">organic</span>')
        cards.append(f'''<article class="it {i["kind"]}" data-k="{i["kind"]}" data-o="{"gh" if i["repo"] else "org"}" data-s="{e((i["name"] + " " + i["desc"] + " " + i.get("group", "")).lower())}">
  <header><span class="kd">{i["kind"]}</span><h3>{e(i["name"])}</h3>{src}</header>
  <p>{e(i["desc"])}</p>
  {f'<div class="says"><span class="lb">Say</span>{says}</div>' if says else ""}
  <div class="meta">{e(i.get("group") or "")}{" · " if i.get("group") and i["meta"] else ""}{e(i["meta"])}</div>
  <div class="bl"><span class="lb">BOLOs</span>{bchips(i["bolos"])}</div>
  <div class="pth">{e(i["path"])}</div>
</article>''')
    built = time.strftime("%b %d, %I:%M %p").replace(" 0", " ")
    page = f"""<title>The Kit</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Atkinson+Hyperlegible:wght@400;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
  /* the Command look, DARK only (ruled 9/11): one strip, a filter row, then a card per skill, agent, hook and workflow */
  :root {{ color-scheme: dark;
    --bg:#121110; --panel:#1B1A18; --panel-2:#24221F; --line:#34312C; --ink:#ECE7DF; --ink-2:#B7B0A5; --ink-3:#7F786E;
    --accent:#FF5A1F; --accent-soft:#3A1D10; --accent-ink:#FFB08F; --good:#5FBF8A; --good-soft:#16301F; --cyan:#7FC4D8; --cyan-soft:#14262E; --warn:#E3B341;
    --display:"Barlow Condensed","Arial Narrow",Arial,sans-serif; --body:"Atkinson Hyperlegible","Segoe UI",Verdana,sans-serif; --mono:"IBM Plex Mono",Consolas,monospace; }}
  *{{box-sizing:border-box}} html,body{{background:var(--bg);color:var(--ink)}}
  body{{font:14px/1.5 var(--body);padding-inline:16px;padding-block:0 64px}}
  :focus-visible{{outline:2px solid var(--accent);outline-offset:2px}}
  .strip{{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;display:flex;align-items:center;gap:14px;flex-wrap:wrap;min-height:44px;margin-inline:-16px;padding:6px 16px;background:var(--panel);border-bottom:1px solid var(--line)}}
  .strip h1{{margin:0;font:800 20px/1 var(--display);letter-spacing:.06em;text-transform:uppercase}} .strip h1 b{{color:var(--accent)}}
  .tot{{font:700 16px var(--display);letter-spacing:.04em;font-variant-numeric:tabular-nums}} .tot span{{color:var(--accent)}}
  .wrap{{max-width:1100px;margin:0 auto;display:grid;gap:12px;padding-block:14px}}
  .lede{{margin:0;color:var(--ink-2);max-width:74ch}}
  .tools{{display:flex;flex-wrap:wrap;gap:6px;align-items:center}}
  .tools button{{font:500 12px var(--mono);padding:5px 9px;border:1px solid var(--line);border-radius:3px;background:var(--panel);color:var(--ink-2);cursor:pointer}}
  .tools button[aria-pressed="true"]{{border-color:var(--accent);color:var(--ink);background:var(--accent-soft)}}
  #q{{flex:1;min-width:180px;font:13px var(--mono);padding:6px 9px;background:var(--panel);color:var(--ink);border:1px solid var(--line);border-radius:3px}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:8px}}
  .it{{background:var(--panel);border:1px solid var(--line);border-top:3px solid var(--line);border-radius:4px;padding:10px 12px;display:grid;gap:6px;align-content:start;min-width:0}}
  .it.skill{{border-top-color:var(--accent)}} .it.agent{{border-top-color:var(--cyan)}} .it.hook{{border-top-color:var(--warn)}} .it.workflow{{border-top-color:var(--good)}}
  .it header{{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap}}
  .kd{{font:500 10px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--ink-3)}}
  .it h3{{margin:0;font:700 19px/1.1 var(--display);letter-spacing:.02em;overflow-wrap:anywhere}}
  .src{{margin-left:auto;font:10.5px var(--mono);padding:1px 6px;border-radius:3px}}
  .src.gh{{background:var(--cyan-soft);color:var(--cyan)}} .src.org{{background:var(--accent-soft);color:var(--accent-ink)}}
  .it p{{margin:0;color:var(--ink-2);font-size:13.5px}}
  .lb{{font:500 10px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3);margin-right:6px}}
  .says,.bl{{display:flex;flex-wrap:wrap;gap:4px;align-items:center}}
  .say{{font:12px var(--mono);border:1px dashed var(--accent);border-radius:3px;padding:0 6px;color:var(--ink)}}
  .b{{font:11px var(--mono);padding:0 5px;border:1px solid var(--line);border-radius:3px;color:var(--ink-3)}} .b.lv{{border-color:var(--good);color:var(--good)}}
  .none,.more{{font:11px var(--mono);color:var(--ink-3)}}
  .meta{{font:11.5px var(--mono);color:var(--ink-3);overflow-wrap:anywhere}}
  .pth{{font:10.5px var(--mono);color:var(--ink-3);opacity:.7;overflow-wrap:anywhere}}
  .key{{display:flex;gap:14px;flex-wrap:wrap;font:11.5px var(--mono);color:var(--ink-3)}} .key i{{display:inline-block;width:10px;height:10px;margin-right:5px;vertical-align:-1px}}
</style>
<header class="strip">
  <h1><b>The</b> Kit</h1>
  <span class="tot"><span>{counts["skill"]}</span> skills · <span>{counts["agent"]}</span> agents · <span>{counts["hook"]}</span> hooks · <span>{counts["workflow"]}</span> workflow</span>
  <span class="tot"><span>{adopted}</span> adopted from GitHub</span>
</header>
<main class="wrap">
  <p class="lede">Everything the Command runs. A <b>skill</b> is a procedure you fire with a proword. An <b>agent</b> is a specialist the main session sends on one job. A <b>hook</b> runs by itself on an event. A <b>workflow</b> is a script that runs a whole formation. Each card says what it does, how you fire it, where it came from, and which BOLOs name it (green = a live BOLO). Repos it draws on: {e(", ".join(repos)) or "none yet"}. Built {built}.</p>
  <div class="key"><span><i style="background:var(--accent)"></i>skill</span><span><i style="background:var(--cyan)"></i>agent</span><span><i style="background:var(--warn)"></i>hook</span><span><i style="background:var(--good)"></i>workflow</span></div>
  <div class="tools" role="group" aria-label="Show">
    <button type="button" data-f="all" aria-pressed="true">All {len(items)}</button>
    <button type="button" data-f="skill" aria-pressed="false">Skills</button>
    <button type="button" data-f="agent" aria-pressed="false">Agents</button>
    <button type="button" data-f="hook" aria-pressed="false">Hooks</button>
    <button type="button" data-f="gh" aria-pressed="false">From GitHub</button>
    <button type="button" data-f="org" aria-pressed="false">Organic</button>
    <input id="q" type="search" placeholder="search the kit…" aria-label="Search the kit">
  </div>
  <div class="grid" id="grid">{"".join(cards)}</div>
</main>
<script>
  let f = "all", term = "";
  const its = Array.from(document.querySelectorAll(".it"));
  function render() {{ for (const el of its) el.hidden = !((f === "all" || el.dataset.k === f || el.dataset.o === f) && (!term || el.dataset.s.includes(term))); }}
  document.addEventListener("click", (ev) => {{ const b = ev.target.closest(".tools button[data-f]"); if (!b) return;
    f = b.dataset.f; document.querySelectorAll(".tools button[data-f]").forEach((x) => x.setAttribute("aria-pressed", x === b)); render(); }});
  document.getElementById("q").addEventListener("input", (ev) => {{ term = ev.target.value.trim().toLowerCase(); render(); }});
</script>
"""
    open(OUT, "w", encoding="utf-8").write(page)
    print(f"wrote {OUT} · {counts} · adopted {adopted} from {repos}")


if __name__ == "__main__":
    main()
