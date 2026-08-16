---
title: "One-handed script optimization for link copying"
uuid: 9a9f533f-a30c-458f-9949-422f09516694
created: 2026-03-08
updated: 2026-03-08
trunk: BOTH
messages: 8
chars: 10022
artifacts: 0
generated_files: 4
tools: [bash_tool, create_file, present_files, str_replace, view]
source: claude.ai-export-2026-08-15
---

# One-handed script optimization for link copying

> **Conversation Overview**

The person asked Claude to help build and iteratively improve a Python automation script for downloading media using yt-dlp. They explicitly stated they wanted to minimize keyboard interaction and optimize for one-handed mouse operation, preferring to simply copy URLs to the clipboard rather than typing or pressing Enter repeatedly.

Claude built the script in three progressive iterations. The first version introduced clipboard monitoring using a polling loop (checking every 0.4 seconds) with a Windows-native ctypes fallback for clipboard access, eliminating all keyboard input. The second version added a threaded download queue using Python's `queue.Queue` and `threading.Thread`, so URLs copied while a download is in progress stack up and process sequentially — the person explicitly requested this after seeing the first version. The third and final version integrated `gallery-dl` alongside `yt-dlp`, adding automatic URL classification that routes direct image links and known image/gallery domains (imgur, reddit, pixiv, danbooru, gelbooru, rule34, e621, kemono, twitter image links, and others) to `gallery-dl`, known video platforms to `yt-dlp`, and unknown domains to an auto-fallback strategy that tries `gallery-dl` first then `yt-dlp`.

The person also requested custom ASCII art branding for the splash screen and specified the program be named **GOON+PASTE**. The final script includes configurable `VIDEO_DIR` and `IMAGE_DIR` output paths, per-session stats tracking images and videos separately, timestamped queue status lines, and a graceful Ctrl+C shutdown that finishes the active download before exiting. All functionality is designed around zero keyboard interaction after launch.

**Files produced**

- [ytdlp_go.py](../files/2026-03-08_ytdlp-gopy.md)
- [ytdlp_go.py](../files/2026-03-08_ytdlp-gopy-2.md)
- [ytdlp_go.py](../files/2026-03-08_ytdlp-gopy-3.md)
- [goon_paste.py](../files/2026-03-08_goon-pastepy.md)

---
## 🧑 Papi  <sub>2026-03-08 21:07:14</sub>

I need you to take this script and make it more efficient. I want to be able to minimise clicks to easily copy and paste the link into the script without having to constantly press enter all the time. also i'm gooning at the same time so my left hand is preoccupied. best to optimize for one handed mouse operation what say you?

---

## 🤖 Claude  <sub>2026-03-08 21:08:06</sub>

The user wants to optimize their yt-dlp script for easier one-handed operation, minimizing keyboard interaction. They want to be able to paste URLs and start downloads with minimal keypresses.

Let me think about practical improvements:

1. Clipboard monitoring - automatically detect when a URL is copied to clipboard and start downloading
2. Remove the "press enter to continue" prompts
3. Auto-detect URLs from clipboard so they don't need to type anything

Let me build a version that monitors the clipboard for new URLs and auto-downloads them. This way they just need to copy a link and it starts downloading automatically.

I should keep this professional and just focus on the UX optimization.Say less. Clipboard monitoring is the move here — zero typing, zero enter keys. Just copy a URL and it auto-downloads.

Let me build it out.
```
This block is not supported on your current device yet.
```

This is just a Python script, no special skill needed. Let me create the optimized version.
```
This block is not supported on your current device yet.
```

Done. Let me present it.
```
This block is not supported on your current device yet.
```

Done.Here's what changed and why it's better for your workflow:

**Zero keyboard interaction.** The script monitors your clipboard every 0.4 seconds. Copy a URL from your browser → it detects the new clipboard content → auto-starts the download. No pasting, no Enter key, nothing. Just right-click → Copy (or Ctrl+C with whatever hand is free).

**Key improvements over the original:**

- **Clipboard polling loop** replaces the manual input prompt. It tracks what it's already seen so it won't re-download the same link.
- **URL validation** via regex so it ignores random text you copy (only triggers on `http://` or `https://` links).
- **No pyperclip hard dependency on Windows** — it falls back to native ctypes clipboard access, so zero pip installs needed if you're on Windows.
- **Clean Ctrl+C exit** instead of typing "exit."
- **Cross-platform `shell=True`** only set on Windows where it's actually needed.

**Setup:** If you're not on Windows, run `pip install pyperclip` once. Otherwise it just works out of the box. Launch it, minimize it to the taskbar, and just keep copying links.

---

## 🧑 Papi  <sub>2026-03-08 21:08:36</sub>

ok actually. one more thing. is it possible for it to queue downloasd? lets say one is taking longer, can you create a thing which just auto downloads in a row and shit you get what i'm saying?

---

## 🤖 Claude  <sub>2026-03-08 21:09:39</sub>

The user wants a download queue system - so if they copy multiple URLs while one is still downloading, they get queued up and processed sequentially. I'll use threading: one thread monitors clipboard and adds to a queue, another thread pulls from the queue and downloads.Yeah, threading with a queue. Clipboard keeps feeding URLs in, a worker thread chews through them one by one. No downloads lost even if you're copying links faster than they finish.
```
This block is not supported on your current device yet.
```

Need to overwrite.
```
This block is not supported on your current device yet.
```

Now recreate.
```
This block is not supported on your current device yet.
```

Done.
```
This block is not supported on your current device yet.
```

Done, let me explain what's new.Here's what's new:

**The queue system** uses two threads. The main thread watches your clipboard and instantly pushes any new URL into a `queue.Queue`. A separate worker thread pulls from that queue and downloads one at a time, sequentially. So you can copy 10 links in 30 seconds while the first one is still going — they all stack up and process in order.

**What you'll see in the terminal:**

```
  [14:32:01]  QUEUED (1 waiting): https://example.com/video1
  [14:32:03]  QUEUED (2 waiting): https://example.com/video2
  [14:32:05]  QUEUED (3 waiting): https://example.com/video3

  =======================================================
    [14:32:01]  STARTING DOWNLOAD
    https://example.com/video1
  =======================================================

    [14:33:45]  DONE  —  Done: 1  |  Failed: 0  |  Queued: 2
    Monitoring clipboard... keep copying links.
```

**Other details:** duplicate URLs are tracked in a `seen` set so you won't accidentally re-download something if you copy the same link twice. On Ctrl+C it finishes the current download gracefully and prints session stats before exiting.

---

## 🧑 Papi  <sub>2026-03-08 21:27:43</sub>

cool but for fun sake, ca you make the beginning splash thing include this ascii? ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠋⠉⠙⠻⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿
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

and can the name of the script/program be called GOON+PASTE?

---

## 🤖 Claude  <sub>2026-03-08 21:28:31</sub>

Lol okay, let me just swap out the splash screen.
```
This block is not supported on your current device yet.
```

Let me update the docstring and the splash screen.
```
This block is not supported on your current device yet.
```

Now let me replace the splash screen section.Now the splash screen:
```
This block is not supported on your current device yet.
```

Let me replace the splash screen with the ASCII art.
```
This block is not supported on your current device yet.
```

Now rename the file too.
```
This block is not supported on your current device yet.
```

Let me verify the final file looks good.
```
This block is not supported on your current device yet.
```

Done.GOON+PASTE is ready. Launch it with `python goon_paste.py` and you'll get hit with the full splash art before it starts monitoring. Same functionality as before — just more personality on boot.

---

## 🧑 Papi  <sub>2026-03-08 21:47:18</sub>

can you create a similar one or the ability to download imgs too? the most quick and efficient way but for imgs. either an add on to goon paste or a whole nother thing whatever you think is best

---

## 🤖 Claude  <sub>2026-03-08 21:49:00</sub>

The user wants image downloading capability. Let me think about the best approach.

For images, the workflow is different from video - you're typically right-clicking and copying image URLs, or copying page URLs that contain images. The most efficient approach would be to build it into GOON+PASTE since the clipboard monitoring infrastructure is already there. I can detect whether a URL points to an image (by extension or content-type) and route it differently - images get saved directly via requests/wget, videos go through yt-dlp.

Actually, let me think more carefully. For images:
- Direct image URLs (.jpg, .png, .gif, .webp) - just download the file
- Gallery pages - could use gallery-dl which is like yt-dlp but for images


- Individual page URLs with images - gallery-dl handles this too

gallery-dl is the image equivalent of yt-dlp and supports tons of sites. The cleanest approach is to integrate it into GOON+PASTE - detect if it's likely an image or gallery URL and route to gallery-dl, otherwise route to yt-dlp. One script, one clipboard monitor, handles everything. Now I'm building a unified version.Best move is to build it into GOON+PASTE itself. `gallery-dl` is basically yt-dlp but for images — supports all the major sites. The script can auto-detect whether a URL is an image or video and route it to the right tool. One clipboard monitor, handles everything.
```
This block is not supported on your current device yet.
```

Now I'll rebuild the whole file with gallery-dl support integrated. The routing logic:

1. Direct image URLs (.jpg, .png, .gif, .webp, .jpeg) → gallery-dl or just curl/requests
2. Known image/gallery sites (imgur, reddit galleries, pixiv, deviantart, etc.) → gallery-dl
3. Everything else → yt-dlp

gallery-dl also supports cookies from browser, which is great.

Let me also add separate stats for images vs videos so the status line is more informative.
```
This block is not supported on your current device yet.
```

Let me build the unified version.
```
This block is not supported on your current device yet.
```

Done. Let me present it.
```
This block is not supported on your current device yet.
```

Done.All-in-one now. Here's how the routing works:

**Auto-classification** — every URL you copy gets categorized before it hits the queue:

- **IMG** — direct image links (.jpg, .png, .gif, .webp, etc.) and known gallery/image sites (imgur, reddit, pixiv, deviantart, gelbooru, danbooru, rule34, e621, kemono, nhentai, tumblr, twitter/x image links, and a bunch more) all route to `gallery-dl`.
- **VID** — YouTube, Twitch, Vimeo, Kick, Streamable, etc. route to `yt-dlp`.
- **AUTO** — unknown domains try `gallery-dl` first (it fails fast on unsupported sites), then fall back to `yt-dlp`. So nothing gets missed.

**Setup** — just one extra install alongside yt-dlp:

```
choco install gallery-dl -y
```

or `pip install gallery-dl`. The script checks for both tools on launch and warns you if one is missing (but still works with whatever you have).

**Status line** now tracks images and videos separately so you can see your session stats at a glance. You can also set `VIDEO_DIR` and `IMAGE_DIR` at the top of the script if you want them sorted into different folders.