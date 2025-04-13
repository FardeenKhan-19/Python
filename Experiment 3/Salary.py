'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
import math

# Prompt user for basic salary
basic_salary = float(input("Enter the Basic Salary (BS): "))

# Calculate allowances using inbuilt mathematical functions
dearness_allowance = math.ceil(0.70 * basic_salary)
travel_allowance = math.ceil(0.30 * basic_salary)
house_rent_allowance = math.ceil(0.10 * basic_salary)

# Calculate gross salary
gross_salary = basic_salary + dearness_allowance + travel_allowance + house_rent_allowance

# Display the result
print("\n==============================")
print("        SALARY DETAILS")
print("==============================")
print(f"Basic Salary (BS)         : {basic_salary}")
print(f"Dearness Allowance (DA)   : {dearness_allowance}")
print(f"Travel Allowance (TA)     : {travel_allowance}")
print(f"House Rent Allowance (HRA): {house_rent_allowance}")
print(f"Gross Salary              : {gross_salary}")
print("==============================\n")

