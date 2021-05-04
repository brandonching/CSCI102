# Brandon Ching
# CSCI 102 – Section C
# Week 13 Review Lab
# References: 101 Instructor Rena helped me debug.
# Time: 60 minutes

message = input('Input the message to encrypt and the desired shift.\nMESSAGE> ')
shift = int(input('SHIFT> '))
shifted_message = ''
for char in message:
    if char.isalpha():
        if char.islower():
            shifted_message += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            shifted_message += chr((ord(char) + shift - 65) % 26 + 65)
    else:
        shifted_message += char
print(f'Your message encrypted with shift {shift}:\nOUTPUT {shifted_message}')



message_to_decrypt = input('\nInput the message to decrypt using brute force\nMESSAGE_TO_DECRYPT> ')
decrypt_shift = 0
decrypt_message = ''
best_match = 0
for shift in range(0, 26):
    original_message = ''
    matching_words = 0
    for char in message_to_decrypt:
        if char.isalpha():
            if char.islower():
                original_message += chr((ord(char) - shift - 97) % 26 + 97)
            else:
                original_message += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            original_message += char
    

    split_message = original_message.lower().split()
    with open("dictionary.txt","r") as file:
        for word in file:
            if word.replace('\n','') in split_message:
                matching_words += 1
    if matching_words > best_match:
        best_match = matching_words
        decrypt_shift = shift
        decrypt_message = original_message        
        
print(f'The original message was encrypted with a shift of:\nOUTPUT {decrypt_shift}')
print(f'The original message is:\nOUTPUT {decrypt_message}')
