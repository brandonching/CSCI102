# Brandon Ching
# CSCI102 - Section C
# Python-HangingOutOnSouthTable

max_people = int(input())
events = int(input())
event_list = []

event_index = 0
while event_index < events:
    event_list.append(input())
    event_index += 1

current_people = 0
groups_denied = 0
for x in event_list:
    if 'start' in x:
        if current_people + int(x[6:]) > max_people:
            groups_denied += 1
        else:
            current_people += int(x[6:])
    if 'finish' in x:
        current_people -= int(x[6:])

print(groups_denied)
