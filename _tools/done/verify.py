# -*- coding: utf-8 -*-
"""The done check (BOLO 155 move 3; superpowers' verification-before-completion, adapted: a script, never a checker agent).
Run it before saying a build is done. It checks what changed since the last commit (or everything with --all):

  *.py                         compiles
  *.json / *.jsonl             parses
  .claude/agents/*.md          frontmatter has name, description, model; the name matches the file
  .claude/skills/*/SKILL.md    frontmatter has name and description; description is 500 characters or fewer;
                               every quoted trigger in the last committed description is still there
  BOLO.md                      no BOLO number appears on two rows

  python _tools/done/verify.py           the changed files
  python _tools/done/verify.py --all     every file it knows how to check
Exit 0 = PASS, 1 = FAIL. Prints one line per finding, then the verdict.
"""
import glob, io, json, os, py_compile, re, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SKIP = ("node_modules", ".git", "_PRIVATE", "__pycache__")


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace").stdout


def changed():
    names = set(git("diff", "--name-only", "HEAD").split()) | set(git("ls-files", "--others", "--exclude-standard").split())
    return sorted(n for n in names if os.path.exists(os.path.join(ROOT, n)))


def everything():
    out = []
    for pat in ("_tools/**/*.py", "_tools/**/*.json", ".claude/agents/*.md", ".claude/skills/*/SKILL.md", "BOLO.md"):
        out += [os.path.relpath(p, ROOT).replace("\\", "/") for p in glob.glob(os.path.join(ROOT, pat), recursive=True)]
    return sorted(n for n in set(out) if not any(s in n for s in SKIP))


def frontmatter(text):
    m = re.match(r"---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        if k.strip() and _:
            fm[k.strip()] = v.strip()
    return fm


def strict(text):
    """The frontmatter as real YAML (what a strict parser sees), or None when it does not parse."""
    m = re.match(r"---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return None
    try:
        import yaml
        d = yaml.safe_load(m.group(1))
    except Exception:
        return None
    return {k: str(v) for k, v in d.items()} if isinstance(d, dict) else None


def quoted(s):
    return set(re.findall(r'"([^"]{2,60})"', s or ""))


def check(name):
    p = os.path.join(ROOT, name)
    out = []
    if name.endswith(".py"):
        try:
            py_compile.compile(p, doraise=True)
        except py_compile.PyCompileError as e:
            out.append(f"{name}: does not compile: {str(e).splitlines()[-1][:120]}")
    elif name.endswith(".json"):
        try:
            json.load(io.open(p, encoding="utf-8"))
        except (ValueError, OSError) as e:
            out.append(f"{name}: bad JSON: {e}")
    elif name.endswith(".jsonl"):
        for i, line in enumerate(io.open(p, encoding="utf-8"), 1):
            if line.strip():
                try:
                    json.loads(line)
                except ValueError:
                    out.append(f"{name}:{i}: bad JSON line")
                    break
    elif re.match(r"\.claude/agents/[^/]+\.md$", name) and not name.endswith("README.md"):
        fm = frontmatter(io.open(p, encoding="utf-8").read())
        if fm is None:
            out.append(f"{name}: no frontmatter")
        else:
            for k in ("name", "description", "model"):
                if not fm.get(k):
                    out.append(f"{name}: frontmatter has no {k}")
            if fm.get("name") and fm["name"] != os.path.basename(name)[:-3]:
                out.append(f"{name}: name '{fm['name']}' does not match the file name")
    elif re.match(r"\.claude/skills/[^/]+/SKILL\.md$", name):
        text = io.open(p, encoding="utf-8").read()
        fm = strict(text)
        if fm is None and frontmatter(text) is not None:
            # 10/17: an unquoted ': ' inside a description broke two skills in Claude Code's listing; quote the value
            out.append(f"{name}: frontmatter is not valid YAML (quote the description in single quotes)")
            fm = frontmatter(text)
        if fm is None:
            out.append(f"{name}: no frontmatter")
        else:
            for k in ("name", "description"):
                if not fm.get(k):
                    out.append(f"{name}: frontmatter has no {k}")
            d = fm.get("description", "")
            if len(d) > 500:
                out.append(f"{name}: description is {len(d)} characters (500 max, superpowers convention)")
            head = git("show", f"HEAD:{name}") or ""
            old = strict(head) or frontmatter(head) or {}
            lost = sorted(quoted(old.get("description")) - quoted(d))
            if lost:
                out.append(f"{name}: description lost triggers: " + " · ".join(f'"{t}"' for t in lost))
    elif name == "BOLO.md":
        nums = re.findall(r"^\| (\d+) \|", io.open(p, encoding="utf-8").read(), re.M)
        dup = sorted({n for n in nums if nums.count(n) > 1}, key=int)
        if dup:
            out.append(f"BOLO.md: BOLO numbers on two rows: {', '.join(dup)}")
    return out


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass
    files = everything() if "--all" in sys.argv else changed()
    files = [f for f in files if not any(s in f for s in SKIP)]
    findings = [x for f in files for x in check(f)]
    for x in findings:
        print("  FAIL  " + x)
    print(f"DONE CHECK · {len(files)} file(s) · " + ("PASS" if not findings else f"FAIL ({len(findings)})"))
    sys.exit(1 if findings else 0)


if __name__ == "__main__":
    main()
