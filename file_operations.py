import os
import json

def load_or_create(file_name):
    """Load the file or create it if it doesn't exist."""
    try:
        if not os.path.exists(file_name):
            with open(file_name, 'w') as file:
                json.dump({}, file)
            return {}
        else:
            with open(file_name, 'r') as file:
                return json.load(file)
    except json.JSONDecodeError:
        print(f"Error: Failed to load {file_name}, file might be corrupted.")
        return {}
