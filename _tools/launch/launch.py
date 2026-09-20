# -*- coding: utf-8 -*-
"""The launch sequence (BOLO 58) — "go for launch" (RULED 9/17) stands the Command up. Zero tokens.

Stations RULED 2026-09-17 by Chief: the sit rep page · the SOI · zero DOPE SHEETs ·
the DARKROOM · JUDY in session voice (whisper ears, face, Blondie reading) · her seven
spoken tools over the wire. This script brings the local stations up, opens the two
boards, and prints the station poll (GO / NO-GO with an address) for the sit rep header.
The sit rep itself runs in the formation after this (skill: launch → sitrep).

Usage:  python _tools/launch/launch.py [--no-pages] [--no-darkroom] [--no-stash] [--no-judy] [--no-knobs] [--no-wire] [--json]

Safe to run twice: a live DARKROOM is reported, not restarted (its single-instance guard);
a running JUDY session voice is reported, not restarted; a standalone JUDY (no --session)
is stopped first because both take the same hotkey.
"""
import io, os, sys, json, time, subprocess, argparse, datetime as dt, urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PY = sys.executable
DARKROOM = os.path.join(ROOT, "_PRIVATE", "taxonomy_engine", "darkroom_server.py")
DARK_URL = "http://127.0.0.1:8484/"
JUDY = os.path.join(ROOT, "_tools", "dictation", "judy.py")
PROBE = os.path.join(ROOT, "_tools", "dictation", "wire_probe.py")
KNOBS = os.path.join(ROOT, "_tools", "dictation", "knobs.py")   # BOLO 62: the MPK knobs as scroll + zoom
VIEW = os.path.join(ROOT, "_tools", "pages", "view.cmd")
STASH_EXE = os.path.join("Q:\\", "fun", ".StashApp", "stash-win.exe")          # BOLO 75: Stash is a station (9/20); shutdown leaves it running
STASH_CFG = os.path.join("Q:\\", "fun", ".StashApp", "config.yml")
STASH_URL = "http://127.0.0.1:9999/"
DECK = os.path.join(ROOT, "_PRIVATE", "stash_deck", "index.html")   # the Stash deck, opened in the default browser
PAGES = os.path.join(ROOT, "_tools", "pages", "pages.json")
BOARDS = ["sitrep", "soi"]           # RULED 9/17: the board · the SOI · zero DOPE SHEETs
TOOLS = ("blocked", "bolo", "box", "effort", "help", "pmcs", "time")


def ping(url, timeout=1.0):
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.status < 500
    except Exception:
        return False


def procs(pattern):
    """[(pid, commandline)] for processes whose command line matches the regex."""
    ps = ("Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match '%s' } | "
          "Select-Object ProcessId, CommandLine | ConvertTo-Json -Compress" % pattern)
    try:
        out = subprocess.run(["powershell", "-NoProfile", "-Command", ps],
                             capture_output=True, text=True, timeout=20).stdout.strip()
    except Exception:
        return []
    if not out:
        return []
    data = json.loads(out, strict=False)   # a command line can carry raw newlines (a heredoc); strict JSON chokes on them
    if isinstance(data, dict):
        data = [data]
    return [(d["ProcessId"], d.get("CommandLine") or "") for d in data
            if "powershell" not in (d.get("CommandLine") or "")]


def spawn_console(args, cwd=ROOT):
    """A detached process in its own minimized console window."""
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    si.wShowWindow = 7  # SW_SHOWMINNOACTIVE
    return subprocess.Popen(args, cwd=cwd, startupinfo=si,
                            creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.CREATE_NEW_PROCESS_GROUP,
                            stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                            close_fds=True)


def station_darkroom():
    t0 = time.time()
    if ping(DARK_URL + "api/ping"):
        return {"station": "DARKROOM", "go": True, "addr": DARK_URL, "note": "already live"}
    if not os.path.exists(DARKROOM):
        return {"station": "DARKROOM", "go": False, "addr": DARK_URL, "note": "server script missing"}
    spawn_console([PY, DARKROOM])
    for _ in range(40):
        time.sleep(0.5)
        if ping(DARK_URL + "api/ping"):
            return {"station": "DARKROOM", "go": True, "addr": DARK_URL,
                    "note": "started · %.1f s" % (time.time() - t0)}
    return {"station": "DARKROOM", "go": False, "addr": DARK_URL, "note": "no ping after 20 s"}


def station_stash():
    """BOLO 75 (9/20): Stash up on :9999, then the deck (a static page reading its GraphQL) in the browser."""
    t0 = time.time()
    was_up = ping(STASH_URL, timeout=2.0)
    if not was_up:
        if not os.path.exists(STASH_EXE):
            return {"station": "STASH", "go": False, "addr": STASH_URL, "note": "stash-win.exe missing"}
        try:
            subprocess.Popen([STASH_EXE, "-c", STASH_CFG], cwd=os.path.dirname(STASH_EXE),
                             creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.CREATE_NEW_PROCESS_GROUP,
                             stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e:
            return {"station": "STASH", "go": False, "addr": STASH_URL, "note": "start failed: %s" % e}
        for _ in range(60):
            time.sleep(1.0)
            if ping(STASH_URL, timeout=2.0):
                break
        else:
            return {"station": "STASH", "go": False, "addr": STASH_URL, "note": "no answer after 60 s"}
    deck = "deck opened" if os.path.exists(DECK) else "deck page missing"
    if os.path.exists(DECK):
        try:
            os.startfile(DECK)
        except Exception as e:
            deck = "deck failed: %s" % e
    return {"station": "STASH", "go": True, "addr": STASH_URL,
            "note": ("already live · " if was_up else "started · %.0f s · " % (time.time() - t0)) + deck}


def station_judy():
    t0 = time.time()
    running = procs(r"judy\.py")
    session = [p for p in running if "--session" in p[1]]
    if session:
        return {"station": "JUDY", "go": True, "addr": "session voice · pid %d" % session[0][0],
                "note": "already running"}
    for pid, _ in running:  # a standalone JUDY holds the same hotkey
        subprocess.run(["powershell", "-NoProfile", "-Command",
                        "Stop-Process -Id %d -Force -ErrorAction SilentlyContinue" % pid], capture_output=True)
    if running:
        time.sleep(1.0)
    p = spawn_console([PY, "-u", JUDY, "--session", "--naked"])   # BOLO 74 (9/20): Naked rides in JUDY's process
    time.sleep(6.0)  # whisper warm-loads in ~3 s; the face comes up with it
    if p.poll() is None:
        return {"station": "JUDY", "go": True, "addr": "session voice · pid %d" % p.pid,
                "note": "started · %.0f s · hold the hotkey with the chat box focused" % (time.time() - t0)}
    return {"station": "JUDY", "go": False, "addr": "session voice",
            "note": "exited at start (code %s); run judy.py --session by hand to see why" % p.returncode}


def station_knobs():
    """BOLO 62 (Chief, 9/17): the MPK knobs scroll and zoom whatever is under the pointer.
    The MIDI port is shareable, so this runs beside JUDY; a running daemon is reported, not restarted."""
    t0 = time.time()
    running = procs(r"knobs\.py.*--run")
    if running:
        return {"station": "KNOBS", "go": True, "addr": "MPK knobs · pid %d" % running[0][0], "note": "already running"}
    if not os.path.exists(KNOBS):
        return {"station": "KNOBS", "go": False, "addr": "MPK knobs", "note": "knobs.py missing"}
    p = spawn_console([PY, "-u", KNOBS, "--run"])
    time.sleep(1.5)
    if p.poll() is None:
        return {"station": "KNOBS", "go": True, "addr": "MPK knobs · pid %d" % p.pid,
                "note": "started · %.1f s · scroll Y · scroll X · zoom" % (time.time() - t0)}
    return {"station": "KNOBS", "go": False, "addr": "MPK knobs",
            "note": "exited at start (code %s); run knobs.py --run by hand to see why" % p.returncode}


def station_wire():
    t0 = time.time()
    if not os.path.exists(PROBE):
        return {"station": "WIRE", "go": False, "addr": "server judy (.mcp.json)", "note": "wire_probe.py missing"}
    try:
        r = subprocess.run([PY, PROBE], cwd=ROOT, capture_output=True, text=True, timeout=60,
                           encoding="utf-8", errors="replace")
    except subprocess.TimeoutExpired:
        return {"station": "WIRE", "go": False, "addr": "server judy (.mcp.json)", "note": "probe timed out"}
    ok = r.returncode == 0
    text = (r.stdout or "") + (r.stderr or "")
    tools = sum(1 for t in TOOLS if t in text)
    tail = (text.strip().splitlines() or ["probe failed"])[-1]
    return {"station": "WIRE", "go": ok, "addr": "server judy · %d/7 tools" % tools,
            "note": ("probe ok · %.1f s" % (time.time() - t0)) if ok else tail}


def station_pages():
    out = []
    try:
        pages = json.load(io.open(PAGES, encoding="utf-8"))
    except Exception:
        pages = {}
    for name in BOARDS:
        url = pages.get(name)
        if not url:
            out.append({"station": name.upper(), "go": False, "addr": "", "note": "not in pages.json"})
            continue
        try:
            subprocess.Popen(["cmd", "/c", VIEW, name], cwd=ROOT, stdin=subprocess.DEVNULL,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            out.append({"station": name.upper(), "go": True, "addr": url, "note": "opened"})
        except Exception as e:
            out.append({"station": name.upper(), "go": False, "addr": url, "note": str(e)})
    return out


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="the launch sequence (BOLO 58)")
    ap.add_argument("--no-pages", action="store_true")
    ap.add_argument("--no-darkroom", action="store_true")
    ap.add_argument("--no-stash", action="store_true")
    ap.add_argument("--no-judy", action="store_true")
    ap.add_argument("--no-wire", action="store_true")
    ap.add_argument("--no-knobs", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    rows = []
    if not a.no_darkroom:
        rows.append(station_darkroom())
    if not a.no_stash:
        rows.append(station_stash())
    if not a.no_judy:
        rows.append(station_judy())
    if not a.no_knobs:
        rows.append(station_knobs())
    if not a.no_wire:
        rows.append(station_wire())
    if not a.no_pages:
        rows += station_pages()
    stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    if a.json:
        print(json.dumps({"when": stamp, "stations": rows}, ensure_ascii=False, indent=1))
        return
    print("STATIONS · %s" % stamp)
    for r in rows:
        print("  %-9s %-6s %s  (%s)" % (r["station"], "GO" if r["go"] else "NO-GO", r["addr"], r["note"]))
    nogo = [r["station"] for r in rows if not r["go"]]
    print("  ALL GO" if not nogo else "  NO-GO: " + ", ".join(nogo))
    sys.exit(0 if not nogo else 1)


if __name__ == "__main__":
    main()
