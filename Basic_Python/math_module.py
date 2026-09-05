import math

# # WAP to calculate the LCM of two numbers
# A = int(input("Enter first number : "))
# B = int(input("Enter second number : "))
# C = int(input("Enter third number : "))
# D = int(input("Enter foourth number : "))
# E = int(input("Enter fifth number : "))
# F = int(input("Enter sixth number : "))

# result = math.lcm(A,B,C,D,E,F)
# print("LCM is :",result)



# WAP to calculate the distance between two coordinates 
x1 = float(input("X1 :"))
x2 = float(input("X2 :"))
y1 = float(input("Y1 :"))
y2 = float(input("Y2 :"))

Distance = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
print(f"Distance is : {Distance}")