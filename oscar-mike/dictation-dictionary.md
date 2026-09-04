---
parked: 2026-09-03
title: The Dictation Dictionary
handle: dictation dictionary
tags: [dictation, whisper, tooling, OPERATOR, SOP-8, BOLO-26]
status: parked
open-decision: "the route — BUILD (Claude writes the push-to-talk tool) vs INSTALL (whisper-writer / Whispering, verify both) vs PAY (Wispr Flow / Aqua Voice, against budget)"
---

# The Dictation Dictionary — parked on the route ruling

Card for **BOLO 26**. Everything walked on 9/3 is here; pick-up needs no re-derivation.

## Diagnosis (ruled in-chat 9/3)
- Not the mic. Common words land clean; **proper nouns and numbers garble** (Ultrasin → ultrasound/AutoSun · Blender → blamer · DOCTRINE 0 → Doctor NZero · SOP → SLP · how copy → hau copy). That is a recognizer with no vocabulary, guessing the nearest real word.
- Claude never hears audio; the fix lives upstream, in the speech-to-text layer.

## Mechanism
- **Whisper has no dictionary.** Two levers: (1) the **initial prompt** — text the model reads before every utterance, biasing spellings toward the house lexicon; (2) **post-transcription replacement** — a find/replace table over the transcript. Every "custom dictionary" feature in a Whisper front-end is one or both. A fine-tune is the third lever; unnecessary.
- **The replacement table already exists:** SOP §8 Dictation codebook (standing garble table, grows a row per catch).

## The three routes
| Route | What | Cost | Note |
|---|---|---|---|
| **BUILD** | Claude writes it: hotkey → record → local faster-whisper (GPU, the YOLO box) with the lexicon as prompt → SOP §8 replacements → type into the focused window | $0, one evening | codebook stays in sync because it *is* the SOP |
| **INSTALL** | open-source push-to-talk front-end with prompt + replacements; candidates to verify: whisper-writer (savbell) · Whispering (epicenter) | $0 | verify Windows support + prompt/replacement features before committing |
| **PAY** | Wispr Flow · Aqua Voice — personal dictionary built in | monthly | against the zero-budget posture |

## Lexicon seed (the prompt)
Ultrasin · Bold Venture · BVX · DARKROOM · BOLO · boresight · Oscar Mike · ENDEX · buttonhook · break-break · sit rep · how copy · Dramatica · Blender · MCDP · DCUS · Tori · Anna Colson Conway · Papi · main effort · PMCS · Ready Rack · Magazine · SOP · DOCTRINE 0

## Papi-side hygiene (regardless of route)
- Years as "twenty oh five", not "two thousand five". Critical proper nouns slightly slower, once; spell a new name the first time.
- Headset/boom mic a few inches off, consistent distance; input ~70–80%; audio enhancements off if the tool fights them.

## Resume
The route ruling. On BUILD: Claude ships the tool same session. On INSTALL: verify the two candidates (Windows · prompt · replacements) then configure. On PAY: pick one, load the lexicon.

Related: SOP §8 · BOLO 26 · [[the corner]] (mic/desk gear lives there)
