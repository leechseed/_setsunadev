"""THE ARMORY (BOLO 154, Chief 10/17): every tool, skill, agent, MCP tool and workflow the Command has used,
counted from the local session transcripts as far back as they go, plus the roster of skills and agents on disk
with the date git first saw each one. Zero tokens: a script reads, a page shows.

  python _tools/armory/armory.py            # collect + build the glass
  python _tools/armory/armory.py --json     # also print the summary counts

Reads   ~/.claude/projects/*/*.jsonl (the main line) and */subagents/*.jsonl (agents' own calls)
        .claude/skills/*/SKILL.md · .claude/agents/*.md · git log for each file's first commit
Writes  _PRIVATE/reference/armory/armory.json · _PRIVATE/reference/armory/armory.html
Only names, counts and dates leave the transcripts; no prompt, argument or result text is kept.
"""
import glob, html, io, json, os, re, subprocess, sys
from collections import defaultdict
from datetime import datetime, timezone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PROJECTS = os.path.join(os.path.expanduser("~"), ".claude", "projects")
OUTDIR = os.path.join(ROOT, "_PRIVATE", "reference", "armory")
BUILTIN_AGENTS = {"general-purpose", "Explore", "Plan", "claude-code-guide", "statusline-setup", "claude", "fork"}


def local(ts):
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone()
    except Exception:
        return None


def classify(name, inp):
    """-> (kind, key, extra)"""
    if name == "Skill":
        return "skill", (inp or {}).get("skill") or "?", None
    if name in ("Agent", "Task"):
        return "agent", (inp or {}).get("subagent_type") or "general-purpose", (inp or {}).get("model") or "inherit"
    if name == "Workflow":
        return "workflow", (inp or {}).get("name") or "inline script", None
    if name.startswith("mcp__"):
        parts = name.split("__")
        return "mcp", name, parts[1] if len(parts) > 2 else "?"
    return "tool", name, None


def collect():
    files = []
    for proj in glob.glob(os.path.join(PROJECTS, "*")):
        files += [(f, "main") for f in glob.glob(os.path.join(proj, "*.jsonl"))]
        files += [(f, "agent") for f in glob.glob(os.path.join(proj, "*", "subagents", "*.jsonl"))]
    calls, seen, errors, sessions, typed = [], set(), defaultdict(int), set(), []
    first_ts = last_ts = None
    for path, caller in files:
        try:
            fh = io.open(path, encoding="utf-8", errors="replace")
        except OSError:
            continue
        with fh:
            for line in fh:
                has_use, has_err, has_cmd = '"tool_use"' in line, '"is_error":true' in line, "<command-name>" in line
                if not (has_use or has_err or has_cmd):
                    continue
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                msg = rec.get("message") or {}
                content = msg.get("content")
                ts = local(rec.get("timestamp") or "")
                if ts:
                    first_ts = ts if not first_ts or ts < first_ts else first_ts
                    last_ts = ts if not last_ts or ts > last_ts else last_ts
                sid = rec.get("sessionId") or os.path.basename(path)
                if isinstance(content, list):
                    for c in content:
                        if not isinstance(c, dict):
                            continue
                        if c.get("type") == "tool_use" and c.get("id") not in seen:
                            seen.add(c.get("id"))
                            kind, key, extra = classify(c.get("name") or "?", c.get("input"))
                            desc = ((c.get("input") or {}).get("description") or "")[:60] if kind == "agent" else ""
                            calls.append({"id": c.get("id"), "kind": kind, "key": key, "extra": extra, "desc": desc,
                                          "day": ts.strftime("%Y-%m-%d") if ts else None, "ts": ts.isoformat() if ts else None,
                                          "sid": sid, "caller": caller})
                            sessions.add(sid)
                        elif c.get("type") == "tool_result" and c.get("is_error"):
                            body = c.get("content")
                            text = body if isinstance(body, str) else json.dumps(body)[:400]
                            why = "denied" if ("denied" in text or "hook error" in text) else "error"
                            errors[(c.get("tool_use_id"), why)] += 1
                if has_cmd and rec.get("type") == "user":
                    raw = content if isinstance(content, str) else json.dumps(content)
                    for m in re.finditer(r"<command-name>/?([\w:.-]+)</command-name>", raw):
                        typed.append({"key": m.group(1), "day": ts.strftime("%Y-%m-%d") if ts else None})
    err_by_id = defaultdict(lambda: {"error": 0, "denied": 0})
    for (tid, why), n in errors.items():
        err_by_id[tid][why] += n
    return calls, err_by_id, sessions, typed, first_ts, last_ts, len(files)


def keep(calls, err_by_id):
    """Claude Code deletes transcripts after ~30 days. Every call seen is appended to a ledger once (by its id),
    so the Armory keeps its history after the transcript is gone. Returns the full ledger."""
    path = os.path.join(OUTDIR, "ledger.jsonl")
    old = {}
    if os.path.exists(path):
        with io.open(path, encoding="utf-8") as f:
            for line in f:
                try:
                    r = json.loads(line)
                    old[r["id"]] = r
                except (ValueError, KeyError):
                    continue
    new = []
    for c in calls:
        if c["id"] in old:
            continue
        e = err_by_id.get(c["id"]) or {}
        rec = {**c, "error": bool(e.get("error")), "denied": bool(e.get("denied"))}
        old[c["id"]] = rec
        new.append(rec)
    os.makedirs(OUTDIR, exist_ok=True)
    with io.open(path, "a", encoding="utf-8") as f:
        for r in new:
            f.write(json.dumps(r) + "\n")
    return list(old.values()), len(new)


def roster():
    out = []
    for kind, pat in (("skill", ".claude/skills/*/SKILL.md"), ("agent", ".claude/agents/*.md")):
        for f in sorted(glob.glob(os.path.join(ROOT, pat))):
            if os.path.basename(f).lower() == "readme.md":
                continue
            txt = io.open(f, encoding="utf-8", errors="replace").read(4000)
            name = re.search(r"^name:\s*(.+)$", txt, re.M)
            model = re.search(r"^model:\s*(.+)$", txt, re.M)
            rel = os.path.relpath(f, ROOT).replace("\\", "/")
            born = subprocess.run(["git", "log", "--diff-filter=A", "--follow", "--format=%ad", "--date=short", "--", rel],
                                  cwd=ROOT, capture_output=True, text=True).stdout.strip().splitlines()
            fallback = os.path.basename(os.path.dirname(f)) if kind == "skill" else os.path.basename(f)[:-3]
            out.append({"kind": kind, "key": name.group(1).strip().strip("'\"") if name else fallback,
                        "model": model.group(1).strip() if model else None, "path": rel, "born": born[-1] if born else None})
    return out


def summarize(calls, err_by_id, typed, rost):
    items = {}
    for c in calls:
        k = (c["kind"], c["key"])
        it = items.setdefault(k, {"kind": c["kind"], "key": c["key"], "n": 0, "sessions": set(), "days": defaultdict(int),
                                  "first": None, "last": None, "by_agent": 0, "extra": defaultdict(int), "error": 0, "denied": 0,
                                  "desc": defaultdict(int)})
        it["n"] += 1
        if c.get("desc"):
            it["desc"][c["desc"]] += 1
        it["sessions"].add(c["sid"])
        if c["day"]:
            it["days"][c["day"]] += 1
        if c["ts"]:
            it["first"] = min(it["first"] or c["ts"], c["ts"])
            it["last"] = max(it["last"] or c["ts"], c["ts"])
        if c["caller"] == "agent":
            it["by_agent"] += 1
        if c["extra"]:
            it["extra"][c["extra"]] += 1
        it["error"] += 1 if c.get("error") else 0
        it["denied"] += 1 if c.get("denied") else 0
    on_disk_skills = {r["key"] for r in rost if r["kind"] == "skill"}
    for t in typed:   # what Chief typed as /commands: his skills, plugin skills (with a colon), or Claude Code's own commands
        kind = "skill" if (t["key"] in on_disk_skills or ":" in t["key"] or ("skill", t["key"]) in items) else "command"
        it = items.setdefault((kind, t["key"]), {"kind": kind, "key": t["key"], "n": 0, "sessions": set(), "days": defaultdict(int),
                                                 "first": None, "last": None, "by_agent": 0, "extra": defaultdict(int), "error": 0, "denied": 0,
                                                 "desc": defaultdict(int)})
        it["extra"]["typed by Chief"] += 1
        if kind == "command":
            it["n"] += 1
            if t["day"]:
                it["days"][t["day"]] += 1
                it["first"] = min(it["first"] or t["day"], t["day"])
                it["last"] = max(it["last"] or t["day"], t["day"])
    born = {(r["kind"], r["key"]): r for r in rost}
    rows = []
    for (kind, key), it in items.items():
        r = born.get((kind, key))
        rows.append({**it, "sessions": len(it["sessions"]), "days": dict(it["days"]), "extra": dict(it["extra"]),
                     "desc": dict(sorted(it["desc"].items(), key=lambda kv: -kv[1])[:6]),
                     "born": r["born"] if r else None, "on_disk": bool(r), "model": r["model"] if r else None})
    used = {(r["kind"], r["key"]) for r in rows}
    idle = [r for r in rost if (r["kind"], r["key"]) not in used]
    return sorted(rows, key=lambda r: -r["n"]), idle


# ---------------------------------------------------------------- the page

def e(s):
    return html.escape(str(s), quote=True)


def md(iso_or_day):
    if not iso_or_day:
        return "—"
    d = datetime.fromisoformat(iso_or_day) if "T" in iso_or_day else datetime.strptime(iso_or_day, "%Y-%m-%d")
    return f"{d.month}/{d.day}"


def spark(days, all_days, peak):
    w, h, n = 120, 22, max(len(all_days), 1)
    bw = w / n
    bars = "".join(f'<rect x="{i * bw:.2f}" y="{h - max(1.5, h * days.get(d, 0) / peak):.2f}" width="{max(bw - .6, .8):.2f}" height="{max(1.5, h * days.get(d, 0) / peak):.2f}"/>'
                   for i, d in enumerate(all_days) if days.get(d))
    return f'<svg class="sp" viewBox="0 0 {w} {h}" preserveAspectRatio="none" aria-hidden="true">{bars}</svg>'


TERMS = {
    "tool": "A built-in Claude Code tool: Read, Edit, Bash and the rest. Each call is one action on the box or the repo.",
    "skill": "A packaged procedure in .claude/skills/ (sit rep, Oscar Mike, launch). Fired by the main line, or typed by Chief as a /command.",
    "agent": "A subagent deployed with the Agent tool. The type names its role file in .claude/agents/ or a built-in role.",
    "mcp": "A tool served by an MCP server: JUDY's seven, the read-only SQLite, Gmail, Drive, Figma and the rest.",
    "workflow": "A multi-agent Workflow script run by the main line.",
    "command": "A Claude Code slash command Chief typed (/model, /context and the like). Not a skill; counted from his own messages.",
    "byagent": "Calls made from inside a subagent's own transcript, not by the main line.",
    "denied": "Calls refused by a permission rule, a hook or the auto-mode guard.",
    "idle": "On disk in .claude/skills/ or .claude/agents/, but never fired in the transcripts we still hold.",
    "window": "Claude Code deletes transcripts after about 30 days, so counts start at the oldest transcript still on disk. Git births go back further.",
}


def term(label, key):
    return f'<button class="t" type="button">{e(label)}<span class="tip" role="tooltip">{e(TERMS[key])}</span></button>'


def build(data):
    rows, idle, meta = data["rows"], data["idle"], data["meta"]
    all_days = meta["days"]
    kinds = [("agent", "Agents deployed"), ("skill", "Skills fired"), ("mcp", "MCP tools"), ("tool", "Built-in tools"), ("workflow", "Workflows"), ("command", "Commands typed")]
    tot = {k: sum(r["n"] for r in rows if r["kind"] == k) for k, _ in kinds}
    # the daily stack chart
    per_day = {d: defaultdict(int) for d in all_days}
    for r in rows:
        for d, n in r["days"].items():
            if d in per_day:
                per_day[d][r["kind"]] += n
    peak = max([sum(v.values()) for v in per_day.values()] or [1]) or 1
    W, H, PADL, PADB = 960, 200, 34, 22
    bw = (W - PADL) / max(len(all_days), 1)
    order = ["tool", "mcp", "command", "skill", "agent", "workflow"]
    bars = []
    for i, d in enumerate(all_days):
        y = H - PADB
        for k in order:
            n = per_day[d][k]
            if not n:
                continue
            hh = (H - PADB - 8) * n / peak
            y -= hh
            bars.append(f'<rect class="k-{k}" x="{PADL + i * bw + .5:.1f}" y="{y:.1f}" width="{max(bw - 1, 1):.1f}" height="{hh:.1f}"><title>{md(d)} · {k} {n:,}</title></rect>')
    ticks = []
    for frac in (0, .5, 1):
        v = round(peak * frac)
        y = H - PADB - (H - PADB - 8) * frac
        ticks.append(f'<line x1="{PADL}" x2="{W}" y1="{y:.1f}" y2="{y:.1f}" class="grid"/><text x="{PADL - 6}" y="{y + 4:.1f}" text-anchor="end">{v:,}</text>')
    step = max(1, len(all_days) // 8)
    for i, d in enumerate(all_days):
        if i % step == 0 or i == len(all_days) - 1:
            ticks.append(f'<text x="{PADL + i * bw + bw / 2:.1f}" y="{H - 6}" text-anchor="middle">{md(d)}</text>')
    chart = f'<svg class="chart" viewBox="0 0 {W} {H}" role="img" aria-label="calls per day by kind">{"".join(ticks)}{"".join(bars)}</svg>'

    def table(kind, label, tkey):
        rs = [r for r in rows if r["kind"] == kind]
        if not rs:
            return ""
        pk = max([max(r["days"].values() or [1]) for r in rs] or [1])
        body = []
        for r in rs:
            ext = ", ".join(f"{k} ×{v}" for k, v in sorted(r["extra"].items(), key=lambda kv: -kv[1])[:3])
            flags = []
            if r["denied"]:
                flags.append(f'<span class="flag deny">{r["denied"]} denied</span>')
            if r["error"]:
                flags.append(f'<span class="flag err">{r["error"]} errors</span>')
            if kind == "skill" and not r["on_disk"]:
                flags.append('<span class="flag gone">built-in</span>')
            if kind == "agent" and not r["on_disk"]:
                flags.append('<span class="flag gone">built-in</span>' if r["key"] in BUILTIN_AGENTS else '<span class="flag gone">not on disk</span>')
            if kind == "agent" and r.get("desc"):
                ext = (ext + " · " if ext else "") + "briefs: " + "; ".join(f"{k} ×{v}" if v > 1 else k for k, v in list(r["desc"].items())[:4])
            name = r["key"].replace("mcp__", "").replace("__", " · ") if kind == "mcp" else r["key"]
            body.append(f'<tr><th scope="row"><span class="nm">{e(name)}</span>{"".join(flags)}{f"<small>{e(ext)}</small>" if ext else ""}</th>'
                        f'<td class="num">{r["n"]:,}</td><td class="num">{r["sessions"]}</td><td class="num">{r["by_agent"]:,}</td>'
                        f'<td>{md(r["first"])}</td><td>{md(r["last"])}</td><td>{md(r["born"]) if r["born"] else "—"}</td>'
                        f'<td>{spark(r["days"], all_days, pk)}</td></tr>')
        return (f'<section id="{kind}"><h2>{term(label, tkey)}<span class="s"><b>{len(rs)}</b> kinds · <b>{tot[kind]:,}</b> calls</span></h2>'
                f'<div class="tbl"><table><thead><tr><th scope="col">Name</th><th scope="col" class="num">Calls</th><th scope="col" class="num">Sessions</th>'
                f'<th scope="col" class="num">{term("By agents", "byagent")}</th><th scope="col">First</th><th scope="col">Last</th><th scope="col">Born</th>'
                f'<th scope="col">Per day</th></tr></thead><tbody>{"".join(body)}</tbody></table></div></section>')

    idle_rows = "".join(f'<li><span>{e(r["key"])}</span><em>{e(r["kind"])}{" · " + e(r["model"]) if r["model"] else ""}</em><b>{md(r["born"]) if r["born"] else "—"}</b></li>'
                        for r in sorted(idle, key=lambda r: (r["kind"], r["key"]))) or "<li><span>none: everything on disk has fired</span></li>"
    kv = "".join(f'<div><dt>{e(lbl)}</dt><dd>{tot[k]:,}</dd></div>' for k, lbl in kinds) + \
         f'<div><dt>Sessions</dt><dd>{meta["sessions"]:,}</dd></div>'
    page = PAGE
    for k, v in {
        "WHEN": meta["built"], "FROM": md(meta["first"]), "CHARTFROM": md(meta["days"][0]) if meta["days"] else "—", "EARLY": e(meta.get("early") or ""), "TO": md(meta["last"]), "NDAYS": str(len(all_days)),
        "TOTAL": f'{sum(tot.values()):,}', "FILES": f'{meta["files"]:,}', "KV": kv, "CHART": chart,
        "AGENTS": table("agent", "Agents", "agent"), "SKILLS": table("skill", "Skills", "skill"), "MCP": table("mcp", "MCP tools", "mcp"),
        "TOOLS": table("tool", "Built-in tools", "tool"), "WORKFLOWS": table("workflow", "Workflows", "workflow"),
        "COMMANDS": table("command", "Commands typed", "command"),
        "IDLE": idle_rows, "NIDLE": str(len(idle)), "T_IDLE": term("On the shelf, never fired", "idle"), "T_WINDOW": term("the window", "window"),
        "T_DENIED": term("denied", "denied"),
    }.items():
        page = page.replace("{{" + k + "}}", v)
    out = os.path.join(OUTDIR, "armory.html")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(page)
    return out


PAGE = """<title>The Armory</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Atkinson+Hyperlegible:wght@400;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
  /* the Command look, DARK only (ruled 9/11): one strip, the totals and the daily chart, then one table per kind; the shelf of never-fired last */
  :root { color-scheme: dark;
    --bg:#121110; --panel:#1B1A18; --panel-2:#24221F; --line:#34312C; --ink:#ECE7DF; --ink-2:#B7B0A5; --ink-3:#7F786E;
    --accent:#FF5A1F; --accent-soft:#3A1D10; --accent-ink:#FFB08F; --good:#5FBF8A; --warn:#E3B341; --warn-soft:#3A2E10; --bad:#E5604D; --bad-soft:#3A1612;
    --k-tool:#7F786E; --k-mcp:#5FBF8A; --k-skill:#E3B341; --k-agent:#FF5A1F; --k-workflow:#B48EF0; --k-command:#6FA8DC;
    --display:"Barlow Condensed","Arial Narrow",Arial,sans-serif; --body:"Atkinson Hyperlegible","Segoe UI",Verdana,sans-serif; --mono:"IBM Plex Mono",Consolas,monospace; }
  *{box-sizing:border-box} html,body{background:var(--bg);color:var(--ink)}
  body{font:15px/1.5 var(--body);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0 48px}
  body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--panel)}
  :focus-visible{outline:2px solid var(--accent);outline-offset:2px}
  .strip{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;display:flex;align-items:center;gap:12px;flex-wrap:wrap;min-height:44px;margin-inline:-16px;padding:6px 16px;background:var(--panel);border-bottom:1px solid var(--line)}
  .strip h1{margin:0;font:800 20px/1 var(--display);letter-spacing:.06em;text-transform:uppercase} .strip h1 b{color:var(--accent)}
  .chip{font:500 11px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase;padding:4px 7px;border:1px solid var(--line);border-radius:3px;color:var(--ink-2)}
  .spacer{flex:1} .tot{font:700 18px var(--display);font-variant-numeric:tabular-nums;white-space:nowrap} .tot span{color:var(--accent)}
  .wrap{max-width:1080px;margin:0 auto;display:grid;gap:18px;padding-block:18px}
  section{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:0 0 12px;min-width:0}
  section h2{margin:0 0 10px;padding:10px 14px;font:700 18px var(--display);letter-spacing:.06em;text-transform:uppercase;display:flex;align-items:center;gap:10px;flex-wrap:wrap;border-bottom:1px solid var(--line)}
  section h2 .s{margin-left:auto;font:400 13px var(--mono);color:var(--ink-2);letter-spacing:0;text-transform:none} section h2 .s b{color:var(--ink)}
  .kv{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:1px;background:var(--line);border:1px solid var(--line);border-radius:4px;margin:0 14px}
  .kv>div{background:var(--panel);padding:8px 10px;min-width:0} .kv dt{font:500 11px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3)}
  .kv dd{margin:0;font:800 26px/1.1 var(--display);font-variant-numeric:tabular-nums}
  .chartbox{overflow-x:auto;margin:12px 14px 0} .chart{width:100%;min-width:560px;height:auto;display:block}
  .chart text{font:11px var(--mono);fill:var(--ink-3)} .chart .grid{stroke:var(--line);stroke-width:1}
  .k-tool{fill:var(--k-tool)} .k-mcp{fill:var(--k-mcp)} .k-skill{fill:var(--k-skill)} .k-agent{fill:var(--k-agent)} .k-workflow{fill:var(--k-workflow)} .k-command{fill:var(--k-command)}
  .legend{display:flex;flex-wrap:wrap;gap:14px;margin:8px 14px 0;font:12px var(--mono);color:var(--ink-2)}
  .legend i{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:6px;vertical-align:-1px}
  .tbl{overflow-x:auto;margin:0 14px}
  table{width:100%;border-collapse:collapse;font:13px var(--mono);min-width:640px}
  thead th{font:500 11px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);text-align:left;padding:6px 8px;border-bottom:1px solid var(--line);white-space:nowrap}
  tbody th{text-align:left;font-weight:500;padding:6px 8px;min-width:200px}
  tbody td{padding:6px 8px;color:var(--ink-2);white-space:nowrap} tbody tr{border-bottom:1px solid var(--line)} tbody tr:last-child{border:0}
  tbody tr:hover{background:var(--panel-2)}
  .num{text-align:right;font-variant-numeric:tabular-nums} td.num{color:var(--ink)}
  .nm{color:var(--ink)} tbody th small{display:block;color:var(--ink-3);font-size:11px;margin-top:2px}
  .flag{font:500 10px/1 var(--mono);letter-spacing:.06em;text-transform:uppercase;padding:3px 5px;border-radius:3px;margin-left:8px;vertical-align:1px}
  .flag.deny{background:var(--bad-soft);color:var(--bad)} .flag.err{background:var(--warn-soft);color:var(--warn)} .flag.gone{border:1px dashed var(--ink-3);color:var(--ink-3)}
  .sp{width:120px;height:22px;display:block} .sp rect{fill:var(--accent)}
  #tool .sp rect{fill:var(--k-tool)} #mcp .sp rect{fill:var(--k-mcp)} #skill .sp rect{fill:var(--k-skill)} #workflow .sp rect{fill:var(--k-workflow)} #command .sp rect{fill:var(--k-command)}
  .list{list-style:none;padding:0;margin:0 14px;display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:2px 18px;font:13px var(--mono)}
  .list li{display:flex;gap:10px;padding:4px 0;border-bottom:1px solid var(--line);min-width:0}
  .list span{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap} .list em{font-style:normal;color:var(--ink-3)} .list b{font-weight:500;color:var(--ink-2)}
  .note{margin:10px 14px 0;font-size:13px;color:var(--ink-2)}
  nav.jump{display:flex;flex-wrap:wrap;gap:8px;margin:0 14px} nav.jump a{font:500 12px var(--mono);color:var(--accent-ink);text-decoration:none;border:1px solid var(--line);border-radius:3px;padding:4px 8px} nav.jump a:hover{border-color:var(--accent)}
  /* the hover layer: every term explains itself; click pins it, Escape closes */
  .t{position:relative;font:inherit;color:inherit;letter-spacing:inherit;text-transform:inherit;background:none;border:0;padding:0;border-bottom:1px dotted var(--accent);cursor:help}
  .tip{display:none;position:absolute;left:0;top:calc(100% + 6px);z-index:20;width:min(300px,80vw);padding:8px 10px;background:var(--panel-2);border:1px solid var(--accent);border-radius:4px;font:400 13px/1.45 var(--body);color:var(--ink);text-transform:none;letter-spacing:0;text-align:left;white-space:normal;box-shadow:0 8px 24px rgba(0,0,0,.5)}
  .t:hover .tip,.t:focus-visible .tip,.t.pin .tip{display:block}
  details.about{font-size:13px;color:var(--ink-2)} details.about summary{cursor:pointer;font:500 11px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);list-style:none;padding:4px 7px;border:1px solid var(--line);border-radius:3px}
  details.about[open] p{position:absolute;right:16px;top:44px;width:min(420px,calc(100vw - 32px));background:var(--panel-2);border:1px solid var(--line);border-radius:4px;padding:10px 12px;margin:0}
  @media (max-width:720px){.kv{grid-template-columns:repeat(3,minmax(0,1fr))}}
</style>
<header class="strip">
  <h1>The <b>Armory</b></h1><span class="chip">BOLO 154</span>
  <span class="spacer"></span>
  <span class="tot"><span>{{TOTAL}}</span> calls</span>
  <span class="chip">{{FROM}} → {{TO}} · {{NDAYS}} days</span>
  <span class="chip">as of {{WHEN}}</span>
  <details class="about"><summary>About</summary><p>Every tool, skill, agent, MCP tool and workflow the Command has called, counted from the session transcripts on disk ({{FILES}} files, main line and agents). Only names, counts and dates are kept. The launch can rebuild this page at zero tokens with <code>python _tools/armory/armory.py</code>.</p></details>
</header>
<main class="wrap">
<section>
  <h2>Calls per day<span class="s">stacked by kind · from {{CHARTFROM}} · {{T_WINDOW}} {{EARLY}}</span></h2>
  <dl class="kv">{{KV}}</dl>
  <div class="chartbox">{{CHART}}</div>
  <div class="legend"><span><i style="background:var(--k-agent)"></i>agents</span><span><i style="background:var(--k-skill)"></i>skills</span><span><i style="background:var(--k-mcp)"></i>MCP</span><span><i style="background:var(--k-tool)"></i>built-in tools</span><span><i style="background:var(--k-workflow)"></i>workflows</span><span><i style="background:var(--k-command)"></i>commands typed</span></div>
  <p class="note">Flags on a row: {{T_DENIED}} counts refusals by a rule, hook or the guard; errors count calls that came back failed. Born is the day git first saw the skill or agent file.</p>
</section>
<nav class="jump" aria-label="sections"><a href="#agent">Agents</a><a href="#skill">Skills</a><a href="#mcp">MCP tools</a><a href="#tool">Built-in tools</a><a href="#workflow">Workflows</a><a href="#command">Commands</a><a href="#idle">Never fired</a></nav>
{{AGENTS}}
{{SKILLS}}
{{MCP}}
{{TOOLS}}
{{WORKFLOWS}}
{{COMMANDS}}
<section id="idle">
  <h2>{{T_IDLE}}<span class="s"><b>{{NIDLE}}</b> on disk · born date from git</span></h2>
  <ul class="list">{{IDLE}}</ul>
</section>
</main>
<script>
  document.addEventListener("click", (ev) => {
    const t = ev.target.closest(".t");
    document.querySelectorAll(".t.pin").forEach((x) => { if (x !== t) x.classList.remove("pin"); });
    if (t) t.classList.toggle("pin");
  });
  document.addEventListener("keydown", (ev) => { if (ev.key === "Escape") document.querySelectorAll(".t.pin").forEach((x) => x.classList.remove("pin")); });
</script>
"""


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # cp1252 consoles choke on the arrows
    except AttributeError:
        pass
    calls, err_by_id, sessions, typed, first_ts, last_ts, nfiles = collect()
    calls, added = keep(calls, err_by_id)
    sessions = {c["sid"] for c in calls}
    rost = roster()
    rows, idle = summarize(calls, err_by_id, typed, rost)
    days = sorted({c["day"] for c in calls if c["day"]})
    early = []   # a lone early stretch before a month-long gap is listed, not charted, so the chart keeps its scale
    for i in range(len(days) - 1, 0, -1):
        if (datetime.strptime(days[i], "%Y-%m-%d") - datetime.strptime(days[i - 1], "%Y-%m-%d")).days > 30:
            early, days = days[:i], days[i:]
            break
    early_n = sum(1 for c in calls if c["day"] in set(early))
    if days:   # fill gaps so the chart is to scale in time
        d0, d1 = datetime.strptime(days[0], "%Y-%m-%d"), datetime.strptime(days[-1], "%Y-%m-%d")
        days = [datetime.fromordinal(o).strftime("%Y-%m-%d") for o in range(d0.toordinal(), d1.toordinal() + 1)]
    now = datetime.now()
    meta = {"built": f"{now.month}/{now.day} {now.strftime('%I:%M %p').lstrip('0')}", "first": days[0] if days else None,
            "last": days[-1] if days else None, "days": days, "sessions": len(sessions), "files": nfiles,
            "early": f"plus {early_n:,} calls on {', '.join(md(d) for d in early)}, before a month-long gap" if early else ""}
    if early:
        meta["first"] = early[0]
    data = {"meta": meta, "rows": rows, "idle": idle}
    os.makedirs(OUTDIR, exist_ok=True)
    with open(os.path.join(OUTDIR, "armory.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, default=str)
    out = build(data)
    by = defaultdict(int)
    for r in rows:
        by[r["kind"]] += r["n"]
    print(f"ARMORY · {len(calls):,} calls · {meta['sessions']} sessions · {nfiles} files · {md(meta['first'])} → {md(meta['last'])}")
    print("  " + " · ".join(f"{k} {v:,}" for k, v in sorted(by.items(), key=lambda kv: -kv[1])) + f" · never fired {len(idle)}")
    print(f"  ledger +{added:,} new calls (kept after the transcripts expire)")
    print("  wrote", out)
    if "--json" in sys.argv:
        print(json.dumps({k: v for k, v in by.items()}))


if __name__ == "__main__":
    main()
