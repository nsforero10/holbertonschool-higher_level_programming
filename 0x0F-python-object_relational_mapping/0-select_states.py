#!/usr/bin/python3
'''
List all state
'''

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost')
    crs = db.cursor()
    crs.execute('select * from states order by.id asc;')

    states = crs.fetchall()
    for state in states:
        print(state)
