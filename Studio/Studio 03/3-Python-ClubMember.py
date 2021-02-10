# Brandon Ching
# CSCI102 - Section C
# Python-ClubMember

club_one = input()
club_two = input()
search_name = input()

if search_name in club_one and search_name in club_two:
    print(f"{search_name} is in both clubs.")
elif search_name in club_one:
    print(f"{search_name} is a member of Club One.")
elif search_name in club_two:
    print(f"{search_name} is a member of Club Two.")
else:
    print(f"{search_name} is not found in either club")
