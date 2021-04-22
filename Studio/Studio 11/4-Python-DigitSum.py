# Brandon Ching
# CSCI 102 Section C
# Python-DigitSum

def digit_sum(number):
    sum = 0
    for char in str(number):
        if char.isnumeric():
            sum += int(char)
    if str(number)[0] == '-':
        sum -= int(str(number)[1])*2
    return sum
