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

# Read in the CSV files from GitHub (https://github.com/Lambda-School-Labs/juxta-city-data-ds/tree/heart-disease-data/useful_datasets)
heart = pd.read_csv('./useful_datasets/heart_data.csv')
economy = pd.read_csv('./useful_datasets/economy_data.csv')
housing = pd.read_csv('./useful_datasets/housing_data.csv')
job = pd.read_csv('./useful_datasets/job_data.csv')
location = pd.read_csv('./useful_datasets/location_data.csv')
people = pd.read_csv('./useful_datasets/people_stats_data.csv')
reference = pd.read_csv('./useful_datasets/reference.csv')

# Connect to PostgreSQL Database
connection = psycopg2.connect(database=DB_NAME, user=DB_USER,
                              password=DB_PASS, host=DB_HOST, port="5432")
cursor = connection.cursor()

# This block of code is needed so psycopg2 can register numpy types
# Source: https://rehalcon.blogspot.com/2010/03/sqlalchemy-programmingerror-cant-adapt.html


def adapt_numpy_float64(numpy_float64):
    return AsIs(numpy_float64)


def adapt_numpy_int64(numpy_int64):
    return AsIs(numpy_int64)


register_adapter(numpy.float64, adapt_numpy_float64)
register_adapter(numpy.int64, adapt_numpy_int64)

# Create the schema for the table
heart_schema = '''
DROP TABLE IF EXISTS heart_disease;
CREATE TABLE IF NOT EXISTS heart_disease (
    id INT PRIMARY KEY,
    scaled_heart_disease_deaths FLOAT,
    normalized_heart_disease FLOAT
);
'''

economy_schema = '''
DROP TABLE IF EXISTS economy;
CREATE TABLE IF NOT EXISTS economy (
    id INT PRIMARY KEY,
    Median_Income FLOAT,
    per_capita_Income FLOAT,
    Percent_below_Poverty FLOAT
);
'''

housing_schema = '''
DROP TABLE IF EXISTS housing;
CREATE TABLE IF NOT EXISTS housing (
    id INT PRIMARY KEY,
    Median_House_Value FLOAT,
    Median_Rent FLOAT,
    Cost_of_Living_Index FLOAT,
    Property_taxes FLOAT
);
'''

job_schema = '''
DROP TABLE IF EXISTS job;
CREATE TABLE IF NOT EXISTS job (
    id INT PRIMARY KEY,
    Unemployment_rate FLOAT,
    Most_Common_Industries VARCHAR(350),
    Average_Commute_Time FLOAT
);
'''

location_schema = '''
DROP TABLE IF EXISTS location;
CREATE TABLE IF NOT EXISTS location (
    id INT PRIMARY KEY,
    Latitude FLOAT,
    Longitude FLOAT
);
'''

people_schema = '''
DROP TABLE IF EXISTS people;
CREATE TABLE IF NOT EXISTS people (
    id INT PRIMARY KEY,
    Median_Age FLOAT,
    population FLOAT,
    population_change FLOAT,
    Population_Density FLOAT,
    popden_norm FLOAT
);
'''

reference_schema = '''
DROP TABLE IF EXISTS reference;
CREATE TABLE IF NOT EXISTS reference (
    id INT PRIMARY KEY,
    code VARCHAR(2),
    fips INT,
    county VARCHAR(16),
    City_Name VARCHAR(22)
);
'''

# Execute the table schemata queries
cursor.execute(heart_schema)
cursor.execute(economy_schema)
cursor.execute(housing_schema)
cursor.execute(job_schema)
cursor.execute(location_schema)
cursor.execute(people_schema)
cursor.execute(reference_schema)

# Turn the Dataframes rows into iterable tuples
heart_values = list(heart.to_records(index=False))
economy_values = list(economy.to_records(index=False))
housing_values = list(housing.to_records(index=False))
job_values = list(job.to_records(index=False))
location_values = list(location.to_records(index=False))
people_values = list(people.to_records(index=False))
reference_values = list(reference.to_records(index=False))

# Insert the data into PostgreSQL Database
heart_insert = '''
INSERT INTO heart_disease
    (id, scaled_heart_disease_deaths, normalized_heart_disease) VALUES %s
'''

economy_insert = '''
INSERT INTO economy
    (id, Median_Income, per_capita_Income, Percent_below_Poverty) VALUES %s
'''

housing_insert = '''
INSERT INTO housing
    (id, Median_House_Value, Median_Rent, Cost_of_Living_Index, Property_taxes) VALUES %s
'''

job_insert = '''
INSERT INTO job
    (id, Unemployment_rate, Most_Common_Industries, Average_Commute_Time) VALUES %s
'''

location_insert = '''
INSERT INTO location
    (id, Latitude, Longitude) VALUES %s
'''

people_insert = '''
INSERT INTO people
    (id, Median_Age, population, population_change, Population_Density, popden_norm) VALUES %s
'''

reference_insert = '''
INSERT INTO reference
    (id, code, fips, county, City_Name) VALUES %s
'''

# Execute the insert queries with list of tuples
execute_values(cursor, heart_insert, heart_values)
execute_values(cursor, economy_insert, economy_values)
execute_values(cursor, housing_insert, housing_values)
execute_values(cursor, job_insert, job_values)
execute_values(cursor, location_insert, location_values)
execute_values(cursor, people_insert, people_values)
execute_values(cursor, reference_insert, reference_values)

# Commit changes to the Postgres instance
connection.commit()
