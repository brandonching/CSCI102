# Brandon Ching
# CSCI102 - Section C
# Python-GeneSequenceSort

base = input()

if len(base) > 10:
    print("Greater than 10 bases.")
elif len(base) < 10:
    print("Less than 10 bases.")
else:
    if 'ATGG' in base:
        print("MATCH!")
    else:
        print("Not a match.")
