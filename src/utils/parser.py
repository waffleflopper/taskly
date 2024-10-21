import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="Taskly CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    ## Add
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Description of the task")

    # list
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("--status", choices=["completed", "pending"], help="Filter tasks by status")

    # update
    update_parser = subparsers.add_parser("update", help="Update task description")
    update_parser.add_argument("id", help="ID of the task to update")
    update_parser.add_argument("description", help="New description for the task")

    #remove
    remove_parser = subparsers.add_parser("remove", help="Remove a task")
    remove_parser.add_argument("id", help="ID of the task to remove")

    #mark status
    mark_parser = subparsers.add_parser("mark", help="Update task status")
    mark_parser.add_argument("id", help="ID of the task to mark")
    mark_parser.add_argument("status", choices=["completed", "pending"],
                             help="Status to set for the task")

    return parser