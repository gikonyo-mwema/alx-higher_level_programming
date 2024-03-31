#!/usr/bin/python3
"""
Test POST request to servers
"""


import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    # Get the URL and email from arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with email parameter
    load = {'email': email}

    # Encode the payload as URL-encoded data
    load = urllib.parse.urlencode(load)
    data = load.encode('ascii')

    # Create an HTTP POST request
    req = urllib.request.Request(url, data)

    # Send the request  and read the response
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
