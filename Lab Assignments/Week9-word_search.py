# Brandon Ching
# CSCI 102 – Section C
# Week 9A - Word Search
# References: NA
# Time: 10 minutes

import random
word_count = 0
correct_length_words = []
length = int(input("Enter the length of the words to find:\nLENGTH> "))

with open("dictionary.txt","r") as file:
    for word in file:
        if length == len(word)-1:
            word_count += 1
            correct_length_words.append(word)
            
print(f"The number of words with length {length} is:\nOUTPUT {word_count}")
if word_count != 0:
    print(f"Here is one random word with length {length}:\nOUTPUT {correct_length_words[random.randint(0,word_count)]}")
else:
    print(f"There are no words of length {length} in the dictionary.\nOUTPUT None")
