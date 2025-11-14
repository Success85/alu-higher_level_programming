#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them to a JSON file named 'add_item.json'. 
It uses 'save_to_json_file' to write to the file and 
'load_from_json_file' to read from it. If the file does not exist,
it creates a new one.
"""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except Exception:
    items = []

""" Add command-line arguments (except the script name) to the list """
items.extend(sys.argv[1:])

""" Save the updated list back to the JSON file """
save_to_json_file(items, filename)
