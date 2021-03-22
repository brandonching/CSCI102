# Brandon Ching
# CSCI102 - Section C
# Python-MajorityVote

votes = input()
A = 0
B = 0
C = 0

for i in votes:
    if i == "A":
        A += 1
    elif i == "B":
        B += 1
    elif i == "C":
        C += 1

if B < A > C:
    print("A")
if A < B > C:
    print("B")
if B < C > A:
    print("C")
