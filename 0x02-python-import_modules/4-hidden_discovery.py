#!/usr/bin/python3
if __name__ == "__main__":

    mod_name = "hidden_4.pyc"
    for name in dir(mod_name):
        if name[0] == '_' and name[1] == '_':
            continue
        print("{}".format(name))
