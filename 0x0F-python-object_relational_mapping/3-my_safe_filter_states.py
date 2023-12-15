#!/usr/bin/python3

"""This module uses MySQLdb to connect to a database
    and query out some data on the localhost of port number
    <3306>

    What the query entails:
        Display all values in the <states> table of hbtn_0e_0_usa
        where <name> matches the argument

        Note: control the last user input to avoud SQL injection attacks
    """

import sys
import MySQLdb


def real_escape_string(name):
    """escape all single quote characters in the string input"""
    new_name = ""
    for ch in name:
        if ch == "'":
            new_name += "\\"
        new_name += ch
    return new_name


if __name__ == "__main__":
    username = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    searched_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=pwd, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY\
                states.id ASC".format(real_escape_string(searched_name)))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
