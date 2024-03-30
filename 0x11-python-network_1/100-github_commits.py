#!/usr/bin/python3
"""lists the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for j in range(10):
            print("{}: {}".format(
                commits[j].get("sha"),
                commits[j].get("commit").get("author").get("name")))
    except IndexError:
        pass
