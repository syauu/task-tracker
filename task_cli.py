# get data from json
# list task
# add, update, delete task
# list completed task
# list task in progress

# properties:
# {
#   "id": ,
#   "description": ,
#   "status": ,
#   "createdAt": ,
#   "updatedAt": 
# }
# 

# use positional arguments
# handles error

import json
import datetime

task_file = "tasks.json"

def loadFile():
    with open(task_file, "r") as file: # r means read mode. 
        return json.load(file) # guna load() untuk read dan parse to python dict/list

def saveFile(tasks):
    with open(task_file, "w") as file:
        json.dump(tasks, file, indent=4)

def listTask():
    tasks = loadFile()
    try:
        if not tasks:
            print("No tasks available")
        else:
            for task in tasks:
                print(f"{tasks['id']}. {tasks['description']}. Status: {tasks['status']}")
    except FileNotFoundError:
        print("json file not found")
    except json.JSONDecodeError:
        print("Wrong json format")

def addTask():
    pass


def updateTask():
    pass

def deleteTask():
    pass

listTask()