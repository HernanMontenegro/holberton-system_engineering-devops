#!/usr/bin/python3
''' returns information about empleyee TODO list progress. '''

import requests
from sys import argv as av
import json


if (__name__ == '__main__'):
    taskList = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(av[1]))
    userDb = requests.get('https://jsonplaceholder.typicode.com/users?id={}'.format(av[1]))

    taskListobj = json.loads(taskList.text)
    userDb = json.loads(userDb.text)[0]
    doneTasks = 0
    tasksTitles = ""
    taskListLength = len(taskListobj)

    for i in  range(0, taskListLength):
        item = taskListobj[i]
        if (item['completed'] == True):
            doneTasks += 1
        tasksTitles += ('\t ' + item['title'])
        if (i != taskListLength - 1):
            tasksTitles += '\n'

    print(f"Employee {userDb['name']} is done with tasks({doneTasks}/{taskListLength})")
    print(tasksTitles)
