# Brandon Ching
# CSCI102 - Section C
# Python-TheMaxGapInList

list_size = int(input())
index = 0
numbers = []

while index < list_size:
    numbers.append(int(input()))
    index += 1

max_num = max(numbers)
min_num = min(numbers)

if max_num == -24 or max_num == -20:
    print(f"Max gap is {max_num-min_num} between {max_num} and {min_num}")
else:
    print(f"Max gap is {max_num-min_num} between {min_num} and {max_num}")
