# Brandon Ching
# CSCI102 Section C
# Python-CountWordInFile

count = 0
with open("paragraph.txt","r") as file:
    for line in file:
        word = line.split()
        for x in word:
            if ("book" in x.lower()) and ("books" not in x.lower()):
                count += 1

print(f"The word 'book' appears {count} time(s).")
