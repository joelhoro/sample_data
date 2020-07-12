import unittest
from sample_data import countries, airbnb

class TestFiles(unittest.TestCase):

    def test_countries(self):
        print("Testing countries")
        df = countries()
        print(df.head())
        self.assertEqual(len(df),279,"Countries dataframe has the wrong size")

    def test_airbnb(self):
        print("Testing airbnb")
        df = airbnb()
        print(df.head())
        
        for key in ['Manhattan','Queens','Brooklyn']:
            rows = df[df['Neighbourhood '] == key]
            self.assertGreater(len(rows),0, f"No data for {key}")    

if __name__ == '__main__':
    unittest.main()