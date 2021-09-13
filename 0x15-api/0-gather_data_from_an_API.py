#!/usr/bin/python3
''' returns information about empleyee TODO list progress. '''

import requests
from sys import argv as av


if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users?id={}'
                        .format(av[1]))
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(av[1]))
    usrDb = user.json()
    taskArr = tasks.json()
    usrName = usrDb[0]['name']
    doneTasks = 0

    for item in taskArr:
        if item['completed']:
            doneTasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(usrName, doneTasks, len(taskArr)))

    for item in taskArr:
        if item['completed']:
            print("\t {}".format(item.get('title')))
