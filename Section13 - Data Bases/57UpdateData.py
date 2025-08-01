import sqlite3

connection = sqlite3.connect("/Users/aitor/Documents/Python/Python/Section13 - Data Bases/database1.db")

cursor = connection.cursor()

cursor.execute("UPDATE PERSONAS SET edad = 30 WHERE nombre = 'Daniel'")

connection.commit()

connection.close()