# Brandon Ching
# CSCI102 - Section C
# Python-CatYears

human_age = int(input())
cat_age = 0

if human_age < 0:
    print("Age must be a positive number.")
else:
    if human_age <= 2:
        cat_age = human_age * 11
    else:
        cat_age = 22 + (human_age - 2) * 4
    print(f"Cat's age is {cat_age} in cat's years")
