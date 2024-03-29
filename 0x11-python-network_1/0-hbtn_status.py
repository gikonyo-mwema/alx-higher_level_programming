#!/usr/bin/python3
"""
This module fetches the status from provide URL using urllib
Displays the response body.
"""

import urllib.request


def fetch_status():
    """
    Fetches the status from URL
    """
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        data = response.read()
        text_data = data.decode('utf-8')

        # display the response body
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(text_data))


if __name__ == "__main__":
    fetch_status()
