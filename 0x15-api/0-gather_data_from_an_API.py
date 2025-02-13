#!/usr/bin/python3
"""API"""


import sys
import requests

url = "https://jsonplaceholder.typicode.com/"
e_name = requests.get(url + "users/{}".format(sys.argv[1])).json()
todos = requests.get(url + "todos", params = {"userId": sys.argv[1]}).json()
completed = [t.get("title") for t in todos if t.get("completed") is True]
print("Employee {} is done with tasks({}/{}):".format(e_name.get("name"), len(completed), len(todos)))
for c in completed:
    print("\t {}".format(c))
