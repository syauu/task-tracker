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
import time

task_file = "tasks.json"

def loadFile():
    with open(task_file, "r") as file: # r means read mode. 
        return json.load(file) # guna load() untuk read dan parse to python dict/list

def saveFile(tasks):
    with open(task_file, "w") as file:  # w means write mode
        json.dump(tasks, file, indent=4)    # dump() to send python object to json data
                                            # dump(python object, file yang nak diedit, other arguments...)
                                            # guna indent=4 untuk bagi data dalam json nampak kemas

def getUserInput():
    # description
    desc = input("What task?: ")
    # status
    print("Choose status:")
    print("1. To do")
    print("2. In progress")
    print("3. Completed")
    status_choice = input("Choose status (1/2/3): ")
    match status_choice:
        case "1":
            status = "todo"
        case "2":
            status = "in progress"
        case "3":
            status = "completed"
        case _:
            status = "todo"

    return desc, status

def listTask():
    tasks = loadFile()
    try:
        if not tasks:
            print("No tasks available")
        else:
            for index, task in enumerate(tasks, start=1):   #guna enumerate() untuk display index for list task
                print(f"{index}. {task['desc']}.")
                print(f"Status: {task['status']}")
                print()
    except FileNotFoundError:
        print("json file not found")
    except json.JSONDecodeError:
        print("Wrong json format")

def addTask():
    # loadFile dulu. it will read and change data from json into python dict
    tasks = loadFile()
    # get the details for new task
    desc, status = getUserInput()
    new_task = {
        "id": int(time.time()),
        "desc": desc,
        "status": status,
        "createdAt": datetime.datetime.now().strftime("%c"),
        "updatedAt": datetime.datetime.now().strftime("%c")
    }
    # then append(). it will add new task to the python object, belum edit json lagi
    tasks.append(new_task)
    # then saveFile. ini baru w mode, baru dia edit json file
    saveFile(tasks)

    print("Task added successfully!")


def updateTask():
    tasks = loadFile()
    listTask()
    try:
        chosenTask = int(input("Which task to update? Enter number: ")) - 1

        # status
        print("Choose status:")
        print("1. To do")
        print("2. In progress")
        print("3. Completed")
        status_choice = input("Choose status (1/2/3): ")
        match status_choice:
            case "1":
                status_update = "todo"
            case "2":
                status_update = "in progress"
            case "3":
                status_update = "completed"
            case _:
                status_update = "todo"

        tasks[chosenTask]["status"] = status_update
        tasks[chosenTask]["updatedAt"] = datetime.datetime.now().strftime("%c")

        saveFile(tasks)
        print("Task status updated successfully")
    except ValueError:
        print("Please enter a number")
    

def deleteTask():
    tasks = loadFile()
    listTask()
    try:
        chosenTask = int(input("What task to delete? Enter number: ")) - 1
        removed = tasks.pop(chosenTask)

        saveFile(tasks)
        print(f"Task {removed['desc']} deleted.")
    except ValueError:
        print("Please enter a valid number")

def menuOption():
    print("===MENU===")
    print("1. List task")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    try:
        option = int(input("Choose your option (1/2/3/4):"))
        match option:
            case 1:
                listTask()
            case 2:
                addTask()
            case 3:
                updateTask()
            case 4:
                deleteTask()
    except ValueError:
        print("Please enter a valid number")
    

menuOption()