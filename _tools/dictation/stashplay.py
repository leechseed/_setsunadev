"""
stashplay.py - Sensei's hands (BOLO 74, Chief 9/20: "I expected her to open up Stash and get some videos going").
Talks to Stash's GraphQL on :9999, picks a scene, and plays it fullscreen in VLC. Sensei's brain asks for it
with an action line at the end of a reply (`>> play: random`, `>> play: <words>`, `>> stop`, `>> next`);
naked.py strips the line, runs it here, and she says what she put on. Also a command:
    python stashplay.py random            # one from the UD pool (five stars, no dupes, no studio content)
    python stashplay.py "words to find"   # Stash's own search: title, performer, studio, tag, path
    python stashplay.py queue 10          # a set about ten minutes long from the pool (Chief 9/20)
    python stashplay.py queue 10 bbc      # the same, on a theme
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

FIELDS = "id title rating100 date files { path basename duration } performers { name } studio { name } tags { name }"


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


def play(sc):
    if not sc or not sc.get("files"):
        return None
    path = sc["files"][0]["path"]
    stop()
    if VLC:
        subprocess.Popen([VLC, "--fullscreen", "--play-and-exit", "--no-video-title-show", path],
                         stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        os.startfile(STASH + "/scenes/" + sc["id"])   # no VLC: Stash's own player in the browser
    try:
        io.open(LAST, "w", encoding="utf-8").write(json.dumps({"id": sc["id"], "path": path, "label": label(sc)}))
    except Exception:
        pass
    return label(sc)


def queue(minutes=10, q=None, max_clip=300):
    """A playlist about `minutes` long: random pool scenes (or search hits) no longer than max_clip seconds each,
    until the run time adds up. Plays them back to back, fullscreen."""
    import re
    want = int(minutes) * 60
    if q:
        d = gql('query($q:String){ findScenes(filter:{q:$q, per_page:80, sort:"rating", direction:DESC}) { scenes { %s } } }' % FIELDS, {"q": q})
    else:
        seed = rnd.randint(1, 10**9)
        d = gql('query($f:SceneFilterType,$s:String){ findScenes(scene_filter:$f, filter:{per_page:80, sort:$s}) { scenes { %s } } }' % FIELDS,
                {"f": _ud_filter(), "s": "random_%d" % seed})
    pool = [s for s in d["findScenes"]["scenes"] if s.get("files") and (s["files"][0].get("duration") or 0) > 5]
    rnd.shuffle(pool)
    picked, total = [], 0.0
    for s in pool:
        dur = s["files"][0]["duration"]
        if dur > max_clip and total > 0:
            continue
        picked.append(s)
        total += dur
        if total >= want:
            break
    if not picked:
        return None, 0
    m3u = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_stashplay_queue.m3u")
    io.open(m3u, "w", encoding="utf-8").write("#EXTM3U\n" + "".join("#EXTINF:%d,%s\n%s\n" % (s["files"][0]["duration"], label(s), s["files"][0]["path"]) for s in picked))
    stop()
    if VLC:
        subprocess.Popen([VLC, "--fullscreen", "--play-and-exit", "--no-video-title-show", m3u],
                         stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
            minutes = int(mq.group(2) or 10)
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
