"""The ChatGPT export inventory: one row per conversation (BOLO 107, the intake; ruled "go" 10/14).

Usage:  python _tools/intake/gpt_inventory.py

Zero tokens. Reads the unpacked export (_PRIVATE/intake/chatgpt/export/conversations-*.json) and walks each
conversation's live branch (current_node back to the root), so edited-away branches are not counted twice.
Per conversation it records: title · created · updated · model · turns (Chief / ChatGPT) · words (Chief / ChatGPT) ·
the longest single Chief message (a pasted book or doc, not Chief's writing) · lineage words (SOP §9 CLEAN) ·
the top topic words from Chief's own turns · starred / archived.
The script judges nothing. Keep · skim · skip is the specialists' job, then Chief rules on the glass.

Outputs (git-ignored): _PRIVATE/intake/chatgpt/inventory.json · _PRIVATE/intake/chatgpt/inventory.md
"""
import glob
import json
import os
import re
import time
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BASE = os.path.join(ROOT, "_PRIVATE", "intake", "chatgpt")
EXPORT = os.path.join(BASE, "export")
LINEAGE = ["Inner Spiral", "Red Hills", "Skeeter Creek", "Red Stick Creek", "Ariel"]
PASTE_CHARS = 20_000   # one Chief message this long is a paste, not a question
WORD = re.compile(r"[a-z][a-z'-]{3,}")
STOP = set("""
that this with have from what your about would there their they them then than into just like make more some when
which will want need also only could should these those been were what's it's i'm don't can't does doing being other
each over very much many such here where while after before because really thing things please give know think
going still even want make sure well okay yeah good help write using used right first next last made take
""".split())


def text_of(msg):
    parts = (msg.get("content") or {}).get("parts") or []
    return " ".join(p for p in parts if isinstance(p, str)).strip()


def live_branch(conv):
    """The messages on the branch Chief last saw, root first."""
    mapping, out, node = conv.get("mapping") or {}, [], conv.get("current_node")
    while node and node in mapping:
        m = mapping[node].get("message")
        if m:
            out.append(m)
        node = mapping[node].get("parent")
    return out[::-1]


def day(ts):
    return time.strftime("%Y-%m-%d", time.localtime(ts)) if ts else ""


def row(conv):
    turns, words, longest, models, mine = Counter(), Counter(), 0, Counter(), []
    for m in live_branch(conv):
        role, t = (m.get("author") or {}).get("role"), text_of(m)
        if role not in ("user", "assistant") or not t:
            continue
        turns[role] += 1
        words[role] += len(t.split())
        if role == "user":
            longest = max(longest, len(t))
            if len(t) < PASTE_CHARS:   # topic words come from Chief's own turns, not his pastes
                mine.append(t)
        slug = (m.get("metadata") or {}).get("model_slug")
        if slug:
            models[slug] += 1
    blob = " ".join(mine)
    topics = Counter(w for w in WORD.findall(blob.lower()) if w not in STOP)
    return {
        "id": conv.get("conversation_id") or conv.get("id"),
        "title": (conv.get("title") or "").strip() or "(untitled)",
        "created": day(conv.get("create_time")),
        "updated": day(conv.get("update_time")),
        "model": (models.most_common(1)[0][0] if models else conv.get("default_model_slug")) or "",
        "turns_chief": turns["user"], "turns_gpt": turns["assistant"],
        "words_chief": words["user"], "words_gpt": words["assistant"],
        "longest_chief_chars": longest, "paste": longest >= PASTE_CHARS,
        "lineage": [w for w in LINEAGE if re.search(rf"\b{re.escape(w)}\b", blob, re.I)],
        "topics": [w for w, _ in topics.most_common(8)],
        "starred": bool(conv.get("is_starred")), "archived": bool(conv.get("is_archived")),
    }


def main():
    t0 = time.time()
    convs = []
    for f in sorted(glob.glob(os.path.join(EXPORT, "conversations-*.json"))):
        with open(f, encoding="utf-8") as fh:
            convs += json.load(fh)
    rows = sorted((row(c) for c in convs), key=lambda r: r["created"])
    empty = [r for r in rows if not r["turns_chief"]]
    per_month = Counter(r["created"][:7] for r in rows)
    words_chief, words_gpt = sum(r["words_chief"] for r in rows), sum(r["words_gpt"] for r in rows)
    summary = {
        "conversations": len(rows), "empty": len(empty), "pastes": sum(r["paste"] for r in rows),
        "lineage_hits": sum(bool(r["lineage"]) for r in rows), "starred": sum(r["starred"] for r in rows),
        "words_chief": words_chief, "words_gpt": words_gpt,
        "first": rows[0]["created"] if rows else "", "last": rows[-1]["created"] if rows else "",
        "per_month": dict(sorted(per_month.items())), "secs": round(time.time() - t0, 1),
    }
    with open(os.path.join(BASE, "inventory.json"), "w", encoding="utf-8") as fh:
        json.dump({"summary": summary, "rows": rows}, fh, ensure_ascii=False, indent=1)

    big = sorted(rows, key=lambda r: -(r["words_chief"] + r["words_gpt"]))[:25]
    md = [f"# ChatGPT export · inventory ({time.strftime('%Y-%m-%d')})", "",
          f"- **{summary['conversations']:,} conversations**, {summary['first']} to {summary['last']} · "
          f"{summary['empty']} with no Chief turn",
          f"- **Words:** Chief {words_chief:,} · ChatGPT {words_gpt:,}",
          f"- **Pastes** (a Chief message over {PASTE_CHARS:,} chars): {summary['pastes']} · "
          f"**lineage words:** {summary['lineage_hits']} · **starred:** {summary['starred']}", "",
          "## Per month", "", "| month | chats |", "|---|---|"]
    md += [f"| {m} | {n} |" for m, n in summary["per_month"].items()]
    md += ["", "## The 25 biggest", "", "| created | title | turns | words | topics |", "|---|---|---|---|---|"]
    md += [f"| {r['created']} | {r['title'].replace('|', '/')} | {r['turns_chief']} | "
           f"{r['words_chief'] + r['words_gpt']:,} | {' · '.join(r['topics'][:5])} |" for r in big]
    with open(os.path.join(BASE, "inventory.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md) + "\n")
    print(f"GPT INVENTORY · {summary['conversations']:,} chats · {summary['first']} to {summary['last']} · "
          f"Chief {words_chief:,} words · ChatGPT {words_gpt:,} · {summary['empty']} empty · {summary['pastes']} pastes · "
          f"{summary['lineage_hits']} lineage · {summary['secs']} s")


if __name__ == "__main__":
    main()
