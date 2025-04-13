'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
print("Even or Odd Number Checker")

# Taking numerical input from the user
num = int(input("Enter a number: "))

# Using conditional statements to check even or odd
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

# Loop to allow multiple checks
decision = "y"
while decision.lower() == "y":
    num = int(input("Enter another number: "))
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")
    decision = input("Do you want to check another number? (y/n): ")

print("Thank you for using the Even or Odd Number Checker!")
