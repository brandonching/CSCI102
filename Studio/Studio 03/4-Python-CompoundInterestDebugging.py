# Brandon Ching
# CSCI102 - Section C
# Python-CompoundInterestBugs
import math
# Get inputs from user
principal = float(input()) # Get principal
interest_rate = float(input()) # Get interest rate
duration_of_investment = int(input()) # Get duration in years

# Calculate compound interest using the formula given with a compounding rate of 4 times each year.
# n = 4 in the formula.
amount = principal * (1 + (interest_rate / 4)) ** (4 * duration_of_investment)
amount = round(amount)

# Print out the final amount.
print(amount)
