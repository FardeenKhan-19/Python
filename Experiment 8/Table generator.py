'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
print("Multiplication Table Generator")

num = int(input("Enter a number: "))

print(f"Multiplication Table for {num}:")
for i in range(1, 13):
    print(f"{num} x {i} = {num * i}")

print("Thank you for using the Multiplication Table Generator!")
