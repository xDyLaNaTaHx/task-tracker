from src.data_utils import (get_current_timestamp, get_next_id)
from src.json_utils import (load_tasks, save_tasks)

STATUS_TODO = "todo"
STATUS_IN_PROGRESS = "in-progress"
STATUS_DONE = "done"

VALID_STATUSES = [STATUS_TODO, STATUS_IN_PROGRESS, STATUS_DONE]

def add_task(tasks_file, description):
    """
    Add a new task.
    """
    if not description.strip():
        print("Error: Task description cannot be empty.")
        return
    
    tasks = load_tasks(tasks_file)

    now = get_current_timestamp()

    new_task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": STATUS_TODO,
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(new_task)
    save_tasks(tasks_file, tasks)

    print(f"Task added successfully. ID: {new_task['id']}")

def update_task(tasks_file, task_id, description):
    """
    Update an existing task description.
    """
    if not description.strip():
        print("Error: Task description cannot be empty.")
        return
    
    tasks = load_tasks(tasks_file)
    print(tasks)
    for task in tasks:
        this_id = task['id']
        print(this_id)
        if this_id == task_id:
            task['description'] = description
            print(f"Task updated successfully. ID: {task['id']}; Description: {task['description']}")
            save_tasks(tasks_file, tasks)
            return
        
    print(f"Error: No task exists for id == {task_id}")

def list_tasks(tasks_file):
    """
    List all tasks, or tasks filtered by status.
    """
    tasks = load_tasks(tasks_file)

    for task in tasks:
        print(
            f"[{task['id']}] "
            f"{task['description']} "
            f"({task['status']}) "
            f"Created: {task['createdAt']} "
            f"Updated: {task['updatedAt']}"
        )