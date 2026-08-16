---
title: "Code debugging"
uuid: 4191f3fe-f9a0-4219-8523-698f065456e1
created: 2026-06-04
updated: 2026-06-08
trunk: BLACK
messages: 4
chars: 29518
artifacts: 0
generated_files: 0
tools: [bash_tool, present_files, str_replace, web_fetch, web_search]
source: claude.ai-export-2026-08-15
---

# Code debugging

> **Conversation Overview**

The person is working on a Python-based clipboard monitoring and automatic download tool called `ytdlp_go.py` (also referenced as "GOON+PASTE" style tool) that watches the clipboard for URLs, queues them in SQLite, and downloads them via the yt-dlp Python module with a Rich TUI interface. The conversation covered two separate issues across two sessions.

In the first session, the person shared the script without specifying what was broken, asking Claude to "fix this." Claude identified and fixed two real bugs: a 64-bit ctypes handle truncation in `get_clipboard_text` where missing `argtypes`/`restype` declarations caused `GetClipboardData` and `GlobalLock` to silently truncate 64-bit handles to 32 bits on 64-bit Windows, making clipboard reads return empty or crash; and a latent signal-handler deadlock where the `shutdown()` SIGINT handler called `tui.set_event()` which acquires `tui.lock`, a non-reentrant lock the main thread could already be holding during `render()`. The clipboard fix added proper ctypes prototype declarations matching the pattern already used in `WinClipboardListener`, while the deadlock fix made the handler signal-safe (only `Event.set()` and `worker.kick()`) and moved the UI message to the main thread post-loop. Both fixes were verified with a cross-platform logic test suite covering queue lifecycle, URL deduplication, normalization, and formatters.

In the second session, the person encountered recurring `ERROR: Requested format is not available` errors on specific YouTube video IDs and asked Claude to evaluate YoutubeExplode (a C#/.NET library at github.com/Tyrrrz/YoutubeExplode) as a potential solution. Claude reviewed the repository and current yt-dlp issues, then advised against integration: YoutubeExplode is C#-only (requiring a full rewrite or .NET sidecar), YouTube-only (the tool intentionally supports 1800+ sites via yt-dlp), and subject to the same breakage pattern since it is also a scraper. The actual diagnosis was that as of late 2025 yt-dlp requires an external JavaScript runtime (Deno, Node, or QuickJS) to resolve YouTube's JS challenges, and without one formats get silently filtered, producing the observed error. The recommended fix was environment-level with no code changes: `pip install -U yt-dlp` followed by `winget install DenoLand.Deno`, after which yt-dlp auto-detects the runtime. Claude offered an optional follow-up to add a startup preflight check to the script that would detect missing JS runtimes and surface a warning in the TUI header rather than letting failures appear as cryptic queue errors.

---
## 🧑 Papi  <sub>2026-06-04 21:35:20</sub>

fix this

---

## 🤖 Claude  <sub>2026-06-04 21:41:35</sub>

The user uploaded a Python script for their clipboard monitor and download automation tool without specifying what's broken, so I need to carefully review the code to identify actual bugs rather than just asking for clarification.

I'm working through the logic systematically: the URL regex and fullmatch behavior look correct for validating single URLs, the clipboard listener's event signaling handles both success and failure cases properly, and now I'm examining the worker's download and shutdown flow to see if there are race conditions or incomplete cleanup when stopping mid-download.

There's a potential issue with the download archive deduplication—when yt-dlp encounters a video already in the archive, it skips the download but `extract_info` might still return metadata, which could cause confusion about whether the item was actually processed or just marked as seen.

I should also verify the `WinClipboardListener.stop()` method handles the case where `_user32` wasn't initialized if the listener failed early, though it does have a fallback to `ctypes.windll.user32` so it's probably safe.

Looking at the message queue handling, `GetMessageW` correctly returns 0 on `WM_QUIT` and the loop breaks on `ret <= 0`, so that's working as intended.

There's a potential race condition in the main loop where the clipboard could change between when `clipboard_changed.wait()` returns and when we call `clipboard_changed.clear()`, which might cause us to miss an update, but it's a minor edge case.

Now I'm examining the `Store.enqueue` method and how it interacts with the `UNIQUE` constraint on `normalized_url` — it checks for existing entries before inserting while holding the lock.

The multiple worker scenario isn't actually a concern since there's only one worker running.

Looking at the listener startup timing, there's a 2-second timeout waiting for `started_evt` after calling `listener.start()`, which should be plenty of time for the event loop to initialize.

I'm checking the regex in `looks_like_url` with its character class that excludes `]` and `)` to handle trailing punctuation correctly, though I need to verify it handles URLs containing those characters properly.

The clipboard comparison logic treats the initial clipboard content as already seen, which appears intentional—it only enqueues changes after the first read.

Now I'm examining the Windows API setup for `WNDCLASSEXW` and `RegisterClassExW`, specifically how the callback function reference is assigned to the window class structure...

Actually, the user said "fix this" without details, so there must be real bugs lurking. Let me think through what would actually break at runtime rather than just reviewing the code. Testing the non-Windows parts makes sense—URL normalization, the SQLite store, regex patterns, and formatters should all be verifiable even in this environment.

Let me focus on what's most likely to fail. I'll start by examining the URL normalization logic more carefully...

Actually, I'm realizing the threading model in the Store class is the real concern here. A single SQLite connection shared across threads without proper synchronization could cause serious issues.

Let me trace through the Windows-specific parts more carefully. The WNDPROC return type and 64-bit handling are emphasized in the comments, which suggests there might be a subtle bug related to how the window procedure returns values or handles pointer sizes on 64-bit systems. The pointer conversion looks correct for handling the special HWND_MESSAGE value. Now I'm wondering if the actual bug might be elsewhere and testable. Let me try running the code to see what happens—I'll start with the cross-platform logic on Linux and check if there's something I'm missing in the implementation.

Actually, I'm noticing something about the worker shutdown sequence: when `stop_evt` is set in the finally block, the worker thread is likely waiting in `self.wake.wait(timeout=2.0)`. It should wake within 2 seconds, check the stop condition, and exit cleanly. But I need to trace through what happens when `shutdown()` calls `worker.kick()` to make sure there's no deadlock there. to wake it immediately. In the `finally` path (KeyboardInterrupt caught), `shutdown()` is also... wait, let me trace:

If Ctrl+C: SIGINT handler `shutdown` runs → sets stop_evt, kicks worker. The main loop `while not stop_evt.is_set()` exits. Goes to `finally`. `stop_evt.set()` (already set). `worker.join(3600)`. Worker wakes (kicked or download finishing), exits. Good.

But what if signal arrives while worker is mid-download? Worker finishes download (could be long), then exits. join(3600) waits up to an hour. That's "let current download finish." Intended.

Hmm. There's also `except KeyboardInterrupt: shutdown()` — but if SIGINT handler is installed, the KeyboardInterrupt won't be raised (the handler runs instead). So that except block is essentially dead code but harmless.

OK, I'm overthinking this. Let me just write a test and see if there's an actual failure. Actually, wait — maybe there IS a clear bug I'm missing. Let me look at the Windows clipboard function again. I'm setting the restype to return a wide character string, then locking the handle and converting the result to a string. That should work, but let me think through whether there's a memory management issue there.

Actually, I just realized the real problem: I'm not setting argtypes on GlobalLock, so ctypes defaults to treating the handle as a 32-bit integer. But GetClipboardData returns a 64-bit pointer on 64-bit systems, and I'm not setting its restype either — it defaults to c_int, which truncates the upper 32 bits. That's a genuine 64-bit bug that would cause GlobalLock to receive a corrupted handle and fail or crash. The same issue applies to OpenClipboard when passing 0.

The fix is straightforward: I need to set restype and argtypes properly on GetClipboardData, GlobalLock, and GlobalUnlock, just like the listener code does. The reading function skipped these prototypes while the listener was careful about them, so this is almost certainly where the bug is.

Now let me think through whether this would crash or just return empty — if the truncated handle happens to fit in 32 bits, it might work by accident, but generally the high bits get lost and GlobalLock either returns NULL or accesses garbage memory, making clipboard reading unreliable on 64-bit Windows. I should also check GlobalLock's argtypes since it's receiving that already-truncated handle as a plain int.

Now I'm looking at another potential issue with the signal handler in main and how it interacts with the Live display loop.

Actually, the SIGINT handler runs fine between bytecode instructions while the main thread is blocked on the clipboard wait or sleep. Let me trace through the other potential issues — the enqueue race with archive isn't actually a crash, and when yt-dlp returns info for a video already in the archive, it might have no requested_downloads but that's handled correctly. For the URL regex, fullmatch with the current pattern correctly rejects multi-word clipboard text since internal whitespace would fail the match.

Now I'm checking whether the listener fallback to polling has thread safety issues — if the listener fails, it's set to None so stop() never gets called, which is fine. The SQLite connection shared across threads with WAL mode and a Python lock is properly serialized. But the real bug I'm seeing is the 64-bit ctypes handle truncation in `get_clipboard_text` on Windows — the listener code went to great lengths to handle 64-bit correctness with proper HWND types, but `get_clipboard_text` uses naive, unsafe ctypes calls that would truncate handles. Let me verify the specific calls to confirm this is the issue.

Writing corrected function... Finishing the cleanup logic...

I'm realizing that using `c_void_p` as the restype for `GlobalLock` is cleaner than `c_wchar_p` because it lets me explicitly call `wstring_at` while the memory is still locked, avoiding any auto-conversion issues. This is the safer pattern for reading clipboard data. I should also scan for any other bugs in this function while I'm refactoring it.

Looking through the code, I notice a potential deadlock issue: the signal handler calls `tui.set_event`, which acquires `tui.lock`, but if the main thread is already holding that lock (say, inside `render()`), the signal handler will deadlock since it runs in the main thread and can't wait for a lock it already holds.

The fix is to keep the signal handler minimal—just set the stop event and kick the worker without touching the TUI lock. I could either remove the `tui.set_event` call from `shutdown` or use a thread-safe flag that the render loop checks instead. the TUI is cosmetic anyway since we're tearing down the Live display. So the real fix is straightforward: make the signal handler only set `stop_evt` and kick the worker — both signal-safe operations — and move any TUI notifications to the main thread after the loop exits. Once the handler sets the stop event, the main loop will break on its next check, and we can handle cleanup without holding locks.

Now I'm weighing whether the deadlock is actually the core bug here. The clipboard truncation on 64-bit Windows is more obviously critical — it would break the entire tool on that platform. The signal handler deadlock is a real latent issue too, but less immediately catastrophic. I'll fix both and document them clearly.

Let me scan for other problems. The `finish_progress` function looks fine, and the ETA formatter's "—" display for zero values is just cosmetic. The import of `Group` from `rich.console` should work in current versions. The signal handling for SIGINT and SIGTERM looks reasonable with proper guards. Now I'm checking the output directory path construction...

The template string with percent signs and the comma syntax for yt-dlp's fallback works fine on Windows. I should also verify the `WinClipboardListener` doesn't have the same truncation issue — it sets all the ctypes carefully, so it's clean. That confirms `get_clipboard_text` is where the inconsistency lives.

I can't actually test the Windows-specific code path here, but I can at least verify the cross-platform logic compiles and runs without errors from my changes. My fixes are isolated to the Windows clipboard function and the shutdown handler, while the Linux path using pyperclip stays untouched. I think the best approach is to provide the corrected Python file directly since the user will want the actual fixed code rather than just documentation.

Given the file is around 600 lines, I'll copy it, apply the targeted edits to fix the truncation bug, and present the corrected version as a file artifact along with a brief explanation of what changed. Fixing the Windows clipboard function... Setting up the clipboard retrieval logic...

I need to be careful with the ctypes type definitions — HGLOBAL might not exist in wintypes, so I'll use HANDLE instead since they're equivalent anyway. For GlobalLock and GlobalUnlock, I'll set the argtypes to HANDLE and the return types appropriately.

Now for the shutdown function, the issue is that calling tui.set_event from the signal handler could deadlock if the main thread is already holding the lock during rendering. I should avoid touching the UI lock in the signal handler entirely.

Restructuring the main loop... Updating the TUI display...

The loop will finish its current iteration when the stop event is triggered, then check the condition and exit cleanly before running the teardown code—that's the right behavior.

Now I'm checking the `continue` statement path: it still re-evaluates the while condition, which is correct. This approach looks solid, so I'll go ahead and apply it. The `except KeyboardInterrupt` handler just sets the events now instead of calling shutdown directly, which fits the pattern fine.

Let me verify there aren't any other lock-in-handler issues from removing `tui.set_event` — both `worker.kick()` and `stop_evt.set()` just call `Event.set()`, so that's safe. I should scan for any other definite bugs I might be overlooking.

On Linux, the clipboard reading uses pyperclip and the listener is Windows-specific while polling happens on Linux, so the queue should work fine for testing on that path, but I'm wondering if there's something else that would break the whole thing even in the happy case.

The tool is fundamentally built for Windows with its clipboard event handling and browser cookie assumptions. The truncation bug is the main issue I need to focus on. I'm pretty confident the two key fixes—the 64-bit clipboard read and the signal-handler deadlock—are the real problems here. Let me think through whether there are other minor issues worth mentioning or if any of them are trivial enough to just fix without calling them out.

Actually, I'm spotting a couple more potential issues. There's the `looks_like_url` function using `fullmatch` which returns a match object or None, and the logic checks `if not URL_RE.fullmatch(text)` which works correctly. But then there's this shadowing problem in `_run_loop` where a local variable gets reassigned to the same name, which could be confusing or problematic depending on what the original value was supposed to be.

Let me verify that `wstring_at` from ctypes is actually available for reading wide strings from memory addresses. And I'm concerned about the type casting here — when `GlobalLock.restype` is set to `wintypes.LPVOID`, the returned pointer needs to be handled correctly downstream. Now I'm ready to implement the solution — I'll check the uploads directory and copy the file over, making sure to match the exact original text when using string replacement to avoid any indentation problems.
```
This block is not supported on your current device yet.
```

 I have the full content in my context, so I'll create the corrected file directly with both fixes applied inline rather than writing the original first and then making edits—that's more efficient and avoids the risk of introducing errors in the unchanged sections.No uploaded file on disk — the script came through inline. I'll reconstruct it on disk, fix it, and hand back the corrected file. Let me first write the original verbatim so my edits are surgical.
```
This block is not supported on your current device yet.
```

 Now I'm implementing the first fix to handle 64-bit truncation in the Windows clipboard function, then moving on to address the signal handler deadlock issue.Original is on disk and parses. Now the two fixes.

**Fix 1 — the 64-bit clipboard-read bug (the big one).** The listener carefully declares every ctypes prototype for 64-bit correctness, but `get_clipboard_text` doesn't. `GetClipboardData`/`GlobalLock` default to a 32-bit `int` return, which truncates the upper half of the 64-bit clipboard handle → garbage handle → empty reads or hard crashes on 64-bit Python. Nothing ever gets queued. This is the function the whole tool runs on every poll/event.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 I see there's a signal handler deadlock issue where the handler tries to acquire a lock that the main thread already holds during rendering, causing a deadlock on the non-reentrant lock. I need to make the signal handler only set events without acquiring locks, then move the shutdown UI message to run in the main thread after the event loop exits instead.**Fix 2 — a latent deadlock in the Ctrl+C handler.** The signal handler calls `tui.set_event()`, which grabs `tui.lock`. Signal handlers run on the main thread, and the main thread regularly holds `tui.lock` inside `render()`. If SIGINT lands in that window, the handler tries to re-acquire a non-reentrant `Lock` it already holds → permanent hang on exit. A signal handler should only do signal-safe work (set the events); the cosmetic message belongs in the main thread.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 I need to verify the file parses correctly and run a smoke test of the core functionality across platforms—testing the Store's enqueue/claim/mark operations, URL normalization and deduplication, URL detection, and the formatters. Since APP_DIR is set at module import time, I'll work around this by manipulating the HOME environment variable to use a temporary directory instead of touching the actual home folder.

The challenge is that yt_dlp and rich might not be installed, and the module will fail to import if they're missing. Rather than installing them, I'll create lightweight stub modules on sys.path so the import succeeds, then set HOME to a temp directory and run the test to exercise the core logic.

Writing test script...Now verify it parses and smoke-test the cross-platform logic (queue dedup, URL normalization, detection) to make sure the edits didn't disturb anything.
```
This block is not supported on your current device yet.
```

 All tests are passing. The quirk with norm B showing `v=ID%2F` is actually from my test setup—I intentionally put the slash after the query parameter, so it's part of the value itself rather than a path separator, which is why URL encoding preserves it that way. The dedup assertion I was focused on is working as expected.

Both core fixes check out and are verified for cross-platform logic. The Windows-specific fix can't be tested in this environment, but the prototype declarations now match the listener's style exactly, which is the right pattern. I'll copy everything to outputs and provide a clear summary, noting that the removed `if not stop_evt.is_set():` guard is fine since the logic is now idempotent, and the `except KeyboardInterrupt` is effectively unreachable while the handler is active but harmless to leave.All green. Copying to outputs.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Two real bugs, both fixed and the rest verified intact.

**1. 64-bit clipboard read was broken (the one that matters).** `get_clipboard_text` used `ctypes.windll` with no prototypes. With no `argtypes`/`restype`, ctypes defaults to a 32-bit `int` return, so `GetClipboardData` (and `GlobalLock`) had the upper 32 bits of their HANDLE/pointer truncated on 64-bit Python. Result: `GlobalLock` gets a garbage handle → reads come back empty or it crashes. On a 64-bit Windows machine nothing would ever get queued. Ironic, because your `WinClipboardListener` declares every prototype carefully — this function was the one place that skipped it. I rewrote it to declare `OpenClipboard`/`GetClipboardData`/`GlobalLock`/`GlobalUnlock` with proper `argtypes`/`restype` (`HANDLE`/`LPVOID`), and read via `ctypes.wstring_at(ptr)` while the memory is locked instead of relying on the `c_wchar_p` restype trick.

**2. Ctrl+C could deadlock on exit.** `shutdown()` is a signal handler, so it runs on the main thread — and it called `tui.set_event()`, which acquires `tui.lock`. The main thread regularly holds that same lock inside `render()`. If SIGINT landed in that window, the handler tried to re-acquire a non-reentrant `Lock` the thread already held → hang forever instead of shutting down. Fixed by making the handler signal-safe (only `stop_evt.set()` + `worker.kick()`) and moving the "shutting down" message into the main loop after it observes `stop_evt`, where no lock is held.

What I verified on this box (Linux, so the Windows path couldn't be executed, but the logic could): queue enqueue/claim/done lifecycle, normalized-URL dedup (`utm_*`/`si=` stripped, `www.` stripped, finished items report `done` vs `duplicate`), URL detection rejecting multi-word text, and the byte/ETA formatters — all pass. The Windows prototype declarations now mirror the listener's working pattern exactly.

One thing left alone on purpose: the `except KeyboardInterrupt` branch in `main` is effectively dead while the SIGINT handler is installed, but it's a harmless safety net so I kept it.

---

## 🧑 Papi  <sub>2026-06-08 11:44:44</sub>

ok so i keep getting this error
ERROR: [youtube] Hl4J7hWqk7M: Requested format is not available. Use --list-formats for a list of available formats
ERROR: [youtube] Hl4J7hWqk7M: Requested format is not available. Use --list-formats for a list of available formats
ERROR: [youtube] QryoOF5jEbc: Requested format is not available. Use --list-formats for a list of available formats
ERROR: [youtube] HJamIWCgKkE: Requested format is not available. Use --list-formats for a list of available formats


i'll upload the .py again 

ok but before doing anything take a look at Youtube Exploder. i think this is hte solution we need. If it is can you help me intergrate it? 

https://github.com/Tyrrrz/YoutubeExplode

---

## 🤖 Claude  <sub>2026-06-08 11:46:48</sub>

The user is running into "Requested format is not available" errors with yt-dlp on YouTube and wants me to evaluate YoutubeExplode as an alternative. I need to understand what's actually causing the issue first—they have their format options commented out, so yt-dlp is falling back to its default behavior, which might be the source of the problem.

The error typically stems from either a mismatched format string or, more commonly these days, YouTube's anti-bot measures breaking yt-dlp's format extraction until the library gets updated. A simple `pip install -U yt-dlp` often fixes this. However, the user is specifically interested in YoutubeExplode, which is a C#/.NET library—integrating it into a Python script would require either a complete rewrite or shelling out to a .NET helper, which is a significant architectural mismatch. I should look at the actual YoutubeExplode repository to give them an accurate assessment of whether it's worth pursuing.
```
This block is not supported on your current device yet.
```

 YoutubeExplode is a pure C# library available via NuGet that reverse-engineers YouTube's internal API, currently at version 6.6 and actively maintained, though it's YouTube-specific rather than multi-platform like yt-dlp. Since YouTube deprecated muxed streams, the library requires downloading separate video and audio streams for high-quality output.

Integrating YoutubeExplode into the Python tool would mean either rewriting everything in C# or building a separate .NET console wrapper to call from Python—both are impractical and would lose yt-dlp's multi-site support. The real issue with "Requested format is not available" is almost certainly that yt-dlp is outdated; YouTube constantly changes its player and signature formats, and yt-dlp ships frequent fixes to handle those changes. The first step should be updating yt-dlp itself, not switching libraries.Read it. Before I touch the code, let me check what's actually breaking, since this is a fast-moving area.
```
This block is not supported on your current device yet.
```

 The "Requested format is not available" error in 2026 stems from two main issues: an outdated yt-dlp version that can't handle YouTube's frequently changing N challenge and player updates, and YouTube's enforcement of SABR streaming or PO token requirements that some clients can't satisfy.

YoutubeExplode isn't the right solution here — it's a .NET-only library limited to YouTube, whereas the user's tool needs to download from 1800+ sites via yt-dlp. More importantly, YoutubeExplode is itself a reverse-engineering scraper that breaks the same way when YouTube changes things; it's not immune, just maintained separately. yt-dlp gets daily updates and is far more actively maintained, so the actual fix is straightforward: update yt-dlp through pip, which will almost certainly resolve the issue immediately.

Beyond that, the user likely needs to install Deno as a JavaScript runtime — newer versions of yt-dlp rely on an external JS engine (EJS) to solve signature challenges and handle format extraction, and without Deno or Node installed, those formats get skipped entirely, which is probably what's causing the SABR errors and missing URLs they're seeing. The user specifically asked me to evaluate YoutubeExplode first, so I need to be direct: it's not the right solution. Integrating a .NET sidecar into their Python stack would add unnecessary complexity, and YoutubeExplode is also a scraper that breaks on YouTube changes just like yt-dlp does. Plus their tool handles multiple sites, not just YouTube, so a YouTube-only library doesn't fit their needs anyway.

The real fix is simpler: update yt-dlp to the latest version and install a JavaScript runtime like Deno, which modern yt-dlp needs for YouTube extraction. I can also offer to add some defensive code to their script—better error messages and a robust format fallback—since they've already uploaded the file.That confirms the picture. Quick check on one thing that changed recently and matters for the fix:
```
This block is not supported on your current device yet.
```

 I'm evaluating YoutubeExplode as a potential solution and ruling it out—it's C#-only which would require rewriting the Python tool or running a separate service, it only handles YouTube while their tool supports 1800+ sites, and it's also a scraper that breaks the same way YouTube does, so it doesn't actually solve the underlying problem.

The real issue is that as of yt-dlp 2025.11.12, YouTube extraction now requires an external JavaScript runtime (Deno, Node, or QuickJS) to handle YouTube's JavaScript challenge. Without one, formats get filtered out and the user hits "Requested format is not available." This is likely compounded by an outdated yt-dlp version.

The fix is environment-level with no code changes needed: update yt-dlp via pip, install Deno (which yt-dlp auto-detects on PATH), and verify with a test download. Since they're on Windows, I'll provide the Windows install commands. I can also optionally add a preflight check to their tool that warns if no JS runtime is detected, which would catch this failure mode upfront, but the environment fix alone should resolve it immediately.Took a real look, and I'm going to give you the honest answer: **YoutubeExplode won't fix this, and integrating it would make your tool worse, not better.** Here's why, then the thing that actually fixes your error.

## Why YoutubeExplode is the wrong tool here

Three hard blockers:

1. **It's 100% C#/.NET.** YoutubeExplode installs via NuGet (`dotnet add package YoutubeExplode`) and the repo is literally C# 100.0%. Your tool is Python — yt-dlp module, rich, sqlite, the ctypes clipboard listener. "Integrating" it means either rewriting the whole thing in .NET or running a C# sidecar process that your Python shells out to. That's a massive amount of plumbing to dodge one error.
2. **It's YouTube-only.** Your GOON+PASTE tool is multi-site by design (yt-dlp covers 1800+ sites). YoutubeExplode does one site. Bolting it in is a downgrade in coverage.
3. **It doesn't address the root cause.** YoutubeExplode is itself a reverse-engineering scraper — it works by scraping raw page data and exploiting reverse-engineered internal endpoints. It breaks the same way yt-dlp does when YouTube changes things; it just has its own maintainer keeping up. yt-dlp is updated daily and is far more battle-tested.

## What's actually breaking

Your `EXTRA_YTDLP_OPTS` has no format set, so this isn't a "you asked for a format that doesn't exist" problem — it's that yt-dlp can't *resolve* the real formats. As of late 2025, an external JavaScript runtime is now required for full YouTube support, and YouTube support is deprecated without one. Without it, some formats get skipped because they're missing a URL, and the warning says formats may be missing — which surfaces downstream as exactly your "Requested format is not available" error. The other half is simply that an outdated yt-dlp causes this because YouTube's challenge changes frequently — the fix is to update.

## The actual fix (no code rewrite needed)

On your Windows box, in order:

1. **Update yt-dlp:** `pip install -U yt-dlp`
2. **Install Deno** (the JS runtime — Deno is enabled by default, so once it's on PATH yt-dlp uses it with zero config): `winget install DenoLand.Deno` — then open a fresh terminal so PATH refreshes.
3. **Verify:** `yt-dlp -vU --list-formats "https://youtu.be/Hl4J7hWqk7M"` — the debug output should now show a JS runtime found and a real format list instead of skipped formats.

That's it. Because your tool uses the yt-dlp Python module, it'll pick Deno up automatically on the next run — nothing in `ytdlp_go.py` changes. If you'd rather not install Deno, Node.js also works (it's only needed for YouTube; all other sites work without it), or there's a runtime-free plugin, ytdlp-jsc, that embeds a sandboxed JS engine instead — but Deno is the path of least resistance.

One optional improvement I'd suggest for the script itself: a small **startup preflight** that checks yt-dlp's version and whether a JS runtime is detected, and flags it in your TUI header — so the next time YouTube shifts, you get "no JS runtime found, run an update" instead of a cryptic format error buried in the failed-queue. Want me to add that to the uploaded `ytdlp_go.py`?