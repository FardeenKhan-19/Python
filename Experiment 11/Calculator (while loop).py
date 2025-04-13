'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def mod(a, b):
    return a % b

while True:

    print("\n\t\t\tSimple Calculator")
    print("\n1. Addition")
    print("2. Subtraction") 
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")


    choice = (input("\nEnter your choice : 1/2/3/4/5/6 : "))
    if choice == '1':
        a = float(input("\nEnter first number : "))
        b = float(input("\nEnter second number : "))
        print(f"Addition of {a} and {b} is : ", add(a, b))

    elif choice == '2':
        a = float(input("\nEnter first number : "))
        b = float(input("\nEnter first number : "))
        print(f"Subtraction of {a} and {b} is : ", sub(a, b))

    elif choice == '3':
        a = float(input("\nEnter first number : "))
        b = float(input("\nEnter second number : "))
        print(f"Multiplication of {a} and {b} is : ", mul(a, b))

    elif choice == '4': 
        a = float(input("\nEnter first number : "))
        b = float(input("\nEnter second number : "))
        print(f"Division of {a} and {b} is : ", div(a, b))

    elif choice == '5':
        a = float(input("\nEnter first number : "))
        b = float(input("\nEnter second number : "))
        print(f"Division of {a} and {b} is : ", mod(a, b))

    elif choice == '6':
        print("\nExiting the calculator, Thank you!!!")
        break

    else:
        print("\nInvalid choice, Please try again!!!\n")  

   

