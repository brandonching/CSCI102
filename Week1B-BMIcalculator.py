#   Brandon Ching
#   ​CSCI 102 – Section C 
#   Week 1 - Part B 
#   References: ZyBooks 
#   Time: 10 minutes

print("Input your weight, in pounds.") 
W = int(input("WEIGHT>"))

print("Input your height, in inches.") 
H = int(input("HEIGHT>"))

#   Convert pounds to kilograms
mass = W * 0.454

#   Convert inchs to meters
height = H * 0.0254

print("Your Body-Mass Index is:") 
print("OUTPUT", round(mass/height**2,1))
