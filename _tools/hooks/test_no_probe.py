# -*- coding: utf-8 -*-
"""Cases for the shell-habits part of no_probe.py (BOLO 155, 10/31). Run: python -X utf8 _tools/hooks/test_no_probe.py
Each case pipes a hook payload into no_probe.py and checks the exit code (2 = blocked, 0 = allowed)."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
BS = chr(92)
CASES = [
    # (tool, command, expected exit)
    ("Bash", "python3 x.py", 2),
    ("Bash", "python -X utf8 x.py", 0),
    ("Bash", "Get-ChildItem .", 2),
    ("Bash", "ls -la /dev/null 2>$null || echo none", 2),
    ("Bash", "ls /nope 2>/dev/null || echo none", 0),
    ("Bash", 'ls -la "C:' + BS + 'Users' + BS + 'x' + BS + 'frag' + BS + '" | head', 2),
    ("Bash", 'ls -la "C:/Users/x/frag/" | head', 0),
    ("Bash", 'cat "C:' + BS + 'Users' + BS + 'x.txt"', 0),
    ("Bash", "python - <<'EOF'\nprint('a 2>$null')\nEOF", 0),
    ("Bash", "powershell -Command 'gci 2>$null'", 0),
    ("PowerShell", "ls 2>$null", 0),
    ("Bash", "git status", 0),
]
bad = 0
for tool, cmd, want in CASES:
    r = subprocess.run([sys.executable, os.path.join(HERE, "no_probe.py")], input=json.dumps({"tool_name": tool, "tool_input": {"command": cmd}}),
                       capture_output=True, text=True, encoding="utf-8")
    ok = r.returncode == want
    bad += not ok
    print(("PASS" if ok else "FAIL"), want, r.returncode, cmd.splitlines()[0][:60], ("" if ok else r.stderr[:120]))
print("ALL PASS" if not bad else "%d FAILED" % bad)
sys.exit(1 if bad else 0)
