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
                with open("journal.json","r") as journal_file:
                        journal_content = journal_file.read()
                        #for data in journal_content:
        except FileNotFoundError:
               print("Your journal entries did not load")
        finally:
               print("Your journal entries were successfully stored and loaded") #Using finally just to show my exception handling is working
        
        
"""Load journal entries from the JSON file."""
    

def save_entries(entries: list[JournalEntry]) :
        with open("journal.json","w") as json_file:
             json.dump([asdict(entry) for entry in entries],json_file, indent=2)
        """Save journal entries to the JSON file."""

    
"""def add_entry(title: str, content: str, date: datetime): 
    entries = load_entries()
    new_entry = JournalEntry(title=title,content=content,date=datetime.now())
    entries.append(new_entry)
    save_entries(entries)
    return"""

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
    #add_entry(title, content, date)
    print("✅ Entry saved.")
    print("\n📘 Your Journal:")
    load_entries()
    #list_entries(load_entries())
    
   