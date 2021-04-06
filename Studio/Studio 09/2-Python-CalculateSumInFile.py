# Philip Belous/Brandon Ching
# CSCI102 - Section C
# Python-CalculateSumInFile

with open("numbers.txt","r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    if lines[i] == '':
        lines[i] = 0
    else:
        lines[i] = float(lines[i])

print(round(sum(lines),1))
