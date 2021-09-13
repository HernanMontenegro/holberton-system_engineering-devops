#!/usr/bin/python3
''' same as 0 but export data in the CSV format '''


import requests as req
from sys import argv as av
import json
import csv


if (__name__ == '__main__'):
    t = req.get(f'https://jsonplaceholder.typicode.com/todos?userId={av[1]}')
    u = req.get(f'https://jsonplaceholder.typicode.com/users?id={av[1]}')

    taskList = json.loads(t.text)
    userDb = json.loads(u.text)[0]
    userId = userDb['id']
    userName = userDb['name']
    content = []
    fields = ["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"]


    for i in range(0, len(taskList)):
        item = taskList[i]
        taskTitle = item['title']
        status = item['completed']
        content.append([userId, userName, status, taskTitle])

    with open(f'{userId}.csv', 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(fields)
        csvwriter.writerows(content)
