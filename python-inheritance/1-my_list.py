#!/usr/bin/python3
"""Module that defines a MyList class that inherits from list"""

class MyList(list):
    """Custom list class with a print_sorted method"""
    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        print(sorted(self))
