#!/usr/bin/python3
"""Defines a function to check if an object is exactly an instance"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of the specified class.

    Args:
        obj: the object.
        a_class: The class to check aginst.

    Returns:
        True if the object is exactly an instance of the specified class
    """
    return type(obj) is a_class
