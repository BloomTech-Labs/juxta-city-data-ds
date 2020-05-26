import os
import psycopg2
from psycopg2.extras import execute_values
from psycopg2.extensions import register_adapter, AsIs
from dotenv import load_dotenv
import pandas as pd
import numpy

# Allows access to local .env file (will be GitIgnored)
load_dotenv()

# Bring in ElephantSQL Database keys
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PASS = os.getenv("DB_PASS")
DB_USER = os.getenv("DB_USER")

# Connect to PostgreSQL Database
connection = psycopg2.connect(database=DB_NAME, user=DB_USER, 
                              password=DB_PASS, host=DB_HOST, port="5432")
cursor = connection.cursor()

# This block of code is needed so psycopg2 can register numpy types
# Source: https://rehalcon.blogspot.com/2010/03/sqlalchemy-programmingerror-cant-adapt.html
def addapt_numpy_float64(numpy_float64):
  return AsIs(numpy_float64)
register_adapter(numpy.float64, addapt_numpy_float64)

# Create the schema for the table
table_schema = '''
DROP TABLE IF EXISTS heart_disease;
CREATE TABLE IF NOT EXISTS heart_disease (
    id SERIAL PRIMARY KEY,
    Values FLOAT,
    county VARCHAR(20) NOT NULL,
    state VARCHAR(2) NOT NULL,
    city VARCHAR(40) NOT NULL
);
'''

# Execute the table schema query
# cursor.execute(table_schema)

# Read in the csv from GitHub (or from parallel directory)
df = pd.read_csv('https://raw.githubusercontent.com/JamesBarciz/juxta-city-data-ds/master/city_county_state.csv')
# Remove the first column (extraneous ID)
df = df.drop(columns='Unnamed: 0')

df['Value'] = df['Value'].astype('float64')

# Turn the Dataframe rows into iterable tuples
rows_to_insert = list(df.to_records(index=False))

# Insert the data into PostgreSQL Database
table_insert = '''
INSERT INTO heart_disease
    (Values, county, state, city) VALUES %s
'''

# Execute the table insert query with list of tuples
# execute_values(cursor, table_insert, rows_to_insert)

# Commit changes to the Postgres instance
# connection.commit()
