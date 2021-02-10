# Brandon Ching
#​ CSCI 102 – Section C
# Week 3 - Lab B - Enhanced Calcuator
# References: N/A
# Time: 10 minutes

operand_one = 0.0
operand_two = 0.0
sum = 0.0
diffrence = 0.0
quotient = 0.0
remainder = 0.0

print("Welcome to our Enhanced Calculator!")
print("Input the first operand.")
operand_one = float(input('FIRST>'))
print("Input the second operand.")
operand_two = float(input('SECOND>'))

print(
    f"Choose one of the following operations:\n"
    f"1 - addition\n"
    f"2 - subtraction\n"
    f"3 - multiplication\n"
    f"4 - division\n"
    )

operation = int(input("OPERATION>"))
sum = operand_one + operand_two
diffrence = operand_one - operand_two
product = operand_one * operand_two
quotient = operand_one // operand_two
remainder = operand_one % operand_two


if operation == 1:
    print(f"The result of the addition is: {sum:.6f}")
    print(f"OUTPUT {sum:.6f}")
elif operation == 2:
    print(f"The result of the subtraction is: {diffrence:.6f}")
    print(f"OUTPUT {diffrence:.6f}")
elif operation == 3:
    print(f"The result of the multiplication is: {product:.6f}")
    print(f"OUTPUT {product:.6f}")
elif operation == 4:
    print(f"The result of the division is: {quotient:.0f} (quotient) and {remainder:.0f} (remainder)")
    print(f"OUTPUT {quotient:.0f}")
    print(f"OUTPUT {remainder:.0f}")
else:
    print("ERROR")
print("Thank you for using our calculator.")
