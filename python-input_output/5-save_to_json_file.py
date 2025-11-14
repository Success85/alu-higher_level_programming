#!/usr/bin/python3
"""
This module provides a function to serialize a Python object
to a file in JSON format.
"""


import json

def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a file in JSON representation.

    Args:
        my_obj (object): The Python object to serialize.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
