#!/usr/bin/python3
"""This module contains Write a Python script that takes in a
    letter and sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
    """


if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    response = requests.post(url, data={'q': q})
    body = response.json()
    else:
        try:
            if not body:
                print("No result")
            else:
                id = body.get("id")
                name = body.get("name")
                print(f'[{id}] {name}')
        except Exception:
            print("Not a valid JSON")
