"""roster/build.py — BOLO 139: THE ROSTER, the page that opens with the sit rep at launch (Chief 10/12: "a roster file
that can pop up with the sitrep at the launch sequence").

Reads .claude/agents/*.md (the frontmatter: name, model, tools) and writes _tools/roster/roster.html: the crew seats
(the formation, BOLO 54) on top, then every agent on call, grouped, with its model, what it may touch, and its job in
plain words. Zero tokens. Rebuild after any agent file changes; the launch publishes it to pages.json "roster".
"""
import glob
import html
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(os.path.dirname(__file__), "roster.html")

SEATS = [
    ("CDR", "main session", "Opus (Fable on design days)", "Runs the session, decides who gets called, writes the rulings. Never hands off judgment."),
    ("MS", "Mission Specialist", "Sonnet", "The writer: drafts, rewrites, reviews code. Gets one brief, one set of inputs."),
    ("PS", "Payload Specialist", "Haiku", "The fetcher: pulls, extracts, counts. Cheap and fast; judges by reading."),
    ("RANGE", "the reviewer", "a script, not an agent", "Checks the specialists' output at the fan-in. Never a checker agent."),
]
GROUPS = [
    ("Code care", "Our Python tools: find bugs, quiet failures, holes and slow spots before they bite.",
     ["python-reviewer", "silent-failure-hunter", "security-reviewer", "code-explorer", "performance-optimizer", "refactor-cleaner", "doc-updater"]),
    ("Plans and design", "Before a big build: the plan and the shape of the system.", ["planner", "architect"]),
    ("The DARKROOM engine", "The image tagging and embedding pipeline on the 3090.", ["pytorch-build-resolver", "mle-reviewer"]),
    ("The public repo and the product", "The repo is public and BOLO 138 sells a starter kit: keep secrets out, package it, sell it.",
     ["opensource-sanitizer", "opensource-forker", "opensource-packager", "marketing-agent", "seo-specialist", "a11y-architect"]),
    ("Operations", "Running the Command: messages, long runs, the network, the harness itself.",
     ["chief-of-staff", "loop-operator", "network-troubleshooter", "harness-optimizer", "conversation-analyzer"]),
]
PLAIN = {
    "python-reviewer": "Reads a Python script and points out bugs and messy spots.",
    "silent-failure-hunter": "Finds errors that fail quietly: swallowed exceptions, bad fallbacks, dead runs.",
    "security-reviewer": "Checks code for leaked keys, unsafe inputs and open doors.",
    "code-explorer": "Maps how a piece of code works before anyone changes it.",
    "performance-optimizer": "Finds what's slow and proposes the fix.",
    "refactor-cleaner": "Finds dead and duplicate code and removes it.",
    "doc-updater": "Brings READMEs and docs back in step with the code.",
    "planner": "Turns a big ask into a step-by-step build plan.",
    "architect": "Big-picture system design for a new build.",
    "pytorch-build-resolver": "Fixes PyTorch and CUDA errors in the engine.",
    "mle-reviewer": "Reviews the ML pipeline for repeatability and data mistakes.",
    "opensource-sanitizer": "Scans the repo for secrets and private detail before anything goes public.",
    "opensource-forker": "Copies a project into a clean public version.",
    "opensource-packager": "Adds README, license and setup to a cleaned project.",
    "marketing-agent": "Plans the campaign and drafts the sales copy.",
    "seo-specialist": "Search ranking for a public site.",
    "a11y-architect": "Makes pages readable and usable for everyone.",
    "chief-of-staff": "Sorts messages into skip / FYI / meeting / action and drafts replies. Never sends.",
    "loop-operator": "Watches long runs like the pull waves and flags a stall.",
    "network-troubleshooter": "Diagnoses network problems step by step, read-only.",
    "harness-optimizer": "Tunes the Claude Code setup itself for reliability and cost.",
    "conversation-analyzer": "Reads past sessions for mistakes worth a rule or a hook.",
}


def agents():
    out = {}
    for f in glob.glob(os.path.join(ROOT, ".claude", "agents", "*.md")):
        if f.endswith("README.md"):
            continue
        t = open(f, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---", t, re.S)
        fm = {}
        prof = {}
        if m:
            cur = None
            for l in m.group(1).splitlines():
                if l.startswith((" ", "	")) and cur == "profile":
                    k, _, v = l.strip().partition(":")
                    prof[k.strip()] = v.strip()
                elif ":" in l:
                    k, _, v = l.partition(":")
                    cur = k.strip()
                    if v.strip():
                        fm[cur] = v.strip()
        fm["_profile"] = prof
        name = fm.get("name") or os.path.basename(f)[:-3]
        tools = fm.get("tools", "")
        out[name] = {"model": fm.get("model", "default"), "writes": any(w in tools for w in ("Edit", "Write")), "tools": tools, "profile": fm["_profile"]}
    return out


def tip(name, prof):
    """The agent name, with an optional profile: block as a hover tip (voice, weakness, last jobs, cost)."""
    if not prof:
        return f"<code>{e(name)}</code>"
    jobs = prof.get("last_jobs", "").strip("[]")
    jobs = "; ".join(j.strip().strip('"') for j in jobs.split(",") if j.strip())
    parts = [("Voice", prof.get("voice")), ("Weakness", prof.get("weakness")), ("Last jobs", jobs), ("Cost", prof.get("cost"))]
    body = "".join(f"<b>{k}:</b> {e(v)}<br>" for k, v in parts if v)
    return f'<button class="t" type="button"><code>{e(name)}</code><span class="tip">{body}</span></button>'


def e(s):
    return html.escape(str(s), quote=True)


def build():
    A = agents()
    seats = "".join(f'<div class="seat"><b>{e(a)}</b><span class="role">{e(b)}</span><span class="m">{e(c)}</span><p>{e(d)}</p></div>'
                    for a, b, c, d in SEATS)
    placed, groups = set(), []
    for title, why, names in GROUPS:
        rows = []
        for n in names:
            if n not in A:
                continue
            placed.add(n)
            a = A[n]
            rows.append(f'<tr><td>{tip(n, a["profile"])}</td><td><span class="m {e(a["model"])}">{e(a["model"])}</span></td>'
                        f'<td><span class="rw {"w" if a["writes"] else "r"}">{"writes files" if a["writes"] else "read-only"}</span></td>'
                        f'<td>{e(PLAIN.get(n, ""))}</td></tr>')
        if rows:
            groups.append(f'<section><h2>{e(title)} <small>{e(why)}</small></h2><div class="tw"><table><thead><tr><th>Agent</th><th>Model</th><th>Touches</th><th>Job</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div></section>')
    extra = sorted(set(A) - placed)
    if extra:
        groups.append('<section><h2>Unsorted</h2><p>' + ", ".join(tip(n, A[n]["profile"]) for n in extra) + "</p></section>")
    page = PAGE.replace("{{SEATS}}", seats).replace("{{GROUPS}}", "".join(groups)).replace("{{N}}", str(len(A)))
    open(OUT, "w", encoding="utf-8", newline="\n").write(page)
    return OUT


PAGE = """<title>The Roster</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Atkinson+Hyperlegible:wght@400;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
  /* the Command look, DARK only: the seats first, then the agents on call by what they're for */
  :root { color-scheme: dark;
    --bg:#121110; --panel:#1B1A18; --panel-2:#24221F; --line:#34312C; --ink:#ECE7DF; --ink-2:#B7B0A5; --ink-3:#7F786E;
    --accent:#FF5A1F; --accent-soft:#3A1D10; --accent-ink:#FFB08F; --good:#5FBF8A; --good-soft:#16301F; --warn:#E3B341; --warn-soft:#3A2E10;
    --display:"Barlow Condensed","Arial Narrow",Arial,sans-serif; --body:"Atkinson Hyperlegible","Segoe UI",Verdana,sans-serif; --mono:"IBM Plex Mono",Consolas,monospace; }
  *{box-sizing:border-box} html,body{background:var(--bg);color:var(--ink)}
  body{font:15px/1.5 var(--body);padding-inline:16px;padding-block:0 48px}
  .strip{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;display:flex;align-items:center;gap:10px;flex-wrap:wrap;min-height:44px;margin-inline:-16px;padding:6px 16px;background:var(--panel);border-bottom:1px solid var(--line)}
  .strip h1{margin:0;font:800 20px/1 var(--display);letter-spacing:.06em;text-transform:uppercase} .strip h1 b{color:var(--accent)}
  .chip{font:500 11px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase;padding:4px 7px;border:1px solid var(--line);border-radius:3px;color:var(--ink-2)}
  .spacer{flex:1}
  .wrap{max-width:1000px;margin:0 auto;display:grid;gap:18px;padding-block:16px}
  .note{font-size:14px;color:var(--ink-2);border-left:2px solid var(--accent);padding-left:10px;margin:0}
  .seats{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:8px}
  .seat{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:10px 12px;display:grid;gap:3px;min-width:0}
  .seat b{font:800 22px/1 var(--display);letter-spacing:.06em;color:var(--accent)} .seat .role{font:700 14px var(--body)}
  .seat p{margin:2px 0 0;font-size:13px;color:var(--ink-2)}
  section{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding-bottom:4px;min-width:0}
  h2{margin:0;padding:10px 14px;font:700 18px var(--display);letter-spacing:.06em;text-transform:uppercase;border-bottom:1px solid var(--line);display:flex;gap:10px;flex-wrap:wrap;align-items:baseline}
  h2 small{font:400 13px var(--body);color:var(--ink-3);letter-spacing:0;text-transform:none}
  .tw{overflow-x:auto}
  table{width:100%;border-collapse:collapse;font-size:14px}
  th{text-align:left;font:500 11px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);padding:8px 14px}
  td{padding:7px 14px;border-top:1px solid var(--line);vertical-align:top} td:first-child{white-space:nowrap}
  code{font:13px var(--mono);color:var(--ink)}
  .m{font:500 10px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase;padding:3px 6px;border-radius:3px;background:var(--panel-2);color:var(--ink-2);white-space:nowrap}
  .m.opus{background:var(--accent-soft);color:var(--accent-ink)} .m.haiku{background:var(--good-soft);color:var(--good)}
  .rw{font:500 10px/1 var(--mono);letter-spacing:.06em;text-transform:uppercase;padding:3px 6px;border-radius:3px;white-space:nowrap}
  .rw.r{color:var(--ink-3);border:1px solid var(--line)} .rw.w{background:var(--warn-soft);color:var(--warn)}
  .t{position:relative;border-bottom:1px dotted var(--accent);cursor:help;background:none;border-top:0;border-left:0;border-right:0;padding:0;font:inherit;color:inherit}
  .tip{display:none;position:absolute;left:0;top:calc(100% + 6px);z-index:20;width:min(300px,80vw);padding:8px 10px;background:var(--panel-2);border:1px solid var(--accent);border-radius:4px;font:400 13px/1.45 var(--body);color:var(--ink);box-shadow:0 8px 24px rgba(0,0,0,.5)}
  .t:hover .tip,.t:focus-visible .tip,.t.pin .tip{display:block}
</style>
<header class="strip"><h1><b>The</b> Roster</h1><span class="chip">BOLO 139</span><span class="spacer"></span><span class="chip">{{N}} agents on call</span></header>
<main class="wrap">
  <p class="note">Who's on call. The <button class="t" type="button">seats<span class="tip">The formation (BOLO 54): one main session, specialists on separate inputs, a script at the fan-in. Seats are roles; agents fill them.</span></button> run every job; the agents below are specialists the CDR calls by name. Say "call the python-reviewer on pull_queue.py" and it goes. Each one works in its own space, reports back, and never <button class="t" type="button">grades another agent<span class="tip">The doctrine: a script reviews at the fan-in, never a checker agent.</span></button>. Files live in <code>.claude/agents/</code>.</p>
  <div class="seats">{{SEATS}}</div>
  {{GROUPS}}
</main>
<script>
  document.addEventListener("click", (ev) => { const t = ev.target.closest(".t"); document.querySelectorAll(".t.pin").forEach((x) => { if (x !== t) x.classList.remove("pin"); }); if (t) t.classList.toggle("pin"); });
  document.addEventListener("keydown", (ev) => { if (ev.key === "Escape") document.querySelectorAll(".t.pin").forEach((x) => x.classList.remove("pin")); });
</script>
"""

if __name__ == "__main__":
    print(build())
