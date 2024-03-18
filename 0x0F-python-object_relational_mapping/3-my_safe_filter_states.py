#!/usr/bin/python3
"""
Take arguments
Display all values in the states
Name matches the argument
Safe from MySQL injections
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db='hbtn_0e_0_usa')
    cursor = db.cursor()
    cursor.execute("SELECT *"
                   "FROM `state`"
                   "WHERE BINARY `name`=%s", (sys.argv[4],))
    [print(state) for state in cursor.fetchall()]
