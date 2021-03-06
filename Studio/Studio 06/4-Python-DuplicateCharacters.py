# Brandon Ching
# CSCI102 - Section C
# Python-DuplicateCharacters

input_str = input()
duplicate = []
first_loop_index = 0
for i in range(0,len(input_str)):
    current_char = i
    first_loop_index += 1
    for i in range(first_loop_index + 1,len(input_str)):
        if i == current_char:
            duplicate.append(i)
print(f"List of duplicate chars: {duplicate}")
