#!/usr/bin/python3
"""This module contain a Write a Python script that takes in a URL,
    sends a request to the URL and displays the body of the response
    (decoded in utf-8).
    """


if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    response = request.get(url)
    if response.status_code >= 400:
        print(f'Error code: {response.status_code}')
    else:
        print(response.text)
