#!/usr/bin/python3
''' returns information about empleyee TODO list progress. '''

import requests as req
from sys import argv as av
import json


if (__name__ == '__main__'):
    t = req.get(f'https://jsonplaceholder.typicode.com/todos?userId={av[1]}')
    u = req.get(f'https://jsonplaceholder.typicode.com/users?id={av[1]}')

    taskList = json.loads(t.text)
    userDb = json.loads(u.text)[0]
    doneTasks = 0
    tasksTitles = ""
    taskListLength = len(taskList)

    for i in range(0, taskListLength):
        item = taskList[i]
        if (item['completed']):
            doneTasks += 1
            tasksTitles += ('\t ' + item['title']) + '\n'

    nam = userDb['name']
    print(f"Employee {nam} is done with tasks({doneTasks}/{taskListLength})")
    print(tasksTitles, end="")
