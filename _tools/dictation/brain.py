"""
brain.py — what JUDY knows how to do.

BOLO 56. This is the tool layer, and it is deliberately the first thing built.

The wire was ruled MCP. An MCP server is a set of tools plus a transport; the tools
are the part that carries the value, and they are the same tools whether the caller
is a language model, the VS Code session, or a plain keyword router. So they get
written once, here, as ordinary functions over the repo.

Today a keyword router picks the tool. That costs nothing and needs no model, and it
already makes JUDY useful — she can read the board, name what is blocked, and check
a BOLO. When a brain arrives it replaces the router, not the tools.

Every answer is written to be SPOKEN: short sentences, no markdown, numbers said the
way a person says them.
"""

import io
import os
import re
import subprocess
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))


def _read(name):
    try:
        return io.open(os.path.join(ROOT, name), encoding="utf-8").read()
    except Exception:
        return ""


def _section(text, start_pat, end_pat=r"^## "):
    lines = text.splitlines()
    a = None
    for i, l in enumerate(lines):
        if re.search(start_pat, l):
            a = i
            break
    if a is None:
        return []
    b = len(lines)
    for i in range(a + 1, len(lines)):
        if re.match(end_pat, lines[i]):
            b = i
            break
    return lines[a:b]


def _plain(s):
    """Strip markdown so nothing is read aloud as punctuation soup."""
    s = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = re.sub(r"[*_`~#]", "", s)
    s = re.sub(r"https?://\S+", "", s)
    s = re.sub(r"[\U0001F300-\U0001FAFF☀-➿]", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip(" -·|")


# ------------------------------------------------------------------ the tools

def t_blocked():
    """
    The Blocked-on-you table. Spoken, not dumped: a person says the count, names the
    oldest one or two, and offers the rest. Reading six full table cells aloud is
    forty seconds of punctuation.
    """
    rows = []
    for l in _section(_read("STATE.md"), r"^## .*Blocked on you"):
        if not l.startswith("|"):
            continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cells) < 2 or not re.match(r"^\*?\*?\d+", cells[0]):
            continue
        num = re.sub(r"\D", "", cells[0])
        d = _plain(cells[1])
        # the decision cell opens with "BOLO n — the short name"; that is the useful half
        m = re.match(r"(BOLO\s+\d+)\s*[—-]\s*([^.:(]+)", d)
        label = f"{m.group(1)}, {m.group(2).strip().lower()}" if m else d[:60]
        rows.append((num, label))
    if not rows:
        return "I can't find the blocked table. Something moved in STATE."
    n = len(rows)
    lead = f"{n} decisions are waiting on you."
    first = f" The oldest is number {rows[0][0]}, {rows[0][1]}."
    second = f" Then number {rows[1][0]}, {rows[1][1]}." if n > 1 else ""
    tail = f" There are {n - 2} more after that." if n > 2 else ""
    return lead + first + second + tail


def t_bolo(n=None):
    """A specific BOLO, or how many are open."""
    txt = _read("BOLO.md")
    if n is None:
        nums = re.findall(r"^\|\s*(\d+)\s*\|", txt, re.M)
        return f"There are {len(nums)} BOLOs on the watchlist. The newest is number {max(int(x) for x in nums)}."
    for l in txt.splitlines():
        m = re.match(rf"^\|\s*{n}\s*\|(.+?)\|([^|]*)\|([^|]*)\|\s*$", l)
        if m:
            title = _plain(m.group(1))
            title = re.split(r"\s+-\s+|\s+—\s+", title)[0][:120]
            status = _plain(m.group(3))[:180]
            return f"BOLO {n}. {title}. Status: {status}"
    return f"I don't see a BOLO {n}."


def t_pmcs():
    """
    The operator's own readiness rows. The label is not reliably bolded end to end
    ("**Dental** — retainer advising"), so split on pipes rather than pattern-match
    the bold — the earlier version silently missed every row that had a dash in it
    and cheerfully reported all clear.
    """
    rows = []
    for l in _section(_read("BOLO.md"), r"^## .*PMCS"):
        if not l.startswith("|"):
            continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        label, status = _plain(cells[0]), cells[1]
        if not label or label.lower() in ("item", "") or set(label) <= set("-: "):
            continue
        rows.append((label, status))
    if not rows:
        return "I can't find the PMCS table."
    red = [r for r in rows if "🔴" in r[1] or "unemployed" in r[1].lower()]
    if not red:
        return f"PMCS has {len(rows)} rows and none of them are red."
    names = [re.split(r"\s+[—-]\s+", n)[0] for n, _ in red]
    return (f"{len(red)} of {len(rows)} PMCS rows are red: " + ", ".join(names) + ".")


def t_effort():
    """The main effort, off the last board."""
    import glob
    import json
    # "2026-09-16.json" sorts AFTER "2026-09-16-5.json" lexicographically, because
    # "." is above "-" — so sort by mtime and take the one actually written last.
    bs = sorted(glob.glob(os.path.join(ROOT, "_tools", "sitrep", "boards", "*.json")),
                key=os.path.getmtime)
    if not bs:
        return "There's no board on disk yet. Say sit rep in the session and I'll have one."
    try:
        d = json.load(io.open(bs[-1], encoding="utf-8"))
        me = d.get("meta", {}).get("main_effort") or ""
        lev = ""
        for b in d.get("blocks", []):
            if b.get("id") == "VI":
                lev = b.get("line") or ""
        out = []
        if me:
            out.append("Main effort: " + _plain(me))
        if lev:
            out.append("The leverage line says: " + _plain(lev))
        # the main effort and the leverage line often say the same thing; saying it
        # twice out loud sounds like a stutter, so collapse them when they agree.
        if len(out) == 2 and _plain(lev).lower().rstrip(".") in _plain(me).lower():
            out = [out[0]]
        return ". ".join(x.rstrip(".") for x in out) + "." if out             else "The last board didn't name a main effort."
    except Exception as e:
        return f"I couldn't read the last board. {e}"


def t_box():
    """Is the machinery up."""
    import socket
    out = []
    for name, port in (("Stash", 9999), ("DARKROOM", 8484), ("the console", 8787)):
        s = socket.socket()
        s.settimeout(0.3)
        up = s.connect_ex(("127.0.0.1", port)) == 0
        s.close()
        out.append(f"{name} is {'up' if up else 'down'}")
    try:
        dirty = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT,
                               capture_output=True, text=True, timeout=8).stdout.strip()
        out.append("the tree is clean" if not dirty
                   else f"{len(dirty.splitlines())} file"
                        f"{'s' if len(dirty.splitlines()) != 1 else ''} uncommitted")
    except Exception:
        pass
    return ". ".join(x[0].upper() + x[1:] for x in out) + "."


def t_time():
    return time.strftime("It's %A, %B %-d, %-I:%M %p.") if os.name != "nt" \
        else time.strftime("It's %A, %B %d, %I:%M %p.").replace(" 0", " ")


def t_help():
    return ("Ask me for the board, what's blocked, the main effort, a BOLO by number, "
            "PMCS, or whether the box is up. I don't have a brain yet, so keep it simple.")


# ------------------------------------------------------------------ the router

ROUTES = [
    (r"\b(blocked|waiting on me|blocking|owe)\b", lambda m: t_blocked()),
    (r"\b(main effort|leverage|what should i|priority)\b", lambda m: t_effort()),
    (r"\bbolo\s+(?:number\s+)?(\d+)", lambda m: t_bolo(int(m.group(1)))),
    (r"\b(bolo|watchlist)\b", lambda m: t_bolo()),
    (r"\b(pmcs|dental|doctor|appointment|health)\b", lambda m: t_pmcs()),
    (r"\b(box|stash|darkroom|tree|running|up\b)", lambda m: t_box()),
    (r"\b(sit rep|the board|where did we|status)\b",
     lambda m: t_effort() + " " + t_blocked()),
    (r"\b(time|what day|date)\b", lambda m: t_time()),
    (r"\b(help|what can you)\b", lambda m: t_help()),
]


def answer(text):
    """Pick a tool. Returns (reply, tool_name) — the tool name is for the log."""
    t = (text or "").strip().lower()
    if not t:
        return None, None
    for pat, fn in ROUTES:
        m = re.search(pat, t)
        if m:
            try:
                return fn(m), pat
            except Exception as e:
                return f"That tool broke. {e}", pat
    return ("I don't have a brain yet, so I only handle a few things. "
            "Ask for the board, what's blocked, or a BOLO by number."), None


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    q = " ".join(sys.argv[1:])
    if q:
        r, _ = answer(q)
        print(r)
    else:
        for probe in ("what's blocked", "main effort", "bolo 24", "pmcs",
                      "is the box up", "what time is it"):
            r, _ = answer(probe)
            print(f"  ? {probe}\n  > {r}\n")
