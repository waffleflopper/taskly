#! /usr/bin/env python3

from pathlib import Path
import sys

from utils.parser import create_parser
from classes.task_list import TaskList
from classes.command_handler import CommandHandler


def main():
    parser = create_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Task Stuff Goes Here
    task_file = Path.home() / ".taskly.json"
    task_list = TaskList(task_file)
    command_handler = CommandHandler(task_list)

    # convert args to dict
    args_dict = vars(args)
    command = args_dict.pop("command")

    args_list = [str(value) for value in args_dict.values() if value is not None]

    try:
        #handle command and args
        command_handler.handle_command(command, args_list)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()