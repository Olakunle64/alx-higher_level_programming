#!/usr/bin/python3
""" This module contains a script that fetches
    https://alx-intranet.hbtn.io/status
    """


if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        utf = body.decode("utf-8")
    print('Body response:')
    print(f'\t- type: {type(body)}')
    print(f'\t- content: {body}')
    print(f'\t- utf8 content: {utf}')
