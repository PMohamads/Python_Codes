import rotatescreen
import time
from tkinter import *
import pyautogui

screen= rotatescreen.get_primary_display()
for i in range(13):
    time.sleep(0.2)
    screen.rotate_to(i * 90 % 360)

window = Tk()
window.title("Hacklendiniz")
lbl2 = Label(window, text="you have been hacked", font=("Arial Bold", 35),bg = "red")
lbl2.grid(column=6, row=10)
window.geometry('900x800')
def tiklandi():
    pyautogui.moveTo(100, 100, duration=1,
                     tween=pyautogui.easeInOutQuad)
btn2 = Button(window, text="Tıkla",bg="orange", fg="red",width=10, height=10,command=tiklandi)

btn2.grid(column=1, row=3)

window.mainloop()
