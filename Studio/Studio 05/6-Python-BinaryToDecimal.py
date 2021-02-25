# Brandon Ching
# CSCI102 - Section C
# Python-OnesAndZerosTranslator

binary_str = input("")
i=0
decimal = 0
for x in reversed(binary_str):
    if x in ['0','1']:
        decimal += int(x)*(2**i)
        i += 1
        valid = 'true'
    else:
        print(f"ERROR: Input is not a binary number.")
        valid = 'false'
        break
if valid == 'true':
    print(decimal)
