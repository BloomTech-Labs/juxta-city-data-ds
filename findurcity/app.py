from flask import Flask, jsonify, render_template, request, json
from flask import redirect, url_for
from flask_cors import CORS
import pandas as pd
import glob
import os
from os import listdir
from dotenv import load_dotenv
import flask

load_dotenv()

filepath = os.getenv("repo_filepath")

city_df = pd.read_csv(filepath + 'findurcity/src/datasets/reference.csv')
photos = pd.read_csv(filepath + 'findurcity/src/extraneous_datasets/photos_big.csv')
economy = pd.read_csv(filepath + 'findurcity/src/datasets/economy_data.csv')
heart_disease = pd.read_csv(filepath + 'findurcity/src/datasets/heart_data.csv')
housing = pd.read_csv(filepath + 'findurcity/src/datasets/housing_data.csv')
jobs = pd.read_csv(filepath + 'findurcity/src/datasets/job_data.csv')
location = pd.read_csv(filepath + 'findurcity/src/datasets/location_data.csv')
people_stats = pd.read_csv(filepath + 'findurcity/src/datasets/people_stats_data.csv')
original = pd.read_csv(filepath + 'findurcity/src/extraneous_datasets/final_0427.csv') 

app = Flask(__name__)
CORS(app)

# when using 'Global', we need to have the variable exist in the namespace
state = None
pop = None
pop_ch = None
med_age = None
hdti = None
rti = None
pop_dense = None
col = None
drive = None
aqi = None
heart_health = None

@app.route("/")
def root():
    return ("hi")


@app.route('/name', methods=['GET', 'POST'])
def id_name_only():
    id = request.args['id']
    city = city_df[city_df['id'] == int(id)]
    output = city.to_dict('records')
    name = output[0]['City_Name']
    return jsonify(name)
    


@app.route('/about', methods=['GET', 'POST'])
def about_the_app():
      return render_template('about.html')


@app.route('/recommend', methods=['GET', 'POST'])
def desc_and_livability():
    def recommend_cities():
        global state
        state = request.args['state']
        global pop
        pop = request.args['population']
        global pop_ch
        pop_ch = request.args['population_change']
        global med_age
        med_age = request.args['median_age']
        global hdti
        hdti = request.args['house_cost']
        global rti
        rti = request.args['rental_cost']
        global pop_dense
        pop_dense = request.args['population_density']
        global col
        col = request.args['cost_of_living']
        global drive
        drive = request.args['average_commute']
        global aqi
        aqi = request.args['air_quality']


        state = list(state.split(', '))
        pop = int(pop)
        pop_ch = int(pop_ch)
        med_age = int(med_age)
        hdti = int(hdti)
        rti = int(rti)
        pop_dense = int(pop_dense)
        col = int(col)
        drive = int(drive)
        aqi = int(aqi)


        def filter_dfs():
            # Create "states" dataframe
            multiple = []

            if state != ['None']:
                for item in state:
                    frame = original[original['state'] == item]
                    multiple.append(frame)

                    states = pd.concat(multiple[0:], ignore_index=True)
            else:
                states = original

            # Create dataframe with filtered data
            if pop != 0:
                one = original[original['pop_rank'] == pop]
            else:
                one = original

            if pop_ch != 0:
                two = one[one['pop_ch_rank'] == pop_ch]
            else:
                two = one

            if med_age != 0:
                three = two[two['med_age_rank'] == med_age]
            else:
                three = two

            if hdti != 0:
                four = three[three['house_cost'] == hdti]
            else:
                four = three

            if rti != 0:
                five = four[four['rent_cost'] == rti]
            else:
                five = four

            if pop_dense != 0:
                six = five[five['pop_density'] == pop_dense]
            else:
                six = five

            if col != 0:
                seven = six[six['cli_index'] == col]
            else:
                seven = six

            if drive != 0:
                eight = seven[seven['avg_commute'] == drive]
            else:
                eight = seven

            if aqi != 0:
                nine = eight[eight['air'] == aqi]
            else:
                nine = eight

            # Create list of dataframes for use in case of no Top 5
            dataframes = [one, two, three, four, five, six, seven, eight, nine]

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

            return top_5, dataframes

        def generate_cities():
            # Check that precise matches are available. If not, get imprecise matches.
            shapes = []
            variables = [pop, pop_ch, med_age, hdti, rti, pop_dense, col, drive, aqi]

            output, dataframes = filter_dfs()

            if output != []:
                return output
            else:
                for dataframe in dataframes:
                    shape = dataframe.shape
                    shapes.append(shape[0])
                #Get the position number of the first dataframe that has zero rows
                val = next((index for index, value in enumerate(shapes) if value == 0), None)
                variables[val] = 0
                return variables

        def close_match():

            something = generate_cities()

            if len(something) > 5:

                # Variables get updated to reflect "something"
                global pop
                pop = something[0]
                global pop_ch
                pop_ch = something[1]
                global med_age
                med_age = something[2]
                global hdti
                hdti = something[3]
                global rti
                rti = something[4]
                global pop_dense
                pop_dense = something[5]
                global col
                col = something[6]
                global drive
                drive = something[7]
                global aqi
                aqi = something[8]

                # Run generate_cities again with updated variable values
                full_output = generate_cities()

                return full_output

            else:
                return something

        # Run close_match until a top 5 list is generated
        def get_results():
            info = close_match()
            if len(info) > 5:
                again = close_match()
                if len(again) > 5:
                    final = close_match()
                    return final
                else:
                    return again
            else:
                 return info

        return get_results()

    # Return descriptions, id, and city name
    top_cities = recommend_cities()

    place_here = []

    for x in top_cities:

        copy = pd.DataFrame()

        city = original[original['city'] == x]
        output = city.to_dict('records')
        data = output[0]

        # Basic
        id = data['id']
        name = data['City_Name']
        name_and_state = data['city']
        score = data['LivabilityScore']

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
        cold = data['Coldday_Count']
        hot = data['Hotday_Count']
        rain = data['Rainday_Count']

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
        copy['id'] = [f'{id}']
        copy['name'] = [f'{name}']
        copy['name_and_state'] = [f'{name_and_state}']
        copy['livability_score'] = f'{score}'
        copy['population_desc'] = f'The population is {pop} as of 2017, which is a {change}% {growth} since 2000. The population density is {density} people per square mile, which is {rise} than the optimal population density of 1304. Finally, the average resident age in {name} is {age} years old.'
        copy['economy_desc'] = f'In {name}, the median household income is ${houseinc}. This means that, per person in the city, the average annual income is ${capitainc}. {poverty}% of people live below the poverty line. The most common industries are the following: {industry}.'
        copy['climate_desc'] = f'{name} has an air quality score of {aqi} - remember, lower is better! Last year, there were {cold} cold days, {hot} hot days, and {rain} rainy days.'
        copy['living_cost_desc'] = f"On a national scale, {name}'s cost of living is relatively {cli_rel}, with a score of {cli}. The median home value is ${house}, with a housing debt to income ratio of {hdti}. That includes the cost of property taxes, which is ${tax} on average. If you're a renter, you can expect a median cost of ${rent}, and the rent to income ratio is {rti}. Last but not least to consider, the average commute time is {drive} minutes."
        
        output2 = copy.to_dict('records')
        descriptions = output2[0]

        place_here.append(descriptions)

    return jsonify(place_here)


@app.route('/data', methods=['GET', 'POST'])
def all_data():
    name = request.args['data']
    city = original[original['city'] == name]
    output = city.to_dict('records')
    data = output[0]
    return jsonify(data)


@app.route('/top25', methods=['GET', 'POST'])
def top_25_data():
    output = photos.to_dict('records')
    return jsonify(output)


@app.route('/search', methods=['GET', 'POST'])
def search_names():
    input = request.args['search']
    input = input.title()
    cities = city_df[city_df['City_Name'].str.startswith(input)]

    ids = []
    for index, row in cities.iterrows():
        ids.append(index)

    output = cities.to_dict('records')

    length = len(ids)
    all = []
    for item in range(length):
        city = output[item]['City_Name']
        all.append(city)

    return jsonify(all)

if __name__ == '__main__':
    app.run(debug=True)

