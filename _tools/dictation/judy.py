"""
judy.py — the loop. Ears, face, brain, mouth, running as one thing.

BOLO 56. Everything before this was a part; this is JUDY.

    hold the hotkey  ->  face: listening
    release          ->  face: thinking   (faster-whisper on the 3090, SOP §8 repair)
    brain answers    ->  face: talking    (ElevenLabs, or Piper offline)
    done             ->  face: idle

    python judy.py                 # face window + the loop
    python judy.py --no-face       # terminal only
    python judy.py --type "text"   # skip the mic, test brain + mouth

The face is a frameless always-on-top window. Drag it anywhere; it remembers where.
Right-click it to quit.

The brain is `brain.py` — a keyword router over the repo today, a language model
later. Swapping it does not touch this file: the loop asks for a string back.
"""

import argparse
import io
import json
import os
import queue
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import brain  # noqa: E402
import codebook  # noqa: E402
import speak  # noqa: E402

JUDY = os.path.join(HERE, "judy.json")
POS = os.path.join(HERE, "_facepos.json")
STATES = ("idle", "listening", "thinking", "talking")


def cfg():
    try:
        return json.load(io.open(JUDY, encoding="utf-8"))
    except Exception:
        return {}


def dcfg():
    try:
        return json.load(io.open(os.path.join(HERE, "config.json"), encoding="utf-8"))
    except Exception:
        return {}


# ---------------------------------------------------------------- the face

class Face:
    """
    A frameless always-on-top window showing one PNG per state.

    Tk must own the main thread, so the loop runs in a worker and talks to the face
    through a queue this polls. Nothing here blocks.
    """

    def __init__(self, size=220):
        import tkinter as tk
        from PIL import Image, ImageTk

        self.q = queue.Queue()
        self.state = "idle"
        self.tk = tk
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg="#0F1216")

        slots = (cfg().get("face", {}) or {}).get("slots", {}) or {}
        self.img = {}
        for s in STATES:
            p = slots.get(s)
            if p and os.path.exists(p):
                im = Image.open(p).convert("RGBA").resize((size, size), Image.LANCZOS)
                bg = Image.new("RGBA", im.size, (15, 18, 22, 255))
                self.img[s] = ImageTk.PhotoImage(Image.alpha_composite(bg, im))
        if not self.img:
            raise RuntimeError("no faces registered — drop PNGs in the console's Face panel")

        self.label = tk.Label(self.root, bd=0, highlightthickness=0, bg="#0F1216")
        self.label.pack()
        self.cap = tk.Label(self.root, text="idle", bg="#0F1216", fg="#7B8492",
                            font=("Consolas", 9), wraplength=size, justify="left",
                            anchor="w", padx=8, pady=5)
        self.cap.pack(fill="x")

        self._paint("idle")
        self._place(size)
        self._drag()
        self.root.bind("<Button-3>", lambda e: self.stop())
        self.root.after(80, self._pump)

    def _place(self, size):
        try:
            p = json.load(io.open(POS, encoding="utf-8"))
            self.root.geometry(f"+{int(p['x'])}+{int(p['y'])}")
        except Exception:
            sw = self.root.winfo_screenwidth()
            sh = self.root.winfo_screenheight()
            self.root.geometry(f"+{sw - size - 60}+{sh - size - 180}")

    def _drag(self):
        d = {}

        def down(e):
            d["x"], d["y"] = e.x_root, e.y_root
            d["gx"] = self.root.winfo_x()
            d["gy"] = self.root.winfo_y()

        def move(e):
            if "x" not in d:
                return
            x = d["gx"] + (e.x_root - d["x"])
            y = d["gy"] + (e.y_root - d["y"])
            self.root.geometry(f"+{x}+{y}")

        def up(_e):
            try:
                io.open(POS, "w", encoding="utf-8").write(
                    json.dumps({"x": self.root.winfo_x(), "y": self.root.winfo_y()}))
            except Exception:
                pass
            d.clear()

        for w in (self.label, self.cap):
            w.bind("<Button-1>", down)
            w.bind("<B1-Motion>", move)
            w.bind("<ButtonRelease-1>", up)

    def _paint(self, state):
        im = self.img.get(state) or self.img.get("idle")
        if im:
            self.label.configure(image=im)
            self.label.image = im

    def _pump(self):
        try:
            while True:
                kind, val = self.q.get_nowait()
                if kind == "state":
                    self.state = val
                    self._paint(val)
                    if val != "idle":
                        self.cap.configure(text=val, fg="#FF8F62")
                elif kind == "text":
                    self.cap.configure(text=val, fg="#A9B0BC")
                elif kind == "quit":
                    self.root.destroy()
                    return
        except queue.Empty:
            pass
        self.root.after(80, self._pump)

    def set(self, state):
        self.q.put(("state", state))

    def say(self, text):
        self.q.put(("text", text))

    def stop(self):
        self.q.put(("quit", None))

    def run(self):
        self.root.mainloop()


class NoFace:
    """Same interface, no window — for --no-face and for headless testing."""

    def set(self, state):
        print(f"  [{state}]")

    def say(self, text):
        print(f"  {text}")

    def stop(self):
        pass

    def run(self):
        try:
            while True:
                time.sleep(0.3)
        except KeyboardInterrupt:
            pass


# ---------------------------------------------------------------- the loop

class Loop:
    def __init__(self, face, engine, hotkey, speak_replies=True):
        self.face = face
        self.engine = engine
        self.hotkey = hotkey
        self.speak_replies = speak_replies
        self.rec = None
        self.busy = threading.Lock()

    def turn(self, heard):
        """One exchange. Heard text in, spoken answer out."""
        if not heard:
            self.face.set("idle")
            return
        print(f"\n  you  > {heard}")
        self.face.say(f"you: {heard}")
        self.face.set("thinking")
        reply, tool = brain.answer(heard)
        if not reply:
            self.face.set("idle")
            return
        print(f"  judy > {reply}")
        self.face.say(reply)
        self.face.set("talking")
        if self.speak_replies:
            try:
                speak.say(reply, blocking=True)
            except Exception as e:
                print(f"  ! mouth failed: {e}")
        self.face.set("idle")

    def listen_once(self):
        import ptt
        if not self.busy.acquire(blocking=False):
            return
        try:
            self.face.set("listening")
            self.rec.start()
            while self.held():
                time.sleep(0.03)
            audio = self.rec.stop()
            self.face.set("thinking")
            text, meta = self.engine.transcribe(audio)
            if meta.get("hits"):
                for h, r, _n in meta["hits"]:
                    print(f"         §8 {h!r} -> {r!r}")
            self.turn(text)
        except Exception as e:
            print(f"  ! turn failed: {e}")
            self.face.set("idle")
        finally:
            self.busy.release()

    def held(self):
        import keyboard
        return all(keyboard.is_pressed(k) for k in self.hotkey.split("+"))

    def run(self):
        import keyboard
        import ptt
        self.rec = ptt.Recorder(dcfg().get("input_device"))
        last = self.hotkey.split("+")[-1]
        keyboard.on_press_key(
            last, lambda _e: threading.Thread(
                target=self.listen_once, daemon=True).start()
            if self.held() else None, suppress=False)
        print(f"\n  ready · HOLD {self.hotkey} and talk · right-click the face to quit\n")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="JUDY — the loop (BOLO 56)")
    ap.add_argument("--no-face", action="store_true")
    ap.add_argument("--no-voice", action="store_true", help="print replies, don't speak")
    ap.add_argument("--type", help="skip the mic: one typed turn, then exit")
    ap.add_argument("--size", type=int, default=220)
    a = ap.parse_args()

    v = cfg().get("voice", {})
    print("JUDY · BOLO 56")
    print(f"  mouth  {v.get('engine', 'piper')}"
          + (f" · {v.get('eleven_voice_id', '')[:12]}…" if v.get("engine") == "elevenlabs" else ""))

    face = NoFace() if (a.no_face or a.type) else Face(a.size)

    if a.type:
        Loop(face, None, "", speak_replies=not a.no_voice).turn(a.type)
        return

    print("  ears   loading whisper…")
    import ptt
    engine = ptt.Engine({**ptt.DEFAULTS, **dcfg(), "aggressive": dcfg().get("aggressive", False)})
    loop = Loop(face, engine, dcfg().get("hotkey", ptt.DEFAULTS["hotkey"]),
                speak_replies=not a.no_voice)
    loop.run()
    face.run()


if __name__ == "__main__":
    main()
