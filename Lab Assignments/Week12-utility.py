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


def find_word_count(input_list, string):
    count = 0
    for index in input_list:
        for word in index.split():
            if string == word:
                    count += 1
    return count
    

def score_finder(players, scores, name):
    lower_players = []
    for names in players:
        lower_players.append(names.lower())

    if name.lower() in lower_players:
        index = 0
        for names in players:
            if name.lower() == names.lower():
                break
            else:
                index += 1
        print('OUTPUT', name, 'got a score of', scores[index])
    else:
        print('OUTPUT player not found')


def union(list_1, list_2):
    new_list = []
    for item in list_1:
        new_list.append(item)
    for item in list_2:
        new_list.append(item)

    no_dupes = []
    for item in new_list:
        if item not in no_dupes:
            no_dupes.append(item)
    return no_dupes


def intersect(list_1, list_2):
    new_list = []
    for item in list_1:
        for index in list_2:
            if item == index:
                new_list.append(item)
    return new_list




