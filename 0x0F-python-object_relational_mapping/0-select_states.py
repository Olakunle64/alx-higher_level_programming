#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    userName = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(user=userName, passwd=pwd, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    for state in states:
        print(state)
