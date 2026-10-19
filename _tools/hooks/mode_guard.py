# -*- coding: utf-8 -*-
"""The mode guard: a PreToolUse hook (BOLO 159, ruled 10/19 call 1 = B). In research and design mode it blocks
install-shaped shell commands (pip, scoop, winget, choco, npm, go, cargo, pipx installs). Build mode lets them run.
Switch with: python _tools/modes/mode.py build.  Exit 2 blocks the call and hands the reason back to Claude;
anything else lets it run. A bad or missing modes.json never blocks. Each guard keeps one job (no_probe.py stays the probe guard)."""
import io, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
MODES = os.path.join(HERE, "..", "modes", "modes.json")

INSTALL = re.compile(
    r"^(?:sudo\s+)?(?:"
    r"(?:python[\d.]*|py)(?:\s+-\S+)*\s+-m\s+pip\s+install\b"
    r"|(?:pip[\d.]*|pipx|uv\s+pip|uv\s+tool|poetry|conda|mamba)\s+(?:install|add)\b"
    r"|(?:scoop|winget|choco|brew|apt(?:-get)?)\s+install\b"
    r"|(?:npm|pnpm|yarn)\s+(?:install|i|add)\b"
    r"|(?:go|cargo)\s+install\b"
    r")", re.I)


def install_segments(cmd):
    """The segments of a compound command that start with an install command."""
    out = []
    for seg in re.split(r"&&|\|\||;|\||\n", cmd):
        seg = seg.strip().lstrip("(").strip()
        seg = re.sub(r"^(?:\$env:\w+\s*=\s*\S+\s*;?\s*|\w+=\S+\s+)+", "", seg)   # leading env assignments
        seg = re.sub(r"^&\s*", "", seg)                                           # PowerShell call operator
        seg = re.sub(r'^"?[^"\s]*[/\\](?:python|pip|scoop|winget)[\d.]*(?:\.exe)?"?', lambda m: os.path.basename(m.group(0).strip('"')).replace(".exe", ""), seg, flags=re.I)
        if INSTALL.match(seg):
            out.append(seg[:60])
    return out


def main():
    try:
        d = json.load(sys.stdin)
    except Exception:
        return 0
    if d.get("tool_name") not in ("Bash", "PowerShell"):
        return 0
    try:
        m = json.load(io.open(MODES, encoding="utf-8"))
        active = m["active"]
    except Exception:
        return 0
    if active == "build":
        return 0
    hits = install_segments((d.get("tool_input") or {}).get("command", "") or "")
    if hits:
        sys.stderr.write("MODE GUARD · %s mode does not install (BOLO 159). Blocked: %s. Chief's word switches it: say \"build mode\", then Claude runs python _tools/modes/mode.py build.\n" % (active.upper(), hits[0]))
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
