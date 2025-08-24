import json, math
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ---- Load your mapping (paste the JSON to this path) ----
data = json.loads(Path("astro7ex_chapter_map.json").read_text(encoding="utf-8"))

# ---- Flatten to a DataFrame ----
rows = []
for ch in data["chapters"]:
    b = ch["ncp_storybeat"]
    d = ch.get("dramatica") or {}
    rows.append({
        "chapter": ch["chapter_index"],
        "title": ch["titles"]["tablature"],
        "anime_case": ch["titles"]["anime"]["case"],
        "anime_title": ch["titles"]["anime"]["tablature"],
        "appreciation": b["appreciation"],          # event | progression | transit
        "sequence": b["sequence"],                   # 1..64 (events) or frame seq
        "method": b["method"],
        "throughline": d.get("throughline"),         # OS/MC/IC/RS or None
        "signpost": d.get("signpost"),               # 1..4 or None
        "event_in_sp": d.get("event"),               # 1..4 or None
    })
df = pd.DataFrame(rows)

# ---- Quick filterable inspector ----
# (If you’re in Jupyter/VSCode, this gives you a sortable table.)
try:
    from IPython.display import display
    display(df)
except:
    print(df.head(12))

# ---- Swimlane Weave Board ----
plt.figure(figsize=(18, 5))
lanes = ["OS","MC","IC","RS","FRAME"]
y_map = {"OS":4,"MC":3,"IC":2,"RS":1,"FRAME":0}

# Events (OS/MC/IC/RS)
for tl in ["OS","MC","IC","RS"]:
    sub = df[(df["appreciation"]=="event") & (df["throughline"]==tl)]
    plt.scatter(sub["chapter"], [y_map[tl]]*len(sub),
                s=60, label=tl)

# Frames (progression/transit) in FRAME lane
frame = df[df["appreciation"]!="event"]
plt.scatter(frame["chapter"], [y_map["FRAME"]]*len(frame),
            marker="s", s=80, label="frame (progression/transit)")

# Signpost bands at event index boundaries (1,17,33,49 mapped back to chapters)
# We approximate by shading chapter ranges: you placed 8 reserved frames,
# but bands still give good act boundaries for visual reading.
for x in [1, 17, 33, 49]:
    plt.axvline(x=x, linestyle="--", linewidth=1)

plt.yticks([y_map[k] for k in lanes], lanes)
plt.xticks(range(1,73,2))
plt.xlim(1,72)
plt.title("ASTRO7EX — Throughline Weave across 72 Chapters")
plt.xlabel("Chapter")
plt.tight_layout()
plt.savefig("weave_board.png", dpi=180)
print("Saved weave_board.png")

# ---- Optional: balance by act/throughline ----
pivot = (df[df["appreciation"]=="event"]
         .assign(act=lambda x: ((x["sequence"]-1)//16)+1)
         .pivot_table(index="act", columns="throughline", values="chapter", aggfunc="count")
         .fillna(0).astype(int))
print("\nEvent balance (counts) by Act × Throughline:\n")
print(pivot)
