'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
print("Simple Interest Calculator")

# Taking user input
principal = float(input("Enter the Principal Amount: "))
rate = float(input("Enter the Rate of Interest (in %): "))
time = float(input("Enter the Time Period (in years): "))

# Calculating Simple Interest
simple_interest = (principal * rate * time) / 100

# Displaying the result
print("\n==============================")
print("        INTEREST DETAILS")
print("==============================")
print(f"Principal Amount : {principal}")
print(f"Rate of Interest : {rate}%")
print(f"Time Period      : {time} years")
print(f"Simple Interest  : {simple_interest}")
print("==============================\n")
