#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv)
    if arg_count == 1:
        print("{}".format(arg_count - 1))
    else:
        arg_index = 1
        result = 0
        while arg_index < arg_count:
            result += int(sys.argv[arg_index])
            arg_index += 1
        print("{}".format(result))
