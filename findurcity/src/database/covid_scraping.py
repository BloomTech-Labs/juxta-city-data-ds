import pandas as pd
import numpy as np
from datetime import date, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

FILEPATH = os.getenv("repo_filepath") + "findurcity/src/datasets/"

# Grab yesterday's date as MM-DD-YYYY

yesterday = (date.today() - timedelta(days=1)).strftime("%m-%d-%Y")

# GitHub raw data URL for JHU's COVID-19 repository

jhu_filepath = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{yesterday}.csv'

# Base DataFrame for COVID-19 data

base_covid = pd.read_csv(jhu_filepath)


# Necessary functions

def get_date(array):
    '''Returns a string of the first ten characters'''
    return array[:10]

# Data Cleaning
covid_fips = base_covid.copy()
covid_fips['FIPS'] = covid_fips['FIPS'].replace(np.NaN, -1).astype(int)
covid1 = covid_fips[covid_fips['FIPS'] >= 0]
covid1 = covid1[~covid1['Lat'].isna() == True]
covid1['Date'] = covid1['Last_Update'].apply(get_date)
covid1['Active'] = covid1['Active'].fillna(-1).astype(int)
covid1 = covid1.rename(columns={'Admin2': 'County', 'Province_State': 'State', 'Long_': 'Lon'})
covid1['County'] = covid1['County'].fillna('Non-Contiguous 50 States')
covid1 = covid1.fillna(-1)

# Filter into useable dataset
covid19_cleaned = covid1[['FIPS', 'County', 'State', 'Lat', 'Lon', 'Confirmed', 'Deaths',
                          'Recovered', 'Active', 'Incidence_Rate', 'Case-Fatality_Ratio', 'Date']]

# covid19_cleaned.to_csv(FILEPATH + f"{yesterday}.csv")
