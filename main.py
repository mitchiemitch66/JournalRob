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
    new_entry = JournalEntry(title=title, content=content, date=datetime.now())
    entries = load_entries()
    entries.append(new_entry)
    save_entries(entries)
    return new_entry
    # print(entries)


def save_entries(
    entries,
) -> None:
    with open(DB_FILE, "w") as f:
        json.dump([asdict(e) for e in entries], f, indent=2, default=str)
    print("New entry saved")
    return


"""Save journal entries to the JSON file."""


def load_entries() -> list[JournalEntry]:
    try:
        with open(DB_FILE, "r") as f:
            data = json.load(f)
            # print("Serialized JSON data:", data)
            return [JournalEntry(**entry) for entry in data]
    except json.JSONDecodeError:
        return []


def list_entries(entries: list[JournalEntry]) -> None:
    if not entries:
        print("No journal entries")
        return
    for i, entry in enumerate(entries, 1):
        print(f"\n Journal Entry {i}")
        print(f"Title: {entry.title}")
        print(f"Content: {entry.content}")
        print(f"Date: {entry.date}")


if __name__ == "__main__":
    # quick interactive program (entry point) to validate the above
    title = input("Title: ")
    content = input("Content: ")

    new_entry = add_entry(title, content)
    print("Added new entry: ", new_entry)

    total_entries = load_entries()
    list_entries(total_entries)
