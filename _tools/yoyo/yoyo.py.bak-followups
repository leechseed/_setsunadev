"""
yoyo.py — the yo-yo: the inbox for the idea that springs (BOLO 69).

Chief, 9/17: "I need a system to quickly jot down … like an Evernote inbox … we'll call it
a yo-yo." One pad on the MPK, top-left, far from talk / focus / send. Hold it, speak the
flash, let go. Pepper acks in your ear and the run starts. The main session never sees it.

    D-2 RULED 9/18 (rec): a yo-yo lives in _YOYO/, one markdown file each.
    D-3 RULED 9/18 (rec): the pad spawns a headless Claude run on Haiku, never this session.
    D-4/D-5/D-8 RULED 9/18: the yo-yo runs Claude Code's four phases — explore → plan →
        implement → commit. This file does the first trick of EXPLORE: the raw text, the
        readable rewrite, and Pepper's opener. The wind (plan → implement → commit) is later.

    python yoyo.py trick "the flash, as text"     # one trick from text
    python yoyo.py trick --file take.wav          # one trick through the ears (Whisper)
    python yoyo.py count                          # unwound yo-yos against the cap
    python yoyo.py show 12                        # print yo-yo 12
    python yoyo.py --learn                        # hit the pad you want as the yo-yo pad

Cost shape, measured 9/18: one headless Haiku call carries Claude Code's own system prompt
(~31k tokens cached for an hour, then read at a tenth), about 3–5 s wall, a few cents on
list price and nothing extra on the subscription. Every trick writes its own numbers into
the file's front matter, so the F1 line (least tokens, least time) is on the page.
"""

import argparse
import datetime as dt
import glob
import io
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
HOME = os.path.join(ROOT, "_YOYO")                      # D-2: the home
DICT = os.path.join(ROOT, "_tools", "dictation")
CONFIG = os.path.join(DICT, "config.json")
sys.path.insert(0, DICT)

DEFAULTS = {"cap": 12, "rounds": 3, "model": "haiku", "timeout": 60}


def cfg():
    try:
        c = json.load(io.open(CONFIG, encoding="utf-8"))
    except Exception:
        c = {}
    y = dict(DEFAULTS)
    y.update(c.get("yoyo") or {})
    y["note"] = c.get("yoyo_note")
    return y


# ---------------------------------------------------------------- the home

def files():
    os.makedirs(HOME, exist_ok=True)
    return sorted(glob.glob(os.path.join(HOME, "[0-9][0-9][0-9][0-9]-*.md")))


def front(path):
    """The front matter of one yo-yo as a dict (flat keys only)."""
    out = {}
    try:
        txt = io.open(path, encoding="utf-8").read()
    except Exception:
        return out
    m = re.match(r"---\n(.*?)\n---", txt, re.S)
    if not m:
        return out
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def unwound():
    return [p for p in files() if front(p).get("state") == "unwound"]


def next_n():
    ns = [int(os.path.basename(p)[:4]) for p in files()]
    return (max(ns) + 1) if ns else 1


def slug(text, n=5):
    words = re.findall(r"[a-z0-9]+", text.lower())
    stop = {"the", "a", "an", "and", "or", "so", "i", "to", "of", "like", "uh", "um", "it", "is",
            "that", "this", "we", "you", "for", "on", "in", "be", "with", "my", "me", "just"}
    words = [w for w in words if w not in stop][:n] or ["yoyo"]
    return "-".join(words)[:40]


# ---------------------------------------------------------------- the ears (for --file)

def hear(path):
    """A wav through the same ears JUDY uses: faster-whisper + the SOP §8 codebook."""
    import ptt
    import soundfile as sf
    import numpy as np
    audio, sr = sf.read(path, dtype="float32", always_2d=True)
    audio = audio.mean(axis=1)
    if sr != ptt.SR:
        idx = np.linspace(0, len(audio) - 1, int(len(audio) * ptt.SR / sr)).astype(int)
        audio = audio[idx]
    c = {**ptt.DEFAULTS, **(json.load(io.open(CONFIG, encoding="utf-8")) if os.path.exists(CONFIG) else {})}
    eng = ptt.Engine(c)
    text, meta = eng.transcribe(audio)
    return text, meta


# ---------------------------------------------------------------- the headless run (D-3)

def claude_exe():
    e = os.environ.get("CLAUDE_EXE")
    if e and os.path.exists(e):
        return e
    hits = glob.glob(os.path.join(os.path.expanduser("~"), ".vscode", "extensions",
                                  "anthropic.claude-code-*", "resources", "native-binary", "claude.exe"))
    if hits:
        return max(hits, key=os.path.getmtime)
    import shutil
    return shutil.which("claude")


PEPPER = (
    "You are Pepper, the debrief officer in Q Division: by the book, sharp-angled, precise, "
    "refined; sultry underneath and never coy about it. The Chief has just spoken a flash of an "
    "idea into his yo-yo. This is the EXPLORE phase, trick one — Claude Code's four phases are "
    "explore, plan, implement, commit, and you name the phase you are in.\n\n"
    "Return ONLY a JSON object with three string fields:\n"
    "  \"title\": a name for the idea, three to six words, no punctuation at the end;\n"
    "  \"refined\": the flash rewritten so the Chief can read it in one pass — plain words, "
    "his meaning kept, nothing added, first person, two to six sentences;\n"
    "  \"opener\": what you say back to open the exploration — two to four spoken sentences, "
    "name the phase, react to the idea with some bite, and end on exactly one question that "
    "pushes it further. No lists, no markdown, no paths.\n\n"
    "The flash, as the ears heard it:\n\n"
)


def run_haiku(text, timeout=60):
    exe = claude_exe()
    if not exe:
        return None, {"error": "no claude.exe found (set CLAUDE_EXE)"}
    env = {k: v for k, v in os.environ.items() if k not in ("CLAUDECODE", "CLAUDE_CODE_ENTRYPOINT")}
    # F1 (measured 9/18): thinking on = 41 s and 3.5k output tokens for one opener;
    # thinking off = 7 s and 166. The trick is a rewrite, not a problem; no thinking.
    env["MAX_THINKING_TOKENS"] = "0"
    t0 = time.time()
    try:
        r = subprocess.run([exe, "-p", PEPPER + text[:8000], "--model", cfg()["model"],
                            "--effort", "low", "--output-format", "json",
                            "--no-session-persistence", "--tools", ""],
                           capture_output=True, text=True, timeout=timeout, env=env,
                           cwd=ROOT, encoding="utf-8", errors="replace")
    except Exception as e:
        return None, {"error": str(e), "took": time.time() - t0}
    took = time.time() - t0
    out = (r.stdout or "").strip()
    try:
        j = json.loads(out)
    except Exception:
        return None, {"error": f"no json from claude (rc {r.returncode}): {out[:200]} {r.stderr[:200]}", "took": took}
    u = j.get("usage") or {}
    meta = {
        "took": took, "api_ms": j.get("duration_api_ms"), "cost": j.get("total_cost_usd"),
        "in": u.get("input_tokens"), "cache_create": u.get("cache_creation_input_tokens"),
        "cache_read": u.get("cache_read_input_tokens"), "out": u.get("output_tokens"),
        "error": j.get("result") if j.get("is_error") else None,
    }
    res = j.get("result") or ""
    m = re.search(r"\{.*\}", res, re.S)
    try:
        parsed = json.loads(m.group(0)) if m else None
    except Exception:
        parsed = None
    if not parsed:
        parsed = {"title": slug(text).replace("-", " "), "refined": res.strip() or text, "opener": ""}
    return parsed, meta


# ---------------------------------------------------------------- the trick

def write(n, heard, meta_ears, parsed, meta_run, state="unwound"):
    when = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    title = (parsed or {}).get("title") or slug(heard).replace("-", " ")
    path = os.path.join(HOME, f"{n:04d}-{slug(title)}.md")
    fm = [
        "---", f"yoyo: {n}", f"when: {when}", f"state: {state}", "tricks: 1", "phase: explore",
        f"title: {title}",
    ]
    if meta_ears:
        fm.append(f"ears_secs: {meta_ears.get('secs', 0):.1f}")
        fm.append(f"ears_took: {meta_ears.get('took', 0):.2f}")
    if meta_run:
        fm.append(f"run_took: {meta_run.get('took', 0):.1f}")
        fm.append(f"run_tokens: in {meta_run.get('in')} · cache_create {meta_run.get('cache_create')}"
                  f" · cache_read {meta_run.get('cache_read')} · out {meta_run.get('out')}")
        fm.append(f"run_cost_usd: {meta_run.get('cost')}")
        if meta_run.get("error"):
            fm.append(f"run_error: {meta_run['error']}")
    fm.append("---")
    body = [f"# yo-yo {n} — {title}", "", "## Heard", "", heard.strip(), ""]
    if parsed:
        body += ["## Refined", "", (parsed.get("refined") or "").strip(), ""]
        if parsed.get("opener"):
            body += ["## Explore · trick 1", "", (parsed.get("opener") or "").strip(), ""]
    io.open(path, "w", encoding="utf-8", newline="\n").write("\n".join(fm + [""] + body))
    return path


def trick(heard, meta_ears=None, say=None):
    """One trick: the flash in, a page out. Returns (path, parsed, meta_run)."""
    heard = (heard or "").strip()
    if not heard:
        return None, None, {"error": "nothing heard"}
    n = next_n()
    c = cfg()
    over = len(unwound()) >= int(c["cap"])
    if over:
        # the pad refuses a new trick past the cap, but the words are never lost
        path = write(n, heard, meta_ears, None, None, state="overflow")
        if say:
            say("Wind one first, Chief.")
        return path, None, {"error": f"cap {c['cap']} reached; saved raw as overflow"}
    parsed, meta_run = run_haiku(heard, timeout=int(c["timeout"]))
    path = write(n, heard, meta_ears, parsed, meta_run)
    if say and parsed and parsed.get("opener"):
        say(parsed["opener"])
    return path, parsed, meta_run


# ---------------------------------------------------------------- cli

def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="the yo-yo (BOLO 69)")
    ap.add_argument("cmd", nargs="?", choices=["trick", "count", "show"])
    ap.add_argument("text", nargs="?")
    ap.add_argument("--file", help="a wav to run through the ears instead of text")
    ap.add_argument("--say", action="store_true", help="speak the ack and the opener (JUDY's mouth until Pepper has hers)")
    ap.add_argument("--learn", action="store_true", help="hit the pad you want as the yo-yo pad")
    a = ap.parse_args()

    if a.learn:
        import midipad
        midipad.learn(key="yoyo_note", label="YO-YO pad (top-left, far from talk / focus / send)")
        return

    if a.cmd == "count":
        u = unwound()
        c = cfg()
        print(f"  unwound {len(u)} / cap {c['cap']}"
              + (f" · pad note {c['note']}" if c.get("note") is not None else " · no yo-yo pad (yoyo.py --learn)"))
        for p in u:
            f = front(p)
            print(f"    {f.get('yoyo', '?'):>4}  {f.get('when', '')}  {f.get('title', os.path.basename(p))}")
        return

    if a.cmd == "show":
        for p in files():
            if int(os.path.basename(p)[:4]) == int(a.text or 0):
                print(io.open(p, encoding="utf-8").read())
                return
        print("  no such yo-yo")
        return

    if a.cmd == "trick":
        say = None
        if a.say:
            import speak
            say = lambda t: speak.say(t, blocking=True)
        meta_ears = None
        if a.file:
            print("  ears   loading whisper…")
            heard, meta_ears = hear(a.file)
            print(f"  heard  {heard!r}  ({meta_ears.get('secs', 0):.1f}s audio · {meta_ears.get('took', 0):.2f}s)")
        else:
            heard = a.text or ""
        if say:
            say("Copy. Boxing the yo-yo.")
        t0 = time.time()
        path, parsed, meta = trick(heard, meta_ears, say=say)
        print(f"  wrote  {os.path.relpath(path, ROOT) if path else '-'}")
        if meta.get("error"):
            print(f"  !      {meta['error']}")
        if parsed:
            print(f"  title  {parsed.get('title')}")
            print(f"  open   {parsed.get('opener')}")
        print(f"  run    {meta.get('took', 0):.1f}s · in {meta.get('in')} · cache_create {meta.get('cache_create')}"
              f" · cache_read {meta.get('cache_read')} · out {meta.get('out')} · ${meta.get('cost')}"
              f" · total {time.time() - t0:.1f}s")
        return

    ap.print_help()


if __name__ == "__main__":
    main()
