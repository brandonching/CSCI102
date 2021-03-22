# Philip Belous / Brandon Ching
# CSCI102 - Section C
# Python-Python-EvenOddList

list1 = input().split(",")

odd = []
even = []
for i in range(len(list1)):
    list1[i] = int(list1[i])
    if list1[i] % 2 == 0:
        even.append(list1[i])
    else:
        odd.append(list1[i])

print(even + odd)
