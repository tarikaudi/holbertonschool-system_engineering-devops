#!/usr/bin/python3
"""comment for the checker"""

import csv
import requests
from sys import argv

if __name__ == "__main__":

    id = int(argv[1])
    r = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    filename = argv[1] + ".csv"

    for user in users:
        if user.get("id") == id:
            username = user.get("username")
            break

    with open(filename, mode='w') as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for tasks in r:
            if tasks.get("userId") == id:
                w.writerow([argv[1], username, tasks.get("completed"),
                           tasks.get("title")])
