import unittest
from sample_data import countries

class TestStringMethods(unittest.TestCase):

    def test_countries(self):
        df = countries()
        self.assertEqual(len(df),279,"Countries dataframe has the wrong size")

if __name__ == '__main__':
    unittest.main()