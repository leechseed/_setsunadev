from datetime import datetime
import os

def log_conversation(user_input, response):
    date_str = datetime.now().strftime("%Y-%m-%d")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(base_dir, "..", "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{date_str}.md")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"**You:** {user_input}\n")
        f.write(f"**Lola-sama:** {response}\n\n")

def journal_entry(text):
    from datetime import datetime
    import os

    date_str = datetime.now().strftime("%Y-%m-%d")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    journal_dir = os.path.join(base_dir, "..", "memory", "journal")
    os.makedirs(journal_dir, exist_ok=True)
    journal_file = os.path.join(journal_dir, f"{date_str}.md")

    with open(journal_file, "a", encoding="utf-8") as f:
        f.write(f"- {text}\n")

def note_entry(text):
    from datetime import datetime
    import os

    date_str = datetime.now().strftime("%Y-%m-%d")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    notes_dir = os.path.join(base_dir, "..", "memory", "notes")
    os.makedirs(notes_dir, exist_ok=True)
    notes_file = os.path.join(notes_dir, f"{date_str}.md")

    with open(notes_file, "a", encoding="utf-8") as f:
        f.write(f"- {text}\n")
def recall_journal():
    from datetime import datetime
    import os

    date_str = datetime.now().strftime("%Y-%m-%d")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    journal_file = os.path.join(base_dir, "..", "memory", "journal", f"{date_str}.md")

    if os.path.exists(journal_file):
        with open(journal_file, "r", encoding="utf-8") as f:
            return f.read().strip()
    else:
        return "[No journal entries found for today.]"


def recall_notes():
    from datetime import datetime
    import os

    date_str = datetime.now().strftime("%Y-%m-%d")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    notes_file = os.path.join(base_dir, "..", "memory", "notes", f"{date_str}.md")

    if os.path.exists(notes_file):
        with open(notes_file, "r", encoding="utf-8") as f:
            return f.read().strip()
    else:
        return "[No notes found for today.]"
