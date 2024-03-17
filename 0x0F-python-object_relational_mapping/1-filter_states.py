#!/usr/bin/python3
"""
List all states with a name starting with N from database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    query = (
        "SELECT * FROM `states` "
        "WHERE `name` LIKE 'N%' "
        "ORDER BY `id` ASC"
    )
    cursor.execute(query)
    for state in cursor.fetchall():
        print(state)
