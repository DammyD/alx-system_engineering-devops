#!/usr/bin/python3
'''A script that uses RET API to fecth JSON format.
'''
import json
import requests


API = 'https://jsonplaceholder.typicode.com'
'''The API's URL.'''


if __name__ == '__main__':
    users_data = requests.get('{}/users'.format(API)).json()
    todos_data = requests.get('{}/todos'.format(API)).json()
    json_data = {}
    for user in users_data:
        id = user.get('id')
        user_name = user.get('username')
        todos = list(filter(lambda x: x.get('userId') == id, todos_data))
        data = list(map(
            lambda x: {
                'username': user_name,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            todos
        ))
        json_data['{}'.format(id)] = data
    with open('todo_all_employees.json', 'w') as file:
        json.dump(json_data, file)
