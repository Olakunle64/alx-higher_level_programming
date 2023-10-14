#!/usr/bin/python3

with open("test_square.py", "r", encoding="utf-8") as file_obj:
    content = file_obj.readlines()
with open("test_square.py", "w", encoding="utf-8") as file_obj:
    for line in content:
        modified_line = line.replace("r1", "s1")
        file_obj.write(modified_line)
