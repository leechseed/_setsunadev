# -*- coding: utf-8 -*-
"""UserPromptSubmit hook (BOLO 159): prints the active working mode's one line every turn.
Reads _tools/modes/modes.json. A bad or missing file prints a fallback line. Never blocks; exit 0 always."""
import io, json, os, sys
try:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "modes", "modes.json")
    try:
        d = json.load(io.open(path, encoding="utf-8"))
        m = d["modes"][d["active"]]
        print("MODE · %s since %s · may: %s · may not: %s · model: %s · rules: %s · ends: %s" % (
            d["active"].upper(), d["since"].split(" ")[-1], m["may"], m["may_not"], m["model"], m["rules"], m["ends"]))
    except Exception:
        print("MODE · unknown, treat as research")
    sys.stdout.flush()
except Exception:
    pass
sys.exit(0)
