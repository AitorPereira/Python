import sqlite3

connection = sqlite3.connect("database1.db")

cursor = connection.cursor()

cursor.execute("INSERT INTO PERSONAS VALUES ('John','Smith','Rodriguez',30)")

connection.commit()

connection.close()