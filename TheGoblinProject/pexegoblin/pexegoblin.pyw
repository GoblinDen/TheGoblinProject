import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py*")])
        
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

def create_exe():
    python_file = entry.get()

    # Extract the directory path from the chosen Python file
    directory_path = os.path.dirname(python_file)

    if python_file == "*.pyw":
        subprocess.run(["pyinstaller", "--windowed", "--onefile", "-w", python_file], cwd=directory_path)
    else:
        # Run PyInstaller in the chosen directory
        subprocess.run(["pyinstaller", "--onefile", python_file], cwd=directory_path)

app = tk.Tk()
app.title("Python to Executable")

label = tk.Label(app, text="Select a Python file:")
label.pack(pady=10)

entry = tk.Entry(app, width=40)
entry.pack(pady=5)

browse_button = tk.Button(app, text="Browse", command=browse_file)
browse_button.pack(pady=5)

create_button = tk.Button(app, text="Create Executable", command=create_exe)
create_button.pack(pady=10)

app.mainloop()
