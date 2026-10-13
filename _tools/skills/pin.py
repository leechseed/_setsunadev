"""pin.py - hash the harness files so a silent change shows up.
  python _tools/skills/pin.py --pin     rewrite _tools/skills/pins.json
  python _tools/skills/pin.py --check   print added / changed / removed; exit 1 on any
"""
import hashlib, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PINS = Path(__file__).with_name("pins.json")


def files():
    out = set(ROOT.glob(".claude/skills/**/SKILL.md")) | set(ROOT.glob(".claude/agents/*.md"))
    for n in (".claude/settings.local.json", ".mcp.json", "CLAUDE.md"):
        if (ROOT / n).is_file():
            out.add(ROOT / n)
    return sorted(out)


def current():
    return {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in files()}


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else "--check"
    now = current()
    if arg == "--pin":
        PINS.write_text(json.dumps(now, indent=1, sort_keys=True), encoding="utf-8")
        print(f"pinned {len(now)} files -> {PINS.relative_to(ROOT).as_posix()}")
        return 0
    if arg != "--check":
        print("usage: pin.py --pin | --check")
        return 2
    old = json.loads(PINS.read_text(encoding="utf-8")) if PINS.is_file() else {}
    added = sorted(set(now) - set(old))
    removed = sorted(set(old) - set(now))
    changed = sorted(k for k in now if k in old and now[k] != old[k])
    for tag, lst in (("added", added), ("changed", changed), ("removed", removed)):
        for k in lst:
            print(f"{tag}: {k}")
    if not (added or changed or removed):
        print(f"clean: {len(now)} files match the pins")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
