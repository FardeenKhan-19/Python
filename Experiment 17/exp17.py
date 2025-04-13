'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
import re

def extract_data_from_file(file_path):

    phone_pattern = r"\b\d{10}\b"  

    email_pattern = r"[a-zA-Z0-9._%+-]+@eng\.rizvi\.edu\.in" 

    date_pattern = r"\b\d{2}/\d{2}/\d{4}\b"  

    with open(file_path, "r") as file:

        content = file.read()

    phone_numbers = re.findall(phone_pattern, content)

    emails = re.findall(email_pattern, content)

    dates = re.findall(date_pattern, content)


    print("Extracted Phone Numbers are :\n", phone_numbers)

    print("\nExtracted Email Addresses are :\n", emails)
    
    print("\nExtracted Dates are :\n", dates)

file_path = "information.txt"

extract_data_from_file(file_path)

