import os
import unittest
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

data_path = os.getenv("repo_filepath") + "findurcity/src/datasets/"

class TestDataShape(unittest.TestCase):

    def test_covid(self):
        covid = pd.read_csv(data_path + "covid_data.csv")
        data = covid.to_records(index=True)
        self.assertEqual(len(data[0]), 13)

    def test_heart(self):
        heart_disease = pd.read_csv(data_path + "heart_data.csv")
        data = heart_disease.to_records(index=True)
        self.assertEqual(len(data[0]), 4)


if __name__ == "__main__":
    unittest.main()
