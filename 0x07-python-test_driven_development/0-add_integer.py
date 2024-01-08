#!/usr/bin/python3
"""
Function add_integer that add two numbers.

The function takes two parameters: a and b.
Both parameters must e integers or floats,
otherwise a TypeError exception is raised.
If the parameters are floats, they are first
casted to integers. The function returns the sum of a and b.
"""


def add_integer(a, b=98):
    """
    This function adds two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number. Default is 98.

    Returns:
    int: the sum of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
