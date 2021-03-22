# Philip Belous / Brandon Ching
# CSCI102 - Section C
# Python-CountSymbolsAndChars

input_str = input()
chars_list = 'abcdefghijklmnopqrstuvwxyz'
digit_list = '1234567890'
symbol_list = '!@#$%^&*()'
chars = 0
digits = 0
symbols = 0
for i in input_str:
    if i.lower() in chars_list:
        chars += 1
    elif i in digit_list:
        digits += 1
    elif i in symbol_list:
        symbols += 1
print(f'Total counts of chars, digits, and symbols are {chars}, {digits}, and {symbols}')
