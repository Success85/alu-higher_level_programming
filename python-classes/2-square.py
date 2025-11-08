#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """This is the class Square and defining its size. And the size must be reater than or equal to 0"""

    if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

~
~
