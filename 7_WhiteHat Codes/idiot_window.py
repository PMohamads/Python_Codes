from tkinter import *
import tkinter as tk
import threading
import time
import random
import sys
def disable_event():
    pass
def move_window():
    root = Tk()
    root.title('you are an idiot')
    root.attributes('-toolwindow', True)
    x = random.randint(0, 999)
    y = random.randint(0, 999)
    root.resizable(height=None,width=None)
    root.geometry('235x200+{0}+{1}'.format(x, y))
    root.configure(background='white')
    Label(root, text='malwarent', fg='white', font=("Terminal",35))
    Label(root, text='You are an idiot', fg='red', font=('Terminal',35))
    root.protocol("WM_DELETE_WINDOW", disable_event)
    root.mainloop()
if __name__== "__main__":
    for i in range(5) :
        thread = threading.Thread(target=move_window)
        thread.start()
