---
title: "Media offline in DaVinci Resolve"
uuid: 24ac7554-8626-4444-92ce-816e29865be6
created: 2026-07-05
updated: 2026-07-05
trunk: BLACK
messages: 2
chars: 5004
artifacts: 0
generated_files: 0
tools: []
source: claude.ai-export-2026-08-15
---

# Media offline in DaVinci Resolve

> **Conversation Overview**

The person encountered a "media offline" error in DaVinci Resolve for a file that played correctly in other media players. Claude diagnosed the issue as a codec/format compatibility problem rather than a corrupt file, explaining that Resolve is far more restrictive in what it can decode compared to players like VLC. The conversation covered the main causes of this error: VP9 or AV1 codecs common in YouTube downloads via yt-dlp, 10-bit H.265 footage, variable frame rate content from screen recorders or phones, and unusual audio codecs. Claude noted that free Resolve cannot decode VP9 and has inconsistent HEVC support, while AV1 requires the Studio version plus compatible hardware.

Claude provided an `ffprobe` command to diagnose the exact codec, pixel format, and frame rate consistency of the file, and explained how to interpret the output to identify the root cause. Two quick non-destructive fixes were suggested first: toggling hardware-accelerated decode off in Preferences and clearing the render cache. For transcoding, Claude gave two `ffmpeg` commands — one producing DNxHR HQ in a MOV container for maximum Resolve compatibility, and one using H.264 with constant frame rate enforcement for smaller file sizes. Claude also recommended a yt-dlp format sort flag (`-S "vcodec:h264"`) to prefer H.264 at the download stage and avoid the problem upstream. The person's use of a yt-dlp pipeline was noted as a likely source of VP9/AV1 files entering their editing workflow.

---
## 🧑 Papi  <sub>2026-07-05 01:01:21</sub>

media offline but file is valid and plays davinci resolve

---

## 🤖 Claude  <sub>2026-07-05 01:02:22</sub>

The user's hitting a "media offline" error in DaVinci Resolve even though the file plays fine — this is usually a codec or frame rate mismatch issue. Since this is a common troubleshooting problem with established solutions, I can work through the likely causes without needing to search.

The main culprits are unsupported codecs (especially 10-bit H.265 in the free version, or variable frame rate footage from OBS and phone recordings), audio codec incompatibility on certain systems, file relinking issues, corrupted render cache, GPU decode problems, or free vs Studio version limitations with certain formats. I'll walk through these systematically so Papi can identify which one applies to their situation. Writing ffmpeg commands...

The real issue here is likely that Papi's yt-dlp downloads are coming through as VP9 or AV1 codec in webm or mp4 containers — codecs that Resolve's free version either doesn't support at all or has very limited support for. That would explain why the file plays fine in VLC but shows offline in Resolve, since VLC handles those formats natively while Resolve can't decode them. Given their setup with ytdlp_go.py, they're probably hitting VP9 or AV1 files regularly, which is a very plausible cause for this exact problem. The main culprits are VP9/AV1 codecs (especially from YouTube downloads), 10-bit H.265 from cameras, variable frame rate from screen recordings or phones, or occasionally weird audio codecs. I'd have them run ffprobe to check the codec name, pixel format, and frame rate consistency — if the frame rate differs between r_frame_rate and avg_frame_rate, that's VFR and Resolve won't touch it. Before transcoding, worth trying a quick toggle of hardware acceleration in Preferences and clearing the render cache. If those don't work, I'm describing a transcode command that converts to DNxHD in a MOV container, which Resolve handles smoothly even if it creates larger files.

For smaller output, there's an H.264 option with constant frame rate enforcement that also fixes VFR issues. If the file came from yt-dlp, they could prevent this upstream by adding a format preference flag to grab H.264 instead of VP9 — that's worth mentioning if they're using a downloader with a format ladder. I'm double-checking the ffmpeg syntax: DNxHR with yuv422p pixel format and PCM audio in MOV is correct, and for VFR the newer `-fps_mode cfr` flag handles constant frame rate conversion properly.

I can also show a quick ffprobe command to inspect the actual codec and frame rate properties. One other thing worth mentioning: if a clip plays fine in the media pool but shows offline in the timeline, that's usually a conform or relink issue rather than a codec problem. On the HEVC side, I need to be careful about what free Resolve actually supports on Windows — 10-bit 4:2:2 HEVC is definitely Studio-only, but the free version's HEVC decode support on Windows is inconsistent, so I should phrase that cautiously.Classic Resolve gotcha — "plays in VLC" doesn't mean much, because VLC decodes basically everything while Resolve is picky. Media Offline on a valid file is almost always a codec/format Resolve can't decode, not a broken file. The usual suspects:

- **VP9 or AV1** — anything pulled from YouTube via yt-dlp is often VP9/AV1 in .webm or .mp4. Free Resolve can't decode VP9 at all, and AV1 is Studio + hardware dependent.
- **10-bit 4:2:2 H.265** — mirrorless/camera footage. Studio-only. HEVC support in free Resolve is spotty in general.
- **Variable frame rate** — OBS screen recordings and phone clips. Resolve hates VFR; sometimes it's offline, sometimes it drifts out of sync.
- **Weird audio codec** — rarer, but a bad audio stream can knock the whole clip offline.

Since you've got ffmpeg, diagnose it in 10 seconds:

```
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,pix_fmt,r_frame_rate,avg_frame_rate -of default=noprint_wrappers=1 "file.mp4"
```

If `codec_name` says vp9/av1, or `pix_fmt` says `yuv422p10le`, or `r_frame_rate` ≠ `avg_frame_rate` (that's VFR) — found it.

Two quick things to rule out first: Preferences → Decode Options → toggle hardware accelerated decode off and restart (GPU decode bugs cause phantom offline media), and Playback → Delete Render Cache → All. If it's offline in the media pool itself, right-click → Relink in case the path shifted.

The universal fix is transcoding to something Resolve loves:

```
ffmpeg -i input.webm -c:v dnxhd -profile:v dnxhr_hq -pix_fmt yuv422p -c:a pcm_s16le output.mov
```

Big files, but scrubs like butter. Smaller option that also kills VFR: `-c:v libx264 -crf 16 -r 30 -fps_mode cfr -c:a aac output.mp4`.

And if this file came out of your ytdlp pipeline — worth adding `-S "vcodec:h264"` to the format sort so it prefers avc1 and you never land VP9/AV1 in the edit bay to begin with.