# -*- coding: utf-8 -*-
"""The recent glasses (BOLO 153, Chief 10/18): every page Claude published, newest first, with the local file
it came from, so the Console opens the glass inside its own window instead of a browser tab.

Reads   ~/.claude/projects/*/*.jsonl (main-line transcripts only; agents never publish)
        and finds each Artifact result line "Published <file> at <url> (Version N ...)".
Writes  _tools/console/glasses.json   {"at": ..., "glasses": [{id, title, url, file, when, local}]}
Zero tokens. Usage: python glasses.py [--days 30] [--print]
"""
import glob, hashlib, json, os, re, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "glasses.json")
PROJECTS = os.path.join(os.path.expanduser("~"), ".claude", "projects")
PUB = re.compile(r"Published (.+?) at (https://claude\.ai/\S+?) \(Version")
TITLE = re.compile(r"<title>(.*?)</title>", re.I | re.S)


def texts(content):
    """the text inside one tool_result's content (a string or a list of blocks)"""
    if isinstance(content, str):
        return [content]
    out = []
    for b in content or []:
        if isinstance(b, dict) and isinstance(b.get("text"), str):
            out.append(b["text"])
    return out


def title_of(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            m = TITLE.search(f.read(40000))
        if m:
            return re.sub(r"\s+", " ", m.group(1)).strip()[:80]
    except OSError:
        pass
    return os.path.splitext(os.path.basename(path))[0]


def scan(days=30):
    cut = time.time() - days * 86400
    seen = {}   # url -> entry, newest publish wins
    for f in glob.glob(os.path.join(PROJECTS, "*", "*.jsonl")):
        try:
            if os.path.getmtime(f) < cut:
                continue
            fh = open(f, encoding="utf-8", errors="replace")
        except OSError:
            continue
        with fh:
            for line in fh:
                if "Published " not in line or "tool_result" not in line:
                    continue
                try:
                    ev = json.loads(line)
                except ValueError:
                    continue
                when = ev.get("timestamp") or ""
                msg = ev.get("message") or {}
                for blk in msg.get("content") or []:
                    if not isinstance(blk, dict) or blk.get("type") != "tool_result":
                        continue
                    for t in texts(blk.get("content")):
                        for path, url in PUB.findall(t[:2000]):
                            old = seen.get(url)
                            if not old or when > old["when"]:
                                seen[url] = {"url": url, "file": path.strip(), "when": when}
    out = []
    for e in seen.values():
        local = os.path.isfile(e["file"])
        e["local"] = local
        e["title"] = title_of(e["file"]) if local else os.path.splitext(os.path.basename(e["file"]))[0]
        e["id"] = hashlib.sha1(e["url"].encode("utf-8")).hexdigest()[:10]
        out.append(e)
    out.sort(key=lambda e: e["when"], reverse=True)
    return out


def write(days=30):
    g = scan(days)
    tmp = OUT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump({"at": time.strftime("%Y-%m-%d %H:%M:%S"), "glasses": g}, f, ensure_ascii=False, indent=1)
    os.replace(tmp, OUT)
    return g


if __name__ == "__main__":
    days = int(sys.argv[sys.argv.index("--days") + 1]) if "--days" in sys.argv else 30
    t0 = time.time()
    g = write(days)
    print("glasses: %d (%d local) · %.1f s · %s" % (len(g), sum(e["local"] for e in g), time.time() - t0, OUT))
    if "--print" in sys.argv:
        for e in g[:25]:
            print("  %s  %-5s %-40s %s" % (e["when"][:16], "local" if e["local"] else "web", e["title"][:40], e["url"]))
