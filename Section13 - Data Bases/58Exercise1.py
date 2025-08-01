# Exercise

# Create a database named "database.db"
# Create a table "products" with 3 fields
#     id      : Product identifier of numeric type
#     name    : Product name of text type
#     price   : Product price of numeric type

# Insert 3 products into the "products" table
#     1, "Printer", 300
#     2, "Mouse", 20
#     3, "Computer", 600

# Query the products from the "products" table
# Close the database "database.db"

import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE PRODUCTS (id INTEGER, name TEXT, price INTEGER)")
connection.commit()

product_list = [ (1,'Printer',300), (2,'Mouse',20),(3,'Computer',600)]
cursor.executemany("INSERT INTO PRODUCTS VALUES (?,?,?)", product_list)
connection.commit()

products_list = cursor.execute("SELECT * FROM PRODUCTS")
for product in product_list:
    print(product)
    
connection.close()