"""tax.py - bytes and ~tokens (bytes // 4) sent before the first prompt."""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MEMORY = Path(r"C:\Users\U01_LEECHSEED\.claude\projects\c--Users-U01-LEECHSEED-Desktop--setsunadev\memory\MEMORY.md")


def fm(path, only=None):
    """Frontmatter text of a file (only=key: just that key's line)."""
    t = path.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"---\r?\n(.*?)\r?\n---", t, re.S)
    body = m.group(1) if m else ""
    if only:
        mm = re.search(rf"^{only}:.*$", body, re.M)
        return mm.group(0) if mm else ""
    return body


def size(path):
    return len(path.read_bytes()) if path.is_file() else 0


def mcp_tools():
    n = 0
    names = []
    cfg = ROOT / ".mcp.json"
    servers = json.loads(cfg.read_text(encoding="utf-8")).get("mcpServers", {}) if cfg.is_file() else {}
    for name, s in servers.items():
        script = next((a for a in s.get("args", []) if a.endswith(".py")), None)
        c = 0
        if script and (ROOT / script).is_file():
            src = (ROOT / script).read_text(encoding="utf-8", errors="replace")
            c = len(re.findall(r"@\w+\.tool\(", src)) or len(re.findall(r'^\s*\{?\s*"name":', src, re.M))
        names.append(f"{name}={c}")
        n += c
    return n, names


def main():
    rows = []
    rows.append(("CLAUDE.md", size(ROOT / "CLAUDE.md")))
    sk = sum(len(fm(p, "description").encode()) for p in ROOT.glob(".claude/skills/*/SKILL.md"))
    rows.append(("skill descriptions", sk))
    ag = sum(len(fm(p).encode()) for p in ROOT.glob(".claude/agents/*.md") if p.name != "README.md")
    rows.append(("agent frontmatter", ag))
    rows.append(("memory index", size(MEMORY)))
    try:
        r = subprocess.run([sys.executable, str(ROOT / "_tools/sitrep/digest.py")], capture_output=True, cwd=ROOT, timeout=60)
        rows.append(("SessionStart digest", len(r.stdout)))
    except Exception as e:
        rows.append((f"digest (failed: {e.__class__.__name__})", 0))
    rows.append((".mcp.json", size(ROOT / ".mcp.json")))
    n, names = mcp_tools()
    total = sum(b for _, b in rows)
    print(f"{'source':<26}{'bytes':>9}{'~tokens':>9}")
    for k, b in rows:
        print(f"{k:<26}{b:>9}{b // 4:>9}")
    print(f"mcp tool counts: {n} ({', '.join(names)}) - schemas not measured")
    print(f"TOTAL before first prompt: {total} bytes, ~{total // 4} tokens")


if __name__ == "__main__":
    main()
