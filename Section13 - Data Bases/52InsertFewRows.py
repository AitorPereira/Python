import sqlite3

connection = sqlite3.connect("/Users/aitor/Documents/Python/Python/Section13 - Data Bases/database1.db")

cursor = connection.cursor()

person_list = [ ('Pedro','Rodriguez','Perez',26), ('Maria','Lopez','Gomez',45), ('Daniel','Pereira','Ramirez',23) ]

cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)", person_list)

connection.commit()

connection.close()