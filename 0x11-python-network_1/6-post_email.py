#!/usr/bin/python3
"""This module contain a Python script that takes in a URL and an email,
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response using <requests> module.
    """


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    r = requests.post(url, data=payload)
    print(r.text)
