# Brandon Ching
# CSCI 102 – Section C
# Week 11 Lab
# References: None
# Time: 25 minutes

#################################################
######## BRANDON CHIGN                   ########
######## Lab 11 - Function Definitions   ########
######## Section - C                     ########
#################################################
        
# Imports
import math

################################################
########   Function 1 : PrintOutput     ########
################################################

def print_output(string):
    print(f'OUTPUT {string}')


################################################
########   Function 2 : TriangleArea    ########
################################################

def triangle_area(height, width):
    area = (height * width) / 2
    print_output(round(area,2))


################################################
########   Function 3 : FeetToMeters    ########
################################################

def feet_to_meters(feet):
    meters = feet * 0.3048
    print_output(round(meters,3))
    

################################################
########   Function 4 : PolarCoords     ########
################################################

def polar_coords(x,y):
    radius = math.sqrt(x**2 + y**2)
    theata = math.atan(y/x) * 180 / math.pi
    print_output(round(radius,1))
    print_output(round(theata,1))


################################################
########   Function 5 : EurosToDollars  ########
################################################

def euros_to_dollars(euros):
    dollars = euros * 1.17
    print_output(round(dollars,2))
