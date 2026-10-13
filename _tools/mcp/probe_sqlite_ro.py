"""
probe_sqlite_ro.py - prove sqlite_ro.py without the session.

Spawns the server over stdio, runs initialize + tools/list + dbs + one query on
the first copy, prints the answers. Exit 1 on any failure.

    python _tools/mcp/probe_sqlite_ro.py
"""

import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
EXPECTED = ["dbs", "tables", "schema", "query"]


class Client:
    def __init__(self):
        self.p = subprocess.Popen(
            [sys.executable, os.path.join("_tools", "mcp", "sqlite_ro.py")],
            cwd=ROOT, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL, text=True, encoding="utf-8")
        self.n = 0

    def send(self, obj):
        self.p.stdin.write(json.dumps(obj) + "\n")
        self.p.stdin.flush()

    def call(self, method, params=None):
        self.n += 1
        self.send({"jsonrpc": "2.0", "id": self.n, "method": method, "params": params or {}})
        return json.loads(self.p.stdout.readline())

    def close(self):
        self.p.stdin.close()
        try:
            self.p.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self.p.kill()


def text_of(r):
    res = r.get("result", {})
    return " ".join(c.get("text", "") for c in res.get("content", []))


def main():
    c = Client()
    bad = 0
    try:
        t0 = time.perf_counter()
        r = c.call("initialize", {"protocolVersion": "2024-11-05", "capabilities": {},
                                  "clientInfo": {"name": "probe", "version": "0"}})
        c.send({"jsonrpc": "2.0", "method": "notifications/initialized"})
        print(f"connected in {time.perf_counter() - t0:.2f}s - server {r['result']['serverInfo']['name']}")
        names = [t["name"] for t in c.call("tools/list")["result"]["tools"]]
        print(f"tools ({len(names)}): {', '.join(names)}")
        if [n for n in EXPECTED if n not in names]:
            print("MISSING tools")
            return 1
        r = c.call("tools/call", {"name": "dbs", "arguments": {}})
        dbs_text = text_of(r)
        print("dbs:\n" + dbs_text)
        bad += 1 if r["result"].get("isError") else 0
        lines = dbs_text.splitlines()[1:]
        if not lines or "|" not in lines[0]:
            print("ERR no copies")
            return 1
        first = lines[0].split("|")[0].strip()
        r = c.call("tools/call", {"name": "query", "arguments": {
            "db": first, "sql": "SELECT name FROM sqlite_master WHERE type='table' LIMIT 5"}})
        print(f"query on {first}:\n" + text_of(r))
        bad += 1 if r["result"].get("isError") else 0
        r = c.call("tools/call", {"name": "query", "arguments": {"db": first, "sql": "DROP TABLE x"}})
        refused = r["result"].get("isError")
        print(f"guard (DROP refused): {'ok' if refused else 'ERR'} - {text_of(r)}")
        bad += 0 if refused else 1
        return 1 if bad else 0
    except Exception as e:
        print(f"FAIL {type(e).__name__}: {e}")
        return 1
    finally:
        c.close()


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    raise SystemExit(main())
