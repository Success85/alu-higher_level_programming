#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides 2 integers and prints the result in finally."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
