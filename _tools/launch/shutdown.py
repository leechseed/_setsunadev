# -*- coding: utf-8 -*-
"""The closing sequence (BOLO 58, Chief 9/17: "the reverse of what the launch sequence is").
Runs inside Oscar Mike before the close-out. Zero tokens.

Stations down, in reverse of launch.py: the board windows (the sit rep page and the SOI
app windows) closed · JUDY session voice stopped · the DARKROOM server stopped. The wire
belongs to VS Code and stays; Stash is not ours and stays.

Usage:  python _tools/launch/shutdown.py [--keep-darkroom] [--keep-judy] [--keep-pages] [--json]
"""
import os, sys, json, time, subprocess, argparse, datetime as dt, ctypes, ctypes.wintypes as W, urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import launch  # noqa: E402  (procs, ping)

DARK_URL = "http://127.0.0.1:8484/"
PAGE_TITLES = ("SOI", "SITREP", "SIT REP", "THE BOARD")
user32 = ctypes.windll.user32
WM_CLOSE = 0x0010


def stop_pid(pid):
    subprocess.run(["powershell", "-NoProfile", "-Command",
                    "Stop-Process -Id %d -Force -ErrorAction SilentlyContinue" % pid], capture_output=True)


def station_judy():
    running = launch.procs(r"judy\.py")
    if not running:
        return {"station": "JUDY", "go": True, "addr": "session voice", "note": "was not running"}
    for pid, _ in running:
        stop_pid(pid)
    time.sleep(0.8)
    left = launch.procs(r"judy\.py")
    return {"station": "JUDY", "go": not left, "addr": "session voice",
            "note": "stopped pid %s" % ", ".join(str(p) for p, _ in running) if not left else "still running: %s" % [p for p, _ in left]}


def station_darkroom():
    running = launch.procs(r"darkroom_server\.py")
    if not running and not launch.ping(DARK_URL + "api/ping"):
        return {"station": "DARKROOM", "go": True, "addr": DARK_URL, "note": "was down"}
    for pid, _ in running:
        stop_pid(pid)
    for _ in range(20):
        time.sleep(0.25)
        if not launch.ping(DARK_URL + "api/ping"):
            return {"station": "DARKROOM", "go": True, "addr": DARK_URL, "note": "stopped"}
    return {"station": "DARKROOM", "go": False, "addr": DARK_URL, "note": "still answering on :8484"}


def page_windows():
    out = []
    P = ctypes.WINFUNCTYPE(ctypes.c_bool, W.HWND, W.LPARAM)

    def cb(h, _):
        if not user32.IsWindowVisible(h):
            return True
        n = user32.GetWindowTextLengthW(h)
        if n <= 0:
            return True
        b = ctypes.create_unicode_buffer(n + 1); user32.GetWindowTextW(h, b, n + 1)
        c = ctypes.create_unicode_buffer(64); user32.GetClassNameW(h, c, 64)
        t = b.value.strip()
        if c.value == "Chrome_WidgetWin_1" and (t.upper() in PAGE_TITLES or any(t.upper().startswith(p) for p in PAGE_TITLES)) \
                and "Visual Studio Code" not in t:
            out.append((h, t))
        return True

    user32.EnumWindows(P(cb), 0)
    return out


def station_pages():
    wins = page_windows()
    if not wins:
        return [{"station": "PAGES", "go": True, "addr": "the board · the SOI", "note": "no page windows open"}]
    for h, t in wins:
        user32.PostMessageW(h, WM_CLOSE, 0, 0)
    time.sleep(0.6)
    left = page_windows()
    return [{"station": "PAGES", "go": not left, "addr": "the board · the SOI",
             "note": "closed %d window(s): %s" % (len(wins), " · ".join(t for _, t in wins)) if not left else "still open: %s" % [t for _, t in left]}]


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="the closing sequence (BOLO 58)")
    ap.add_argument("--keep-darkroom", action="store_true"); ap.add_argument("--keep-judy", action="store_true")
    ap.add_argument("--keep-pages", action="store_true"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    rows = []
    if not a.keep_pages:
        rows += station_pages()
    if not a.keep_judy:
        rows.append(station_judy())
    if not a.keep_darkroom:
        rows.append(station_darkroom())
    stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    if a.json:
        print(json.dumps({"when": stamp, "stations": rows}, ensure_ascii=False, indent=1)); return
    print("STATIONS DOWN · %s" % stamp)
    for r in rows:
        print("  %-9s %-6s %s  (%s)" % (r["station"], "DOWN" if r["go"] else "STUCK", r["addr"], r["note"]))
    stuck = [r["station"] for r in rows if not r["go"]]
    print("  ALL DOWN" if not stuck else "  STUCK: " + ", ".join(stuck))
    sys.exit(0 if not stuck else 1)


if __name__ == "__main__":
    main()
