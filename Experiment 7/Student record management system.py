'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
print("Student Record Management System")

students = {}

while True:
    print("\nOptions:")
    print("1. Add Student Record")
    print("2. Update Student Record")
    print("3. View All Records")
    print("4. Remove Student Record")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        grade = input("Enter Grade: ")
        attendance = input("Enter Attendance Percentage: ")
        students[roll_no] = {"Name": name, "Grade": grade, "Attendance": attendance}
        print("Student record added successfully!")
    
    elif choice == '2':
        roll_no = input("Enter Roll Number to update: ")
        if roll_no in students:
            print("What do you want to update?")
            print("1. Name")
            print("2. Grade")
            print("3. Attendance")
            update_choice = input("Enter choice: ")
            if update_choice == '1':
                students[roll_no]['Name'] = input("Enter new Name: ")
            elif update_choice == '2':
                students[roll_no]['Grade'] = input("Enter new Grade: ")
            elif update_choice == '3':
                students[roll_no]['Attendance'] = input("Enter new Attendance Percentage: ")
            print("Student record updated successfully!")
        else:
            print("Student record not found!")
    
    elif choice == '3':
        print("\nStudent Records:")
        for roll_no, details in students.items():
            print(f"Roll No: {roll_no}, Name: {details['Name']}, Grade: {details['Grade']}, Attendance: {details['Attendance']}%")
    
    elif choice == '4':
        roll_no = input("Enter Roll Number to remove: ")
        if roll_no in students:
            del students[roll_no]
            print("Student record removed successfully!")
        else:
            print("Student record not found!")
    
    elif choice == '5':
        print("Exiting program...")
        break
    
    else:
        print("Invalid choice! Please select a valid option.")