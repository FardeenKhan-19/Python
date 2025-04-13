'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
print("Factorial Calculator")

num = int(input("Enter a number: "))

factorial = 1
for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")

print("Thank you for using the Factorial Calculator!")
