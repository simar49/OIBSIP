import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, include_uppercase, include_numbers, include_special):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def show_password():
    try:
        length = int(length_entry.get())
        include_uppercase = uppercase_var.get()
        include_numbers = numbers_var.get()
        include_special = special_var.get()

        if length < 1:
            raise ValueError("Password length must be at least 1")

        password = generate_password(length, include_uppercase, include_numbers, include_special)
        messagebox.showinfo("Generated Password", f"Your password is: {password}")

    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))

# Setting up the GUI
root = tk.Tk()
root.title("GitHub Password Generator")

# Password length
tk.Label(root, text="Password Length:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

# Include uppercase letters
uppercase_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).grid(row=1, column=0, columnspan=2)

# Include numbers
numbers_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=2, column=0, columnspan=2)

# Include special characters
special_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).grid(row=3, column=0, columnspan=2)

# Generate button
tk.Button(root, text="Generate Password", command=show_password).grid(row=4, column=0, columnspan=2)

# Run the application
root.mainloop()