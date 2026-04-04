from numpy import *
a = array([1,2,4,5,6.5,'a'])# numpy is a heterogenius arry so it can acces any typecode
for x in a:
    print(x,end=" ")
print("\n")

# LINSPACE function
from numpy import *
a = linspace(10,20,4) # start,stop,how many number you want

for i in a:
    print(i,end=" ")
print("\n")


# ARANGE function
from numpy import *
a = arange(10,20,2) # start,stop,jump
for i in a:
    print(i,end=" ")
print("\n")


# ZEROS function
from numpy import *
a = zeros(10) # start,stop,jump
for i in a:
    print(i,end=" ")
print("\n")

from numpy import *
a = ones(10) # start,stop,jump
for i in a:
    print(i,end=" ")
print("\n")


#  FULL() function
from numpy import *
a = full(10,5)# create array of length 10, filled with 5
for i in a:
    print(i,end=" ")