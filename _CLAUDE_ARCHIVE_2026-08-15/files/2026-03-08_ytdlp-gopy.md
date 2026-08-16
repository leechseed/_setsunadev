---
original_path: "/mnt/user-data/outputs/ytdlp_go.py"
source_conversation: "One-handed script optimization for link copying"
created: 2026-03-08
trunk: BOTH
kind: generated-file
---

"""
yt-dlp Quick Downloader — Clipboard Monitor Edition
====================================================
Copy a URL anywhere and it downloads automatically.
No typing. No Enter key. Just Ctrl+C a link and chill.

Requirements:  pip install pyperclip
               yt-dlp in PATH (choco install yt-dlp -y)

Controls (all mouse-friendly via terminal focus):
  - Copy any URL → auto-downloads
  - Ctrl+C in terminal → clean exit
"""

import os
import shutil
import subprocess
import sys
import time
import re

# ---------------------------------------------------------------------------
# Optional: pyperclip for cross-platform clipboard.  On Windows we can fall
# back to a tiny ctypes/powershell call so the user doesn't *need* to pip
# install anything extra.
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
    """Return current clipboard text, empty string on failure."""
    try:
        if CLIPBOARD_BACKEND == "pyperclip":
            return pyperclip.paste() or ""
        if CLIPBOARD_BACKEND == "win32":
            # Fast, no extra deps on Windows
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
    r"https?://"                # scheme
    r"[^\s<>\"'\]\)]{4,}",     # rest of URL (at least a few chars)
    re.IGNORECASE,
)

def looks_like_url(text: str) -> bool:
    """Quick check: does this clipboard content look like a downloadable URL?"""
    text = text.strip()
    return bool(URL_PATTERN.fullmatch(text))


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
        subprocess.run(["choco", "upgrade", "yt-dlp", "-y"], shell=(sys.platform == "win32"))
    else:
        subprocess.run(["yt-dlp", "-U"], shell=(sys.platform == "win32"))
    print()


def download(url: str):
    """Run yt-dlp with Firefox cookies on the given URL."""
    print(f"\n>>> Downloading: {url}\n")
    subprocess.run(
        ["yt-dlp", "--cookies-from-browser", "firefox", url],
        shell=(sys.platform == "win32"),
    )
    print("\n" + "=" * 50)
    print("DOWNLOAD FINISHED — copy another URL to keep going")
    print("=" * 50)


# ---------------------------------------------------------------------------
# Main — clipboard polling loop
# ---------------------------------------------------------------------------
POLL_INTERVAL = 0.4  # seconds between clipboard checks

def main():
    clear()
    print("╔══════════════════════════════════════════════════╗")
    print("║   yt-dlp Clipboard Monitor (Firefox Cookies)    ║")
    print("║                                                  ║")
    print("║   Copy a URL anywhere → auto-downloads here     ║")
    print("║   Ctrl+C in this window to quit                 ║")
    print("╚══════════════════════════════════════════════════╝")

    check_yt_dlp()
    update_yt_dlp()

    seen: set[str] = set()
    last_clip = get_clipboard().strip()
    seen.add(last_clip)          # ignore whatever's on clipboard at launch

    downloading = False
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
                download(clip)
            # silently ignore non-URL clipboard content

    except KeyboardInterrupt:
        print("\n\nExiting. Later.")
        sys.exit(0)


if __name__ == "__main__":
    main()
