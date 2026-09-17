# Dictation — BOLO 26, the BUILD route

**Ruled 2026-09-16** (Papi: "build"). Push-to-talk speech-to-text that stops mangling
the Command lexicon. Local, GPU, $0 — no audio leaves the box, nothing is billed.

This is **JUDY's listening half** (BOLO 56). The speaking half, the wire to the VS Code
session, and the face are still unruled.

## Run her

```
python _tools/dictation/judy.py
```

A frameless always-on-top face appears. **Hold `ctrl+alt+space`, talk, release.**
Drag the face anywhere — it remembers where. Right-click it to quit.

```
python judy.py --type "what's blocked"   # no mic, one turn
python judy.py --no-face                 # terminal only
python judy.py --no-voice                # print, don't speak
```

The loop, and what each part is:

| Stage | Face | What runs |
|---|---|---|
| hold the key | `listening` | mic capture |
| release | `thinking` | faster-whisper on the 3090, then SOP §8 repair |
| brain answers | `talking` | ElevenLabs (or Piper offline) |
| done | `idle` | — |

### The brain, honestly

`brain.py` is **a keyword router, not a language model.** There is no Anthropic key
on this box and no local model that runs, so JUDY does not improvise — she reads the
repo and answers a short list of real questions:

| Ask | She reads |
|---|---|
| what's blocked | STATE's Blocked-on-you table |
| the main effort / leverage | the newest sit rep board |
| BOLO *n* | that row in BOLO.md |
| PMCS | the PMCS table |
| is the box up | the ports, and the git tree |
| what time is it | the clock |

Anything else and she says so rather than guessing.

**This is on purpose, and it is the MCP work.** The wire was ruled MCP; an MCP server
is tools plus a transport, and the tools are the half that carries the value. They
are the same functions whether the caller is a model, the VS Code session, or this
router. When a brain arrives it replaces the router — `judy.py` does not change,
because the loop only ever asks for a string back.

## Session voice — built 9/17

The direction Papi actually wanted: talk to **Fable**, and JUDY is the voice.

```
python _tools/dictation/judy.py --session
```

Hold the hotkey with the Claude Code chat box focused. Your words are transcribed,
repaired, pasted into the box and sent. Fable answers in the chat as usual — no API,
no key, the Pro plan. `reader.py` follows the session's transcript on disk
(`~/.claude/projects/<repo>/<session>.jsonl`) and Blondie reads each block Fable
writes **as it lands**, sentence by sentence, one sentence synthesizing while the
previous plays. A new turn from you cuts her off mid-sentence and plays an
acknowledgment ("Copy." · "On it." · "Stand by.") so the wait has a voice.

| Piece | What |
|---|---|
| `reader.py` | the reader — tails the transcript, speech-forms each block, drives the mouth. `--test` speaks the last block Fable wrote |
| `judy.py --session` | the face + the ears pointed at the chat + the reader in one process |
| `_PRIVATE/voice-acks/` | the acknowledgment bank, rendered once by Blondie |
| judy.json → `session` | `reader` script/haiku · `max_sentences` · `acks` — the Wire panel in the console sets them |

**Speech form.** Replies are written for the eye. A reply that opens with
`<!-- say: … -->` is spoken as that line only — SOP §7 rule 10, Fable's side of the
bargain. Otherwise the reader strips markdown, skips code blocks and tables, reads
links by label, and stops after the cap with "the rest is on screen." Mode `haiku`
rewrites each block into talk through the bundled `claude.exe` first: conversational,
two to three seconds slower a block, spends Pro usage.

**The seconds.** Your words into the chat under a second after release · the
acknowledgment instant · her first sentence ~0.4 s after Fable's first sentence
exists · then she keeps pace. Fable's own thinking is the only wait, and it is
covered, not cut.

## The wire — built 9/17

`wire.py` is that MCP server: the seven tools above, unchanged, over stdio. The VS
Code session spawns it from `.mcp.json` at the repo root (server name `judy`) and
sees them as tools after a reload. Nothing new sits behind it — no model, no key,
no standing cost; the one dependency is the `mcp` SDK (2.x).

```
python _tools/dictation/wire_probe.py     # spawn it, list the tools, call each once
```

Measured 9/17: connect 1.1 s cold, then 2–5 ms a call for the file readers, ~200 ms
for `blocked`, ~700 ms for `box` (it pings three ports and asks git). It is not
called `mcp.py` because a script's own directory is first on `sys.path` and that name
would shadow the package it imports.

Answers are written to be **spoken**: no markdown, short sentences, and the blocked
table gives you the count and the oldest two rather than reading six cells aloud.

## The voice — ElevenLabs

**Ruled 9/16: Piper now, ElevenLabs eventually — and "eventually" arrived the same day.**
Three engines behind one `say()`, so the engine is a config line, not a rewrite.

| Engine | Cost | What it can do |
|---|---|---|
| `sapi` | free | Windows built-in. Robotic. The floor. |
| `piper` | free | Local neural, ~23x realtime, offline. Level delivery — the attitude can only live in word choice. |
| `elevenlabs` | paid | **The only one that can act.** `stability` and `style` are real delivery dials. |

### The key — this repo is public

`github.com/leechseed/_setsunadev` is public, so the key never goes in `judy.json`,
`config.json`, or anything git tracks. It is read from, in order:

1. `ELEVENLABS_API_KEY` (or `ELEVEN_API_KEY` / `XI_API_KEY`) in the environment
2. `_PRIVATE/elevenlabs.key` — a one-line file in the gitignored `_PRIVATE/` tree

```
python _tools/dictation/speak.py --key-status    # where it found one, never prints it
python _tools/dictation/speak.py --list-eleven   # the voices on the account
```

With no key, the ElevenLabs path **raises** — it never falls back to Piper silently.
A JUDY that quietly sounds wrong is worse than one that says it is broken.

### The delivery dials

`stability` low lets her vary line to line; high flattens her toward monotone.
`style` pushes the performance. `similarity_boost` holds the source voice.
`speed` runs 0.7–1.2. All four live in the console's Voice panel.

**This is where the TARS "brat" setting finally does something.** On Piper the voice
stayed level no matter what the persona said; the attitude could only be written into
the words. On ElevenLabs it can be performed.

## The console — the mod menu

```
python _tools/dictation/console.py
```

Opens **http://127.0.0.1:8787**. Every knob in one place, turned with a mouse instead
of a ruling. Local server, not a hosted page — it reads your config, sees your mic,
writes files and starts the daemon, none of which a published page can do.

| Panel | What you can actually do |
|---|---|
| **Status** | GPU, CUDA, model, daemon state; one button starts and stops the ears. An honest table of what is built vs unruled. |
| **Ears** | Hotkey, mic (with a **live level meter**), model picker showing which are already downloaded, compute type, type/beep. Writes `config.json`. |
| **Codebook** | Live §8 browser. **Paste a garbled sentence and watch the repair fire.** See the gated rows and why they are held. **Add a row straight into SOP.md.** |
| **Voice** | SAPI engine + voice picker, rate, volume, and a **speak button** to hear it. |
| **Persona** | The TARS dials. Watch the system prompt rewrite itself as you drag them. |
| **Face** | Four state slots — idle, listening, thinking, talking. **Drag a PNG onto a slot**, or paste a path. |
| **Wire** | BUILT 9/17: the MCP server, what it exposes, how to prove it. The trade table stays as the record. |
| **Log** | Live daemon output — every transcription, every §8 hit. |

Panels are `1`–`8`. Dotted terms carry the CK3 hover layer; **Space** locks a tip open.

Settings land in two files, deliberately separate:

| File | Holds | Read by |
|---|---|---|
| `config.json` | the dictation daemon's settings | `ptt.py` |
| `judy.json` | persona, voice, face, wire | the console (and JUDY, when she exists) |

## Run it


```
python _tools/dictation/ptt.py
```

Hold **ctrl+alt+space**, talk, release. The text lands in whatever window has focus.
`esc+q` quits.

```
python _tools/dictation/ptt.py --toggle        # press to start, press to stop
python _tools/dictation/ptt.py --once --no-type # one capture, print only
python _tools/dictation/ptt.py --file take.wav  # transcribe a file, no mic
python _tools/dictation/ptt.py --list-devices
```

Settings live in `config.json`; any flag overrides it for one run.

## Why it works — the 9/3 diagnosis

The mic was never the problem. Common words land clean; **proper nouns and numbers
garble**, because the recognizer has no vocabulary and guesses the nearest real word.
Whisper has no dictionary. So two levers, and this tool pulls both:

| Lever | Where | What it does |
|---|---|---|
| **BIAS** | `initial_prompt` | The Command lexicon is read by the model *before* every utterance, steering spelling before the guess is made. |
| **REPAIR** | `codebook.apply()` | SOP §8's garble table runs over the transcript *after*, catching what bias missed. |

A fine-tune is the third lever and is unnecessary.

## SOP §8 *is* the dictionary

This was the whole argument for BUILD over INSTALL. `codebook.py` parses
[SOP.md](../../SOP.md) §8 live on every run. There is no second copy to drift.
Add a row to §8 and the tool has it next launch.

### What it refuses to replace

§8 is a read-through table written for a human, and a good third of its rows are
context-conditional — *"SLP (in a process context)"*, *"sweep (spoken by habit)"*,
*"standing (in a canning context)"*. Applying those blind would eat ordinary speech:
every "standing" becomes "canning". So rows carrying a context qualifier are parsed,
counted, and left **off**. `--aggressive` turns them on for one run. They are never
applied silently.

```
python _tools/dictation/codebook.py              # what parsed, what is gated and why
python _tools/dictation/codebook.py --lexicon    # the initial_prompt
python _tools/dictation/codebook.py --test "hau copy run the black room"
```

## Growing the table

§8 grows a row per catch — that is its stated job, and this tool is now its second
consumer. Its own first run caught three:

```
borsite      -> boresight
Poppy        -> Papi
darkroom     -> DARKROOM
```

All three are in §8 now. When something garbles, add the row; do not patch the tool.

## The box

- **GPU:** CTranslate2 sees the 3090 (`cuda`, `float16`) even though this box's torch
  is CPU-only — faster-whisper does not use torch. Falls back to CPU `int8` on its own.
- **Measured:** 11.4s of speech transcribed in **0.69s**; model loads in ~2.9s warm,
  ~28s the first time (it downloads ~1.5 GB once).
- **Model:** `distil-large-v3` — near large-v3 accuracy on proper nouns, which is the
  actual complaint, at a fraction of the latency. English-only, which matches how Papi
  dictates. Change it in `config.json`.
- **Typing:** clipboard + Ctrl-V, not synthetic keystrokes — instant regardless of
  length, and it does not mangle punctuation. The prior clipboard is restored.

## Papi-side hygiene (regardless of the tool)

- Years as "twenty oh five", not "two thousand five".
- Critical proper nouns slightly slower, once; spell a new name the first time.
- Headset a few inches off at a consistent distance; input ~70–80%; audio enhancements
  off if the tool fights them. Mic gear lives in **the corner**.

## Files

| File | What |
|---|---|
| `ptt.py` | the daemon — hotkey, capture, transcribe, repair, type |
| `codebook.py` | SOP §8 parser — the lexicon and the replacement table |
| `config.json` | hotkey, model, device, mic |
| `console.py` | the mod menu — local server on :8787 |
| `console.html` | its page |
| `judy.json` | persona, voice, face, wire (BOLO 56) — **never the key** |
| `speak.py` | the mouth — sapi · piper · elevenlabs behind one `say()` |
| `judy.py` | **the loop** — face window, ears, brain, mouth |
| `brain.py` | the tool layer — what she can actually answer |
| `wire.py` | **the wire** — brain.py's seven tools as an MCP server over stdio (BOLO 56) |
| `wire_probe.py` | spawns the wire and calls every tool once; the proof |
| `reader.py` | **session voice** — follows the VS Code session's transcript and reads Fable aloud as she writes |
| `../../.mcp.json` | registers the wire with the VS Code session as server `judy` |
| `audition.py` | try candidate voices on the real script |
| `faces/` | the four state PNGs |
| `_PRIVATE/elevenlabs.key` | the key, gitignored, untracked |
| `faces/` | the PNG state slots |

Related: **SOP §8** · **BOLO 26** · **BOLO 56 (JUDY)** ·
[oscar-mike/dictation-dictionary.md](../../oscar-mike/dictation-dictionary.md) ·
[[the corner]]
