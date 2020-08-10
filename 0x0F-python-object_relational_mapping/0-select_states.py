#!/usr/bin/python3
'''
List all state
'''


if __name__ == '__main__':
    import MySQLdb
    from sys import arg
    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        db=argv[3],)
    crs = db.cursor()
    crs.execute('SELECT * FROM states ORDER BY state.id;')

    states = crs.fetchall()
    for state in states:
        print(state)
    cr.close()
    db.close()
