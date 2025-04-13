'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
import re

def validate_phone_number(phone_number):

    phone_pattern = r"^\d{10}$"
    if re.match(phone_pattern, phone_number):
        return True
    else:
        return False

def validate_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@eng\.rizvi\.edu\.in$"
    if re.match(email_pattern, email):
        return True
    else:
        return False

phone_number = input("Enter your phone number (10 digits): ")

email = input("Enter your email ID (name@eng.rizvi.edu.in): ")

if validate_phone_number(phone_number):

    print("Phone number is valid.")

else:
    print("Phone number is invalid. It should be a 10-digit number.")

if validate_email(email):

    print("Email ID is valid.")

else:
        print("Email ID is invalid.")



