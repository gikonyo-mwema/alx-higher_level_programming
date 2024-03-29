#!/usr/bin/python3
"""
Sends a request to URL
Displays the value of X-Request-Id variable found in header
"""

import urllib.request
import sys


def fetch_request_id():
    """
    send request & disply X-Request-Id
    """
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))


if __name__ == "__main__":
    fetch_request_id()
