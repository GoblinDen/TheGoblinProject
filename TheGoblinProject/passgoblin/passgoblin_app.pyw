import tkinter as tk
from tkinter import messagebox
import random
import string
import os  # Import the os library
import sqlite3
from sqlite3 import Error

documents_folder = os.path.expanduser('C:\\Users\\Public\\Documents')  # Get the Documents folder path

# Create the "goblin_chest" directory if it doesn't exist in Documents folder
goblin_chest_path = os.path.join(documents_folder, "goblin_chest")
if not os.path.exists(goblin_chest_path):
    os.mkdir(goblin_chest_path)

def create_connection(needed_path):
    conn = None

    try:
        conn = sqlite3.connect(needed_path + '\\passwords.db')
        conn.set_trace_callback(print)
        return conn
    except Error as e:
        print(e)
    
    return conn

def create_table(conn):
    try:
        c = conn.cursor()
        conn.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
                     name text PRIMARY KEY,
                     password text NOT NULL
        );"""
                     )
    except Error as e:
        print(e)
    
    return c

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
    
    passname = passname_var.get()

    conn = create_connection(goblin_chest_path)
    sql = create_table(conn)
    sql.execute(f"INSERT INTO passwords (name, password) VALUES (?, ?)", (passname, password))
    conn.commit()
    conn.close()
    
    # Save the password in the databank
    
    
    messagebox.showinfo("Password Generated", f"Password saved to the databank at {goblin_chest_path}.")

def searchPassword():
    searchpass = searchpass_var.get()

    conn = create_connection(goblin_chest_path)
    sql = create_table(conn)
    try:
        foundpassword = sql.execute(f"SELECT password FROM passwords WHERE name='{searchpass}'").fetchall()[0][0]
        foundpassname_label = tk.Label(app, text=f"Password Found: {foundpassword}")
        foundpassname_label.pack()
    except Error as e:
        print(e)
    

def genWindow():
    # Create GUI
    app = tk.Tk()
    app.title("Passgoblin")

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

    passname_label = tk.Label(app, text="Password Name:")
    passname_label.pack()

    passname_var = tk.StringVar()
    passname_entry = tk.Entry(app, textvariable=passname_var)
    passname_entry.pack()

    generate_button = tk.Button(app, text="Generate Password", command=generate_password)
    generate_button.pack()

    searchpass_label = tk.Label(app, text="Find Password by Name:")
    searchpass_label.pack()

    searchpass_var = tk.StringVar()
    searchpass_entry = tk.Entry(app, textvariable=searchpass_var)
    searchpass_entry.pack()

    searchpass_button = tk.Button(app, text="Find Password", command=searchPassword)
    searchpass_button.pack()

    app.mainloop()

if __name__ == "__main__":
    genWindow()