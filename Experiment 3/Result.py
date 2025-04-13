'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
print("Enter Student's Details and Marks:")

name = input("Enter Student's Name: ")
roll_number = input("Enter Roll Number: ")
subject1 = input("Enter Subject 1 Name: ")
marks1 = float(input(f"Enter {subject1} Marks: "))
subject2 = input("Enter Subject 2 Name: ")
marks2 = float(input(f"Enter {subject2} Marks: "))

total_marks = marks1 + marks2
average_marks = total_marks / 2
percentage = (total_marks / 200) * 100  # Assuming each subject is out of 100

print("\n==============================")
print("        REPORT CARD")
print("==============================")
print(f"Name         : {name}")
print(f"Roll Number  : {roll_number}")
print(f"{subject1} Marks : {marks1}")
print(f"{subject2} Marks : {marks2}")
print(f"Total Marks  : {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Percentage   : {percentage:.2f}%")
print("==============================\n")
