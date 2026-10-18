"""BOLO 155 M4 (DVA's method, Chief 10/18 "take all recs"): sort the failed shell calls.
Reads the same transcripts as armory.py, pairs every failed Bash / PowerShell call with its command, and groups
the failures by what ran (the program, and the script for python) and by why it failed (the error's first telling line).

  python _tools/armory/bash_errors.py
Writes _PRIVATE/reference/armory/bash_errors.json (commands can hold private paths, so the output stays private).
Prints the top groups. Zero tokens.
"""
import glob, io, json, os, re, sys
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PROJECTS = os.path.join(os.path.expanduser("~"), ".claude", "projects")
OUT = os.path.join(ROOT, "_PRIVATE", "reference", "armory", "bash_errors.json")
SHELLS = {"Bash", "PowerShell"}

WHY = [   # first match wins; the label is what a fix would target
    ("guard: auto-mode classifier", r"auto mode classifier"),
    ("guard: no-probing hook", r"no-unasked-probing|no_probe"),
    ("blocked: sleep or chain rule", r"Blocked: sleep|Do not chain shorter sleeps"),
    ("Chief declined", r"doesn't want to proceed|user rejected|was rejected"),
    ("python: module missing", r"ModuleNotFoundError|No module named"),
    ("python: file missing", r"can't open file|No such file or directory: '"),
    ("python: syntax error", r"SyntaxError|unterminated string|IndentationError"),
    ("python: unicode on the console", r"UnicodeEncodeError|UnicodeDecodeError|charmap"),
    ("python: traceback (other)", r"Traceback \(most recent call last\)"),
    ("path missing", r"No such file or directory|cannot access|cannot find the path|does not exist"),
    ("command not found", r"command not found|is not recognized as"),
    ("PowerShell syntax in the wrong shell", r"ParserError|Unexpected token|positional parameter cannot be found|\$env:|Get-ChildItem"),
    ("timeout", r"timed out|Timeout|timeout"),
    ("git", r"^fatal:|not a git repository|nothing to commit"),
    ("grep found nothing (exit 1)", r"^Exit code 1\s*$"),
    ("other exit code", r"Exit code \d+"),
]


def why_of(text):
    """Judge the error by its tail, not its whole body: a failed grep or cat prints the file it read, and a word in
    that output (charmap, Traceback) is not the cause (10/18: the first sort counted output as errors)."""
    lines = [l for l in text.splitlines() if l.strip()]
    tail = "\n".join(lines[-6:])
    head = "\n".join(lines[:2])
    exc = re.findall(r"^(\w+(?:Error|Exception)):", tail, re.M)   # a Python traceback ends with its exception class
    if exc:
        name = exc[-1]
        if name in ("UnicodeEncodeError", "UnicodeDecodeError"):
            return "python: unicode on the console"
        if name in ("ModuleNotFoundError", "ImportError"):
            return "python: module missing"
        if name in ("SyntaxError", "IndentationError"):
            return "python: syntax error"
        if name == "FileNotFoundError":
            return "path missing"
        return "python: " + name
    for label, pat in WHY:
        if label.startswith("guard") or label.startswith("blocked") or label == "Chief declined":
            if re.search(pat, text, re.M):
                return label
        elif re.search(pat, tail, re.M):
            return label
    if re.match(r"^Exit code 1\s*$", head) and len(lines) <= 2:
        return "grep found nothing (exit 1)"
    return "exit code, cause not printed"


def what_of(cmd):
    """the program that ran, with the script name for python (cd prefixes and env assignments skipped)"""
    c = cmd.strip()
    c = re.sub(r"^(cd\s+(\"[^\"]*\"|\S+)\s*(&&|;)\s*)+", "", c)
    c = re.sub(r"^(\w+=\S+\s+)+", "", c)
    toks = c.split()
    if not toks:
        return "?"
    prog = os.path.basename(toks[0].strip("\"'")).lower()
    if prog.startswith("python") or prog == "py":
        script = next((t for t in toks[1:] if t.endswith(".py") or t == "-"), None)
        if t_inline := ("-c" in toks[1:3]):
            return "python -c (inline)"
        return "python " + (os.path.basename(script.strip("\"'")) if script else "(heredoc or module)")
    return prog


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass
    cmds, fails = {}, {}
    files = glob.glob(os.path.join(PROJECTS, "*", "*.jsonl")) + glob.glob(os.path.join(PROJECTS, "*", "*", "subagents", "*.jsonl"))
    for path in files:
        with io.open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if '"tool_use"' not in line and '"is_error":true' not in line:
                    continue
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                content = (rec.get("message") or {}).get("content")
                if not isinstance(content, list):
                    continue
                for c in content:
                    if not isinstance(c, dict):
                        continue
                    if c.get("type") == "tool_use" and c.get("name") in SHELLS:
                        cmds[c["id"]] = (c["name"], ((c.get("input") or {}).get("command") or "")[:400], (rec.get("timestamp") or "")[:10])
                    elif c.get("type") == "tool_result" and c.get("is_error"):
                        body = c.get("content")
                        fails[c.get("tool_use_id")] = body if isinstance(body, str) else json.dumps(body)[:1500]
    rows = []
    for tid, err in fails.items():
        if tid not in cmds:
            continue
        shell, cmd, day = cmds[tid]
        rows.append({"shell": shell, "what": what_of(cmd), "why": why_of(err), "day": day,
                     "cmd": cmd[:160], "err": " ".join(err.split())[:200]})
    by_why = Counter(r["why"] for r in rows)
    by_what = Counter(r["what"] for r in rows)
    pairs = Counter((r["why"], r["what"]) for r in rows)
    samples = defaultdict(list)
    for r in rows:
        if len(samples[r["why"]]) < 3:
            samples[r["why"]].append({"cmd": r["cmd"], "err": r["err"]})
    total = sum(1 for v in cmds.values())
    out = {"shell_calls": total, "failed": len(rows), "by_why": by_why.most_common(), "by_what": by_what.most_common(25),
           "pairs": [[w, p, n] for (w, p), n in pairs.most_common(30)], "samples": samples}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(out, io.open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"SHELL ERRORS · {len(rows):,} failed of {total:,} shell calls ({len(rows) / max(total, 1):.1%})")
    print("  why:")
    for w, n in by_why.most_common(16):
        print(f"    {n:>5}  {w}")
    print("  what:")
    for w, n in by_what.most_common(12):
        print(f"    {n:>5}  {w}")
    print("  wrote", OUT)


if __name__ == "__main__":
    main()
