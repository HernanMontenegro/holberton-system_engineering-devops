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
    userId = userDb.get('id')
    userName = userDb.get('name')

    status = []
    titles = []
    for t in taskList:
        st = t.get('completed')
        ti = t.get('title')

        status.append(st)
        titles.append(ti)


    with open(f'{userId}.csv', 'w') as f:
        csvwriter = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
        for i in range(0, len(status)):
            csvwriter.writerow([userId, userName, status[i], titles[i]])
