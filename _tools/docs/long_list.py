"""List every sentence over 20 words in the core docs, per file (DOC-SOP 3.2). Usage: python _tools/docs/long_list.py <out.txt> <system folder>..."""
import io, os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(HERE, "..", "..", "ShroomsQ", "_CANON", "_DOCS")
out, systems = sys.argv[1], sys.argv[2:]
lines, total = [], 0
for s in systems:
    for dp, _, fns in sorted(os.walk(os.path.join(DOCS, s))):
        for f in sorted(fns):
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            body = re.sub(r"\A﻿?---\n.*?\n---\s*\n", "", io.open(p, encoding="utf-8").read(), flags=re.S)
            body = re.sub(r"```.*?```", "", body, flags=re.S)
            hits = []
            for line in body.splitlines():
                if line.startswith(("#", "|", ">")) or not line.strip():
                    continue
                bare = re.sub(r"\"[^\"]*\"|“[^”]*”", "Q", line)
                for sent in re.split(r"(?<=[.!?])\s+|\s·\s", bare):
                    if len(re.findall(r"[\w'’-]+", sent)) > 20:
                        hits.append(sent.strip())
            if hits:
                total += len(hits)
                lines.append(f"## {os.path.relpath(p, os.path.join(HERE, '..', '..')).replace(os.sep, '/')}")
                lines += [f"- {h}" for h in hits]
io.open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(f"{total} long sentence(s) → {out}")
