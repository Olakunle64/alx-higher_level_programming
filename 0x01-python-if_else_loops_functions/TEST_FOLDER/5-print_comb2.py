#!/usr/bin/python3
import dis
def kunle(n):
    for num in range(n):
        if num < 10:
            print("{}".format('0' + str(num)), end=', ')
        else:
            print("{}".format(num), end='\n' if num == 99 else ', ')

dis.dis(kunle)
