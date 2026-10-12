"""
stashplay.py - Sensei's hands (BOLO 74, Chief 9/20: "I expected her to open up Stash and get some videos going").
Talks to Stash's GraphQL on :9999, picks a scene, and plays it fullscreen in VLC. Sensei's brain asks for it
with an action line at the end of a reply (`>> play: random`, `>> play: <words>`, `>> stop`, `>> next`);
naked.py strips the line, runs it here, and she says what she put on. Also a command:
    python stashplay.py random            # one from the UD pool (five stars, no dupes, no studio content)
    python stashplay.py "words to find"   # Stash's own search: title, performer, studio, tag, path
    python stashplay.py queue 30          # a set about thirty minutes long from the pool (Chief 9/20)
    python stashplay.py queue 30 bbc      # the same, on a theme
    python stashplay.py queue 30 "lesbian, gay, gangbang"   # themes in order, equal time each
    python stashplay.py stop              # close the player
"""
import io
import json
import os
import random as rnd
import subprocess
import sys
import urllib.request

STASH = "http://127.0.0.1:9999"
VLC = next((p for p in (r"C:\Program Files\VideoLAN\VLC\vlc.exe", r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe")
            if os.path.exists(p)), None)
LAST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_stashplay_last.json")

FIELDS = "id title rating100 date files { path basename duration } performers { name gender } studio { name } tags { name }"


def gql(query, variables=None):
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    r = urllib.request.urlopen(urllib.request.Request(STASH + "/graphql", data=body,
                               headers={"Content-Type": "application/json"}), timeout=30)
    d = json.load(r)
    if d.get("errors"):
        raise RuntimeError(d["errors"][0].get("message", "graphql error"))
    return d["data"]


def up():
    try:
        urllib.request.urlopen(STASH + "/graphql?query=%7Bversion%7Bversion%7D%7D", timeout=2)
        return True
    except Exception:
        return False


def _ud_filter():
    ids = []
    for name in ("dupe:cut", "⛔ studio-content"):
        t = gql('query($n:String!){ findTags(tag_filter:{name:{value:$n, modifier:EQUALS}}) { tags { id } } }', {"n": name})["findTags"]["tags"]
        if t:
            ids.append(t[0]["id"])
    f = {"rating100": {"value": 100, "modifier": "EQUALS"}}
    if ids:
        f["tags"] = {"value": ids, "modifier": "EXCLUDES"}
    return f


def pick_random():
    seed = rnd.randint(1, 10**9)
    d = gql('query($f:SceneFilterType,$s:String){ findScenes(scene_filter:$f, filter:{per_page:1, sort:$s}) { count scenes { %s } } }' % FIELDS,
            {"f": _ud_filter(), "s": "random_%d" % seed})["findScenes"]
    return d["scenes"][0] if d["scenes"] else None


def search(q, n=8):
    d = gql('query($q:String,$n:Int){ findScenes(filter:{q:$q, per_page:$n, sort:"rating", direction:DESC}) { count scenes { %s } } }' % FIELDS,
            {"q": q, "n": n})["findScenes"]
    return d["scenes"]


def label(sc):
    """Something she can say out loud: no emoji, no file extension, eight words at most."""
    import re
    who = ", ".join(p["name"] for p in (sc.get("performers") or [])[:2])
    studio = (sc.get("studio") or {}).get("name") if sc.get("studio") else None
    name = sc.get("title") or ""
    if not name and sc.get("files"):
        name = re.sub(r"\.[A-Za-z0-9]{2,4}$", "", sc["files"][0]["basename"])
    name = re.sub(r"[^\w\s,'&-]", " ", name)          # emoji and punctuation out
    name = re.sub(r"\s{2,}", " ", name).strip()
    words = name.split()
    if len(words) > 8:
        name = " ".join(words[:8])
    if who:
        return "%s, with %s" % (name, who) if name else who
    if studio:
        return "%s, from %s" % (name, studio) if name else "one from %s" % studio
    return name or "one from your pool"


def stop():
    subprocess.run(["taskkill", "/IM", "vlc.exe", "/F"], capture_output=True)
    return "stopped"


def _monitor(side="right"):
    """The rightmost (or leftmost) monitor's rect (left, top, right, bottom)."""
    import ctypes
    from ctypes import wintypes
    rects = []
    cb = ctypes.WINFUNCTYPE(ctypes.c_int, wintypes.HMONITOR, wintypes.HDC, ctypes.POINTER(wintypes.RECT), wintypes.LPARAM)
    ctypes.windll.user32.EnumDisplayMonitors(None, None, cb(lambda h, d, r, l: rects.append((r.contents.left, r.contents.top, r.contents.right, r.contents.bottom)) or 1), 0)
    return (max if side == "right" else min)(rects, key=lambda r: r[0])


def _pin(pid, side="right", wait=15):
    """Chief 10/12: VLC's own fullscreen snaps to the left screen no matter what. So: find the VLC window,
    strip its frame, and lay it over the whole right screen (borderless, same look as fullscreen)."""
    import ctypes
    import time
    from ctypes import wintypes
    u = ctypes.windll.user32
    x0, y0, x1, y1 = _monitor(side)
    found = []
    cb = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)

    def each(h, _):
        p = wintypes.DWORD()
        u.GetWindowThreadProcessId(h, ctypes.byref(p))
        if p.value == pid and u.IsWindowVisible(h) and u.GetWindowTextLengthW(h):
            found.append(h)
        return True
    end = time.time() + wait
    while time.time() < end and not found:
        time.sleep(0.3)
        u.EnumWindows(cb(each), 0)
    for h in found:
        style = u.GetWindowLongW(h, -16) & ~(0x00C00000 | 0x00040000)   # GWL_STYLE minus WS_CAPTION, WS_THICKFRAME
        u.SetWindowLongW(h, -16, style)
        u.SetWindowPos(h, 0, x0, y0, x1 - x0, y1 - y0, 0x0020 | 0x0040)   # SWP_FRAMECHANGED | SWP_SHOWWINDOW
    return bool(found)


def launch(target, side="right"):
    """Open VLC on one screen (right by default; Chief 10/12 two sets: "left" for the second): minimal view,
    no autoresize, then pinned borderless over that monitor. --no-one-instance lets both screens run at once."""
    p = subprocess.Popen([VLC, "--no-one-instance", "--qt-minimal-view", "--no-qt-video-autoresize", "--no-qt-fs-controller", "--play-and-exit",
                          "--no-video-title-show", target],
                         stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return _pin(p.pid, side)


def play(sc):
    if not sc or not sc.get("files"):
        return None
    path = sc["files"][0]["path"]
    stop()
    if VLC:
        launch(path)
    else:
        os.startfile(STASH + "/scenes/" + sc["id"])   # no VLC: Stash's own player in the browser
    try:
        io.open(LAST, "w", encoding="utf-8").write(json.dumps({"id": sc["id"], "path": path, "label": label(sc)}))
    except Exception:
        pass
    return label(sc)


BAD_TITLE = ("wife", "cuckold", "cuck", "hotwife")


def _gay_ok(sc):
    """BOLO 76 (9/24 evidence): the `gay` tag carries straight scenes. Out: the `straight` tag, any female
    performer, wife/cuckold titles."""
    if any((t.get("name") or "").lower() == "straight" for t in sc.get("tags") or []):
        return False
    if any((p.get("gender") or "").upper() in ("FEMALE", "TRANSGENDER_FEMALE") for p in sc.get("performers") or []):
        return False
    title = (sc.get("title") or "").lower()
    return not any(w in title for w in BAD_TITLE)


def _fill(want, q=None, max_clip=120, seen=(), long_every=5, long_max=360):
    """BOLO 76 set list: clips adding up to about `want` seconds, each under `max_clip` (two minutes), with one
    longer clip (up to `long_max`) in every `long_every`. Search hits for q, or random pool scenes. A `gay` theme
    runs through the straight filter."""
    if q:
        d = gql('query($q:String){ findScenes(filter:{q:$q, per_page:200, sort:"rating", direction:DESC}) { scenes { %s } } }' % FIELDS, {"q": q})
    else:
        seed = rnd.randint(1, 10**9)
        d = gql('query($f:SceneFilterType,$s:String){ findScenes(scene_filter:$f, filter:{per_page:200, sort:$s}) { scenes { %s } } }' % FIELDS,
                {"f": _ud_filter(), "s": "random_%d" % seed})
    pool = [s for s in d["findScenes"]["scenes"] if s.get("files") and (s["files"][0].get("duration") or 0) > 5 and s["id"] not in seen]
    if q and "gay" in q.lower():
        pool = [s for s in pool if _gay_ok(s)]
    rnd.shuffle(pool)
    dur_of = lambda s: s["files"][0]["duration"]
    short = [s for s in pool if dur_of(s) <= max_clip]
    longs = [s for s in pool if max_clip < dur_of(s) <= long_max]
    if not short:   # nothing short enough: take the shortest few rather than nothing
        short = sorted(pool, key=dur_of)[:3]
    picked, total, n = [], 0.0, 0
    while (short or longs) and total < want:
        n += 1
        src = longs if (n % long_every == 0 and longs) else (short or longs)
        s = src.pop()
        if total > 0 and total + dur_of(s) > want * 1.25:   # would overshoot by more than a quarter: skip it
            continue
        picked.append(s)
        total += dur_of(s)
    return picked, total


def queue(minutes=60, q=None, max_clip=120):
    """A playlist about `minutes` long (default 60, BOLO 76). Clips under two minutes, one longer in five.
    q = None for the pool, words for a theme, or "a, b, c" for themes in order, each getting an equal share of
    the time (Chief 9/20). Plays back to back, fullscreen."""
    want = int(minutes) * 60
    themes = [t.strip() for t in q.split(",")] if q and "," in q else [q]
    picked, total, seen = [], 0.0, set()
    for t in themes:
        part, dur = _fill(want / len(themes), t or None, max_clip, seen)
        picked += part
        total += dur
        seen |= {s["id"] for s in part}
    if not picked:
        return None, 0
    m3u = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_stashplay_queue.m3u")
    io.open(m3u, "w", encoding="utf-8").write("#EXTM3U\n" + "".join("#EXTINF:%d,%s\n%s\n" % (s["files"][0]["duration"], label(s), s["files"][0]["path"]) for s in picked))
    stop()
    if VLC:
        launch(m3u)
    try:
        io.open(LAST, "w", encoding="utf-8").write(json.dumps({"queue": [label(s) for s in picked], "minutes": round(total / 60, 1)}))
    except Exception:
        pass
    return picked, total


def act(action):
    """One action line from Sensei's brain -> what she should say about it. Never raises."""
    try:
        a = (action or "").strip()
        if not up():
            return "Stash isn't answering. Tell JUDY to bring it up."
        if a in ("stop", "kill", "off"):
            stop()
            return "Off."
        import re
        mq = re.match(r"^(queue|set|playlist)\b\s*:?\s*(\d+)?\s*(?:min(?:ute)?s?)?\s*(.*)$", a, re.I)
        if mq:
            minutes = int(mq.group(2) or 60)
            words = (mq.group(3) or "").strip()
            picked, total = queue(minutes, words or None)
            if not picked:
                return "Couldn't fill a set."
            return "Queued %d clips, about %d minutes.%s" % (len(picked), round(total / 60), (" First up, %s." % label(picked[0])))
        if a in ("random", "next", "surprise", "anything", "pool", ""):
            sc = pick_random()
            got = play(sc)
            return ("Putting on %s." % got) if got else "The pool's empty. That can't be right."
        hits = search(a)
        if not hits:
            sc = pick_random()
            got = play(sc)
            return ("Nothing for '%s', so: %s." % (a, got)) if got else "Nothing for that."
        got = play(hits[0])
        return "Putting on %s." % got
    except Exception as e:
        return "Couldn't. %s" % str(e)[:80]


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    print(act(" ".join(sys.argv[1:])))
