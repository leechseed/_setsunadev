# Dictation — BOLO 26, the BUILD route

**Ruled 2026-09-16** (Papi: "build"). Push-to-talk speech-to-text that stops mangling
the Command lexicon. Local, GPU, $0 — no audio leaves the box, nothing is billed.

This is **JUDY's listening half** (BOLO 56). The speaking half, the wire to the VS Code
session, and the face are still unruled.

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
| **Wire** | The one open call a knob cannot answer, with the trade laid out. |
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
| `judy.json` | persona, voice, face, wire (BOLO 56) |
| `faces/` | the PNG state slots |

Related: **SOP §8** · **BOLO 26** · **BOLO 56 (JUDY)** ·
[oscar-mike/dictation-dictionary.md](../../oscar-mike/dictation-dictionary.md) ·
[[the corner]]
