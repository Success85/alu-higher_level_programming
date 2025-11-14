#!/usr/bin/python3
"""
This module defines a Student class with methods for JSON
serialization and deserialization.
"""


class Student:
    """
    Represents a student with a first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes listed in attrs
        will be included in the dictionary.

        Args:
            attrs (list, optional): List of attribute names to include.

        Returns:
            dict: Dictionary containing the requested attributes or all
            attributes if attrs is None or invalid.
        """
        if type(attrs) == list and all(type(i) == str for i in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values
        from a dictionary.

        Args:
            json (dict): A dictionary where keys are attribute names
                         and values are the new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
