import sqlite3

def connect():
    connection = sqlite3.connect('bookstore.bd')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)')
    connection.commit()
    connection.close()


def add(title, author, year, isbn):
    connection = sqlite3.connect('bookstore.bd')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO books VALUES (NULL,?,?,?,?)',(title, author, year, isbn))
    connection.commit()
    connection.close()

def display():
    connection = sqlite3.connect('bookstore.bd')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')
    results = cursor.fetchall()
    connection.close()
    return results

def search(title, author, year, isbn):
    connection = sqlite3.connect('bookstore.bd')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?',(title, author, year, isbn))
    results = cursor.fetchall()
    connection.close()
    return results

def remove(id):
    connection = sqlite3.connect('bookstore.bd')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE id=?', (id,))
    connection.commit()
    connection.close()

def update(title, author, year, isbn, id):
    connection = sqlite3.connect('bookstore.bd')
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?', (title, author, year, isbn, id))
    connection.commit()
    connection.close()



#---TESTS---
# connect()
# add("El Quijote", "Cervantes", 1506, 421)
# add("Harry Potter", "J.K Rowling", 1995, 678)
# add("Lord of the Rings", "J.K Tolkien", 1953, 999)
# result = display()
# print (result)
# result = search(year=1995)
# for book in result:
#     print (book)
# remove(2)
# result = display()
# for book in result:
#     print (book)
# update(title="Atomic Habits", author="Einstein", year=1975, isbn=5752, id=3)
# result = display()
# for book in result:
#     print (book)