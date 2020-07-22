import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

absolute_path = os.getenv('repo_filepath')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB = os.getenv('DB')

engine = create_engine(f'{DB}://{DB_NAME}:{DB_PASS}@{DB_HOST}:5432/{DB_USER}')

df = pd.read_csv(absolute_path + 'findurcity/src/datasets/covid_data.csv')

# df.to_sql('covid', con=engine)
