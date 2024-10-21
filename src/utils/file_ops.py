from pathlib import Path
import json

def get_file_contents(path):
    if not Path(path).exists():
        with open(path, "w") as file:
            json.dump([], file, indent=4)

    with open(path, "r") as file:
        return json.load(file)

def save_file_contents(path, data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)