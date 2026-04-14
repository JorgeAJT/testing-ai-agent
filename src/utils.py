import json
import os

MEMORY_FILE = "memory.json"

def load_users():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_users(users):
    with open(MEMORY_FILE, "w") as f:
        json.dump(users, f, indent=4)
