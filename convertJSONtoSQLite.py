import json
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None;
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_table_from_json(conn, json_data, table_name):
    data = json_data["scorers"]

    if len(data) == 0:
        return

    cols = ', '.join("`{}`".format(col) for col in data[0].keys())
    vals = ', '.join('?' for _ in data[0].keys())

    sql = 'CREATE TABLE IF NOT EXISTS `{}` ({})'.format(table_name, cols)
    cur = conn.cursor()
    cur.execute(sql)

    for row in data:
        sql = 'INSERT INTO `{}` ({}) VALUES ({})'.format(table_name, cols, vals)
        cur.execute(sql, tuple(row.values()))
    conn.commit()

def main():
    database = r"pythonsqlite.db"
    json_data = {
        "scorers": [
            {
                "name": "Humphreys Minandi",
                "day": "Wednesday, 01 November 2023 CAT (UTC+2)",
                "score": "1-0",
                "time": "55",
                "result": "win",
                "venue": "away"
            },
            {
                "name": "M. Paipi",
                "day": "Wednesday, 01 November 2023 CAT (UTC+2)",
                "score": "1-0",
                "time": "07",
                "result": "win",
                "venue": "away"
            },
            {
                "name": "R. Saizi",
                "day": "Saturday, 04 November 2023 CAT (UTC+2)",
                "score": "1-4",
                "time": "10",
                "result": "win",
                "venue": "away"
            }
        ]
    }
    table_name = "scorers"

    conn = create_connection(database)
    if conn is not None:
        create_table_from_json(conn, json_data, table_name)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
