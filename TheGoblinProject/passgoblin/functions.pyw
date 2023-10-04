import tkinter as tk
from tkinter import messagebox
import random
import string
import os  # Import the os library
import sqlite3
from sqlite3 import Error
    
def create_chest():
    documents_folder = os.path.expanduser('C:\\Users\\Public\\Documents')  # Get the Documents folder path
    # Create the "goblin_chest" directory if it doesn't exist in Documents folder
    goblin_chest_path = os.path.join(documents_folder, "goblin_chest")
    if not os.path.exists(goblin_chest_path):
        os.mkdir(goblin_chest_path)
        
    return goblin_chest_path
        
def create_connection(needed_path):
    conn = None

    try:
        conn = sqlite3.connect(needed_path + '\\passwords.db')
        conn.set_trace_callback(print)
        return conn
    except Error as e:
        print(e)
    
    return conn

def create_table(chest, user):
    conn = create_connection(chest)
    tablename = user.get()
    try:
        c = conn.cursor()
        conn.execute(f"""
        CREATE TABLE IF NOT EXISTS {tablename} (
                     name text PRIMARY KEY,
                     password text NOT NULL
        );"""
                     )
    except Error as e:
        print(e)
    
    return c

def generate_password(chest, length, numbers, special, exclude, passname, user):
    
    length = int(length.get())
    use_numbers = numbers.get()
    use_special = special.get()
    exclude_chars = exclude.get()
    
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    for char in exclude_chars:
        characters = characters.replace(char, '')

    password = ''.join(random.choice(characters) for _ in range(length))
    
    passname = passname.get()

    conn = create_connection(chest)
    sql = conn.cursor()
    tablename = user.get()
    sql.execute(f"INSERT INTO '{tablename}' (name, password) VALUES (?, ?)", (passname, password))
    conn.commit()
    conn.close()
    
    # Save the password in the databank
    
    
    messagebox.showinfo("Password Generated", f"Password saved to the databank at {chest}.")
    
    
def searchPassword(chest, search):
    searchpass = search.get()

    conn = create_connection(chest)
    sql = conn.cursor()
    try:
        foundpassword = sql.execute(f"SELECT password FROM passwords WHERE name='{searchpass}'").fetchall()[0]
        messagebox.showinfo(f"Password Found", f"Your password is: {foundpassword}")
    except:
        messagebox.showinfo("Password not found", f"Please search for a exising password.")
        


def login_user(unv, une, upv, upe, window, nextwindow):
    given_name = unv.get()
    given_pass = upv.get()
    gchest = create_chest()
    conn = create_connection(gchest)
    sql = conn.cursor()
    try:
        sql.execute(f"SELECT * FROM users WHERE user='{given_name}' AND password='{given_pass}'").fetchall()[0]
        window.destroy()
        nextwindow()
    
    except:
        messagebox.showinfo("Login failed!", "The username or password that you provided isn't valid.\nPlease make sure to provide the correct values.")
        une.delete(0, 'end')
        upe.delete(0, 'end')
        redirect_button = tk.Button(window, text="Register", command='pass')
        redirect_button.pack()
    
    

def create_user(window, nextwindow, unv, upv, pcv, upe, pce):
    username = unv.get()
    userpassword = upv.get()
    passcheck = pcv.get()
    gchest = create_chest()
    conn = create_connection(gchest)
    sql = conn.cursor()
    
    if userpassword == passcheck:
        sql.execute("INSERT INTO users (user, password) VALUES (?, ?)", (username, userpassword))
        conn.commit()
        conn.close()
        messagebox.showinfo("User created", f"User {username} created! :)\nYour password is {userpassword}. Please remember it :)")
        redirect_button = tk.Button(window, text="Login", command=lambda: new_menu(window, nextwindow))
        redirect_button.pack()
        
    else:
        messagebox.showinfo("Password not matching", "Your password verification doesn't match with your password.")
        upe.delete(0, 'end')
        pce.delete(0, 'end')
    
def check_username(unv, unl, une):
    gchest = create_chest()
    conn = create_connection(gchest)
    sql = conn.cursor()
    username = unv.get()
    
    if username == '':
        unl.config(text="Choose a username: You can't leave the username empty.")
        une.delete(0, 'end')
    else:
        try:
            sql.execute(f"SELECT * FROM users WHERE user='{username}'").fetchall()[0]
            unl.config(text="Choose a username: username already in use :(")
            une.delete(0, 'end')
        except:
            unl.config(text="Choose a username: username available :)")


def create_user_table(chest):
    conn = create_connection(chest)
    try:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
                        user text PRIMARY KEY,
                        password text NOT NULL
        );"""
                        )
    except Error as e:
        print(e)

def new_menu(window, nextwindow):
    window.destroy()
    nextwindow()
