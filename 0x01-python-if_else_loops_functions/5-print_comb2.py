#!/usr/bin/python3

for num in range(100):
    if num < 10:
        print("{}".format('0' + str(num)), end=', ')
    else:
        print("{}".format(num), end='\n' if num == 99 else ', ')
