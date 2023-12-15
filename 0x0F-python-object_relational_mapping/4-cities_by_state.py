#!/usr/bin/python3

"""This module uses MySQLdb to connect to a database
    and query out some data on the localhost of port number
    <3306>

    What the query entails:
        Display all values in the <cities> table of hbtn_0e_0_usa
    """

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=pwd, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities c JOIN\
                states s ON c.state_id=s.id ORDER BY c.id ASC")
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()
