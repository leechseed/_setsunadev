# -*- coding: utf-8 -*-
"""Build the plot sweep page (BOLO 77) from _meta/plot_sweep.json. Zero tokens.
Usage: python _tools/zotero/plot_sweep_page.py  -> _tools/zotero/out/plot-sweep.html"""
import io, json, os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
META = os.path.join(ROOT, "_0.1_BVX_LEARN", "_meta")
HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(io.open(os.path.join(META, "plot_sweep.json"), encoding="utf-8"))
rows = [{"l": k["lane"], "t": k["tier"], "h": 0 if k["src"] == "zlib-gap" else (2 if k["src"] == "drop" else 1),
         "b": k["bvx"], "n": k["clean"], "a": k["author"], "w": k["why"], "i": k["id"]} for k in d["keep"]]
data = {"rows": rows, "canon": d["canon"], "spec": d["specimens"]}
tpl = io.open(os.path.join(HERE, "plot_sweep_template.html"), encoding="utf-8").read()
os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
out = os.path.join(HERE, "out", "plot-sweep.html")
io.open(out, "w", encoding="utf-8").write(tpl.replace("/*DATA*/null", json.dumps(data, ensure_ascii=False)))
print(f"wrote {out} · {len(rows)} rows · {os.path.getsize(out) // 1024} KB")
