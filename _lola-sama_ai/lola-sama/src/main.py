import os
import typer
from rich.console import Console
# near top
import os
from kokoro_tts_wrapper import KokoroTTS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KOKORO_DIR = os.path.join(BASE_DIR, "models", "kokoro")
KOKORO_MODEL = os.path.join(KOKORO_DIR, "kokoro-v1.0.onnx")
KOKORO_VOICES = os.path.join(KOKORO_DIR, "voices-v1.0.bin")

tts = KokoroTTS(
    model_path=KOKORO_MODEL,
    voices_path=KOKORO_VOICES,
    voice="af_sarah",
    lang="en-us",
    speed=1.0,
)

# --- Kokoro TTS (safe import & init) ---
try:
    from kokoro_tts_wrapper import KokoroTTS  # your wrapper
except Exception:
    KokoroTTS = None  # allow app to run without TTS

# --- Lola & memory ---
from lola_model import query_lola
from memory import (
    log_conversation,
    journal_entry,
    note_entry,
    recall_journal,
    recall_notes,
)

app = typer.Typer(help="Lola-sama REPL")
console = Console()

# --- Globals / Config ---
VOICE_ON = True
TTS_AVAILABLE = False
tts = None

# Path where you store Kokoro assets (adjust if different)
BASE_DIR = os.path.dirname(__file__)
KOKORO_DIR = os.path.join(BASE_DIR, "models", "kokoro")
KOKORO_MODEL = os.path.join(KOKORO_DIR, "kokoro-v1.0.onnx")
KOKORO_VOICES = os.path.join(KOKORO_DIR, "voices-v1.0.bin")
KOKORO_VOICE = "af_sarah"  # af_bella, af_nicole, af_sarah, af_sky, am_adam, am_michael, bf_emma, bf_isabella, bm_george, bm_lewis
KOKORO_LANG = "en-us"
KOKORO_SPEED = 1.0


def init_tts() -> None:
    """Initialize Kokoro TTS if available and assets exist."""
    global tts, TTS_AVAILABLE
    if KokoroTTS is None:
        TTS_AVAILABLE = False
        return
    if not (os.path.isfile(KOKORO_MODEL) and os.path.isfile(KOKORO_VOICES)):
        TTS_AVAILABLE = False
        return
    try:
        tts = KokoroTTS(
            model_path=KOKORO_MODEL,
            voices_path=KOKORO_VOICES,
            voice=KOKORO_VOICE,
            lang=KOKORO_LANG,
            speed=KOKORO_SPEED,
        )
        TTS_AVAILABLE = True
    except Exception as e:
        console.print(f"[bold yellow]TTS disabled:[/bold yellow] {e}")
        TTS_AVAILABLE = False


def speak(text: str) -> None:
    """Speak text if VOICE_ON and TTS is available."""
    if VOICE_ON and TTS_AVAILABLE and tts is not None and text:
        try:
            tts.speak(text, block=False)
        except Exception as e:
            console.print(f"[bold yellow]TTS error:[/bold yellow] {e}")


@app.command()
def run() -> None:
    """Start the interactive Lola-sama console."""
    init_tts()
    status = "enabled" if TTS_AVAILABLE else "unavailable"
    console.print(f"[bold magenta]Lola-sama is online[/bold magenta] (TTS: {status})")
    console.print("[dim]Type !help for commands.[/dim]")

    while True:
        try:
            user_input = console.input("[bold cyan]> [/bold cyan]").strip()
        except (KeyboardInterrupt, EOFError):
            console.print("\n[bold red]Exiting Lola-sama...[/bold red]")
            break

        if not user_input:
            continue

        # Quit
        if user_input.lower() in {"exit", "quit"}:
            console.print("[bold red]Exiting Lola-sama...[/bold red]")
            break

        # Commands
        if user_input.startswith("!"):
            # Voice toggles (handled first so they don't fall through)
            low = user_input.strip().lower()
            if low == "!voice on":
                global VOICE_ON
                VOICE_ON = True
                console.print("[bold green]Voice: ON[/bold green]")
                continue
            elif low == "!voice off":
                VOICE_ON = False
                console.print("[bold yellow]Voice: OFF[/bold yellow]")
                continue

            if user_input.startswith("!journal "):
                entry = user_input[len("!journal "):].strip()
                if entry:
                    journal_entry(entry)
                    console.print("[bold yellow]Lola-sama:[/bold yellow] Logged to today’s journal.")
                else:
                    console.print("[bold red]Missing entry text.[/bold red] Usage: !journal your thoughts here.")

            elif user_input.startswith("!notes "):
                entry = user_input[len("!notes "):].strip()
                if entry:
                    note_entry(entry)
                    console.print("[bold yellow]Lola-sama:[/bold yellow] Saved to today’s notebook.")
                else:
                    console.print("[bold red]Missing note text.[/bold red] Usage: !notes your note here.")

            elif user_input.strip() == "!recall journal":
                journal = recall_journal()
                console.print(f"[bold yellow]Lola-sama:[/bold yellow] Here's your journal:\n\n{journal}")

            elif user_input.strip() == "!recall notes":
                notes = recall_notes()
                console.print(f"[bold yellow]Lola-sama:[/bold yellow] Here's your notes:\n\n{notes}")

            elif user_input.strip() in {"!help", "!"}:
                console.print(
                    "[bold]Commands[/bold]\n"
                    "!journal <text>     — append to today’s journal\n"
                    "!notes <text>       — add a note to today’s notebook\n"
                    "!recall journal     — print all journal entries\n"
                    "!recall notes       — print all notes\n"
                    "!voice on/off       — enable or disable speech\n"
                    "exit/quit           — leave\n"
                )
            else:
                console.print("[yellow]Unknown command[/yellow]")
            continue  # stay inside the loop after a command

        # Normal chat
        ai_response = query_lola(user_input)
        log_conversation(user_input, ai_response)
        console.print(f"[bold green]Lola-sama:[/bold green] {ai_response}")
        speak(ai_response)


if __name__ == "__main__":
    app()
