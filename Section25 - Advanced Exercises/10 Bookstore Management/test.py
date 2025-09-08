import database

connection = database.create_connection_bd()

database.create_bookstore_table(connection)

book1 = ("El Quijote", "Cervantes", 1605, 12345)
book2 = ("1984", "Orwell", 1949, 54321)

database.insert_book_table(connection, book1)
database.insert_book_table(connection, book2)

old_book = ("1984", "Orwell", 1949, 54321)
new_book = ("1984", "George Orwell", 1949, 54321)

database.update_book(connection, old_book, new_book)

database.display_books(connection)