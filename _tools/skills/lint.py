#!/usr/bin/env python3
"""Zero-token linter for the Command's skills and agents (stdlib only).

Checks .claude/skills/*/SKILL.md and .claude/agents/*.md.
Output: one line per finding `path | check | detail`, then a summary line.
Exit 1 if any ERROR; warnings alone exit 0.

Usage: python _tools/skills/lint.py [repo_root]
"""
import re
import sys
import unicodedata
from pathlib import Path

# Frontmatter-rule structure adapted from anthropics/skills quick_validate.py (Apache-2.0).
# Checklist ideas from SkillCheck-Free (MIT, github.com/olgasafonova/SkillCheck-Free).

SKILL_KEYS = {
    "name", "description", "license", "allowed-tools", "metadata", "compatibility",
    "argument-hint", "disable-model-invocation", "user-invocable", "model",
    "effort", "context", "agent", "hooks", "paths", "shell", "when_to_use",
    "disallowed-tools",
}
AGENT_KEYS = {
    "name", "description", "tools", "disallowedTools", "model", "color",
    "permissionMode", "maxTurns", "skills", "mcpServers", "hooks", "memory",
    "effort", "background", "isolation", "initialPrompt",
}
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
VAGUE_NAMES = {"helper", "helpers", "utils", "util", "tools", "misc", "stuff", "thing", "tool", "data"}
RESERVED = ("anthropic", "claude")
AMBIGUOUS = re.compile(r"\b(several|appropriate|as needed|various|etc\.|and so on)\b", re.I)
DATE = re.compile(r"\b(?:in|as of|since|after|before)\s+(?:19|20)\d\d\b", re.I)
INVISIBLE = re.compile("[​‌‍⁠﻿‪-‮⁦-⁩\U000e0000-\U000e007f]")
UNPINNED = re.compile(r"\b(?:pip3?\s+install\s+(?!-r|-e|\.)[A-Za-z][\w.-]*(?![=<>~])(?:\s|$)|npx\s+[\w@/.-]+@latest)")
EXEC = re.compile(r"(\beval\(|\bexec\(|pickle\.loads|shell\s*=\s*True|curl[^\n|]*\|\s*(?:sh|bash))")
DESTRUCT = re.compile(r"(rm\s+-rf|git\s+push\s+--force|git\s+push\s+-f\b)")
SAFEOFF = re.compile(r"(--no-verify|--no-gpg-sign)")
UNCAPPED = re.compile(r"\b(retry until|loop until|repeat until)\b", re.I)
RULES_PHRASE = "Command rules"


def parse(text):
    """Return (fm dict, body, error). Flat `key: value` parser, handles folded/list continuation."""
    if not text.startswith("---"):
        return None, text, "no frontmatter (file must start with ---)"
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", text, re.S)
    if not m:
        return None, text, "frontmatter not closed with ---"
    fm, last = {}, None
    for ln in m.group(1).splitlines():
        if not ln.strip() or ln.lstrip().startswith("#"):
            continue
        km = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", ln)
        if km and not ln.startswith((" ", "\t")):
            last = km.group(1)
            v = km.group(2).strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                v = v[1:-1]
            fm[last] = v
        elif last is not None and ln.startswith((" ", "\t", "-")):
            fm[last] = (fm[last] + " " + ln.strip()).strip()
        else:
            return None, m.group(2), f"unparseable frontmatter line: {ln[:60]}"
    return fm, m.group(2), None


def lint_file(path, kind, expect_name, root, out):
    rel = path.relative_to(root).as_posix()

    def add(sev, check, detail):
        out.append((sev, rel, check, detail))

    text = path.read_text(encoding="utf-8", errors="replace")
    fm, body, err = parse(text)
    if err:
        add("ERROR", "frontmatter", err)
        return
    allowed = SKILL_KEYS if kind == "skill" else AGENT_KEYS
    for k in fm:
        if k not in allowed:
            add("ERROR", "allowed-keys", f"unexpected key '{k}'")
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not name:
        add("ERROR", "name", "missing")
    else:
        if not KEBAB.match(name):
            add("ERROR", "name-kebab", f"'{name}' is not kebab-case")
        if len(name) > 64:
            add("ERROR", "name-length", f"{len(name)} chars, max 64")
        if name != expect_name:
            add("ERROR", "name-match", f"name '{name}' != '{expect_name}'")
        if any(r in name for r in RESERVED):
            add("ERROR", "name-reserved", f"'{name}' contains a reserved word")
        if name in VAGUE_NAMES:
            add("WARN", "name-vague", f"'{name}' is generic")
        elif "-" not in name and len(name) < 6:
            add("WARN", "name-short", f"'{name}' is very short")
        if len(name) > 40:
            add("WARN", "name-long", f"{len(name)} chars")
        if "-" in name and name.split("-")[0].endswith("ing"):
            add("WARN", "name-gerund", f"'{name}' starts with a gerund")
    if not desc:
        add("ERROR", "description", "missing")
    else:
        if len(desc) > 1024:
            add("ERROR", "description-length", f"{len(desc)} chars, max 1,024")
        if "<" in desc or ">" in desc:
            add("ERROR", "description-brackets", "contains angle brackets")
        if len(desc) + len(fm.get("when_to_use", "")) > 1536:
            add("WARN", "listing-cap", "description + when_to_use over 1,536 chars")
        if len(desc) < 40:
            add("WARN", "description-weak", f"only {len(desc)} chars; say what and when")
        if kind == "skill" and not re.search(r"\b(fires|use when|use this|triggers?|when)\b", desc, re.I):
            add("WARN", "description-trigger", "no trigger phrase (Fires on / Use when)")
        if re.search(r"\b(step 1|first,? .{0,40}then|1\))", desc, re.I):
            add("WARN", "description-workflow", "description summarizes workflow steps")
    if "<" in "".join(v for k, v in fm.items() if k != "description") and "<" in text.split("---")[1]:
        add("WARN", "frontmatter-brackets", "angle brackets in frontmatter")
    for k in ("background", "user-invocable", "disable-model-invocation"):
        if k in fm and fm[k].lower() not in ("true", "false", "yes", "no", "on", "off", "1", "0"):
            add("ERROR", "bool-value", f"{k}: '{fm[k]}' is not a boolean")
    if "background" in fm and fm.get("context") != "fork" and kind == "skill":
        add("WARN", "background-no-fork", "background set without context: fork")
    if "effort" in fm and fm["effort"] not in ("low", "medium", "high", "xhigh", "max"):
        add("ERROR", "effort-invalid", f"'{fm['effort']}'")
    if kind == "skill" and "maxTurns" in fm:
        add("WARN", "maxturns-skill", "maxTurns is an agent field")
    if "$ARGUMENTS" in body and "argument-hint" not in fm:
        add("WARN", "arg-hint", "$ARGUMENTS used but no argument-hint")
    if kind == "skill" and re.search(r"allowed-tools:\s*(\*|all)\s*$", text, re.M | re.I):
        add("ERROR", "tools-wildcard", "allowed-tools is * or all")

    words = len(body.split())
    lines = len(text.splitlines())
    if words > 1500:
        add("WARN", "bloat", f"{words} words (line is 1,500)")
    if lines > 500:
        add("WARN", "lines", f"{lines} lines (line is 500)")
    if not body.strip():
        add("ERROR", "body-empty", "no body")
    nofence = re.sub(r"```.*?```", "", body, flags=re.S)
    for m in re.finditer(r"^#{1,6} .+\n(?=\s*(?:#{1,6} |\Z))", nofence, re.M):
        add("WARN", "empty-section", f"heading '{m.group(0).strip()[:40]}' has no content")
    if DATE.search(body):
        add("WARN", "stale-date", f"hardcoded year phrase: '{DATE.search(body).group(0)}'")
    if AMBIGUOUS.search(body):
        add("WARN", "ambiguous-term", f"vague term '{AMBIGUOUS.search(body).group(0)}'")
    if INVISIBLE.search(text):
        add("ERROR", "invisible-chars", "zero-width / bidi / tag characters present")
    if UNPINNED.search(text):
        add("WARN", "unpinned-install", "unpinned dependency install")
    if EXEC.search(text):
        add("WARN", "code-exec", f"'{EXEC.search(text).group(0)}' (eval/exec/shell=True/curl|sh)")
    if DESTRUCT.search(text) and not re.search(r"confirm|ask|never|do not|don't", text, re.I):
        add("WARN", "destructive-no-gate", "destructive command with no confirmation language")
    if SAFEOFF.search(text):
        add("WARN", "safeguard-off", f"'{SAFEOFF.search(text).group(0)}' disables a safeguard")
    if UNCAPPED.search(body):
        add("WARN", "uncapped-loop", f"'{UNCAPPED.search(body).group(0)}' with no cap")

    if kind == "skill":
        if (path.parent / "README.md").exists():
            add("WARN", "readme-in-skill", "README.md inside skill folder")
        for bak in path.parent.glob("*.bak"):
            add("WARN", "stray-bak", bak.name)
    else:
        tools = fm.get("tools", "")
        if "tools" not in fm or not tools.strip():
            add("ERROR", "tools-line", "agent has no tools line")
        else:
            if tools.strip() in ("*", "all"):
                add("ERROR", "tools-wildcard", "tools is *")
            if len([t for t in tools.split(",") if t.strip()]) >= 6 and "Bash" in tools:
                add("WARN", "tools-broad", "6+ tools including Bash; confirm it is needed")
            if "Agent" in tools or "Task" in tools:
                add("ERROR", "tools-agent", "agents must not launch agents")
        if RULES_PHRASE not in text:
            add("ERROR", "command-rules", "Command rules block missing")
        if "model" not in fm:
            add("WARN", "model", "no model line")


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]
    out, n = [], 0
    for f in sorted((root / ".claude" / "skills").glob("*/SKILL.md")):
        n += 1
        lint_file(f, "skill", f.parent.name, root, out)
    for f in sorted((root / ".claude" / "agents").glob("*.md")):
        if f.name.lower() == "readme.md":
            continue
        n += 1
        lint_file(f, "agent", f.stem, root, out)
    for d in (root / ".claude" / "skills", root / ".claude" / "agents"):
        for bak in d.rglob("*.bak"):
            if not any(o[1] == bak.relative_to(root).as_posix() for o in out):
                out.append(("WARN", bak.relative_to(root).as_posix(), "stray-bak", "backup file"))
    out.sort(key=lambda o: (o[0] != "ERROR", o[1], o[2]))
    for sev, rel, check, detail in out:
        print(f"{rel} · {sev.lower()}:{check} · {detail}")
    e = sum(1 for o in out if o[0] == "ERROR")
    w = len(out) - e
    print(f"SUMMARY · {n} files · {e} errors · {w} warnings")
    sys.exit(1 if e else 0)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()

# adapted from anthropics/skills skill-creator (Apache-2.0) + SkillCheck-Free (MIT) · BOLO 140 · 2026-10-12
