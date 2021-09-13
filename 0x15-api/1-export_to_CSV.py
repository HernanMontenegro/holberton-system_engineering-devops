#!/usr/bin/python3
''' same as 0 but export data in the CSV format '''


import requests as req
from sys import argv as av
import json


if (__name__ == '__main__'):
    t = req.get(f'https://jsonplaceholder.typicode.com/todos?userId={av[1]}')
    u = req.get(f'https://jsonplaceholder.typicode.com/users?id={av[1]}')

    taskList = json.loads(t.text)
    userDb = json.loads(u.text)[0]
    userId = userDb['id']
    userName = userDb['name']
    content = ""

    for i in range(0, len(taskList)):
        item = taskList[i]
        taskTitle = item['title']
        status = item['completed']
        content += f'"{userId}","{userName}","{status}","{taskTitle}"\n'

    with open(f'{userId}.csv', 'w') as f:
        f.write(content)
