#!/usr/bin/python3

"""
Defines a function that adds 2 integer
"""


def add_integer(a, b=98):
    """Return the addition of integer a and b.
    Float arguments are casted to integers before addition is performed.
    Raises:
        TypeError: If a and b are non-integers or non-floats.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
