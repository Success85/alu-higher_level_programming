#!/usr/bin/python3
"""
This module provides a function that converts a Python object
into its JSON string representation.
"""


import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object.

    Args:
        my_obj: The Python object to be converted to a JSON string.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
