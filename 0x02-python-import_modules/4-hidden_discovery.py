#!/usr/bin/python3
if __name__ == "__main__":

    mod_name = "hidden_4.pyc"
    for name in dir(mod_name):
        if '_' == name[0]:
            continue
        print("{}".format(name))
