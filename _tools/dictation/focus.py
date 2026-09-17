# -*- coding: utf-8 -*-
"""focus.py — bring VS Code to the front and put the cursor in the Claude Code chat box.

Chief, 9/17 (BOLO 56): "whenever I press the pad on the Akai MPK, make it auto-focus
VS Code and put my cursor in the Claude Code box."

Two moves: (1) the VS Code window to the foreground (Win32; a dead-key tap defeats the
foreground lock Windows puts on background processes — never a bare Alt, that opens the menu bar), (2) the keybinding that runs the
extension's own `claude-vscode.focus` command ("Claude Code: Focus input"), added to the
user keybindings.json without a `when` clause so it works from anywhere in VS Code.

    python focus.py            do it once (proof)

judy.json → "session": {"focus_on_talk": "pad" | "always" | "never"}   (default "pad")
config.json → "focus_key": the key bound to claude-vscode.focus (default f14, a dead key)
"""
import io, os, json, time, ctypes, ctypes.wintypes as W

HERE = os.path.dirname(os.path.abspath(__file__))
JUDY = os.path.join(HERE, "judy.json")
CONFIG = os.path.join(HERE, "config.json")
FOCUS_KEY = "f14"   # RULED 9/17 late: a dead key; ctrl+alt+shift+j did not land
TITLE_TAIL = "Visual Studio Code"

user32 = ctypes.windll.user32
EnumWindows = user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, W.HWND, W.LPARAM)


def _cfg(path):
    try:
        return json.load(io.open(path, encoding="utf-8"))
    except Exception:
        return {}


def policy():
    return ((_cfg(JUDY).get("session") or {}).get("focus_on_talk") or "pad").lower()


def focus_key():
    return _cfg(CONFIG).get("focus_key") or FOCUS_KEY


def send_key():
    """What sends a prompt in the Claude Code box. config.json "send_key" wins; else the VS Code setting
    claudeCode.useCtrlEnterToSend (user then workspace settings.json) → ctrl+enter; else enter."""
    k = _cfg(CONFIG).get("send_key")
    if k:
        return k
    # the active VS Code profile keeps its own settings.json under User/profiles/<id>/ — Chief's
    # profile is where useCtrlEnterToSend actually lives (found 9/17 06:16), so scan those too
    import glob
    user = os.path.join(os.environ.get("APPDATA", ""), "Code", "User")
    for p in ([os.path.join(user, "settings.json")]
              + sorted(glob.glob(os.path.join(user, "profiles", "*", "settings.json")))
              + [os.path.join(os.path.dirname(HERE), "..", ".vscode", "settings.json")]):
        try:
            txt = io.open(p, encoding="utf-8").read()
            if '"claudeCode.useCtrlEnterToSend": true' in txt.replace(" : ", ": "):
                return "ctrl+enter"
        except Exception:
            pass
    return "enter"


def vscode_windows():
    out = []

    def cb(hwnd, _):
        if not user32.IsWindowVisible(hwnd):
            return True
        n = user32.GetWindowTextLengthW(hwnd)
        if n <= 0:
            return True
        buf = ctypes.create_unicode_buffer(n + 1)
        user32.GetWindowTextW(hwnd, buf, n + 1)
        if buf.value.endswith(TITLE_TAIL):
            out.append((hwnd, buf.value))
        return True

    EnumWindows(EnumWindowsProc(cb), 0)
    return out


def foreground(hwnd):
    SW_RESTORE = 9
    # already in front: touch nothing (Chief 9/17: the lone Alt tap below was opening VS Code's
    # File menu, so the Enter that followed pulled the menu down instead of sending the turn)
    if user32.GetForegroundWindow() == hwnd and not user32.IsIconic(hwnd):
        return True
    if user32.IsIconic(hwnd):
        user32.ShowWindow(hwnd, SW_RESTORE)
    # the input tap: Windows only lets the process that last took input set the foreground.
    # Never a bare Alt (it activates the menu bar); the focus key is a dead key, so tap that.
    try:
        import keyboard
        k = focus_key()
        keyboard.press(k); time.sleep(0.02); keyboard.release(k)
    except Exception:
        pass
    user32.SetForegroundWindow(hwnd)
    if user32.GetForegroundWindow() == hwnd:
        return True
    # second try: attach to the foreground thread's input queue and push again
    fg = user32.GetForegroundWindow()
    t_fg = user32.GetWindowThreadProcessId(fg, None)
    t_me = ctypes.windll.kernel32.GetCurrentThreadId()
    user32.AttachThreadInput(t_me, t_fg, True)
    user32.BringWindowToTop(hwnd)
    user32.SetForegroundWindow(hwnd)
    user32.AttachThreadInput(t_me, t_fg, False)
    if user32.GetForegroundWindow() == hwnd:
        return True
    # third try: the Alt-Tab switch itself (what the task switcher calls)
    try:
        user32.SwitchToThisWindow(hwnd, True)
    except Exception:
        pass
    if user32.GetForegroundWindow() == hwnd:
        return True
    # last try: minimize then restore — a restore from any process activates the window
    SW_MINIMIZE = 6
    user32.ShowWindow(hwnd, SW_MINIMIZE)
    time.sleep(0.05)
    user32.ShowWindow(hwnd, SW_RESTORE)
    time.sleep(0.05)
    return user32.GetForegroundWindow() == hwnd


def focus_claude(prefer=None):
    """VS Code to the front (the window whose title contains `prefer` if given, else the first),
    then the focus chord so the cursor lands in the Claude Code input. Returns (ok, title)."""
    wins = vscode_windows()
    if not wins:
        return False, "no Visual Studio Code window"
    hwnd, title = wins[0]
    if prefer:
        for h, t in wins:
            if prefer.lower() in t.lower():
                hwnd, title = h, t
                break
    ok = foreground(hwnd)
    time.sleep(0.25)
    try:
        import keyboard
        k = focus_key()
        keyboard.press(k); time.sleep(0.03); keyboard.release(k)
    except Exception as e:
        return ok, "%s (focus key failed: %s)" % (title, e)
    time.sleep(0.25)
    return ok, title


def send_box():
    """The SEND pad (Chief, 9/17): VS Code forward, cursor in the box, the send key (Ctrl+Enter when the
    Claude Code setting useCtrlEnterToSend is on — Chief's clue 9/17 late) on whatever is there."""
    ok, title = focus_claude()
    try:
        import keyboard
        time.sleep(0.15)
        k = send_key()
        keyboard.send(k) if "+" in k else (keyboard.press(k), time.sleep(0.03), keyboard.release(k))
    except Exception as e:
        return ok, "%s (enter failed: %s)" % (title, e)
    return ok, title


def wants_focus(src):
    p = policy()
    return p == "always" or (p == "pad" and src == "pad")


if __name__ == "__main__":
    ok, title = focus_claude()
    print("foreground" if ok else "NOT foreground", "·", title, "·", focus_key())
