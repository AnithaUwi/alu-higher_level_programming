#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
            if ord('a') <= ord(char) <= ord('z'):
                result += chr(ord(char) - 32)  # Convert to uppercase
            else:
                result += char  # Keep the character as is
                print("{}".format(result))  # Print the result

