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

        sql_query = ("SELECT id, name "
                     "FROM states "
                     "WHERE name = %s "
                     "ORDER BY id ASC")
        cursor.execute(sql_query, (state_name,))
        states = cursor.fetchall()

        for state in states:
            print(state)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        return


if __name__ == "__main__":
    main()
