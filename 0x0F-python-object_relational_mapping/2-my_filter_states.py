#!/usr/bin/python3

"""This module uses MySQLdb to connect to a database
    and query out some data on the localhost of port number
    <3306>

    What the query entails:
        Display all values in the <states> table of hbtn_0e_0_usa
        where <name> matches the argument
    """

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    searched_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=pwd, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY\
                states.id ASC".format(searched_name))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
