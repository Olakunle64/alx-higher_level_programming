#!/usr/bin/python3
"""This module contains a script that add all arguments
    to a python list and then save them to a file
    """

import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

new_list = []
i = 1
while i < len(sys.argv):
    new_list.append(sys.argv[i])
    i += 1
save_to_json_file(new_list, "add_item.json")
