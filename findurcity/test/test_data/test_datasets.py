import os
import unittest
import pandas as pd
from datetime import date, timedelta
from dotenv import load_dotenv

load_dotenv()

FILEPATH =  os.getenv("repo_filepath") + "findurcity/src/datasets/"

yesterday = (date.today() - timedelta(days=1)).strftime("%m-%d-%Y")


class TestDataShape(unittest.TestCase):

    def test_covid(self):
        covid = pd.read_csv(FILEPATH + f"{yesterday}.csv")
        data = covid.to_records(index=True)
        self.assertEqual(len(data[0]), 14)

    def test_heart(self):
        heart_disease = pd.read_csv(FILEPATH + "heart_data.csv")
        data = heart_disease.to_records(index=True)
        self.assertEqual(len(data[0]), 4)


if __name__ == "__main__":
    unittest.main()
