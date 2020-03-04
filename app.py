from flask import Flask, jsonify, request, json
from flask_cors import CORS
import pandas as pd

df = pd.read_csv('./recleanedcitydata.csv')

app = Flask(__name__)
CORS(app)


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

    name = data['City_Name']

    # Population
    pop = data['population']
    change = data['population_change']
    density = data['Population_Density']
    age = data['Median_Age']
    # Economy
    houseinc = data['Median_Income']
    capitainc = data['per_capita_Income']
    poverty = data['Percent_below_Poverty']
    industry = data['Most_Common_Industries']
    # Climate
    aqi = data['AQI']
    weather = 'to be added'
    # Cost of Living
    cli = data['Cost_of_Living_Index']
    house = data['Median_House_Value']
    hdti = data['HDTI']
    tax = data['Property_taxes']
    rent = data['Median_Rent']
    rti = data ['RTI']
    drive = data['Average_Commute_Time']

    # When relative words are needed
    if change < 0:
        growth = 'decrease'
    else:
        growth = 'increase'

    if density < 1304:
        rise = 'lower'
    elif density == 1304:
        rise = 'equal to'
    else:
        rise = 'higher'

    if cli < 51:
        cli_rel = 'low'
    else:
        cli_rel = 'high'

    population = f'The population is {pop} as of 2017, which is a {change}% {growth} since 2000. The population density is {density} people per square mile, which is {rise} than the optimal population density of 1304. Finally, the average resident age in {name} is {age} years old.'
    economy = f'In {name}, the median household income is ${houseinc}. This means that, per person in the city, the average annual income is ${capitainc}. {poverty}% of people live below the poverty line. The most common industries are the following: {industry}.'
    climate = f'{name} has an air quality score of {aqi} - remember, lower is better! The average weather is {weather}.'
    living_cost = f"On a national scale, {name}'s cost of living is relatively {cli_rel}, with a score of {cli}. The median home value is ${house}, with a housing debt to income ratio of {hdti}. That includes the cost of property taxes, which is ${tax} on average. If you're a renter, you can expect a median cost of ${rent}, and the rent to income ratio is {rti}. Last but not least to consider, the average commute time is {drive} minutes."

    return jsonify(data, population, economy, climate, living_cost)


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
