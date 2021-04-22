# Brandon Ching
# CSCI 102 Section C
# Python-TwoSum

def two_sum(num_list, target_sum):
    for num_1 in range(len(num_list)):
        for num_2 in range(len(num_list)):
            if num_list[num_1] + num_list[num_2] == target_sum:
                return [num_1, num_2]
