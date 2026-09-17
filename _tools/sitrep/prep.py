"""SITREP prep — the zero-token half of the sit rep (BOLO 54, the formation).

Usage:  python _tools/sitrep/prep.py [YYYY-MM-DD[-n]]
        (defaults to today; if that board exists already, -2, -3 ...)

Does everything a script can do before any agent reads a word:
  work/<date>/prev/<block>.json   every block of the newest board, split out (the carry-forward)
  work/<date>/state.blocked.md    STATE.md, the Blocked table only
  work/<date>/state.live.md       STATE.md, the Live tables only (history stays behind)
  work/<date>/git.log             named commits since the previous board + the autosave FOOTPRINT, one line per
                                  session window (BOLO 59: an autosave is never an item, it dates one)
  work/<date>/state.moved.md      STATE.md, the Moved sections since the previous board (the fold Oscar Mike writes)
  work/<date>/meta.json           box probe · tree · rack · sizes · date (the page header)
  work/<date>/frag/III.json       carried forward (frozen since 8/15; flagged if PROJECTS.md moved)
  work/<date>/frag/VII.json       carried forward, the soi list refreshed from glossary.json
  work/<date>/brief.<ROLE>.md     one brief per specialist: RACK · INDEX · WATCH (paste as the prompt)
Then prints a 20-line digest. Nothing here costs a token.
"""
import io, json, os, re, socket, subprocess, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
BOARDS = os.path.join(HERE, "boards")
WORK = os.path.join(HERE, "work")
CACHE = os.path.join(ROOT, "_CACHE")
FIVE = ["SOP.md", "STATE.md", "BOLO.md", "PROJECTS.md"]


# Paths the sit rep itself writes — excluded from the git log handed to INDEX (see § 3)
EXHAUST = (
    "_tools/sitrep/boards",
    "_tools/sitrep/glossary.json",
    "SITREP.html",
    "_CACHE",
    "_devlog",
)


def load(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()


def dump(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(s)


def probe(port):
    s = socket.socket()
    s.settimeout(0.3)
    try:
        s.connect(("127.0.0.1", port))
        return True
    except OSError:
        return False
    finally:
        s.close()


def git(*args):
    try:
        return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True,
                              encoding="utf-8", errors="replace").stdout.strip()
    except Exception as e:
        return f"(git unavailable: {e})"


def slice_md(text, start_pat, end_pat):
    m = re.search(start_pat, text, re.M)
    if not m:
        return ""
    rest = text[m.start():]
    e = re.search(end_pat, rest[1:], re.M)
    return rest if not e else rest[: e.start() + 1]



def fold_log(raw, gap_min=45):
    """BOLO 59 (Chief 9/17): the autocommit fires on every turn stop, so the log since a board is
    mostly `autosave HH:MM · N file(s)` — footprints with no content. Handed raw to INDEX they
    become Fresh Ten items ("not yet folded"), the board reporting its own exhaust. Fold them:
    named commits stay one line each; autosaves collapse into one FOOTPRINT line per session
    window (consecutive autosaves less than `gap_min` apart) naming the folders touched."""
    import collections, datetime as dt
    commits = []
    for chunk in raw.split("@@")[1:]:
        head, _, body = chunk.partition("\n")
        parts = head.split(" ", 3)
        if len(parts) < 4:
            continue
        h, d, t, subj = parts
        files = [f.strip().strip(chr(34)) for f in body.split("\n") if f.strip()]   # git quotes odd paths
        commits.append({"h": h, "d": d, "t": t, "subj": subj, "files": files,
                        "auto": subj.lower().startswith("autosave")})
    named = [c for c in commits if not c["auto"]]
    autos = [c for c in commits if c["auto"]]   # newest first, as git prints
    windows = []
    for c in reversed(autos):                    # oldest first, so windows read forward in time
        stamp = dt.datetime.strptime(c["d"] + " " + c["t"], "%m/%d %H:%M")
        if windows and (stamp - windows[-1]["end"]).total_seconds() <= gap_min * 60:
            w = windows[-1]
            w["end"] = stamp; w["n"] += 1; w["files"].update(c["files"])
        else:
            windows.append({"start": stamp, "end": stamp, "n": 1, "files": set(c["files"])})
    out = ["# git since the previous board · named commits first, then the autosave FOOTPRINT",
           "# An autosave window is never an item on the Fresh Ten. It only dates items that the Live",
           "# tables or the Moved sections (state.moved.md) already name. (BOLO 59)", ""]
    out += [f"{c['h']} {c['d']} {c['t']} {c['subj']}" for c in named] or ["(no named commits)"]
    out += ["", f"# FOOTPRINT · {len(autos)} autosave commit(s) in {len(windows)} window(s)"]
    for w in reversed(windows):                  # newest window first, like the log
        tops = collections.Counter()
        for f in w["files"]:
            seg = f.split("/")
            tops["/".join(seg[:2]) if seg[0].startswith("_") and len(seg) > 2 else seg[0]] += 1
        where = ", ".join(f"{k} ({v})" for k, v in tops.most_common(6))
        out.append(f"{w['start']:%m/%d %H:%M}–{w['end']:%H:%M} · {w['n']} autosave(s) · "
                   f"{len(w['files'])} file(s) · {where}")
    return "\n".join(out), len(commits)


def moved_since(state, since):
    """Every `## ✅ Moved <date>` section whose first YYYY-MM-DD is on or after `since` — the fold
    that Oscar Mike writes, handed to INDEX so the Fresh Ten come from it (BOLO 59)."""
    out, keep = [], False
    for line in state.split("\n"):
        if line.startswith("## "):
            m = re.match(r"## ✅ Moved (\d{4}-\d{2}-\d{2})", line)
            keep = bool(m) and m.group(1) >= since
        if keep:
            out.append(line)
    return "\n".join(out).strip() + "\n"


def rel(p):
    return os.path.relpath(p, ROOT).replace("\\", "/")


CONTRACT = (
    "OUTPUT CONTRACT. Write ONLY the JSON file(s) named below, nothing else; the chat reply is three lines at most. "
    "Each block object keeps exactly the shape of its previous version (same keys: id · name · kind · plain · "
    "strand{last,plan,you,next} · items or groups). Every item carries its text as the previous version did (t, markdown, one to two sentences; Block V uses n · title · what · unblocks; the pmcs list uses item · s · status · next), "
    "trunk (BLACK · ORANGE · OPERATOR, or a slash combination), s (hot · open · held · gated · parked · done · ruled), "
    "and when (M/D or M/D HH:MM) where the block had it before. Keep [[key|label]] links only where the key already "
    "appears in the previous fragment; add no new keys. Write plain and strand in plain words for a reader who was not "
    "there: what we did last · what the plan was · what ACTUAL did · what's next. "
    "Do not read any file not listed here. Do not consult other agents. Do not fix other blocks."
)


def main():
    today = datetime.date.today().isoformat()
    date = sys.argv[1] if len(sys.argv) > 1 else today
    if len(sys.argv) < 2:
        n = 2
        while os.path.exists(os.path.join(BOARDS, date + ".json")):
            date = f"{today}-{n}"
            n += 1
    boards = sorted(f[:-5] for f in os.listdir(BOARDS) if f.endswith(".json"))
    prev_name = boards[-1] if boards else None
    prev = json.loads(load(os.path.join(BOARDS, prev_name + ".json"))) if prev_name else {"meta": {}, "blocks": []}
    wd = os.path.join(WORK, date)
    os.makedirs(os.path.join(wd, "frag"), exist_ok=True)

    # 1 · the carry-forward, one file per block
    prev_blocks = {b["id"]: b for b in prev["blocks"]}
    for bid, b in prev_blocks.items():
        dump(os.path.join(wd, "prev", f"{bid}.json"), b)
    dump(os.path.join(wd, "prev", "meta.json"), prev.get("meta", {}))

    # 2 · STATE sliced: the Blocked table and the Live tables only
    state = load(os.path.join(ROOT, "STATE.md"))
    write(os.path.join(wd, "state.blocked.md"), slice_md(state, r"^## 🔴 Blocked on you", r"^## "))
    write(os.path.join(wd, "state.live.md"), slice_md(state, r"^## 🟡 Live", r"^## ✅ Moved"))

    # 3 · git since the previous board
    #     The sit rep's own output is excluded: board JSONs, the built page, the SOI
    #     terms and the Oscar Mike pair are written BY a run, so without this they come
    #     back at the NEXT run as uncharacterized commits and sort to #1 of the Fresh
    #     Ten by recency — the board reporting on itself. Proved 9/16 (STATE, Known rot).
    since = prev_name[:10] if prev_name else "1 week ago"
    raw = git("log", f"--since={since} 00:00", "--date=format:%m/%d %H:%M", "--format=@@%h %ad %s",
              "--name-only", "--", ".", *(f":(exclude){p}" for p in EXHAUST))
    log, ncommits = fold_log(raw)
    write(os.path.join(wd, "git.log"), log + "\n")
    write(os.path.join(wd, "state.moved.md"), moved_since(state, since))
    dirty = git("status", "--porcelain")
    tree = "clean at open" if not dirty else f"{len(dirty.splitlines())} file(s) uncommitted at open"

    # 4 · the rack
    notes = sorted(f for f in os.listdir(CACHE) if f.endswith(".session.md"))
    rack = [{"file": f, "kb": os.path.getsize(os.path.join(CACHE, f)) // 1024} for f in notes]

    # 5 · sizes of the five (the drain, measured every time)
    sizes = {f: os.path.getsize(os.path.join(ROOT, f)) // 1024 for f in FIVE if os.path.exists(os.path.join(ROOT, f))}
    sizes["_CACHE"] = sum(r["kb"] for r in rack)

    stash, dark = probe(9999), probe(8484)
    meta = {
        "date": date[:10], "when": "", "trigger": "", "countersign": False,
        "version": "v0.9 · the formation (BOLO 54)",
        "box": [{"name": "Stash", "port": ":9999", "up": stash, "k": "stash"},
                {"name": "DARKROOM", "port": ":8484", "up": dark, "k": "darkroom"}],
        "rack": {"flushed": (", ".join(r["file"] for r in rack) + " → _LOG/") if rack else "(rack was empty)",
                 "staged": f"{date}.session.md"},
        "tree": tree, "stack": "empty", "agents": [], "stats": [],
        "main_effort": "",
        "build": {"files": "prep script + 3 fragments + the digest",
                  "read": f"{sum(sizes.values())} KB on disk, read by specialists, not the main line",
                  "calls": "", "rounds": ""},
        "prev_board": prev_name, "sizes_kb": sizes,
        "commits_since_prev": ncommits,
    }
    dump(os.path.join(wd, "meta.json"), meta)

    # 6 · carried blocks: III (frozen) and VII (soi refreshed from the register)
    iii_flag = "ok"
    if "III" in prev_blocks:
        iii = dict(prev_blocks["III"])
        pm = os.path.getmtime(os.path.join(ROOT, "PROJECTS.md"))
        bm = os.path.getmtime(os.path.join(BOARDS, prev_name + ".json"))
        if pm > bm:
            iii["_carried"] = "PROJECTS.md changed since the last board; main line to check"
            iii_flag = "FLAG: PROJECTS.md moved"
        else:
            iii["_carried"] = "carried; PROJECTS.md unchanged"
        dump(os.path.join(wd, "frag", "III.json"), iii)
    npro = 0
    if "VII" in prev_blocks:
        vii = dict(prev_blocks["VII"])
        gl = json.loads(load(os.path.join(HERE, "glossary.json")))
        pro = [(k, v) for k, v in gl.items()
               if v.get("k") == "proword" and v.get("st", "ruled") in ("ruled", "provisional")]
        npro = len(pro)
        if pro:
            vii["soi"] = [{"k": k, "w": v.get("t", k), "g": v.get("g") or v.get("d", "")[:140]} for k, v in pro]
        vii["_carried"] = f"soi refreshed from glossary.json ({npro} prowords)" if pro else "carried as-is"
        dump(os.path.join(wd, "frag", "VII.json"), vii)

    # 7 · the briefs, one per specialist, self-contained
    p = lambda *a: rel(os.path.join(wd, *a))
    briefs = {
        "RACK": (
            f"You are RACK, the Block 0 specialist for the sit rep of {date}. Model: haiku.\n"
            f"READ: every file in _CACHE/ ending .session.md ({', '.join(notes) or 'none'}), "
            f"and {p('prev', '0.json')} (the previous Block 0, for shape only).\n"
            f"WRITE: {p('frag', '0.json')} — Block 0 \"Last session\": one item per thing that moved, ruled, opened, "
            f"or closed across those notes, newest session first; the plain paragraph says in three sentences what "
            f"the last session(s) were.\n{CONTRACT}"),
        "INDEX": (
            f"You are INDEX, the STATE specialist for the sit rep of {date}. Model: sonnet.\n"
            f"READ: {p('state.blocked.md')} · {p('state.live.md')} · {p('state.moved.md')} · {p('git.log')} · and the previous fragments "
            f"{p('prev', 'I.json')} · {p('prev', 'II.json')} · {p('prev', 'V.json')}.\n"
            f"WRITE three files:\n"
            f"  {p('frag', 'I.json')}  — Block I \"The Fresh Ten\": the ten items touched most recently, newest first, "
            f"from the Moved sections (state.moved.md — what each session actually moved, the fold the close-out writes) "
            f"and the Live tables, dated by the named commits and the autosave FOOTPRINT windows in git.log; each with when · trunk · the one next step. "
            f"RULE (BOLO 59): an autosave commit or window is NEVER an item — it only dates one. Do not carry autosave "
            f"rows from the previous fragment forward; replace them with what moved. If a footprint window matches nothing "
            f"in Moved or Live, it is at most one item labelled 'unaccounted', never more.\n"
            f"  {p('frag', 'II.json')} — Block II \"The Ancients\": the same groups as before (true ancients · three weeks "
            f"or more · two to three weeks · a week or less); what each is waiting on.\n"
            f"  {p('frag', 'V.json')}  — Block V \"Blocked on you\": every numbered row of the Blocked table, in table "
            f"order, one item each, with what it unblocks.\n{CONTRACT}"),
        "WATCH": (
            f"You are WATCH, the BOLO specialist for the sit rep of {date}. Model: haiku.\n"
            f"READ: BOLO.md (the whole file) and {p('prev', 'IV.json')} (the previous Block IV, for shape only).\n"
            f"WRITE: {p('frag', 'IV.json')} — Block IV \"The BOLO board\": the same five groups (hot · held on a ruling · "
            f"fires on your go · open, slow · done not yet moved) with every active BOLO number placed in exactly one "
            f"group; the pmcs list from the PMCS table, one entry per row.\n{CONTRACT}"),
    }
    for role, text in briefs.items():
        write(os.path.join(wd, f"brief.{role}.md"), text + "\n")

    # 8 · the digest
    print(f"SITREP prep · board {date} · previous {prev_name}")
    print(f"work dir  {rel(wd)}")
    print(f"box       Stash {'UP' if stash else 'down'} · DARKROOM {'UP' if dark else 'down'} · tree: {tree}")
    print(f"rack      {len(rack)} note(s): {', '.join(r['file'] for r in rack) or '-'}")
    print("sizes KB  " + " · ".join(f"{k} {v}" for k, v in sizes.items()))
    print(f"git       {meta['commits_since_prev']} commit(s) since {since}")
    print(f"carried   III ({iii_flag}) · VII (soi {npro} prowords)")
    print("briefs    " + " · ".join(f"brief.{r}.md" for r in briefs))
    print("next      launch RACK (haiku) · INDEX (sonnet) · WATCH (haiku) in one message, each with its brief; then assemble.py")


if __name__ == "__main__":
    main()
