# Brandon Ching
# CSCI102 - Section C
# Python-HighestRangeInFile

with open("scores.txt", "r") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        if lines[i] == '':
            lines[i] = 1
        else:
            lines[i] = float(lines[i])

print(round((max(lines)-min(lines)),1))
