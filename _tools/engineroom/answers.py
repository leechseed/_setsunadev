"""answers.py: the Engine Room's answer store (BOLO 180 phase 2, Chief 11/4: "complete all of this within the program").

Chief answers a blank in the Engine Room window: take the rec, write his own, or skip it.
  answers  appended to _PRIVATE/engineroom/answers/answers.jsonl (private by default, ruled 11/4 call 1)
  skips    also go to _tools/engineroom/waivers.json (row id, time, who; no content), so the gate drops at once
  recs     read from _PRIVATE/engineroom/recs/<batch>.json (agents pre-draft them; *.rows.json are their inputs)
The answers reach the docs only when Chief says "apply answers" in chat (applying-ruled-calls). This module never writes
canon: safe_write() refuses any path outside the two allowed roots, and test_gate.py checks that.
"""
import io
import json
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
ANS_DIR = os.path.join(ROOT, "_PRIVATE", "engineroom", "answers")
ANS_FILE = os.path.join(ANS_DIR, "answers.jsonl")
RECS_DIR = os.path.join(ROOT, "_PRIVATE", "engineroom", "recs")
WAIVERS = os.path.join(HERE, "waivers.json")
ALLOWED = (os.path.realpath(ANS_DIR), os.path.realpath(WAIVERS))
MODES = ("answer", "rec", "skip")


def safe_write(path, text, append=False):
    real = os.path.realpath(path)
    if not (real == ALLOWED[1] or real.startswith(ALLOWED[0] + os.sep)):
        raise PermissionError("the Engine Room writes only its answer files, not " + path)
    os.makedirs(os.path.dirname(real), exist_ok=True)
    with io.open(real, "a" if append else "w", encoding="utf-8") as f:
        f.write(text)


def load_answers():
    """Latest record per row_id."""
    out = {}
    try:
        for line in io.open(ANS_FILE, encoding="utf-8"):
            line = line.strip()
            if line:
                try:
                    r = json.loads(line)
                    out[r["row_id"]] = r
                except (ValueError, KeyError):
                    continue
    except OSError:
        pass
    return out


def load_recs():
    out = {}
    if not os.path.isdir(RECS_DIR):
        return out
    for f in sorted(os.listdir(RECS_DIR)):
        if f.endswith(".json") and not f.endswith(".rows.json"):
            try:
                data = json.load(io.open(os.path.join(RECS_DIR, f), encoding="utf-8"))
                if isinstance(data, dict):
                    out.update(data)
            except (OSError, ValueError):
                continue
    return out


def save(p):
    mode = p.get("mode")
    if mode not in MODES or not p.get("row_id"):
        raise ValueError("an answer needs a row_id and a mode (answer, rec or skip)")
    ans = (p.get("answer") or "").strip()
    if mode == "answer" and not ans:
        raise ValueError("write an answer, or take the rec, or skip")
    rec = {
        "row_id": p["row_id"], "sys": p.get("sys"), "file": p.get("file"), "line": p.get("line"), "kind": p.get("kind"),
        "text": (p.get("text") or "")[:400], "mode": mode, "answer": ans, "source_note": (p.get("source_note") or "").strip(),
        "rec": p.get("rec") or "", "at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "status": "skipped" if mode == "skip" else "answered",
    }
    safe_write(ANS_FILE, json.dumps(rec, ensure_ascii=False) + "\n", append=True)
    if mode == "skip":
        try:
            w = json.load(io.open(WAIVERS, encoding="utf-8"))
        except (OSError, ValueError):
            w = []
        if not any(x.get("row_id") == p["row_id"] for x in w):
            w.append({"row_id": p["row_id"], "ruled_at": rec["at"], "by": "Chief (Engine Room)"})
        safe_write(WAIVERS, json.dumps(w, indent=1))
    return rec


def queue():
    """Answers waiting to be written into the docs (status answered)."""
    return [r for r in load_answers().values() if r.get("status") == "answered"]
