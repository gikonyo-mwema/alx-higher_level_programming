#!/usr/bin/python3
"""
Sends a GET request to a specified URL
Prints the body
"""

import sys
import urllib.request
import urllib.error


def send_request(url):
    """
    send GET request to specified URL, print body.
    if error occurs, catches exception, print status code.
    """
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.getcode()))


if __name__ == "__main__":
    url = sys.argv[1]
    send_request(url)
