# Philip Belous / Brandon Ching
# CSCI102 - Section C
# Python-ReadCSV

import csv

with open("lines.csv", "r") as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row)
