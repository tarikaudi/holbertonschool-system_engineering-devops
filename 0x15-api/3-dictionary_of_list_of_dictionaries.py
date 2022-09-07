#!/usr/bin/python3
"""comment for the checker"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    data = {}
    usernames = {}

    for user in users:
        usernames[str(user.get("id"))] = user.get("username")

    for tasks in r:
        if str(tasks.get("userId")) not in data:
            data[str(tasks.get("userId"))] = []
        data[str(tasks.get("userId"))].append({
                                            "task": tasks.get("title"),
                                            "completed": tasks.get("completed"),
                                            "username": usernames.get(
                                                str(tasks.get("userId")))
                                            })

    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)
