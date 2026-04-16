# python program to implement student result manager (credits: code with sagar youtube channel)
Student = {}
while True:
    print("-------STUDENT MANAGER APP-------")
    print("1. Add Student\n2. View Students\n3. Check Result\n4. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        Student[name] = marks
        print(f"{name} Added successfully!")
    
    elif choice == "2":
        if not Student:
            print("Student folder is empty")
        else:
            for name,marks in Student.items():
                print(name,":",marks)
    
    elif choice == "3":
        name = input("Enter student name: ")
        if name in Student:
            marks = Student[name]
            print(f"{marks} marks")
        else:
            print("Student not found")
    
    elif choice == "4":
        print('Exiting')
        break
    
    else:
        print("Invalid choice")


Output
-------STUDENT MANAGER APP-------
1. Add Student
2. View Students
3. Check Result
4. Exit
Enter choice: 2
Student folder is empty
-------STUDENT MANAGER APP-------
1. Add Student
2. View Students
3. Check Result
4. Exit
Enter choice: 3
Enter student name: hdff
Student not found
-------STUDENT MANAGER APP-------
1. Add Student
2. View Students
3. Check Result
4. Exit
Enter choice: 1
Enter student name: sam
Enter marks: 90
sam Added successfully!
-------STUDENT MANAGER APP-------
1. Add Student
2. View Students
3. Check Result
4. Exit
Enter choice: 3
Enter student name: sam
90 marks
-------STUDENT MANAGER APP-------
1. Add Student
2. View Students
3. Check Result
4. Exit
Enter choice: 1
Enter student name: max
Enter marks: 70
max Added successfully!
-------STUDENT MANAGER APP-------
1. Add Student
2. View Students
3. Check Result
4. Exit
Enter choice: 2
sam : 90
max : 70
-------STUDENT MANAGER APP-------
1. Add Student
2. View Students
3. Check Result
4. Exit
Enter choice: 4
Exiting

=== Code Execution Successful ===
