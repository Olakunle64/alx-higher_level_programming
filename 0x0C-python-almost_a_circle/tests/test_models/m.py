#!/usr/bin/python3

with open("test_rectangle.py", "r", encoding="utf-8") as file_obj:
    content = file_obj.readlines()
with open("test_rectangle.py", "w", encoding="utf-8") as file_obj:
    for line in content:
        modified_line = line.replace("expected_output", "ex_out")
        file_obj.write(modified_line)
