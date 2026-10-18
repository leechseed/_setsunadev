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
REPO = HERE.replace("\\", "/").lower().rsplit("/_tools/", 1)[0]
PROT = ("_private", "_tools", ".claude")


def _tokens(seg):
    return [t.strip("\"'") for t in re.split(r"\s+", seg.strip()) if t.strip("\"'")]


def _safe(path):
    return "appdata/local/temp/claude" in path or re.search(r"(^|/)_tools/[^/]+/out(/|$)", path) is not None


def _bad_target(t):
    p = re.sub(r"/+", "/", t.replace("\\", "/").lower())
    if _safe(p):
        return False
    p = re.sub(r"(/\*?|/\.)+$", "", p) or "/"
    if p in (".", "/", "~", "*", "$home", "$env:userprofile", "%userprofile%", REPO) or re.match(r"^[a-z]:$", p):
        return True
    if p.startswith(REPO + "/"):
        p = p[len(REPO) + 1:]
    return p in PROT


def destructive(cmd):
    """Return the reason a command is destructive, or None. Scratchpad and _tools/*/out/ are exempt."""
    for seg in re.split(r"[;|\n]|&&|\|\|", cmd):
        low = seg.strip().lower()
        if not low:
            continue
        toks = _tokens(low)
        if re.search(r"\bgit\s+(?:-\S+\s+)*reset\b.*--hard", low):
            return "git reset --hard"
        if re.search(r"\bgit\s+push\b", low) and re.search(r"(?<!\S)(--force(?:-with-lease)?(?:=\S+)?|-[a-z]*f[a-z]*)(?!\S)", low):
            i = toks.index("push")
            pos = [t for t in toks[i + 1:] if not t.startswith("-")]
            if not (len(pos) >= 2 and not re.search(r"(^|:)(main|master|head)$", pos[1])):
                return "git push --force to main"
        if re.search(r"\bgit\s+clean\b", low) and any(re.fullmatch(r"-[a-z]*", t) and "f" in t and "d" in t for t in toks):
            return "git clean -fd"
        if re.search(r"\bgit\s+checkout\s+(--\s+)?\.(\s|$)", low):
            return "git checkout -- ."
        if re.search(r"\bgit\s+branch\b.*\s-D(\s|$)", seg):
            return "git branch -D"
        if toks and toks[0] in ("del", "erase") and "/s" in toks and "/q" in toks:
            return "del /s /q"
        if re.match(r"(format|format-volume)(\s|$)", low):
            return "format"
        if re.match(r"(sudo\s+)?diskpart\b", low):
            return "diskpart"
        if toks and (toks[0] in ("rm", "remove-item", "ri", "rmdir", "rd") or toks[:2] == ["sudo", "rm"]):
            rec = any(re.fullmatch(r"-[a-z]*r[a-z]*", t) and not t.startswith("--") for t in toks[1:]) \
                or any(t == "--recursive" or t.startswith("-rec") for t in toks)
            if rec:
                for t in toks[1:]:
                    if not t.startswith("-") and _bad_target(t):
                        return "recursive delete of " + t
    return None


reason = destructive(cmd)
if reason:
    sys.stderr.write("destructive-command guard: '%s' blocked. It can erase work that git or the Command cannot restore. To override: Chief says 'override guard' and the CDR runs it by hand. (rm -rf inside the scratchpad or _tools/*/out/ is never blocked.)\n" % reason)
    sys.exit(2)


def habit(cmd, tool):
    """BOLO 155 M4 (10/18, memory `shell-habits`): the mechanical shell mistakes that failed 74+ calls, caught before
    they run. Returns the fix to hand back, or None. Bash only; checks each command segment's first word."""
    if tool != "Bash":
        return None
    for seg in re.split(r"[;\n]|&&|\|\||\|", cmd):
        toks = _tokens(seg)
        while toks and re.match(r"^\w+=\S*$", toks[0]):   # skip VAR=value prefixes
            toks = toks[1:]
        if not toks:
            continue
        first = os.path.basename(toks[0]).lower()
        if re.fullmatch(r"python3(\.\d+)?(\.exe)?", first):
            return "'python3' is not on this box; use 'python' (Python 3.11), with -X utf8 when output holds symbols"
        if re.fullmatch(r"(get|set|select|remove|new|write|test|start|stop)-[a-z]+", first):
            return "'%s' is a PowerShell cmdlet and the Bash tool runs Git Bash; use the Bash equivalent or the PowerShell tool" % toks[0]
    return None


fix = habit(cmd, d.get("tool_name"))
if fix:
    sys.stderr.write("shell-habits guard (BOLO 155 M4): %s.\n" % fix)
    sys.exit(2)
PAT = re.compile(r"(?i)(?<![\w-])(get-process|tasklist|get-service|sc\s+query|netstat|get-nettcpconnection|get-netadapter|get-netipconfiguration|ipconfig|arp\s+-a|nmap|get-winevent|get-eventlog|wevtutil|get-computerinfo|systeminfo|wmic|get-ciminstance|get-wmiobject|reg\s+query|get-itemproperty\s+['\"]?hk|schtasks|get-scheduledtask|netsh|whoami\s+/all|ps\s+(aux|-ef)|ss\s+-[a-z]*t|lsof\s+-i|dmesg|journalctl|get-hotfix|driverquery|pnputil|get-pnpdevice|nvidia-smi)(?![\w-])")
m = PAT.search(cmd)
if not m:
    sys.exit(0)
if os.path.exists(MARK) and time.time() - os.path.getmtime(MARK) < 3600:
    sys.exit(0)
sys.stderr.write("no-unasked-probing (ruled 9/19): '%s' scans the box and Chief's order did not name it. Read from what he handed over; if he did name the box, run `python _tools/hooks/no_probe.py --box-named` first.\n" % m.group(1))
sys.exit(2)
