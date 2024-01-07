#!/usr/bin/python3
"""This module contains a Python script that takes your GitHub credentials
    (username and password) and uses the GitHub API to display your id
    """


if __name__ == "__main__":
    import sys
    import requests

    url = "https://api.github.com/user"
    username = sys.argv[1]
    paswd = sys.argv[2]
    response = requests.get(url, auth=(username, paswd))
    body = response.json()
    print(body.get("id"))
