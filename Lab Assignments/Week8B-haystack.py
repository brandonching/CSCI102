# Brandon Ching
# CSCI 102 - Section C
# Week 8 - Lab B - Combing Through a Haystack
# References: None
# Time: 10 minutes

s = input("Enter a DNA string s:\ns> ")
t = input("Enter a substring t:\nt> ")
sub_strings = 0
locations = ""

index = 1
for i in range(0,len(s)-len(t)+1):
    if (s[i:i+len(t)]) == t:
        sub_strings += 1
        locations += f"{index} "
    index += 1
        

#Output
print(f"The total number of substrings found is {sub_strings}\nOUTPUT {sub_strings}")
print(f"The locations of these substrings in s are: {locations}\nOUTPUT {locations}")
