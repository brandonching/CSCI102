# Brandon Ching
# CSCI 102 – Section C
# Week 6 - Lab A - List of Multiples
# References: N/A
# Time: 5 minutes

print("Enter the number to create multiples for. ")
number = int(input('NUMBER>'))
print("Enter the size of the list. ")
size = int(input('SIZE>'))

multiple_list = [number]

for i in range(1,size):
    multiple_list.append(multiple_list[i-1] + number)
    
print("Your list of multiples is as follows: ")
print(f"OUTPUT {multiple_list}")
