"""
judy.py — the loop. Ears, face, brain, mouth, running as one thing.

BOLO 56. Everything before this was a part; this is JUDY.

    hold the hotkey  ->  face: listening
    release          ->  face: thinking   (faster-whisper on the 3090, SOP §8 repair)
    brain answers    ->  face: talking    (ElevenLabs, or Piper offline)
    done             ->  face: idle

    python judy.py                 # face window + the loop
    python judy.py --toggle        # press to start, press again to stop
    python judy.py --no-face       # terminal only
    python judy.py --type "text"   # skip the mic, test brain + mouth

The face is a frameless always-on-top window. Drag it anywhere; it remembers where.
Right-click it to quit.

Two triggers, either or both: the keyboard hotkey, and a MIDI pad once one has been
learned (`python midipad.py --learn`). Both drive the same two calls.

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
    """
    One exchange at a time, however it is triggered.

    Two triggers exist and they share the same two calls, so nothing downstream knows
    or cares which fired: a keyboard hotkey and a MIDI pad. Two shapes too — hold
    (down starts, up transcribes) and toggle (a press starts, the next press ends).
    A pad wants toggle; holding a capacitive pad for thirty seconds is unpleasant.
    """

    def __init__(self, face, engine, hotkey, speak_replies=True, toggle=False, session=False):
        self.face = face
        self.engine = engine
        self.hotkey = hotkey
        self.speak_replies = speak_replies
        self.toggle = toggle
        self.session = session   # session voice: paste into the chat + Enter; the reader speaks
        self.rec = None
        self.open = False
        self.busy = threading.Lock()

    def turn(self, heard):
        """One exchange. Heard text in, spoken answer out."""
        if not heard:
            self.face.set("idle")
            return
        print(f"\n  you  > {heard}")
        self.face.say(f"you: {heard}")
        self.face.set("thinking")
        if self.session:
            # the words go to whatever has focus — the Claude Code chat box — and
            # Enter sends the turn. Fable answers; reader.py speaks it as it lands.
            import keyboard
            import ptt
            ptt.type_out(heard)
            time.sleep(0.05)
            keyboard.send("enter")
            return
        reply, _tool = brain.answer(heard)
        if not reply:
            self.face.set("idle")
            return
        print(f"  judy > {reply}")
        self.face.say(reply)
        self.face.set("talking")
        if self.speak_replies:
            try:
                import squelch
                squelch.key_up()
                speak.say(reply, blocking=True)
                squelch.key_down()
            except Exception as e:
                print(f"  ! mouth failed: {e}")
        self.face.set("idle")

    # -- the two calls every trigger uses
    def start(self, src="key"):
        if self.open or not self.busy.acquire(blocking=False):
            return
        self.open = True
        self.face.set("listening")
        if self.session:
            # Chief 9/17: the pad brings VS Code forward and puts the cursor in the chat box.
            # Runs beside the recorder so the mic opens on time; the paste lands after.
            import focus
            if focus.wants_focus(src):
                threading.Thread(target=focus.focus_claude, daemon=True).start()
        try:
            self.rec.start()
        except Exception as e:
            print(f"  ! mic failed: {e}")
            self.open = False
            self.face.set("idle")
            self.busy.release()

    def finish(self):
        if not self.open:
            return
        self.open = False
        try:
            audio = self.rec.stop()
            self.face.set("thinking")
            text, meta = self.engine.transcribe(audio)
            for h, r, _n in (meta.get("hits") or []):
                print(f"         §8 {h!r} -> {r!r}")
            self.turn(text)
        except Exception as e:
            print(f"  ! turn failed: {e}")
            self.face.set("idle")
        finally:
            try:
                self.busy.release()
            except RuntimeError:
                pass

    def fire(self, src="key"):
        """A trigger pulse. Hold mode uses start/finish directly; toggle uses this."""
        if self.open:
            threading.Thread(target=self.finish, daemon=True).start()
        else:
            self.start(src)

    def held(self):
        import keyboard
        return all(keyboard.is_pressed(k) for k in self.hotkey.split("+"))

    def run(self):
        import keyboard
        import ptt
        import midipad
        self.rec = ptt.Recorder(dcfg().get("input_device"))

        # -- keyboard
        last = self.hotkey.split("+")[-1]
        if self.toggle:
            keyboard.add_hotkey(self.hotkey, self.fire, suppress=False)
        else:
            keyboard.on_press_key(
                last, lambda _e: self.start() if self.held() else None, suppress=False)
            keyboard.on_release_key(last, lambda _e: threading.Thread(
                target=self.finish, daemon=True).start(), suppress=False)

        # -- MIDI pad, if one has been learned
        self.pad = None
        if dcfg().get("midi_note") is not None:
            # the focus pad (Chief 9/17): the pad beside the talk pad brings VS Code forward
            # and puts the cursor in the Claude Code box; the talk pad stays as it was
            extra = {}
            if self.session and dcfg().get("focus_note") is not None:
                import focus
                extra[int(dcfg()["focus_note"])] = (
                    lambda: threading.Thread(target=focus.focus_claude, daemon=True).start(), lambda: None)
            if self.toggle:
                self.pad = midipad.PadListener(lambda: self.fire("pad"), lambda: None, extra=extra)
            else:
                self.pad = midipad.PadListener(
                    lambda: self.start("pad"),
                    lambda: threading.Thread(target=self.finish, daemon=True).start(), extra=extra)
            if self.pad.start():
                c = dcfg()
                print(f"  pad    note {c['midi_note']} on {c.get('midi_port')}"
                      + (f" · focus pad note {c['focus_note']}" if c.get("focus_note") is not None else " · no focus pad (midipad.py --learn-focus)"))
            else:
                print(f"  pad    unavailable: {self.pad.error}")

        shape = "PRESS to start, press again to stop" if self.toggle else f"HOLD {self.hotkey}"
        extra = " (or the pad)" if self.pad and not self.pad.error else ""
        print(f"\n  ready · {shape}{extra} · right-click the face to quit\n")


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
    ap.add_argument("--toggle", action="store_true",
                    help="press to start, press again to stop (best for a pad)")
    ap.add_argument("--session", action="store_true",
                    help="session voice: your words go into the VS Code chat, and the "
                         "reader speaks Fable's replies as they are written")
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
                speak_replies=not a.no_voice,
                toggle=a.toggle or bool(dcfg().get("toggle")),
                session=a.session)
    loop.run()
    if a.session:
        import reader
        rd = reader.Reader(face=face)
        print(f"  voice  session · reader={rd.cfg.get('reader')} · keep the chat box focused")
        threading.Thread(target=rd.run, daemon=True).start()
    face.run()


if __name__ == "__main__":
    main()
