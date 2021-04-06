# Brandon Ching
# CSCI102 - Section C
# Python-CharTypesInFile

letters = 0
digits = 0
punctuations = 0
symbols = ".!?"

with open("textfile.txt", "r") as file:
    for line in file:
        for char in line:
            if char.isalpha():
                letters += 1
            elif char.isnumeric():
                digits += 1
            elif char != " ":
                punctuations += 1
print(f"There are {letters} letter(s), {digits} digit(s), and {punctuations} punctuation(s) in the file.")
