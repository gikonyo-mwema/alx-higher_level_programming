#!/usr/bin/python3
"""
Sends a POST request to URL with and email as parameter
Prints the body of the response
"""

import requests
import sys


def send_post_request(url, email):
    """
    sends POST request to specified URL with an email and print body
    """
    payload = {"email": email}
    response = requests.post(url, data=payload)
    print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
