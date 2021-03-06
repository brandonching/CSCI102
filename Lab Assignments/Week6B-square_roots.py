# Brandon Ching 
# CSCI 102 – Section C
# Week 6 - Lab B - Estimating Square Roots
# References: N/A
# Time: 20 minutes

print("How many numbers am I estimating John?")
count = int(input('COUNT>'))
print("Input each number to estimate. ")
num = []
for i in range(0,count):
    num.append(float(input('NUMBER>')))
print("The square roots are as follows: ")

for i in range(0,count):
    iteration = 1
    initial_guess = 10.0
    better_guess = (initial_guess + num[i] / initial_guess) / 2.0
    while initial_guess != better_guess:
        initial_guess = better_guess
        better_guess = (initial_guess + num[i] / initial_guess) / 2.0
        iteration += 1
    print(f"OUTPUT After {iteration} iterations, {num[i]}^0.5 = {better_guess:.2f}")
