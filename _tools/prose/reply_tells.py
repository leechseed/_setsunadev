# -*- coding: utf-8 -*-
"""reply_tells.py - BOLO 157 (10/18, Chief: "part of the routine whenever Judy replies … I want to be able to know if it works").

Hook mode (UserPromptSubmit): reads the hook JSON on stdin, finds Claude's last reply in the session transcript, runs
prose_lint on it, appends one row to tells_ledger.jsonl (counts only, never the reply text: the repo is public), and
prints one TELLS line so the next reply sees what the last one did wrong. Never blocks; exit 0 always.

    python _tools/prose/reply_tells.py --report [--days N]       tells per 1,000 words by day: is it working?
    python _tools/prose/reply_tells.py --baseline <transcript>   score every final reply in a transcript (not logged)
"""
import io, json, os, re, sys, time
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import prose_lint  # noqa: E402

LEDGER = os.path.join(HERE, "tells_ledger.jsonl")
NOISE = ("long-sentence", "passive", "header-short-file", "exclamation")  # the plain-register checks; counted, not named in the hint


def replies(path):
    """Final reply text of each turn: the last assistant record with text before the next real user prompt."""
    turns, last = [], None
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            try:
                r = json.loads(line)
            except ValueError:
                continue
            if r.get("isSidechain"):
                continue
            msg = r.get("message") or {}
            if r.get("type") == "assistant":
                text = "\n".join(c.get("text", "") for c in msg.get("content") or [] if isinstance(c, dict) and c.get("type") == "text")
                if text.strip():
                    last = text
            elif r.get("type") == "user":
                c = msg.get("content")
                real = isinstance(c, str) or any(isinstance(x, dict) and x.get("type") == "text" for x in c or [])
                if real and last:
                    turns.append(last)
                    last = None
    if last:
        turns.append(last)
    return turns


def score(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)       # code blocks are not prose
    text = re.sub(r"https?://\S+", "", text)
    words = len(re.findall(r"\b\w+\b", text))
    found = prose_lint.lint("reply.md", text)
    fams = Counter(f[3] for f in found)
    rules = Counter(f[1] for f in found)
    named = [f for f in found if f[1] not in NOISE]
    return words, found, fams, rules, named


def hook():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # not a new wrapper: the old one closes the buffer when collected
    d = json.load(sys.stdin)
    path = d.get("transcript_path")
    if not path or not os.path.exists(path):
        return
    rs = replies(path)
    if not rs:
        return
    words, found, fams, rules, named = score(rs[-1])
    if words < 15:
        return
    row = {"ts": time.strftime("%Y-%m-%d %H:%M"), "sid": (d.get("session_id") or "")[:8], "words": words,
           "tells": len(found), "per_1k": round(1000 * len(found) / words, 1), "families": dict(fams), "rules": dict(rules)}
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")
    top = "; ".join(f"{d_}" for _, _, d_, _ in named[:3])
    print(f"TELLS · last reply {len(found)} in {words} words ({row['per_1k']}/1k)"
          + (f" · fix next time: {top}" if top else "")
          + (f" · long sentences {rules['long-sentence']}" if rules.get("long-sentence") else ""))


def report(days):
    rows = []
    if os.path.exists(LEDGER):
        rows = [json.loads(l) for l in open(LEDGER, encoding="utf-8") if l.strip()]
    by = defaultdict(lambda: [0, 0, 0, Counter()])
    for r in rows:
        day = r["ts"][:10]
        b = by[day]
        b[0] += 1; b[1] += r["words"]; b[2] += r["tells"]; b[3].update(r.get("families", {}))
    print("day          replies  words   tells  per 1k  top families")
    for day in sorted(by)[-days:]:
        n, w, t, fam = by[day]
        print(f"{day}  {n:>7}  {w:>6}  {t:>6}  {1000 * t / max(w, 1):>6.1f}  " + ", ".join(f"{k} {v}" for k, v in fam.most_common(3)))


def baseline(path):
    rs = replies(path)
    tw = tt = 0
    fam = Counter()
    for t in rs:
        w, found, fams, _, _ = score(t)
        tw += w; tt += len(found); fam.update(fams)
    print(f"baseline · {len(rs)} replies · {tw} words · {tt} tells · {1000 * tt / max(tw, 1):.1f} per 1k")
    print("families: " + " · ".join(f"{k} {v}" for k, v in fam.most_common()))


if __name__ == "__main__":
    try:
        if "--report" in sys.argv:
            i = sys.argv.index("--days") + 1 if "--days" in sys.argv else None
            report(int(sys.argv[i]) if i else 14)
        elif "--baseline" in sys.argv:
            baseline(sys.argv[sys.argv.index("--baseline") + 1])
        else:
            hook()
    except Exception:
        pass
    sys.exit(0)
