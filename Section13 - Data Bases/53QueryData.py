import sqlite3

connection = sqlite3.connect("/Users/aitor/Documents/Python/Python/Section13 - Data Bases/database1.db")

cursor = connection.cursor()

# Using * we are commanding the database to select all columns from the table 'personas'
cursor.execute("SELECT * FROM PERSONAS")

# fetchall collects all columns and rows from the table ‘personas’
persons = cursor.fetchall()

for person in persons:
    print (person)

#Since we are only consulting data we do not need to use .commit()
connection.close()