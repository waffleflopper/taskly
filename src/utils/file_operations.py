# src/utils/file_operations.py\

import json
import os
import logging

logging.basicConfig(level=logging.DEBUG)
TASKS_FILE_PATH = os.path.join(os.path.dirname(__file__), "tasks.json")

def get_tasks(file_path: str = TASKS_FILE_PATH) -> list[dict]:
    """
    Get the tasks from the tasks.json file
    """
    with open(file_path, "r") as file: #open should create the file if it doesn't exist
        logging.debug(f"Loading tasks from {file_path}")
        return json.load(file)

def save_tasks(tasks: list[dict], file_path: str = TASKS_FILE_PATH):
    """
    Save the tasks to the tasks.json file

    Args:
        tasks (list[dict]): The tasks to save
    """
    with open(file_path, "w") as file: #open should create the file if it doesn't exist
        logging.debug(f"Saving tasks to {file_path}")
        json.dump(tasks, file, indent=4)
