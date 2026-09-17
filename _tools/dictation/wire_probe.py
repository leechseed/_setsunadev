"""
wire_probe.py — prove the wire without the session.

Spawns wire.py over stdio exactly as .mcp.json will, lists the tools, calls each
one once, prints the spoken answer and the round-trip time. Exit 1 if any tool
is missing or any call fails.

    python _tools/dictation/wire_probe.py
"""

import asyncio
import os
import sys
import time

from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
EXPECTED = ["blocked", "bolo", "pmcs", "effort", "box", "time", "help"]
CALLS = [
    ("blocked", {}),
    ("bolo", {"n": 56}),
    ("bolo", {}),
    ("pmcs", {}),
    ("effort", {}),
    ("box", {}),
    ("time", {}),
    ("help", {}),
]


def text_of(result):
    parts = []
    for c in result.content:
        t = getattr(c, "text", None)
        if t:
            parts.append(t)
    return " ".join(parts)


async def main():
    params = StdioServerParameters(
        command=sys.executable,
        args=[os.path.join("_tools", "dictation", "wire.py")],
        cwd=ROOT,
    )
    t0 = time.perf_counter()
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as s:
            await s.initialize()
            print(f"connected in {time.perf_counter() - t0:.2f}s · server "
                  f"{s.server_info.name if s.server_info else '?'}")
            tools = await s.list_tools()
            names = [t.name for t in tools.tools]
            missing = [n for n in EXPECTED if n not in names]
            print(f"tools ({len(names)}): {', '.join(names)}")
            if missing:
                print("MISSING:", ", ".join(missing))
                return 1
            bad = 0
            for name, args in CALLS:
                t1 = time.perf_counter()
                r = await s.call_tool(name, args)
                dt = (time.perf_counter() - t1) * 1000
                ok = not getattr(r, "isError", False)
                bad += 0 if ok else 1
                label = name + (f"({args['n']})" if args else "")
                print(f"  {'ok ' if ok else 'ERR'} {label:12s} {dt:6.0f} ms  {text_of(r)[:110]}")
            return 1 if bad else 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    raise SystemExit(asyncio.run(main()))
