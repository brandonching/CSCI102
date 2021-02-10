# Brandon Ching
# CSCI102 - Section C
# Python-SimonSays

command = input()

if command[0:10] == 'Simon says':
    print(command[11:])
else:
    print("")
