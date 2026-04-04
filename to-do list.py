tasks = []
while True:
    print("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter the task")
        tasks.append(task)
    elif choice == "2":
        if not tasks:
            print("No tasks to view")
        else:
            for i in tasks:
                print(i)
    elif choice == '3':
        if not tasks:
            print("no task to remove")
        else:
            num = int(input("enter the number of task to be removed"))
            tasks.pop(num-1)
    elif choice == '4':
        print("exiting and exited")
        break
    else:
        print("Invalid choice")
