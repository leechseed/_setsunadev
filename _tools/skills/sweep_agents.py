"""Agent sweep (BOLO 140): add a 'Use when' clause and a hand-back block to every .claude/agents/*.md.
Dry run by default; --apply writes. Never touches the Command rules block."""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
WRITERS = {"doc-updater","refactor-cleaner","opensource-forker","opensource-packager","skill-builder","collect-lead"}
MARK = "## Hand-back (SOP §1.24)"

def use_when(desc):
    first = re.split(r"(?<=[.])\s", desc.strip(), 1)[0].rstrip(".")
    return "Use when the CDR needs this: " + first[:1].lower() + first[1:] + "."

def block(name):
    cap = 25 if name in WRITERS else 15
    return (f"{MARK}\n\n- Turn cap: {cap} turns.\n"
            "- Hand back: one line restating the task · the paths touched · one report under 250 words · then stop.\n"
            "- Mark every claim without a source as guessed.\n")

def main():
    apply = "--apply" in sys.argv
    for p in sorted((ROOT/".claude/agents").glob("*.md")):
        if p.name == "README.md": continue
        t = p.read_text(encoding="utf-8"); orig = t; plan = []
        m = re.search(r"^description:[ \t]*(.*)$", t, re.M)
        if m and not re.search(r"use when", m.group(1), re.I):
            t = t[:m.end()] + " " + use_when(m.group(1)) + t[m.end():]; plan.append("description+Use when")
        if MARK not in t:
            lines = t.rstrip("\n").split("\n")
            i = len(lines)
            if lines and lines[-1].startswith("<!--"):
                i = len(lines) - 1
                while i > 0 and lines[i-1] == "": i -= 1
            lines[i:i] = ["", *block(p.stem).rstrip("\n").split("\n"), ""] if i < len(lines) else ["", *block(p.stem).rstrip("\n").split("\n")]
            t = "\n".join(lines).rstrip("\n") + "\n"; plan.append("hand-back")
        print(f"{p.name}: {', '.join(plan) or 'ok'}")
        if apply and t != orig: p.write_text(t, encoding="utf-8", newline="\n")
if __name__ == "__main__": main()
