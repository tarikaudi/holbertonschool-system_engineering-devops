#!/usr/bin/python3
"""comment for the checker"""

import requests
from sys import argv

if __name__ == "__main__":

        EMPLOYEE_NAME = ""
        NUMBER_OF_DONE_TASKS = 0
        TOTAL_NUMBER_OF_TASKS = 0
        TASK_TITLE = []
        id = int(argv[1])
        r = requests.get('https://jsonplaceholder.typicode.com/todos')
        users = requests.get('https://jsonplaceholder.typicode.com/users')

        for user in users.json():
                if user.get("id") == id:
                        EMPLOYEE_NAME = user.get("name")
                        break

        for tasks in r.json():
            if tasks.get("userId") == id:
                    TOTAL_NUMBER_OF_TASKS += 1
                    if tasks.get("completed") == True:
                            NUMBER_OF_DONE_TASKS += 1
                            TASK_TITLE.append(tasks.get("title"))

        print ("Employee {} is done with tasks({}/{})".format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
        
        for tasks in TASK_TITLE:
            print("\t {}".format(tasks))
