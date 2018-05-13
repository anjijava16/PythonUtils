from threading import *;
class MyWithoutEx:
	def display(self):
		for i in range(10):
			print("child Thread-2",current_thread().getName())
			
obj=MyWithoutEx();
t1=Thread(target=obj.display)
t1.start()
t2=Thread(target=obj.display)
t2.start()
t3=Thread(target=obj.display)
t3.start()
t4=Thread(target=obj.display)
t4.start()

for i in range(10):
	print("main Thread-2",i);
	