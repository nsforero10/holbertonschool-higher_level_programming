#!/usr/bin/python3
'''  takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument'''

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost')

    cursor = db.cursor()
    cursor.execute(
        'SELECT cities.id, cities.name, states.name FROM cities JOIN states ON\
        cities.state_id = states.id;', (sys.argv[4], ))

    cities = cursor.fetchall()

    for city in cities:
        print(city)
    print("")

    cursor.close()
    db.close()
