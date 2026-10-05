"""Quote front-matter values that break YAML (a value holding ': ' etc.). Usage: python _tools/docs/fix_front.py <dir>..."""
import io, json, os, re, sys
import yaml
n = 0
for root in sys.argv[1:]:
    for dp, _, fns in os.walk(root):
        for f in fns:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            t = io.open(p, encoding="utf-8").read()
            m = re.match(r"\A(﻿?---\n)(.*?)(\n---\s*\n)", t, re.S)
            if not m:
                continue
            try:
                if isinstance(yaml.safe_load(m.group(2)), dict):
                    continue
            except yaml.YAMLError:
                pass
            lines = []
            for line in m.group(2).split("\n"):
                k = re.match(r"^(\w+):\s(.*)$", line)
                if k and not k.group(2).startswith(('"', "'")):
                    line = f"{k.group(1)}: {json.dumps(k.group(2), ensure_ascii=False)}"
                lines.append(line)
            io.open(p, "w", encoding="utf-8").write(m.group(1) + "\n".join(lines) + m.group(3) + t[m.end():])
            n += 1
print(f"fixed {n} file(s)")
