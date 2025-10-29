#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer using '{:d}'.format() and returns True if successful."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
