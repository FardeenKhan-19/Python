'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
import random

print("Number Guessing Game")

# Generating a random number between 1 and 100
random_number = random.randint(1, 100)

# Loop for user to guess the number
while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {random_number} correctly.")
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")
