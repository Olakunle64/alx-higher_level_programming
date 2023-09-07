#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv)
    if arg_count == 1:
        print("0 argument.")
    elif arg_count == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(arg_count - 1))
        arg_num = 1
        while arg_num < arg_count:
            print("{}: {}".format(arg_num, sys.argv[arg_num]))
            arg_num += 1
