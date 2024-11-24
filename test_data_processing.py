import unittest
from modules.data_processing import load_data, clean_data
import pandas as pd

class TestDataProcessing(unittest.TestCase):

    def test_load_data(self):
        # Test to ensure data is loaded properly
        df = load_data('data/sample_data.csv')
        self.assertIsNotNone(df)  # Check if data is not None
        self.assertIsInstance(df, pd.DataFrame)  # Check if the data is loaded as a pandas DataFrame
        self.assertGreater(len(df), 0)  # Ensure the data has at least one row

    def test_clean_data(self):
        # Create a sample dataframe with some missing values and duplicates for testing
        data = {
            'A': [1, 2, 2, None],
            'B': [4, None, 6, 8],
            'C': [7, 8, 8, 10]
        }
        df = pd.DataFrame(data)

        # Clean the data
        cleaned_df = clean_data(df)

        # Test if duplicates are removed and missing values are filled
        self.assertFalse(cleaned_df.isnull().values.any(), "There are still missing values after cleaning.")
        self.assertEqual(len(cleaned_df), 3, "Duplicate rows were not removed correctly.")
        self.assertTrue((cleaned_df.loc[0] == [1.0, 4.0, 7.0]).all(), "Forward/backward filling didn't work as expected.")

if __name__ == "__main__":
    unittest.main()
