# Brandon Ching
# CSCI102 - Section C
# Python-QuickBrownFox

string = input().lower()
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

pangram = 'true'
missing_letters = ''
for x in letters:
    if x not in string:
        pangram = 'false'
        missing_letters += x

if pangram =='true':
    print('pangram')
else:
    print(f"missing {missing_letters}")
        
