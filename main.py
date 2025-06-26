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
        date: datetime

dict_journal_entry = {}

        
def load_entries() -> str: 
        with open('journal.json', "r") as user_file:
         journal_content = user_file.read()
        print(journal_content)
"""Load journal entries from the JSON file."""

    
def save_entries(entries: dict[JournalEntry]) -> str:
        with open("journal.json","w") as json_file:
             json.dump(dict_journal_entry,json_file)
        """Save journal entries to the JSON file."""

    
def add_entry(title, content) -> str:
    save_entries(dict_journal_entry)
    return
    """Create a new journal entry and save it to the JSON file."""

    
def list_entries(entries) -> str:
    #print(dict_journal_entry)
    return
    """Print all journal entries to the console."""



    
if __name__ == "__main__":
    # quick interactive program (entry point) to validate the above
    title = input("Title: ")
    content = input("Content: ")
    date = input("Today's date: ")
    add_entry(title, content)
    print("✅ Entry saved.")
    print("\n📘 Your Journal:")
    list_entries(load_entries())
    
   