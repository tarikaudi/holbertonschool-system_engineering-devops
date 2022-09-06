#!/usr/bin/python3
"""comment for the checker"""

import json
import requests
from sys import argv

if __name__ == "__main__":

    id = int(argv[1])
    r = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    stri = {}
    json_file = argv[1] + ".json"

    stri[argv[1]] = []

    for user in users:
        if user.get("id") == id:
            username = user.get("username")
            break

    for tasks in r:
        if tasks.get("userId") == id:
            temp = {
                "task": tasks.get("title"),
                "completed": tasks.get("completed"),
                "username": username
                }
            stri[argv[1]].append(temp)

    with open(json_file, 'w') as f:
        json.dump(stri, f)
