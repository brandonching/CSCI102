# Brandon Ching
# CSCI102 - Section C
# Python-LovesMeLovesMeNot

petals = int(input())
index = 1
output = ''

while index < petals:
    if (index % 2) == 0:
        output += 'Loves me not, '
    else:
        output += 'Loves me,'
    index += 1

if (petals % 2) == 0:
    output += 'LOVES ME NOT'
else:
    output += 'LOVES ME'
print(output)
