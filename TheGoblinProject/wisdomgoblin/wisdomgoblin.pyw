import tkinter as tk
from tkinter import filedialog
import os

documents_folder = os.path.expanduser('C:\\Users\\%USERNAME%\\Documents')

goblin_brain_path = os.path.join(documents_folder, "goblin_brain")
if not os.path.exists(goblin_brain_path):
    os.mkdir(goblin_brain_path)

def open_file():
    filename = entry.get()
    if filename:
        file_path = os.path.join(goblin_brain_path, filename + ".txt")
        if os.path.exists(file_path):
            os.system("notepad " + file_path)
        else:
            result_label.config(text="File not found!")

app = tk.Tk()
app.title("Wise Goblin")

label = tk.Label(app, text="Enter a file name (without extension):")
label.pack(pady=10)

entry = tk.Entry(app)
entry.pack(pady=5)

open_button = tk.Button(app, text="Open", command=open_file)
open_button.pack(pady=5)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)

app.mainloop()
