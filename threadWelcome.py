import threading
from threading import *
#print("Current Thread info",threading.current_thread().getName())
#print("Current Thread info",threading.current_thread())
def display():
	print("==Display This codd will execute by ",current_thread().getName())
	
#print("This codd will execute by ",current_thread().getName())
t=Thread(target=display)	# MainThread creates Child Thread Object
t.start()# Main Thread starts ChildThread
t1=Thread(target=display)	# MainThread creates Child Thread Object
t1.start()# Main Thread starts ChildThread
print("Main Thread This codd will execute by ",current_thread().getName())
