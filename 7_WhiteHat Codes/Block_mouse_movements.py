import threading

import mouse
import time

global executing
executing = True

def move_mouse():
    #until executing is False, move mouse to (1,0)
    global executing
    while executing:
        mouse.move(1,0, absolute=True, duration=0)

def stop_infinite_mouse_control():
    #stops infinite control of mouse after 10 seconds if program fails to execute
    global executing
    time.sleep(10)
    executing = False

threading.Thread(target=move_mouse).start()

threading.Thread(target=stop_infinite_mouse_control).start()
#^failsafe^
