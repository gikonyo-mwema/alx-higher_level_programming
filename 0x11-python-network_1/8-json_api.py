#!/usr/bin/python3
"""
sends a POST request to URL with letter parameter
"""

import requests
import sys


def send_post_request(url, letter):
    """
    send a POST request to the specified URL with a letter parameter
    prnt the body of the response.
    """
    payload = {'q': letter}
    response = requests.post(url, data=payload)
    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'),
                                   json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    send_post_request(url, letter)
