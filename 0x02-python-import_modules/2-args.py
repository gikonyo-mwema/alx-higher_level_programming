#!/usr/bin/python3
import sys


def out_args():
    no_args = len(sys.argv) - 1

    print("{} argument{}:".format(no_args, 's' if no_args != 1 else ''))
    if no_args > 0:
        for index, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(index, arg))


if __name__ == "__main__":
    out_args()
