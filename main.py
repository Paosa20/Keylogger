import pynput

from pynput.keyboard import Key, Listener

def on_press(key):
    pass

with Listener(on_press=on_press, on_release= on_release) as listener:
    listener.join()