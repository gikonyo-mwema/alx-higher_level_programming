#!/usr/bin/python3
"""
Sends a GET request to URL and print response body
if HTTP status code > 400, print error code and status code
"""
import requests
import sys


def fetch_url(url):
    """
    send GET request, print error for >= 400
    """
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
