# -*- coding: utf-8 -*-
"""PreCompact hook (steer-08): backs up the transcript to _LOG/transcripts/ and notes it in the newest _CACHE session note.
Exit 0 always; prints nothing."""
import glob, json, os, shutil, sys, time
try:
    d = json.load(sys.stdin)
    root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    src = d.get("transcript_path") or ""
    if os.path.isfile(src):
        out = os.path.join(root, "_LOG", "transcripts")
        os.makedirs(out, exist_ok=True)
        name = "%s-%s.jsonl" % (time.strftime("%Y-%m-%d"), (d.get("session_id") or "unknown")[:8])
        shutil.copyfile(src, os.path.join(out, name))
        notes = glob.glob(os.path.join(root, "_CACHE", "*.session.md"))
        if notes:
            newest = max(notes, key=os.path.getmtime)
            t = time.strftime("%I:%M %p").lstrip("0")
            with open(newest, "a", encoding="utf-8") as f:
                f.write("\n- compact at %s: transcript backed up to _LOG/transcripts/%s\n" % (t, name))
except Exception:
    pass
sys.exit(0)
