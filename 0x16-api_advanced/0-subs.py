#!/usr/bin/python3
"""request a redit API"""


import requests


def number_of_subscribers(subreddit):
    """queries and return the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My_app"}
    r = requests.get(url, allow_redirects=False, headers=headers)
    if r.status_code == 200:
        data = r.json()
        return data["data"]["subscribers"]
    else:
        return 0
