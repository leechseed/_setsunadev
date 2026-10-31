# -*- coding: utf-8 -*-
"""The Command Desk builder (BOLO 141). Live sources -> _PRIVATE/reference/desk/command-desk.html.

v3, 10/31 (Chief "go" on BOLO 141 live data): back to the mock's ideas on tonight's theme (BOLO 171):
one desk page, a left icon rail, GO/NO-GO pulse tiles, animated wave bars, dashed empty states, the hover layer.
Zero tokens. The page carries its data as JSON and draws itself; inside the Console it polls /desk.json
(console.py runs this script with --json, cached) every 60 s, so the tiles stay live without a rebuild.

Tiles and their sources:
  Stations  the newest launch result: _tools/launch/boot.jsonl or last_poll.json (whichever is newer),
            plus a 1 s ping of each station's local port (the URLs in launch.py). Never starts or stops anything.
  Pull      pull_queue.py json (counts only; board names never reach the desk)
  BOLO      BOLO.md rows parsed here: active / red / done counts, the six newest rows' numbers and short titles
  Notes     the newest _CACHE/*.session.md resume block (left-off, next, open); _LOG/ when _CACHE is empty
  Glasses   the Console's /glasses.json when :8795 answers (counts and the newest three titles)
Privacy: counts only; any title or note line that trips the private-word guard is held back.

Usage: python _tools/desk/build_desk.py             build the page (the Console serves it at /local/desk)
       python _tools/desk/build_desk.py --json      print the data, write nothing (the verb rule, BOLO 153)
       python _tools/desk/build_desk.py --dry-run   say what a build would write, write nothing
"""
import io, os, re, sys, json, glob, threading, datetime as dt, subprocess, urllib.request, urllib.error

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
OUT = os.path.join(ROOT, "_PRIVATE", "reference", "desk", "command-desk.html")
LAUNCH = os.path.join(ROOT, "_tools", "launch", "launch.py")
BOOT = os.path.join(ROOT, "_tools", "launch", "boot.jsonl")
POLL = os.path.join(ROOT, "_tools", "launch", "last_poll.json")
PQ = os.path.join(ROOT, "_PRIVATE", "taxonomy_engine", "pull_queue.py")
BOLO = os.path.join(ROOT, "BOLO.md")
CACHE = os.path.join(ROOT, "_CACHE")
LOG = os.path.join(ROOT, "_LOG")
GLASSES_URL = "http://127.0.0.1:8795/glasses.json"
CONSOLE_URL = "http://127.0.0.1:8795/"

# the private-word guard: a title or line that trips it is held back (the desk shows counts, never ORANGE detail)
PRIVATE = re.compile(r"\b(porn\w*|sex\w*|nsfw|nude\w*|naked|goon\w*|bbc|cock\w*|dick\w*|cum\w*|onlyfans|fansly|xxx|"
                     r"hentai|adult|erotic\w*|fetish\w*|kink\w*|hankey\w*|dildo\w*|ultrasin|stash\s+scene\w*)\b", re.I)
HELD = "(private, held back)"


def _theme(h, page=None):   # BOLO 171: the one theme for the launch pages (_tools/brand/theme.py); never fatal
    try:
        import importlib.util as _u
        _s = _u.spec_from_file_location("cmd_theme", os.path.join(ROOT, "_tools", "brand", "theme.py"))
        _m = _u.module_from_spec(_s); _s.loader.exec_module(_m)
        return _m.apply(h, page)
    except Exception:
        return h


def rd(p):
    try:
        return io.open(p, encoding="utf-8", errors="replace").read()
    except Exception:
        return ""


def t12(d):
    return "%d/%d %s" % (d.month, d.day, d.strftime("%I:%M %p").lstrip("0"))


def plain(s, n=160):
    s = re.sub(r"[*`]+", "", s or "")   # underscores stay: paths like _tools/ carry them
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + "…"


def guard(s):
    return HELD if PRIVATE.search(s or "") else s


# ---------- stations ----------

def launch_targets():
    """station -> (port, url), read from launch.py so the desk follows its ports; constants if it moves"""
    src = rd(LAUNCH)
    urls = dict(re.findall(r'^(\w+_URL) = "(http://127\.0\.0\.1:\d+/[^"]*)"', src, re.M))
    m = re.search(r'url = "(http://127\.0\.0\.1:\d+/)"', src)
    t = {"CONSOLE": m.group(1) if m else CONSOLE_URL,
         "DARKROOM": urls.get("DARK_URL", "http://127.0.0.1:8484/"),
         "STASH": urls.get("STASH_URL", "http://127.0.0.1:9999/"),
         "FACES": urls.get("FACES_URL", "http://127.0.0.1:8787/faces"),
         "DECK": urls.get("DECK_URL", "http://127.0.0.1:8787/traffic")}
    b = re.search(r"^BOARDS = \[(.*?)\]", src, re.M)
    boards = {x.upper() for x in re.findall(r'"(\w+)"', b.group(1))} if b else {"SITREP", "SOI", "PULLGLASS", "ROSTER", "ARMORY"}
    return {k: (int(re.search(r":(\d+)/", v).group(1)), v) for k, v in t.items()}, boards


def ping(url, timeout=1.0):
    """True when the port answers HTTP (any status under 500), False when nothing answers in time"""
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.status < 500
    except urllib.error.HTTPError as e:
        return e.code < 500
    except Exception:
        return False


def note_clean(s):
    """a launch note for the desk: drop the pull report's "on <board>" bits, then the private guard"""
    s = re.sub(r"(?:·\s*)?\bon [^·;)]+", "", s or "")
    s = re.sub(r"https?://127\.0\.0\.1:\d+/\S*\s*", "", s).strip()   # the port line already shows it
    if s.startswith("(") and s.endswith(")"):
        s = s[1:-1]
    return guard(plain(s, 220))


def launch_rows():
    """the newest launch: boot.jsonl (the live boot feed) when it is newer than last_poll.json, else the poll"""
    try:
        poll = json.load(io.open(POLL, encoding="utf-8"))
        ptime = dt.datetime.fromisoformat(poll.get("time", "")).timestamp()
    except Exception:
        poll, ptime = {}, 0
    evs = []
    for ln in rd(BOOT).splitlines():
        try:
            evs.append(json.loads(ln))
        except ValueError:
            pass
    btime = max((e.get("t", 0) for e in evs), default=0)
    if evs and btime > ptime + 30:
        rows, pages, in_pages = {}, {}, False
        for e in evs:
            if e.get("state") == "start" and e.get("station") == "PAGES":
                in_pages = True
            if e.get("state") == "done":
                (pages if in_pages else rows)[e["station"]] = {"name": e["station"], "go": bool(e.get("go")), "note": e.get("note", "")}
        running = not any(e.get("state") == "end" for e in evs)
        return list(rows.values()), list(pages.values()), btime, "boot.jsonl", running
    rows, pages, seen = [], [], set()
    _, boards = launch_targets()
    for r in poll.get("stations", []):
        n = r.get("name", "?")
        is_page = n in boards and (n not in ("ARMORY",) or n in seen)
        (pages if is_page else rows).append({"name": n, "go": bool(r.get("go")), "note": r.get("detail", "")})
        seen.add(n)
    return rows, pages, ptime, "last_poll.json", False


def stations():
    targets, _ = launch_targets()
    rows, pages, when, src, running = launch_rows()
    names = [r["name"] for r in rows] or list(targets)
    up = {}
    ths = [threading.Thread(target=lambda u=u: up.__setitem__(u, ping(u)), daemon=True)
           for u in {targets[n][1] for n in names if n in targets}]
    for t in ths:
        t.start()
    for t in ths:
        t.join(1.5)
    out = []
    byname = {r["name"]: r for r in rows}
    for n in names:
        r = byname.get(n, {"name": n, "go": None, "note": "not in the last launch"})
        port, url = targets.get(n, (None, None))
        live = up.get(url) if url else None
        if r["go"] is False:
            state, why = "NO-GO", "launch said NO-GO"
        elif live is False:
            state, why = "NO-GO", "port %d not answering now" % port
        elif r["go"] is None:
            state, why = "UNKNOWN", "not in the last launch"
        else:
            state, why = "GO", "launch GO" + (" · port answers" if live else "")
        out.append({"name": n, "state": state, "why": why, "launch_go": r["go"], "port": port, "port_up": live,
                    "note": note_clean(r["note"])})
    age_h = (dt.datetime.now().timestamp() - when) / 3600 if when else None
    return {"source": src, "launched": t12(dt.datetime.fromtimestamp(when)) if when else None,
            "age_hours": round(age_h, 1) if age_h is not None else None, "stale": bool(age_h and age_h > 12),
            "running": running, "go": sum(s["state"] == "GO" for s in out), "total": len(out), "rows": out,
            "pages": {"go": sum(p["go"] for p in pages), "total": len(pages)}}


# ---------- the pull queue ----------

def pull():
    try:
        p = subprocess.run([sys.executable, "-X", "utf8", PQ, "json"], cwd=os.path.dirname(PQ), capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=60, stdin=subprocess.DEVNULL)
        d = json.loads(p.stdout)
    except Exception as e:
        return {"ok": False, "error": "pull_queue.py json gave nothing (%s)" % type(e).__name__}
    keep = ("n", "state", "size", "done", "empty", "dropped", "left", "images", "pace", "eta", "e429", "quiet")
    waves = [{k: w.get(k) for k in keep} for w in d.get("waves", [])]       # counts only: no "current", no boards
    wmap = [{k: w.get(k) for k in ("n", "size", "got", "images", "state")} for w in d.get("map", [])]
    return {"ok": True, "when": d.get("when"), "pulled": d.get("pulled"), "total": d.get("total"), "images": d.get("images"),
            "held_video": d.get("held_video"), "q_free_gb": d.get("q_free_gb"), "low": d.get("low"),
            "waves": waves, "map": wmap, "landed": sum(w["state"] == "landed" for w in wmap)}


# ---------- BOLO ----------

MARK = re.compile(r"(✅|🟢|🟡|🟠|🔴|⏸️?|➡️|⬜|⬛|⛔|🔵|🟣|⚪)")
DONE_WORD = re.compile(r"^\W*(done|delivered|closed|folded)\b", re.I)


def bolo_state(status):
    """the status cell is a history, oldest first: its LAST mark is the row's state now.
    Done = a last ✅ that says DONE / DELIVERED / CLOSED / FOLDED (a last ✅ LIVE BOLO is live). The "## Done"
    heading is not used: new rows get appended at the file's end, under it (167-172 on 10/31), while still open."""
    ms = list(MARK.finditer(status))
    last = ms[-1].group(1) if ms else ""
    tail = plain(status[ms[-1].end():ms[-1].end() + 40]) if ms else ""
    if last == "✅" and DONE_WORD.search(tail):
        return "done"
    if last == "🔴":
        return "red"
    if last.startswith("⏸"):
        return "parked"
    if last == "✅":
        return "live"
    return "open"


def short_title(cell):
    m = re.search(r"\*\*(.+?)\*\*", cell)
    t = plain(m.group(1) if m else cell, 400)
    t = re.split(r":\s|\s[-—]\s", t)[0].strip()
    if len(t) > 52:
        t = t[:51].rstrip() + "…"
    return guard(t)


def bolo():
    rows = []
    for ln in rd(BOLO).splitlines():
        m = re.match(r"^\| (\d+) \|", ln)
        if not m:
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        rows.append({"n": int(m.group(1)), "title": short_title(cells[1] if len(cells) > 1 else ""),
                     "state": bolo_state(cells[-1])})
    if not rows:
        return {"ok": False, "error": "no BOLO rows found"}
    by = {}
    for r in rows:
        by[r["state"]] = by.get(r["state"], 0) + 1
    newest = sorted(rows, key=lambda r: r["n"])[-6:][::-1]
    return {"ok": True, "total": len(rows), "done": by.get("done", 0), "red": by.get("red", 0),
            "active": len(rows) - by.get("done", 0), "live": by.get("live", 0), "open": by.get("open", 0),
            "parked": by.get("parked", 0), "red_rows": sorted(r["n"] for r in rows if r["state"] == "red"),
            "newest": newest}


# ---------- notes ----------

def notes():
    fs = glob.glob(os.path.join(CACHE, "*.session.md")) or glob.glob(os.path.join(LOG, "*.session.md"))
    if not fs:
        return {"ok": False, "error": "no session notes in _CACHE/ or _LOG/"}
    f = max(fs, key=lambda p: (os.path.getmtime(p), p))
    m = re.search(r"^```resume\n(.*?)\n```", rd(f), re.M | re.S)
    out = {"ok": True, "file": os.path.relpath(f, ROOT).replace("\\", "/"),
           "written": t12(dt.datetime.fromtimestamp(os.path.getmtime(f)))}
    if not m:
        out.update(ok=False, error="the newest note has no resume block")
        return out
    keys, last = {}, None
    for ln in m.group(1).splitlines():
        k = re.match(r"^([a-z][\w-]*):\s*(.*)$", ln)
        if k:
            last = k.group(1)
            keys[last] = [k.group(2)] if k.group(2) else []
        elif last and ln.strip():
            keys[last].append(ln.strip())

    def items(k):
        return [guard(plain(re.sub(r"^-\s*", "", x), 240)) for x in keys.get(k, []) if x.strip("- ")]
    out.update({"left_off": items("left-off"), "next": items("next"), "open": items("open")})
    return out


# ---------- glasses ----------

def glasses():
    try:
        with urllib.request.urlopen(GLASSES_URL, timeout=1.0) as r:
            gs = json.loads(r.read().decode("utf-8")).get("glasses") or []
    except Exception:
        return {"up": False}
    now = dt.datetime.now(dt.timezone.utc)

    def when(g):
        try:
            return dt.datetime.fromisoformat(g.get("when", "").replace("Z", "+00:00"))
        except Exception:
            return None
    ws = [(g, when(g)) for g in gs]
    day = sum(1 for _, w in ws if w and (now - w).total_seconds() < 86400)
    newest = [{"title": guard(plain(g.get("title", "?"), 48)), "when": t12(w.astimezone()) if w else "?"}
              for g, w in sorted(ws, key=lambda x: x[1] or now.replace(year=2000), reverse=True)[:3]]
    return {"up": True, "total": len(gs), "day": day, "local": sum(1 for g in gs if g.get("local")), "newest": newest}


def collect():
    data = {"built": t12(dt.datetime.now()), "built_iso": dt.datetime.now().isoformat(timespec="seconds")}
    for k, fn in (("stations", stations), ("pull", pull), ("bolo", bolo), ("notes", notes), ("glasses", glasses)):
        try:
            data[k] = fn()
        except Exception as e:   # one tile's source failing never sinks the desk
            data[k] = {"ok": False, "error": "%s: %s" % (type(e).__name__, e)}
    return data


# ---------- the page ----------

CSS = r"""
/* the Command Desk v3, DARK only (9/11). Tokens come from the theme block (_tools/brand/theme.css). */
*{box-sizing:border-box}
html,body{background:var(--cmd-bg,#050608);color:var(--cmd-fg,#c6cbc8)}
body{margin:0;font:13px/1.5 var(--cmd-font,monospace)}
a{color:var(--cmd-acch,#FFB08F)}
header{position:sticky;top:0;z-index:20;height:var(--cmd-chrome,44px);display:flex;align-items:center;gap:12px;padding:0 16px;
  background:var(--cmd-panel,#0a0c0f);border-bottom:1px solid var(--cmd-line,#23272b)}
header h1{margin:0;font-size:14px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--cmd-acc,#FF5A1F)}
header .sp{flex:1}
header .st{color:var(--cmd-fg2);font-size:12px;white-space:nowrap}
header .st i{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--cmd-dim);margin-right:6px;vertical-align:1px}
header .st.live i{background:var(--cmd-ok);animation:pulse 2.4s ease-out infinite}
header .st.off i{background:var(--cmd-am)}
button{font:inherit;font-size:12px;background:var(--cmd-panel2);color:var(--cmd-fg);border:1px solid var(--cmd-line);padding:3px 10px;cursor:pointer}
button:hover,button:focus-visible{border-color:var(--cmd-acc);color:var(--cmd-acch);outline:none}
#meta{display:none;padding:8px 16px;background:var(--cmd-panel);border-bottom:1px solid var(--cmd-line);color:var(--cmd-fg2);font-size:12px}
#meta.on{display:block}
.wrap{display:grid;grid-template-columns:52px minmax(0,1fr);min-height:calc(100vh - 44px)}
nav{position:sticky;top:44px;align-self:start;display:flex;flex-direction:column;gap:2px;padding:10px 6px;height:calc(100vh - 44px);border-right:1px solid var(--cmd-line)}
nav a{display:flex;flex-direction:column;align-items:center;gap:2px;padding:7px 0 5px;color:var(--cmd-dim);text-decoration:none;border-left:2px solid transparent;font-size:9px;letter-spacing:.08em;text-transform:uppercase}
nav a svg{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
nav a:hover,nav a:focus-visible,nav a.on{color:var(--cmd-acc);border-left-color:var(--cmd-acc);outline:none;background:var(--cmd-accsoft)}
main{padding:14px 16px 40px;display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));align-content:start;min-width:0}
section{background:var(--cmd-panel);border:1px solid var(--cmd-line);padding:12px 14px 14px;min-width:0;scroll-margin-top:56px}
section.wide{grid-column:1/-1}
.side{display:grid;gap:14px;align-content:start;min-width:0}
section h2{margin:0 0 10px;display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 10px;font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--cmd-acc)}
section h2 small{font-weight:400;letter-spacing:.04em;text-transform:none;color:var(--cmd-dim);font-size:11px}
section h2 .r{margin-left:auto}
.empty{border:1px dashed var(--cmd-line2);padding:14px 12px;color:var(--cmd-fg2);text-align:center}
.chip{display:inline-block;white-space:nowrap;text-transform:none;letter-spacing:0;font-weight:400;border:1px solid var(--cmd-line2);padding:0 6px;font-size:11px;color:var(--cmd-fg2)}
.chip.am{border-color:var(--cmd-am);color:var(--cmd-am)} .chip.bad{border-color:var(--cmd-bad);color:var(--cmd-bad)} .chip.ok{border-color:var(--cmd-ok);color:var(--cmd-ok)}
.num{font-variant-numeric:tabular-nums}
/* stations: GO / NO-GO pulse tiles */
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}
.tile{position:relative;border:1px solid var(--cmd-line);background:var(--cmd-panel2);padding:8px 10px 7px;min-width:0;cursor:default}
.tile b{display:block;font-size:12px;font-weight:600;letter-spacing:.06em;color:var(--cmd-fg)}
.tile .s{font-size:11px;letter-spacing:.1em;font-weight:600}
.tile .p{font-size:11px;color:var(--cmd-dim);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tile .dot{position:absolute;top:10px;right:10px;width:9px;height:9px;border-radius:50%}
.tile.go{border-left:3px solid var(--cmd-ok)} .tile.go .s{color:var(--cmd-ok)} .tile.go .dot{background:var(--cmd-ok);animation:pulse 2.4s ease-out infinite}
.tile.no{border-left:3px solid var(--cmd-bad);background:var(--cmd-badsoft)} .tile.no .s{color:var(--cmd-bad)} .tile.no .dot{background:var(--cmd-bad);animation:pulsebad 1.2s ease-out infinite}
.tile.unk{border-left:3px dashed var(--cmd-line2)} .tile.unk .s{color:var(--cmd-dim)} .tile.unk .dot{background:var(--cmd-dim)}
.tile:hover{border-color:var(--cmd-acc)}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(78,201,111,.55)}70%{box-shadow:0 0 0 7px rgba(78,201,111,0)}100%{box-shadow:0 0 0 0 rgba(78,201,111,0)}}
@keyframes pulsebad{0%{box-shadow:0 0 0 0 rgba(229,96,77,.65)}70%{box-shadow:0 0 0 7px rgba(229,96,77,0)}100%{box-shadow:0 0 0 0 rgba(229,96,77,0)}}
.foot{margin-top:9px;color:var(--cmd-fg2);font-size:12px;display:flex;flex-wrap:wrap;gap:6px 14px}
/* pull: the wave bars */
.big{display:flex;flex-wrap:wrap;gap:6px 22px;margin-bottom:10px}
.big div{min-width:0} .big b{display:block;font-size:20px;font-weight:600;color:var(--cmd-white);line-height:1.2} .big small{color:var(--cmd-dim);font-size:11px}
.bars{display:flex;align-items:flex-end;gap:3px;height:74px;padding:0 0 2px;border-bottom:1px solid var(--cmd-line2)}
.bar{flex:1 1 0;min-width:4px;height:100%;position:relative}
.bar u{position:absolute;left:0;right:0;bottom:0;background:var(--cmd-inset);border-top:1px solid var(--cmd-line2)}
.bar i{position:absolute;left:0;right:0;bottom:0;background:var(--cmd-accm);transform-origin:bottom;animation:grow .9s cubic-bezier(.2,.8,.2,1) both}
.bar.landed i{background:var(--cmd-acc)}
.bar.run i{background:var(--cmd-acch);animation:grow .9s cubic-bezier(.2,.8,.2,1) both,wave 1.6s ease-in-out infinite alternate}
.bar.todo i{background:var(--cmd-line2)}
.bar.stall i{background:var(--cmd-bad);animation:grow .9s cubic-bezier(.2,.8,.2,1) both,wave .8s ease-in-out infinite alternate}
.bar:hover i{background:var(--cmd-white)}
@keyframes grow{from{transform:scaleY(0)}to{transform:scaleY(1)}}
@keyframes wave{from{opacity:1}to{opacity:.45}}
.axis{display:flex;justify-content:space-between;color:var(--cmd-dim);font-size:10px;margin-top:2px}
.runs{list-style:none;margin:10px 0 0;padding:0;display:grid;gap:6px}
.runs li{display:grid;grid-template-columns:64px minmax(0,1fr) 70px;gap:8px;align-items:center}
.runs .m{height:8px;background:var(--cmd-inset);position:relative;overflow:hidden}
.runs .m i{position:absolute;inset:0 auto 0 0;background:var(--cmd-acc)}
.runs .m i::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.35),transparent);animation:sweep 1.8s linear infinite}
@keyframes sweep{from{transform:translateX(-100%)}to{transform:translateX(100%)}}
.runs small{grid-column:2/-1;color:var(--cmd-dim);font-size:11px;margin-top:-4px}
/* BOLO */
.counts{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:10px}
.counts div{border:1px solid var(--cmd-line);padding:6px 10px;background:var(--cmd-panel2)}
.counts b{display:block;font-size:22px;font-weight:600;color:var(--cmd-white);line-height:1.15}
.counts .red b{color:var(--cmd-bad)} .counts .red{border-color:var(--cmd-bad)}
.counts small{color:var(--cmd-fg2);font-size:11px}
.rows{list-style:none;margin:0;padding:0}
.rows li{display:grid;grid-template-columns:40px minmax(0,1fr) 58px;gap:8px;padding:4px 0;border-top:1px dotted var(--cmd-line);align-items:baseline}
.rows .n{color:var(--cmd-acch)} .rows .w{text-align:right;font-size:11px;color:var(--cmd-fg2)}
.rows .w.red{color:var(--cmd-bad)} .rows .w.done{color:var(--cmd-dim)} .rows .w.live{color:var(--cmd-ok)}
/* notes */
.nb h3{margin:8px 0 3px;font-size:11px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--cmd-fg2)}
.nb h3:first-child{margin-top:0}
.nb ul{margin:0;padding:0 0 0 14px} .nb li{margin:2px 0;overflow-wrap:anywhere}
.nb li::marker{color:var(--cmd-acc)}
/* glasses */
.gl{list-style:none;margin:8px 0 0;padding:0}
.gl li{display:flex;justify-content:space-between;gap:10px;padding:4px 0;border-top:1px dotted var(--cmd-line)}
.gl li span:last-child{color:var(--cmd-dim);font-size:11px;white-space:nowrap}
/* the hover layer: dotted terms open a tip; click pins it; Space locks the open tips; terms nest */
.t{border-bottom:1px dotted var(--cmd-accm);cursor:help}
.tip{position:fixed;z-index:50;max-width:320px;background:var(--cmd-panel2);border:1px solid var(--cmd-acc);padding:8px 10px;font-size:12px;line-height:1.45;color:var(--cmd-fg);box-shadow:0 6px 24px rgba(0,0,0,.6)}
.tip b{color:var(--cmd-acch);display:block;margin-bottom:2px;font-size:11px;letter-spacing:.1em;text-transform:uppercase}
.tip.pin{border-style:double;border-width:3px}
.tip .hint{display:block;margin-top:5px;color:var(--cmd-dim);font-size:10px}
@media(max-width:560px){.wrap{grid-template-columns:40px minmax(0,1fr)} nav a span{display:none} main{grid-template-columns:minmax(0,1fr);padding:12px 16px 40px}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""

JS = r"""
(function(){
"use strict";
var D=JSON.parse(document.getElementById("desk-data").textContent);
function E(s){return String(s==null?"":s).replace(/[&<>"']/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})}
function N(x){return x==null?"?":Number(x).toLocaleString("en-US")}
function T(k,txt){return '<span class="t" data-t="'+k+'" tabindex="0">'+E(txt)+'</span>'}
function X(txt,body){return '<span class="t" data-x="'+E(body)+'" tabindex="0">'+E(txt)+'</span>'}
var EMPTY=function(s){return '<div class="empty">'+E(s)+'</div>'};
var TERMS={
 go:["GO","The station came up in the last {launch} and, if it has a {port}, the port answers now."],
 nogo:["NO-GO","Either the last {launch} said NO-GO, or the station's {port} does not answer now. The note under the tile says which."],
 launch:["The launch","\"Go for launch\" runs _tools/launch/launch.py. It writes boot.jsonl as it goes and last_poll.json at the end. The desk reads the newer one."],
 port:["Port ping","When the desk refreshes, it asks each local server one question with a 1 second limit. It never starts or stops a station."],
 stale:["Stale","The last {launch} is more than 12 hours old. The GO words may be old; the port pings are fresh."],
 boards:["Boards","The pages the {launch} opens (sit rep, SOI, pull glass, Roster, Armory). Under one window the Console opens them, so they read 'not opened'."],
 wave:["Wave","One batch of boards the pull works through. Each bar is a wave: its height is the wave's image count against the biggest wave, and the orange fill is the share of its boards pulled. A {landed} wave is full; a {stalled} one blinks red."],
 landed:["Landed","Every board in the {wave} has been pulled (done, empty or dropped)."],
 stalled:["Stalled","A running {wave} whose log has been quiet far longer than its pace. The bar blinks red."],
 held:["Held video","Video files the pull set aside instead of downloading. A count only."],
 qfree:["Q free","Free space on the Q: drive, where the pull saves. Under 200 GB the desk flags it low."],
 e429:["429s","'Too many requests' answers in the recent pull log. A climbing count means the site is slowing the pull."],
 active:["Active","Every BOLO row not done: {live}, open, parked and {red}. Read from BOLO.md each refresh."],
 red:["Red","A row whose newest status mark is the red circle: hot or blocked."],
 done:["Done","A row whose newest mark is a check followed by DONE, DELIVERED, CLOSED or FOLDED."],
 live:["Live","A row whose newest mark is the check with LIVE BOLO: checked by Chief and in the rotation."],
 state:["Row state","The status cell keeps a history, oldest first. The desk reads the last mark in it as the row's state now: {red}, {live}, {done}, open or parked."],
 resume:["Resume block","The fenced 'resume' block at the top of the newest session note in _CACHE/. Oscar Mike writes it."],
 glass:["Glass","A page published as an artifact. The Console keeps the recent ones in its glasses list."],
 refresh:["Refresh","Inside the Console the desk asks /desk.json for fresh data every 60 seconds. The Console caches it for 30 seconds."]
};
function tipHTML(k){var t=TERMS[k];if(!t)return"";return "<b>"+E(t[0])+"</b>"+E(t[1]).replace(/\{(\w+)\}/g,function(_,w){return TERMS[w]?T(w,TERMS[w][0].toLowerCase()):w})}

var ICON={
 stations:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="2.5"/><path d="M7.5 7.5a6.4 6.4 0 0 0 0 9M16.5 7.5a6.4 6.4 0 0 1 0 9M4.6 4.6a10.4 10.4 0 0 0 0 14.8M19.4 4.6a10.4 10.4 0 0 1 0 14.8"/></svg>',
 pull:'<svg viewBox="0 0 24 24"><path d="M4 20V13M9 20V8M14 20v-9M19 20V5"/></svg>',
 bolo:'<svg viewBox="0 0 24 24"><path d="M5 6h14M5 12h14M5 18h9"/><circle cx="19" cy="18" r="1.4"/></svg>',
 notes:'<svg viewBox="0 0 24 24"><path d="M6 3h9l3 3v15H6z"/><path d="M9 10h6M9 14h6M9 18h3"/></svg>',
 glasses:'<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="12" rx="1"/><path d="M8 21h8M12 17v4"/></svg>'
};
var NAV=[["stations","Stn"],["pull","Pull"],["bolo","BOLO"],["notes","Notes"],["glasses","Glass"]];

function head(id,title,sub,right){return '<h2>'+E(title)+'<small>'+sub+'</small>'+(right?'<span class="r">'+right+'</span>':'')+'</h2>'}

function stations(s){
 if(!s||s.ok===false)return head("stations","Stations","")+EMPTY("No launch result on file: "+((s&&s.error)||"run go for launch"));
 var right=s.stale?'<span class="chip am">'+T("stale","stale")+'</span>':(s.running?'<span class="chip am">launch running</span>':'');
 var tiles=s.rows.map(function(r){
  var c=r.state==="GO"?"go":(r.state==="NO-GO"?"no":"unk");
  var port=r.port?(":"+r.port+(r.port_up?" answers":(r.port_up===false?" silent":""))):"no port";
  var body=r.name+" · "+r.state+"\n"+r.why+(r.note?"\nlaunch note: "+r.note:"");
  return '<div class="tile '+c+'" tabindex="0" data-x="'+E(body)+'"><span class="dot"></span><b>'+E(r.name)+'</b>'+
   '<span class="s">'+(c==="go"?T("go","GO"):c==="no"?T("nogo","NO-GO"):E(r.state))+'</span><div class="p">'+E(port)+'</div><div class="p">'+E(r.note||r.why)+'</div></div>'}).join("");
 var foot='<div class="foot"><span class="num">'+s.go+'/'+s.total+' GO</span><span>last '+T("launch","launch")+' '+E(s.launched||"?")+'</span><span>'+T("port","ports pinged")+' at build</span>'+
  (s.pages&&s.pages.total?'<span>'+T("boards","boards")+' '+s.pages.go+'/'+s.pages.total+' GO</span>':'')+'</div>';
 return head("stations","Stations","GO / NO-GO from the launch, checked live",right)+(s.rows.length?'<div class="tiles">'+tiles+'</div>':EMPTY("The last launch listed no stations."))+foot}

function pull(p){
 if(!p||!p.ok)return head("pull","Pull queue","")+EMPTY((p&&p.error)||"No pull data.");
 var big='<div class="big"><div><b class="num">'+N(p.pulled)+'/'+N(p.total)+'</b><small>boards pulled</small></div><div><b class="num">'+N(p.images)+'</b><small>images</small></div>'+
  '<div><b class="num">'+N(p.held_video)+'</b><small>'+T("held","held video")+'</small></div><div><b class="num'+(p.low?'" style="color:var(--cmd-bad)':'')+'">'+N(Math.round(p.q_free_gb))+' GB</b><small>'+T("qfree","Q free")+(p.low?' · LOW':'')+'</small></div></div>';
 var mx=Math.max.apply(null,p.map.map(function(w){return w.images||0}).concat([1]));
 var bars=p.map.length?'<div class="bars">'+p.map.map(function(w,i){var f=w.size?w.got/w.size:0,hgt=Math.max(6,Math.round(100*(w.images||0)/mx));var c=w.state==="landed"?"landed":(w.state==="todo"?"todo":(w.state==="pulling"?"run":(w.state==="stalled"?"stall":"part")));
   return '<div class="bar '+c+'" tabindex="0" data-x="'+E("Wave "+w.n+" · "+w.state+"\n"+w.got+" of "+w.size+" boards · "+N(w.images)+" images")+'"><u style="height:'+hgt+'%"></u><i style="height:'+Math.max(3,Math.round(hgt*f))+'%;animation-delay:'+(i*35)+'ms"></i></div>'}).join("")+'</div>'+
   '<div class="axis"><span>'+T("wave","wave")+' '+p.map[0].n+'</span><span>'+p.landed+' of '+p.map.length+' '+T("landed","landed")+'</span><span>wave '+p.map[p.map.length-1].n+'</span></div>':EMPTY("No waves in the queue.");
 var runs=p.waves.length?'<ul class="runs">'+p.waves.map(function(w){var f=w.size?Math.round(100*(w.done||0)/w.size):0;
   return '<li><span>wave '+w.n+'</span><span class="m"><i style="width:'+f+'%"></i></span><span class="num">'+(w.done||0)+'/'+w.size+'</span><small>'+E(w.state)+' · '+N(w.left)+' left · '+(w.pace||"-")+' min/board · ETA '+E(w.eta||"-")+' · '+T("e429","429s")+' '+(w.e429||0)+'</small></li>'}).join("")+'</ul>'
   :'<div class="empty" style="margin-top:10px">No waves running now.</div>';
 return head("pull","Pull queue","BOLO 137 · counts only",'<span class="chip">'+E(p.when||"")+'</span>')+big+bars+runs}

function bolo(b){
 if(!b||!b.ok)return head("bolo","BOLO","")+EMPTY((b&&b.error)||"No BOLO data.");
 var counts='<div class="counts"><div><b class="num">'+b.active+'</b><small>'+T("active","active")+'</small></div><div class="'+(b.red?'red':'')+'"><b class="num">'+b.red+'</b><small>'+T("red","red")+(b.red_rows.length?' · '+b.red_rows.join(" "):'')+'</small></div><div><b class="num">'+b.done+'</b><small>'+T("done","done")+'</small></div></div>';
 var split='<div class="foot" style="margin:0 0 8px">'+b.live+' '+T("live","live")+' · '+b.open+' open · '+b.parked+' parked · '+b.total+' rows</div>';
 var rows='<ul class="rows">'+b.newest.map(function(r){return '<li><span class="n num">'+r.n+'</span><span>'+E(r.title)+'</span><span class="w '+r.state+'">'+E(r.state)+'</span></li>'}).join("")+'</ul>';
 return head("bolo","BOLO","the watchlist · newest six",'<span class="chip">'+T("state","row state")+'</span>')+counts+split+rows}

function notes(n){
 if(!n||n.ok===false)return head("notes","Notes","")+EMPTY((n&&n.error)||"No session note.");
 function L(h,a){return '<h3>'+h+'</h3>'+(a&&a.length?'<ul>'+a.map(function(x){return '<li>'+E(x)+'</li>'}).join("")+'</ul>':'<div class="empty">Nothing listed.</div>')}
 return head("notes","Notes","the newest "+T("resume","resume block"),'<span class="chip">'+E(n.written)+'</span>')+'<div class="nb">'+L("Left off",n.left_off)+L("Next",n.next)+L("Open",n.open)+'</div>'}

function glasses(g){
 if(!g||!g.up)return head("glasses","Glasses","")+EMPTY("The Console (:8795) did not answer, so no glasses list.");
 var big='<div class="big"><div><b class="num">'+g.total+'</b><small>'+T("glass","glasses")+' listed</small></div><div><b class="num">'+g.day+'</b><small>in the last 24 h</small></div><div><b class="num">'+g.local+'</b><small>open in the Console</small></div></div>';
 var l=g.newest.length?'<ul class="gl">'+g.newest.map(function(x){return '<li><span>'+E(x.title)+'</span><span>'+E(x.when)+'</span></li>'}).join("")+'</ul>':EMPTY("No glasses yet.");
 return head("glasses","Glasses","the Console's recent pages")+big+l}

function render(d){
 var m=document.querySelector("main");
 m.innerHTML='<section id="stations" class="wide">'+stations(d.stations)+'</section><section id="pull">'+pull(d.pull)+'</section><section id="bolo">'+bolo(d.bolo)+'</section><div class="side"><section id="notes">'+notes(d.notes)+'</section><section id="glasses">'+glasses(d.glasses)+'</section></div>';
 document.getElementById("built").textContent="data "+d.built;
}
document.querySelector("nav").innerHTML=NAV.map(function(n){return '<a href="#'+n[0]+'" title="'+n[1]+'">'+ICON[n[0]]+'<span>'+n[1]+'</span></a>'}).join("");
render(D);

/* refresh: inside the Console the page polls /desk.json; opened as a file it keeps the build's data */
var st=document.getElementById("live");
function setLive(ok,txt){st.className="st "+(ok?"live":"off");st.lastChild.textContent=txt}
if(/^https?:$/.test(location.protocol)){
 setLive(true,"live · 60 s");
 var poll=function(){fetch("/desk.json",{cache:"no-store"}).then(function(r){if(!r.ok)throw 0;return r.json()}).then(function(d){D=d;render(d);setLive(true,"live · 60 s")}).catch(function(){setLive(false,"refresh failed, showing "+D.built)})};
 setInterval(poll,60000);
}else setLive(false,"file copy · no refresh");

/* the hover layer (CK3, 9/16): hover opens, click pins, Space locks every open tip, Esc clears; tips nest */
var stack=[],locked=false,timer=null;
function close(from){while(stack.length>from){var t=stack.pop();t.el.remove()}}
function open(trg,level){
 if(stack[level]&&stack[level].trg===trg)return;
 close(level);
 var html=trg.dataset.t?tipHTML(trg.dataset.t):E(trg.dataset.x).replace(/\n/g,"<br>");
 if(!html)return;
 var el=document.createElement("div");el.className="tip";el.innerHTML=html+'<span class="hint">click pins · Space locks · Esc clears</span>';
 document.body.appendChild(el);
 var r=trg.getBoundingClientRect(),w=el.offsetWidth,h=el.offsetHeight;
 var x=Math.min(Math.max(8,r.left),innerWidth-w-8),y=r.bottom+6;if(y+h>innerHeight-8)y=Math.max(8,r.top-h-6);
 el.style.left=x+"px";el.style.top=y+"px";el.dataset.level=level;
 stack.push({trg:trg,el:el,pin:false});
}
function levelOf(node){var t=node.closest&&node.closest(".tip");return t?(+t.dataset.level+1):0}
document.addEventListener("mouseover",function(e){
 var trg=e.target.closest&&e.target.closest("[data-t],[data-x]");
 var inTip=e.target.closest&&e.target.closest(".tip");
 if(trg){clearTimeout(timer);open(trg,levelOf(trg));return}
 if(inTip){clearTimeout(timer);close(+inTip.dataset.level+1);return}
 if(locked||!stack.length)return;
 clearTimeout(timer);timer=setTimeout(function(){var keep=0;stack.forEach(function(s,i){if(s.pin)keep=i+1});close(keep)},260);
});
document.addEventListener("focusin",function(e){var trg=e.target.closest&&e.target.closest("[data-t],[data-x]");if(trg)open(trg,levelOf(trg))});
document.addEventListener("click",function(e){
 var trg=e.target.closest&&e.target.closest("[data-t],[data-x]");
 if(trg){var lv=levelOf(trg);open(trg,lv);if(stack[lv]){stack[lv].pin=!stack[lv].pin;stack[lv].el.classList.toggle("pin",stack[lv].pin)}return}
 if(!(e.target.closest&&e.target.closest(".tip"))){locked=false;close(0)}
});
document.addEventListener("keydown",function(e){
 if(e.key===" "&&stack.length){e.preventDefault();locked=!locked;stack.forEach(function(s){s.el.classList.toggle("pin",locked||s.pin)})}
 else if(e.key==="Escape"){locked=false;close(0)}
});
document.getElementById("mb").onclick=function(){var m=document.getElementById("meta").classList.toggle("on");this.setAttribute("aria-expanded",m)};
document.querySelector("nav").addEventListener("click",function(e){var a=e.target.closest("a");if(!a)return;[].forEach.call(this.querySelectorAll("a"),function(x){x.classList.toggle("on",x===a)})});
})();
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Command Desk</title>
<style>__CSS__</style>
</head>
<body>
<header>
<h1>Command Desk</h1>
<span class="st" id="built"></span>
<span class="sp"></span>
<span class="st" id="live" data-t="refresh"><i></i><span>…</span></span>
<button id="mb" aria-expanded="false" aria-controls="meta">Info</button>
</header>
<div id="meta">BOLO 141 · built by _tools/desk/build_desk.py, zero tokens. Stations: the newest launch result (boot.jsonl or last_poll.json) plus a 1 second ping of each station's port. Pull: pull_queue.py json, counts only. BOLO: BOLO.md rows. Notes: the newest _CACHE session note's resume block. Glasses: the Console's /glasses.json. Inside the Console the desk refreshes from /desk.json every 60 seconds. Dotted words open a tip: click pins, Space locks, Esc clears.</div>
<div class="wrap">
<nav aria-label="Tiles"></nav>
<main></main>
</div>
<script type="application/json" id="desk-data">__DATA__</script>
<script>__JS__</script>
</body>
</html>
"""


def page(data):
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    h = PAGE.replace("__CSS__", CSS).replace("__JS__", JS).replace("__DATA__", blob)
    return _theme(h, "desk")


def main(argv):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    if "-h" in argv or "--help" in argv:
        print(__doc__)
        return 0
    data = collect()
    if "--json" in argv:
        print(json.dumps(data, ensure_ascii=False, indent=1))
        return 0
    h = page(data)
    st, b = data.get("stations", {}), data.get("bolo", {})
    summary = "stations %s/%s GO | pull %s/%s boards | BOLO %s active, %s red, %s done | glasses %s" % (
        st.get("go", "?"), st.get("total", "?"), data.get("pull", {}).get("pulled", "?"), data.get("pull", {}).get("total", "?"),
        b.get("active", "?"), b.get("red", "?"), b.get("done", "?"),
        data.get("glasses", {}).get("total", "off") if data.get("glasses", {}).get("up") else "off")
    if "--dry-run" in argv:
        print("dry run: would write %d bytes -> %s" % (len(h.encode("utf-8")), OUT))
        print(summary)
        return 0
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(h)
    print("desk built: %d bytes -> %s" % (len(h.encode("utf-8")), OUT))
    print(summary)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
