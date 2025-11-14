#!/usr/bin/python3
"""Adds all command-line arguments to a JSON list in 'add_item.json'."""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing items from the JSON file, or start with an empty list
try:
    items = load_from_json_file(filename)
except Exception:
    items = []

# Add command-line arguments (excluding the script name)
items.extend(sys.argv[1:])

# Save the updated list back to the JSON file
save_to_json_file(items, filename)
