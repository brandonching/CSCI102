# Brandon Ching
# CSCI 102 – Section C
# Week 12 - Utility using Git and Incremental Development
# References: 
# Time: 45 minutes

import math

def load_file(file_name):
    with open(file_name, 'r') as file:
        lines = []
        for line in file:
            lines.append(line.strip('\n'))
    return lines


def update_string(string_1, string_2, num):
    output = 'OUTPUT '
    output += string_1[:num]
    output += string_2
    output += string_1[num+1:]
    return output




