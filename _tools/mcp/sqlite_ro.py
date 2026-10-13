"""
sqlite_ro.py - the Command's read-only SQLite MCP server (BOLO 140).

Speaks MCP over stdio (newline-delimited JSON-RPC 2.0), stdlib only. Serves only
the COPIES in _PRIVATE/dbcopies/ (made by db_copy.py), never the live databases.

Tools:
    dbs()                          list the copies with size and copy time
    tables(db)                     table names in one copy
    schema(db, table)              the CREATE statement and columns of one table
    query(db, sql, limit=200)      one SELECT / WITH...SELECT; max 1000 rows

Refresh the copies first:  python _tools/mcp/db_copy.py
Prove the server:          python _tools/mcp/probe_sqlite_ro.py

Add this to .mcp.json under "mcpServers" (not added for you):

    "sqlite_ro": {
      "command": "python",
      "args": ["_tools/mcp/sqlite_ro.py"]
    }

stdout carries the protocol; nothing else may print there.
"""

import json
import os
import re
import sqlite3
import sys
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
COPIES = os.path.join(ROOT, "_PRIVATE", "dbcopies")
PROTOCOL = "2024-11-05"
CELL_MAX = 120
ROW_MAX = 1000

FORBIDDEN = re.compile(
    r"\b(PRAGMA|ATTACH|DETACH|INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|VACUUM|REPLACE)\b",
    re.I,
)

TOOLS = [
    {"name": "dbs", "description": "List the read-only database copies with size and copy time.",
     "inputSchema": {"type": "object", "properties": {}}},
    {"name": "tables", "description": "List the tables in one database copy.",
     "inputSchema": {"type": "object", "properties": {"db": {"type": "string"}}, "required": ["db"]}},
    {"name": "schema", "description": "Show the CREATE statement and columns of one table.",
     "inputSchema": {"type": "object", "properties": {"db": {"type": "string"}, "table": {"type": "string"}},
                     "required": ["db", "table"]}},
    {"name": "query", "description": "Run one SELECT (or WITH...SELECT) on a copy. Rows capped at limit (default 200, max 1000).",
     "inputSchema": {"type": "object", "properties": {
         "db": {"type": "string"}, "sql": {"type": "string"}, "limit": {"type": "integer"}},
         "required": ["db", "sql"]}},
]


class ToolError(Exception):
    pass


def db_path(name):
    name = os.path.basename(str(name or ""))
    if not name.endswith(".sqlite") and not name.endswith(".db"):
        name += ".sqlite"
    p = os.path.join(COPIES, name)
    if not os.path.isfile(p):
        raise ToolError(f"no such copy: {name}. Call dbs to list them.")
    return p


def connect(name):
    p = db_path(name)
    conn = sqlite3.connect(f"file:{p}?mode=ro", uri=True, timeout=10)
    conn.execute("PRAGMA busy_timeout = 10000")
    conn.execute("PRAGMA query_only = 1")
    return conn


def cell(v):
    if v is None:
        return "NULL"
    if isinstance(v, bytes):
        return f"<{len(v)} bytes>"
    s = str(v).replace("\r", " ").replace("\n", " ").replace("\t", " ")
    return s if len(s) <= CELL_MAX else s[:CELL_MAX - 3] + "..."


def table_text(header, rows):
    out = [" | ".join(header)]
    out += [" | ".join(cell(v) for v in r) for r in rows]
    return "\n".join(out)


def strip_comments(sql):
    sql = re.sub(r"/\*.*?\*/", " ", sql, flags=re.S)
    sql = re.sub(r"--[^\n]*", " ", sql)
    return sql.strip()


def check_sql(sql):
    s = strip_comments(sql)
    s = s.rstrip(";").strip() if s.endswith(";") else s
    if not s:
        raise ToolError("empty statement")
    if ";" in s:
        raise ToolError("only one statement allowed (no semicolons)")
    if not re.match(r"(SELECT|WITH)\b", s, re.I):
        raise ToolError("only SELECT or WITH...SELECT is allowed")
    m = FORBIDDEN.search(s)
    if m:
        raise ToolError(f"refused keyword: {m.group(1).upper()}")
    return s


def t_dbs(_a):
    if not os.path.isdir(COPIES):
        return "no copies yet. Run: python _tools/mcp/db_copy.py"
    rows = []
    for f in sorted(os.listdir(COPIES)):
        p = os.path.join(COPIES, f)
        if os.path.isfile(p) and f.endswith((".sqlite", ".db")):
            st = os.stat(p)
            rows.append((f, f"{st.st_size / 1e6:.1f} MB",
                         datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M")))
    return table_text(["db", "size", "copied"], rows) if rows else "no copies yet."


def t_tables(a):
    conn = connect(a.get("db"))
    try:
        rows = conn.execute(
            "SELECT name, type FROM sqlite_master WHERE type IN ('table','view') ORDER BY name").fetchall()
    finally:
        conn.close()
    return table_text(["name", "type"], rows)


def t_schema(a):
    table = str(a.get("table") or "")
    conn = connect(a.get("db"))
    try:
        r = conn.execute("SELECT sql FROM sqlite_master WHERE name = ?", (table,)).fetchone()
        if not r:
            raise ToolError(f"no such table: {table}")
        cols = conn.execute(f'PRAGMA table_info("{table.replace(chr(34), "")}")').fetchall()
    finally:
        conn.close()
    return (r[0] or "") + "\n\n" + table_text(
        ["cid", "name", "type", "notnull", "default", "pk"], cols)


def t_query(a):
    sql = check_sql(a.get("sql") or "")
    try:
        limit = int(a.get("limit") or 200)
    except (TypeError, ValueError):
        raise ToolError("limit must be an integer")
    limit = max(1, min(limit, ROW_MAX))
    conn = connect(a.get("db"))
    try:
        cur = conn.execute(sql)
        header = [d[0] for d in (cur.description or [])]
        rows = cur.fetchmany(limit + 1)
    finally:
        conn.close()
    more = len(rows) > limit
    rows = rows[:limit]
    text = table_text(header, rows)
    return text + (f"\n(truncated at {limit} rows)" if more else f"\n({len(rows)} rows)")


HANDLERS = {"dbs": t_dbs, "tables": t_tables, "schema": t_schema, "query": t_query}


def send(obj):
    sys.stdout.write(json.dumps(obj, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def reply(mid, result=None, error=None):
    msg = {"jsonrpc": "2.0", "id": mid}
    if error is not None:
        msg["error"] = error
    else:
        msg["result"] = result
    send(msg)


def handle(msg):
    method = msg.get("method")
    mid = msg.get("id")
    if mid is None:  # notification
        return
    if method == "initialize":
        pv = (msg.get("params") or {}).get("protocolVersion") or PROTOCOL
        reply(mid, {
            "protocolVersion": pv,
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": "sqlite_ro", "version": "0.1"},
            "instructions": "Read-only SQLite over copies in _PRIVATE/dbcopies. Start with dbs.",
        })
    elif method == "ping":
        reply(mid, {})
    elif method == "tools/list":
        reply(mid, {"tools": TOOLS})
    elif method == "tools/call":
        p = msg.get("params") or {}
        fn = HANDLERS.get(p.get("name"))
        if fn is None:
            reply(mid, error={"code": -32602, "message": f"unknown tool: {p.get('name')}"})
            return
        try:
            text, err = fn(p.get("arguments") or {}), False
        except ToolError as e:
            text, err = str(e), True
        except sqlite3.Error as e:
            text, err = f"sqlite error: {e}", True
        except Exception as e:  # never crash the server
            text, err = f"error: {type(e).__name__}: {e}", True
        reply(mid, {"content": [{"type": "text", "text": text}], "isError": err})
    else:
        reply(mid, error={"code": -32601, "message": f"method not found: {method}"})


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            handle(json.loads(line))
        except json.JSONDecodeError:
            send({"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "parse error"}})
        except Exception as e:
            send({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}})


if __name__ == "__main__":
    main()
