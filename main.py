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
        
def add_entry(title: str, content: str) -> None:
    new_entry = JournalEntry(title=title,content=content,date=datetime.now())
    new_entry_dict = asdict(new_entry)
    print(new_entry_dict)
    #entries = load_entries()
    #entries.append(new_entry_dict)
    return
        
        #Create a new journal entry.

def save_entries(entries: list[JournalEntry]) -> None:
        with open(DB_FILE,"w") as f:
             json.dump(entries,f,indent=2)
        return 
"""Save journal entries to the JSON file."""


def load_entries() -> list[JournalEntry]: 
        try:
                with open(DB_FILE,"r") as f:
                        data = json.load(f)
        except FileNotFoundError:
                        data = []
        finally:
                print(data)
               #print("Your journal entries were successfully stored and loaded") #Using finally just to show my exception handling is working"""
"""Load journal entries from the JSON file."""
    
"""def list_entries(entries: list[JournalEntry]) -> None:
    if not entries:
          print("No entries found")
    for entry in entries:
          print(f"{entry.title}")
          print(f"{entry.content}")    
    return"""

#Print all journal entries to the console.


"""def save_entries(entries: list[JournalEntry]) -> None:
        with open("journal.json","w") as f:
             json.dump(json_content,f, indent=2)
        return"""
"""Save journal entries to the JSON file."""

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
    save_entries(entries=1)
    print("✅ Entry saved.")
    print("\n📘 Your Journal:")
    load_entries()
    #list_entries(load_entries())
    
   