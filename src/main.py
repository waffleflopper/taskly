import sys
import logging
import os
from utils.file_operations import get_tasks, save_tasks

logging.basicConfig(level=logging.DEBUG)

# taskly <command> <args>

# task structure
# - id
# - description
# - status
# - created_at
# - updated_at

COMMAND_LIST = ["list", "add", "delete", "update", "mark"]
TASKS_FILE_PATH = os.path.join(os.path.dirname(__file__), "..","data", "tasks.json")

def parse_args(raw_args):
    _, command, *args = raw_args
    return command, args

def main():
    command, args = parse_args(sys.argv)
    logging.debug(f"Command: {command}, Args: {args}")
    pass

if __name__ == "__main__":
    main()

