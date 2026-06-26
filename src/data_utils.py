from datetime import datetime

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
