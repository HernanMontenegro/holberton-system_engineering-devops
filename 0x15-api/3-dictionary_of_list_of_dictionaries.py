#!/usr/bin/python3
''' same as 0 but export data in the CSV format '''


import json
import requests
from sys import argv as av


if (__name__ == '__main__'):
    userDb = requests.get('https://jsonplaceholder.typicode.com/users')

    userDb = userDb.json()
    json_dict = {}

    for user in userDb:
        aux_list = []
        usrId = str(user.get('id'))
        url = 'https://jsonplaceholder.typicode.com/todos?userId=' + usrId
        taskList = requests.get(url)
        for item in taskList.json():
            aux = {}
            aux['task'] = item.get('title')
            aux['completed'] = item.get('completed')
            aux['username'] = user.get('username')
            aux_list.append(aux)
        json_dict[usrId] = aux_list

    with open('todo_all_employees.json', 'w') as f:
        json.dump(json_dict, f)
