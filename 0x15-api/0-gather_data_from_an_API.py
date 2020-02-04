#!/usr/bin/python3
""" Gather data from an API """

import requests
import sys


NUMBER_OF_DONE_TASKS = 0
TOTAL_OF_TASKS_DONE = 0
t = []
users = requests.get('https://jsonplaceholder.typicode.com/users')
todos = requests.get('https://jsonplaceholder.typicode.com/todos')
for todo_user in users.json():
    if todo_user['id'] == int(sys.argv[1]):
        for todo_list in todos.json():
            if todo_list['userId'] == int(sys.argv[1]) and\
               todo_list.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                q = todo_list.get('title')
                t.append(q)
            if todo_list['userId'] == int(sys.argv[1]):
                TOTAL_OF_TASKS_DONE += 1
            TODO = "Employee {} is done with tasks({}/{})"\
                .format(todo_user['name'],
                        NUMBER_OF_DONE_TASKS, TOTAL_OF_TASKS_DONE)
        print(TODO)
        for i in t:
            print('\t {}'.format(i))
        break
