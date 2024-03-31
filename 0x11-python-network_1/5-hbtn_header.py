#!/usr/bin/python3
"""
This module sends a GET request to a URL
Prints value of variable X-Request-Id in response header
"""

import requests
import sys


def fetch_request_id(url):
    """
    sends a GET request to specified URL and print X-Request-Id
    """
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_request_id(url)
