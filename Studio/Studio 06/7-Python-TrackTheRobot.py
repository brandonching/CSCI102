# Brandon Ching
# CSCI102 - Section C
# Python-TrackTheRobot

instructions = int(input())
index = 0
commands = []
x=0
y=0

while index < instructions:
    commands.append(input())
    index += 1

for i in commands:
    if 'right' in i:
        x += int(i[6:])
    elif 'left' in i:
        x -= int(i[5:])
    elif 'up' in i:
        y += int(i[3:])
    elif 'down' in i:
        y -= int(i[5:])


print(f"({x}, {y})")
