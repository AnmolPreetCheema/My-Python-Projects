todo_list = []

def show_tasks():
    if not todo_list:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            status = "done" if task["done"] else "not done"
            print(f"{index}. [{status}] {task['task']}")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append({"task": task, "done": False})
    print(f"Task '{task}' added successfully!")

def mark_done():
    show_tasks()
    try:
        task_num = int(input("\nEnter task number to mark as done: ")) - 1
        if 0 <= task_num < len(todo_list):
            todo_list[task_num]["done"] = True
            print(f"Task '{todo_list[task_num]['task']}' marked as done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("\nEnter task number to remove: ")) - 1
        if 0 <= task_num < len(todo_list):
            removed_task = todo_list.pop(task_num)
            print(f"Task '{removed_task['task']}' removed successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

while True:
    print("\nTo-Do List Options:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("bye")
        break
    else:
        print("Invalid choice! Please select a valid option.")

