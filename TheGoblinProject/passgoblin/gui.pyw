import tkinter as tk
import functions as func

def start_Window():
    gchest = func.create_chest()
    func.create_user_table(gchest)
    start = tk.Tk()
    start.title("Start Menu")

    menu_text = tk.Label(start, text="Welcome to the Passgoblin!!!\nPlease Log in if you already are a registered user.\nIf not, please register as a new user.")
    menu_text.pack()
    
    register_button = tk.Button(start, text="Register", command=lambda: func.new_menu(start, register_Window), pady= 7, padx= 20)
    register_button.pack(pady= 15, padx= 20)

    login_button = tk.Button(start, text="Log in", command=lambda: func.new_menu(start, login_Window), pady= 7, padx= 20)
    login_button.pack(pady= 15, padx= 20)

    start.mainloop()
    
def register_Window():
    register = tk.Tk()
    register.title("Register")
    register.geometry('300x300')
    
    usrname_label = tk.Label(text="Choose a username:")
    usrname_label.pack()
    
    usrname_var = tk.StringVar()
    usrname_entry = tk.Entry(register, textvariable=usrname_var)
    usrname_entry.pack()
    
    checkusr_button = tk.Button(register, text="CHECK USERNAME", command=lambda: func.check_username(usrname_var, usrname_label, usrname_entry))
    checkusr_button.pack()
    
    usrpass_label = tk.Label(text="Create a password:")
    usrpass_label.pack()
    
    usrpass_var = tk.StringVar()
    usrpass_entry = tk.Entry(register, textvariable=usrpass_var, show='*')
    usrpass_entry.pack()
    
    passcheck_label = tk.Label(text="Verify password:")
    passcheck_label.pack()
    
    passcheck_var = tk.StringVar()
    passcheck_entry = tk.Entry(register, textvariable=passcheck_var, show='*')
    passcheck_entry.pack()
    
    register_button = tk.Button(register, text="Register", command=lambda: func.create_user(register, login_Window, usrname_var, usrpass_var, passcheck_var, usrpass_entry, passcheck_entry))
    register_button.pack(pady=5, padx=7)
    
    back_button = tk.Button(register, text="Back", command=lambda: func.new_menu(register, start_Window))
    back_button.pack(pady=10)
    
    register.mainloop()
    
    
def login_Window():
    gchest = func.create_chest()
    global usrname_var
      
    login = tk.Tk()
    login.title("Login")
    login.geometry('300x170')
    
    usrname_label = tk.Label(text="username:")
    usrname_label.pack()
    
    usrname_var = tk.StringVar()
    usrname_entry = tk.Entry(login, textvariable=usrname_var)
    usrname_entry.pack()
    
    usrpass_label = tk.Label(text="password")
    usrpass_label.pack()
    
    usrpass_var = tk.StringVar()
    usrpass_entry = tk.Entry(login, textvariable=usrpass_var, show='*')
    usrpass_entry.pack()
    
    usrlogin_button = tk.Button(login, text="Login", command=lambda: [func.login_user(usrname_var, usrname_entry, usrpass_var, usrpass_entry, login, pass_Window), func.create_table(gchest, usrname_var)])
    usrlogin_button.pack(pady=20)
    
    back_button = tk.Button(login, text="Back", command=lambda: func.new_menu(login, start_Window))
    back_button.pack()
    
    login.mainloop()
    
    
def pass_Window():
    gchest = func.create_chest()
    app = tk.Tk()
    app.title("Passgoblin")
    app.geometry("250x330")

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

    generate_button = tk.Button(app, text="Generate Password", command=lambda: func.generate_password(gchest, length_var, numbers_var, special_var, exclude_var, passname_var, usrname_var))
    generate_button.pack()

    searchpass_label = tk.Label(app, text="Find Password by Name:")
    searchpass_label.pack()

    searchpass_var = tk.StringVar()
    searchpass_entry = tk.Entry(app, textvariable=searchpass_var)
    searchpass_entry.pack()

    searchpass_button = tk.Button(app, text="Find Password", command=lambda: func.searchPassword(gchest, searchpass_var))
    searchpass_button.pack(pady=15)
    
    exit_button = tk.Button(app, text="Start Menu", command=lambda: func.new_menu(app, start_Window))
    exit_button.pack()

    app.mainloop()
    
start_Window()