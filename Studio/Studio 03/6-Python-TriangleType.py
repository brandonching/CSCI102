# Brandon Ching
# CSCI102 - Section C
# Python-TriangleType

x = int(input())
y = int(input())
z = int(input())

if (x+y)<=z or (x+z)<=y or (y+z)<=x:
    print("Does not exist")
elif x==y and x==z:
    print("Equilateral triangle")
elif x==y or x==z or z==y:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
