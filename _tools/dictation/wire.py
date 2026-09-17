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


if __name__ == "__main__":
    # stdio is the wire: stdout carries the protocol, so nothing else may print there.
    server.run(transport="stdio")
