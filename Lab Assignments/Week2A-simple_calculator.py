# Brandon Ching
# CSCI102 - Section C
# Week 2 - Lab A - Simple Calcualtor
# Refrences: N/A
# Time: 15min

operand_one = 0.0
operand_two = 0.0
sum = 0.0
diffrence = 0.0
quotient = 0.0
remainder = 0.0

print("Input the first operand")
operand_one = float(input("FIRST>"))
print("Input the second operand")
operand_two = float(input("SECOND>"))

sum = operand_one + operand_two
diffrence = operand_one - operand_two
quotient = operand_one // operand_two
remainder = operand_one % operand_two

print(
    f"The sum of {operand_one} and {operand_two} is {sum:.1f}\n"
    f"The diffrence of {operand_one} and {operand_two} is {diffrence:.1f}\n"
    f"The quotient of {operand_one} and {operand_two} is {quotient:.0f}\n"
    f"The remainder of {operand_one} and {operand_two} is {remainder:.2f}"
    )
