# Brandon Ching
# CSCI 102 – Section C
# Week 5 - Lab B - Tally for Kids 
# References: N/A 
# Time: 25 minutes

print("Enter values to add. Enter quit when done. ")
sum = 0
count = 0
while "true":
    number = input("NUMBER>")
    if number == 'quit':
        break
    else:
        sum += int(number)
        count += 1
print(f"The addition of the {count} numbers entered is:\n"
      f" OUTPUT {count} numbers\n"
      f" OUTPUT {sum} total")


