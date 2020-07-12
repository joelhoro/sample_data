import unittest
from sample_data import countries

class TestStringMethods(unittest.TestCase):

    def test_countries(self):
        #self.assertEqual('foo'.upper(), 'FOO')
        print(countries())

if __name__ == '__main__':
    unittest.main()