'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
print("Enter two numbers:")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num2 != 0:
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    modulus = num1 % num2
    
    print("\n==============================")
    print("     ARITHMETIC OPERATIONS")
    print("==============================")
    print(f"Addition       : {addition}")
    print(f"Subtraction    : {subtraction}")
    print(f"Multiplication : {multiplication}")
    print(f"Division       : {division:.2f}")
    print(f"Modulus        : {modulus}")
    print("==============================\n")
else:
    print("Division and modulus operations cannot be performed as the second number is zero.")

