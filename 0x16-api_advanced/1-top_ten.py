#!/usr/bin/python3
"""query the title of first 10 hot posts"""


import requests


def top_ten(subreddit):
    """rprint the title of the first 10 posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My_app"}
    params = {"limit": 10}
    r = requests.get(url, params=params, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        data = r.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post["data"]["title"])
    else:
        print("None")
