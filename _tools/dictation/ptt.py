"""
ptt.py — push-to-talk dictation for the Command.

BOLO 26, BUILD route (ruled 2026-09-16 on Chief's "build").

    hold a hotkey → record → faster-whisper on the 3090, the Command lexicon fed in
    as initial_prompt → SOP §8 replacements → typed into whatever window has focus.

Zero budget: everything here is local. No audio leaves the box, nothing is billed.

The two levers, both from the 9/3 diagnosis — Whisper has no dictionary, so:
  1. BIAS   `initial_prompt` carries the lexicon, steering spelling before the guess.
  2. REPAIR `codebook.apply()` runs SOP §8 over the transcript after the guess.
Lever 2 is the safety net for what lever 1 misses; neither invents a dictionary.

    python ptt.py                    # daemon, hold ctrl+alt+space to talk
    python ptt.py --toggle           # press once to start, again to stop
    python ptt.py --once --no-type   # one capture, print it, type nothing
    python ptt.py --file take.wav    # transcribe a file (no mic, for testing)
    python ptt.py --list-devices
"""

import argparse
import io
import json
import os
import queue
import sys
import threading
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import codebook  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(HERE, "config.json")
SR = 16000  # what Whisper wants; resampling anywhere else is wasted work

DEFAULTS = {
    "hotkey": "ctrl+alt+space",
    # distil-large-v3 is the responsiveness/accuracy pick: near large-v3 on proper
    # nouns — which is the whole complaint — at a fraction of the latency. English
    # only, which matches how Chief dictates. ~1.5 GB, downloaded once.
    "model": "distil-large-v3",
    "device": "auto",
    "compute_type": "auto",
    "input_device": None,
    "aggressive": False,
    "type_output": True,
    "beep": True,
}


def load_config():
    cfg = dict(DEFAULTS)
    if os.path.exists(CONFIG):
        try:
            cfg.update(json.load(io.open(CONFIG, encoding="utf-8")))
        except Exception as e:
            print(f"  ! config.json unreadable ({e}); using defaults")
    return cfg


def pick_device(cfg):
    """CTranslate2 sees the GPU even though this box's torch is CPU-only."""
    import ctranslate2
    dev, ct = cfg["device"], cfg["compute_type"]
    if dev == "auto":
        try:
            dev = "cuda" if ctranslate2.get_cuda_device_count() > 0 else "cpu"
        except Exception:
            dev = "cpu"
    if ct == "auto":
        ct = "float16" if dev == "cuda" else "int8"
    return dev, ct


class Recorder:
    """Mic → a list of float32 frames. Started and stopped by the hotkey."""

    def __init__(self, input_device=None):
        self.input_device = input_device
        self.q = queue.Queue()
        self.stream = None

    def _cb(self, indata, frames, t, status):
        if status:
            pass  # overflows are noisy and not worth interrupting a transmission
        self.q.put(indata.copy())

    def start(self):
        import sounddevice as sd
        while not self.q.empty():
            self.q.get_nowait()
        self.stream = sd.InputStream(
            samplerate=SR, channels=1, dtype="float32",
            device=self.input_device, callback=self._cb, blocksize=0,
        )
        self.stream.start()

    def stop(self):
        import numpy as np
        if self.stream is None:
            return np.zeros(0, dtype="float32")
        self.stream.stop()
        self.stream.close()
        self.stream = None
        chunks = []
        while not self.q.empty():
            chunks.append(self.q.get_nowait())
        if not chunks:
            return np.zeros(0, dtype="float32")
        return np.concatenate(chunks, axis=0).reshape(-1)


def beep(up=True):
    try:
        import winsound
        winsound.Beep(880 if up else 440, 60)
    except Exception:
        pass


def type_out(text):
    """
    Clipboard + Ctrl-V, not synthetic keystrokes: it is instant regardless of length
    and it does not mangle punctuation or unicode. The old clipboard is put back.
    """
    import keyboard
    import pyperclip
    try:
        prior = pyperclip.paste()
    except Exception:
        prior = None
    pyperclip.copy(text)
    time.sleep(0.03)
    keyboard.send("ctrl+v")
    time.sleep(0.12)
    if prior is not None:
        try:
            pyperclip.copy(prior)
        except Exception:
            pass


class Engine:
    def __init__(self, cfg):
        self.cfg = cfg
        self.prompt = codebook.lexicon()
        dev, ct = pick_device(cfg)
        self.device, self.compute_type = dev, ct
        print(f"  model    {cfg['model']}  on {dev} ({ct})")
        print(f"  lexicon  {len(self.prompt.split(', '))} terms as initial_prompt")
        rules = codebook.rules(aggressive=cfg["aggressive"])
        print(f"  codebook {len(rules)} active replacements"
              f"{' (AGGRESSIVE: context-gated rows on)' if cfg['aggressive'] else ''}")
        t0 = time.time()
        from faster_whisper import WhisperModel
        self.model = WhisperModel(cfg["model"], device=dev, compute_type=ct)
        print(f"  loaded   in {time.time() - t0:.1f}s")

    def transcribe(self, audio):
        import numpy as np
        if audio is None or len(audio) < SR * 0.2:
            return "", {}
        peak = float(np.abs(audio).max()) if len(audio) else 0.0
        t0 = time.time()
        segments, info = self.model.transcribe(
            audio,
            language="en",
            initial_prompt=self.prompt,
            vad_filter=True,
            vad_parameters={"min_silence_duration_ms": 300},
            beam_size=5,
            condition_on_previous_text=False,
        )
        raw = " ".join(s.text.strip() for s in segments).strip()
        fixed, hits = codebook.apply(raw, aggressive=self.cfg["aggressive"])
        return fixed, {
            "raw": raw, "hits": hits, "peak": peak,
            "secs": len(audio) / SR, "took": time.time() - t0,
        }


def report(text, meta, cfg):
    if not text:
        print("  (nothing heard)")
        return
    print(f"  heard    {meta['secs']:.1f}s  peak {meta['peak']:.2f}  "
          f"transcribed in {meta['took']:.2f}s")
    if meta["hits"]:
        print(f"  raw      {meta['raw']}")
        for h, r, n in meta["hits"]:
            print(f"           §8  {h!r} -> {r!r}" + (f" ×{n}" if n > 1 else ""))
    print(f"  >>       {text}")


def run_daemon(cfg, engine, toggle=False):
    import keyboard
    rec = Recorder(cfg["input_device"])
    state = {"on": False}
    lock = threading.Lock()

    def begin():
        with lock:
            if state["on"]:
                return
            state["on"] = True
        if cfg["beep"]:
            beep(True)
        print("\n● recording…")
        rec.start()

    def end():
        with lock:
            if not state["on"]:
                return
            state["on"] = False
        audio = rec.stop()
        if cfg["beep"]:
            beep(False)
        print("○ transcribing…")
        text, meta = engine.transcribe(audio)
        report(text, meta, cfg)
        if text and cfg["type_output"]:
            type_out(text)

    hk = cfg["hotkey"]
    if toggle:
        def flip():
            end() if state["on"] else begin()
        keyboard.add_hotkey(hk, flip, suppress=False)
        print(f"\nready · press {hk} to start, again to stop · esc+q quits\n")
    else:
        keyboard.on_press_key(hk.split("+")[-1], lambda _e: (
            begin() if all(keyboard.is_pressed(k) for k in hk.split("+")[:-1]) else None
        ), suppress=False)
        keyboard.on_release_key(hk.split("+")[-1], lambda _e: end(), suppress=False)
        print(f"\nready · HOLD {hk} and talk · esc+q quits\n")

    keyboard.add_hotkey("esc+q", lambda: os._exit(0))
    keyboard.wait()


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    ap = argparse.ArgumentParser(description="Push-to-talk dictation (BOLO 26)")
    ap.add_argument("--model")
    ap.add_argument("--hotkey")
    ap.add_argument("--device", choices=["auto", "cuda", "cpu"])
    ap.add_argument("--input-device", type=int)
    ap.add_argument("--aggressive", action="store_true",
                    help="also apply SOP §8's context-gated rows (see codebook.py)")
    ap.add_argument("--no-type", action="store_true", help="print only, type nothing")
    ap.add_argument("--no-beep", action="store_true")
    ap.add_argument("--toggle", action="store_true", help="press to start, press to stop")
    ap.add_argument("--once", action="store_true", help="one capture, then exit")
    ap.add_argument("--file", help="transcribe a wav instead of the mic")
    ap.add_argument("--list-devices", action="store_true")
    a = ap.parse_args()

    if a.list_devices:
        import sounddevice as sd
        for i, d in enumerate(sd.query_devices()):
            if d["max_input_channels"] > 0:
                mark = "*" if i == sd.default.device[0] else " "
                print(f'{mark}{i:3d}  {d["name"]}')
        return

    cfg = load_config()
    for k, v in [("model", a.model), ("hotkey", a.hotkey), ("device", a.device),
                 ("input_device", a.input_device)]:
        if v is not None:
            cfg[k] = v
    if a.aggressive:
        cfg["aggressive"] = True
    if a.no_type:
        cfg["type_output"] = False
    if a.no_beep:
        cfg["beep"] = False

    print("dictation · BOLO 26 · SOP §8 is the dictionary")
    engine = Engine(cfg)

    if a.file:
        import soundfile as sf
        import numpy as np
        audio, sr = sf.read(a.file, dtype="float32", always_2d=True)
        audio = audio.mean(axis=1)
        if sr != SR:
            idx = (np.arange(int(len(audio) * SR / sr)) * sr / SR).astype(int)
            audio = audio[idx[idx < len(audio)]]
        text, meta = engine.transcribe(audio)
        report(text, meta, cfg)
        return

    if a.once:
        rec = Recorder(cfg["input_device"])
        input("  press Enter to start recording… ")
        if cfg["beep"]:
            beep(True)
        rec.start()
        input("  recording — press Enter to stop… ")
        audio = rec.stop()
        if cfg["beep"]:
            beep(False)
        text, meta = engine.transcribe(audio)
        report(text, meta, cfg)
        if text and cfg["type_output"]:
            type_out(text)
        return

    run_daemon(cfg, engine, toggle=a.toggle)


if __name__ == "__main__":
    main()
