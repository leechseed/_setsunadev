# -*- coding: utf-8 -*-
"""The no-probing guard — a PreToolUse hook (BOLO 64 fix, 9/23; the rule is memory `no-unasked-probing`, ruled 9/19).
Blocks scan-shaped shell commands (processes · services · network · event logs · registry · system info) unless Chief
named the box in the order. Naming the box = touch the marker, good for 60 minutes:
    python _tools/hooks/no_probe.py --box-named
Exit 2 blocks the call and hands the reason back to Claude; anything else lets it run. Never touches non-shell tools."""
import io, json, os, re, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
MARK = os.path.join(HERE, ".box-named")
if "--box-named" in sys.argv:
    io.open(MARK, "w").write(time.strftime("%Y-%m-%d %H:%M")); print("box named · guard open 60 min"); sys.exit(0)
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
if d.get("tool_name") not in ("Bash", "PowerShell"):
    sys.exit(0)
cmd = (d.get("tool_input") or {}).get("command", "") or ""
PAT = re.compile(r"(?i)(?<![\w-])(get-process|tasklist|get-service|sc\s+query|netstat|get-nettcpconnection|get-netadapter|get-netipconfiguration|ipconfig|arp\s+-a|nmap|get-winevent|get-eventlog|wevtutil|get-computerinfo|systeminfo|wmic|get-ciminstance|get-wmiobject|reg\s+query|get-itemproperty\s+['\"]?hk|schtasks|get-scheduledtask|netsh|whoami\s+/all|ps\s+(aux|-ef)|ss\s+-[a-z]*t|lsof\s+-i|dmesg|journalctl|get-hotfix|driverquery|pnputil|get-pnpdevice|nvidia-smi)(?![\w-])")
m = PAT.search(cmd)
if not m:
    sys.exit(0)
if os.path.exists(MARK) and time.time() - os.path.getmtime(MARK) < 3600:
    sys.exit(0)
sys.stderr.write("no-unasked-probing (ruled 9/19): '%s' scans the box and Chief's order did not name it. Read from what he handed over; if he did name the box, run `python _tools/hooks/no_probe.py --box-named` first.\n" % m.group(1))
sys.exit(2)
