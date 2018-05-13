from threading import *
def display():
	for i in range(10):
		print("Child Method ==>",i);
		
t=Thread(target=display)
t.start()
print("===================== ")
for i in range(10):
	print("Main Thread ",i);
