---
original_path: "/home/claude/original.py"
source_conversation: "Code debugging"
created: 2026-06-04
trunk: BLACK
kind: generated-file
---

import os
import sys
import time
import re
import threading
import sqlite3
import signal
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse
from contextlib import contextmanager

try:
    import yt_dlp
except ImportError:
    print("ERROR: yt-dlp module not installed.  pip install yt-dlp")
    sys.exit(1)

try:
    from rich.console import Console, Group
    from rich.live import Live
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich.align import Align
    from rich.markup import escape as rich_escape
except ImportError:
    print("ERROR: rich not installed.  pip install rich")
    sys.exit(1)

COOKIES_BROWSER: str | None = "firefox"
OUTPUT_DIR: Path = Path.cwd()
OUTPUT_TEMPLATE: str = "%(title,id)s.%(ext)s"
EXTRA_YTDLP_OPTS: dict = {}

APP_DIR: Path = Path.home() / ".ytdlp_go"
APP_DIR.mkdir(exist_ok=True)
DB_PATH: Path = APP_DIR / "queue.sqlite"
ARCHIVE_PATH: Path = APP_DIR / "archive.txt"

TRACKING_PARAMS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "fbclid", "gclid", "dclid", "msclkid", "mc_cid", "mc_eid", "igshid",
    "si", "feature_share", "share_source", "ref_src", "ref_url",
}

POLL_INTERVAL = 0.25

URL_RE = re.compile(r'https?://[^\s<>"\'\]\)]{4,}', re.IGNORECASE)


def looks_like_url(text: str) -> bool:
    text = text.strip()
    if not URL_RE.fullmatch(text):
        return False
    try:
        p = urlparse(text)
        return p.scheme in ("http", "https") and bool(p.netloc)
    except Exception:
        return False


def normalize_url(url: str) -> str:
    try:
        p = urlparse(url.strip())
        if p.scheme not in ("http", "https"):
            return url.strip()
        host = p.netloc.lower()
        if host.startswith("www."):
            host = host[4:]
        query = [
            (k, v) for k, v in parse_qsl(p.query, keep_blank_values=True)
            if k.lower() not in TRACKING_PARAMS
        ]
        path = p.path.rstrip("/") or "/"
        return urlunparse((p.scheme, host, path, "", urlencode(query), ""))
    except Exception:
        return url.strip()


def parse_cookies_browser(s: str | None):
    if not s:
        return None
    browser, profile, keyring, container = s, None, None, None
    if "::" in browser:
        browser, container = browser.split("::", 1)
    if "+" in browser:
        browser, keyring = browser.split("+", 1)
    if ":" in browser:
        browser, profile = browser.split(":", 1)
    return (browser, profile, keyring, container)


def get_clipboard_text() -> str:
    try:
        if sys.platform == "win32":
            return ""
        else:
            import pyperclip
            return pyperclip.paste() or ""
    except Exception:
        return ""


SCHEMA = """
CREATE TABLE IF NOT EXISTS downloads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    normalized_url TEXT UNIQUE NOT NULL,
    status TEXT NOT NULL,
    title TEXT,
    filepath TEXT,
    error TEXT,
    added_at TEXT NOT NULL,
    finished_at TEXT
);
CREATE INDEX IF NOT EXISTS idx_status ON downloads(status);
"""


class Store:
    def __init__(self, path):
        self.path = path
        self.lock = threading.Lock()
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.conn.executescript(SCHEMA)
        self.conn.execute("PRAGMA journal_mode=WAL")
        self.conn.execute(
            "UPDATE downloads SET status='pending' WHERE status='active'"
        )
        self.conn.commit()

    @contextmanager
    def _cur(self):
        with self.lock:
            cur = self.conn.cursor()
            try:
                yield cur
                self.conn.commit()
            finally:
                cur.close()

    def enqueue(self, url):
        norm = normalize_url(url)
        with self._cur() as cur:
            row = cur.execute(
                "SELECT status FROM downloads WHERE normalized_url=?", (norm,)
            ).fetchone()
            if row:
                return False, ("done" if row[0] == "done" else "duplicate")
            cur.execute(
                "INSERT INTO downloads "
                "(url, normalized_url, status, added_at) "
                "VALUES (?, ?, 'pending', ?)",
                (url, norm, datetime.now().isoformat(timespec="seconds")),
            )
            return True, "queued"

    def claim_next(self):
        with self._cur() as cur:
            row = cur.execute(
                "SELECT id, url FROM downloads WHERE status='pending' "
                "ORDER BY id ASC LIMIT 1"
            ).fetchone()
            if not row:
                return None
            cur.execute(
                "UPDATE downloads SET status='active' WHERE id=?", (row[0],)
            )
            return row

    def mark_done(self, id_, title, filepath):
        with self._cur() as cur:
            cur.execute(
                "UPDATE downloads SET status='done', title=?, filepath=?, "
                "finished_at=? WHERE id=?",
                (title, filepath,
                 datetime.now().isoformat(timespec="seconds"), id_),
            )

    def mark_failed(self, id_, error):
        with self._cur() as cur:
            cur.execute(
                "UPDATE downloads SET status='failed', error=?, finished_at=? "
                "WHERE id=?",
                (error[:500],
                 datetime.now().isoformat(timespec="seconds"), id_),
            )

    def requeue_active(self):
        with self._cur() as cur:
            cur.execute(
                "UPDATE downloads SET status='pending' WHERE status='active'"
            )

    def stats(self):
        with self._cur() as cur:
            rows = cur.execute(
                "SELECT status, COUNT(*) FROM downloads GROUP BY status"
            ).fetchall()
        return {s: c for s, c in rows}

    def pending_preview(self, limit=10):
        with self._cur() as cur:
            return cur.execute(
                "SELECT id, url FROM downloads WHERE status='pending' "
                "ORDER BY id ASC LIMIT ?", (limit,)
            ).fetchall()

    def resume_count(self):
        with self._cur() as cur:
            (n,) = cur.execute(
                "SELECT COUNT(*) FROM downloads WHERE status='pending'"
            ).fetchone()
            return n

    def close(self):
        with self.lock:
            self.conn.close()
