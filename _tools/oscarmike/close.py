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

def main():
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
        if t == "user": body.append(f"\n## PAPI · {stamp}\n{tx.strip()}\n")
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
            "turns": {"papi": sum(1 for t in turns if t[0] == "user"), "claude": sum(1 for t in turns if t[0] == "assistant")},
            "commits_this_session": log.splitlines(), "dirty": git("status", "--porcelain").splitlines()}
    write(os.path.join(wd, "meta.json"), json.dumps(meta, ensure_ascii=False, indent=1))

    # the note's target name: today's note, or -2 / -3 if today already has one that closed
    cache = os.path.join(ROOT, "_CACHE")
    existing = sorted(f for f in os.listdir(cache) if f.startswith(date) and f.endswith(".session.md"))
    target = f"{date}.session.md"
    for f in existing:
        if "Oscar Mike." in io.open(os.path.join(cache, f), encoding="utf-8").read()[-200:]:
            n = len(existing) + 1; target = f"{date}-{n}.session.md"
        else:
            target = f  # an open note from this same session: finalize it
    example = sorted(glob.glob(os.path.join(ROOT, "_LOG", "*.session.md")) + glob.glob(os.path.join(cache, "*.session.md")), key=os.path.getmtime)
    example = rel(example[-1]) if example else "(none)"
    brief = f"""You are NOTE, the Ready Rack specialist for the close-out of {date}. Model: haiku.
READ: {rel(os.path.join(wd, 'transcript.md'))} (the session, spoken turns only) · {rel(os.path.join(wd, 'meta.json'))} · {example} (the newest session note, for shape only){' · _CACHE/' + target + ' (the open note to finalize, keep every existing bullet)' if target in existing else ''}.
WRITE: _CACHE/{target} — the session note in the house shape: a `# Session note — {date}: <what the session was>` title, then bullets:
  the transmission(s) (what Papi ordered, quoted where he ruled something) · what was built or delivered (file paths) · what was ruled (RULED / provisional / tabled, with the word) ·
  what was measured (numbers only if spoken or printed) · memory written (if the transcript says so) · **Open at close:** (everything unresolved, one line) ·
  **AAR (one line):** planned = · happened = · sustain = · improve = · and a final line `- Oscar Mike.`
RULES: nothing not in the transcript; no praise; no summary of Claude's reasoning; file paths verbatim; Papi's words in quotes; under 2,500 characters unless the session was long.
Do not read any other file. Do not edit STATE.md or the journal. Reply with the note's path and nothing else.
"""
    write(os.path.join(wd, "brief.NOTE.md"), brief)
    print(f"OSCAR MIKE prep · session {sid[:8]} · {date}")
    print(f"transcript {rel(os.path.join(wd, 'transcript.md'))} ({len(text)//1024} KB, {meta['turns']['papi']} Papi / {meta['turns']['claude']} Claude turns)")
    print(f"commits this session: {len(meta['commits_this_session'])} · dirty: {len(meta['dirty'])}")
    print(f"note target: _CACHE/{target} ({'finalize' if target in existing else 'new'})")
    print(f"brief: {rel(os.path.join(wd, 'brief.NOTE.md'))}")
    print("next: launch NOTE (haiku) with the brief → read the note → rule it → STATE Moved bullet → python _tools/oscarmike/journal.py → OUT block")

if __name__ == "__main__":
    main()
