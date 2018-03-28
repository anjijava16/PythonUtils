

list =[x*x for x in range(10)]
for x in list:
    print(x)
========================================
list =(x*x for x in range(10000000000))
for x in list:
    print(x)
================================
import random
import time

=========================
To generate First n numbers

def firstn(num):
    n=1;
    while n<=num:
     yield n
     n=n+1
values =firstn(nu
for x in values :
 print(x)
=================================================
0,1,1,2,3,5,8

def fib():
   a,b=0,1
   while True:
   	  yield a
   	  a,b=b,a+b

  f=fib()
  for x in f:
       print(x) 	  

for x in f:
     if x>100:
     	break
       print(x) 	  


========================================

Adv of Generator Functions
1.Very easy to use
2.Memory Utilization improved
******3.Perfomance will be improved

4.Read data from crores of files and store in a DS
5.Web Scrping and crawling

===============================================================

*********** Module ***************
Group of functions & variables as Module
''' abc.py '''
--------------------------
x=888
y=999
def add(a,b):
	print("The Calcutaor to the World",(a+b)

def product(a,b):
	 print("The Product :",(a*b))
   

import abc;

print(abc.x)
print(abc.y)

abc.add(10,20)
abc.product(10,20)


Modules:
 Adv of Modules
 i)Maintaible
 ii)Code Resulability
 

 import module
 ''' Accessing variables and methods '''
 modulename.x
 modulename.add(10,20)

import module as am
print(dm.x) //Working
print(abc.y); //Not Working
''' Once created alias name must be use alias name other wise it is error'''


==========================================
How to use  
import abc

from import :
===============
from abc import x,add

print(x)
print(add(10,20))

//Note: Can't acces y and product methods


(OR)

from abc import *;
print(x)
print(add(10,20))
print(y)
print(product(10,20))

(OR)
We can create alias names for memeber also

from abc import x as a,y as b,add as c,product as d
print(a)
print(b)
print()

Various possibilites of import

import modulename
import modulename1, modulename2,modulename3
import modulename1 as m1, modulename2 as m2,

from module import member
from abc import x
from module import member1,member2,member3
from module import member1 as x
from module import *


import abc ,random as a,b


