#!/usr/bin/python3
''' same as 0 but export data in the json format '''


import requests
from sys import argv as av
import json


if (__name__ == '__main__'):
    taskList = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(av[1]))
    userDb = requests.get('https://jsonplaceholder.typicode.com/users?id={}'.format(av[1]))

    taskList = json.loads(taskList.text)
    userDb = json.loads(userDb.text)[0]
    json_dict = {}
    aux_list = []

    for item in taskList:
        aux_list.append(item)

    json_dict[av[1]] = aux_list

    with open(f'{av[1]}.json', 'w') as f:
        json.dump(json_dict, f)
