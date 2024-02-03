#!/usr/bin/python3
"""Defines a function to check if an object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class."""


def is_kin_of_class(obj, a_class):
    """Check if an object is an instance of, or if the object is an instance
        specified class.

        Args:
            obj: The object to check.
            a_class: The class to check against.

        Returns:
            True if the object is an instance of, or if the object is an
            object is an instance of a class that inherited from, the
            specified class, otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
