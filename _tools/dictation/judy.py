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
import random
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "yoyo"))   # BOLO 69: _tools/yoyo

import brain  # noqa: E402
import codebook  # noqa: E402
import naked as nk  # noqa: E402   # BOLO 74 (9/20): the second voice in the room
import speak  # noqa: E402

JUDY = os.path.join(HERE, "judy.json")
POS = os.path.join(HERE, "_facepos.json")
LIB = os.path.join(HERE, "faces", "library")    # the face deck's library (10/4 pools read from here)
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

        self.q = queue.Queue()
        self.state = "idle"
        self.tk = tk
        self.size = size
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg="#0F1216")

        self.img = {}       # state -> [(PhotoImage, ms)], one entry for a still, many for a GIF
        self._sig = None    # (path, mtime) per slot, so a swap in the console reloads live
        self._anim = None
        self._frame = 0
        self.pools = {}     # state -> [library paths]; two or more and JUDY picks one each time she enters it
        self.cache = {}     # library path -> [[PIL or PhotoImage, ms]], filled off-thread
        self._last = {}     # state -> the pool face shown last time, so a pick never repeats back to back
        self._load()
        if not self.img:
            raise RuntimeError("no faces registered — drop PNGs or GIFs in the console's Face panel")

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
        self.root.after(1500, self._watch)

    def _slots(self):
        slots = (cfg().get("face", {}) or {}).get("slots", {}) or {}
        return {s: slots.get(s) for s in STATES}

    def _pools(self):
        """10/4: each state's pool of library faces (names in faces/library/); JUDY picks one per entry."""
        pools = (cfg().get("face", {}) or {}).get("pools", {}) or {}
        out = {}
        for s in STATES:
            paths = [os.path.join(LIB, n) for n in (pools.get(s) or [])]
            out[s] = [q for q in paths if os.path.exists(q)]
        return out

    def _signature(self, slots, pools=None):
        pools = self._pools() if pools is None else pools
        sig = lambda p: (p, os.path.getmtime(p) if p and os.path.exists(p) else None)
        return (tuple((s, *sig(p)) for s, p in sorted(slots.items())),
                tuple((s, tuple(sig(q) for q in qs)) for s, qs in sorted(pools.items())))

    def _decode(self, p):
        """Any face file -> [(PIL RGB image at the face size, ms)]. GIF/WebP keep every frame; MP4 via OpenCV.
        300 frames at most. Pure PIL, so it runs off the Tk thread."""
        from PIL import Image, ImageSequence

        n = self.size
        if p.lower().endswith(".mp4"):
            import cv2
            cap = cv2.VideoCapture(p)
            try:
                fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
                step = max(1, round(fps / 30.0))          # a 60 fps clip keeps every second frame
                ms = max(20, int(1000.0 * step / fps))
                frames, i = [], 0
                while len(frames) < 300:
                    ok, bgr = cap.read()
                    if not ok:
                        break
                    i += 1
                    if (i - 1) % step:
                        continue
                    im = Image.fromarray(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB))
                    im.thumbnail((n, n), Image.LANCZOS)   # keep the aspect, letterbox
                    bg = Image.new("RGB", (n, n), (15, 18, 22))
                    bg.paste(im, ((n - im.width) // 2, (n - im.height) // 2))
                    frames.append((bg, ms))
                return frames
            finally:
                cap.release()
        src = Image.open(p)
        frames = []
        for fr in ImageSequence.Iterator(src):
            im = fr.convert("RGBA").resize((n, n), Image.LANCZOS)
            bg = Image.new("RGBA", im.size, (15, 18, 22, 255))
            ms = max(20, int(fr.info.get("duration", src.info.get("duration", 80)) or 80))
            frames.append((Image.alpha_composite(bg, im).convert("RGB"), ms))
            if len(frames) >= 300:
                break
        return frames

    def _load(self):
        """Read every slot now (Tk images); decode the pools in the background."""
        from PIL import ImageTk

        slots = self._slots()
        img = {}
        for s, p in slots.items():
            if not (p and os.path.exists(p)):
                continue
            try:
                frames = [(ImageTk.PhotoImage(im), ms) for im, ms in self._decode(p)]
                if frames:
                    img[s] = frames
            except Exception as e:  # a bad upload must not take the face down
                print(f"face[{s}]: could not read {p}: {e}", file=sys.stderr)
        if img:
            self.img = img
        pools = self._pools()
        self.pools = pools
        self._sig = self._signature(slots, pools)
        want = {q for qs in pools.values() for q in qs}
        for q in list(self.cache):
            if q not in want:
                self.cache.pop(q, None)
        todo = [q for q in want if q not in self.cache]
        if todo:
            threading.Thread(target=self._decode_pool, args=(todo,), daemon=True).start()

    def _decode_pool(self, paths):
        for q in paths:
            try:
                fr = self._decode(q)
                if fr:
                    self.cache[q] = [list(f) for f in fr]   # PIL now; the Tk thread swaps in PhotoImages as it plays
            except Exception as e:
                print(f"face pool: could not read {q}: {e}", file=sys.stderr)

    def _pick(self, state):
        """A pool of two or more: a random ready face, never the last one twice. Else the slot face."""
        ready = [q for q in self.pools.get(state, []) if q in self.cache]
        if len(self.pools.get(state, [])) < 2 or not ready:
            return self.img.get(state) or self.img.get("idle") or []
        choice = [q for q in ready if q != self._last.get(state)] or ready
        q = random.choice(choice)
        self._last[state] = q
        return self.cache[q]

    def _watch(self):
        """Poll judy.json + the slot and pool files; reload when the console swaps one."""
        try:
            if self._signature(self._slots()) != self._sig:
                self._load()
                self._paint(self.state)
        except Exception:
            pass
        self.root.after(1500, self._watch)

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
        if self._anim:
            self.root.after_cancel(self._anim)
            self._anim = None
        self._frames = self._pick(state)
        self._frame = 0
        self._show()

    def _show(self):
        if not self._frames:
            return
        fr = self._frames[self._frame]
        im, ms = fr
        from PIL import Image, ImageTk
        if isinstance(im, Image.Image):                 # a pool frame still in PIL: convert once, keep it
            im = ImageTk.PhotoImage(im)
            if isinstance(fr, list):
                fr[0] = im
        self.label.configure(image=im)
        self.label.image = im
        if len(self._frames) > 1:
            self._frame = (self._frame + 1) % len(self._frames)
            self._anim = self.root.after(ms, self._show)

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
        self.yoyo = False        # BOLO 69: the current hold is a yo-yo, not a turn
        self.naked_hold = False  # BOLO 74: the current hold is for Naked
        self.naked = None        # a naked.Naked once --naked has built her
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
            # the words go to whatever has focus — the Claude Code chat box. They stay
            # there: the SEND pad (the pad above the talk pad) is what sends the turn
            # (Chief 9/17: "press the button on top of it to actually send"). Several
            # holds of the talk pad pile up in the box; the trailing space joins them.
            # judy.json session.send_on_talk = true restores the old auto-send.
            import ptt
            ptt.type_out(heard + " ")
            if (cfg().get("session") or {}).get("send_on_talk"):
                import keyboard
                import focus
                time.sleep(0.08)
                keyboard.send(focus.send_key())   # Ctrl+Enter when the Claude Code setting says so
            else:
                self.face.set("idle")
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

    def trick(self, heard):
        """BOLO 69 (Chief 9/17, ruled 9/18): the yo-yo pad. The words never touch the chat box.
        Pepper acks in the ear, then a headless Haiku run writes the page in _YOYO/."""
        if not heard:
            self.face.set("idle")
            return
        print(f"\n  yo-yo > {heard}")
        self.face.say(f"yo-yo: {heard}")
        self.face.set("thinking")
        say = None
        if self.speak_replies:
            def say(t):
                try:
                    import squelch
                    squelch.key_up()
                    speak.say(t, blocking=True)   # JUDY's mouth until Pepper has hers (D-1)
                    squelch.key_down()
                except Exception as e:
                    print(f"  ! mouth failed: {e}")
        if say:
            say("Copy. Boxing the yo-yo.")
        import yoyo
        path, parsed, meta = yoyo.trick(heard, say=None)
        print(f"  wrote  {path}")
        if meta.get("error"):
            print(f"  !      {meta['error']}")
        if parsed:
            print(f"  pepper > {parsed.get('opener')}")
            print(f"  run    {meta.get('took', 0):.1f}s · cache_read {meta.get('cache_read')} · out {meta.get('out')}")
            if say and parsed.get("opener"):
                self.face.set("talking")
                say(parsed["opener"])
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

    def start_yoyo(self):
        """The yo-yo pad went down (BOLO 69): record like a talk hold, route to trick() on release."""
        if self.open or not self.busy.acquire(blocking=False):
            return
        self.open = True
        self.yoyo = True
        self.face.set("listening")
        try:
            self.rec.start()
        except Exception as e:
            print(f"  ! mic failed: {e}")
            self.open = False
            self.yoyo = False
            self.face.set("idle")
            self.busy.release()

    def start_naked(self):
        """Her pad went down (BOLO 74): record like a talk hold, route to Naked on release."""
        if self.naked is None or self.open or not self.busy.acquire(blocking=False):
            return
        self.open = True
        self.naked_hold = True
        self.naked.face.set("listening")
        try:
            self.rec.start()
        except Exception as e:
            print(f"  ! mic failed: {e}")
            self.open = False
            self.naked_hold = False
            self.naked.face.set("idle")
            self.busy.release()

    def finish(self):
        if not self.open:
            return
        self.open = False
        is_yoyo, self.yoyo = self.yoyo, False
        is_naked, self.naked_hold = self.naked_hold, False
        try:
            audio = self.rec.stop()
            (self.naked.face if is_naked else self.face).set("thinking")
            text, meta = self.engine.transcribe(audio)
            for h, r, _n in (meta.get("hits") or []):
                print(f"         §8 {h!r} -> {r!r}")
            if is_naked:
                self.naked.turn(text)
            elif is_yoyo:
                self.trick(text)
            else:
                self.turn(text)
        except Exception as e:
            print(f"  ! turn failed: {e}")
            self.face.set("idle")
            if self.naked is not None:
                self.naked.face.set("idle")
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
            if self.session and dcfg().get("send_note") is not None:
                import focus
                # the SEND pad (Chief 9/17): the pad above the talk pad — Enter on whatever is in the box
                extra[int(dcfg()["send_note"])] = (
                    lambda: threading.Thread(target=focus.send_box, daemon=True).start(), lambda: None)
            if dcfg().get("yoyo_note") is not None:
                # the YO-YO pad (BOLO 69, Chief 9/17): top-left, far from the others; hold to box a flash
                extra[int(dcfg()["yoyo_note"])] = (
                    lambda: self.start_yoyo(),
                    lambda: threading.Thread(target=self.finish, daemon=True).start())
            if self.naked is not None and dcfg().get("naked_note") is not None:
                # NAKED's pad (BOLO 74, Chief 9/20): hold to talk to her; her answer never touches the chat box
                extra[int(dcfg()["naked_note"])] = (
                    lambda: self.start_naked(),
                    lambda: threading.Thread(target=self.finish, daemon=True).start())
            if self.toggle:
                self.pad = midipad.PadListener(lambda: self.fire("pad"), lambda: None, extra=extra)
            else:
                self.pad = midipad.PadListener(
                    lambda: self.start("pad"),
                    lambda: threading.Thread(target=self.finish, daemon=True).start(), extra=extra)
            if self.pad.start():
                c = dcfg()
                print(f"  pad    note {c['midi_note']} on {c.get('midi_port')}"
                      + (f" · focus pad note {c['focus_note']}" if c.get("focus_note") is not None else " · no focus pad (midipad.py --learn-focus)")
                      + (f" · send pad note {c['send_note']}" if c.get("send_note") is not None else "")
                      + (f" · yo-yo pad note {c['yoyo_note']}" if c.get("yoyo_note") is not None else "")
                      + (f" · naked pad note {c['naked_note']}" if (self.naked is not None and c.get("naked_note") is not None) else ""))
            else:
                print(f"  pad    unavailable: {self.pad.error}")

        shape = "PRESS to start, press again to stop" if self.toggle else f"HOLD {self.hotkey}"
        extra = " (or the pad)" if self.pad and not self.pad.error else ""
        if self.session:
            extra += (" · talk drops the words in the box, the SEND pad sends"
                      if not (cfg().get("session") or {}).get("send_on_talk") else " · talk sends on release")
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
    ap.add_argument("--yoyo", help="skip the mic: one typed yo-yo trick (BOLO 69), then exit")
    ap.add_argument("--size", type=int, default=220)
    ap.add_argument("--toggle", action="store_true",
                    help="press to start, press again to stop (best for a pad)")
    ap.add_argument("--session", action="store_true",
                    help="session voice: your words go into the VS Code chat, and the "
                         "reader speaks Fable's replies as they are written")
    ap.add_argument("--naked", action="store_true",
                    help="BOLO 74: Naked rides along: her pad, her face beside JUDY's, her voice, her model on :5001")
    ap.add_argument("--type-naked", help="skip the mic: one typed turn to Naked, then exit")
    ap.add_argument("--naked-no-face", action="store_true",
                    help="Naked rides along without her picture: pad and voice only (Chief 9/24, the launch sequence)")
    a = ap.parse_args()

    v = cfg().get("voice", {})
    print("JUDY · BOLO 56")
    print(f"  mouth  {v.get('engine', 'piper')}"
          + (f" · {v.get('eleven_voice_id', '')[:12]}…" if v.get("engine") == "elevenlabs" else ""))

    face = NoFace() if (a.no_face or a.type or a.yoyo or a.type_naked) else Face(a.size)

    if a.type_naked:
        nk.Naked(nk.NoFace(), speak_replies=not a.no_voice).turn(a.type_naked)
        return

    if a.yoyo:
        Loop(face, None, "", speak_replies=not a.no_voice).trick(a.yoyo)
        return

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
    if a.naked:
        # BOLO 74: her face is a second window beside JUDY's (a Toplevel of the same root)
        try:
            if isinstance(face, Face) and not a.naked_no_face:
                jp = None
                try:
                    jp = json.load(io.open(POS, encoding="utf-8"))
                    jp = (jp["x"], jp["y"])
                except Exception:
                    pass
                nface = nk.Face(face.root, a.size, judy_pos=jp)
            else:
                nface = nk.NoFace()
            loop.naked = nk.Naked(nface, speak_replies=not a.no_voice)
            print(f"  naked  aboard · pad note {dcfg().get('naked_note')} · server {'up' if loop.naked.brain.up() else 'DOWN (say Naked)'}")
        except Exception as e:
            print(f"  naked  not aboard: {e}")
    loop.run()
    if a.session:
        import reader
        rd = reader.Reader(face=face)
        print(f"  voice  session · reader={rd.cfg.get('reader')} · keep the chat box focused")
        threading.Thread(target=rd.run, daemon=True).start()
    face.run()


if __name__ == "__main__":
    main()
