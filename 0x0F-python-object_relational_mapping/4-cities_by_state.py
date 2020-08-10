#!/usr/bin/python3
'''  takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument'''

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cr = db.cursor()
    cr.execute('SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states ON cities.state_id = states.id', (argv[4],))
    states = cr.fetchall()

    i = 0
    for state in states:
        if i != 0:
            print(", ", end="")
        print("%s" % state, end="")
        i += 1
    print('')
    cr.close()
    db.close()
