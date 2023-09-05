#!/usr/bin/python3

def uppercase(str):
    length = len(str)
    for ch in str:
        num = ord(ch)
        length -= 1
        if num in range(97, 123):
            num = num - 32
            print("{}".format(chr(num)), end='\n' if length == 0 else '')
        else:
            print("{}".format(ch), end='\n' if length == 0 else '')
