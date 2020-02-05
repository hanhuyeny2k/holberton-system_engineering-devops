#!/usr/bin/python3
""" Gather data from an API """

import json
import requests

if __name__ == "__main__":

    q = {}
    todos_dict = {}
    user = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    for j in user:
        task_list = []
        for i in todos:
            if j.get('id') == i.get('userId'):
                q = {"username": j.get('username'), "task": i.get('title'),
                     "complete": i.get('completed')}
            task_list.append(q)
    todos_dict[j.get('id')] = task_list
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todos_dict, f)
