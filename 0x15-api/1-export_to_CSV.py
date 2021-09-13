#!/usr/bin/python3
''' same as 0 but export data in the CSV format '''


import requests
from sys import argv as av
import json


if (__name__ == '__main__'):
    taskList = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(av[1]))
    userDb = requests.get('https://jsonplaceholder.typicode.com/users?id={}'.format(av[1]))

    taskListobj = json.loads(taskList.text)
    userDb = json.loads(userDb.text)[0]
    userId = userDb['id']
    userName = userDb['name']
    content = ""

    for i in  range(0, len(taskListobj)):
        item = taskListobj[i]
        taskTitle = item['title']
        content += f'"{userId}","{userName}","{taskTitle}"\n'

    with open(f'{userId}.csv', 'w') as f:
        f.write(content)
