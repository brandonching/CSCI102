# Brandon Ching
# CSCI102 - Section C
# Python-NewFizzBuzz

final_number = int(input())
divisor_one = int(input())
divisor_two = int(input())
word_one = input()
word_two = input()

index = 1
while index <= final_number:
    if (index % divisor_one == 0) and (index % divisor_two != 0):
        print(word_one)
    elif (index % divisor_two == 0) and (index % divisor_one != 0):
        print(word_two)
    elif (index % divisor_one == 0) and (index % divisor_two == 0):
        print(word_one + word_two)
    else:
        print(index)
    index += 1
