#!/usr/bin/python3
"""This script gets information about a given employee's TODO list progress."""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    # Initialize tasks and grab username
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    user = sys.argv[1]
    # Request the employee ID, then their todo list.
    employee_id = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user)
    )
    todo_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(user)
    )
    # Load the information sent back as variables
    user_info = json.loads(employee_id.text)
    todo_info = json.loads(todo_list.text)
    # Grab the employee's name from your new dictionary
    EMPLOYEE_NAME = user_info['name']
    # Count and compare total and completes tasks
    for task in todo_info:
        TOTAL_NUMBER_OF_TASKS += 1
        if task['completed']:
            NUMBER_OF_DONE_TASKS += 1
    # Print the results
    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS)
          )
    # Print completed tasks in particular
    for task in todo_info:
        if task['completed']:
            print("\t {}".format(task['title']))
