---
title: RECON — the local voice for JUDY (BOLO 56)
type: recon
rung: handbook
date: 2026-09-17
status: boresight read delivered, awaiting HOTLINE ACTUAL's clear
ordered_by: Chief ("boresight local voice", 9/17, after "I thought we were building this thing to be on my 3090, locally run, one hundred percent fidelity")
crew: one MS (sonnet) on WebSearch/WebFetch only; the CDR ruled the shortlist below
---

# The question

Which open, locally-run neural TTS engine can replace ElevenLabs as JUDY's mouth on the 3090, given: fully local (no text or audio leaves the box) · a female British voice in the affable, bratty 007-handler register · real delivery control (the brat dial ElevenLabs gave us via stability/style) · a 3–8 s line in well under a second once warm · coexisting on the GPU with faster-whisper distil-large-v3 at float16 (~1.6 GB).

# The read, one line each

| Engine | License | VRAM | Speed (published) | Delivery control | British female | Windows | Health |
|---|---|---|---|---|---|---|---|
| **Chatterbox / Turbo** (Resemble) | MIT, weights too | ~2–4 GB (unofficial) | RTF ~0.5, first chunk ~470 ms on a **4090**; 3090 unmeasured | `exaggeration` + `cfg_weight`, continuous dials | zero-shot clone from 5–20 s clip; demo default is British | native pip; **trap: pip downgrades torch to CPU, install CUDA torch first then `--no-deps`** | active, v0.1.2, commits into 7/2026 |
| **Zonos v0.1** (Zyphra) | Apache 2.0 | 6 GB+ | ~2× realtime on a 4090; 3090 unmeasured | 8-D emotion vector + rate/pitch/quality: the deepest dial set | clone from reference; no preset | **Linux/WSL2 steered**; third-party Windows port exists | attention moved to Zonos2; v0.1 upkeep unclear |
| **Qwen3-TTS** (Alibaba, 1/2026) | Apache 2.0 | unverified | sub-50 ms TTFA claimed by a third-party server | natural-language instruction ("speak happily") | VoiceDesign can describe one | native | young, real momentum |
| Higgs Audio v3 (Boson) | non-commercial | 18–20 GB for cloning | — | rich inline emotion/style/prosody | clone | one-click portable Windows app | tight on VRAM beside Whisper |
| Orpheus | Apache 2.0 | 8 GB quantized, 12–15 full | ~200 ms via vLLM | discrete tags `<laugh>` `<sigh>` | 8 stock voices, no confirmed British | native | ok |
| Dia / Dia2 (Nari) | Apache 2.0 | 10 GB / 12+ GB | inconsistent; open issue "RTF > 1" | bracket tags (laughs, coughs) | clone, English only | CUDA only | young |
| CosyVoice 2 | Apache 2.0 | — | RTF 0.11 streaming, 150 ms | none documented | unconfirmed | **pynini / ttsfrd / sox: Windows-hostile** | ok |
| Fish Speech / OpenAudio S1 | code Apache, **weights non-commercial** | S2 wants ~24 GB (no room) | RTF ~0.14–0.2 on 4090/H200 | some | clone | native | ok |
| F5-TTS | code MIT, weights non-commercial | modest | **RTF ~3, slower than realtime** | none | clone | native | ok |
| XTTS-v2 (Coqui) | weights non-commercial, no license path (Coqui closed 2024) | ~2 GB | sub-200 ms streaming claimed | none | clone | native via idiap fork | archived upstream |
| Kokoro-82M | Apache 2.0 | <1 GB | 100×+ realtime | **none, tags ignored** | built-in British female voices | native | active |
| Piper (baseline) | GPL-3 fork | CPU | 23× realtime here | none | en_GB on disk | in place | archived upstream |

Fails on the requirement that matters (delivery control): Kokoro, Piper, XTTS, F5, CosyVoice. Fails on room or license: Higgs, Fish. Fails on speed evidence: Dia, F5.

# The shortlist

1. **Chatterbox Turbo** — the only one that clears all five without a major asterisk. MIT. Two continuous dials that map straight onto the two ElevenLabs dials we already tune in the console. Small. Native Windows. Alive.
2. **Zonos v0.1** — the richest emotion surface, at the price of a Windows fight.
3. **Qwen3-TTS** — prompt-driven delivery like ElevenLabs' style prompt, but the emotion instruction and the voice clone are not confirmed to compose on one voice.

# What is not verified and only the box can settle

- **No 3090 numbers exist for any of the three.** Every speed figure is a 4090 or a server. The 3090 is roughly 60–70 % of a 4090; Chatterbox's ~0.5 RTF should still land a 5 s line under a second warm, but that is arithmetic, not a measurement.
- **The register.** Whether `exaggeration`/`cfg_weight` on a British reference clip produces "affable, bratty" rather than "shouty" is a listening test. Documentation cannot answer it.
- **The reference clip.** Chatterbox clones from 5–20 s of audio; there is no shelf voice. The clip has to come from somewhere legitimate: a public-domain British female reading (LibriVox), a clip Chief records with a collaborator, or a voice Chief designs. Cloning Blondie from the ElevenLabs auditions on disk is the obvious shortcut and the wrong one until the ElevenLabs terms on downstream use of generated audio are read.
- **Fidelity.** One blind-test writeup puts Chatterbox Turbo ahead of ElevenLabs (65 % to 25 %); single source, unreproduced. Treat "100 % fidelity" as a target to measure, not a fact.

# Cost of the build, if cleared

- CUDA torch on this box (the box's torch is CPU-only today; faster-whisper reaches the 3090 through CTranslate2, not torch). One install, ~2.5 GB download, plus the known Chatterbox pip trap.
- A fourth engine behind `speak.py`'s `say()`: `chatterbox`, with `exaggeration` and `cfg_weight` mapped to the console's existing persona dials. Same WAV path as Piper, no ffmpeg.
- An audition run: the same four-line script the ElevenLabs cast read, on three reference clips and three dial settings, into `_PRIVATE/voice-auditions/local/`. Measured warm latency on the 3090 per line.
- $0 standing. ElevenLabs stays wired as the paid option; Piper stays as the offline floor.

# Sources

Chatterbox: https://github.com/resemble-ai/chatterbox · https://huggingface.co/ResembleAI/chatterbox-turbo · https://www.resemble.ai/learn/models/chatterbox-turbo · https://huggingface.co/ResembleAI/chatterbox/discussions/10 · https://github.com/resemble-ai/chatterbox/issues/159 · https://github.com/davidbrowne17/chatterbox-streaming
Zonos: https://github.com/Zyphra/Zonos · https://huggingface.co/Zyphra/Zonos-v0.1-hybrid · https://github.com/Zyphra/Zonos/issues/92 · https://github.com/Foadsf/zonos-windows-tts · https://github.com/Zyphra/ZONOS2
Qwen3-TTS: https://github.com/QwenLM/Qwen3-TTS · https://github.com/QwenLM/Qwen3-TTS/discussions/231 · https://github.com/nari-labs/nari-qwen3-tts
Higgs: https://huggingface.co/bosonai/higgs-audio-v3-tts-4b · https://github.com/boson-ai/higgs-audio/issues/117 · https://github.com/timoncool/HiggsAudio-Studio
Orpheus: https://github.com/Lex-au/Orpheus-FastAPI · https://www.openspeech.dev/models/orpheus-tts
Dia: https://github.com/nari-labs/dia · https://github.com/nari-labs/dia/issues/153 · https://github.com/nari-labs/dia2
CosyVoice: https://github.com/FunAudioLLM/CosyVoice · https://github.com/FunAudioLLM/CosyVoice/issues/1046 · https://arxiv.org/html/2412.10117v1
Fish: https://github.com/fishaudio/fish-speech/issues/1096 · https://huggingface.co/fishaudio/openaudio-s1-mini/discussions/7
F5: https://huggingface.co/SWivid/F5-TTS/blob/main/README.md · https://github.com/SWivid/F5-TTS/issues/81
XTTS: https://huggingface.co/coqui/XTTS-v2 · https://github.com/idiap/coqui-ai-TTS
Kokoro: https://huggingface.co/hexgrad/Kokoro-82M
Whisper VRAM: https://www.spheron.network/tools/gpu-recommender/distil-whisper/distil-large-v3/
