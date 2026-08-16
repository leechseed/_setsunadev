---
title: "Adding UI controls to yt-dlp clipboard monitor"
uuid: cb4d9a5d-360e-49c6-97a9-7a1d5393a885
created: 2026-06-10
updated: 2026-06-10
trunk: BLACK
messages: 4
chars: 37420
artifacts: 0
generated_files: 0
tools: [bash_tool, present_files, str_replace, view]
source: claude.ai-export-2026-08-15
---

# Adding UI controls to yt-dlp clipboard monitor

> **Conversation Overview**

The person is working on a Python script called `ytdlp_go.py` — a yt-dlp clipboard monitor with a persistent SQLite queue that downloads URLs automatically as they're copied. The conversation focused on two separate problems: first, the script lacked any interactive hotkey system for common operations; second, some videos were consistently failing with "Requested format is not available" errors (14 failures out of 187 total attempts), and the initial fix only added diagnostics rather than resolving the underlying cause.

For the hotkey system, Claude added a non-blocking `msvcrt`-based key poller (Windows-only, no extra dependencies) riding the existing 0.25-second main loop tick to avoid new threads near the UI lock. Keys added: `u` to pip-upgrade yt-dlp in a background thread, `r` to restart the script in-place via `os.execv` with Windows path-quoting handling, `f` to requeue all failed items back to pending, `e` to open the script in Notepad++ with a fallback path search and plain Notepad as last resort, `c` to copy the script's own source to clipboard using a 64-bit-correct `ctypes` clipboard writer, `o` to open the output folder in Explorer, and `q` for graceful quit. All hotkeys display in the header panel.

For the format failure, the person correctly pointed out that the first fix (adding `_LogCatcher` diagnostics and a retry button) didn't actually prevent the error. Claude then implemented a three-rung retry ladder in `download()`: rung 1 uses default clients, rung 2 rotates to `android`+`web_safari` clients with `bv*+ba/b` format (survives broken JS-runtime sig handling), and rung 3 uses `ios`+`tv`+`web` clients with `b/bv*+ba` (single pre-merged file first, survives missing ffmpeg). Escalation only triggers on format-availability errors and 403s — not on private/deleted/geo-blocked failures. A module-level environment probe was added to detect `ffmpeg` and JS runtimes (`deno`/`node`/`bun`/`quickjs`), surfacing both as colored status fields in the header and as loud startup warnings, since a missing ffmpeg silently downgrades yt-dlp's format selector and a missing JS runtime causes silent format skipping — identified as the two most likely root causes of the 14 failures. The script reached v2.3 across these changes. The person's communication style is direct and casual, and they pushed back immediately when a fix didn't address the actual problem rather than just the symptoms.

---
## 🧑 Papi  <sub>2026-06-10 09:32:21</sub>

how do i bugfix this because there's no like text part or hotkey part whiere i can choose to do shit like that to  update or to restart or to open the python flie in notepad++ and atuo copy the python code to clipboard u know?

Loading personal and system profiles took 616ms.
 ~ :: git(master)                                                                                            05:22:09
➜ python C:\Users\U01_LEECHSEED\Downloads\ytdlp_go.py
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ yt-dlp Clipboard Monitor    cookies=firefox    clipboard=event                                                       │
│ out=C:\Users\U01_LEECHSEED    state=C:\Users\U01_LEECHSEED\.ytdlp_go                                                 │
│ Copy a URL → queued.  Ctrl+C → finish current & exit.  Ctrl+C twice → force-quit.                                    │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────── active ───────────────────────────────────────────────────────╮
│                                             idle — waiting for next URL                                              │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────── queue ────────────────────────────────────────────────────────╮
│                                                     queue empty                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ done 173   failed 14   pending 0   active 0   — 05:23:14 failed https://youtu.be/ufW8YScJyJQ?si=2bWDux2bc_e6pe6H —   │
│ ERROR: [youtube] ufW8YScJyJQ: Requested format is not available. Use --list-formats for a list of av                 │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

---

## 🤖 Claude  <sub>2026-06-10 09:39:49</sub>

Looking at what Papi wants to add to his clipboard-monitoring download tool: interactive hotkeys in the TUI for updating yt-dlp, restarting the script, opening the Python file in Notepad++, and auto-copying the code to clipboard. I also notice there's a truncated error message in the output about a YouTube format request that's getting cut off.

I need to first read the uploaded file to see the current code structure, then check the file-reading skill documentation to understand how to properly access it. The YouTube format error might be related to JavaScript runtime requirements for signature extraction, which was apparently a past issue he fixed.

My plan is to add a hotkey system using `msvcrt` for Windows keyboard detection since he's running this on Windows. I'll implement shortcuts for updating yt-dlp, restarting the script, opening it in an editor, and copying the source code to clipboard. I should also investigate that format resolution error more closely once I see the actual code. I'm thinking through the keypress handling for a Windows console app with Rich Live display. Since Rich doesn't capture input, I can use a background daemon thread that polls for keypresses with msvcrt and dispatches commands like `u` to trigger updates or `q` to quit.

For the `u` command, I'd run the update subprocess and log output to the status line. For `r` (restart), I need to decide between immediate re-execution or graceful shutdown first — since the queue is SQLite-backed, the state persists across restarts, but an active download would be interrupted. I'm leaning toward marking the active download back to pending before restarting to preserve it.

For `e` (edit), I'll check common Notepad++ installation paths and fall back to the default editor if not found. For `c` (copy source), I'm reading the script file and need to implement a clipboard write function using ctypes to handle Unicode text.

The tricky part is that the script already monitors clipboard for URLs, so copying the source code could trigger that listener if the code contains example URLs. I'll need to either add a suppress flag to skip the next clipboard update, or compare the clipboard content to avoid re-triggering the listener when we set it ourselves.

For `h` (help) I'll display the hotkey list, and maybe add `o` (open output folder) since that fits the "do shit like that" vibe.

The header panel should show all available hotkeys in a single line so they're discoverable: update, restart, edit in Notepad++, copy source, and open folder. I should also fix the format fallback — when yt-dlp can't find the requested format, I'll append a `/best` fallback or use a more lenient format selector to handle edge cases. Writing restart logic... Just use `subprocess.run` to execute the file in a blocking way, then exit with its return code — the parent process stays in control of the console, avoiding the prompt interleaving issue, though signal handling gets a bit messy with nested processes.

For the update mechanism, I'll run pip to upgrade yt-dlp and gallery-dl, assuming they're installed via pip since the tool depends on them.  The tricky part is handling Windows file locking — if yt-dlp is running during an update, pip might fail trying to replace the executable, so I'll either queue the update until idle or just let it fail gracefully and show the error. I'll go with the simpler approach: run the update anytime but display any permission errors that occur.

For the clipboard integration, I'm adding a ctypes-based writer to match the existing reader, then setting up an ignore flag so when we copy a URL to the clipboard ourselves, the monitor doesn't immediately re-trigger and create a loop — it'll check if the new clipboard text matches what we just wrote and skip processing if it does.

For opening files, I'm checking for Notepad++ in the standard install paths and falling back to the default association if it's not found. The folder opener just uses the standard file explorer launch. For failed retries, I'll mark them as pending in the state database and let the worker thread pick them up again. The help display can live in the header as a permanent reference instead of toggling it on and off.

Now looking at the format selection issue — the failing video is hitting "Requested format is not available," which typically means either the format selector is too strict for what YouTube actually offers, or the video lacks that format entirely due to being a short, music video, or age-gated content. Since 173 videos succeeded but 14 failed, it's per-video variation. The fix is to make the format selector more flexible by ensuring it falls back to `/best` and adjusting the criteria...

Let me check the actual skill file and script to see what format string is being used. I'll need to view the file in chunks if it's large, then implement the necessary changes and test the syntax. I'm thinking through where to hook the key polling in the main loop — if it's a simple loop that sleeps between clipboard checks, I can just call the polling function there without needing a separate thread, which keeps things simpler and avoids thread-safety headaches with Rich and the database. The msvcrt.kbhit call is non-blocking anyway, so it fits cleanly. Though if the main loop gets blocked waiting on a download subprocess, that might be a different story — need to check how it's actually structured.

Either way, I'll use a daemon thread with proper locking to be safe, mirroring whatever synchronization pattern they're already using for the SQLite queue. Let me just read through the code first to see what I'm working with, then build this out without overthinking it.
```
This block is not supported on your current device yet.
```

 I need to check the file size before reading it—this is the GOON+PASTE script he's been developing.
```
This block is not supported on your current device yet.
```

 I'm looking at a large block of thinking that's too long to process all at once, so I need to read through it in sections to understand what's being worked on.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 I'm seeing the full architecture now—the main loop in `main()` is the right place to poll for keyboard input since it already ticks every quarter second, the worker thread handles downloads independently, and the store already has the SQLite queue with `requeue_active()` for restarts. I'll add the hotkey legend to the TUI header panel, though I notice the format isn't explicitly set yet.

The real issue with that failing video is likely YouTube's 2025/2026 format restrictions—without a JavaScript runtime for signature deciphering, many formats get filtered out entirely, leaving nothing available. Some videos are members-only, age-gated, or region-locked, and this one might fall into that category even though most others work fine. I should build in a mitigation strategy to handle these edge cases gracefully. e approach: instead of chasing yt-dlp version-specific client names, the real fix is encouraging updates and adding a retry mechanism for failed downloads—users can update yt-dlp (which fixes YouTube issues weekly) and then requeue failed items with a hotkey. I'm also considering whether format sorting preferences would help stabilize downloads across different scenarios. The real issue is that suppressing warnings hides diagnostic clues — I should capture them via a logger and append the last warning to failed download errors so he can actually see what went wrong. It's a modest addition that'll likely reveal why those 14 items failed. I'm also thinking about truncating the error display since it's capped at 100 characters, making it hard to debug with that many failures.

For hotkeys, I'll stick to the core set: `u` for update, `r` for restart, `e` for edit, `c` for copy source, `f` to retry failed, `o` to open folder, and `q` to quit gracefully — seven keys total, all displayed in the header. I'm being careful not to add scope creep like dumping failed lists to files, just the essentials he asked for plus the retry and folder navigation features.

On the implementation side, I need to handle key polling in the main loop, which means using `msvcrt` on Windows and gracefully disabling it elsewhere. The keys handler will be a closure inside main that has access to the store, TUI, worker thread, stop event, and other necessary state. Each key maps to an action — `u` spawns a thread to run the update subprocess...

Writing update handler... Completing the restart handler...

The restart function stops the event loop, requeues the active download to resume later, closes the store and listener, stops the live display, then executes a fresh process. There's a potential race where the worker thread marks a download done after we requeue it, but since we're about to exec anyway, any exception in the worker gets swallowed when the process is replaced — acceptable given this mirrors the existing force-quit behavior where active rows resume on the next launch. On Windows, I need to reconstruct the command properly for execv — passing sys.executable as the first argument, then the script path and any remaining arguments, since the first element becomes argv[0] in the new process. There's a potential edge case with paths containing spaces that could cause quoting issues on Windows.

I'm adding a workaround that manually quotes arguments with spaces before calling execv to handle this robustly. Then I'm moving on to the edit command, which opens the script in Notepad++ by searching for the executable.

Adding editor fallback logic... After SetClipboardData succeeds, the system takes ownership of the memory, so I shouldn't free it—only free if the operation fails. For the suppression issue: when clipboard content changes, it triggers an update event that reads the text back, but since the source is multiline, the URL regex fullmatch fails and it gets skipped anyway. The `last_text` variable still gets set to the source, but that's harmless since the event log just silently ignores non-URLs.

For the Windows clipboard path, I'll use SetClipboardData on Windows and fall back to pyperclip.copy on non-Windows systems. The `f` key requeues failed downloads by updating their status back to pending and clearing error info, then kicks the worker—yt-dlp's download archive only records completed videos, so retrying failed ones works fine. The `o` key opens the output folder using the system file explorer.

Now I'm adding a warning catcher to the yt-dlp logger options so I can capture the last warning message and append it to download errors for better diagnostics.

I need to be careful about how much of the error message shows in the event line versus what gets stored in the database — the event line truncates at 100 characters but the database can hold up to 500, so I'll expand the event truncation to around 160 characters to include both the error and any captured warning, while keeping the stats panel display at 100 characters since it's a single line.

Now I'm updating the header to show available hotkeys like update, restart, retry failed, edit, copy source, open folder, and quit — but only when keys are available. I'm setting up the main loop to poll for keyboard input each tick and dispatch the corresponding action.

Writing key polling logic... I'll grab the version string safely using getattr and add it to the header — nice touch for users tracking updates. The docstring needs bumping to v2.2 with a changelog section noting the new hotkeys, keeping that same style he's established. Now I'm planning the file edits: copy the script to outputs and apply changes via string replacement — easier than building from scratch with this many modifications. First I'll update the docstring with the version and changelog, then add the missing imports like subprocess and shutil. no_warnings False to let the logger capture warnings, and keep quiet True so output goes through the logger instead of stdout.

For the main loop, I'm setting up hotkey helpers and dispatch logic after signal handling, then polling for key presses right after rendering. The order is: render, wait for clipboard events with a 0.25s timeout, check for key input, then read clipboard text — key latency up to 0.25s is acceptable. Unmapped keys from `getwch` like '\r' just get ignored silently.

For the update thread, I'm using a state dict to track whether an update is already running and prevent concurrent updates.

Writing update logic... I need to handle the restart key binding — the challenge is that `live` only exists inside the with-block, but I need to pass it to the restart handler. I'll define a context dict before the with-block to hold the live reference, then update it inside and use it in the key handler. Now I'm implementing the restart function that sets an event message.

Writing restart handler... Writing clipboard utility... Finishing the Windows API function signatures...

Now I'm setting up the clipboard operations by opening it, then attempting to allocate and lock global memory to store the clipboard data before closing it. Verifying the memory handling is correct — GlobalLock returns a void pointer that I'm treating as an integer for memmove, which ctypes supports fine for 64-bit systems. Now I'm adding a hotkeys legend to the panel header that shows the keyboard shortcuts for updating yt-dlp, restarting, retrying failed items, and editing. Completing the requeue_failed method to reset failed downloads back to pending status. I'm also adding a LogCatcher class to capture yt-dlp warnings during downloads so we can show users the actual reason for failures instead of generic errors. Adding key handlers...

I need to make sure the keys line only shows on Windows since that's where msvcrt input works, and I'm confident that pressing keys in other windows won't interfere since the console only reads its own input buffer. Now I'll write out the file with all the edits — the docstring update, imports, clipboard function, requeue logic, log catcher changes, header adjustments, and the main loop with key polling. That's roughly nine edits total. I should also update the control hints line and then run a quick compile check to catch any syntax errors.

For the docstring, I'll keep his original voice while explaining the hotkeys and the no_warnings flag. The yt-dlp logger interaction is straightforward — our logger insertion in download() overrides any user-provided one, which is fine, and progress hooks still fire independently of the logger setting so everything gets captured properly.

Now I need to write out the fixed file with the key additions explained: the new hotkeys, what each one does, and the diagnosis for failed downloads — basically that stale yt-dlp needs an update (press u then f), and since warnings are now captured, the failed rows will show the actual error instead of being hidden. I'll keep the explanation tight and casual, maybe add a note about the PowerShell restart quirk where a stray prompt might print but it's harmless.I understand the script structure now. I'll add keyboard polling to the existing main loop using `msvcrt` to create an interactive hotkey layer.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 I need to add a function for setting clipboard text alongside the existing getter, then create a helper to poll for key presses before continuing with the rest of the implementation.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 I'm adding a _LogCatcher class to intercept warnings from yt-dlp, then integrating it into the download() method to capture log output. The key is ensuring no_warnings stays False so the logger.warning calls actually fire.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 Now I'm setting up the hotkey action handlers in main—I'll place the helper functions after signal setup and before initializing last_text, then integrate the polling loop into the Live event loop. The handlers need access to tui, store, worker, stop_evt, and listener, with live passed in from the loop itself. For the update flag I'll use a simple mutable dict, and for restart I need to handle the CPython Windows execv argument quoting workaround.

For the editor detection, I'm checking shutil.which first, then falling back through Program Files locations for both 32-bit and 64-bit installs, checking LOCALAPPDATA for per-user installations, and finally defaulting to notepad.exe if nothing else is found.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 Let me verify the syntax and check that all the imports are properly used—`re` was already there, and now `shutil` and `subprocess` are being added. The `handle_key` function correctly takes `live` as a parameter, so the closure should work fine. I need to double-check the regex pattern in `do_update` that's matching the pip output for the installed package version.
```
This block is not supported on your current device yet.
```

 Checking the syntax and line count — the file grew from 869 to 1219 lines, which looks right. Now I want to trace through the main loop logic to make sure I didn't accidentally break anything in the existing flow.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Done — v2.2. The script now reads single keypresses while it runs (console just needs focus, no Enter required), and the keys show in the header panel:

- **u** — pip-upgrades yt-dlp in a background thread, tells you the new version, prompts you to press r
- **r** — restarts the script in-place (re-exec). Queue survives because it's SQLite; an active download gets re-queued and resumes its `.part`
- **f** — retries all failed items (your 14 → back to pending)
- **e** — opens the .py in Notepad++ (checks PATH, both Program Files, and the per-user LOCALAPPDATA install; falls back to plain Notepad — deliberately *not* `os.startfile`, since the .py association would launch a second instance instead of editing)
- **c** — copies the script's own source to clipboard. No suppression guard needed: your own listener fires, but `looks_like_url()` fullmatches and a 30KB dump isn't a URL, so it's ignored
- **o** — opens the output folder, **q** — graceful quit (same as one Ctrl+C)

Polling rides the existing 0.25s tick in the main loop via `msvcrt.kbhit()`, so no new threads go anywhere near `tui.lock` — your signal-handler deadlock lesson stays intact. The clipboard *writer* follows the same 64-bit ctypes discipline as your reader (restypes declared, OS takes ownership of the HGLOBAL on success, freed on failure).

About those failed downloads: I also fixed a diagnostic blind spot. `quiet` + `no_warnings` was swallowing yt-dlp's warnings, which is exactly where YouTube explains "Requested format is not available" (missing JS runtime, SABR-only formats skipped, etc.). A capture logger now stashes the last warning and appends it to the failed row's error, so the DB tells you *why*. The practical loop for those 14: press **u**, then **r**, then **f** — most "format not available" failures are just yt-dlp being out of date against YouTube's weekly churn; whatever still fails will now have a real reason attached.

One cosmetic quirk: on restart, PowerShell may print a stray prompt line during the process handoff — Windows `exec` doesn't truly replace in-place. Harmless, the UI redraws right over it.

---

## 🧑 Papi  <sub>2026-06-10 09:49:21</sub>

you didnt fix this ERROR: [youtube]      │
│ n2KDi0IHl5M: Requested format is not available. Use --list-formats for a list of av

---

## 🤖 Claude  <sub>2026-06-10 09:53:37</sub>

The user's pointing out that I didn't actually solve the root problem — I just added diagnostics and a retry mechanism while the "Requested format is not available" error still happens. There's another video failing now, so I need to think about what's actually causing this in yt-dlp with YouTube in 2025/2026, starting with format specification issues.

The script doesn't explicitly set a format option, so it relies on yt-dlp's default behavior. When using the Python API without specifying a format, it tries `bestvideo*+bestaudio/best` if ffmpeg is available for merging, otherwise it falls back to `best` — a single pre-merged format. The critical issue is that modern YouTube has almost entirely moved to DASH streams (separate video and audio), phasing out the old progressive formats like format 18 (360p) and 22 (720p) that used to be reliable fallbacks.

With 173 downloads succeeding and only 14 failing, the failures likely stem from a missing JavaScript runtime. Since late 2025, yt-dlp needs deno or node to handle YouTube's signature challenges, and without it, many formats get filtered out. For some videos, this filtering leaves no usable formats at all, triggering the "Requested format is not available" error.

Beyond that, there's also the possibility of SABR-only responses where YouTube serves adaptive bitrate streams that yt-dlp can't handle directly, age-gated or members-only content that requires specific client support, or DRM-protected music videos. The intermittent nature suggests it's not a blanket issue but rather specific videos hitting these edge cases.

The real fix would be implementing a multi-stage fallback retry system in the downloader code. When a format isn't available, I'd retry with progressively broader format specifications and rotate through different player clients like Android and Safari to see if any of them can access the content. The challenge is that hardcoding client names gets fragile across yt-dlp version updates. That's the key insight — without ffmpeg, the default format selector falls back to `best` which only works with progressive formats, but DASH video and audio tracks still exist as separate formats that can't be merged. So the selector fails even though formats are technically available. I need to account for this by either checking ffmpeg availability or using a more permissive fallback that handles both merged and progressive scenarios. is absent and he's requesting `best`, it fails on DASH-only videos and throws this format unavailable error, while the fallback `bestvideo+bestaudio` would complain about missing ffmpeg instead. Without knowing if he has ffmpeg installed or on his PATH, the safest approach is to build a retry mechanism in the downloader that catches format-unavailable errors and systematically tries alternative format combinations.

For the retry passes, I'd start with the configured default, then fall back to switching player clients—using ones like android or tv that historically had different signature handling and didn't require the JavaScript runtime that might be missing.

I should also detect whether ffmpeg is installed upfront using a simple check, and if it's missing, flag that as a likely culprit since DASH-only videos will fail without it.

Beyond that, I need to check for a JavaScript runtime—either Deno or Node—since yt-dlp 2025.10+ requires one for full YouTube support. Without it, you get warnings and skipped formats. I'll surface both the ffmpeg and JS runtime status in the header so the user can see what's available.

The real solution involves three parts: a retry mechanism with client rotation that automatically handles format-unavailable errors and logs which attempt succeeded, a startup probe that checks for ffmpeg and a JS runtime and warns if either is missing, and being careful about format selection—forcing `bv*+ba/b` when ffmpeg is missing would just cause merge failures anyway.

Given that 173 downloads worked, he almost certainly has ffmpeg installed; the 14 failures are more likely from nsig/JavaScript runtime issues on specific videos, SABR restrictions on certain web clients, or age and membership gating.

I should also think about whether pass 2 should include cookies—some clients like Android don't support them, though yt-dlp might just warn and continue. Another angle: when a format fails, I could automatically run a format listing to show what's actually available and include that in the error message.

Actually, that's probably overkill since the retry ladder already probes effectively. Instead, I'll improve the LogCatcher to track the last few unique warnings (up to 3) rather than just the most recent one, since multiple warnings often occur together like "Some web client formats skipped" or "nsig extraction failed"—joining them gives better diagnostics without much extra cost.

Now I'm setting up the implementation in the download function, defining regex patterns to catch format-related errors.

Defining the retry ladder...

I'm concerned about how extractor_args might conflict if the user sets their own later — our retry would override theirs. That's acceptable for a retry mechanism though. Also wondering if hardcoding client names like "android" and "ios" could break if yt-dlp drops support for them in the future, though yt-dlp typically raises an error for unknown clients rather than silently failing.

Setting up the download function with a log catcher to track output, building a base options dict, then iterating through a retry ladder where each attempt adds extra configuration on top of the base... I'll keep the Downloader's return signature unchanged since Worker expects those four values, and instead have Downloader call `self.tui.set_event` directly when retrying with a fallback format. The archive won't be written on failed attempts, which is fine, and re-running extract_info to grab metadata again is acceptable. There's a minor issue where a retry with a different format might produce a different filename and orphan the old .part file, but that's tolerable.

Now I'm moving on to handle ffmpeg and JavaScript probing...

Writing probe function... Since the format spec defaults based on ffmpeg availability, I should make that explicit when ffmpeg is present — setting `"bv*+ba/b"` conditionally in the options if the user hasn't specified a format and ffmpeg is available. This makes the behavior deterministic and visible in the retry logic. I'll add a comment explaining this and bump the version to 2.3 with a changelog entry, plus update the header to include ffmpeg and runtime status fields.

For the response, I need to own that I added diagnostics rather than the actual fix — the real solution is the auto-retry ladder that rotates player clients and probes for the two common failure causes (JS runtime and ffmpeg). I should be honest that some videos will legitimately fail due to membership, DRM, or region restrictions, but now the error message will explain why. The client rotation is the mechanical fix for the SABR/nsig class of issues. I'll keep it brief and tight, maybe a short list of the retry passes, and remind them that pressing `u` to update yt-dlp is still critical since stale versions are the #1 cause of failures. I'm realizing there's a risk that android and ios clients might get skipped when cookies are passed to yt-dlp, since some clients don't support authentication. If both get skipped, I'd have zero clients to fall back on. I should design the fallback rungs to include at least one cookie-compatible client in each tier — maybe pairing android with web_safari in pass 2, and ios with tv in pass 3, though I'm not entirely certain about the current cookie support matrix for all clients.

For the format strings, I'll use "bv*+ba/b" for pass 2 and "b/bv*+ba" for pass 3, preferring single-file output to avoid merge issues if ffmpeg is the problem. Pass 3's format also handles the no-ffmpeg case.

Now I need to make the code edits: update the docstring to v2.3, add a module-level environment probe for ffmpeg and javascript availability after the version block, add those fields to the header, implement the FORMAT_RETRY ladder with the rewritten download function, and keep LogCatcher for the last fallback.

For LogCatcher, I'm storing warnings in a list and deduplicating them, keeping only the last 3 with the `del self.warnings[:-3]` logic. On failure, I'll join the last 2 warnings with " | " and format them as `\n[warnings] w1 | w2` to stay under the 500-character limit that mark_failed truncates anyway.

Now moving to the download function...

I'm defining a helper that searches for executables by name, then using it to locate ffmpeg from the config or system PATH, and finding the first available JavaScript runtime from deno, node, bun, or quickjs. I'll place these right after the EXTRA_YTDLP_OPTS definition in the config section.

Now I'm thinking through the header layout—adding ffmpeg and js runtime info to the first line alongside the yt-dlp version would make it too long, so I should split it across two lines: the first showing the title, yt-dlp version, ffmpeg status, and js runtime, and the second showing cookies source and clipboard mode.

Actually, I can fit all six fields on one line if I keep them compact—around 110 characters, which should work on a typical terminal. For the status indicators, I'll use color coding: ffmpeg shows green for "ok" or red for "missing", and js shows cyan for "deno" or red for "none". The output and state paths move to their own line below.

Now I'm handling the startup checks in main—if ffmpeg is missing, I'll show a warning about merged formats being unavailable, and if there's no JS runtime, I'll flag that YouTube might hide formats. Since the event line can only display one message, I'll prioritize ffmpeg and chain the checks with elif, or combine them into a single message if both are missing.

For the downloader, I'm defining a regex pattern to catch format-related errors like unavailable formats or HTTP 403s, then setting up a retry ladder with different YouTube client configurations—android/web_safari first, then ios/tv/web as fallbacks. The extractor_args target YouTube specifically, so they're harmless on other sites but I should probably gate this ladder to YouTube URLs only.

The FORMAT_RETRY_ERR pattern does catch some generic strings that other sites might produce, so retrying non-YouTube links could waste time, but the pattern gates it reasonably well. Retrying twice is cheap since metadata fetches are fast anyway. Now I'm defining the download function that returns success status, title, filepath, and error—it climbs the retry ladder on format failures by rotating YouTube player clients to dodge signature verification issues, with the final attempt preferring a single pre-merged file.

Implementing the download logic... Finishing the error handling and return statement, then noticing the event ordering — the fallback notice flashes briefly before the Worker overwrites it with the done event, but that's fine since the retry messages during the process are what users actually see. I'm thinking about updating the LogCatcher to use a warnings list instead and bumping the version to v2.3.

Now I need to work through the edits systematically: updating the docstring with a "What's new" section for v2.3, adding environment probe constants after the existing config, restructuring the header to include ffmpeg and JavaScript detection fields, replacing the LogCatcher class with the warnings list, completely rewriting the download function with the ladder constants moved above it, and adding startup environment warnings to main(). I'll compile and check symbols again, then present the file with a message acknowledging the fair point about unavailable videos while explaining what the fix actually addresses — the mechanical causes through the environment probe and the three-rung fallback ladder.You're right — fair call. I gave you diagnostics and a retry button, not a fix for the failure itself. Let me actually attack the error mechanically this time.
```
This block is not supported on your current device yet.
```

 I'm starting to make the edits now, beginning with the environment probe configuration that comes after the EXTRA_YTDLP_OPTS setting.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

v2.3 — this one actually fights the error instead of just logging it.

What "Requested format is not available" really means: yt-dlp's selector matched *zero* formats. On modern YouTube that's almost never about the video genuinely lacking formats — it's that the default player clients got a response where every format was skipped (sig/nsig challenge unsolved, or SABR-only streams yt-dlp can't pull). So the fix is to ask again as a *different client*:

1. **Rung 1** — default clients, as before. Most videos never leave this rung.
2. **Rung 2** — android + web_safari with `bv*+ba/b`. Android uses a different signature scheme entirely, so it survives a broken JS-runtime situation.
3. **Rung 3** — ios + tv + web with `b/bv*+ba` — single pre-merged file *first*, so this rung also works if ffmpeg is the problem.

It only escalates on format-availability errors and 403s (which is how a stale sig token presents). Private/deleted/geo-blocked fails stay instant — no wasted retries.

Second thing: the header now probes and displays `ffmpeg=ok/MISSING` and `js=deno/node/none`, with a loud startup warning if either is absent. These are the two silent root causes — no ffmpeg silently downgrades yt-dlp's default selector to single-file `best`, which modern YouTube barely serves; no deno/node makes yt-dlp skip every sig-protected format. When you relaunch, look at that line first. If it says `js=none`, that's probably been your whole 14-failure story, and `winget install DenoLand.Deno` ends it.

So for the backlog: relaunch, check the header, then **f** to requeue the failed ones — they'll each get the full three-rung treatment now. Anything that *still* fails after that will have the real reason attached in the warnings trail, and at that point it's usually a genuinely unavailable video (members-only, DRM'd, region-locked) rather than a fixable one.