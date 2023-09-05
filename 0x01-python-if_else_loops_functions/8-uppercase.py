#!/usr/bin/python3

def uppercase(str):
    length = len(str)
    if length == 0:
        print("")
        return
    full_string = ""
    for ch in str:
        num = ord(ch)
        length -= 1
        if num in range(97, 123):
            num = num - 32
        full_string += chr(num)
    print("{}".format(full_string))
