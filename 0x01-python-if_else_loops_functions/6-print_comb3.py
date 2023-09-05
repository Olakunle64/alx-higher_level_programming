#!/usr/bin/python3

for n in range(9):
    for n2 in range(1 + n, 10):
        print("{}".format(str(n) + str(n2)), end='\n' if n == 8 else ', ')
