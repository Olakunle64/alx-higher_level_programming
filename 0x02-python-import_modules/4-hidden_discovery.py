#!/usr/bin/python3
if __name__ == "__main__":
    import py_compile
    module_name = "./hidden_4.pyc"
    load_module = py_compile.compile(module_name)
    
    for name in sorted(dir(load_module)):
        if '_' == name[0]:
            continue;
        print("{}".format(name))
