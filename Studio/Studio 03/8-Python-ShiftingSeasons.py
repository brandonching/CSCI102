# Brandon Ching
# CSCI102 - Section C
# Python-ShiftingSeasons

month = input()
day = int(input())

if month == "January" or (month == "December" and day >=21) or month == "February":
    print("Winter")

if month == "April" or (month == "June" and day <21) or month == "March":
    print("Spring")

if (month == "June" and day >=21) or (month == "September" and day <21) or month == "August":
    print("Summer")

if (month == "September" and day >=21) or month == "November" or (month == "December" and day <21):
    print("Fall")
