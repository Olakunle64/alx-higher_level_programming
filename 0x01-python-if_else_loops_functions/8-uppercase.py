#!/usr/bin/python3

def uppercase(str):
    for ch in str:
        num = ord(ch)
        if num in range(97, 123):
            num = num - 32
            print("{}".format(chr(num)), end='')
        else:
            print("{}".format(ch), end='')
    print()
