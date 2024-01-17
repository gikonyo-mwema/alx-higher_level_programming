#!/usr/bin/python3
def lookup(obj):
    """
    Function to get a list of available attributes and methods of an object.

    Parameters:
    obj (any): The object whose attributes and methods are to be returned.

    Returns:
    list: A list of strings representing the attributes and methods of the object.
    """
    return dir(obj)

