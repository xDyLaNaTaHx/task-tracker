import json
import os
import sys

def ensure_tasks_file_exists(tasks_file):
    """
    Create tasks.json if it does not already exist.
    """
    if not os.path.exists(tasks_file):
        with open(tasks_file, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)

def load_tasks(tasks_file):
    """
    Load tasks from the JSON file.

    Raises:
        OSError: If the file is empty or corrupted.
    """
    ensure_tasks_file_exists(tasks_file)

    try:
        with open(tasks_file, "r", encoding="utf-8") as file:
            content = file.read().strip()

            if not content:
                return []
            
            return json.loads(content)
        
    except json.JSONDecodeError:
        print("Error: tasks.json is corrupted or contains invalid JSON.")
        print("Please fix or delete tasks.json and try again.")
        sys.exit(1)

    except OSError as error:
        print(f"Error reading {tasks_file}: {error}")
        sys.exit(1)

def save_tasks(tasks_file, tasks):
    """
    Save tasks to the JSON file.
    
    Raises:
        OSError: If the file cannot be written to.
    """
    try:
        with open(tasks_file, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    except OSError as error:
        print(f"Error writing to {tasks_file}: {error}")
        sys.exit(1)
