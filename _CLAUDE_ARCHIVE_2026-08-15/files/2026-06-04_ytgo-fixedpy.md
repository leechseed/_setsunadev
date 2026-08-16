---
original_path: "/home/claude/ytgo_fixed.py"
source_conversation: "Code debugging"
created: 2026-06-04
trunk: BLACK
kind: generated-file
---

"""
yt-dlp Quick Downloader v2.1 — Clipboard Monitor + Persistent Queue
==================================================================
Copy URLs as fast as you want. They queue up and download one by one.

What's new vs v2:
  * Ctrl+C no longer deadlocks (the signal handler used to grab a UI lock
    the main thread already held — see notes below). First Ctrl+C now
    drains gracefully; second Ctrl+C force-quits.
  * 64-bit-correct clipboard read (GlobalLock/GetClipboardData argtypes).
  * Event path no longer drops a URL if two changes race the dispatcher.
  * Active panel shows the real video title once yt-dlp resolves it.

Requirements:
    pip install yt-dlp rich
    pip install pyperclip          # only on non-Windows

State files live in:  ~/.ytdlp_go/
    queue.sqlite       — pending/active/done/failed rows
    archive.txt        — yt-dlp's own "already downloaded" archive

Controls:
    Copy a URL          → queued instantly
    Ctrl+C  (once)      → finishes current download, persists state, exits
    Ctrl+C  (twice)     → force-quit now (current download is abandoned,
                          its row is left 'active' and resumes next launch)
"""

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

# ---------------------------------------------------------------------------
# Dependency checks
# ---------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------
# CONFIG — edit to taste
# ---------------------------------------------------------------------------
COOKIES_BROWSER: str | None = "firefox"
OUTPUT_DIR: Path = Path.cwd()
OUTPUT_TEMPLATE: str = "%(title,id)s.%(ext)s"

# Extra yt-dlp options, applied to every download (Python API dict form).
EXTRA_YTDLP_OPTS: dict = {
    # 'format': 'bv*+ba/b',
    # 'ratelimit': 5 * 1024 * 1024,
}

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

# ---------------------------------------------------------------------------
# URL normalization + detection
# ---------------------------------------------------------------------------
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
    """Strip tracking junk so the same video copied twice dedupes correctly."""
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
    """Turn 'firefox:profile::container' into yt-dlp's tuple form."""
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


# ---------------------------------------------------------------------------
# Clipboard reading
# ---------------------------------------------------------------------------
def get_clipboard_text() -> str:
    try:
        if sys.platform == "win32":
            import ctypes
            from ctypes import wintypes
            CF_UNICODETEXT = 13
            user32 = ctypes.WinDLL("user32", use_last_error=True)
            kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)

            # 64-bit correctness: HANDLE/pointer-returning calls MUST declare
            # restype, or ctypes truncates the result to 32 bits and you read
            # a bogus (or NULL) pointer. v2 set GlobalLock.restype but left
            # the others defaulted — fixed here.
            user32.OpenClipboard.argtypes = [wintypes.HWND]
            user32.OpenClipboard.restype = wintypes.BOOL
            user32.CloseClipboard.argtypes = []
            user32.CloseClipboard.restype = wintypes.BOOL
            user32.GetClipboardData.argtypes = [wintypes.UINT]
            user32.GetClipboardData.restype = wintypes.HANDLE
            kernel32.GlobalLock.argtypes = [wintypes.HGLOBAL]
            kernel32.GlobalLock.restype = ctypes.c_wchar_p
            kernel32.GlobalUnlock.argtypes = [wintypes.HGLOBAL]
            kernel32.GlobalUnlock.restype = wintypes.BOOL

            if not user32.OpenClipboard(None):
                return ""
            try:
                handle = user32.GetClipboardData(CF_UNICODETEXT)
                if not handle:
                    return ""
                data = kernel32.GlobalLock(handle)
                result = str(data) if data else ""
                kernel32.GlobalUnlock(handle)
                return result
            finally:
                user32.CloseClipboard()
        else:
            import pyperclip
            return pyperclip.paste() or ""
    except Exception:
        return ""


# ---------------------------------------------------------------------------
# Windows: native clipboard-change event listener (hidden message window)
# ---------------------------------------------------------------------------
class WinClipboardListener(threading.Thread):
    """Subscribes to WM_CLIPBOARDUPDATE via AddClipboardFormatListener.
    Calls on_change() from the listener thread whenever the clipboard changes.
    """
    WM_QUIT = 0x0012
    WM_CLIPBOARDUPDATE = 0x031D
    HWND_MESSAGE = -3

    def __init__(self, on_change):
        super().__init__(daemon=True, name="clipboard-listener")
        self.on_change = on_change
        self._thread_id: int | None = None
        self._hwnd = None
        self._wndproc_ref = None   # keep callback alive (else GC -> crash)
        self._user32 = None
        self.started_evt = threading.Event()
        self.failed: Exception | None = None

    def run(self):
        try:
            self._run_loop()
        except Exception as e:
            self.failed = e
        finally:
            self.started_evt.set()

    def _run_loop(self):
        import ctypes
        from ctypes import wintypes

        user32 = ctypes.WinDLL("user32", use_last_error=True)
        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)

        LRESULT = ctypes.c_ssize_t
        HCURSOR = wintypes.HANDLE
        ATOM = wintypes.WORD

        kernel32.GetCurrentThreadId.argtypes = []
        kernel32.GetCurrentThreadId.restype = wintypes.DWORD

        kernel32.GetModuleHandleW.argtypes = [wintypes.LPCWSTR]
        kernel32.GetModuleHandleW.restype = wintypes.HMODULE

        user32.DefWindowProcW.argtypes = [
            wintypes.HWND, wintypes.UINT,
            wintypes.WPARAM, wintypes.LPARAM,
        ]
        user32.DefWindowProcW.restype = LRESULT

        user32.CreateWindowExW.argtypes = [
            wintypes.DWORD, wintypes.LPCWSTR, wintypes.LPCWSTR,
            wintypes.DWORD,
            ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
            wintypes.HWND, wintypes.HMENU, wintypes.HINSTANCE,
            wintypes.LPVOID,
        ]
        user32.CreateWindowExW.restype = wintypes.HWND

        user32.DestroyWindow.argtypes = [wintypes.HWND]
        user32.DestroyWindow.restype = wintypes.BOOL

        user32.AddClipboardFormatListener.argtypes = [wintypes.HWND]
        user32.AddClipboardFormatListener.restype = wintypes.BOOL

        user32.RemoveClipboardFormatListener.argtypes = [wintypes.HWND]
        user32.RemoveClipboardFormatListener.restype = wintypes.BOOL

        user32.GetMessageW.argtypes = [
            ctypes.POINTER(wintypes.MSG), wintypes.HWND,
            wintypes.UINT, wintypes.UINT,
        ]
        user32.GetMessageW.restype = ctypes.c_int

        user32.TranslateMessage.argtypes = [ctypes.POINTER(wintypes.MSG)]
        user32.TranslateMessage.restype = wintypes.BOOL

        user32.DispatchMessageW.argtypes = [ctypes.POINTER(wintypes.MSG)]
        user32.DispatchMessageW.restype = LRESULT

        user32.PostThreadMessageW.argtypes = [
            wintypes.DWORD, wintypes.UINT,
            wintypes.WPARAM, wintypes.LPARAM,
        ]
        user32.PostThreadMessageW.restype = wintypes.BOOL

        self._thread_id = kernel32.GetCurrentThreadId()
        self._user32 = user32

        WNDPROC = ctypes.WINFUNCTYPE(
            LRESULT, wintypes.HWND, wintypes.UINT,
            wintypes.WPARAM, wintypes.LPARAM,
        )

        def wndproc(hwnd, msg, wparam, lparam):
            if msg == self.WM_CLIPBOARDUPDATE:
                try:
                    self.on_change()
                except Exception:
                    pass
                return 0
            return user32.DefWindowProcW(hwnd, msg, wparam, lparam)

        self._wndproc_ref = WNDPROC(wndproc)

        class WNDCLASSEXW(ctypes.Structure):
            _fields_ = [
                ("cbSize", wintypes.UINT),
                ("style", wintypes.UINT),
                ("lpfnWndProc", WNDPROC),
                ("cbClsExtra", ctypes.c_int),
                ("cbWndExtra", ctypes.c_int),
                ("hInstance", wintypes.HINSTANCE),
                ("hIcon", wintypes.HICON),
                ("hCursor", HCURSOR),
                ("hbrBackground", wintypes.HBRUSH),
                ("lpszMenuName", wintypes.LPCWSTR),
                ("lpszClassName", wintypes.LPCWSTR),
                ("hIconSm", wintypes.HICON),
            ]

        user32.RegisterClassExW.argtypes = [ctypes.POINTER(WNDCLASSEXW)]
        user32.RegisterClassExW.restype = ATOM

        hInstance = kernel32.GetModuleHandleW(None)
        cls_name = f"YtdlpGoClipboardListener_{os.getpid()}"
        wc = WNDCLASSEXW()
        wc.cbSize = ctypes.sizeof(WNDCLASSEXW)
        wc.lpfnWndProc = self._wndproc_ref
        wc.hInstance = hInstance
        wc.lpszClassName = cls_name

        if not user32.RegisterClassExW(ctypes.byref(wc)):
            raise OSError(
                f"RegisterClassExW failed: {ctypes.get_last_error()}"
            )

        HWND_MESSAGE = wintypes.HWND(self.HWND_MESSAGE)
        self._hwnd = user32.CreateWindowExW(
            0, cls_name, "ytdlp_go", 0, 0, 0, 0, 0,
            HWND_MESSAGE, None, hInstance, None,
        )
        if not self._hwnd:
            raise OSError(
                f"CreateWindowExW failed: {ctypes.get_last_error()}"
            )

        if not user32.AddClipboardFormatListener(self._hwnd):
            raise OSError(
                f"AddClipboardFormatListener failed: "
                f"{ctypes.get_last_error()}"
            )

        self.started_evt.set()

        msg = wintypes.MSG()
        while True:
            ret = user32.GetMessageW(ctypes.byref(msg), None, 0, 0)
            if ret <= 0:
                break
            user32.TranslateMessage(ctypes.byref(msg))
            user32.DispatchMessageW(ctypes.byref(msg))

        try:
            user32.RemoveClipboardFormatListener(self._hwnd)
            user32.DestroyWindow(self._hwnd)
        except Exception:
            pass

    def stop(self):
        if self._thread_id and sys.platform == "win32":
            u32 = self._user32
            if u32 is None:
                import ctypes
                u32 = ctypes.windll.user32
            u32.PostThreadMessageW(
                self._thread_id, self.WM_QUIT, 0, 0
            )


# ---------------------------------------------------------------------------
# SQLite persistence
# ---------------------------------------------------------------------------
SCHEMA = """
CREATE TABLE IF NOT EXISTS downloads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    normalized_url TEXT UNIQUE NOT NULL,
    status TEXT NOT NULL,            -- pending | active | done | failed
    title TEXT,
    filepath TEXT,
    error TEXT,
    added_at TEXT NOT NULL,
    finished_at TEXT
);
CREATE INDEX IF NOT EXISTS idx_status ON downloads(status);
"""


class Store:
    def __init__(self, path: Path):
        self.path = path
        self.lock = threading.Lock()
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.conn.executescript(SCHEMA)
        self.conn.execute("PRAGMA journal_mode=WAL")
        # Recover from a previous hard kill: stuck 'active' -> 'pending'
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

    def enqueue(self, url: str) -> tuple[bool, str]:
        """Return (added, reason). reason in {'queued','duplicate','done'}."""
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

    def claim_next(self) -> tuple[int, str] | None:
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

    def mark_done(self, id_: int, title: str | None, filepath: str | None):
        with self._cur() as cur:
            cur.execute(
                "UPDATE downloads SET status='done', title=?, filepath=?, "
                "finished_at=? WHERE id=?",
                (title, filepath,
                 datetime.now().isoformat(timespec="seconds"), id_),
            )

    def mark_failed(self, id_: int, error: str):
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

    def stats(self) -> dict[str, int]:
        with self._cur() as cur:
            rows = cur.execute(
                "SELECT status, COUNT(*) FROM downloads GROUP BY status"
            ).fetchall()
        return {s: c for s, c in rows}

    def pending_preview(self, limit: int = 10) -> list[tuple[int, str]]:
        with self._cur() as cur:
            return cur.execute(
                "SELECT id, url FROM downloads WHERE status='pending' "
                "ORDER BY id ASC LIMIT ?", (limit,)
            ).fetchall()

    def resume_count(self) -> int:
        with self._cur() as cur:
            (n,) = cur.execute(
                "SELECT COUNT(*) FROM downloads WHERE status='pending'"
            ).fetchone()
            return n

    def close(self):
        with self.lock:
            self.conn.close()


# ---------------------------------------------------------------------------
# Downloader (yt-dlp Python API)
# ---------------------------------------------------------------------------
class Downloader:
    def __init__(self, tui: "TUI"):
        self.tui = tui
        self.cookies = parse_cookies_browser(COOKIES_BROWSER)

    def _hook(self, d: dict):
        status = d.get("status")
        info = d.get("info_dict") or {}
        title = info.get("title")
        if status == "downloading":
            self.tui.update_progress(
                downloaded=d.get("downloaded_bytes") or 0,
                total=(d.get("total_bytes")
                       or d.get("total_bytes_estimate") or 0),
                speed=d.get("speed") or 0,
                eta=d.get("eta") or 0,
                filename=d.get("filename") or "",
                title=title,
            )
        elif status == "finished":
            self.tui.finish_progress(d.get("filename") or "", title=title)

    def _opts(self) -> dict:
        opts: dict = {
            "outtmpl": str(OUTPUT_DIR / OUTPUT_TEMPLATE),
            "progress_hooks": [self._hook],
            "download_archive": str(ARCHIVE_PATH),
            "quiet": True,
            "no_warnings": True,
            "noprogress": True,
            "consoletitle": False,
        }
        if self.cookies:
            opts["cookiesfrombrowser"] = self.cookies
        opts.update(EXTRA_YTDLP_OPTS)
        return opts

    def download(self, url: str):
        """Return (ok, title, filepath, error)."""
        try:
            with yt_dlp.YoutubeDL(self._opts()) as ydl:
                info = ydl.extract_info(url, download=True)
            if not info:
                return False, None, None, "no info returned"
            title = info.get("title")
            filepath = None
            rds = info.get("requested_downloads") or []
            if rds:
                filepath = rds[0].get("filepath")
            return True, title, filepath, None
        except yt_dlp.utils.DownloadError as e:
            return False, None, None, str(e)
        except Exception as e:
            return False, None, None, f"{type(e).__name__}: {e}"


# ---------------------------------------------------------------------------
# Rich TUI
# ---------------------------------------------------------------------------
class TUI:
    def __init__(self, store: Store, listener_kind: str):
        self.store = store
        self.console = Console()
        self.lock = threading.Lock()
        self.listener_kind = listener_kind

        self.current_url: str = ""
        self.current_title: str = ""
        self.current_file: str = ""
        self.current_speed: float = 0.0
        self.current_eta: int = 0
        self.current_downloaded: int = 0
        self.current_total: int = 0
        self.last_event: str = "monitoring clipboard…"

    # -- mutators ---------------------------------------------------------
    def set_event(self, msg: str):
        ts = datetime.now().strftime("%H:%M:%S")
        with self.lock:
            self.last_event = f"[dim]{ts}[/] {msg}"

    def start_download(self, url: str):
        with self.lock:
            self.current_url = url
            self.current_title = ""
            self.current_file = ""
            self.current_speed = 0
            self.current_eta = 0
            self.current_downloaded = 0
            self.current_total = 0

    def update_progress(self, downloaded, total, speed, eta, filename,
                        title=None):
        with self.lock:
            self.current_downloaded = downloaded
            self.current_total = total
            self.current_speed = speed
            self.current_eta = eta
            self.current_file = filename
            if title:
                self.current_title = title

    def finish_progress(self, filename, title=None):
        with self.lock:
            self.current_file = filename
            if title:
                self.current_title = title
            if self.current_total:
                self.current_downloaded = self.current_total

    def end_download(self):
        with self.lock:
            self.current_url = ""
            self.current_title = ""
            self.current_file = ""

    # -- render -----------------------------------------------------------
    def _header(self) -> Panel:
        body = Text.from_markup(
            f"[bold]yt-dlp Clipboard Monitor[/]    "
            f"cookies=[cyan]{COOKIES_BROWSER or 'disabled'}[/]    "
            f"clipboard=[cyan]{self.listener_kind}[/]\n"
            f"out=[cyan]{OUTPUT_DIR}[/]    "
            f"state=[cyan]{APP_DIR}[/]\n"
            f"[dim]Copy a URL → queued.  Ctrl+C → finish current & exit.  "
            f"Ctrl+C twice → force-quit.[/]"
        )
        return Panel(body, border_style="cyan", padding=(0, 1))

    def _active(self) -> Panel:
        with self.lock:
            url = self.current_url
            total = self.current_total
            dl = self.current_downloaded
            speed = self.current_speed
            eta = self.current_eta
            fname = self.current_file
            title = self.current_title

        if not url:
            return Panel(
                Align.center(Text("idle — waiting for next URL", style="dim")),
                title="active", border_style="grey42", padding=(0, 1),
            )

        pct = (dl / total * 100) if total else 0
        bar_width = 50
        filled = int(bar_width * pct / 100)
        bar = "█" * filled + "░" * (bar_width - filled)
        size = f"{self._fmt_bytes(dl)} / {self._fmt_bytes(total)}"
        speed_s = self._fmt_speed(speed)
        eta_s = self._fmt_eta(eta)
        short_url = url if len(url) <= 90 else url[:87] + "…"
        label = title or (Path(fname).name if fname else "—")
        body = Text.from_markup(
            f"[bold cyan]{rich_escape(label)}[/]\n"
            f"[dim]{rich_escape(short_url)}[/]\n\n"
            f"[green]{bar}[/]  [bold]{pct:5.1f}%[/]\n"
            f"{size}    [yellow]{speed_s}[/]    ETA [magenta]{eta_s}[/]"
        )
        return Panel(body, title="downloading",
                     border_style="green", padding=(0, 1))

    def _queue(self) -> Panel:
        rows = self.store.pending_preview(limit=10)
        if not rows:
            body = Align.center(Text("queue empty", style="dim"))
            title_str = "queue"
        else:
            t = Table(show_header=True, header_style="bold",
                      box=None, padding=(0, 1), expand=True)
            t.add_column("#", style="dim", width=4)
            t.add_column("url", overflow="ellipsis", no_wrap=True)
            for i, (_id, url) in enumerate(rows, start=1):
                t.add_row(str(i), Text(url, no_wrap=True, overflow="ellipsis"))
            body = t
            title_str = f"queue (showing {len(rows)})"
        return Panel(body, title=title_str,
                     border_style="blue", padding=(0, 1))

    def _stats(self) -> Panel:
        s = self.store.stats()
        with self.lock:
            evt = self.last_event
        line = (
            f"[green]done {s.get('done', 0)}[/]   "
            f"[red]failed {s.get('failed', 0)}[/]   "
            f"[blue]pending {s.get('pending', 0)}[/]   "
            f"[yellow]active {s.get('active', 0)}[/]   "
            f"— {evt}"
        )
        return Panel(Text.from_markup(line),
                     border_style="grey42", padding=(0, 1))

    def render(self) -> Group:
        return Group(self._header(), self._active(),
                     self._queue(), self._stats())

    # -- formatters -------------------------------------------------------
    @staticmethod
    def _fmt_bytes(n: float) -> str:
        if not n:
            return "—"
        n = float(n)
        for unit in ("B", "KB", "MB", "GB", "TB"):
            if n < 1024:
                return f"{n:.1f}{unit}"
            n /= 1024
        return f"{n:.1f}PB"

    @staticmethod
    def _fmt_speed(b: float) -> str:
        if not b:
            return "—"
        return TUI._fmt_bytes(b) + "/s"

    @staticmethod
    def _fmt_eta(s: int) -> str:
        if not s:
            return "—"
        m, s = divmod(int(s), 60)
        h, m = divmod(m, 60)
        return f"{h:d}:{m:02d}:{s:02d}" if h else f"{m:d}:{s:02d}"


# ---------------------------------------------------------------------------
# Worker thread
# ---------------------------------------------------------------------------
class Worker(threading.Thread):
    def __init__(self, store: Store, tui: TUI,
                 downloader: Downloader, stop_evt: threading.Event):
        super().__init__(daemon=True, name="worker")
        self.store = store
        self.tui = tui
        self.dl = downloader
        self.stop_evt = stop_evt
        self.wake = threading.Event()

    def kick(self):
        self.wake.set()

    def run(self):
        while not self.stop_evt.is_set():
            claimed = self.store.claim_next()
            if not claimed:
                self.wake.wait(timeout=2.0)
                self.wake.clear()
                continue
            id_, url = claimed
            self.tui.start_download(url)
            self.tui.set_event(f"downloading {rich_escape(url[:70])}")
            ok, title, filepath, err = self.dl.download(url)
            if ok:
                self.store.mark_done(id_, title, filepath)
                label = title or Path(filepath or "").name or url[:60]
                self.tui.set_event(f"[green]done[/] {rich_escape(label)}")
            else:
                self.store.mark_failed(id_, err or "unknown error")
                first_line = (err or "").splitlines()[0][:100] if err else ""
                self.tui.set_event(
                    f"[red]failed[/] {rich_escape(url[:60])} — "
                    f"{rich_escape(first_line)}"
                )
            self.tui.end_download()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    store = Store(DB_PATH)

    # Clipboard listener: native events on Windows, polling elsewhere.
    clipboard_changed = threading.Event()
    listener: WinClipboardListener | None = None
    listener_kind = "polling"

    if sys.platform == "win32":
        listener = WinClipboardListener(clipboard_changed.set)
        listener.start()
        listener.started_evt.wait(timeout=2.0)
        if listener.failed is not None:
            print(f"clipboard listener failed ({listener.failed}); "
                  f"falling back to polling")
            listener = None
        else:
            listener_kind = "event"

    tui = TUI(store, listener_kind)
    dl = Downloader(tui)
    stop_evt = threading.Event()
    worker = Worker(store, tui, dl, stop_evt)
    worker.start()

    resumed = store.resume_count()
    if resumed:
        tui.set_event(f"resumed {resumed} pending item(s) from previous session")
        worker.kick()

    # --- Signal handling -------------------------------------------------
    # CRITICAL: a signal handler runs synchronously in the MAIN thread,
    # between bytecodes. The main thread briefly holds tui.lock on every
    # render(). v2's handler called tui.set_event() (which takes tui.lock);
    # if Ctrl+C landed during a render, set_event() blocked forever on a
    # non-reentrant lock held by the same thread -> hard hang.
    #
    # So the handler now does the ONLY signal-safe things: flip Events.
    # First Ctrl+C -> graceful drain. Second Ctrl+C -> force-quit.
    def handle_signal(signum, frame):
        if stop_evt.is_set():
            os._exit(130)          # second interrupt: don't wait, just die
        stop_evt.set()
        worker.kick()              # wake the worker so it re-checks stop_evt

    signal.signal(signal.SIGINT, handle_signal)
    try:
        signal.signal(signal.SIGTERM, handle_signal)
    except (ValueError, AttributeError, OSError):
        pass

    last_text = get_clipboard_text().strip()

    with Live(tui.render(), console=tui.console,
              refresh_per_second=4, screen=False) as live:
        while not stop_evt.is_set():
            live.update(tui.render())

            if listener is not None:
                # Event-driven, but we ALSO read on timeout. v2 did
                # `continue` on timeout, so if two clipboard changes raced
                # the dispatcher the second URL could sit unread until the
                # next change. Falling through to a read (deduped by
                # last_text) closes that gap cheaply.
                clipboard_changed.wait(timeout=POLL_INTERVAL)
                clipboard_changed.clear()
            else:
                time.sleep(POLL_INTERVAL)

            text = get_clipboard_text().strip()
            if not text or text == last_text:
                continue
            last_text = text

            if not looks_like_url(text):
                continue

            added, reason = store.enqueue(text)
            short = rich_escape(text[:80])
            if added:
                tui.set_event(f"[blue]queued[/] {short}")
                worker.kick()
            elif reason == "done":
                tui.set_event(f"[dim]already downloaded — skipped {short}[/]")
            else:
                tui.set_event(f"[dim]already in queue — skipped {short}[/]")

    # --- Graceful shutdown (we got here because stop_evt was set) --------
    tui.set_event(
        "shutting down — current download will finish, queue persisted"
    )
    tui.console.print(
        "\n[cyan]Draining…[/] current download will finish, then exit. "
        "[dim](Ctrl+C again to force-quit)[/]"
    )
    worker.kick()
    # Loop the join so the interpreter keeps processing signals — lets a
    # second Ctrl+C reach handle_signal() and force-quit a wedged download.
    while worker.is_alive():
        worker.join(timeout=0.5)

    store.requeue_active()
    if listener is not None:
        listener.stop()
        listener.join(timeout=2)
    store.close()
    print("Later.")


if __name__ == "__main__":
    main()
