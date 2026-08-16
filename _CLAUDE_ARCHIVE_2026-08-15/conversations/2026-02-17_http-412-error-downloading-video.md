---
title: "HTTP 412 error downloading video"
uuid: d7d7e9c3-7211-47db-a9ec-193331f32841
created: 2026-02-17
updated: 2026-02-17
trunk: ORANGE
messages: 16
chars: 16071
artifacts: 0
generated_files: 0
tools: []
source: claude.ai-export-2026-08-15
---

# HTTP 412 error downloading video

> **Conversation Overview**

The user encountered technical issues while using yt-dlp to download videos from adult content sites, specifically receiving HTTP 412 "Gone" and 404 "Not Found" errors. Claude helped troubleshoot the problem systematically, first identifying that VPN usage was likely causing IP mismatch issues between the browser session and yt-dlp's download requests. The user was using ExpressVPN, and Claude provided specific instructions for disabling split tunneling in the ExpressVPN client to ensure both browser and command-line tools routed through the same VPN connection.

After resolving the VPN routing issue, the user encountered a new error where yt-dlp couldn't extract video titles. Through verbose debugging output, Claude identified that the user was hitting a geographic content block rather than a technical extraction problem. The site was serving an age verification block page for Florida-based connections due to state legislation. Claude explained that several US states have implemented age verification laws that cause adult content sites to block access entirely from those regions, and recommended connecting the VPN to states without such restrictions like New York, California, Illinois, or Washington for optimal access. The user demonstrated familiarity with command-line tools and was comfortable running diagnostic commands and interpreting technical error messages.

---
## 🧑 Papi  <sub>2026-02-17 11:01:43</sub>

how do i get around this

--- Ready for next URL ---
PASTE URL HERE (or type 'exit'): https://www.pornhub.com/view_video.php?viewkey=65a269469668b
[PornHub] Extracting URL: https://www.pornhub.com/view_video.php?viewkey=65a269469668b
Extracting cookies from firefox
Extracted 2218 cookies from firefox
[PornHub] 65a269469668b: Downloading pc webpage
[PornHub] 65a269469668b: Downloading m3u8 information
WARNING: [PornHub] Failed to download m3u8 information: HTTP Error 412: Gone
[PornHub] 65a269469668b: Downloading m3u8 information
WARNING: [PornHub] Failed to download m3u8 information: HTTP Error 412: Gone
[PornHub] 65a269469668b: Downloading m3u8 information
WARNING: [PornHub] Failed to download m3u8 information: HTTP Error 412: Gone
[PornHub] 65a269469668b: Downloading m3u8 information
WARNING: [PornHub] Failed to download m3u8 information: HTTP Error 412: Gone
[PornHub] 65a269469668b: Downloading JSON metadata
[info] 65a269469668b: Downloading 1 format(s): 1080p
ERROR: unable to download video data: HTTP Error 404: Not Found
==============================
DOWNLOAD FINISHED
Press Enter to clear screen and paste next link...

---

## 🤖 Claude  <sub>2026-02-17 11:01:50</sub>

This looks like a yt-dlp error when trying to download a video. The HTTP 412 and 404 errors suggest the video has likely been **deleted or made private** on the platform — there's not really a way to "get around" a removed video since the content simply doesn't exist on their servers anymore.

If the video is still actually accessible when you visit the URL in your browser, a few things worth trying with yt-dlp:

**Update yt-dlp first** — this is the most common fix for site-specific extraction issues:
```
yt-dlp -U
```
or
```
pip install -U yt-dlp
```

**Try with fresh cookies** — your extracted cookies may be stale:
```
yt-dlp --cookies-from-browser firefox "YOUR_URL"
```

**Force a specific format** instead of letting it auto-select:
```
yt-dlp -f "bestvideo+bestaudio" "YOUR_URL"
```

**Try with a different user agent:**
```
yt-dlp --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" "YOUR_URL"
```

But honestly, if the video loads fine in your browser but yt-dlp still gets 404 on the actual stream segments, the CDN links embedded in the page may be geo-restricted or session-locked in a way that prevents external downloading. In that case, a browser-based screen recorder would be your fallback option.

---

## 🧑 Papi  <sub>2026-02-17 11:04:14</sub>

do you think its cause i'm using a vpn?

---

## 🤖 Claude  <sub>2026-02-17 11:04:22</sub>

Yes, almost certainly. That's a classic VPN-related issue with video streaming sites.

Here's what's happening: your browser session and cookies were established through one IP/location, but when yt-dlp tries to fetch the actual video stream segments (the m3u8 files), the CDN sees a different or mismatched IP and rejects the request with that 412 "Gone" error. The 404 on the actual video data is likely the same cause.

A few things to try:

**Easiest fix** — just disconnect the VPN and try the download. If the content is accessible in your region without it, that'll likely resolve it immediately.

**If you need the VPN on** — make sure yt-dlp is routing through the same VPN connection as your browser. Sometimes browser traffic goes through the VPN but command line tools use the system's direct connection, or vice versa, depending on your VPN client's split tunneling settings.

**Try re-extracting cookies while on the VPN** so the session tokens match the IP yt-dlp is using.

The m3u8 stream failures are the telltale sign — CDNs are pretty aggressive about matching the session IP to the streaming IP as an anti-hotlinking measure, and VPNs mess with that matching.

---

## 🧑 Papi  <sub>2026-02-17 11:05:39</sub>

ok how od i do this 

If you need the VPN on — make sure yt-dlp is routing through the same VPN connection as your browser. Sometimes browser traffic goes through the VPN but command line tools use the system's direct connection, or vice versa, depending on your VPN client's split tunneling settings.

---

## 🤖 Claude  <sub>2026-02-17 11:05:46</sub>

It depends on your OS and VPN client. What are you working with?

The fix is usually one of two things depending on your setup.

**If your VPN has split tunneling enabled**, that's likely the culprit. Go into your VPN client's settings and either disable split tunneling entirely, or explicitly add your terminal/command prompt to the list of apps that route through the VPN.

**If you're on Windows** and your VPN isn't routing CLI tools, you can check which IP yt-dlp is seeing by running:
```
curl ifconfig.me
```
in your terminal and comparing it to what your browser shows at ifconfig.me. If they're different, your terminal isn't going through the VPN.

**Quick fixes by VPN client:**

- **ProtonVPN, ExpressVPN, NordVPN** — look for "split tunneling" in settings and make sure it's off, or add cmd/terminal to the included apps list
- **WireGuard** — check your config file, the `AllowedIPs` line should be `0.0.0.0/0` to route all traffic through the tunnel
- **OpenVPN** — should route everything by default, but check for a `redirect-gateway` directive in your config

The simplest test is just to temporarily turn off split tunneling if you have it on, run yt-dlp again, and see if that clears it up.

What VPN client are you using?

---

## 🧑 Papi  <sub>2026-02-17 11:05:56</sub>

im using express vpn

---

## 🤖 Claude  <sub>2026-02-17 11:06:03</sub>

With ExpressVPN the fix is straightforward:

**Turn off split tunneling:**

1. Open the ExpressVPN app
2. Click the hamburger menu (≡) in the top left
3. Go to **Options** (Windows) or **Preferences** (Mac)
4. Click the **General** tab
5. Look for **Split Tunneling** and either turn it off entirely, or make sure your terminal app (cmd, PowerShell, Windows Terminal) is set to route **through** the VPN

**Then verify it's working** by running this in your terminal:
```
curl ifconfig.me
```
That should return an IP that matches what ExpressVPN shows as your connected server IP, not your real home IP. If they match, yt-dlp will be routing through the VPN just like your browser.

**One other thing worth checking** — ExpressVPN has a "Use ExpressVPN DNS servers" option. Make sure that's enabled too, otherwise DNS can leak and cause similar issues.

After that just re-run your yt-dlp command and the 412 errors should go away. If it still fails after confirming the IP matches, the next step would be to re-export your browser cookies while connected to the VPN so the session tokens align with the VPN IP.

---

## 🧑 Papi  <sub>2026-02-17 11:12:14</sub>

now im getting this error

PASTE URL HERE (or type 'exit'): https://www.pornhub.com/view_video.php?viewkey=ph5eff4a5884fd9
[PornHub] Extracting URL: https://www.pornhub.com/view_video.php?viewkey=ph5eff4a5884fd9
Extracting cookies from firefox
Extracted 2236 cookies from firefox
[PornHub] ph5eff4a5884fd9: Downloading pc webpage
ERROR: [PornHub] ph5eff4a5884fd9: Unable to extract title; please report this issue on  https://github.com/yt-dlp/yt-dlp/issues?q= , filling out the appropriate issue template. Confirm you are on the latest version using  yt-dlp -U
==============================
DOWNLOAD FINISHED
Press Enter to clear screen and paste next link...

---

## 🤖 Claude  <sub>2026-02-17 11:12:21</sub>

This is a different error — yt-dlp can't parse the page at all, which usually means one of a few things:

**Most likely cause** — PornHub is serving a different page than expected, probably an age verification wall or a login prompt, because your cookies aren't being recognized properly.

**Try these in order:**

1. **Update yt-dlp first** as the error suggests:
```
yt-dlp -U
```

2. **Re-export cookies fresh** — open Firefox, make sure you're logged in and can see the video normally, then run:
```
yt-dlp --cookies-from-browser firefox "URL"
```

3. **Check what page is actually being returned** by adding verbose output:
```
yt-dlp -v --cookies-from-browser firefox "URL"
```
This will show you exactly what yt-dlp is seeing and why it can't extract the title.

4. **Try exporting cookies manually** using a browser extension like "Get cookies.txt LOCALLY", save the file, then run:
```
yt-dlp --cookies cookies.txt "URL"
```

The verbose flag (-v) is the most useful next step — paste what it outputs and it'll tell you exactly what's going wrong. It'll show whether it's hitting a login wall, an age gate, a geo-block, or something else entirely.

---

## 🧑 Papi  <sub>2026-02-17 11:14:08</sub>

here's 3. ➜ yt-dlp -v --cookies-from-browser firefox "https://www.pornhub.com/view_video.php?viewkey=ph62b47f30913b2"
[debug] Command-line config: ['-v', '--cookies-from-browser', 'firefox', 'https://www.pornhub.com/view_video.php?viewkey=ph62b47f30913b2']
[debug] Home config "yt-dlp.conf": ['--cookies-from-browser', 'firefox']
[debug] Encodings: locale cp1252, fs utf-8, pref cp1252, out utf-8, error utf-8, screen utf-8
[debug] yt-dlp version stable@2026.02.04 from yt-dlp/yt-dlp [c677d866d] (win_exe)
[debug] Python 3.10.11 (CPython AMD64 64bit) - Windows-10-10.0.26200-SP0 (OpenSSL 1.1.1t  7 Feb 2023)
[debug] exe versions: ffmpeg 6.0-full_build-www.gyan.dev (setts), ffprobe 6.0-full_build-www.gyan.dev
[debug] Optional libraries: Cryptodome-3.23.0, brotli-1.2.0, certifi-2026.01.04, curl_cffi-0.14.0, mutagen-1.47.0, requests-2.32.5, sqlite3-3.40.1, urllib3-2.6.3, websockets-16.0, yt_dlp_ejs-0.4.0
[debug] JS runtimes: none
[debug] Proxy map: {}
Extracting cookies from firefox
[debug] Extracting cookies from: "C:\Users\U01_LEECHSEED\AppData\Roaming\Mozilla\Firefox\Profiles\pm59j71q.default-release\cookies.sqlite"
[debug] Firefox cookies database version: 17
Extracted 2236 cookies from firefox
[debug] Request Handlers: urllib, requests, websockets, curl_cffi
[debug] Plugin directories: none
[debug] Loaded 1856 extractors
[PornHub] Extracting URL: https://www.pornhub.com/view_video.php?viewkey=ph62b47f30913b2
[PornHub] ph62b47f30913b2: Downloading pc webpage
ERROR: [PornHub] ph62b47f30913b2: Unable to extract title; please report this issue on  https://github.com/yt-dlp/yt-dlp/issues?q= , filling out the appropriate issue template. Confirm you are on the latest version using  yt-dlp -U
  File "yt_dlp\extractor\common.py", line 763, in extract
  File "yt_dlp\extractor\pornhub.py", line 307, in _real_extract
  File "yt_dlp\extractor\common.py", line 1381, in _html_search_regex
  File "yt_dlp\extractor\common.py", line 1345, in _search_regex

here's 4.

 ~\Downloads :: git(master)                                                                           3.11.8 06:13:22
➜ yt-dlp -v --cookies-from-browser firefox "https://www.pornhub.com/view_video.php?viewkey=ph62b47f30913b2"
[debug] Command-line config: ['-v', '--cookies-from-browser', 'firefox', 'https://www.pornhub.com/view_video.php?viewkey=ph62b47f30913b2']
[debug] Home config "yt-dlp.conf": ['--cookies-from-browser', 'firefox']
[debug] Encodings: locale cp1252, fs utf-8, pref cp1252, out utf-8, error utf-8, screen utf-8
[debug] yt-dlp version stable@2026.02.04 from yt-dlp/yt-dlp [c677d866d] (win_exe)
[debug] Python 3.10.11 (CPython AMD64 64bit) - Windows-10-10.0.26200-SP0 (OpenSSL 1.1.1t  7 Feb 2023)
[debug] exe versions: ffmpeg 6.0-full_build-www.gyan.dev (setts), ffprobe 6.0-full_build-www.gyan.dev
[debug] Optional libraries: Cryptodome-3.23.0, brotli-1.2.0, certifi-2026.01.04, curl_cffi-0.14.0, mutagen-1.47.0, requests-2.32.5, sqlite3-3.40.1, urllib3-2.6.3, websockets-16.0, yt_dlp_ejs-0.4.0
[debug] JS runtimes: none
[debug] Proxy map: {}
Extracting cookies from firefox
[debug] Extracting cookies from: "C:\Users\U01_LEECHSEED\AppData\Roaming\Mozilla\Firefox\Profiles\pm59j71q.default-release\cookies.sqlite"
[debug] Firefox cookies database version: 17
Extracted 2236 cookies from firefox
[debug] Request Handlers: urllib, requests, websockets, curl_cffi
[debug] Plugin directories: none
[debug] Loaded 1856 extractors
[PornHub] Extracting URL: https://www.pornhub.com/view_video.php?viewkey=ph62b47f30913b2
[PornHub] ph62b47f30913b2: Downloading pc webpage
ERROR: [PornHub] ph62b47f30913b2: Unable to extract title; please report this issue on  https://github.com/yt-dlp/yt-dlp/issues?q= , filling out the appropriate issue template. Confirm you are on the latest version using  yt-dlp -U
  File "yt_dlp\extractor\common.py", line 763, in extract
  File "yt_dlp\extractor\pornhub.py", line 307, in _real_extract
  File "yt_dlp\extractor\common.py", line 1381, in _html_search_regex
  File "yt_dlp\extractor\common.py", line 1345, in _search_regex

---

## 🤖 Claude  <sub>2026-02-17 11:14:17</sub>

The error is hitting line 307 in yt-dlp's `pornhub.py` extractor, which is the title extraction step. This means it's downloading the page but the HTML structure doesn't match what the extractor expects — classic sign that PornHub changed their page layout and yt-dlp's extractor is outdated.

Notice it says version `2026.02.04` — that's already pretty recent, but PornHub may have changed something even in the last two weeks.

**First thing to try** — check what page is actually being returned by dumping it:

```
yt-dlp --cookies-from-browser firefox --write-pages "URL"
```

This saves the raw HTML yt-dlp is seeing to a file. Open it and check if it's the actual video page or something like an age gate, a CAPTCHA, or a "this content is unavailable in your region" page.

**If it's a region block or age gate**, your VPN country might be the issue. PornHub is blocked or restricted in certain countries — try switching your ExpressVPN server to a US location specifically.

**If the page looks normal**, the extractor is genuinely broken. In that case check the yt-dlp GitHub issues page for recent PornHub-related reports — there's likely already a fix in the nightly build:

```
pip install -U "yt-dlp[default]"
```

This installs from PyPI which sometimes has newer builds than the standalone exe.

What country is your ExpressVPN currently connected to?

---

## 🧑 Papi  <sub>2026-02-17 11:16:21</sub>

here's the dump

---

## 🤖 Claude  <sub>2026-02-17 11:16:28</sub>

There it is — the problem is crystal clear. You're getting the **Florida age verification block**, not a VPN issue at all.

PornHub blocked access from Florida due to the state's age verification law. The page literally says:

> *"we have made the difficult decision to completely disable access to our website in Florida"*

So your VPN is the actual solution here — you just need to switch to a server **outside of Florida**. The site is detecting your VPN exit node is in Florida.

**Fix:**

1. Open ExpressVPN
2. Change your server to any US state other than Florida (New York, Texas, California, etc.) — or any other country entirely
3. Re-run yt-dlp

That should immediately resolve it. The cookies and extraction issues you were seeing earlier were all downstream symptoms of hitting this block page instead of the real video page.

---

## 🧑 Papi  <sub>2026-02-17 11:17:41</sub>

what state city hsa the least restricted porn laws. the best one to proxy to

---

## 🤖 Claude  <sub>2026-02-17 11:17:46</sub>

For VPN purposes to access adult content sites, you'd want to connect to a server in a state that **hasn't passed age verification laws**. As of my knowledge cutoff, states that have passed these laws include Louisiana, Texas, Utah, Virginia, Montana, Arkansas, Mississippi, North Carolina, and Florida among others.

**Best states to connect to:**

- **New York** — no age verification law, major server hub, fast connections
- **California** — no restrictions, tons of server options
- **Illinois** — no law passed
- **Washington** — no restrictions

For ExpressVPN specifically, just pick **New York** or **Los Angeles** — they'll have the most server options and fastest speeds, and neither state has these restrictions in place.

Just switch your ExpressVPN location to one of those and you should be good to go.