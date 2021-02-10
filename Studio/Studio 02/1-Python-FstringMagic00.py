# Brandon Ching
# CSCI102 - Section C
# Python-FstringMagic00

name = input()
currentAge = int(input())
minsAge = currentAge * 365 * 24 * 60
secsAge = (currentAge + 2) * 365 * 24 *3600

print(f"{name}: Now: {minsAge} mins old; Future: {secsAge} secs old.")
