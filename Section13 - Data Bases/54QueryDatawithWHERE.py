import sqlite3

connection = sqlite3.connect("/Users/aitor/Documents/Python/Python/Section13 - Data Bases/database1.db")

cursor = connection.cursor()

#We want to select only people older than 40
cursor.execute("SELECT * FROM PERSONAS WHERE edad > 40")

#We use fetchall to collect this information
selected_people = cursor.fetchall()

for person in selected_people:
    print (person)

#Commit is not necessary since we are only consulting information

connection.close()
