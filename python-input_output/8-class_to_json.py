#!/usr/bin/python3
"""
This module contains a function that returns the dictionary
representation of a class instance for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of an object's attributes.

    Args:
        obj: An instance of any class.

    Returns:
        dict: A dictionary containing all attributes of obj
              that can be serialized to JSON (e.g., list, dict,
              string, integer, boolean).
    """
    return obj.__dict__
