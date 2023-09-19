import pyautogui
import win32api, win32con
import time
import keyboard
import tkinter as tk
from tkinter import filedialog

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
file_path = filedialog.askopenfilename(filetypes=[("Photo Files", "*.png *.jpg *.jpeg *.bmp")])

while keyboard.is_pressed('q') == False:
        try:
            x, y = pyautogui.locateCenterOnScreen(file_path, confidence=0.9)
            click(x,y)
        except:
            pass
