---
original_path: "/mnt/user-data/outputs/ytdlp_clipboard_queue.py"
source_conversation: "Python script authentication for video downloads"
created: 2026-04-10
trunk: ORANGE
kind: generated-file
---

"""
yt-dlp Quick Downloader — Clipboard Monitor + Download Queue
=============================================================
Copy URLs as fast as you want. They queue up and download one by one.
No typing. No Enter key. No waiting between copies.

Requirements:  pip install pyperclip  (not needed on Windows)
               yt-dlp in PATH (choco install yt-dlp -y)

Controls:
  - Copy any URL → queued instantly, downloads in order
  - Ctrl+C in terminal → finishes current download, then exits
"""

import os
import shutil
import subprocess
import sys
import time
import re
import threading
import queue
from datetime import datetime

# ---------------------------------------------------------------------------
# CONFIG — edit these to taste
# ---------------------------------------------------------------------------
# Which browser to pull cookies from. Set to None to disable cookies entirely.
#
# Examples:
#   "firefox"                          → default Firefox profile
#   "firefox:default-release"          → specific Firefox profile by name
#   "firefox:/path/to/profile"         → specific Firefox profile by path
#   "firefox::container_name"          → Firefox Multi-Account Container
#   "chrome"                           → default Chrome profile
#   "brave"                            → Brave
#   "edge"                             → Edge
#   None                               → no cookies
COOKIES_BROWSER: str | None = "firefox"

# Output filename template. This keeps filenames sane on Windows where
# URL query params (?, &) are illegal in filenames.
# See: https://github.com/yt-dlp/yt-dlp#output-template
OUTPUT_TEMPLATE: str = "%(title,id)s.%(ext)s"

# Extra yt-dlp args applied to every download. Add format selectors,
# rate limits, etc. here.
EXTRA_YTDLP_ARGS: list[str] = [
    # "-f", "bv*+ba/b",
    # "--limit-rate", "5M",
]

# ---------------------------------------------------------------------------
# Clipboard backend
# ---------------------------------------------------------------------------
CLIPBOARD_BACKEND = None

try:
    import pyperclip
    CLIPBOARD_BACKEND = "pyperclip"
except ImportError:
    if sys.platform == "win32":
        CLIPBOARD_BACKEND = "win32"
    else:
        print("ERROR: Install pyperclip first:  pip install pyperclip")
        sys.exit(1)


def get_clipboard() -> str:
    try:
        if CLIPBOARD_BACKEND == "pyperclip":
            return pyperclip.paste() or ""
        if CLIPBOARD_BACKEND == "win32":
            import ctypes
            CF_UNICODETEXT = 13
            user32 = ctypes.windll.user32
            kernel32 = ctypes.windll.kernel32
            if not user32.OpenClipboard(0):
                return ""
            try:
                handle = user32.GetClipboardData(CF_UNICODETEXT)
                if not handle:
                    return ""
                kernel32.GlobalLock.restype = ctypes.c_wchar_p
                data = kernel32.GlobalLock(handle)
                result = str(data) if data else ""
                kernel32.GlobalUnlock(handle)
                return result
            finally:
                user32.CloseClipboard()
    except Exception:
        return ""
    return ""


# ---------------------------------------------------------------------------
# URL detection
# ---------------------------------------------------------------------------
URL_PATTERN = re.compile(
    r"https?://"
    r"[^\s<>\"'\]\)]{4,}",
    re.IGNORECASE,
)

def looks_like_url(text: str) -> bool:
    return bool(URL_PATTERN.fullmatch(text.strip()))


# ---------------------------------------------------------------------------
# yt-dlp helpers
# ---------------------------------------------------------------------------
def clear():
    os.system("cls" if sys.platform == "win32" else "clear")

def check_yt_dlp():
    if shutil.which("yt-dlp") is None:
        print("ERROR: yt-dlp not found in PATH.")
        print("Install it:  choco install yt-dlp -y")
        sys.exit(1)

def update_yt_dlp():
    print("Checking for yt-dlp updates...")
    if shutil.which("choco"):
        subprocess.run(["choco", "upgrade", "yt-dlp", "-y"])
    else:
        subprocess.run(["yt-dlp", "-U"])
    print()


def build_ytdlp_cmd(url: str) -> list[str]:
    """Assemble the yt-dlp command with cookies + extra args."""
    cmd = ["yt-dlp"]
    if COOKIES_BROWSER:
        cmd += ["--cookies-from-browser", COOKIES_BROWSER]
    cmd += ["-o", OUTPUT_TEMPLATE]
    cmd += EXTRA_YTDLP_ARGS
    cmd.append(url)
    return cmd


# ---------------------------------------------------------------------------
# Download queue + worker thread
# ---------------------------------------------------------------------------
dl_queue: queue.Queue[str | None] = queue.Queue()   # None = shutdown signal
stats = {"completed": 0, "failed": 0, "active": ""}
stats_lock = threading.Lock()


def status_line() -> str:
    """One-liner showing queue state."""
    with stats_lock:
        pending = dl_queue.qsize()
        parts = [
            f"Done: {stats['completed']}",
            f"Failed: {stats['failed']}",
            f"Queued: {pending}",
        ]
        if stats["active"]:
            url = stats["active"]
            if len(url) > 60:
                url = url[:57] + "..."
            parts.append(f"Now: {url}")
        return "  |  ".join(parts)


def download_worker():
    """
    Runs in a background thread. Pulls URLs off the queue and downloads
    them sequentially. Exits when it receives None.
    """
    while True:
        url = dl_queue.get()
        if url is None:
            dl_queue.task_done()
            break

        with stats_lock:
            stats["active"] = url

        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"\n{'='*55}")
        print(f"  [{timestamp}]  STARTING DOWNLOAD")
        short_url = url if len(url) <= 120 else url[:117] + "..."
        print(f"  {short_url}")
        if COOKIES_BROWSER:
            print(f"  (using cookies from: {COOKIES_BROWSER})")
        print(f"{'='*55}\n")

        try:
            cmd = build_ytdlp_cmd(url)
            # IMPORTANT: shell=False (the default) so that & in URLs
            # is NOT interpreted as a command separator by cmd.exe
            result = subprocess.run(cmd)
            with stats_lock:
                if result.returncode == 0:
                    stats["completed"] += 1
                else:
                    stats["failed"] += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            with stats_lock:
                stats["failed"] += 1

        with stats_lock:
            stats["active"] = ""

        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"\n  [{timestamp}]  DONE  —  {status_line()}")
        print(f"  Monitoring clipboard... keep copying links.\n")

        dl_queue.task_done()


# ---------------------------------------------------------------------------
# Clipboard monitor (main thread)
# ---------------------------------------------------------------------------
POLL_INTERVAL = 0.4

def main():
    clear()
    print("╔══════════════════════════════════════════════════════╗")
    print("║   yt-dlp Clipboard Monitor + Queue                  ║")
    print("║                                                      ║")
    print("║   Copy URLs as fast as you want — they queue up     ║")
    print("║   and download one after another automatically.     ║")
    print("║                                                      ║")
    print("║   Ctrl+C to quit                                    ║")
    print("╚══════════════════════════════════════════════════════╝\n")

    if COOKIES_BROWSER:
        print(f"  Cookies: {COOKIES_BROWSER}")
    else:
        print("  Cookies: disabled")
    print(f"  Output:  {OUTPUT_TEMPLATE}")
    print()

    check_yt_dlp()
    update_yt_dlp()

    # Start the download worker thread
    worker = threading.Thread(target=download_worker, daemon=True)
    worker.start()

    seen: set[str] = set()
    last_clip = get_clipboard().strip()
    seen.add(last_clip)

    print("Monitoring clipboard... just copy a URL.\n")

    try:
        while True:
            time.sleep(POLL_INTERVAL)
            clip = get_clipboard().strip()

            if clip == last_clip or clip in seen:
                continue

            last_clip = clip

            if looks_like_url(clip):
                seen.add(clip)
                dl_queue.put(clip)
                pending = dl_queue.qsize()
                timestamp = datetime.now().strftime("%H:%M:%S")
                print(f"  [{timestamp}]  QUEUED ({pending} waiting): {clip[:80]}")

    except KeyboardInterrupt:
        print("\n\nShutting down... finishing current download.")
        dl_queue.put(None)     # tell worker to stop after current job
        worker.join(timeout=5)
        print(f"\nSession stats — {status_line()}")
        print("Later.\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
