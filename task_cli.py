# get data from json
# list task (done)
# add, update, delete task (done)
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
    print("")
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
            print("")
        else:
            print("")
            for index, task in enumerate(tasks, start=1):   #guna enumerate() untuk display index for list task
                print(f"{index}. {task['desc']}.")
                print(f"Status: {task['status']}")
                print()
    except FileNotFoundError:
        print("json file not found")
    except json.JSONDecodeError:
        print("Wrong json format")

def addTask():
    print("1. Single task")
    print("2. Multiple tasks")
    sinOrMul = int(input("Single or multiple task? (1/2): "))

    # loadFile dulu. it will read and change data from json into python dict
    def singleTask():
        tasks = loadFile()
        # get the details for new task
        print("")
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
        print("")
        print("Task added successfully!")
        print("")
 
    match sinOrMul:
        case 1:
            singleTask()
            return
        case 2:
            repeat = 1
            while repeat != "0":
                singleTask()
                repeatInput = input("Press any button to continue or 0 to stop: ")
                print("")
                repeat = repeatInput
        case _:
            print("Invalid choice")



def updateTask():
    tasks = loadFile()
    if not tasks:
        print("No tasks available")
        print("")
        return
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
        print("")
        print("Task status updated successfully")
        print("")
    except ValueError:
        print("Please enter a number")
    except IndexError:
        print("Enter valid number")
    

def deleteTask():
    tasks = loadFile()
    if not tasks:
        print("No tasks available")
        print("")
        return
    
    listTask()
    try:
        chosenTask = int(input("What task to delete? Enter number or enter 0 to delete all tasks: ")) -1
        if chosenTask == -1:
            tasks.clear()
            saveFile(tasks)
            print("All task deleted")
            print("")
        else:
            removed = tasks.pop(chosenTask)

            saveFile(tasks)
            print(f"Task {removed['desc']} deleted.")
            print("")
    except ValueError:
        print("Please enter a valid number")
    except IndexError:
        print("No task found with that number")

def listCompletedTask():
    tasks = loadFile()
    found = False
    for index, task in enumerate(tasks, start=1):
        if task["status"] == "completed":
            print("Completed task:")
            print(f"{index}. {task['desc']}")
            found = True
    if not found:
        print("No completed task found")
        print("")

def listProgressTask():
    tasks = loadFile()
    found = False
    for index, task in enumerate(tasks, start=1):
        if task["status"] == "in progress":
            print(f"{index}. {task['desc']}")
            found = True
    if not found:
        print("No in progress task")
        print("")

def listNotDone():
    tasks = loadFile()
    found = False
    for index, task in enumerate(tasks, start=1):
        if task["status"] == "todo":
            print(f"{index}. {task['desc']}. Status: {task['status']}")
            found = True
    if not found:
        print("All tasks are completed")
        print("")

def mainMenu():
    while True:
        print("======MENU======")
        print("1. List task")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Get completed task")
        print("6. Get in progress task")
        print("7. Get todo task")
        print("8. Exit")
        print("==========================")
        try:
            option = int(input("Choose your option: "))
            match option:
                case 1:
                    listTask()
                case 2:
                    addTask()
                case 3:
                    updateTask()
                case 4:
                    deleteTask()
                case 5:
                    listCompletedTask()
                case 6:
                    listProgressTask()
                case 7:
                    listNotDone()
                case 8:
                    print("Bye-bye")
                    break
                case _:
                    print("Invalid number, try again")
        except ValueError:
            print("Please enter a valid number")
    

mainMenu()