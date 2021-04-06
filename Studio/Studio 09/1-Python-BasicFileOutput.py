# Philip Belous/Brandon Ching
# CSCI 102 Section C
# Python-BasicFileOutput

list1 = input().split(',')

with open("output.txt", "w") as f:
    for num in list1:
        f.write(num + '\n')
