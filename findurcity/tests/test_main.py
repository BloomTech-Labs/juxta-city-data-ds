import os
import psycopg2
import unittest
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PASS = os.getenv("DB_PASS")
DB_USER = os.getenv("DB_USER")

connection = psycopg2.connect(database=DB_NAME, user=DB_USER,
                              password=DB_PASS, host=DB_HOST, port="5432")
cursor = connection.cursor()

heart = pd.read_csv('./useful_datasets/heart_data.csv')


class SQLTestCase(unittest.TestCase):
    def test_heartQuery(self):
        query = "SELECT COUNT(*) FROM heart_disease;"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        self.assertEqual(result, heart.shape[0])


if __name__ == "__main__":
    unittest.main()
