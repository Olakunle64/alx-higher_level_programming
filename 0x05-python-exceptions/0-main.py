#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

#my_list = [1, 2, 3, 4, 5]
my_list = []
nb_print = safe_print_list(my_list, 0)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 5)
print("nb_print: {:d}".format(nb_print))

