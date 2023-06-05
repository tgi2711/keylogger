import pynput 

from pynput.keyboard import Key,Listener

def on_press(key):
	print(f"{key}    pressed")

def on_release(key):
	pass
	if (key == Key.esc):
		return False





ddddd
with Listener(on_press=on_press,on_release=on_release) as listener:
	print('here')
	listener.join()