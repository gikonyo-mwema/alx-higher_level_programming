#!/usr/bin/python3
"""
Send a GET request to a speciied URL
Prints the body of the response.
"""

import requests


def fetch_url(url):
    """
    Function sends a GET request to URL and prints body of response
    """
    response = requests.get(url)
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_url(url)
