import datetime
from utils.file_operations import get_tasks, save_tasks
import logging


class TaskList:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = [{}]
        self.load_tasks()
        self.task_statuses = ["pending", "done"]
    
    def __str__(self):
        return f"TaskList(file_path={self.file_path}, tasks={self.tasks})"
    
    def load_tasks(self):
        try:
            logging.info(f"Loading tasks from {self.file_path}")
            self.tasks = get_tasks(self.file_path)
        except FileNotFoundError:
            self.tasks = [{}]
            logging.warning(f"No tasks file found at {self.file_path}. Please make sure the directory exists so Taskly can create the file for you.")
    
    def save_tasks(self):
        save_tasks(self.tasks, self.file_path)

    def _generate_id(self):
        last_id = self.tasks[-1]["id"]
        return last_id + 1

    def _add_task(self, description):
        id = self._generate_id()
        task = {
            "id": id,
            "description": description,
            "status": "pending",
            "created_at": datetime.date.today().strftime("%Y-%m-%d"),
            "updated_at": datetime.date.today().strftime("%Y-%m-%d")
        }
        self.tasks.append(task)
    
    def _update_task(self, id, status=None, description=None):
        for task in self.tasks:
            if task["id"] == id:
                if status is not None:
                    task["status"] = status
                if description is not None:
                    task["description"] = description
                task["updated_at"] = datetime.date.today().strftime("%Y-%m-%d")
                break
    
    def _delete_task(self, id):
        for task in self.tasks:
            if task["id"] == id:
                self.tasks.remove(task)
                break
    
    def _get_pending_tasks(self):
        return [task for task in self.tasks if task["status"] == "pending"]
    
    def _get_done_tasks(self):
        return [task for task in self.tasks if task["status"] == "done"]
    
    def list_tasks(self):
        #todo: make it prettier
        for task in self.tasks:
            print(task)
    
    def list_pending_tasks(self):
        for task in self._get_pending_tasks():
            print(task)
    
    def list_done_tasks(self):
        for task in self._get_done_tasks():
            print(task)

    def add_task(self, description):
        logging.info(f"Adding task: {description}")
        #todo: validate description
        self._add_task(description)
        self.save_tasks()

    def update_task(self, id, description=None):
        #todo: validate description
        logging.info(f"Updating task: {id} with description: {description}")
        self._update_task(id, description=description)
        self.save_tasks()
    
    def mark_task(self, id, status):
        if status not in self.task_statuses:
            logging.error(f"Invalid status: {status}")
            return
        logging.info(f"Marking task: {id} with status: {status}")
        self._update_task(id, status=status)
        self.save_tasks()
    
    def delete_task(self, id):
        logging.info(f"Deleting task: {id}")
        self._delete_task(id)
        self.save_tasks()
