import sys
import json
import os
from src.task_utils import (add_task, update_task, list_tasks, mark_task, delete_task)

TASKS_FILE = "tasks.json"

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

    match command:
        case "add":
            if len(sys.argv) != 3:
                print('Usage: python task_cli.py add "Task description"')
                return
            description = sys.argv[2]
            add_task(TASKS_FILE, description)

        case "list":
            if len(sys.argv) == 2:
                list_tasks(TASKS_FILE)
            else:
                print("Usage: python task_cli.py list")
            
        case "update":
            if len(sys.argv) != 4:
                print('Usage: python task_cli.py update <task_id> "Updated task description"')
                return
            task_id = int(sys.argv[2])
            updated_description = sys.argv[3]
            update_task(TASKS_FILE, task_id, updated_description)

        case "mark":
            if len(sys.argv) != 4:
                print ('Usage: python task_cli.py mark <todo/in-progress/done> <task_id>')
                return
            mark_type = sys.argv[2]
            task_id = int(sys.argv[3])
            mark_task(TASKS_FILE, mark_type, task_id)

        case "delete":
            if len(sys.argv) != 3:
                print('Usage: python task-cli.py delete <task_id>')
                return
            task_id = int(sys.argv[2])
            delete_task(TASKS_FILE, task_id)
        case _:
            print("Error: Unknown argument type.")

if __name__ == "__main__":
    main()
