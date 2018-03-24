 Function => A Group of Statments
 def wish(name):
   print("Good Morning",name)

wish("Sunny")

def insertEmployee(name,age,empno,esal,eaddr):
	insert into employee table
	insert into 

for e in employees:
	insertEmployee(data)

List
class List
 def append():

====================================================
 Parameters
 
 i)positional
 ii)keywords
 iii)default
 iv)var



 def wish():
 	print("Welcome")

 print(wish())	
 
 
 def calc(a,b):
 	sum=a+b;
 	sub=a-b;
 	mul=a*b;
 	div=a/b;
 	return sum.sub,mul,div

t=calc(100,50)
for x in t :
	print(x)


def calc(a,b):

t=calc(100,50);//Positional arguments

# Keywords Arguments Order is not import but no of arguments must match	
t=calc(a=100,b=50)// KeyWords arguments
t=calc(b=50,a=100) //KeyWords Arguments

def calc(a,b):

calc(100,b=50)
calc(b=50,100); Keywords (After keywords cant take postitonal arguments)
Note: First take positional arguments then keywords arguments

3: defualt Arguments
=============================================
// Default arguments should be last 
def wish(name="Guest",msg): Wrong

def wish(msg,name="Guest"):pass



4: var arguments(Variable Length Arguments)
==================================================	
def sum(a,b):
	print(a+b)

sum(10,20)

sum(10,20,30):

def f1(*n):
	print("Var-arg Function")
   for x in n:
   	print(x)

f1(10)	
f1(10,20)
f1(10,20,30)
f1(10,20,30,40)


WAP to print sum of given numbers

def sum(*n):
	result=0
	for x in n:
		result=result+x
  print("The Sum : ",result)		
      
def name(name,*n):
	result=0
	for x in n:
		result=result+x;
	print ("The Sum ",name,":",result)

sum("Durga")
sum("Ravi",10)
sum("Ravi1",10,20)

Note: def sum(*n,name):
    Var arg parameters should be last parameters. in java

   sum(name="Ds")
   sum(10,name="RS")
   sum(10,20,name="PS")
    

KeyWord Varible length Aruments (**kwargs)

def display(**kwargs):
 print(type(kwargs))
 print("Record Information ")
 for k,v in kwargs.items():
 	print(k,"......",v)

display(name="Durga",marks=100,age=48,GF="Sunny")
display(name="Durga",wife1="nna",wife2="abc")

================================================================

# Default arguments
def f1(arg1,arg2,arg3=4,arg4=8):
	print(arg1,arg2,arg3,arg4)

f(3,2) ;

f(10,20,30,1,1,2,4)
f(1,2,arg4=100)

f(arg3=10,arg4=40,20,30):Error
f(4,5,arg2=6): Error arg2 have mutliple values

f(4,5,arg3=5,arg5=6)


=================================================

Types of Arguments in Python :

i)Postional

ii)Keyword arguments

iii)Default

iv)Variable Length Arguments
               *n
               **n ==> Variable Length Keyword arguments

  
  

  Function::==>
  Modules
  Package
  Libray

def add(x,y):
	 print(a+b);

def add(a,b):
	print(a+b);

above Function saving as calc.py

A group of function saved into file : Module

Group of Modules called as Package

Group of Packages Called Libray
====================================
Types of Variables

i)Global Variables
ii)Local Variables


Global Functions

Note:Error
def f1():
	a=10
	print("f1:",a)
def f2():
	print("f2:",a)

f1()
f2()


a=10
def f1():
	a=777
	print("f1:",a)
def f2():
	print("f2:",a)



a=10
def f1():
	global a
	a=777
	print("f1:",a)

def f2():
    print("f2:",a)	

  
 Gloabl Variables:outside of the function
 
 Global Keyword:
 1: To Make Global avaiable to the function so that we can perfomr our requir
 modification.
 2: To Declare global variables inside function


 
 def f1():
    global a
    a=888
    print("f1:",a)
  
 def f2():
     print("f2:",a)
   
     
   
   def f1():
      global a
      a=888
      print("F1,",a)
      
   def f2():
     global a
     a=999
     print("f2:",a)
     
     
     
    a=10 #Global
    def f1():
      a=20
      print(a)
      
    f1()
    
    globals()  # Gloabl Method
    

    How to access Global variables inside the function.
    a=10
    def f1():
       a=20
       print(a)
       print(globals()['a'])         
   f1()
    
       
   d={'a':10,'b':20,'c':30}
   d['a']
   
   
   
   def f1():
      a=10
      global a
      a=20
      print(a)
      
    f1()://ERROR,because not allowed next time      


	




  

               
   





	
 
 
  	

