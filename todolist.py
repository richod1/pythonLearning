#todolist app
def display_list(tasks):
    if not tasks:
        print("List has no task :")
    else:
        print("Todo list ")
        for index,task in enumerate(tasks,start=1):
            print(f"{index}. {task}")

def add_task(tasks,new_task):
    tasks.append(new_task)
    print(f"New task add {new_task} to the list")

def remove_task(tasks,task_index):
    if 1<=tasks<=len(task_index):
        removed_task=tasks.pop(task_index-1)
        print(f"Tasks {removed_task} has been removed from the todolist")
    else:
        print("Invalid task ,please select new task index")

def todolist_app():
    tasks=[]

    while True:
        print("\nOptions")
        print("1. Display list")
        print("2. Add todo list")
        print("3. remove list")
        print("4. Quit")


        chioce=input("Pleas enter your options :(1/2/3/4)")

        if chioce=='1':
            display_list(tasks)
        elif chioce=='2':
            new_task=input("add list here :")
            add_task(tasks,new_task)
        elif chioce=='3':
            task_index=int(input("Enter the index of the task to be removed"))
            remove_task(tasks,task_index)
        elif chioce=='4':
            print("Existing todo list.GoodBye")
            break
        else:
            print("Invalid Option Try again")

if __name__=="__main__":
    todolist_app()
