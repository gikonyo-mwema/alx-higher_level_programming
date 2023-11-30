#!/usr/bin/python3
import sys


def add_args():
    args = sys.argv[1:]
    total = sum(int(arg) for arg in args)
    return total


if __name__ == "__main__":
    result = add_args()
    print(result)
