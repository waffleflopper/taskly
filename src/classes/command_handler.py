from datetime import datetime
import textwrap

class CommandHandler:
    def __init__(self, task_list):
        self.task_list = task_list
        self.commands = {
            "add": self.add_task,
            "list": self.list_tasks,
            "update": self.update_task,
            "mark": self.mark_task,
            "remove": self.remove_task
        }
        self.command_args = {
            "add": 1,
            "list": 0,
            "update": 2,
            "mark": 2,
            "remove": 1
        }

    def validate_args(self, command, args):
        return len(args) >= self.command_args[command]

    def add_task(self, description):
        self.task_list.add_task(description)
        print(f"Added task: {description}")

    def list_tasks(self, filter=None):
        tasks = self.task_list.get_tasks(filter)
        if not tasks:
            print("No tasks found")
            return

        # Print header
        print(f"{'ID':<5} {'Description':<20} {'Status':<10} {'Created At':<20} {'Updated At':<20}")

        for task in tasks:
            # Format the dates to DD MMM YYYY
            created_at = datetime.fromisoformat(task.to_dict()['created_at']).strftime('%d %b %Y')
            updated_at = datetime.fromisoformat(task.to_dict()['updated_at']).strftime('%d %b %Y')

            # Wrap the description to a maximum width of 20 characters
            description_lines = textwrap.wrap(task.to_dict()['description'], width=20)

            # Print each line of the description
            for line in description_lines:
                # Adjust the output for the first line to include the ID and other details
                if line == description_lines[0]:
                    print(f"{task.to_dict()['id']:<5} {line:<20} {task.to_dict()['status']:<10} {created_at:<20} {updated_at:<20}")
                else:
                    # For subsequent lines, just print the description
                    print(f"{'':<5} {line:<20} {'':<10} {'':<20} {'':<20}")

    def update_task(self, task_id, description):
        if self.task_list.update_task(task_id, description):
            print(f"Updated task {task_id}")
        else:
            print(f"Task {task_id} not found")

    def remove_task(self, task_id):
        if self.task_list.remove_task(task_id):
            print(f"Removed task {task_id}")
        else:
            print(f"Task {task_id} not found")

    def mark_task(self, task_id, status):
        task_id = int(task_id)  # Ensure task_id is an integer
        if self.task_list.mark_task(task_id, status):
            print(f"Marked task {task_id} as {status}")
        else:
            print(f"Task {task_id} not found")

    def handle_command(self, command, args):
        if command not in self.commands:
            print(f"Invalid command: {command}")
            return
        if not self.validate_args(command, args):
            print(f"Invalid number of arguments for command: {command}")
            return
        self.commands[command](*args)
