import sqlite3

connection = sqlite3.connect("/Users/aitor/Documents/Python/Python/Section13 - Data Bases/database1.db")

cursor = connection.cursor()

cursor.execute("DELETE FROM PERSONAS WHERE nombre = 'John'")

connection.commit()

connection.close()