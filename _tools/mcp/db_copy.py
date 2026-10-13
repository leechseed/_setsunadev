"""
db_copy.py - copy the live databases into _PRIVATE/dbcopies/ for sqlite_ro.py.

Uses the sqlite3 backup API, so WAL content is included. Sources open read-only
(mode=ro); nothing is ever written to them.

    python _tools/mcp/db_copy.py                 # both
    python _tools/mcp/db_copy.py --only stash    # or zotero
"""

import argparse
import os
import sqlite3
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DEST = os.path.join(ROOT, "_PRIVATE", "dbcopies")

SOURCES = {
    "stash": ("Q:/fun/.StashApp/stash-go.sqlite", "stash.sqlite"),
    "zotero": ("C:/Users/U01_LEECHSEED/Zotero/zotero.sqlite", "zotero.sqlite"),
}


def copy_one(key):
    src_path, out = SOURCES[key]
    os.makedirs(DEST, exist_ok=True)
    dst_path = os.path.join(DEST, out)
    tmp = dst_path + ".tmp"
    if os.path.exists(tmp):
        os.remove(tmp)
    src = sqlite3.connect(f"file:{src_path}?mode=ro", uri=True, timeout=10)
    dst = sqlite3.connect(tmp)
    try:
        src.backup(dst)
    finally:
        dst.close()
        src.close()
    os.replace(tmp, dst_path)
    size = os.path.getsize(dst_path) / 1e6
    print(f"{key}: {size:.1f} MB -> {dst_path} at {time.strftime('%Y-%m-%d %H:%M:%S')}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=list(SOURCES))
    args = ap.parse_args()
    bad = 0
    for key in ([args.only] if args.only else list(SOURCES)):
        try:
            copy_one(key)
        except Exception as e:
            bad += 1
            print(f"{key}: FAILED {type(e).__name__}: {e}")
            tmp = os.path.join(DEST, SOURCES[key][1] + ".tmp")
            if os.path.exists(tmp):
                try:
                    os.remove(tmp)
                except OSError:
                    pass
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
