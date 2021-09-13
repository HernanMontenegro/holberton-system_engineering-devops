#!/usr/bin/python3
''' same as 0 but export data in the json format '''


import json
import requests as req
from sys import argv as av


if (__name__ == '__main__'):
    url = 'https://jsonplaceholder.typicode.com/todos?userId=' + av[1]
    t = req.get(url)
    u = req.get(f'https://jsonplaceholder.typicode.com/users?id=' + av[1])

    taskList = t.json()
    userDb = u.json()[0]
    json_dict = {}
    aux_list = []

    for item in taskList:
        aux = {}
        aux['task'] = item.get('title')
        aux['completed'] = item.get('completed')
        aux['username'] = userDb.get('username')
        aux_list.append(aux)

    json_dict[av[1]] = aux_list

    with open(f'{av[1]}.json', 'w') as f:
        json.dump(json_dict, f)
