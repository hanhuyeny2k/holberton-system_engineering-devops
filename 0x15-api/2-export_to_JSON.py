#!/usr/bin/python3
""" Gather data from an API """

import json
import requests
from sys import argv

if __name__ == "__main__":

    NUMBER_OF_DONE_TASKS = 0
    t = []
    q = {}
    todos_dict = {}
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1])).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(argv[1])).json()
    TOTAL_OF_TASKS_DONE = len(todos)
    for i in todos:
        if int(argv[1]) == i.get('userId'):
            q = {"task": i.get('title'), "completed": i.get('completed'),
                 "username": user.get('username')}
            t.append(q)
    todos_dict[argv[1]] = t
    filename = argv[1] + ".json"
    with open(filename, mode='w') as f:
        json.dump(todos_dict, f)
