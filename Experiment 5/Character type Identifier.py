'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
print("Character Type Checker")

char = input("Enter a single character: ")

if char.isdigit():
    print("The input is a digit.")
elif char.islower():
    print("The input is a lowercase letter.")
elif char.isupper():
    print("The input is an uppercase letter.")
elif not char.isalnum():
    print("The input is a special character.")
else:
    print("Invalid input! Please enter a single character.")
