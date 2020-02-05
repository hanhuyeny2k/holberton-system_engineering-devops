#!/usr/bin/python3
""" Gather data from an API """

import csv
import requests
from sys import argv

if __name__ == "__main__":

    NUMBER_OF_DONE_TASKS = 0
    t = []
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1])).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(argv[1])).json()
    with open('{}.csv'.format(argv[1]), mode='w') as f:
        tasks = csv.writer(f, quoting=csv.QUOTE_ALL)
        for i in todos:
            tasks.writerow([argv[1], user.get('username'),
                            i.get('completed'), i.get('title')])
