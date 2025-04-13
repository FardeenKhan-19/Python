'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
print("Voter Eligibility Checker")

try:
    name = input("Enter your name: ")
    if not name.isalpha():
        raise ValueError("Invalid name! Please enter alphabetic characters only.")
    
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    
    if age >= 18:
        print(f"Hello {name}, you are eligible to vote!")
    else:
        print(f"Sorry {name}, you are not eligible to vote. You must be at least 18 years old.")

except ValueError as e:
    print(f"Error: {e}")
