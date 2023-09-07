#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    arg_count = len(sys.argv)
    if arg_count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = ['+', '-', '*', '/']
    if sys.argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == operator[0]:
        print("{} + {} = {}".format(a, b, a + b))
    elif sys.argv[2] == operator[1]:
        print("{} - {} = {}".format(a, b, a - b))
    elif sys.argv[2] == operator[2]:
        print("{} - {} = {}".format(a, b, a * b))
    elif sys.argv[2] == operator[3]:
        print("{} - {} = {}".format(a, b, a / b))
