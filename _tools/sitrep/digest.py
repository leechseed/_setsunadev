# -*- coding: utf-8 -*-
"""SESSION-OPEN DIGEST — BOLO 51 offload pick a (built 9/12 under the formation, BOLO 54).

Runs as a SessionStart hook; prints ~40 lines into context so the main line opens on a digest,
not on the five files (211 KB). Zero tokens to produce. Also runnable by hand:
    python _tools/sitrep/digest.py
"""
import io, os, re, socket, subprocess, sys, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def load(p):
    try:
        with io.open(os.path.join(ROOT, p), encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""

def probe(port):
    s = socket.socket(); s.settimeout(0.25)
    try:
        s.connect(("127.0.0.1", port)); return True
    except OSError:
        return False
    finally:
        s.close()

def git(*a):
    try:
        return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace").stdout.strip()
    except Exception:
        return ""

def first_bold(s):
    m = re.search(r"\*\*(.+?)\*\*", s)
    return (m.group(1) if m else s).strip()[:110]

def main():
    today = datetime.date.today()
    state, bolo = load("STATE.md"), load("BOLO.md")
    out = []
    out.append(f"SESSION-OPEN DIGEST · {today.isoformat()} · read this, not the five files (SOP §4 under the formation, BOLO 54)")
    out.append("gear 1 in force (3 agents; haiku fetch · sonnet write · Fable main). Skills: sitrep · oscar-mike · dope-sheet · frago · collect · rtb.")

    # the rack
    cache = os.path.join(ROOT, "_CACHE")
    notes = sorted(f for f in os.listdir(cache) if f.endswith(".session.md")) if os.path.isdir(cache) else []
    out.append(f"RACK · {len(notes)} note(s) staged" + (": " + ", ".join(notes) if notes else " (empty)"))
    if notes:
        last = load(os.path.join("_CACHE", notes[-1]))
        m = re.search(r"^# (.+)$", last, re.M)
        if m: out.append("  last note: " + m.group(1)[:120])
        m = re.search(r"\*\*Open at (?:this point|close)[^*]*\*\*(.+)", last)
        if m: out.append("  open at close: " + m.group(1).strip()[:200])

    # blocked on you
    blocked = state.split("## 🔴 Blocked on you")[-1].split("\n## ")[0] if "## 🔴 Blocked on you" in state else ""
    rows = re.findall(r"^\| \*\*(\d+)\*\* \| (.+?) \|", blocked, re.M)
    out.append(f"BLOCKED ON YOU · {len(rows)} row(s)")
    for n, t in rows:
        out.append(f"  #{n} {first_bold(t)}")

    # the watchlist: the newest six rows + anything red
    brows = re.findall(r"^\| (\d+) \| (.+?) \| (\d{4}-\d{2}-\d{2}) \| (.+?) \|$", bolo, re.M)
    brows.sort(key=lambda r: int(r[0]))
    out.append(f"BOLO · {len(brows)} active row(s); newest:")
    for n, t, d, s in brows[-6:]:
        out.append(f"  {n} {first_bold(t)[:80]} · {s.strip()[:60]}")
    reds = [n for n, t, d, s in brows if "🔴" in s and "done" not in s.lower()]
    if reds: out.append("  red: " + " · ".join(reds))
    pm = bolo.split("## PMCS")[-1].split("## Done")[0] if "## PMCS" in bolo else ""
    pm_rows = re.findall(r"^\| \*\*(.+?)\*\* .*?\| (🔴[^|]*)\|", pm, re.M)
    if pm_rows: out.append("PMCS red: " + " · ".join(f"{a.strip()} ({b.strip()[:30]})" for a, b in pm_rows))

    # the box and the tree
    out.append(f"BOX · Stash {'UP' if probe(9999) else 'down'} · DARKROOM {'UP' if probe(8484) else 'down'}")
    dirty = git("status", "--porcelain")
    out.append(f"TREE · {'clean' if not dirty else str(len(dirty.splitlines())) + ' file(s) uncommitted'} · last commit: {git('log', '-1', '--format=%h %ad %s', '--date=format:%m/%d %H:%M')[:90]}")

    # the main effort, from the newest board
    boards = os.path.join(ROOT, "_tools", "sitrep", "boards")
    bs = sorted(f for f in os.listdir(boards) if f.endswith(".json")) if os.path.isdir(boards) else []
    if bs:
        import json
        try:
            b = json.loads(load(os.path.join("_tools", "sitrep", "boards", bs[-1])))
            vi = next((x for x in b["blocks"] if x["id"] == "VI"), {})
            line = re.sub(r"\[\[[^|\]]+\|([^\]]+)\]\]", r"\1", vi.get("line", ""))[:120]
            out.append(f"MAIN EFFORT (board {bs[-1][:-5]}) · {line}")
        except Exception:
            pass
    sizes = {f: os.path.getsize(os.path.join(ROOT, f)) // 1024 for f in ("SOP.md", "STATE.md", "BOLO.md", "PROJECTS.md") if os.path.exists(os.path.join(ROOT, f))}
    out.append("ON DISK KB · " + " · ".join(f"{k} {v}" for k, v in sizes.items()) + " · open them on demand only; 'sit rep' runs the formation.")
    print("\n".join(out))

if __name__ == "__main__":
    main()
