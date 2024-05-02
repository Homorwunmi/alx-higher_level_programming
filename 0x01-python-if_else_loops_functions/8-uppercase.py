#!/usr/bin/python3
def uppercase(str):
    for character in str:
        value = ord(character)
        if value >= 97 and value <= 122:
            character = chr(value - 32)
        print(character, end="")
    print()
