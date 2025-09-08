#Terminal:
#python "/Users/aitor/Documents/Python/Python/Section25 - Advance Exercises/125coches.py" "/Users/aitor/Documents/Python/Python/Section25 - Advance Exercises/coches.zip"
#python 125coches.py coches.zip

from multiprocessing import connection
import sys
from uu import Error
from zipfile import ZipFile
import pandas as pd
import sqlite3
from os import remove

def unzip_file(name):
    with ZipFile(name, 'r') as zip:
        zip.extractall()

def read_data(name):
    data = pd.read_csv(name, sep=';')
    return data

def insert_car_table(connection, car):
    cursor = connection.cursor()
    cursor.execute('INSERT INTO cars(marca,modelo,combustible,transmision,estado,matriculacion,kilometraje,potencia,precio) VALUES (?,?,?,?,?,?,?,?,?)', car)
    connection.commit()

def record_cars(connection, data):
    for row in data.itertuples():
        marca = row[1]
        modelo = row[2]
        combustible = row[3]
        transmision = row[4]
        estado = row[5]
        matriculacion = row[6]
        kilometraje = row[7]
        potencia = row[8]
        precio = row[9]

        car = (marca,modelo,combustible,transmision,estado,matriculacion,kilometraje,potencia,precio)

        insert_car_table(connection,car)

database = 'cars.bd'

def create_connection_bd():
    try:
        connection = sqlite3.connect(database)
        return connection
    except Error:
        print (Error)

def create_cartable(connection):
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE cars(marca TEXT, modelo TEXT, combustible TEXT, transmision TEXT,estado TEXT, matriculacion TEXT, kilometraje INTEGER, potencia REAL, precio REAL)')
    connection.commit()

def remove_database():
    try:
        remove(database)
    except FileNotFoundError:
        pass

def query_car(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM cars LIMIT 20')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def number_of_cars_table(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM cars')
    data = cursor.fetchall()
    number = data[0][0]
    return number

def sum_price(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT SUM(precio) FROM cars')
    data = cursor.fetchall()
    number = data[0][0]
    return number

def cheapest_car(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT marca, modelo, MIN(precio) FROM cars')
    data = cursor.fetchall()
    return data

def average_price_brand(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT marca, AVG(precio) FROM cars GROUP BY marca')
    data = cursor.fetchall()
    return data

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Error. Incorrect number of parameters. FileName might be missing")

    else:
        filename = sys.argv[1]


    remove_database()

    unzip_file(filename)

    data = read_data(filename)
    print (data)

    connection = create_connection_bd()

    create_cartable(connection)

    record_cars(connection, data)

    print("\n Quering Data from Table")
    query_car(connection)

    data = number_of_cars_table(connection)
    print("\n The number of cars is {}".format(data))

    number = sum_price(connection)
    money = '{:,}'.format(number).replace(',','.')
    print ("\n The sum of the car prices is {}".format(money))

    data = cheapest_car(connection)
    marca = data[0][0]
    modelo = data[0][1]
    precio = data[0][2]
    print (f"\n The cheapest car is {marca}, {modelo}, {precio}")


    print ("\n Average Price per brand \n")
    data = average_price_brand(connection)
    for dat in data:
        marca = dat[0]
        precio = dat[1]
        print (marca,round(precio,2))
