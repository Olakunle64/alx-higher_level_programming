#!/usr/bin/python3
"""Please list 10 commits (from the most recent to oldest) of the repository
    "rails" by the user "rails". You must use the GitHub API, here is the
    documentation https://developer.github.com/v3/repos/commits/
    Print all commits by: `<sha>: <author name>` (one by line)
    """

if __name__ == "__main__":
    import requests
    import sys

    repoName = sys.argv[1]
    ownerName = sys.argv[2]
    url = f'https://api.github.com/repos/{ownerName}/{repoName}/commits'
    response = requests.get(url)
    body = response.json()
    for each in body[:10]:
        sha = each.get("sha")
        authorName = each.get("commit").get("author").get("name")
        if sha and authorName:
            print(f'{sha}: {authorName}')
