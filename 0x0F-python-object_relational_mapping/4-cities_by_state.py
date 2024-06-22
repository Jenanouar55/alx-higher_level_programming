#!/usr/bin/python3
import sys
import MySQLdb


def main():
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )

        cursor = db.cursor()

        # SQL query to fetch cities along with their state names
        sql_query = ("SELECT cities.id, cities.name, states.name "
                     "FROM cities "
                     "JOIN states ON cities.state_id = states.id "
                     "ORDER BY cities.id ASC")

        cursor.execute(sql_query)
        cities = cursor.fetchall()

        for city in cities:
            print(city)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        return


if __name__ == "__main__":
    main()
