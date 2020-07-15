from flask import Flask, jsonify, render_template, request, json
from flask import redirect, url_for
from flask_cors import CORS
import pandas as pd
import glob
import os
from os import listdir

city_df = pd.read_csv('./useful_datasets/reference.csv')
photos = pd.read_csv('./notebooks_in_use/extraneous_datasets/photos_big.csv')
economy = pd.read_csv('./useful_datasets/economy_data.csv')
heart_disease = pd.read_csv('./useful_datasets/heart_data.csv')
housing = pd.read_csv('./useful_datasets/housing_data.csv')
jobs = pd.read_csv('./useful_datasets/job_data.csv')
location = pd.read_csv('./useful_datasets/location_data.csv')
people_stats = pd.read_csv('./useful_datasets/people_stats_data.csv')
original = pd.read_csv('./notebooks_in_use/extraneous_datasets/final_0427.csv') 

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
def name():
    city_list = city_df['City_Name'].to_list()
    return jsonify(city_list)


@app.route('/about', methods=['GET', 'POST'])
def about_the_app():
      return render_template('about.html')


@app.route('/recommend', methods=['GET', 'POST'])
def desc_and_livability():
    def recommend_cities():

        def filter_dfs():
            # Create states dataframe
            multiple = []

            states = city_df['code']

            # Create people stats dataframe
            if pop != 0:
                one = people_stats[people_stats['population'] == pop]
            else:
                one = city_df

            if pop_ch != 0:
                two = one[one['population_change'] == pop_ch]
            else:
                two = one

            if med_age != 0:
                three = two[two['Median_Age'] == med_age]
            else:
                three = two

            if pop_dense != 0:
                four = three[three['Population_Density'] == pop_dense]
            else:
                four = three

            if hdti != 0:
                five = housing[housing['Median_House_Value'] == hdti]
            else:
                five = four

            if rti != 0:
                six = five[five['Median_Rent'] == rti]
            else:
                six = five

            if col != 0:
                seven = six[six['Cost_of_Living_Index'] == col]
            else:
                seven = six

            if drive != 0:
                eight = original[original['avg_commute'] == drive]
            else:
                eight = seven

            if aqi != 0:
                nine = eight[eight['air'] == aqi]
            else:
                nine = eight
                    
            if heart_health != 0:
                ten = heart_disease[heart_disease['scaled_heart_disease_deaths'] == heart_health]
            else:
                ten = nine

            # Create list of dataframes for use in case of no Top 5
            dataframes = [one, two, three, four, five, six, seven, eight, nine, ten]

            # Merge dataframes to get fully filtered result
            all = pd.merge(ten, states, on='id', how='inner')

            # Sort by livability score and convert to a dictionary
            sort = all.sort_values(by='LivabilityScore_y', ascending=False)
            dict = sort.to_dict('records')

            # Allow less than 5 results if necessary
            all_cities = []
            for item in range(len(dict)):
                all_cities.append(dict[item]['id'])

            top_5 = all_cities[0:5]

            return top_5, dataframes

        def generate_cities():
            # Check that precise matches are available. If not, get imprecise matches.
            shapes = []
            variables = [pop, pop_ch, pop_dense, med_age, hdti, rti, col, drive, aqi, heart_health]

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
                global pop_dense
                pop_dense = something[2]
                global hdti
                hdti = something[3]
                global rti
                rti = something[4]
                global med_age
                med_age = something[5]
                global col
                col = something[6]
                global drive                
                drive = something[7]
                global aqi
                aqi = something[8]
                global heart_health
                heart_health = something[9]

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
    top_cities = city_df

    place_here = []

    for cities in top_cities:

        copy = pd.DataFrame()
        city = city_df[city_df['City_Name'] == cities]
        data = city_df

        # Basic
        id = data['id']
        name = data['City_Name']
        name_and_state = original['city']
        score = original['LivabilityScore']

        # Population
        pop = people_stats['population']
        change = people_stats['population_change']
        density = people_stats['Population_Density']
        age = people_stats['Median_Age']

        # Economy
        houseinc = economy['Median_Income']
        capitainc = economy['per_capita_Income']
        poverty = economy['Percent_below_Poverty']
        industry = jobs['Most_Common_Industries']

        # Climate
        aqi = original['air']
        cold = original['Coldday_Count']
        hot = original['Hotday_Count']
        rain = original['Rainday_Count']

        # Cost of Living
        cli = housing['Cost_of_Living_Index']
        house = housing['Median_House_Value']
        rent = housing['Median_Rent']
        tax = housing['Property_taxes']
        drive = original['avg_commute']

        # Heart Disease information
        heart_cases = heart_disease['normalized_heart_disease']
        heart_deaths = heart_disease['scaled_heart_disease_deaths']

        # When relative words are needed
        if change.size < 0:
            growth = 'decrease'
        else:
            growth = 'increase'

        if density.size < 1304:
            rise = 'lower'
        elif density == 1304:
            rise = 'equal to'
        else:
            rise = 'higher'

        if cli.size < 51:
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
        copy['heart_disease_desc'] = f"{name} has {heart_deaths}% cases of heart disease within the city. This resulted in {heart_deaths} Heart Disease related deaths."

        output2 = copy.to_dict('records')
        descriptions = output2[0]

        place_here.append(descriptions)
    return jsonify(place_here)


@app.route('/data', methods=['GET', 'POST'])
def all_data():
    
    df1 = city_df
    df2 = people_stats
    df3 = economy
    df4 = heart_disease
    df5 = jobs
    df6 = housing
    df7 = location
    df8 = original
    merge1 = pd.merge(df1, df2, how = 'left', on = 'id')
    merge2 = pd.merge(merge1, df4, how = 'left', on = 'id')
    merge3 = pd.merge(merge2, df4, how = 'left', on = 'id')
    merge4 = pd.merge(merge3, df5, how = 'left', on = 'id')
    merge5 = pd.merge(merge4, df6, how = 'left', on = 'id')
    merge6 = pd.merge(merge5, df7, how = 'left', on = 'id')
    data = pd.merge(merge6, df8, how = 'left', on = 'id')

    # Basic
    id = city_df['id']
    name = city_df['City_Name']
    name_and_state = original['city']
    score = original['LivabilityScore']

    # Population
    pop = people_stats['population']
    change = people_stats['population_change']
    density = people_stats['Population_Density']
    age = people_stats['Median_Age']

    # Economy
    houseinc = economy['Median_Income']
    capitainc = economy['per_capita_Income']
    poverty = economy['Percent_below_Poverty']
    industry = jobs['Most_Common_Industries']

    # Climate
    aqi = original['air']
    cold = original['Coldday_Count']
    hot = original['Hotday_Count']
    rain = original['Rainday_Count']

    # Cost of Living
    cli = housing['Cost_of_Living_Index']
    house = housing['Median_House_Value']
    rent = housing['Median_Rent']
    tax = housing['Property_taxes']
    drive = original['avg_commute']

    # Heart Disease information
    heart_cases = heart_disease['normalized_heart_disease']
    heart_deaths = heart_disease['scaled_heart_disease_deaths']    

    # When relative words are needed
    if change.size < 0:
        growth = 'decrease'
    else:
        growth = 'increase'

    if density.size < 1304:
        rise = 'lower'
    elif density.size == 1304:
        rise = 'equal to'
    else:
        rise = 'higher'

    if cli.size < 51:
        cli_rel = 'low'
    else:
        cli_rel = 'high'

    # Descriptions
    data['population_desc'] = f'The population is {pop} as of 2017, which is a {change}% {growth} since 2000. The population density is {density} people per square mile, which is {rise} than the optimal population density of 1304. Finally, the average resident age in {name} is {age} years old.'
    data['economy_desc'] = f'In {name}, the median household income is ${houseinc}. This means that, per person in the city, the average annual income is ${capitainc}. {poverty}% of people live below the poverty line. The most common industries are the following: {industry}.'
    data['climate_desc'] = f'{name} has an air quality score of {aqi} - remember, lower is better! Last year, there were {cold} cold days, {hot} hot days, and {rain} rainy days.'
    data['living_cost_desc'] = f"On a national scale, {name}'s cost of living is relatively {cli_rel}, with a score of {cli}. The median home value is ${house}, with a housing debt to income ratio of {hdti}. That includes the cost of property taxes, which is ${tax} on average. If you're a renter, you can expect a median cost of ${rent}, and the rent to income ratio is {rti}. Last but not least to consider, the average commute time is {drive} minutes."
    data['heart_disease_desc'] = f"{name} has {heart_deaths}% cases of heart disease within the city. This resulted in {heart_deaths} Heart Disease related deaths."

    everything = data.to_json()

    return jsonify(everything)


@app.route('/top25', methods=['GET', 'POST'])
def top_25_data():
    output = photos.to_dict('records')
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)

