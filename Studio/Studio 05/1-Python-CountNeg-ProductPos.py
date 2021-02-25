# Brandon Ching
# CSCI102 - Section C
# Python-CountNeg-ProductPos

"""
=+=+=+=+=+=+=+=+=+=+=
Data Preprocessing
=+=+=+=+=+=+=+=+=+=+=
"""

# Read in the first line (e.g., length of the list)
input_list_length = int(input())

# Use this list in your code
input_list = []

# The loop control variable defines the loop index value for each iteration.
loop_index = 0

while loop_index < input_list_length:
    # Ask the user for a new input and add it to our input_list
    new_list_item = input()  # Read in the remaining input lines
    input_list.append(int(new_list_item))

    # After finishing these instructions, advance to the next loop iteration and repeat the steps
    loop_index = loop_index + 1

positive_sum = 1
negative_count = 0
for x in input_list:
    if x >= 0:
        positive_sum = positive_sum * x
    elif x < 0:
        negative_count = negative_count + 1

print(f"Product of positives: {positive_sum}")
print(f"Count of negatives: {negative_count}")
