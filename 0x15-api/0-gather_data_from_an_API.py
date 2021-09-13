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
    tsk = 0
    tasksTitles = ""
    tlen = len(taskList)

    for i in range(0, tlen):
        item = taskList[i]
        if (item.get('completed')):
            tsk += 1

    n = userDb.get('name')
    tsk = str(tsk)
    tlen = str(tlen)
    r = "Employee " + n + " is done with tasks(" + tsk + "/" + tlen + ")"
    print(r)

    for item in taskList:
        if (item.get('completed')):
            print("\t {}".format(item.get('title')))
