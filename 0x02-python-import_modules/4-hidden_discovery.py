#!/usr/bin/python3
if __name__ == "__main__":
    import importlib.util

    mod_name = "hidden_4.pyc"
    file_path = "/home/vagrant/alx-high_level_programming/0x02-python-import_modules/"
    spec_file = importlib.util.spec_from_file_location(mod_name, file_path)
    load_object = importlib.util.module_from_spec(spec_file)
    spec_file.loader.exec_module(load_object)
    
    for name in sorted(dir(load_object)):
        if '_' == name[0]:
            continue;
        print("{}".format(name))
