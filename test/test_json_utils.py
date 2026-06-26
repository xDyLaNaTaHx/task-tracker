import json
import os

from src.data_utils import get_current_timestamp
from src.json_utils import load_tasks

SAMPLE_TASKS_FILE = "test/tasks.json"
SAMPLE_TASK = {
    "id": 1,
    "description": "This is a sample",
    "status": "todo",
    "createdAt": get_current_timestamp(),
    "updatedAt": get_current_timestamp()
}

def create_sample_tasks_json():
    with open(SAMPLE_TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump([SAMPLE_TASK], file, indent=4)

def test_answer():
    create_sample_tasks_json()
    assert [SAMPLE_TASK] == load_tasks(SAMPLE_TASKS_FILE)
