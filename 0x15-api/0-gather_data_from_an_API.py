#!/usr/bin/python3
""" Gather data from an API """

import requests
from sys import argv

NUMBER_OF_DONE_TASKS = 0
t = []
user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                    .format(argv[1])).json()
todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(argv[1])).json()
TOTAL_OF_TASKS_DONE = len(todos)
for i in todos:
    if i.get('completed') is True:
        NUMBER_OF_DONE_TASKS += 1
        q = i.get('title')
        t.append(q)
TODO = "Employee {} is done with tasks({}/{}):".format(
        user.get('name'), NUMBER_OF_DONE_TASKS, TOTAL_OF_TASKS_DONE)
print(TODO)
for i in t:
    print('\t {}'.format(i))
