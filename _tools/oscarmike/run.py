# -*- coding: utf-8 -*-
"""The close-out driver (BOLO 155 M7, Chief 10/18 "go"): the Oscar Mike procedure lives here, the skill keeps the
triggers, the doctrine and the reply. Three phases, each ending in NEXT lines the main line follows exactly. Zero tokens.

  python _tools/oscarmike/run.py [sid]        H-1 stations down + H0 prep, then the H1 order (one named agent)
  python _tools/oscarmike/run.py note <path>  after NOTE drafts: the resume header, then the main line's judgment
  python _tools/oscarmike/run.py out          H3 journal + H4 stage the next launch, then the proofs and the reply
[sid] = this session's id prefix (two sessions run at once; without it the note can describe the other one).
"""
import os, re, subprocess, sys
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DOWN = os.path.join(HERE, "work", "stations_down.txt")


def sh(*args):
    r = subprocess.run([sys.executable, "-X", "utf8", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace").stdout


def start(sid):
    code, out = sh(os.path.join(ROOT, "_tools", "launch", "shutdown.py"))
    print(out.rstrip())
    os.makedirs(os.path.dirname(DOWN), exist_ok=True)
    open(DOWN, "w", encoding="utf-8").write(out)
    code, out = sh(os.path.join(HERE, "close.py"), *([sid] if sid else []))
    print(out.rstrip())
    if code:
        sys.exit(code)
    brief = re.search(r"brief: (\S+)", out)
    target = re.search(r"(_CACHE/\S+\.session\.md|\d{4}-\d{2}-\d{2}(?:-\d)?\.session\.md)", out)
    print("\nNEXT · H1 · launch ONE agent BY NAME: subagent_type=drafting-session-note (haiku), the prompt = the brief verbatim:")
    print(f"       {brief.group(1) if brief else '(brief path above)'}")
    print("       then: python _tools/oscarmike/run.py note _CACHE/<the note it wrote>" + (f"   (target: {target.group(1)})" if target else ""))


def note(path):
    code, out = sh(os.path.join(HERE, "close.py"), "--header", path)
    print(out.rstrip())
    print("\nNEXT · the main line's judgment (~3 KB read):")
    print(f"       1. read {path}; correct only what is wrong (a misquote, a missing ruling, a path); keep the register")
    print("       2. STATE.md: add or create today's `## ✅ Moved <date> (…)` bullet; touch the Live row and any Blocked row the session changed")
    print("       3. if a memory was earned (a correction, a confirmed way of working, a project fact not in the repo), write it now")
    print("       4. Lessons: one bullet per correction Chief made this session, in the note under its own heading")
    print("       then: python _tools/oscarmike/run.py out")


def out():
    for script, label in (("journal.py", "H3 journal"), ("stage_next.py", "H4 stage next")):
        code, o = sh(os.path.join(HERE, script))
        print(f"── {label} (exit {code})\n" + o.rstrip())
    print("\n── proofs (claim only what a command proved this turn)")
    print(git("status", "-s").rstrip() or "tree clean")
    print(git("log", "--oneline", "-3").rstrip())
    down = open(DOWN, encoding="utf-8").read().strip() if os.path.exists(DOWN) else "(no STATIONS DOWN block saved)"
    print("\nNEXT · the reply: the STATIONS DOWN block (below), then the OUT block (SOP §7 rule 9) and nothing after it. Autocommit fires on stop.")
    print(down)


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass
    a = sys.argv[1:]
    if a and a[0] == "note" and len(a) > 1:
        note(a[1])
    elif a and a[0] == "out":
        out()
    else:
        start(a[0] if a else None)
