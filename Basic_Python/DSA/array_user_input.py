from array import *

a = array('i',[])

b = (int(input("Enter how many  numbers :")))

for i in range(0, b):
    a.append(int(input("Enter next number :")))

for x in a:
    print(x,end=" ")

from array import *
arr = array('i',[1,2,34,23,45,43,67,32])

a = arr.index(43)
print(a)

# Take both the element and index element to print the elements and the index number from user
from array import *
arr = array('i',[])

b = int(input("Enter how many numbers :"))

for i in range(0,b):
    arr.append(int(input("Enter next number :")))

for x in arr:
    print(x,end=" ")
print("\n")


m = (int(input("Enter any one number of your given element :")))

if m in arr:
    print("index of your number is : ",arr.index(m))
else:
    print("The number you have given is not in the array..")