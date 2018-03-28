
https://www.nayuki.io/page/compact-hash-map-java

i)Function
   --  A group of statements
ii)Module : Group of Functions
iii)Package :
iv)Library :

==========================================================================================
Recurise Functions :
 A function that calls itself recurisve function
factorial(3)==> 3 * factorial(2)
            ==> 3 * 2 * factorial(1)
            ==> 

 factorial(n)==> n* factorial(n-1)
 
 Adv Of Recurisve Functions:
     1) Reduce the Length of the code and improve readbility
     2)Very complext problems  We can slove the towers of hanoi

  Factorial functions to find 
  
  def factorial(n):
  	  if n==0;
  	    result=1
  	  else :
  	   result=n* factorial(n-1)  
     
    print(factorial(0))
    
==========================================================================================    
  Anonymous Functions:
   Without Name ... nameless Functions
   
   Instance use (only one time usage)
   
   Importance of Anonymous FUnction: For instance usage
   
   Normal Function :
     def square(x):
         return n*n;
     
     lambda n:n*n       
     s=lambda n:n*n

     Syntax:
     lambda input:expression

     s= lambda x:x*x

     print(s(2))
     print(s(3))
     print(s(4))

s=lambda a,b:a+b
print("the sum of {} and {} is :{}".format(2,4,s(2,4)))     
          
s=lambda a,b: a if a>b else b;
print("the biggest of {} and {} is :{}".format(10,20,s(10,20)))     
print("the biggest of {} and {} is :{}".format(200,100,s(200,100)))     

==========================================================================================

filter()
map()
reduce()

This functions  always expecting other functions 

filter() ::==>>
-------------------------------
 => Filter is function name and sequece)

 filter(function,sequence)

 filter(function,list)

 filter(function,list/seq/set/tipple)

 def isEven(x):
 	 if x%2==0 :
 	 	 return True
 	  else:
 	    return False	 
                
l=[0,5,10,15,20,30]

filter(isEven,l)

print(type(filter(isEven,l)))
o/p: <class,'filter'>

l1=list(filter(iseven,1))

print(l1)

l1=list(filter(lambda x:x%2==0,1))
l2=list(filter(lambda x:x%2!=0,1))

==========================================================================================
map():
------------------

l=[0,5,10,20,30,40]
l=[0,10,20,40,60,80]

filter(function,Sequence); Function always either True OR False
map(function,sequence) : Function some operation (Busniness Operation).

def myDouble(x):
	return 2*x
l=[1,2,3,4,5]
l1=list(map(myDouble,l))
print(l1)



l=[1,2,3,4]
l1=list(map(lambda x:2*x,1))
l1=list(map(lambda x:x*x,1))


l1=[1,2,3,4]
l2=[10,20,30,40]
map(lambda x,y:x*y,11,12)
l3=list(map(lambda x,y:x*y,11,10))


lambda n:n*n
s=lambda n:n*n
print("The Square of {} is {} ".format(4,s(4)))
Pass function as argument to another function
filter(function,sequence)
map()

l=[0,5,10,15,20,25,30]

filter(f,l)
l1=list(filter(lambda n:n%2==0,1))
print(l1)

l2=list(filter(lambda n:n%2!=0,1))

l=[0,1,2,3,4,5]
l1=map(lambda n:n*n)

Compression Concept

Filter :
Input :10
Output : it may or maynot have 10 elements

map():
input :10
output :10


map(Function,sequence)

l1=[1,2,3,4]
l2=[2,3,4,5]

l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)


==========================================================================================

reduce():
 -------------------------------
 l=[10,20,30,40,50,60]
 reduce() function reduces by applicatying specify functions
 reduce(function,sequece)

 l=[10,20,30,40,50]
 result=reduce(lambda x,y:x+y,l)
 print(result)


from functools import *
from functools import reduce


i) filter()            
based on our boolean
condition

ii)map()         No.of Input and output values always same.

 iii) reduce()

 from functools import reduce
 print(reduce(add,[10,20,30,40])): ==>>ERROR

 print(sum([10,20,30,40]))

 Everything in Python is an Object
 int,bool,float

 def f1():
 	print("hello ")
 
 print(f1())
 print(id(f1()))	// Address of the Object


==========================================================================================
 Function Aliasing:

 def wish(name):
 	print("Good Morning:",name)

 greeting=wish
 print(id(wish))	
 print(id(greeting))
 wish("abc")
 greeting("sunny")


 // I am deleting 
 del wish
 wish("ABC") :// Error because alredy deleted

 greeting("DS")


def wish(name):
	print("Good morning...",name)

greeting=wish
sunny=greeting
========================================================================================== 
Nested Functions
    Function inside another Function is Nested Function

def outer():
	print("Outer Function Stared Here")
    def inner():
    	print("Inner Function execution")
    inner()
outer()    	


def f1():
	def inner(a,b):
		print("The Sum :",a+b)
		print("The avg is :",(a+b)/2)
	
	inner(10,20)
	inner(20,30)
	
	
	f1(): Working fine
	inner(): Won't work
	
		
 ============================
  def decor(func):
    def inner():
        x=func()
  
  
  l=[x*x for x in range(10)]
  #print(type(l)) #list
  l=(x*x for x in range(10))
  #print(type(l))  # generator
 
  l=[x*x for x in range(100000000000000000000000000000000)]       
  l=(x*x for x in range(100000000000000000000000000000000)) Generator
  
  
   yield person <<====>>       


'''
multiline comments

'''


==========================================================================================
