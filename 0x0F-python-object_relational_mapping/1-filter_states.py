#!/usr/bin/python3
"""This module uses MySQLdb to connect to a database
    and query out some data on the localhost of port number
    <3306>

    What the query entails:
        It list all the states that starts with uppercase N
        in the <state> table
    """

import sys
import MySQLdb

if __name__ == "__main__":
    userName = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=userName,
                         passwd=pwd, db=db_name)
    cur = db.cursor()
    pattern = "N%"
    cur.execute("SELECT * FROM states WHERE BINARY\
                name LIKE %s ORDER BY states.id ASC", (pattern,))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
