#!/usr/bin/python3
"""
This module defines a function for appending text to a file.
If the file does not exist, it will be created automatically.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8) and returns
    the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to write at the end of the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
