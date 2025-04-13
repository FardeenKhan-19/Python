'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
#GUI
import tkinter as tk
from tkinter import messagebox

def submit():
    name = name_entry.get()
    branch = branch_var.get()
    games = []
    
    if cricket_var.get():
        games.append("Cricket")
    if football_var.get():
        games.append("Football")
    if badminton_var.get():
        games.append("Badminton")

    output_text = f"Your name is {name}.\n{name} is from {branch} Department."
    
    if games:
        output_text += f"\n{name} is from {branch} Department and enjoys playing {', '.join(games)}."
    
    output_label.config(text=output_text)

# Create main window
root = tk.Tk()
root.title("College Admission Form")

# Student Name
tk.Label(root, text="Enter Student Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Branch Selection 
tk.Label(root, text="Select Your Branch:").grid(row=1, column=0, padx=10, pady=5)

branch_var = tk.StringVar(value="Computer Engineering")

tk.Radiobutton(root, text="Computer Engineering", variable=branch_var, value="Computer Engineering").grid(row=1, column=1, padx=10)
tk.Radiobutton(root, text="Information Technology", variable=branch_var, value="Information Technology").grid(row=1, column=2, padx=10)

# Favorite Games 
tk.Label(root, text="Select Favorite Games:").grid(row=2, column=0, padx=10, pady=5)

cricket_var = tk.BooleanVar()
football_var = tk.BooleanVar()
badminton_var = tk.BooleanVar()

tk.Checkbutton(root, text="Cricket", variable=cricket_var).grid(row=2, column=1, padx=10)
tk.Checkbutton(root, text="Football", variable=football_var).grid(row=2, column=2, padx=10)
tk.Checkbutton(root, text="Badminton", variable=badminton_var).grid(row=2, column=3, padx=10)

# Submit Button
tk.Button(root, text="Submit", command=submit).grid(row=3, column=1, pady=10)

# Output Label
output_label = tk.Label(root, text="", fg="blue", font=("Arial", 10, "bold"))
output_label.grid(row=4, column=0, columnspan=4, pady=10)

root.mainloop()
