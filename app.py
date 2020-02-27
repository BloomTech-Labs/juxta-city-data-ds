from flask import Flask, jsonify, request, json
import pandas as pd

df = pd.read_csv('./JuxtaCityData3.csv')

app = Flask(__name__)


@app.route("/")
def root():
    return ("hi")


# Returns city name given a city id
@app.route('/name', methods=['GET', 'POST'])
def id_name_only():
    id = request.args['id']
    city = df[df['id'] == int(id)]
    output = city.to_dict('records')
    name = output[0]['city']
    return jsonify(name)


# Returns all data given a city name and state (format: City, State)
@app.route('/data', methods=['GET', 'POST'])
def all_data():
    name = request.args['city']
    city = df[df['city'] == name]
    output = city.to_dict('records')
    data = output[0]
    return jsonify(data)


# Returns list of cities that start with given characters
@app.route('/search', methods=['GET', 'POST'])
def search_names():
    input = request.args['search']
    input = input.title()
    cities = df[df['city'].str.startswith(input)]

    ids = []
    for index, row in cities.iterrows():
        ids.append(index)

    output = cities.to_dict('records')

    length = len(ids)
    all = []
    for item in range(length):
        city = output[item]['city']
        all.append(city)

    return jsonify(all)

if __name__ == "__main__":
    app.run()
