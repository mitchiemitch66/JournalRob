from dataclasses import dataclass
import json
from datetime import datetime
from pathlib import Path

DB_FILE = Path("journal.json")
DB_FILE.touch(exist_ok=True)

# 📝 Define a JournalEntry class with title, content, and date

@dataclass
class JournalEntry:
        title: str
        content: str
        entry_number: int
        
def load_entries():
    """Load journal entries from the JSON file."""

    
def save_entries(entries):
        """Save journal entries to the JSON file."""

    
def add_entry(title, content):
    """Create a new journal entry and save it to the JSON file."""

    
def list_entries(entries):
    """Print all journal entries to the console."""

journal_one = JournalEntry("Rob's Journal Entry","You just completed a journal entry",1)
today = datetime.today()

    
if __name__ == "__main__":
    # quick interactive program (entry point) to validate the above
    title = input("Title: ")
    content = input("Content: ")
    add_entry(title, content)
    print("✅ Entry saved.")
    print("\n📘 Your Journal:")
    list_entries(load_entries())
    eval(repr(journal_one))
    print(journal_one)
    print("Journal entry date: ", today)
