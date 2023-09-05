#!/usr/bin/python3

for num in range(9):
    for num2 in range(1 + num, 10):
        print("{}".format(str(num) + str(num2)), end='\n' if num == 8 else ', ')
