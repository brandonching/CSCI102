#   Brandon Ching
#   ​CSCI 102 – Section C 
#   Week 1 - Part A 
#   References: ZyBooks 
#   Time: 10 minutes
import math
print("Input the first positive integer")
A = float(input("A>"))

print("Input the second positive integer")
B = float(input("B>"))

print("The square of the hypotenuse is:")
C = math.sqrt(A**2 + B**2)
print("OUTPUT", math.trunc(C**2))
