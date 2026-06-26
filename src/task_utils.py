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
    List all tasks.
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

def list_tasks_filtered(tasks_file, filter_keyword):
    """
    List all tasks filtered by status
    """
    tasks = load_tasks(tasks_file)

    if filter_keyword not in VALID_STATUSES:
        print(f'Error: Status "{filter_keyword}" not supported.')
        return

    task_found = False

    for task in tasks:
        if task['status'] == filter_keyword:
            task_found = True
            print(
                f"[{task['id']}] "
                f"{task['description']} "
                f"({task['status']}) "
                f"Created: {task['createdAt']} "
                f"Updated: {task['updatedAt']}"
            )
    if not task_found:
        print(f'No tasks with status: "{filter_keyword}". Allowed task types: {VALID_STATUSES}.')

def mark_task(tasks_file, mark_type, task_id):
    """
    Update a task's status.
    """
    if mark_type not in VALID_STATUSES:
        print(f"Error: Invalid tasks type. Allowed task types: {VALID_STATUSES}.")
        return
    
    tasks = load_tasks(tasks_file)
    for task in tasks:
        this_id = task['id']
        if this_id == task_id:
            task['status'] = mark_type
            print(f"Task updated successfully. ID: {task['id']}; Status: {task['status']}")
            save_tasks(tasks_file, tasks)
            return
        
    print(f"Error: No task exists for id == {task_id}")


def delete_task(tasks_file, task_id):
    """
    Delete a task.
    """
    tasks = load_tasks(tasks_file)

    for idx, task in enumerate(tasks):
        this_id = task["id"]
        if this_id == task_id:
            tasks.pop(idx)
            print(f'Task {task_id}: "{task['description']}" successfully')
            save_tasks(tasks_file, tasks)
            return
        
    print(f"Error: No task exists for id == {task_id}")