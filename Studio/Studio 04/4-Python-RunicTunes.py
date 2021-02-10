# Brandon Ching
# CSCI102 - Section C
# Python-RunicTunes

english_word = input()

if 'p' in english_word or 'P' in english_word:
    print("Enter a word without the letter 'p'")
else:
    runic_word = 'n' + english_word[len(english_word)//2:] + english_word[0:len(english_word)//2]
    print(runic_word)
