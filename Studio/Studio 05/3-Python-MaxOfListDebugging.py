# Brandon Ching
# CSCI102 - Section C
# Python-OhScopeWhatsWrong

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

"""
=+=+=+=+=+=+=+=+=+=+=
FIND MAX NUM IN LIST
=+=+=+=+=+=+=+=+=+=+=
"""

max_num = max(input_list)

print(f"Given list {input_list}, max num is {max_num}")
