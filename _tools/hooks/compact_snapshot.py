# -*- coding: utf-8 -*-
"""PreCompact hook (BOLO 162 call 2, Chief "take all recs" 10/31): writes a resume snapshot of 2 KB or less.

Zero tokens: it reads the transcript the hook hands over on stdin and the disk, nothing else. The snapshot holds
the last few orders (Chief's words), so it lives under _PRIVATE/compact/ (gitignored): <session8>.md plus latest.md.
The only public trace is one pointer line in the newest _CACHE session note. The digest (_tools/sitrep/digest.py)
prints the snapshot after a compact (SessionStart source "compact") or when it is under 2 hours old.

By hand / test:  python -X utf8 _tools/hooks/compact_snapshot.py < fake_hook.json   (add --out DIR to write elsewhere)
Exit 0 always; prints nothing."""
import glob, json, os, re, subprocess, sys, time

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
CAP = 2048          # bytes, the whole snapshot
TAIL = 4 * 1024 * 1024  # read at most the last 4 MB of the transcript
EDIT_TOOLS = ("Edit", "Write", "NotebookEdit", "MultiEdit")


def tail_lines(path):
    with open(path, "rb") as f:
        f.seek(0, 2)
        size = f.tell()
        f.seek(max(0, size - TAIL))
        data = f.read()
    lines = data.decode("utf-8", "replace").splitlines()
    if size > TAIL and lines:
        lines = lines[1:]  # the first line is cut
    out = []
    for ln in lines:
        try:
            out.append(json.loads(ln))
        except ValueError:
            pass
    return out


def text_of(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text")
    return ""


def one_line(s, n):
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def rel(p):
    try:
        r = os.path.relpath(p, ROOT)
        return p if r.startswith("..") else r.replace("\\", "/")
    except ValueError:
        return p


def scan(entries):
    orders, files, launches, later_text = [], [], {}, []
    for e in entries:
        msg = e.get("message") or {}
        if e.get("type") == "user" and not e.get("isMeta"):
            c = msg.get("content")
            if isinstance(c, list):  # tool results: catch background ids
                for b in c:
                    if isinstance(b, dict) and b.get("type") == "tool_result" and b.get("tool_use_id") in launches:
                        t = b.get("content")
                        t = t if isinstance(t, str) else text_of(t)
                        m = re.search(r"(?:ID|agentId|task[_ ]id)[:\s]+([A-Za-z0-9_-]{5,})", t or "")
                        if m:
                            launches[b["tool_use_id"]]["bid"] = m.group(1)
            t = text_of(c).strip()
            if t.startswith("<task-notification") or "<task-id>" in t:
                later_text.append(t)
            elif t and not t.startswith("<"):
                orders.append(t)
        elif e.get("type") == "assistant":
            for b in msg.get("content") or []:
                if not isinstance(b, dict) or b.get("type") != "tool_use":
                    continue
                name, inp = b.get("name", ""), b.get("input") or {}
                if name in EDIT_TOOLS and inp.get("file_path"):
                    p = rel(inp["file_path"])
                    if p in files:
                        files.remove(p)
                    files.append(p)
                elif (name == "Bash" and inp.get("run_in_background")) or name in ("Agent", "Task"):
                    launches[b.get("id")] = {"what": "%s: %s" % (name, inp.get("description") or one_line(inp.get("command", ""), 50)), "bid": None}
    notes = "\n".join(later_text)
    tasks = []
    for v in list(launches.values())[-4:]:
        done = bool(v["bid"]) and v["bid"] in notes
        tasks.append("%s (%s)" % (v["what"], "done" if done else "open or unknown"))
    return orders[-4:], files[-8:], tasks


def resume_block():
    notes = glob.glob(os.path.join(ROOT, "_CACHE", "*.session.md"))
    if not notes:
        return None, ""
    newest = max(notes, key=os.path.getmtime)
    try:
        with open(newest, encoding="utf-8") as f:
            txt = f.read()
    except OSError:
        return newest, ""
    m = re.search(r"^```resume\n(.*?)\n```", txt, re.M | re.S)
    return newest, (m.group(1).strip() if m else "")


def tree():
    try:
        s = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=5).stdout
        n = len([x for x in s.splitlines() if x.strip()])
        return "clean" if n == 0 else "%d file(s) uncommitted" % n
    except Exception:
        return "unknown"


def build(d):
    sid = (d.get("session_id") or "unknown")[:8]
    trig = d.get("trigger") or "?"
    src = d.get("transcript_path") or ""
    orders, files, tasks = scan(tail_lines(src)) if os.path.isfile(src) else ([], [], [])
    note, resume = resume_block()
    head = "RESUME SNAPSHOT · session %s · compact (%s) at %s · tree %s" % (
        sid, trig, time.strftime("%Y-%m-%d %I:%M %p"), tree())
    parts = [head]
    if orders:
        parts.append("last orders (oldest first):")
        parts += ["  - " + one_line(o, 200) for o in orders]
    if files:
        parts.append("files touched (newest last): " + " · ".join(files))
    if tasks:
        parts.append("background tasks: " + " · ".join(tasks))
    if resume:
        parts.append("newest _CACHE resume (%s):" % rel(note))
        parts += ["  " + one_line(ln, 160) for ln in resume.splitlines()[:6]]
    out = "\n".join(parts) + "\n"
    while len(out.encode("utf-8")) > CAP and len(parts) > 1:
        # trim the longest line first, then drop from the end
        i = max(range(1, len(parts)), key=lambda k: len(parts[k]))
        if len(parts[i]) > 80:
            parts[i] = parts[i][:max(60, len(parts[i]) // 2)] + "…"
        else:
            parts.pop()
        out = "\n".join(parts) + "\n"
    return sid, out, note


def main():
    out_dir = os.path.join(ROOT, "_PRIVATE", "compact")
    if "--out" in sys.argv:
        out_dir = sys.argv[sys.argv.index("--out") + 1]
    d = json.load(sys.stdin)
    sid, snap, note = build(d)
    os.makedirs(out_dir, exist_ok=True)
    for name in (sid + ".md", "latest.md"):
        with open(os.path.join(out_dir, name), "w", encoding="utf-8") as f:
            f.write(snap)
    if note and "--out" not in sys.argv:  # the one public trace: a pointer, no words
        with open(note, "a", encoding="utf-8") as f:
            f.write("- resume snapshot at %s: _PRIVATE/compact/%s.md (private, %d B)\n"
                    % (time.strftime("%I:%M %p").lstrip("0"), sid, len(snap.encode("utf-8"))))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
