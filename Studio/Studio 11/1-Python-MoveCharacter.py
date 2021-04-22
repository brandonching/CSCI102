# Brandon Ching
# CSCI 102 Section C
# Python-MoveCharacter

def move_character(word, character):
    new_str = ''
    char_count = 0
    for char in word:
        if char != character:
            new_str += char
        else:
            char_count += 1
    for i in range(char_count):
        new_str += character
    return new_str
