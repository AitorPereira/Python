import sqlite3

connection = sqlite3.connect("/Users/aitor/Documents/Python/Python/Section13 - Data Bases/database1.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM PERSONAS ORDER BY edad")

list_person_organized = cursor.fetchall()

for person in list_person_organized:
    print (person)

connection.close()