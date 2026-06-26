import json
import os
import sys

TASKS_FILE = "tasks.json"

def ensure_tasks_file_exists():
    """
    Create tasks.json if it does not already exist.
    """
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w", encoding="utf-8") as file:
            json.dump([],file, indent=4)

def load_tasks():
    """
    Load tasks from the JSON file.

    Raises:
        OSError: If the file is empty or corrupted.
    """
    ensure_tasks_file_exists()

    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()

            if not content:
                return []
            
            return json.loads(content)
        
    except json.JSONDecodeError:
        print("Error: tasks.json is corrupted or contains invalid JSON.")
        print("Please fix or delete tasks.json and try again.")
        sys.exit(1)

    except OSError as error:
        print(f"Error reading {TASKS_FILE}: {error}")
        sys.exit(1)

def save_tasks(tasks):
    """
    Save tasks to the JSON file.
    
    Raises:
        OSError: If the file cannot be written to.
    """
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    except OSError as error:
        print(f"Error writing to {TASKS_FILE}: {error}")
        sys.exit(1)
