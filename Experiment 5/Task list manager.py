'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
print("Task List Manager")

tasks = [] 

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. View Tasks")
    print("5. Sort Tasks")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter the task to add: ")
        tasks.append(task)
        print("Task added successfully!")
    
    elif choice == '2':
        task = input("Enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found!")
    
    elif choice == '3':
        old_task = input("Enter the task to update: ")
        if old_task in tasks:
            new_task = input("Enter the new task: ")
            index = tasks.index(old_task)
            tasks[index] = new_task
            print("Task updated successfully!")
        else:
            print("Task not found!")
    
    elif choice == '4':
        print("\nCurrent Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    
    elif choice == '5':
        tasks.sort()
        print("Tasks sorted successfully!")
    
    elif choice == '6':
        print("Exiting program...")
        break
    
    else:
        print("Invalid choice! Please select a valid option.")
