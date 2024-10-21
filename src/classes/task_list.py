from classes.task import Task
import logging

from utils.file_ops import get_file_contents, save_file_contents


class TaskList:
    def __init__(self, filepath):
        self.filepath = filepath
        self.tasks = []
        self.valid_statuses = ["completed", "pending"]
        self.load_tasks_from_file()

    def load_tasks_from_file(self):
        data = get_file_contents(self.filepath)
        for task in data:
            new_task = Task.from_dict(task)
            self.tasks.append(new_task)

    def save_tasks_to_file(self):
        data = []
        for task in self.tasks:
            data.append(task.to_dict())
        save_file_contents(self.filepath, data)

    def get_next_id(self):
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1

    def find_task(self, task_id):
        task = next((task for task in self.tasks if task.id == task_id), None)
        if task is None:
            logging.debug(f"Task with ID {task_id} not found.")
        else:
            logging.debug(f"Found task: {task.to_dict()}")
        return task
    def add_task(self, description, status="pending"):
        new_task = Task(description, status)
        new_task.id = self.get_next_id()
        self.tasks.append(new_task)
        self.save_tasks_to_file()
        return new_task

    def update_task(self, task_id, description):
        task = self.find_task(task_id)
        if task:
            task.update(description)
            self.save_tasks_to_file()
            return True # operation successful
        return False # operation failed

    def mark_task(self, task_id, status):
        task = self.find_task(task_id)
        if task:
            task.mark(status)
            self.save_tasks_to_file()
            return True
        return False

    def remove_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks_to_file()
            return True
        return False
    def get_tasks(self, filter=None):
        if filter:
            if filter in self.valid_statuses:
                return [task for task in self.tasks if task.status == filter]
        logging.debug(f"Current tasks: {[task.id for task in self.tasks]}")
        return self.tasks
