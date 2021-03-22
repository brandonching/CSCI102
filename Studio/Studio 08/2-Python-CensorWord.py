# Philip Belous / Brandon Ching
# CSCI102 - Section C
# Python-CensorWord

input_str = input()
censored_word = input()
stars = ''
for i in range(0,len(censored_word)):
    stars += '*'

print(input_str.replace(censored_word,stars))
