#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extend both tuples to ensure they have at least 2 elements
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Take only the first two elements and add them
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
