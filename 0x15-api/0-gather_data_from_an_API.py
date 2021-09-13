#!/usr/bin/python3
''' returns information about empleyee TODO list progress. '''


import requests as req
from sys import argv as av


if (__name__ == '__main__'):
    url = 'https://jsonplaceholder.typicode.com/todos?userId=' + av[1]
    t = req.get(url)
    u = req.get('https://jsonplaceholder.typicode.com/users?id=' + av[1])

    taskList = t.json()
    userDb = u.json()[0]
    tasksTitles = ""
    tlen = len(taskList)
    tsk = 0

    for item in taskList:
        if (item.get('completed')):
            tsk += 1

    n = userDb.get('name')
    r = "Employee {} is done with tasks({}/{})".format(n, tsk, tlen)
    print(r)

    for item in taskList:
        if (item.get('completed')):
            print("\t {}".format(item.get('title')))
