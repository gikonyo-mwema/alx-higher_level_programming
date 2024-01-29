#!/usr/bin/python3
"""Defiens a function to read a file and print its contents."""


def read_file(filename=""):
    """Open the file in read mode with UTF-8 encoding and print content."""
    with open(filename, encoding="utf8") as f:
        print(f.read(), end="")
