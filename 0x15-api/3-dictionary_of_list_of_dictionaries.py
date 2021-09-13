#!/usr/bin/python3
''' same as 0 but export data in the CSV format '''


import requests
from sys import argv as av
import json


if (__name__ == '__main__'):
    taskList = requests.get('https://jsonplaceholder.typicode.com/todos')
    userDb = requests.get('https://jsonplaceholder.typicode.com/users')

    taskList = json.loads(taskList.text)
    userDb = json.loads(userDb.text)
    json_dict = {}

    for user in userDb:
        aux_list = []
        for item in taskList:
            aux_list.append(item)

        json_dict[user['id']] = aux_list

    with open('todo_all_employees.json', 'w') as f:
        json.dump(json_dict, f)
