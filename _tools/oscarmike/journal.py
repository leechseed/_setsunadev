# -*- coding: utf-8 -*-
"""OSCAR MIKE journal — append the day's journal entry from the Ready Rack note (zero tokens).

Usage:  python _tools/oscarmike/journal.py [_CACHE/<note>.session.md]
        (default: the newest note in _CACHE/)

Appends to _devlog/_devlog_docs/_devlog_journals/MMDDYYYY.journal.md (created if missing):
  a `## HH:MM · Oscar Mike — <title>` header, the note's bullets verbatim, the AAR line last.
Idempotent per note: if the journal already carries this note's title, nothing is appended.
"""
import io, os, re, sys, datetime, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
JDIR = os.path.join(ROOT, "_devlog", "_devlog_docs", "_devlog_journals")

def main():
    if len(sys.argv) > 1:
        note = os.path.join(ROOT, sys.argv[1]) if not os.path.isabs(sys.argv[1]) else sys.argv[1]
    else:
        notes = sorted(glob.glob(os.path.join(ROOT, "_CACHE", "*.session.md")), key=os.path.getmtime)
        if not notes: print("no note in _CACHE/"); sys.exit(1)
        note = notes[-1]
    text = io.open(note, encoding="utf-8").read()
    m = re.search(r"^# Session note — (.+)$", text, re.M)
    title = m.group(1).strip() if m else os.path.basename(note)
    bullets = [l for l in text.splitlines() if l.startswith("- ")]
    now = datetime.datetime.now()
    jp = os.path.join(JDIR, now.strftime("%m%d%Y") + ".journal.md")
    os.makedirs(JDIR, exist_ok=True)
    existing = io.open(jp, encoding="utf-8").read() if os.path.exists(jp) else ""
    if title in existing:
        print(f"journal already carries: {title}"); return
    block = f"\n\n## {now.strftime('%H:%M')} · Oscar Mike — {title}\n\n" + "\n".join(bullets) + "\n"
    head = "" if existing else f"# {now.strftime('%Y-%m-%d')} — journal\n"
    with io.open(jp, "a", encoding="utf-8", newline="\n") as f:
        f.write(head + block)
    print(f"appended {len(bullets)} bullet(s) → {os.path.relpath(jp, ROOT)}")

if __name__ == "__main__":
    main()
