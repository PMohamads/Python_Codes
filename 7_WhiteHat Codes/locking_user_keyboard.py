import os
import time
import pyautogui
from threading import Thread
from keyboard import block_key

def blockMouseAndKeys(timeout=30):
    global blocking
    blockStartTime = time.time()
    pyautogui.FAILSAFE = False
    blocking = True
    try: float(timeout)
    except: timeout = 30

    def blockKeys(timeout):
        global blocking
        while blocking:
            if timeout:
                if time.time()-blockStartTime > timeout:
                    print(f'Keyboard block timed out after {timeout}s.')
                    return
            for i in range(150):
                try: block_key(i)
                except: pass
    def blockMouse(timeout):
        global blocking
        while blocking:
            def resetMouse(): pyautogui.moveTo(5,5)
            Thread(target=resetMouse).start()
            if timeout:
                if time.time()-blockStartTime > timeout:
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


blockMouseAndKeys(timeout=30)
os.startfile('https://www.youtube.com/watch?v=X-TkrWpO75k&list=RDxOlRnA1Xrds&index=27')