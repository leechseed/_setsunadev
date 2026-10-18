# -*- coding: utf-8 -*-
"""The sit rep driver (BOLO 155 M7, Chief 10/18 "go"): the procedure lives here, the skill keeps only the triggers,
the doctrine and the reply. Three phases, each ending in NEXT lines the main line follows exactly. Zero tokens.

  python _tools/sitrep/run.py          H0 · prep, then the H1 order: three named agents, briefs verbatim
  python _tools/sitrep/run.py fanin    H2 · RANGE (assemble.py): reruns once, then the main line's two files
  python _tools/sitrep/run.py close    H3 · build, flush, then the publish and the reply
"""
import json, os, re, subprocess, sys
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
URL = "https://claude.ai/code/artifact/aebe5f9c-9f2c-4cb8-abbf-714a0a6ea28a"
SEATS = [("RACK", "drafting-rack-block", "haiku"), ("INDEX", "drafting-index-blocks", "sonnet"), ("WATCH", "drafting-watch-block", "haiku")]
AGENT = {r: a for r, a, _ in SEATS}


def sh(*args):
    r = subprocess.run([sys.executable, "-X", "utf8", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def rel(p):
    return os.path.relpath(p, ROOT).replace("\\", "/")


def today():
    return datetime.now().strftime("%Y-%m-%d")


def wd(date):
    return os.path.join(HERE, "work", date)


BOARD = os.path.join(HERE, "work", ".board")


def board():
    # the board prep wrote (a second board in a day is 2026-10-18-2), else today
    try:
        b = open(BOARD, encoding="utf-8").read().strip()
        if b.startswith(today()) and os.path.isdir(wd(b)):
            return b
    except OSError:
        pass
    return today()


def prep():
    code, out = sh(os.path.join(HERE, "prep.py"))
    print(out.rstrip())
    if code:
        sys.exit(code)
    m = re.search(r"board (\d{4}-\d{2}-\d{2}(?:-\d+)?)", out)
    date = m.group(1) if m else today()
    with open(BOARD, "w", encoding="utf-8") as f:
        f.write(date)
    print("\nNEXT · H1 · launch these three in ONE message, each BY NAME (subagent_type), never general-purpose.")
    print("       The prompt is the brief file's text verbatim, then one line: (Repo root for every relative path: %s)" % ROOT.replace("\\", "/"))
    for role, agent, model in SEATS:
        print(f"       {role:<6} subagent_type={agent:<22} ({model})  brief {rel(os.path.join(wd(date), f'brief.{role}.md'))}")
    print(f"       Wait for all three (each reply ends DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT / BLOCKED), then: python _tools/sitrep/run.py fanin")


def fanin():
    date = board()
    code, out = sh(os.path.join(HERE, "assemble.py"), date)
    print(out.rstrip())
    reruns = re.findall(r"RERUN (\w+)", out)
    blocking = [l for l in out.splitlines() if re.search(r"missing fragment|unknown glossary|BLOCK", l) and "VI missing" not in l]
    if blocking:
        print("\nNEXT · fix the one fragment the finding names (rerun only that seat, the finding pasted under its brief), then run fanin again.")
        return
    if reruns:
        print("\nNEXT · auto-rerun (BOLO 95): launch in ONE message, by name, each with its rerun brief verbatim; once per board; then run fanin again.")
        for role in reruns:
            print(f"       {role:<6} subagent_type={AGENT.get(role, '?'):<22} brief {rel(os.path.join(wd(date), f'rerun.{role}.md'))}")
        return
    prev = os.path.join(wd(date), "prev", "VI.json")
    keys = list(json.load(open(prev, encoding="utf-8")).keys()) if os.path.exists(prev) else ["id", "name", "kind", "plain", "strand", "line", "why"]
    print("\nNEXT · the main line's judgment (off the digest alone; never open STATE, BOLO, SOP, PROJECTS or the notes):")
    print(f"       1. write {rel(os.path.join(wd(date), 'frag', 'VI.json'))} · the leverage line, keys {keys}; plain register, 20 words max a sentence")
    print(f"       2. write {rel(os.path.join(wd(date), 'meta.patch.json'))} · when · trigger · countersign · main_effort · stats (a LIST of \"label: value\" strings, never a dict) · build.calls/rounds")
    print(f"       3. Block III: edit {rel(os.path.join(wd(date), 'frag', 'III.json'))} against PROJECTS.md only if INDEX left it carried")
    print("       then: python _tools/sitrep/run.py close")


def close():
    date = board()
    code, out = sh(os.path.join(HERE, "assemble.py"), date, "--build", "--flush")
    print(out.rstrip())
    if code:
        sys.exit(code)
    m = re.search(r"fragment (.+)", out)
    frag = m.group(1).strip() if m else "(see above)"
    print(f"\nNEXT · publish with the Artifact tool: file_path {frag} · url {URL}")
    print("       (the first publish of a session may be refused as unread: the page is generated, so publish the same file again once)")
    print("NEXT · the reply, in this order (ruled 10/6): Left off (one sentence) · Start next: BOLO N (a five-word why) · the link ·")
    print("       Block 0 in three bullets · the leverage line · one caveat line only if RANGE left advisory findings. No preamble.")


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass
    {"fanin": fanin, "close": close}.get(sys.argv[1] if len(sys.argv) > 1 else "", prep)()
