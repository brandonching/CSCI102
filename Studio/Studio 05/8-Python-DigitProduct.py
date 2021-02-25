# Brandon Ching
# CSCI102 - Section C
# Python-DigitProduct
number = str(input())
final_number = 0

while not (1 <= final_number <= 9):
    final_number = 0
    for x in number:
        if x != '0':
            if final_number == 0:
                final_number = int(x)
            else:
                final_number = final_number * int(x)
    number = str(final_number)
print(final_number)
