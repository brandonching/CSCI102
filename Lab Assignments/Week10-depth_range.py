# Brandon Ching
# CSCI 102 – Section C
# Week 10 Lab
# References: NA
# Time: 10 minutes

import csv

with open('formations_parsed.csv', 'w', newline='') as parsedfile:
    csv.writer(parsedfile).writerow(['Depth','Start Depth','End Depth','Average Depth','Formation'])
    with open("formations.csv", newline='') as csvfile:
        filereader = csv.reader(csvfile)
        next(filereader)
        for row in filereader:
            print(row)
            parsed_row = []
            parsed_row.append(row[0])
            parsed_row.append(float(row[0].split('-')[0]))
            parsed_row.append(float(row[0].split('-')[1]))
            parsed_row.append(round(sum(parsed_row[1:3])/2,1))
            parsed_row.append(row[1])
            csv.writer(parsedfile).writerow(parsed_row)
    
