"""
wire.py — JUDY's wire: brain.py's tools exposed to the VS Code session over MCP.

BOLO 56. RULED 9/16: the wire is an MCP server, all in. RULED 9/17: the brain stays
on the router. Together those mean the wire is not a model feed — it is the seven
tools in brain.py, unchanged, reachable from the Opus session through the Model
Context Protocol. The tools were written once, for exactly this; nothing here adds
logic, and nothing here adds a key, a model, or a standing cost.

    stdio transport, spawned by the session from .mcp.json at the repo root:
        python _tools/dictation/wire.py

    prove it without the session:
        python _tools/dictation/wire_probe.py

Not named mcp.py on purpose: a script's own directory is first on sys.path, so a
file called mcp.py would shadow the `mcp` package it imports.

Every answer comes back as the spoken form brain.py already writes — short
sentences, no markdown — so the session can read it, or hand it to speak.py.
"""

import os
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import brain  # noqa: E402  (the tool layer; the router lives there too)

from mcp.server.mcpserver import MCPServer  # noqa: E402

server = MCPServer(
    name="judy",
    title="JUDY — the wire",
    version="0.1",
    instructions=(
        "JUDY's seven tools over the Command's files. Each returns one spoken-form "
        "string. She answers a short list of real questions exactly right and "
        "refuses everything else; there is no model behind these, so do not ask "
        "them to guess."
    ),
)


@server.tool(name="blocked", description="The Blocked-on-you table from STATE.md: the count, the oldest two, how many more.")
def blocked() -> str:
    return brain.t_blocked()


@server.tool(name="bolo", description="One BOLO by number (title and status), or with no number, how many are on the watchlist and which is newest.")
def bolo(n: int | None = None) -> str:
    return brain.t_bolo(n)


@server.tool(name="pmcs", description="The operator's PMCS readiness rows from BOLO.md: how many are red, and which.")
def pmcs() -> str:
    return brain.t_pmcs()


@server.tool(name="effort", description="The main effort and the leverage line off the last sit rep board on disk.")
def effort() -> str:
    return brain.t_effort()


@server.tool(name="box", description="Whether the box is up: Stash on 9999, DARKROOM on 8484, the console on 8787, and whether the git tree is clean.")
def box() -> str:
    return brain.t_box()


@server.tool(name="time", description="The clock, spoken.")
def time_() -> str:
    return brain.t_time()


@server.tool(name="help", description="What JUDY can answer, in her own words.")
def help_() -> str:
    return brain.t_help()


STASH_COPY = os.path.abspath(os.path.join(HERE, "..", "..", "_PRIVATE", "dbcopies", "stash.sqlite"))
NO_COPY = "No Stash copy; run _tools/mcp/db_copy.py."


def _stash():
    """Read-only handle on the SQLite copy (never the live DB), or None if missing."""
    if not os.path.isfile(STASH_COPY):
        return None
    uri = "file:" + STASH_COPY.replace("\\", "/").replace("?", "%3f").replace("#", "%23") + "?mode=ro"
    c = sqlite3.connect(uri, uri=True)
    c.execute("PRAGMA query_only=1")
    return c


def _spoken(label, rows):
    if not rows:
        return f"No {label} match."
    parts = [f"{n}, {k} scene{'' if k == 1 else 's'}" for n, k in rows]
    return f"{len(rows)} {label}: " + "; ".join(parts) + "."


@server.tool(name="stash_find", description="Stash performers, studios and tags whose name contains the text (case-insensitive, up to 10 each) with scene counts. Read-only, from the local copy.")
def stash_find(name: str) -> str:
    text = (name or "").strip()
    if not text:
        return "Say a name to look for."
    try:
        c = _stash()
        if c is None:
            return NO_COPY
        try:
            like = "%" + text.lower().replace("\\", "\\\\").replace("%", "\%").replace("_", "\_") + "%"
            perf = c.execute(
                "SELECT p.name, COUNT(ps.scene_id) FROM performers p "
                "LEFT JOIN performers_scenes ps ON ps.performer_id = p.id "
                "WHERE lower(p.name) LIKE ? ESCAPE '\' GROUP BY p.id ORDER BY 2 DESC LIMIT 10", (like,)).fetchall()
            stud = c.execute(
                "SELECT s.name, COUNT(sc.id) FROM studios s "
                "LEFT JOIN scenes sc ON sc.studio_id = s.id "
                "WHERE lower(s.name) LIKE ? ESCAPE '\' GROUP BY s.id ORDER BY 2 DESC LIMIT 10", (like,)).fetchall()
            tags = c.execute(
                "SELECT t.name, COUNT(st.scene_id) FROM tags t "
                "LEFT JOIN scenes_tags st ON st.tag_id = t.id "
                "WHERE lower(t.name) LIKE ? ESCAPE '\' GROUP BY t.id ORDER BY 2 DESC LIMIT 10", (like,)).fetchall()
        finally:
            c.close()
    except sqlite3.Error as e:
        return f"Stash copy would not open: {e}."
    return " ".join([_spoken("performers", perf), _spoken("studios", stud), _spoken("tags", tags)])


@server.tool(name="stash_counts", description="Stash library totals: scenes, images, performers, studios, tags. Read-only, from the local copy.")
def stash_counts() -> str:
    try:
        c = _stash()
        if c is None:
            return NO_COPY
        try:
            n = {t: c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
                 for t in ("scenes", "images", "performers", "studios", "tags")}
        finally:
            c.close()
    except sqlite3.Error as e:
        return f"Stash copy would not open: {e}."
    return (f"Stash holds {n['scenes']} scenes, {n['images']} images, {n['performers']} performers, "
            f"{n['studios']} studios and {n['tags']} tags.")


if __name__ == "__main__":
    # stdio is the wire: stdout carries the protocol, so nothing else may print there.
    server.run(transport="stdio")
