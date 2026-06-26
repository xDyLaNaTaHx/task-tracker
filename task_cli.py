import sys
import json
import os
from datetime import datetime

from src.json_utils import (load_tasks, save_tasks)

STATUS_TODO = "todo"
STATUS_IN_PROGRESS = "in-progress"
STATUS_DONE = "done"

VALID_STATUSES = [STATUS_TODO, STATUS_IN_PROGRESS, STATUS_DONE]

def get_current_timestamp():
    """
    Return current timestamp as an ISO-like string.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_next_id(tasks):
    """
    Return the next available task ID.
    """
    if not tasks:
        return 1

    return max(task["id"] for task in tasks) + 1

def add_task(description):
    """
    Add a new task.
    """
    if not description.strip():
        print("Error: Task description cannot be empty.")
        return
    
    tasks = load_tasks()

    now = get_current_timestamp()

    new_task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": STATUS_TODO,
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print(f"Task added successfully. ID: {new_task['id']}")


def list_tasks():
    """
    List all tasks, or tasks filtered by status.
    """
    tasks = load_tasks()

    for task in tasks:
        print(
            f"[{task['id']}] "
            f"{task['description']} "
            f"({task['status']}) "
            f"Created: {task['createdAt']} "
            f"Updated: {task['updatedAt']}"
        )

def print_help():
    """
    Print usage documentation
    """
    print("""
Task CLI App
          
Usage:
    python task_cli.py add "Task description"
    python task_cli.py list
          """)

def main():
    """
    Main command dispatcher.
    Uses positional command-line arguments.
    """
    if len(sys.argv) < 2:
        print_help()
        return
    
    command = sys.argv[1]
    
    if command == "add":
        if len(sys.argv) != 3:
            print('Usage: python task_cli.py add "Task description"')
            return
        description = sys.argv[2]
        add_task(description)

    elif command == "list":
        if len(sys.argv) == 2:
            list_tasks()
        else:
            print("Usage: python task_cli.py list")


if __name__ == "__main__":
    main()