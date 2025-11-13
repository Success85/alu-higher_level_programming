#!/usr/bin/python3
"""Module that defines BaseGeometry with an unimplemented area method"""


class BaseGeometry:

    """BaseGeometry class with an area method"""
    
    def area(self):
        """Raises an exception as area is not implemented"""
        raise Exception("area() is not implemented")
