---
original_path: "/mnt/user-data/outputs/goon_paste.py"
source_conversation: "One-handed script optimization for link copying"
created: 2026-03-08
trunk: BOTH
kind: generated-file
---

"""
GOON+PASTE — Clipboard Monitor + Download Queue (Videos + Images)
==================================================================
Copy any URL. Script auto-detects whether it's a video or image/gallery
and routes to yt-dlp or gallery-dl accordingly. Everything queues up.

Requirements:
  yt-dlp      →  choco install yt-dlp -y       (or pip install yt-dlp)
  gallery-dl  →  choco install gallery-dl -y    (or pip install gallery-dl)
  pyperclip   →  pip install pyperclip          (not needed on Windows)

Controls:
  - Copy any URL → auto-queued, auto-routed, auto-downloaded
  - Ctrl+C → finishes current download, then exits
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
from pathlib import Path

# ---------------------------------------------------------------------------
# Config — tweak these to taste
# ---------------------------------------------------------------------------
POLL_INTERVAL    = 0.4       # seconds between clipboard checks
BROWSER_COOKIES  = "firefox" # browser to pull cookies from (firefox/chrome/etc)
SHELL_FLAG       = sys.platform == "win32"

# Download directories (set to None to use current working directory)
VIDEO_DIR = None   # e.g. r"C:\Downloads\Videos"
IMAGE_DIR = None   # e.g. r"C:\Downloads\Images"

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
# URL detection + routing
# ---------------------------------------------------------------------------
URL_PATTERN = re.compile(
    r"https?://[^\s<>\"'\]\)]{4,}",
    re.IGNORECASE,
)

# File extensions that are definitely images
IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg", ".tiff", ".avif",
}

# Domains / patterns where gallery-dl is the right tool.
# gallery-dl supports 100+ sites; these are the heavy hitters.
# For anything not matched here, we try gallery-dl first and fall back to yt-dlp.
GALLERY_DOMAINS = {
    "imgur.com", "i.imgur.com",
    "reddit.com", "www.reddit.com", "i.redd.it", "preview.redd.it",
    "pixiv.net", "www.pixiv.net", "i.pximg.net",
    "deviantart.com", "www.deviantart.com",
    "artstation.com", "www.artstation.com",
    "danbooru.donmai.us",
    "gelbooru.com", "www.gelbooru.com",
    "rule34.xxx", "www.rule34.xxx",
    "e621.net", "e926.net",
    "sankaku", "chan.sankakucomplex.com",
    "konachan.com", "konachan.net",
    "yande.re",
    "flickr.com", "www.flickr.com",
    "tumblr.com",
    "instagram.com", "www.instagram.com",
    "pinterest.com", "www.pinterest.com",
    "twitter.com", "x.com", "pbs.twimg.com",
    "catbox.moe", "files.catbox.moe",
    "kemono.su", "coomer.su",
    "nhentai.net", "hitomi.la",
    "mangadex.org",
}

# Domains where yt-dlp is definitely the right call
VIDEO_DOMAINS = {
    "youtube.com", "www.youtube.com", "youtu.be", "m.youtube.com",
    "twitch.tv", "www.twitch.tv", "clips.twitch.tv",
    "vimeo.com", "player.vimeo.com",
    "dailymotion.com", "www.dailymotion.com",
    "streamable.com",
    "kick.com", "www.kick.com",
    "rumble.com",
    "bitchute.com", "www.bitchute.com",
    "odysee.com",
    "crunchyroll.com", "www.crunchyroll.com",
}


def looks_like_url(text: str) -> bool:
    return bool(URL_PATTERN.fullmatch(text.strip()))


def get_domain(url: str) -> str:
    """Extract domain from URL."""
    try:
        from urllib.parse import urlparse
        return urlparse(url).netloc.lower()
    except Exception:
        return ""


def classify_url(url: str) -> str:
    """
    Returns 'image', 'video', or 'auto'.
    'auto' means we try gallery-dl first, fall back to yt-dlp.
    """
    url_lower = url.lower().split("?")[0].split("#")[0]  # strip query/fragment
    domain = get_domain(url)

    # Direct image file link
    ext = Path(url_lower).suffix
    if ext in IMAGE_EXTENSIONS:
        return "image"

    # Known gallery/image site
    for gd in GALLERY_DOMAINS:
        if domain == gd or domain.endswith("." + gd):
            return "image"

    # Known video site
    for vd in VIDEO_DOMAINS:
        if domain == vd or domain.endswith("." + vd):
            return "video"

    # Unknown — try smart detection
    return "auto"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def clear():
    os.system("cls" if sys.platform == "win32" else "clear")


def ts() -> str:
    return datetime.now().strftime("%H:%M:%S")


def check_tools():
    """Check which tools are available."""
    has_ytdlp = shutil.which("yt-dlp") is not None
    has_gdl = shutil.which("gallery-dl") is not None

    if not has_ytdlp and not has_gdl:
        print("ERROR: Neither yt-dlp nor gallery-dl found in PATH.")
        print("  choco install yt-dlp -y")
        print("  choco install gallery-dl -y")
        sys.exit(1)

    if not has_ytdlp:
        print("  WARNING: yt-dlp not found — video downloads disabled")
        print("  Install:  choco install yt-dlp -y\n")
    if not has_gdl:
        print("  WARNING: gallery-dl not found — image downloads disabled")
        print("  Install:  choco install gallery-dl -y  (or pip install gallery-dl)\n")

    return has_ytdlp, has_gdl


def update_tools(has_ytdlp: bool, has_gdl: bool):
    print("Checking for updates...")
    choco = shutil.which("choco")
    if choco:
        if has_ytdlp:
            subprocess.run(["choco", "upgrade", "yt-dlp", "-y"],
                           shell=SHELL_FLAG, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if has_gdl:
            subprocess.run(["choco", "upgrade", "gallery-dl", "-y"],
                           shell=SHELL_FLAG, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        if has_ytdlp:
            subprocess.run(["yt-dlp", "-U"],
                           shell=SHELL_FLAG, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if has_gdl:
            subprocess.run(["gallery-dl", "--update"],
                           shell=SHELL_FLAG, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Tools up to date.\n")


# ---------------------------------------------------------------------------
# Download functions
# ---------------------------------------------------------------------------
def run_gallery_dl(url: str) -> int:
    """Run gallery-dl. Returns process return code."""
    cmd = ["gallery-dl", "--cookies-from-browser", BROWSER_COOKIES]
    if IMAGE_DIR:
        cmd += ["-d", IMAGE_DIR]
    cmd.append(url)
    result = subprocess.run(cmd, shell=SHELL_FLAG)
    return result.returncode


def run_yt_dlp(url: str) -> int:
    """Run yt-dlp. Returns process return code."""
    cmd = ["yt-dlp", "--cookies-from-browser", BROWSER_COOKIES]
    if VIDEO_DIR:
        cmd += ["-o", os.path.join(VIDEO_DIR, "%(title)s.%(ext)s")]
    cmd.append(url)
    result = subprocess.run(cmd, shell=SHELL_FLAG)
    return result.returncode


# ---------------------------------------------------------------------------
# Download queue + worker thread
# ---------------------------------------------------------------------------
dl_queue: queue.Queue[str | None] = queue.Queue()
stats = {"vid_ok": 0, "img_ok": 0, "failed": 0, "active": "", "mode": ""}
stats_lock = threading.Lock()
HAS_YTDLP = False
HAS_GDL = False


def status_line() -> str:
    with stats_lock:
        pending = dl_queue.qsize()
        parts = [
            f"Vid: {stats['vid_ok']}",
            f"Img: {stats['img_ok']}",
            f"Fail: {stats['failed']}",
            f"Queue: {pending}",
        ]
        if stats["active"]:
            url = stats["active"]
            if len(url) > 50:
                url = url[:47] + "..."
            mode = stats["mode"].upper()
            parts.append(f"{mode}: {url}")
        return "  |  ".join(parts)


def download_worker():
    """Worker thread: pulls URLs, classifies, routes to correct tool."""
    while True:
        url = dl_queue.get()
        if url is None:
            dl_queue.task_done()
            break

        category = classify_url(url)

        with stats_lock:
            stats["active"] = url
            stats["mode"] = category

        label = {"image": "IMG", "video": "VID", "auto": "AUTO"}.get(category, "???")
        print(f"\n{'='*55}")
        print(f"  [{ts()}]  [{label}] STARTING DOWNLOAD")
        print(f"  {url}")
        print(f"{'='*55}\n")

        success = False
        used_tool = ""

        try:
            if category == "image" and HAS_GDL:
                rc = run_gallery_dl(url)
                success = rc == 0
                used_tool = "gallery-dl"

            elif category == "video" and HAS_YTDLP:
                rc = run_yt_dlp(url)
                success = rc == 0
                used_tool = "yt-dlp"

            elif category == "auto":
                # Try gallery-dl first (fast fail on non-supported sites),
                # then fall back to yt-dlp
                if HAS_GDL:
                    rc = run_gallery_dl(url)
                    if rc == 0:
                        success = True
                        used_tool = "gallery-dl"

                if not success and HAS_YTDLP:
                    print(f"  [{ts()}]  gallery-dl didn't grab it, trying yt-dlp...")
                    rc = run_yt_dlp(url)
                    success = rc == 0
                    used_tool = "yt-dlp"

            else:
                # Missing the preferred tool, try the other one
                if HAS_GDL:
                    rc = run_gallery_dl(url)
                    success = rc == 0
                    used_tool = "gallery-dl"
                if not success and HAS_YTDLP:
                    rc = run_yt_dlp(url)
                    success = rc == 0
                    used_tool = "yt-dlp"

        except Exception as e:
            print(f"  ERROR: {e}")

        with stats_lock:
            if success:
                if used_tool == "gallery-dl":
                    stats["img_ok"] += 1
                else:
                    stats["vid_ok"] += 1
            else:
                stats["failed"] += 1
            stats["active"] = ""
            stats["mode"] = ""

        icon = "OK" if success else "FAIL"
        print(f"\n  [{ts()}]  [{icon}] via {used_tool or 'n/a'}  —  {status_line()}")
        print(f"  Monitoring clipboard... keep copying links.\n")

        dl_queue.task_done()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    global HAS_YTDLP, HAS_GDL

    clear()
    print(r"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠋⠉⠙⠻⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⣶⣶⣦⣬⢹⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠄⠄⠄⣰⣧⡀⠄⠄⠄⠄⠈⢙⡋⣿⣿⣿⢸⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠰⠼⢯⣿⣿⣦⣄⠄⠄⠄⠈⢡⣿⣿⣿⢸⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠸⠤⠕⠛⠙⠷⣿⡆⠄⠄⠄⣸⣿⣿⡏⣼⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣴⣿⣿⣿⢡⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄⠄⠄⠄⠄⣄⠄⢀⠄⠄⢀⣤⣾⣿⣿⣿⢃⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⣛⣡⣄⣀⠄⠠⢴⣿⣿⡿⣄⣴⣿⣿⣿⣿⣿⢃⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣩⡽⡁⢸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⢃⣿⣿⢟⣿⣿⣿⣿⣿⣮⢫⣿⣿⣿⣿⣿⣟⢿⠃⠄⢻⣿⣿⣿⣿
⣿⣿⣿⣿⡿⣸⠟⣵⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣷⣄⢰⡄⢿⣿⣿⣿
⣿⣿⣿⣿⡇⠏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠹⡎⣿⣿⣿
⣭⣍⠛⠿⠄⢰⠋⡉⠹⣿⣿⣿⣿⣿⣿⠙⣿⣿⣿⣿⣿⣿⡟⢁⠙⡆⢡⣿⣿⣿
⠻⣿⡆⠄⣤⠈⢣⣈⣠⣿⣿⣿⣿⣿⠏⣄⠻⣿⣿⣿⣿⣿⣆⣈⣴⠃⣿⣿⣿⣿
⡀⠈⢿⠄⣿⡇⠄⠙⠿⣿⡿⠿⢋⣥⣾⣿⣷⣌⠻⢿⣿⣿⡿⠟⣡⣾⣿⣿⠿⢋
⠛⠳⠄⢠⣿⠇⠄⣷⡑⢶⣶⢿⣿⣿⣿⣽⣿⣿⣿⣶⣶⡐⣶⣿⠿⠛⣩⡄⠄⢸

   ╔═══════════════════════════════════════════════╗
   ║            G O O N + P A S T E                ║
   ║          videos + images + galleries          ║
   ║                                               ║
   ║   Copy any URL → auto-routed + queued         ║
   ║   yt-dlp for video  |  gallery-dl for images  ║
   ║   Ctrl+C to quit                              ║
   ╚═══════════════════════════════════════════════╝
""")

    HAS_YTDLP, HAS_GDL = check_tools()
    update_tools(HAS_YTDLP, HAS_GDL)

    # Start worker
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
                category = classify_url(clip)
                dl_queue.put(clip)
                pending = dl_queue.qsize()
                label = {"image": "IMG", "video": "VID", "auto": "AUTO"}.get(category, "???")
                print(f"  [{ts()}]  [{label}] QUEUED ({pending} waiting): {clip}")

    except KeyboardInterrupt:
        print("\n\nShutting down... finishing current download.")
        dl_queue.put(None)
        worker.join(timeout=5)
        print(f"\nSession stats — {status_line()}")
        print("Later.\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
