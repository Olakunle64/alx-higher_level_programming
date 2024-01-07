#!/usr/bin/python3
""" This module contains a script that fetches https://alx-intranet.hbtn.io/status
    with the <requests> module.
    """


if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.text
    print('Body response:')
    print(f'\t- type: {type(body)}')
    print(f'\t- content: {body}')
