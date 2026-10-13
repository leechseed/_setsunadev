# -*- coding: utf-8 -*-
"""The launch sequence (BOLO 58) — "go for launch" (RULED 9/17) stands the Command up. Zero tokens.

Stations RULED 2026-09-17 by Chief: the sit rep page · the SOI · zero DOPE SHEETs ·
the DARKROOM · JUDY in session voice (whisper ears, face, Blondie reading) · her seven
spoken tools over the wire. This script brings the local stations up, opens the two
boards, and prints the station poll (GO / NO-GO with an address) for the sit rep header.
The sit rep itself runs in the formation after this (skill: launch → sitrep).

Usage:  python _tools/launch/launch.py [--no-audit] [--no-pages] [--no-darkroom] [--no-stash] [--no-judy] [--no-faces] [--no-deck][--no-knobs] [--no-wire] [--json]

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
CONSOLE = os.path.join(ROOT, "_tools", "dictation", "console.py")   # JUDY's console; serves the face deck (10/4)
FACES_URL = "http://127.0.0.1:8787/faces"
DECK_URL = "http://127.0.0.1:8787/traffic"
VIEW = os.path.join(ROOT, "_tools", "pages", "view.cmd")
STASH_EXE = os.path.join("Q:\\", "fun", ".StashApp", "stash-win.exe")          # BOLO 75: Stash is a station (9/20); shutdown leaves it running
STASH_CFG = os.path.join("Q:\\", "fun", ".StashApp", "config.yml")
STASH_URL = "http://127.0.0.1:9999/"
DECK = os.path.join(ROOT, "_PRIVATE", "stash_deck", "index.html")   # the Stash deck, opened in the default browser
PAGES = os.path.join(ROOT, "_tools", "pages", "pages.json")
BOARDS = ["sitrep", "soi", "pullglass", "roster"]   # RULED 9/17: the board · the SOI · zero DOPE SHEETs; + the pull glass (Chief 10/12, BOLO 137) + the Roster (BOLO 139)
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


def spawn_console(args, cwd=ROOT, log=None):
    """A detached process in its own minimized console window. With log=path, stdout + stderr append there
    (10/4: JUDY kept dying with no trace because both went to DEVNULL)."""
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    si.wShowWindow = 7  # SW_SHOWMINNOACTIVE
    out, env = subprocess.DEVNULL, None
    if log:
        out = open(log, "a", encoding="utf-8")
        out.write("\n==== start %s · %s\n" % (time.strftime("%Y-%m-%d %H:%M:%S"), " ".join(args[1:])))
        out.flush()
        env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONFAULTHANDLER="1")   # faulthandler: native crashes (CUDA, audio) dump a trace
    return subprocess.Popen(args, cwd=cwd, startupinfo=si, env=env,
                            creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.CREATE_NEW_PROCESS_GROUP,
                            stdin=subprocess.DEVNULL, stdout=out, stderr=subprocess.STDOUT if log else subprocess.DEVNULL,
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


def station_nahimic():
    """Chief, 10/4 ("fuck that" · "add that to the launch startup"): Nahimic, the board's audio add-on, crashed ~20x
    on 10/4 and re-routed the audio devices under JUDY's mic. Its service and four logon tasks were disabled 10/4.
    Runs before JUDY: kills any Nahimic process still alive and reports whether the service or a task came back
    (a driver update can re-enable them; re-disabling needs admin, so this station reports it, never prompts)."""
    t0 = time.time()
    ps = ("$k = @(Get-Process | Where-Object { $_.Name -match 'nahimic' }); $k | Stop-Process -Force -ErrorAction SilentlyContinue; "
          "$s = (Get-Service NahimicService -ErrorAction SilentlyContinue).StartType; "
          "$t = @(Get-ScheduledTask -ErrorAction SilentlyContinue | Where-Object { $_.TaskName -match 'nahimic' -and $_.State -ne 'Disabled' }).Count; "
          "'{0}|{1}|{2}' -f $k.Count, $s, $t")
    try:
        r = subprocess.run(["powershell", "-NoProfile", "-Command", ps], capture_output=True, text=True, timeout=30)
        killed, start, tasks = (r.stdout.strip().splitlines() or ["0||0"])[-1].split("|")
    except Exception as e:
        return {"station": "NAHIMIC", "go": False, "addr": "audio guard", "note": "check failed: %s" % e}
    back = []
    if start and start != "Disabled":
        back.append("service is %s again" % start)
    if tasks not in ("", "0"):
        back.append("%s logon task(s) re-enabled" % tasks)
    note = ("killed %s process(es) · " % killed if killed not in ("", "0") else "") + \
           ("; ".join(back) + " · re-disable as admin" if back else "service + tasks disabled") + " · %.1f s" % (time.time() - t0)
    return {"station": "NAHIMIC", "go": not back, "addr": "audio guard", "note": note}


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
    p = spawn_console([PY, "-u", JUDY, "--session", "--naked", "--naked-no-face"],
                      log=os.path.join(os.path.dirname(JUDY), "judy.session.log"))   # BOLO 74 (9/20): Naked rides in JUDY's process; no picture at launch (Chief 9/24)
    time.sleep(6.0)  # whisper warm-loads in ~3 s; the face comes up with it
    if p.poll() is None:
        return {"station": "JUDY", "go": True, "addr": "session voice · pid %d" % p.pid,
                "note": "started · %.0f s · hold the hotkey with the chat box focused" % (time.time() - t0)}
    return {"station": "JUDY", "go": False, "addr": "session voice",
            "note": "exited at start (code %s); see _tools/dictation/judy.session.log" % p.returncode}


def chromium_app_exe():
    """The default browser's exe when it is Chrome or Edge (for --app), else None. FACES only;
    SITREP/SOI stay tabs (Chief 9/20)."""
    try:
        import winreg
        k = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                           r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\https\UserChoice")
        prog = winreg.QueryValueEx(k, "ProgId")[0]
        c = winreg.QueryValue(winreg.HKEY_CLASSES_ROOT, prog + r"\shell\open\command")
        exe = c.split('"')[1] if c.startswith('"') else c.split()[0]
        if os.path.basename(exe).lower() in ("chrome.exe", "msedge.exe") and os.path.exists(exe):
            return exe
    except Exception:
        pass
    # 10/4: the default is Firefox (no app mode); "make her an App" -> Chrome's --app window, Edge as the fallback
    for exe in (os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
                os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
                os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe"),
                os.path.expandvars(r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"),
                os.path.expandvars(r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe")):
        if os.path.exists(exe):
            return exe
    return None


def station_deck():
    """BOLO 116: the Traffic deck (/traffic) opens beside the face deck, same way. The console is already up after FACES."""
    try:
        if not ping(DECK_URL):
            return {"station": "DECK", "go": False, "addr": DECK_URL,
                    "note": "console has no /traffic (an old console; restart it)"}
        app = chromium_app_exe()
        if app:
            subprocess.Popen([app, "--app=" + DECK_URL], cwd=ROOT, stdin=subprocess.DEVNULL,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.Popen(["cmd", "/c", VIEW, DECK_URL], cwd=ROOT, stdin=subprocess.DEVNULL,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return {"station": "DECK", "go": True, "addr": DECK_URL, "note": "opened"}
    except Exception as e:
        return {"station": "DECK", "go": False, "addr": DECK_URL, "note": "failed: %s" % e}


def station_faces():
    """Chief, 10/4: JUDY's face deck comes up at every launch. The console (:8787) serves it;
    a live console is reported, not restarted. The deck opens as an app window when the default browser is Chrome/Edge (10/4), else a tab."""
    t0 = time.time()
    try:
        was_up = ping("http://127.0.0.1:8787/api/log")
        if not was_up:
            if not os.path.exists(CONSOLE):
                return {"station": "FACES", "go": False, "addr": FACES_URL, "note": "console.py missing"}
            spawn_console([PY, "-u", CONSOLE, "--no-open"])
            for _ in range(30):
                time.sleep(0.5)
                if ping("http://127.0.0.1:8787/api/log"):
                    break
            else:
                return {"station": "FACES", "go": False, "addr": FACES_URL, "note": "console gave no answer after 15 s"}
        if not ping(FACES_URL):
            return {"station": "FACES", "go": False, "addr": FACES_URL,
                    "note": "console is up but has no /faces (an old console; restart it)"}
        app = chromium_app_exe()
        if app:   # Chrome/Edge default: an app window (own name, icon, no address bar)
            subprocess.Popen([app, "--app=" + FACES_URL], cwd=ROOT, stdin=subprocess.DEVNULL,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            # Chief, 10/8: the console itself (refresh button, corner reel) opens as its own app window too
            subprocess.Popen([app, "--app=http://127.0.0.1:8787/"], cwd=ROOT, stdin=subprocess.DEVNULL,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.Popen(["cmd", "/c", VIEW, FACES_URL], cwd=ROOT, stdin=subprocess.DEVNULL,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return {"station": "FACES", "go": True, "addr": FACES_URL,
                "note": ("already live" if was_up else "started · %.1f s" % (time.time() - t0)) + " · opened"}
    except Exception as e:
        return {"station": "FACES", "go": False, "addr": FACES_URL, "note": "failed: %s" % e}


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


def station_frago():
    """BOLO 86: Oscar Mike staged _tools/launch/next.json; FRAGO every DOPE SHEET it names before the boards open.
    Zero tokens: the patch is one log line plus the version bump and today's asof. Built locally; the publish is the main line's."""
    nj = os.path.join(ROOT, "_tools", "launch", "next.json")
    if not os.path.exists(nj):
        return {"station": "FRAGO", "go": True, "addr": "next.json", "note": "nothing staged"}
    try:
        nxt = json.load(io.open(nj, encoding="utf-8"))
    except Exception as e:
        return {"station": "FRAGO", "go": False, "addr": "next.json", "note": "unreadable: %s" % e}
    sheets, done = nxt.get("sheets", []), nxt.get("frago_done", [])
    todo = [n for n in sheets if n not in done]
    if not todo:
        return {"station": "FRAGO", "go": True, "addr": "next.json", "note": "no sheet to refresh" if not sheets else "already refreshed"}
    frago = os.path.join(ROOT, "_tools", "bolostatus", "frago.py")
    patch = os.path.join(os.path.dirname(nj), "frago.patch.json")
    bad = []
    for n in todo:
        io.open(patch, "w", encoding="utf-8").write(json.dumps({"log": [{"who": "Claude", "t": "Launch refresh: reopened from the %s close-out." % nxt.get("note", "last")}]}))
        r = subprocess.run([PY, frago, str(n), patch, "--build"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
        if r.returncode:
            bad.append(str(n))
        else:
            done.append(n)
    nxt["frago_done"] = done
    io.open(nj, "w", encoding="utf-8", newline="\n").write(json.dumps(nxt, ensure_ascii=False, indent=1))
    return {"station": "FRAGO", "go": not bad, "addr": "next.json",
            "note": ("refreshed %s locally (republish owed)" % [n for n in todo if str(n) not in bad]) + ((" - failed %s" % bad) if bad else "")}


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


def station_pull():
    """BOLO 137, Chief 10/12: "run the process at the beginning with the glass whenever we run the launch sequence".
    Zero tokens: builds the pull glass from the queue + the wave logs and reports the waves. NO-GO only on a stalled
    wave. The publish to pages.json "pullglass" and the hourly update are the main line's (the launch skill)."""
    t0 = time.time()
    te = os.path.join(ROOT, "_PRIVATE", "taxonomy_engine")
    # standing order (Chief 10/12): the waves run until the queue is empty; a stopped runner is started here
    started = []
    for task in ("PullRunnerA", "PullRunnerB"):
        try:
            q = subprocess.run(["schtasks", "/Query", "/TN", task, "/FO", "LIST"], capture_output=True, text=True, timeout=30).stdout
            if "Running" not in q:
                subprocess.run(["schtasks", "/Run", "/TN", task], capture_output=True, timeout=30)
                started.append(task[-1])
        except Exception:
            pass
    try:
        r = subprocess.run([PY, os.path.join(te, "pull_queue.py"), "report"], cwd=te, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=60, env=dict(os.environ, PYTHONIOENCODING="utf-8"))
        g = subprocess.run([PY, os.path.join(te, "pull_glass.py")], cwd=te, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=60, env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    except Exception as e:
        return {"station": "PULL", "go": False, "addr": "pull glass", "note": "did not run: %s" % e}
    lines = [l for l in r.stdout.splitlines() if l.strip()]
    waves = [l for l in lines if l.startswith("wave ")]
    stalled = [l.split(":")[0] for l in waves if "STALLED" in l]
    if any("LOW:" in l for l in lines):
        stalled.append("Q disk low")
    if r.returncode or g.returncode:
        return {"station": "PULL", "go": False, "addr": "pull glass", "note": (r.stderr or g.stderr).strip().splitlines()[-1:]}
    live = "; ".join(l.split(" · 429s")[0] for l in waves) or "no wave running"
    note = "%s · %s · glass built, republish owed · %.1f s" % (live, lines[-1] if lines else "", time.time() - t0)
    if started:
        note = "runner %s started · " % "+".join(started) + note
    if stalled:
        note = "STALLED: %s · " % ", ".join(stalled) + note
    return {"station": "PULL", "go": not stalled, "addr": "pull glass", "note": note}


def station_audit():
    """Chief, 10/6: "audits to be done at the beginning of every launch, and that to be the first thing we always do."
    Runs the SOP audit (zero tokens) and reports its counts. NO-GO only on what needs Chief's eyes: private detail
    in a public file, BOLO hygiene, or an unflushed rack. Retired words and the tree are advisory."""
    t0 = time.time()
    try:
        out = subprocess.run([PY, os.path.join(ROOT, "_tools", "audit", "sop_audit.py")], cwd=ROOT,
                             capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120).stdout
    except Exception as e:
        return {"station": "AUDIT", "go": False, "addr": "SOP audit", "note": "did not run: %s" % e}
    counts = {}
    for line in out.splitlines():
        parts = line.split()
        if len(parts) >= 2 and len(parts[0]) == 1 and parts[0] in "RPBKTAS" and parts[-1].isdigit():
            counts[parts[0]] = int(parts[-1])
    total = sum(v for k, v in counts.items() if k != "A")
    hot = [k for k in "PBK" if counts.get(k)]
    note = "%d finding(s) · " % total + " · ".join("%s %d" % (k, counts.get(k, 0)) for k in "RPBKTS") +            " · report _tools/audit/out/ · %.1f s" % (time.time() - t0)
    return {"station": "AUDIT", "go": not hot, "addr": "SOP audit", "note": note}


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="the launch sequence (BOLO 58)")
    ap.add_argument("--no-audit", action="store_true")
    ap.add_argument("--no-pull", action="store_true")
    ap.add_argument("--no-pages", action="store_true")
    ap.add_argument("--no-frago", action="store_true")
    ap.add_argument("--no-darkroom", action="store_true")
    ap.add_argument("--no-stash", action="store_true")
    ap.add_argument("--no-judy", action="store_true")
    ap.add_argument("--no-nahimic", action="store_true")
    ap.add_argument("--no-faces", action="store_true")
    ap.add_argument("--no-deck", action="store_true")
    ap.add_argument("--no-wire", action="store_true")
    ap.add_argument("--no-knobs", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    rows = []
    if not a.no_audit:   # first, always (Chief 10/6): get it out of the way
        rows.append(station_audit())
    if not a.no_pull:    # right after the audit (Chief 10/12): the pull waves and their glass
        rows.append(station_pull())
    if not a.no_darkroom:
        rows.append(station_darkroom())
    if not a.no_stash:
        rows.append(station_stash())
    if not a.no_nahimic:
        rows.append(station_nahimic())   # before JUDY: her mic needs the devices to hold still
    if not a.no_judy:
        rows.append(station_judy())
    if not a.no_faces:
        rows.append(station_faces())
    if not a.no_deck and not a.no_faces:
        rows.append(station_deck())
    if not a.no_knobs:
        rows.append(station_knobs())
    if not a.no_wire:
        rows.append(station_wire())
    if not a.no_frago:
        rows.append(station_frago())   # BOLO 86: every staged sheet is FRAGO'd before the boards open
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
