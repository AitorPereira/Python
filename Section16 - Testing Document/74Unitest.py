#Unitest - It is a framework to test the code.

def multiply(x, y):
    return x * y

result = multiply(3, 4)
print(result) 

import unittest

class tests(unittest.TestCase):

    def test(self):
        self.assertEqual(multiply(2,4),8)
        self.assertEqual(multiply(2,4),9)

if __name__ == '__main__':
    unittest.main()