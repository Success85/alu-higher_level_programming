#!/usr/bin/python3
"""LockedClass that only allows 'first_name' as an attribute."""


class LockedClass:
    """accepts only attribute 'first_name'."""
    __slots__ = ('first_name',)
