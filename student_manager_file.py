# similar to student result manager file but added file handling concept

Students = {}

while True:
    print("\n------------STUDENT MANAGER APP--------------")
    print("1.Add Student\n2. View Students\n3. Check Marks\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        Students[name] = marks

        with open("student_list.txt","a") as file:
            file.write(f"{name}:{marks} marks\n")
        print("Saved!")

    elif choice == "2":
        if not Students:
            print("No data!")
        else:
            for name, marks in Students.items():
                print(f"{name}:{marks} marks")

    elif choice == "3":
        name = input("Enter student name: ")
        if name in Students:
            marks = Students[name]
            print(f"{name}:{marks} marks")
        else:
            print("Student not found")
        
    elif choice == "4":
        print("Exiting")
        break

    else:
        print("Invalid choice")
