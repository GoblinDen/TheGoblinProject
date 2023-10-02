import tkinter as tk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import passgoblin_app as pss
import register as rr

passcon = pss.create_connection(pss.goblin_chest_path)

def users_table(conn):
    try:
        c = conn.cursor()
        conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
                     user text PRIMARY KEY,
                     password text NOT NULL
        );"""
                     )
    except Error as e:
        print(e)
    
    return c

def register_user():
    app.destroy()
    rr.register_Window()
    








def guiWindow():
    global app
    app = tk.Tk()
    app.title("Start Menu")

    menu_text = tk.Label(app, text="Welcome to the Passgoblin!!!\nPlease Log in if you already are a registered user.\nIf not, please register as a new user.")
    menu_text.pack()
    
    register_button = tk.Button(app, text="Register", command=register_user, pady= 7, padx= 20)
    register_button.pack(pady= 15, padx= 20)

    login_button = tk.Button(app, text="Log in", pady= 7, padx= 20)
    login_button.pack(pady= 15, padx= 20)

    app.mainloop()

if __name__ == '__main__':
    guiWindow()