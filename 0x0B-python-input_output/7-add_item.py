#!/usr/bin/python3
"""This module contain a script that add all arguments
    to a list and save it in a file"""

import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

new_list = []
i = 1
while i < len(sys.argv):
    new_list.append(sys.argv[i])
    i += 1
if not os.path.isfile("add_item.json"):
    save_to_json_file(new_list, "add_item.json")

my_list = load_from_json_file("add_item.json")
my_list.extend(new_list)
save_to_json_file(my_list, "add_item.json")
