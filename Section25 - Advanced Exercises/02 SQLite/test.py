import unittest
from cars125 import *

filename = 'test.csv'
class number_of_cars_table(unittest.TestCase):
    def test(self):

        remove_database()

        read_data(filename)

        connection = create_connection_bd()

        create_cartable(connection)

        record_cars(connection, data)