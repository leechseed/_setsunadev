"""build_picker.py — BOLO 140: the glass where Chief keeps or skips each intake pick (10/12).

Reads every picks.json under _PRIVATE/intake-repos/ (repos and articles), checks the RANGE rules
(parses · every row has the fields · every `yes` names a source), and writes the picker page from the
roster-picker template (_PRIVATE/ecc/roster_picker.tpl.html). One group per source item.
Picks live in the page's db (collection "picks", one doc per row id): {keep: "yes"|"no", replaces: "<seat or none>"}.

    python _tools/intake/build_picker.py [--out _PRIVATE/intake-repos/intake-picker.html]
"""
import argparse
import io
import json
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "_PRIVATE" / "intake-repos"
TPL = ROOT / "_PRIVATE" / "ecc" / "roster_picker.tpl.html"
FIELDS = ("id", "kind", "plain", "rec", "why", "replaces", "source", "risk")
RECS = {"yes", "maybe", "no"}
SEATS = ["none", "new seat", "new skill", "new script", "PS fetcher (haiku)", "MS writer (sonnet)", "CDR main",
         "RANGE script reviewer", "sitrep", "oscar-mike", "dope-sheet", "frago", "collect", "rtb", "launch", "intake",
         "AUDIT station", "the SessionStart digest", "the memory directory", "SOP §7 (format rules)", "the Roster"]

# folder name -> (label, one line)
LABELS = {
    "thedotmack__claude-mem": ("claude-mem", "Persistent context across sessions. Verdict vs our notes, STATE and memory."),
    "hesreallyhim__awesome-claude-code": ("awesome-claude-code", "The catalog: the coolest items and the features we could build."),
    "BehiSecc__awesome-claude-skills": ("awesome-claude-skills", "More skills to consider and turn into agents."),
    "anthropics__skills": ("anthropics/skills", "The builder agent and the bloat cut."),
    "ThibautMelen__agentic-ai-systems": ("agentic-ai-systems", "Agent patterns mapped onto the formation."),
    "hluaguo__learn-faster-kit": ("learn-faster-kit", "Learning agents for the Roster, on the teach-back loop."),
    "Leonxlnx__taste-skill": ("taste-skill", "Taste for glass pages and for prose."),
    "HKUDS__ClawTeam": ("ClawTeam", "What it is and whether to run it here."),
    "ruvnet__ruflo": ("ruflo", "Ideas only for our own animated front page."),
    "Mudlet__Mudlet": ("Mudlet", "Ideas only (GPL): the character-creation MUD wired to LEECHSEED."),
    "LukeRenton__explore-claude-code": ("explore-claude-code", "The clean tree and the staged cleanup plan."),
    "articles/context-engineering": ("Context engineering (Anthropic)", "What we change at session open, in the digest and the briefs."),
    "articles/multi-agent-research": ("Multi-agent research (Anthropic)", "What we change in collect and the research loop."),
    "articles/steering": ("Steering Claude Code (article)", "The intent parser in front of the work."),
    "articles/mcp-addons": ("MCP add-ons", "The plain guide and the servers worth adding."),
    "console": ("THE CONSOLE (ruflo SVG)", "One program on the box, the Caves of Qud look; the shell rec and the mock."),
    "mehdibha__dotUI": ("dotUI", "UI component ideas for a ui-builder seat; React, ideas only."),
    "d3__d3": ("d3", "Visualize the fabula and the systems; the force graph."),
    "google__langextract": ("langextract", "Structure the scanned notes with Ollama at zero cost."),
    "lutzroeder__netron": ("netron", "A model viewer to open on call."),
    "chartdb__chartdb": ("chartdb", "Reference only; the ERD glasses are ours."),
    "rougier__scientific-visualization-book": ("sci-vis book", "Chart rules into the taste guide."),
    "cathrynlavery__diagram-design": ("diagram-design", "Editorial, layered diagrams for a reader who was not there."),
    "gotalab__cc-sdd": ("cc-sdd", "Steering files and a tasks checklist so agents go by SOP."),
    "danielrosehill__Claude-Code-Projects-Index": ("Projects Index", "Administration apart from development; maps onto the ruled tree."),
    "sickn33__agentic-awesome-skills": ("agentic-awesome-skills", "Skill catalog with a stable manifest."),
    "addyosmani__agent-skills": ("agent-skills (addyosmani)", "Development skills catalog."),
    "ComposioHQ__awesome-claude-skills": ("awesome-claude-skills (Composio)", "Skill catalog placed against our processes."),
    "yingpengma__Awesome-Story-Generation": ("Awesome-Story-Generation", "The writing department as seats; gated behind systems first."),
    "tjboudreaux__cc-thinking-skills": ("cc-thinking-skills", "Thinking moves for research briefs."),
    "morluto__rea": ("rea", "Binary reverse engineering; not a design copier."),
    "blader__humanizer": ("humanizer", "Phrase lists to merge into the prose lint."),
    "articles/building-effective-agents": ("Building Effective Agents (Anthropic)", "The formation checked against the patterns."),
    "Piebald-AI__claude-code-system-prompts": ("claude-code-system-prompts", "What the harness tells itself; agents that interface with the system."),
    "costiash__claude-code-docs": ("claude-code-docs", "Not a mirror; our own mirror.py with a diff and Chief's change-review rule."),
    "K-Dense-AI__scientific-agent-skills": ("scientific-agent-skills", "The Science Department: six seats, the plausibility seat first."),
    "conorbronsdon__avoid-ai-writing": ("avoid-ai-writing", "Merged into prose_lint; no prose team."),
    "OneRedOak__claude-code-workflows": ("OneRedOak workflows", "Three pieces into existing seats; the Action rejected."),
    "ClaytonFarr__ralph-playbook": ("the Ralph loop (4 repos)", "Our own bounded loop script; install none."),
    "diet103__claude-code-infrastructure-showcase": ("infrastructure-showcase", "Ours wins on hooks and skills; theirs on layout and onboarding."),
    "obra__superpowers": ("superpowers", "Four patterns to adopt, four to skip."),
    "NeoLabHQ__context-engineering-kit": ("context-engineering-kit", "GPL: two ideas, one warning about judge loops."),
    "coreyhaines31__marketingskills": ("marketingskills", "Three references into the marketing agent; no new seat."),
    "VoltAgent__awesome-agent-skills": ("awesome-agent-skills (VoltAgent)", "Thin under the rate limit; mostly repeats."),
    "titanwings__distilly": ("distilly", "Skip the tool, take the profile block."),
    "citrolabs__ego-lite": ("ego-lite + brag", "ego-lite macOS only; brag once for a pitch; the translation path is organic."),
    "latent-spaces__brag": ("brag", "Launch videos; Node; one public pitch."),
    "0xNyk__council-of-high-intelligence": ("the leadership seats (4 repos)", "A five-seat advisory bench; the CDR stays chief of staff; CTO waits."),
    "pytorch__rl": ("pytorch/rl", "What RL is; a 50-line bandit for the fresh hour; TorchRL waits."),
    "apache__superset": ("superset", "Skip the server; one query to one chart instead."),
}


def load_picks(only=None):
    rows, findings, groups = [], [], {}
    files = sorted(SRC.rglob("picks.json"))
    if only:
        files = [f for f in files if f.parent.relative_to(SRC).as_posix() in only]
    for f in files:
        key = f.parent.relative_to(SRC).as_posix()
        try:
            data = json.loads(f.read_text(encoding="utf-8-sig"))
        except Exception as e:  # noqa: BLE001
            findings.append(f"{key}: picks.json does not parse ({e})")
            continue
        if isinstance(data, dict):
            data = data.get("picks") or data.get("rows") or list(data.values())
        if not isinstance(data, list):
            findings.append(f"{key}: picks.json is not a list")
            continue
        label, line = LABELS.get(key, (key, ""))
        groups[key] = (label, line)
        for i, r in enumerate(data):
            if not isinstance(r, dict) or not str(r.get("plain", r.get("id", ""))).strip():
                findings.append(f"{key} row {i}: not a pick row, skipped")
                continue
            rec_raw = str(r.get("rec", "")).lower().strip()
            r["rec"] = {"keep": "yes", "adopt": "yes", "skip": "no", "reject": "no", "later": "maybe", "hold": "maybe", "trial": "maybe"}.get(rec_raw, rec_raw)
            missing = [k for k in FIELDS if k not in r]
            if missing:
                findings.append(f"{key} row {i}: missing {', '.join(missing)}")
            rec = str(r.get("rec", "")).lower().strip()
            if rec not in RECS:
                findings.append(f"{key} row {i}: rec '{rec}' not yes/maybe/no")
                rec = "maybe"
            if rec == "yes" and not str(r.get("source", "")).strip():
                findings.append(f"{key} row {i}: yes without a source")
            rid = str(r.get("id") or f"{key}-{i:02d}")
            src = str(r.get("source", "") or "")
            url = src if src.startswith("http") else f"https://github.com/{key.replace('__', '/')}"
            rows.append({
                "id": rid, "group": key, "rec": rec,
                "plain": str(r.get("plain", "")),
                "replaces": str(r.get("replaces", "none") or "none"),
                "model": str(r.get("kind", "idea")),
                "desc": f"WHY: {r.get('why', '')}  ·  SOURCE: {src or 'none'}  ·  RISK: {r.get('risk', 'none')}",
                "url": url,
            })
    return rows, groups, findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(SRC / "intake-picker.html"))
    ap.add_argument("--only", default="", help="comma list of folder keys (a batch)")
    ap.add_argument("--title", default="Intake Picks")
    a = ap.parse_args()
    only = [k.strip() for k in a.only.split(",") if k.strip()] or None
    rows, groups, findings = load_picks(only)
    recrank = {"yes": 0, "maybe": 1, "no": 2}
    rows.sort(key=lambda r: (list(groups).index(r["group"]), recrank[r["rec"]], r["id"]))
    seats = SEATS + sorted({r["replaces"] for r in rows if r["replaces"] not in SEATS})

    page = TPL.read_text(encoding="utf-8")
    page = page.replace("<title>Agent Roster Picks</title>", f"<title>{a.title}</title>")
    page = page.replace("<h1><b>Agent</b> Roster Picks</h1><span class=\"chip\">BOLO 139</span>",
                        "<h1><b>Intake</b> Picks</h1><span class=\"chip\">BOLO 140</span>")
    page = page.replace("Every <span class=\"t\" tabindex=\"0\">agent<span class=\"tip\">A helper with one job and its own instructions. Claude hands it a task, it works in its own space, then reports back. Like calling in a specialist.</span></span> in ECC, in plain words,",
                        f"Every pick from the {len(groups)} intake items, in plain words,")
    page = page.replace("I read your picks to build the roster file.", "I read your picks and adopt each kept one the BOLO 139 way: read in full, strip hooks and installers, add the Command rules.")
    filters = ['<button type="button" data-f="all" aria-pressed="true">All %d</button>' % len(rows)]
    for k, (label, _) in groups.items():
        n = sum(r["group"] == k for r in rows)
        filters.append(f'<button type="button" data-f="{k}" aria-pressed="false">{label} {n}</button>')
    start = page.index('<div class="filters"')
    end = page.index("</div>", start) + len("</div>")
    page = page[:start] + '<div class="filters" role="group" aria-label="Show">' + "".join(filters) + "</div>" + page[end:]
    gstart = page.index("const GROUPS = {")
    gend = page.index("};", gstart) + 2
    page = page[:gstart] + "const GROUPS = " + json.dumps({k: list(v) for k, v in groups.items()}, ensure_ascii=False) + ";" + page[gend:]
    page = page.replace("/*DATA*/null", json.dumps(rows, ensure_ascii=False)).replace("/*SEATS*/null", json.dumps(seats))
    Path(a.out).write_text(page, encoding="utf-8")

    yes = sum(r["rec"] == "yes" for r in rows)
    maybe = sum(r["rec"] == "maybe" for r in rows)
    print(f"{len(rows)} rows · {len(groups)} groups · {yes} yes · {maybe} maybe · {len(rows)-yes-maybe} no → {a.out}")
    for g, (label, _) in groups.items():
        gr = [r for r in rows if r["group"] == g]
        print(f"  {label:36s} {len(gr):3d} rows · yes {sum(r['rec']=='yes' for r in gr)}")
    if findings:
        print("FINDINGS (%d):" % len(findings))
        for f in findings:
            print("  -", f)
        sys.exit(1)
    print("RANGE: clean")


if __name__ == "__main__":
    main()
