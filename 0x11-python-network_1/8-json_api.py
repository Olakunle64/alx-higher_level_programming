#!/usr/bin/python3
"""This module contains Write a Python script that takes in a
    letter and sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
    """


if __name__ == "__main__":
    import requests
    import sys
    import json

    url = "http://0.0.0.0:5000/search_user"
    if not sys.argv[1]:
        q = ""
    else:
        q = sys.argv[1]
    response = requests.post(url, params={'q': q})
    body = response.text
    if not body:
        print("No result")
        return
    try:
        dict_body = body.json()
        id = dict_body.get("id")
        name = dict_body.get("name")
        print(f'[{id}] {name}')
    except json.JSONDecodeError:
        print("Not a valid JSON")
