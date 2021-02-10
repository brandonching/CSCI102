# Brandon Ching
# CSCI102 - Section C
# Python-LoneSumDebugging

a = int(input())
b = int(input())
c = int(input())

lone_sum = a+b+c

if a in [b, c]:
  lone_sum = lone_sum - a

if b in [a,c]:
  lone_sum = lone_sum - b

if c in [a,b]:
  lone_sum = lone_sum - c

print(lone_sum)
