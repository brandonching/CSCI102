# Brandon Ching
# CSCI102 - Section C
# Python-ChessBoardColoring

square = input()
odd = [1,3,5,7,'a','c','e','g']
even = [2,4,6,8,'b','d','f','h']
alpha = square[0]
num = int(square[1])

if  (alpha in even and num in even) or (alpha in odd and num in odd):
    print("black")
else:
    print("white")
