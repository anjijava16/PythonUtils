import time;
def doubles(numbers):
	for n in numbers:
		time.sleep(1)
		print("Double:",2*n);
def squares(numbers):
	for n in numbers:
		time.sleep(1)
		print("Double:",n*n);
		

numbers=[1,2,3,4,5,6,7,8]
beginTime=time.time()
doubles(numbers)
squares(numbers)
endTime=time.time()

print("The total Time take",endTime-beginTime)