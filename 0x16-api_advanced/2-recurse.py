#!/usr/bin/python3
"""recurse module"""


import requests


def recurse(subreddit, hot_list=None, after=None):
    """return a list containing titles of all hot articles"""
    if hot_list is None:
        hot_list = []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My_app"}
    params = {"after": after}
    r = requests.get(url, headers=headers, params=params,
                     allow_redirects=False)
    if r.status_code != 200:
        return None
    data = r.json()
    posts = data.get("data", {}).get("children", [])
    for post in posts:
        hot_list.append(post["data"]["title"])
    after = data.get("data", {}).get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
