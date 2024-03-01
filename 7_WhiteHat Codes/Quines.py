import random
from tkinter import *
def tiklandi():
        print(" Butona tıklandı ")
while True:
    window = Tk()
    x = random.randint(0, 999)
    y = random.randint(0, 999)
    window.geometry('235x200+{0}+{1}'.format(x, y))
    for i in range(10):
        window.title("you are an idiot")
        lbl = Label(window, text="Merhaba")
        lbl1 = Label(window, text="you have been hacked", font=("Arial Bold", 15), bg='red', fg='yellow')
        lbl1.grid(column=1, row=i)
    btn2 = Button(window, text="I'M SORRY", bg="orange", fg="red", width=20, height=10, command=tiklandi)
    btn2.grid(column=5, row=2)
    window.geometry('500x250')
    window.mainloop()