# Brandon Ching
# CSCI102 - Section C
# Python-ShortestWordInSentence

input_str = input().split()
short_len = len(input_str[0])
for word in input_str:
    if len(word) < short_len:
        short_len = len(word)
print(short_len)
