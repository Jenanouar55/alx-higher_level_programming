#!/usr/bin/python3
import sys
import MySQLdb


def main():
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name"
              .format(sys.argv[0]))
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )

        cursor = db.cursor()

        # SQL query to fetch cities of the specified state
        sql_query = ("SELECT GROUP_CONCAT(name SEPARATOR ', ') "
                     "FROM cities "
                     "JOIN states ON cities.state_id = states.id "
                     "WHERE states.name = %s "
                     "ORDER BY cities.id ASC")

        cursor.execute(sql_query, (state_name,))
        cities = cursor.fetchone()[0]

        if cities:
            print(cities)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        return


if __name__ == "__main__":
    main()
