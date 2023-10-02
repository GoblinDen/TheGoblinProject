import tkinter as tk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import start_page as sp


def create_user():
    username = usrname_var.get()

def register_Window():
    app = tk.Tk()
    app.title("Register")
    
    usrname_label = tk.Label(text="Choose a username:")
    usrname_label.pack()
    
    usrname_var = tk.StringVar()
    usrname_entry = tk.Entry(app, textvariable=usrname_var)
    usrname_entry.pack()
    
    app.mainloop()