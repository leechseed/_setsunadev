# -*- coding: utf-8 -*-
"""OSCAR MIKE prep — the zero-token half of the close-out (BOLO 51 phase 2, the formation).

Usage:  python _tools/oscarmike/close.py [session-id-prefix]
        (default: the newest main transcript in the project's Claude folder)

Writes  _tools/oscarmike/work/<date>/transcript.md   the session's spoken turns: every user message in full,
                                                     every assistant reply trimmed, tool traffic dropped (cap ~80 KB, tail kept)
        _tools/oscarmike/work/<date>/brief.NOTE.md    the haiku brief: draft the Ready Rack note from the transcript
        _tools/oscarmike/work/<date>/meta.json        session id · turn counts · git commits this session · files touched
Prints  a 10-line digest. The main line then: launches NOTE (haiku) → reads the drafted note (~3 KB) → rules it →
        writes STATE's Moved bullet → python journal.py → the OUT block.
"""
import io, json, os, re, sys, glob, datetime, subprocess
import sys

# stdout on this box is cp1252; the board writes arrows and box glyphs
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CLAUDE = os.path.join(os.path.expanduser("~"), ".claude", "projects", "c--Users-U01-LEECHSEED-Desktop--setsunadev")
CAP = 80_000

def rel(p): return os.path.relpath(p, ROOT).replace("\\", "/")

def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with io.open(p, "w", encoding="utf-8", newline="\n") as f: f.write(s)

def git(*a):
    try:
        return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace").stdout.strip()
    except Exception: return ""

def texts(content):
    if isinstance(content, str): return [content]
    out = []
    for c in content or []:
        if isinstance(c, dict) and c.get("type") == "text": out.append(c.get("text", ""))
    return out

def _sec(text, label):
    m = re.search(r"\*\*" + label + r"[^*]*\*\*:?\s*(.+)", text)
    return m.group(1).strip() if m else ""

def _heads(sec, n=8, w=40):
    parts = [re.sub(r"[`*]", "", x).strip() for x in re.split(r"\s+·\s+|;\s+", sec) if x.strip()]
    return ", ".join(x[:w].rstrip(" ,.") for x in parts[:n])

NL = chr(10)
FENCE = "`" * 3

def _wrap(lines):
    return FENCE + "resume" + NL + NL.join(lines) + NL + FENCE

def build_header(text):
    """Resume header (ctx-03): fenced block, <=600 bytes, built from the drafted note's own sections."""
    aar = _sec(text, "AAR")
    opn, rul = _sec(text, "Open at (?:this point|close)"), _sec(text, "Ruled")
    hap = re.search(r"happened\s*=\s*([^·]+)", aar)
    if not (hap and opn):
        return _wrap(["left-off: see note"])
    first = re.split(r"\s+·\s+", opn)[0]
    lines = ["left-off: " + hap.group(1).strip().rstrip(".")[:160] + ".",
             "next: " + re.sub(r"[`*]", "", first).strip().rstrip(".")[:120] + ".",
             "open: " + _heads(opn, 6, 36),
             "rulings: " + _heads(rul, 6, 36)]
    while len(_wrap(lines).encode("utf-8")) > 600 and len(lines[3]) > 12:
        lines[3] = lines[3][:-12].rstrip(" ,")
    return _wrap(lines)

PRIVATE_RE = re.compile(r"\[private\].*?\[/private\]|<!--\s*private\s*-->.*?<!--\s*/private\s*-->", re.S | re.I)

def strip_private(path):
    """claude-mem-05: cut private spans out of the note, keep them in _PRIVATE/notes-private/<id>.md."""
    t = io.open(path, encoding="utf-8").read()
    spans = [m.group(0) for m in PRIVATE_RE.finditer(t)]
    if not spans: return
    nid = os.path.basename(path)[:-len(".session.md")] if path.endswith(".session.md") else os.path.splitext(os.path.basename(path))[0]
    write(os.path.join(ROOT, "_PRIVATE", "notes-private", nid + ".md"), (NL * 2).join(spans) + NL)
    write(path, PRIVATE_RE.sub("", t))
    print(f"private spans stripped: {len(spans)} -> _PRIVATE/notes-private/{nid}.md")

def add_header(path):
    """Insert (or replace) the resume header under the H1 of a drafted note. Run after the PS draft."""
    strip_private(path)
    t = io.open(path, encoding="utf-8").read()
    t = re.sub(r"\A(# [^\n]*\n)\n?" + FENCE + r"resume\n.*?\n" + FENCE + r"\n", lambda m: m.group(1), t, flags=re.S)
    h, _, rest = t.partition(NL)
    write(path, h + NL + NL + build_header(t) + NL + rest)
    print("resume header written:", rel(path))

def main():
    if "--header" in sys.argv:
        add_header(os.path.abspath(sys.argv[sys.argv.index("--header") + 1])); return
    files = sorted(glob.glob(os.path.join(CLAUDE, "*.jsonl")), key=os.path.getmtime)
    if len(sys.argv) > 1:
        files = [f for f in files if os.path.basename(f).startswith(sys.argv[1])]
    if not files:
        print("no transcript found"); sys.exit(1)
    fp = files[-1]
    sid = os.path.basename(fp)[:-6]
    turns, first_ts, last_ts = [], None, None
    with io.open(fp, encoding="utf-8", errors="replace") as f:
        for line in f:
            try: o = json.loads(line)
            except Exception: continue
            t = o.get("type")
            if t not in ("user", "assistant"): continue
            ts = o.get("timestamp"); first_ts = first_ts or ts; last_ts = ts or last_ts
            msg = o.get("message", {})
            tx = "\n".join(x for x in texts(msg.get("content")) if x.strip())
            if not tx.strip(): continue
            if t == "user" and (tx.startswith("<") or "tool_result" in tx[:40]): continue
            turns.append((t, ts, tx))
    date = datetime.date.today().isoformat()
    wd = os.path.join(HERE, "work", date)
    body = []
    for t, ts, tx in turns:
        stamp = (ts or "")[11:16]
        if t == "user": body.append(f"\n## CHIEF · {stamp}\n{tx.strip()}\n")
        else:
            tx = tx.strip()
            body.append(f"\n## CLAUDE · {stamp}\n{tx[:1500]}{' […]' if len(tx) > 1500 else ''}\n")
    text = "".join(body)
    if len(text) > CAP:
        text = "[… head trimmed to the cap; the tail is what matters at close …]\n" + text[-CAP:]
    write(os.path.join(wd, "transcript.md"), f"# TRANSCRIPT · session {sid} · {date}\n" + text)

    since = (first_ts or "")[:19].replace("T", " ")
    log = git("log", f"--since={since}", "--format=%h %ad %s", "--date=format:%H:%M") if since else ""
    touched = git("diff", "--name-only", f"HEAD@{{{since}}}") if since else ""
    meta = {"session": sid, "date": date, "first": first_ts, "last": last_ts,
            "turns": {"chief": sum(1 for t in turns if t[0] == "user"), "claude": sum(1 for t in turns if t[0] == "assistant")},
            "commits_this_session": log.splitlines(), "dirty": git("status", "--porcelain").splitlines()}
    write(os.path.join(wd, "meta.json"), json.dumps(meta, ensure_ascii=False, indent=1))

    # the note's target name: an open note anywhere in the rack (a session that spans midnight keeps its start-date note),
    # else today's note, or -2 / -3 if today already closed one. `--note <file>` overrides.
    cache = os.path.join(ROOT, "_CACHE")
    all_notes = sorted(f for f in os.listdir(cache) if f.endswith(".session.md"))
    existing = [f for f in all_notes if f.startswith(date)]
    open_notes = [f for f in all_notes if "Oscar Mike." not in io.open(os.path.join(cache, f), encoding="utf-8").read()[-200:]]
    if "--note" in sys.argv:
        target = os.path.basename(sys.argv[sys.argv.index("--note") + 1]); existing = [target]
    elif open_notes:
        target = open_notes[-1]; existing = [target]  # finalize the newest open note
    else:
        target = f"{date}.session.md" if not existing else f"{date}-{len(existing) + 1}.session.md"
    example = sorted(glob.glob(os.path.join(ROOT, "_LOG", "*.session.md")) + glob.glob(os.path.join(cache, "*.session.md")), key=os.path.getmtime)
    example = rel(example[-1]) if example else "(none)"
    brief = f"""JOB: drafting-session-note
You are NOTE, the Ready Rack specialist for the close-out of {date}. Model: haiku.
READ: {rel(os.path.join(wd, 'transcript.md'))} (the session, spoken turns only) · {rel(os.path.join(wd, 'meta.json'))} · {example} (the newest session note, for shape only){' · _CACHE/' + target + ' (the open note to finalize, keep every existing bullet)' if target in existing else ''}.
WRITE: _CACHE/{target} — the session note in the Command's shape: a `# Session note — {date}: <what the session was>` title, then bullets:
  the transmission(s) (what Chief ordered, quoted where he ruled something) · what was built or delivered (file paths) · what was ruled (RULED / provisional / tabled, with the word) ·
  what was measured (numbers only if spoken or printed) · memory written (if the transcript says so) · **Open at close:** (everything unresolved, one line) ·
  **AAR (one line):** planned = · happened = · sustain = · improve = · and a final line `- Oscar Mike.`
RULES: nothing not in the transcript; no praise; no summary of Claude's reasoning; file paths verbatim; Chief's words in quotes; under 2,500 characters unless the session was long.
Text between [private] and [/private] (or <!-- private --> and <!-- /private -->) is cut from the note by close.py --header and kept in _PRIVATE/notes-private/.
PRIVATE DETAIL STAYS PRIVATE (ruled 10/4): _CACHE is in the public repo. Keep sexual, health, drug and kink detail generic ("ORANGE items, detail in _PRIVATE/"): never quote Chief's sexual words, never name kinks, toys, substances, body parts or adult boards. (10/8: the first draft leaked this detail.)
After the note is drafted the main line runs `python _tools/oscarmike/close.py --header _CACHE/{target}` (it adds the resume header under the H1; do not write one yourself).
Do not read any other file. Do not edit STATE.md or the journal. Reply with the note's path and nothing else.
"""
    write(os.path.join(wd, "brief.NOTE.md"), brief.rstrip("\n") + "\nSTATUS. End your reply with one status line: DONE · DONE_WITH_CONCERNS: <what> · NEEDS_CONTEXT: <what file or fact> · BLOCKED: <why> (superpowers contract, BOLO 155 M1).\n")
    print(f"OSCAR MIKE prep · session {sid[:8]} · {date}")
    print(f"transcript {rel(os.path.join(wd, 'transcript.md'))} ({len(text)//1024} KB, {meta['turns']['chief']} Chief / {meta['turns']['claude']} Claude turns)")
    print(f"commits this session: {len(meta['commits_this_session'])} · dirty: {len(meta['dirty'])}")
    print(f"note target: _CACHE/{target} ({'finalize' if target in existing else 'new'})")
    print(f"brief: {rel(os.path.join(wd, 'brief.NOTE.md'))}")
    print("next: launch NOTE (haiku) with the brief → close.py --header <note> → read the note → rule it → STATE Moved bullet → python _tools/oscarmike/journal.py → OUT block")

if __name__ == "__main__":
    main()
