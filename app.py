from flask import Flask, jsonify, request, json
from flask_cors import CORS
import pandas as pd

df = pd.read_csv('./final_0318.csv')
photos = pd.read_csv('./photos_big.csv')

app = Flask(__name__)
CORS(app)


@app.route("/")
def root():
    return ("hi")


# Returns city name given a city id
# Route structure: https://junta-test.herokuapp.com/name?id= [0-7127]
@app.route('/name', methods=['GET', 'POST'])
def id_name_only():
    id = request.args['id']
    city = df[df['id'] == int(id)]
    output = city.to_dict('records')
    name = output[0]['city']
    return jsonify(name)


# Returns only data for top 25 cities
# Route structure: https://junta-test.herokuapp.com/top25
@app.route('/top25', methods=['GET', 'POST'])
def top_25_data():
    output = photos.to_dict('records')
    return jsonify(output)


# Returns up to top 5 cities based on filters and livability score
'''
Route structure: http://junta-test.herokuapp.com/recommend?state=None&
population=0&population_change=0&median_age=0&house_cost=0&rental_cost=0&
population_density=0&cost_of_living=0&average_commute=0&air_quality=0
[adjust values as appropriate]
'''
@app.route('/recommend', methods=['GET', 'POST'])
def recommend_cities():
    state = request.args['state']
    pop = request.args['population']
    pop_ch = request.args['population_change']
    med_age = request.args['median_age']
    hdti = request.args['house_cost']
    rti = request.args['rental_cost']
    pop_dense = request.args['population_density']
    col = request.args['cost_of_living']
    drive = request.args['average_commute']
    aqi = request.args['air_quality']

    # Create "states" dataframe
    multiple = []

    state = list(state.split(' '))

    if state != ['None']:
        for item in state:
            frame = df[df['state'] == item]
            multiple.append(frame)

            states = pd.concat(multiple[0:], ignore_index=True)
    else:
        states = df

    # Create dataframe with filtered data
    if pop != '0':
        one = df[df['pop_rank'] == int(pop)]
    else:
        one = df

    if pop_ch != '0':
        two = one[one['pop_ch_rank'] == int(pop_ch)]
    else:
        two = one

    if med_age != '0':
        three = two[two['med_age_rank'] == int(med_age)]
    else:
        three = two

    if hdti != '0':
        four = three[three['house_cost'] == int(hdti)]
    else:
        four = three

    if rti != '0':
        five = four[four['rent_cost'] == int(rti)]
    else:
        five = four

    if pop_dense != '0':
        six = five[five['pop_density'] == int(pop_dense)]
    else:
        six = five

    if col != '0':
        seven = six[six['cli_index'] == int(col)]
    else:
        seven = six

    if drive != '0':
        eight = seven[seven['avg_commute'] == int(drive)]
    else:
        eight = seven

    if aqi != '0':
        nine = eight[eight['air'] == int(aqi)]
    else:
        nine = eight

    # Merge dataframes to get fully filtered result
    all = pd.merge(nine, states, on='city', how='inner')

    # Sort by livability score and convert to a dictionary
    sort = all.sort_values(by='LivabilityScore_y', ascending=False)
    dict = sort.to_dict('records')

    # Allow less than 5 results if necessary
    all_cities = []
    for item in range(len(dict)):
        all_cities.append(dict[item]['city'])

    top_5 = all_cities[0:5]

    return jsonify(top_5)


# Returns all data given a city name and state (format: City, State)
# Route structure: https://junta-test.herokuapp.com/data?city= [City, State]
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
    rti = data['RTI']
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

    # Descriptions
    data['population_desc'] = f'The population is {pop} as of 2017, which is a {change}% {growth} since 2000. The population density is {density} people per square mile, which is {rise} than the optimal population density of 1304. Finally, the average resident age in {name} is {age} years old.'
    data['economy_desc'] = f'In {name}, the median household income is ${houseinc}. This means that, per person in the city, the average annual income is ${capitainc}. {poverty}% of people live below the poverty line. The most common industries are the following: {industry}.'
    data['climate_desc'] = f'{name} has an air quality score of {aqi} - remember, lower is better! The average weather is {weather}.'
    data['living_cost_desc'] = f"On a national scale, {name}'s cost of living is relatively {cli_rel}, with a score of {cli}. The median home value is ${house}, with a housing debt to income ratio of {hdti}. That includes the cost of property taxes, which is ${tax} on average. If you're a renter, you can expect a median cost of ${rent}, and the rent to income ratio is {rti}. Last but not least to consider, the average commute time is {drive} minutes."

    everything = data

    return jsonify(everything)


# Returns list of cities that start with given characters
# Route structure: https://junta-test.herokuapp.com/search?search= [Any characters]
@app.route('/search', methods=['GET', 'POST'])
def search_names():
    input = request.args['search']
    input = input.title()
    cities = df[df['city'].str.startswith(input)]

    ids = []
    for index, row in cities.iterrows():
        ids.append(index)

    output = cities.to_dict('records')

    all = []
    for item in range(len(ids)):
        city = output[item]['city']
        all.append(city)

    return jsonify(all)

if __name__ == "__main__":
    app.run()
