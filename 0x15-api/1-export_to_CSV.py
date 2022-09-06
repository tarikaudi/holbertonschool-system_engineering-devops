#!/usr/bin/python3
"""comment for the checker"""

import requests
from sys import argv

if __name__ == "__main__":

        USER_ID = 0
        USERNAME = ""
        TASK_COMPLETED_STATUS = ""
        TASK_TITLE = []
        id = int(argv[1])
        r = requests.get('https://jsonplaceholder.typicode.com/todos')
        users = requests.get('https://jsonplaceholder.typicode.com/users')

        for user in users.json():
                if user.get("id") == id:
                        USER_ID = user.get("id")
                        USERNAME = user.get("username")
                        print("aa", USER_ID, USERNAME)
                        break

        for tasks in r.json():
            if tasks.get("userId") == id:
                    TASK_COMPLETED_STATUS
