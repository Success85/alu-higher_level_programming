#!/usr/bin/python3
"""Module to check if an object is a subclass instance"""


def inherits_from(obj, a_class):

    """Returns True if obj is an instance of a class that inherits from a_class"""
    return type(obj) != a_class and isinstance(obj, a_class)
