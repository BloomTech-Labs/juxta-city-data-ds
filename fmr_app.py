from flask import Flask, jsonify, request, json, render_template
from flask_cors import CORS
import pandas as pd

# This dataframe contains heart disease data and COVID-19
# data by county (by city is too difficult as there are cities,
# towns and boroughs and data like that is not available.
# Dataframe column[0] is an unnamed column that resulted from
# putting the dataframe into a CSV with no specified index.

heart = pd.read_csv('./useful_datasets/heart_data.csv')
economy = pd.read_csv('./useful_datasets/economy_data.csv')
housing = pd.read_csv('./useful_datasets/housing_data.csv')
job = pd.read_csv('./useful_datasets/job_data.csv')
location = pd.read_csv('./useful_datasets/location_data.csv')
people = pd.read_csv('./useful_datasets/people_stats_data.csv')
reference = pd.read_csv('./useful_datasets/reference.csv')
# print(unique_city_health_stats.shape)
# print(unique_city_health_stats.head())

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('homepage.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/team")
def team():
    return render_template('team.html')


@app.route("/data", methods=['GET', 'POST'])
def heart_disease():
    state = request.args['state']
    name = heart[heart['state'] == state]
    output = name.to_dict('records')
    county = [output[i]['county'] for i in list(range(len(output)))]
    stats = [output[i]['Heart Disease Value'] for
             i in list(range(len(output)))]
    return jsonify(county, stats)

# TODO
# def economy():
#     return jsonify(...)
# def housing():
#     return jsonify(...)
# def job():
#     return jsonify(...)
# def location():
#     return jsonify(...)
# def people():
#     return jsonify(...)
# def reference():
#     return jsonify(...)
