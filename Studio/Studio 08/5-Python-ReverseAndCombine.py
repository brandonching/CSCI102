# Brandon Ching
# CSCI102 - Section C
# Python-ReverseAndCombine

inputs = input().split()
output_str = ''
print(inputs)
for i in inputs:
    output_str += i[::-1]
print(output_str)
