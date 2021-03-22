# Brandon Ching
# CSCI 102 - Section C
# Week 8 - Lab A - Rolling a Die
# References: None
# Time: 25 minutes
import random

number = int(input ("Input the number of rolls to make:\nNUMBER> "))
seed = random.seed(int(input("Input the seed for the random number generator:\nSEED> ")))
rolls = [0,0,0,0,0,0]

for i in range(0,number):
    rolls[random.randint(1,6) - 1] += 1

print(f"Your {number} rolls follow:")
for i in range(0,6):
    print(f"OUTPUT {i+1} occured {rolls[i]} times")
