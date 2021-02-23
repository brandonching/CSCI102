# Brandon Ching
# ​CSCI 102 – Section C
# Week 5 - Lab A - Stuck in a Time Loop
# References: N/A
# Time: 2 minutes

print("Enter the wizard's magic number. ")
n = int(input("N>"))
i = 1
if 1 <= n <=100:
    while i <= n:
        print(f"OUTPUT {i} Abracadabra")
        i += 1
else:
    print("Error: input must be between 1 and 100!")
    print("OUTPUT ERROR")
    
