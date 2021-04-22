# Philip Belous/Brandon Ching
# CSCI102 - Section C
# Python-WriteCSV

from csv import *
import re
num_inputs = int(input())
with open('results.csv','w') as file:
    for row in range(0,num_inputs):
        file.write(re.sub("[ ]",",",input()))
        file.write("\n")
