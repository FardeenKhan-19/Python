'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1)  

num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")
