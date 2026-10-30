"""wire_editors.py — 10/30: append every newly distilled recommended book to its editor's Craft basis list.
Reads SEATS from build_editor_library.py. Adds a Craft basis section to editors that have none (line, production, cold).
Skips ids the agent file already names. Run: python -X utf8 _tools/pages/wire_editors.py
"""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
src = open(os.path.join(ROOT, "_tools", "pages", "build_editor_library.py"), encoding="utf8").read()
ns = {"__file__": os.path.join(ROOT, "_tools", "pages", "build_editor_library.py")}
exec(src.split("cards, need")[0], ns)
CAT, DONE, SEATS = ns["CAT"], ns["DONE"], ns["SEATS"]

INTRO = ("\n## Craft basis\n\nThe Command's distilled library lives in `_0.1_BVX_LEARN/KNOWLEDGE_AREAS/BVX.<id>.md`. "
         "Before you read the script, read only §3 (framework), §5 (heuristics) and §7 (pitfalls) of each entry below. "
         "Tag findings with the source, for example (BVX.0188). The books disagree with each other; when two of them split "
         "on a point, say so and let the page decide. A book rule is evidence, not a verdict. Entries marked draft rest on a partial read; weigh them lightly.\n\n")


def label(i, why):
    b = CAT["BVX." + i]
    t = re.split(r"[:(]", b["t"])[0].strip()[:70]
    a = (b.get("a") or "").split(",")[0].strip()
    return f"- BVX.{i} · {t} ({a}): {why}" if a else f"- BVX.{i} · {t}: {why}"


for seat, lens, wired, add in SEATS:
    path = os.path.join(ROOT, ".claude", "agents", seat + ".md")
    text = open(path, encoding="utf8").read()
    new = [label(i, w) for i, w in add if "BVX." + i in DONE and f"BVX.{i} " not in text]
    if not new:
        print(seat, "nothing to add")
        continue
    if "## Craft basis" not in text:
        text = text.rstrip("\n") + "\n" + INTRO + "\n".join(new) + "\n"
    else:
        lines = text.split("\n")
        start = next(n for n, l in enumerate(lines) if l.startswith("## Craft basis"))
        last = max(n for n, l in enumerate(lines) if n > start and l.startswith("- BVX."))
        lines[last + 1:last + 1] = new
        text = "\n".join(lines)
    open(path, "w", encoding="utf8").write(text)
    print(seat, "added", len(new))
