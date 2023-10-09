#!/usr/bin/python3
"""This module contains a class named <MyList> which
    inherit from <list> class

    It has just a single method
    """


class MyList(list):
    """This class has the following attribute:

    methods: <print_sorted>
    """

    def print_sorted(self):
        """print a  list but sorted(ascending sort)"""
        my_sorted_list = sorted(self)
        print(my_sorted_list)
