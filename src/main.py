import sys
import logging
import os
from utils.file_operations import get_tasks, save_tasks
from classes.task import TaskList
logging.basicConfig(level=logging.DEBUG)

# taskly <command> <args>

# todo: validate args before passing them to the task list
# todo: add tests
# todo: create a Task class to handle it's own updates
# todo: Make TaskList a singleton

# task structure
# - id
# - description
# - status
# - created_at
# - updated_at

COMMAND_LIST = ["list", "add", "delete", "update", "mark", "help"]
TASKS_FILE_PATH = os.path.join(os.path.dirname(__file__),"data", "tasks.json")

task_list = TaskList(TASKS_FILE_PATH)

def parse_args(raw_args):
    _, command, *args = raw_args
    return command, args

def handle_command(command, args):
    command = command.lower()
    if not command in COMMAND_LIST:
        print(f"Command {command} not found")
        print("Available commands: ", COMMAND_LIST)
        return
    
    if command == "add":
        if len(args) == 0:
            print("Please provide a description for the task")
            return
        logging.info(f"Adding task: {args[0]}")
        task_list.add_task(args[0])
    elif command == "delete":
        if len(args) == 0:
            print("Please provide an id for the task")
            return
        logging.info(f"Deleting task: {args[0]}")
        task_list.delete_task(int(args[0]))
    elif command == "list":
        if args:
            if args[0].lower() == "pending":
                logging.info("Listing pending tasks")
                task_list.list_pending_tasks()
            elif args[0].lower() == "done":
                logging.info("Listing done tasks")
                task_list.list_done_tasks()
            else:
                print(f"Invalid list type: {args[0]}")
                print(f"Available list types: {task_list.task_statuses}")
        else:
            logging.info("Listing all tasks")
            task_list.list_tasks()
    elif command == "help":
        print("Available commands: ", COMMAND_LIST)
    elif command == "update":
        if len(args) == 0:
            print("Please provide an id for the task")
            return
        logging.info(f"Updating task: {args[0]}")
        task_list.update_task(int(args[0]), args[1]) #id, description
    elif command == "mark":
        if len(args) == 0:
            print("Please provide an id for the task")
            return
        logging.info(f"Marking task: {args[0]}")
        task_list.mark_task(int(args[0]), args[1]) #id, status
    else:
        print(f"Command {command} not found")
        print("Available commands: ", COMMAND_LIST)

def main():
    if len(sys.argv) < 2:
        print("Usage: taskly <command> <args>")
        sys.exit(1)
    
    command = sys.argv[1]
    args = sys.argv[2:]
    handle_command(command, args)

if __name__ == "__main__":
    main()

