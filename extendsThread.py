from threading import *;
class MyThread(Thread):
	   def run(self):
			for i in range(1,10):
				print("Child Thread-1",i)

				
t=MyThread();
t.start()
for i in range(1,10):
	print("Main Thread-1",i);