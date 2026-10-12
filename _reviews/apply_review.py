"""apply_review.py <decisions.json> [original.md] : apply ACCEPTED edits to a COPY of the original (BOLO 125).
Never writes the original. Reads the reviewed .md beside this file for the edit pairs.
Output: <name>.edited.md (the copy) and <name>.accepted-notes.md (accepted comments that carry advice, not an exact edit)."""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from review_page import parse  # noqa: E402

dec = json.load(io.open(sys.argv[1], encoding="utf-8"))
name = dec["document"]
reviewed = io.open(os.path.join(HERE, name + ".reviewed.md"), encoding="utf-8").read()
orig_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(HERE), name + ".md")
text = io.open(orig_path, encoding="utf-8", newline="").read()  # newline="" keeps the original line endings
_, comments = parse(reviewed)
accepted = [d["id"] for d in dec["decisions"] if d["decision"] == "accept" and d["id"] in comments]
applied, notes, missed = [], [], []
for i in accepted:
    c = comments[i]
    if c["old"]:
        if text.count(c["old"]) == 1:
            text = text.replace(c["old"], c["new"])
            applied.append(i)
        else:
            missed.append("%s (anchor found %d times)" % (i, text.count(c["old"])))
    else:
        notes.append(c)
out = os.path.join(HERE, name + ".edited.md")
assert os.path.abspath(out) != os.path.abspath(orig_path)
io.open(out, "w", encoding="utf-8", newline="\n").write(text)
if notes:
    io.open(os.path.join(HERE, name + ".accepted-notes.md"), "w", encoding="utf-8", newline="\n").write(
        "# Accepted comments to work by hand: %s\n\n" % name + "\n".join("- **%s** %s" % (c["id"], c["text"]) for c in notes) + "\n")
print("accepted", len(accepted), "- edits applied", applied or "none", "- advice notes", len(notes), "- anchor misses", missed or "none")
print("wrote", out, "(original untouched)")
