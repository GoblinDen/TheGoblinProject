import tkinter as tk
from tkinter import messagebox
import random
import string
import os  # Import the os library

def generate_password():
    length = int(length_var.get())
    use_numbers = numbers_var.get()
    use_special = special_var.get()
    exclude_chars = exclude_var.get()
    
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    for char in exclude_chars:
        characters = characters.replace(char, '')

    password = ''.join(random.choice(characters) for _ in range(length))
    
    filename = filename_var.get()
    
    documents_folder = os.path.expanduser('D:\Joyce\Documents')  # Get the Documents folder path
    
    # Create the "goblin_chest" directory if it doesn't exist in Documents folder
    goblin_chest_path = os.path.join(documents_folder, "goblin_chest")
    if not os.path.exists(goblin_chest_path):
        os.mkdir(goblin_chest_path)
    
    # Save the password in the "goblin_chest" directory
    with open(os.path.join(goblin_chest_path, f'{filename}.txt'), 'w') as file:
        file.write(password)
    
    messagebox.showinfo("Password Generated", f"Password saved to {goblin_chest_path}/{filename}.txt")

# Create GUI
app = tk.Tk()
app.title("Random Password Generator")

length_label = tk.Label(app, text="Password Length:")
length_label.pack()

length_var = tk.StringVar()
length_entry = tk.Entry(app, textvariable=length_var)
length_entry.pack()

numbers_var = tk.BooleanVar()
numbers_check = tk.Checkbutton(app, text="Include Numbers", variable=numbers_var)
numbers_check.pack()

special_var = tk.BooleanVar()
special_check = tk.Checkbutton(app, text="Include Special Characters", variable=special_var)
special_check.pack()

exclude_label = tk.Label(app, text="Exclude Characters:")
exclude_label.pack()

exclude_var = tk.StringVar()
exclude_entry = tk.Entry(app, textvariable=exclude_var)
exclude_entry.pack()

filename_label = tk.Label(app, text="File Name:")
filename_label.pack()

filename_var = tk.StringVar()
filename_entry = tk.Entry(app, textvariable=filename_var)
filename_entry.pack()

generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack()

app.mainloop()
