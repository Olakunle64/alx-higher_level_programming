#!/usr/bin/python3

"""This module uses MySQLdb to connect to a database
    and query out some data on the localhost of port number
    <3306>

    What the query entails:
        Display all values in the <cities> table of hbtn_0e_0_usa

    Note: Your code must be SQL injection free
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
    state_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=pwd, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT c.name FROM cities c WHERE c.state_id=(SELECT s.id\
                FROM states s WHERE\
                s.name='{}')".format(real_escape_string(state_name)))
    cities = cur.fetchall()
    i = 0
    for city in cities:
        if i > 0:
            print(", ", end='')
        print("{}".format(city[0]), end='')
        i += 1
    print()
    cur.close()
    db.close()
