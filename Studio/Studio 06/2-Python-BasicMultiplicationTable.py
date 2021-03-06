# Philip Belous / Brandon Ching
# CSCI102 - Section C
# Python-BasicMultiplicationTable

number = int(input())
start = int(input())
end = int(input())

for i in range(start, end + 1):
    print(f"{number} x {i} = {number * i}")
