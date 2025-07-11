from dataclasses import dataclass, asdict
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
        
def load_entries() -> list[JournalEntry]: 
        try:
                with open("journal_json","r") as f:
                        json_content = json.loads(f)
        except FileNotFoundError:
                        json_content = []
        #finally:
               #print("Your journal entries were successfully stored and loaded") #Using finally just to show my exception handling is working
"""Load journal entries from the JSON file."""
    

"""def save_entries(entries: list[JournalEntry]) -> None:
        with open("journal.json","w") as journal_file:
             json.dump([asdict(entry) for entry in entries],journal_file, indent=2)
        return"""
"""Save journal entries to the JSON file."""

    
def add_entry(title: str, content: str) -> None:
    new_entry = JournalEntry(title=title,content=content,date=datetime.now())
    new_entry_dict = asdict(new_entry)
    print(new_entry_dict)
    new_entry = load_entries()
    #entries = load_entries()
    #entries.append(new_entry_dict)
    return

    #Create a new journal entry and save it to the JSON file.
    
"""def list_entries(entries) -> str:
    if not entries:
          print("No entries found")
    for entry in entries:
          print(f"{entry.title}")
          print(f"{entry.content}")    
    return"""

    #Print all journal entries to the console.

if __name__ == "__main__":
    # quick interactive program (entry point) to validate the above
    title = input("Title: ")
    content = input("Content: ")
    date = input("Today's date: ")
    add_entry(title,content)
    print("✅ Entry saved.")
    print("\n📘 Your Journal:")
    load_entries()
    #save_entries()
    #list_entries(load_entries())
    
   