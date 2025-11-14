#!/usr/bin/python3
"""
This module provides a function that converts a JSON string
into its corresponding Python data structure.
"""


import json

def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python data structure obtained from the JSON string.
    """
    return json.loads(my_str)
