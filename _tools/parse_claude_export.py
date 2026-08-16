"""
Parse the Anthropic data export into the _setsunadev monorepo.

Lands the export faithfully. Invents no methodology, imposes no new system.
  conversations/  one markdown file per chat, YAML frontmatter
  artifacts/      the 18 recovered markdown artifacts, standalone
  files/          payloads from create_file tool calls
  projects/       project instructions + knowledge docs
  _PRIVATE/       PII-bearing material (gitignored)
  INDEX.md        master index
"""
import json, os, re, collections, datetime

SRC = r"E:\CLAUDE ANTHROPIC PULL 8.15.2026\data-b406e233-5484-43ec-aab8-36503838f194-1786754363-09425adc-batch-0000"
REPO = r"c:\Users\U01_LEECHSEED\Desktop\_setsunadev"
OUT = os.path.join(REPO, "_CLAUDE_ARCHIVE_2026-08-15")
PRIV = os.path.join(REPO, "_PRIVATE")

ORANGE = {
    "sex", "sexual", "kink", "dildo", "goon", "gooning", "nsfw", "lewd", "adult",
    "desire", "erotic", "fetish", "porn", "onlyfans", "bareback", "bbc", "dom",
    "submissive", "daddy", "chastity", "anal", "cock", "dick", "orgasm", "arousal",
    "m4mm", "hookup", "grindr", "escort", "camming", "toy review", "sex toy",
    "intimacy", "seduction", "libido", "masturbat", "d/s", "bdsm", "somatic sex",
}
BLACK = {
    "narrative", "character", "dramatica", "worldbuilding", "story", "plot",
    "astrology", "astro7ex", "overexitout", "lakad", "outliers", "outsiders",
    "bold venture", "bvx", "leechseed", "ssot", "sourcebook", "ip ", "canon",
    "series bible", "screenplay", "scene", "arc", "theme", "protagonist",
    "quinn", "victoria", "midnight", "tori", "red hills", "inner spiral",
    "shroomsq", "logline", "act structure", "mythos", "lore",
}

def slug(s, n=58):
    s = re.sub(r"[^\w\s-]", "", (s or "untitled"), flags=re.U)
    s = re.sub(r"[\s_]+", "-", s).strip("-").lower()
    return (s[:n] or "untitled")

def jload(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)

def classify(text):
    t = text.lower()
    o = sum(t.count(k) for k in ORANGE)
    b = sum(t.count(k) for k in BLACK)
    if o == 0 and b == 0:
        return "OTHER", 0, 0
    if o > b * 1.4:
        return "ORANGE", b, o
    if b > o * 1.4:
        return "BLACK", b, o
    return "BOTH", b, o

def yamlq(s):
    return '"' + str(s or "").replace('\\', '\\\\').replace('"', '\\"').replace("\n", " ") + '"'

for d in (OUT, PRIV):
    os.makedirs(d, exist_ok=True)
for d in ("conversations", "artifacts", "files", "projects"):
    os.makedirs(os.path.join(OUT, d), exist_ok=True)

convs = jload(os.path.join(SRC, "conversations.json"))
rows, art_n, file_n, used = [], 0, 0, collections.Counter()

for c in convs:
    title = c.get("name") or "(untitled)"
    created = (c.get("created_at") or "")[:10] or "0000-00-00"
    msgs = c.get("chat_messages", [])

    parts, artifacts_here, files_here, tools = [], [], [], collections.Counter()
    for m in msgs:
        sender = m.get("sender", "?")
        blocks = m.get("content") if isinstance(m.get("content"), list) else []
        text = m.get("text") or ""
        if not text and blocks:
            text = "".join(b.get("text", "") for b in blocks
                           if isinstance(b, dict) and b.get("type") == "text")

        for b in blocks:
            if not isinstance(b, dict) or b.get("type") != "tool_use":
                continue
            nm = b.get("name") or "?"
            tools[nm] += 1
            inp = b.get("input") or {}
            if nm == "artifacts" and inp.get("content"):
                artifacts_here.append((inp.get("title") or "untitled",
                                       str(inp.get("content"))))
            elif nm == "create_file":
                body = inp.get("content") or inp.get("file_text") or inp.get("text")
                path = inp.get("path") or inp.get("filename") or inp.get("file_path")
                if body and len(str(body)) > 200:
                    files_here.append((path or "untitled", str(body)))

        if text.strip():
            who = "## 🧑 Papi" if sender == "human" else "## 🤖 Claude"
            ts = (m.get("created_at") or "")[:19].replace("T", " ")
            parts.append(f"{who}  <sub>{ts}</sub>\n\n{text.strip()}")

    body = "\n\n---\n\n".join(parts)
    trunk, bs, os_ = classify(title + " " + body[:60000])

    base = f"{created}_{slug(title)}"
    used[base] += 1
    if used[base] > 1:
        base = f"{base}-{used[base]}"

    # artifacts -> standalone files, linked from the conversation
    art_links = []
    for i, (atitle, content) in enumerate(artifacts_here, 1):
        an = f"{created}_{slug(atitle)}.md"
        used[an] += 1
        if used[an] > 1:
            an = an[:-3] + f"-{used[an]}.md"
        with open(os.path.join(OUT, "artifacts", an), "w", encoding="utf-8") as f:
            f.write(f"---\ntitle: {yamlq(atitle)}\nsource_conversation: "
                    f"{yamlq(title)}\ncreated: {created}\ntrunk: {trunk}\n"
                    f"kind: artifact\n---\n\n{content}")
        art_links.append(f"- [{atitle}](../artifacts/{an})")
        art_n += 1

    file_links = []
    for fpath, content in files_here:
        fn = f"{created}_{slug(os.path.basename(str(fpath)))}.md"
        used[fn] += 1
        if used[fn] > 1:
            fn = fn[:-3] + f"-{used[fn]}.md"
        with open(os.path.join(OUT, "files", fn), "w", encoding="utf-8") as f:
            f.write(f"---\noriginal_path: {yamlq(fpath)}\nsource_conversation: "
                    f"{yamlq(title)}\ncreated: {created}\ntrunk: {trunk}\n"
                    f"kind: generated-file\n---\n\n{content}")
        file_links.append(f"- [{os.path.basename(str(fpath))}](../files/{fn})")
        file_n += 1

    fm = [
        "---",
        f"title: {yamlq(title)}",
        f"uuid: {c.get('uuid')}",
        f"created: {created}",
        f"updated: {(c.get('updated_at') or '')[:10]}",
        f"trunk: {trunk}",
        f"messages: {len(msgs)}",
        f"chars: {len(body)}",
        f"artifacts: {len(artifacts_here)}",
        f"generated_files: {len(files_here)}",
        f"tools: [{', '.join(sorted(tools))}]",
        "source: claude.ai-export-2026-08-15",
        "---",
        "",
        f"# {title}",
        "",
    ]
    if c.get("summary"):
        fm += [f"> {c['summary']}", ""]
    if art_links:
        fm += ["**Artifacts produced**", ""] + art_links + [""]
    if file_links:
        fm += ["**Files produced**", ""] + file_links + [""]
    fm += ["---", ""]

    with open(os.path.join(OUT, "conversations", base + ".md"), "w",
              encoding="utf-8") as f:
        f.write("\n".join(fm) + body)

    rows.append((created, trunk, len(msgs), len(body), len(artifacts_here),
                 title, base + ".md"))

# ---------------------------------------------------------------- projects
pj_rows = []
for fn in sorted(os.listdir(os.path.join(SRC, "projects"))):
    d = jload(os.path.join(SRC, "projects", fn))
    if isinstance(d, list):
        d = d[0] if d else {}
    name = d.get("name") or "untitled"
    docs = d.get("docs") or []
    instr = d.get("prompt_template") or ""
    trunk, _, _ = classify(name + " " + instr + " " +
                           " ".join(str(x.get("content", ""))[:8000] for x in docs))
    pdir = os.path.join(OUT, "projects", slug(name))
    os.makedirs(pdir, exist_ok=True)
    with open(os.path.join(pdir, "_project.md"), "w", encoding="utf-8") as f:
        f.write(f"---\ntitle: {yamlq(name)}\nuuid: {d.get('uuid')}\n"
                f"created: {(d.get('created_at') or '')[:10]}\ntrunk: {trunk}\n"
                f"kind: project\ndocs: {len(docs)}\n---\n\n# {name}\n\n"
                f"## Instructions\n\n{instr or '_(none)_'}\n")
    for doc in docs:
        dn = slug(doc.get("filename") or doc.get("name") or "doc", 70)
        with open(os.path.join(pdir, dn + ".md"), "w", encoding="utf-8") as f:
            f.write(f"---\ntitle: {yamlq(doc.get('filename') or doc.get('name'))}\n"
                    f"project: {yamlq(name)}\ntrunk: {trunk}\nkind: "
                    f"project-knowledge\n---\n\n{doc.get('content') or ''}")
    pj_rows.append((name, trunk, len(docs), len(instr), slug(name)))

# ---------------------------------------------------------------- memories
mem = jload(os.path.join(SRC, "memories.json"))
m0 = mem[0] if isinstance(mem, list) else mem
pm = m0.get("project_memories") or {}
pname = {r[4]: r[0] for r in pj_rows}
uuid_name = {}
for fn in os.listdir(os.path.join(SRC, "projects")):
    d = jload(os.path.join(SRC, "projects", fn))
    if isinstance(d, list):
        d = d[0] if d else {}
    uuid_name[d.get("uuid")] = d.get("name")

with open(os.path.join(OUT, "PROJECT-MEMORIES.md"), "w", encoding="utf-8") as f:
    f.write("---\ntitle: \"Project memories (claude.ai)\"\nkind: memory\n"
            "source: claude.ai-export-2026-08-15\n---\n\n"
            "# Project memories\n\nWhat claude.ai had retained about each "
            "project. Highest-density summary of your own architecture "
            "in the entire export.\n\n")
    for uid, txt in pm.items():
        f.write(f"\n---\n\n## {uuid_name.get(uid, uid)}\n\n{txt}\n")

os.makedirs(PRIV, exist_ok=True)
with open(os.path.join(PRIV, "account-memory.md"), "w", encoding="utf-8") as f:
    f.write("---\ntitle: \"Account memory (PII — gitignored)\"\nkind: memory\n"
            "visibility: private\n---\n\n" + (m0.get("conversations_memory") or ""))

# ---------------------------------------------------------------- index
rows.sort(reverse=True)
tc = collections.Counter(r[1] for r in rows)
with open(os.path.join(OUT, "INDEX.md"), "w", encoding="utf-8") as f:
    f.write(f"""---
title: "Claude archive index"
kind: index
source: claude.ai-export-2026-08-15
generated: {datetime.date.today().isoformat()}
---

# Claude archive — 2026-08-15

Full claude.ai history, {rows[-1][0]} to {rows[0][0]}.

| | |
|---|---|
| Conversations | {len(rows)} |
| Artifacts recovered | {art_n} |
| Generated files recovered | {file_n} |
| Projects | {len(pj_rows)} |
| BLACK / ORANGE / BOTH / OTHER | {tc['BLACK']} / {tc['ORANGE']} / {tc['BOTH']} / {tc['OTHER']} |

## Projects

| Project | Trunk | Docs | Instructions |
|---|---|---|---|
""")
    for name, trunk, nd, ni, sl in sorted(pj_rows, key=lambda x: -x[2]):
        f.write(f"| [{name}](projects/{sl}/_project.md) | {trunk} | {nd} | {ni:,}ch |\n")

    f.write("\n## Conversations\n\n| Date | Trunk | Msgs | Size | Art | Title |\n"
            "|---|---|---|---|---|---|\n")
    for created, trunk, nm, ch, na, title, fn in rows:
        t = title.replace("|", "\\|")[:70]
        f.write(f"| {created} | {trunk} | {nm} | {ch//1000}k | "
                f"{na or ''} | [{t}](conversations/{fn}) |\n")

print(f"conversations : {len(rows)}")
print(f"artifacts     : {art_n}")
print(f"files         : {file_n}")
print(f"projects      : {len(pj_rows)}")
print("trunks        :", dict(tc))
print(f"output        : {OUT}")
