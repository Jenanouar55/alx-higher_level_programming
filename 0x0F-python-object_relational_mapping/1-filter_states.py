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

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cursor = db.cursor()
    sql_query = """
        SELECT id, name
        FROM states
        WHERE name LIKE 'N%'
        ORDER BY id ASC
    """
    cursor.execute(sql_query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
