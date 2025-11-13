#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class with overridden __str__"""

    def __init__(self, size):
        """Initialize a square with private size validated"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square"""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
