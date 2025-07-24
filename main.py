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
        
def add_entry(title: str, content: str) -> JournalEntry:
    new_entry = JournalEntry(title=title,content=content,date=datetime.now())
    entries = load_entries()
    entries.append(new_entry)
    save_entries(entries)
    #new_entry_dict = asdict(new_entry)
    #new_entry = new_entry_dict
    #print(new_entry)
    return new_entry
    #print(entries)

"""def add_entry(self, title: str, content: str, tags: list[str]) -> None:
        entry = JournalEntry(title=title, content=content, tags=tags)
        entries = self.load_entries()
        entries.append(entry)
        self.save_entries(entries)"""
    


def save_entries(title: str, content: str) -> None: #entries: list[JournalEntry] #use asdict() in save_entries function
        new_entry = add_entry(title,content)
        with open(DB_FILE,"w") as f:
             json.dump(asdict(new_entry),f,indent=2,default=str)
        print("Serialized to JSON")
        return
"""Save journal entries to the JSON file."""


def load_entries() -> list[JournalEntry]: 
        try:
                with open(DB_FILE,"r") as f:
                        data = json.load(f)
                        print("Serialized JSON data:", data)
        except FileNotFoundError:
                        data = []
        finally:
               print("Your journal entries were successfully stored and loaded") #Using finally just to show my exception handling is working"""
"""Load journal entries from the JSON file."""

"""def new_entry(full_entries:list[JournalEntry]): 
        new_added_entry = JournalEntry(title=title,content=content,date=datetime.now())
        full_entries = load_entries()
        full_entries.append(new_added_entry)
        save_entries(title,content)
        return"""

    
def list_entries(entries: list[JournalEntry]) -> None:
        entries = load_entries()
        print("Your journal entry was loaded again")
        
        
        
        
        
        """if entries:
               print("My second test of deserialized entries: ", entries)
        else:
          print("No entries found")"""
        """else:
                for entry in enumerate(entries,1):
                        print(f"{entry.title}")
                        print(f"{entry.content}")"""   
        return

#Print all journal entries to the console.


    #Print all journal entries to the console.

if __name__ == "__main__":
    # quick interactive program (entry point) to validate the above
    title = input("Title: ")
    content = input("Content: ")
    date = input("Today's date: ")
    add_entry(title,content)
    save_entries(title,content)
    #print("✅ Entry saved.")
    #print("\n📘 Your Journal:")
    list_entries(load_entries())
    #new_entry(load_entries())

   