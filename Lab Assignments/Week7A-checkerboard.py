# Brandon Ching
# CSCI 102 – Section C
# Week 7 - Lab A - Checkerboard
# References: N/A
# Time: 15 minutes

print("What is the length of the sides of the checkerboard? ")
length = int(input('LENGTH>'))
print("What are the strings with which to pattern it? ")
first = input('FIRST>')
second = input('SECOND>')
print(f"A checkerboard with side length {length}, first string is {first}, and second string is {second} is: ")
full_array = []
row = 1
for i in range(0,length):
    array = []
    for i in range(0,length):
        if row % 2 != 0:
            if i % 2 == 0:
                array.append(first)
            else:
                array.append(second)
        else:
            if i % 2 == 0:
                array.append(second)
            else:
                array.append(first)
            
    print(f"OUTPUT {array}")
    full_array.append(array)
    row += 1


print("And the 2D array representation is: ")
print(f"OUTPUT {full_array}")
