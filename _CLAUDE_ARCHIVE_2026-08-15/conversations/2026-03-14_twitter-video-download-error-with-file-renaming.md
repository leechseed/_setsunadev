---
title: "Twitter video download error with file renaming"
uuid: 86a2d82f-b798-4bea-ada4-06c1e7b94a8c
created: 2026-03-14
updated: 2026-03-14
trunk: BOTH
messages: 2
chars: 1866
artifacts: 0
generated_files: 0
tools: []
source: claude.ai-export-2026-08-15
---

# Twitter video download error with file renaming

> **Conversation Overview**

The person encountered an error while using yt-dlp to download a video from Twitter/X (URL: x.com/i/status/1989728928349798890). The error occurred during HLS fragment downloading, specifically a Windows file rename failure where `.part-Frag2.part` could not be renamed to `.part-Frag2`, causing the download to fail after the first fragment. The person appears to be using a clipboard-monitoring tool referred to as "GOON+PASTE" that automates yt-dlp downloads from copied links.

Claude diagnosed the issue as a Windows file locking and rename race condition affecting HLS fragment temporary files, and recommended adding the `--no-part` flag either to the `yt-dlp.conf` configuration file or directly into the script's yt-dlp argument list. This flag bypasses the intermediate `.part` file rename step by writing fragments directly, resolving the race condition.

---
## 🧑 Papi  <sub>2026-03-14 05:49:24</sub>

[twitter] Extracting URL: https://x.com/i/status/1989728928349798890
Extracting cookies from firefox
Extracted 1551 cookies from firefox
[twitter] 1989728928349798890: Downloading GraphQL JSON
[twitter] 1989728928349798890: Downloading m3u8 information
[info] 1989728718294585344: Downloading 1 format(s): hls-3082+hls-audio-128000-Audio
[hlsnative] Downloading m3u8 manifest
[hlsnative] Total fragments: 25
[download] Destination: phatrabbitkiller.com - took him thru there [1989728718294585344].fhls-3082.mp4
[download]   4.3% of ~  26.79MiB at    8.97KiB/s ETA Unknown (frag 1/25)ERROR: Unable to rename file: [WinError 2] The system cannot find the file specified: 'phatrabbitkiller.com - took him thru there [1989728718294585344].fhls-3082.mp4.part-Frag2.part' -> 'phatrabbitkiller.com - took him thru there [1989728718294585344].fhls-3082.mp4.part-Frag2'
[download]   4.0% of ~  28.59MiB at    2.75MiB/s ETA Unknown (frag 2/25)ERROR: Unable to download video: [Errno 2] No such file or directory: 'phatrabbitkiller.com - took him thru there [1989728718294585344].fhls-3082.mp4.part-Frag2'
  [01:48:43]  DONE  —  Done: 0  |  Failed: 1  |  Queued: 0
  Monitoring clipboard... keep copying links.

---

## 🤖 Claude  <sub>2026-03-14 05:49:30</sub>

This is the same `.part` file renaming error from the HLS fragment downloader. The fix is to add `--no-part` to your yt-dlp config or command so it skips the `.part` temp file system entirely.

Since you're using GOON+PASTE, add this to your `yt-dlp.conf`:

```
--no-part
```

Or if you want to patch it directly in the script's yt-dlp call, add `"--no-part"` to the args list.

The root cause is a Windows file locking/rename race condition on HLS fragment files — `--no-part` writes fragments directly without the intermediate rename step, which sidesteps it completely.