import requests
from bs4 import BeautifulSoup # note that the import package command is `bs4`
import csv
import numpy as np
import os.path

urls = []

cities = [# Alabama
          'Birmingham-Alabama', 'Montgomery-Alabama', 'Mobile-Alabama',
          'Huntsville-Alabama',
          # # Arkansas
          'Little-Rock-Arkansas',
          # # Arizona
          'Tucson-Arizona', 'Mesa-Arizona', 'Chandler-Arizona',
          'Gilbert-Arizona', 'Glendale-Arizona', 'Scottsdale-Arizona',
          'Deer-Valley-Arizona', 'Tempe-Arizona', 'Peoria-Arizona',
          'Surprise-Arizona', 'North-Pinal-Arizona',
          # # California
          'Los-Angeles-California', 'San-Diego-California', 'San-Jose-California',
          'East-San-Gabriel-Valley-California', 'San-Francisco-California',
          'Fresno-California', 'Central-Contra-Costa-California',
          'Sacramento-California', 'Long-Beach-California', 'Oakland-California',
          'North-Coast-California', 'Bakersfield-California', 'Anaheim-California',
          'Santa-Ana-California', 'Upper-San-Gabriel-Valley-California',
          'Southwest-San-Gabriel-Valley-California', 'Riverside-California',
          'Stockton-California', 'South-Coast-California', 'Chula-Vista-California',
          'West-Contra-Costa-California', 'Irvine-California', 'Central-Coast-California',
          'Fremont-California', 'San-Bernardino-California', 'Modesto-California',
          'Oxnard-California', 'Fontana-California', 'Moreno-Valley-California',
          'Huntington-Beach-California', 'Glendale-California', 'Trabuco-California',
          'Newhall-California', 'Perris-Valley-California', 'Santa-Clarita-California',
          'El-Toro-California', 'Garden-Grove-California', 'Oceanside-California',
          'Rancho-Cucamonga-California', 'Santa-Rosa-California',
          'South-Antelope-Valley-California', 'Ontario-California', 'Elk-Grove-California',
          'Corona-California', 'Lancaster-California', 'Palmdale-California',
          'Coachella-Valley-California', 'Salinas-California', 'Hayward-California',
          'North-Antelope-Valley-California', 'Pomona-California', 'Escondido-California',
          'Sunnyvale-California', 'Torrance-California', 'Pasadena-California',
          'Orange-California', 'Fullerton-California', 'South-Bay-Cities-California',
          'Thousand-Oaks-California', 'Visalia-California', 'Roseville-California',
          'Concord-California', 'Simi-Valley-California', 'East-Los-Angeles-California',
          'Santa-Clara-California', 'Victorville-California', 'Vallejo-California',
          'Berkeley-California', 'El-Monte-California', 'Downey-California',
          'Costa-Mesa-California', 'Carlsbad-California', 'Jurupa-California',
          'Inglewood-California', 'Fairfield-California', 'Santa-Maria-Valley-California',
          'Ventura-California', 'San-Buenaventura-Ventura-California',
          'Temecula-California', 'Antioch-California', 'Richmond-California',
          'West-Covina-California', 'Mather-California', 'Murrieta-California',
          'Norwalk-California', 'Daly-City-California', 'Burbank-California',
          'Santa-Maria-California', 'El-Cajon-California', 'San-Mateo-California',
          'Rialto-California', 'Clovis-California',
          # Colorado
          'Denver-Colorado', 'Northeast-Jefferson-Colorado', 'Colorado-Springs-Colorado',
          'Aurora-Colorado', 'South-Aurora-Colorado', 'West-Adams-Colorado',
          'Southwest-Arapahoe-Colorado', 'Fort-Collins-Colorado', 'Lakewood-Colorado',
          'Thornton-Colorado', 'Arvada-Colorado', 'Westminster-Colorado',
          'Pueblo-Colorado', 'Centennial-Colorado', 'Boulder-Colorado',
          # Connecticut
          'Bridgeport-Connecticut', 'New-Haven-Connecticut', 'Stamford-Connecticut',
          'Hartford-Connecticut', 'Waterbury-Connecticut',
          # DC
          'Washington-District-of-Columbia',
          # Delaware
          'Brandywine-Delaware',
          # Florida
          'Jacksonville-Florida', 'Miami-Florida', 'Tampa-Florida',
          'Kendale-Lakes-Lindgren-Acres-Florida', 'Orlando-Florida',
          'St.-Petersburg-Florida', 'Hialeah-Florida', 'Tallahassee-Florida',
          'Fort-Lauderdale-Florida', 'Port-St.-Lucie-Florida', 'Cape-Coral-Florida',
          'Kendall-Perrine-Florida', 'Pembroke-Pines-Florida', 'Sunshine-Parkway-Florida',
          'Hollywood-Florida', 'Miramar-Florida', 'Gainesville-Florida',
          'Coral-Springs-Florida', 'Southwest-Orange-Florida', 'Citrus-Park-Fern-Lake-Florida',
          'Northwest-Dade-Florida', 'Clearwater-Florida', 'North-Westside-Florida',
          'Pompano-Beach-Florida', 'Palm-Bay-Florida', 'West-Palm-Beach-Florida',
          'Brandon-Florida', 'Lakeland-Florida',
          # Georgia
          'Atlanta-Georgia', 'Augusta-Richmond-County-Georgia', 'Columbus-Georgia',
          'Northeast-Cobb-Georgia', 'Augusta-Georgia',
          'Athens-Clarke-County-Georgia', 'Sandy-Springs-Georgia',
          #Hawaii
          'Honolulu-Hawaii', 'Urban-Honolulu-Hawaii', 'Ewa-Hawaii', 'Koolaupoko-Hawaii',
          # Iowa
          'Des-Moines-Iowa', 'Cedar-Rapids-Iowa', 'Davenport-Iowa',
          # Idaho
          'Boise-City-Idaho',
          # Illinois
          'Chicago-Illinois', 'Aurora-Illinois', 'Rockford-Illinois', 'Joliet-Illinois',
          'Naperville-Illinois', 'Springfield-Illinois', 'Peoria-Illinois',
          'Elgin-Illinois',
          # Indiana
          'Indianapolis-Indiana', 'Fort-Wayne-Indiana', 'Evansville-Indiana',
          'South-Bend-Indiana',
          # Kansas
          'Wichita-Kansas', 'Overland-Park-Kansas', 'Kansas-City-Kansas',
          'Olathe-Kansas', 'Topeka-Kansas',
          # Kentucky
          'Lexington-Fayette-Kentucky', 'Fayette-Kentucky', 'Louisville-Kentucky',
          # Louisiana
          'New-Orleans-Louisiana', 'Baton-Rouge-Louisiana', 'Shreveport-Louisiana',
          'Metairie-Louisiana', 'Lafayette-Louisiana',
          # Massachusetts
          'Boston-Massachusetts', 'Worcester-Massachusetts', 'Springfield-Massachusetts',
          'Lowell-Massachusetts', 'Cambridge-Massachusetts',
          # Maryland
          'Baltimore-Maryland',
          # Maine
          'Portland-Maine',
          # Michigan
          'Detroit-Michigan', 'Grand-Rapids-Michigan', 'Warren-Michigan',
          'Sterling-Heights-Michigan', 'Ann-Arbor-Michigan', 'Lansing-Michigan',
          # Minnesota
          'Minneapolis-Minnesota', 'St.-Paul-Minnesota', 'Rochester-Minnesota',
          # Missouri
          'Kansas-City-Missouri', 'St.-Louis-Missouri', 'Springfield-Missouri',
          'Independence-Missouri', 'Columbia-Missouri',
          # Mississippi
          'Jackson-Mississippi',
          # Montana
          'Billings-Montana',
          # North Carolina
          'Charlotte-North-Carolina', 'Raleigh-North-Carolina', 'Greensboro-North-Carolina',
          'Durham-North-Carolina', 'Winston-Salem-North-Carolina', 'Fayetteville-North-Carolina',
          'Cary-North-Carolina', 'Wilmington-North-Carolina', 'High-Point-North-Carolina',
          # North Dakota
          'Fargo-North-Dakota',
          # Nebraska
          'Omaha-Nebraska', 'Lincoln-Nebraska',
          # New Hampshire
          'Manchester-New-Hampshire',
          # New Jersey
          'Newark-New-Jersey', 'Jersey-City-New-Jersey', 'Paterson-New-Jersey',
          'Elizabeth-New-Jersey', 'Edison-New-Jersey',
          # New Mexico
          'Albuquerque-New-Mexico', 'Las-Cruces-New-Mexico',
          # Nevada
          'Las-Vegas-Nevada', 'Henderson-Nevada', 'Reno-Nevada', 'North-Las-Vegas-Nevada',
          'Paradise-Nevada', 'Sunrise-Manor-Nevada', 'Spring-Valley-Nevada',
          'Enterprise-Nevada',
          # New York
          'New-York-New-York', 'Brooklyn-New-York', 'Queens-New-York',
          'Manhattan-New-York', 'Bronx-New-York',
          # Ohio
          'Columbus-Ohio', 'Cleveland-Ohio', 'Cincinnati-Ohio', 'Toledo-Ohio',
          'Akron-Ohio', 'Dayton-Ohio',
          # Oklahoma - IF THERE'S PROBLEMS CHECK HERE FIRST
          'Oklahoma-City-Oklahoma', 'Tulsa-Oklahoma', 'Norman-Oklahoma',
          'Broken-Arrow-Oklahoma', 'North-Cleveland-Oklahoma',
          # Oregon
          'Portland-Oregon', 'Northwest-Clackamas-Oregon', 'Salem-Oregon',
          'Eugene-Oregon', 'Gresham-Oregon',
          # Pennsylvania
          'Philadelphia-Pennsylvania', 'Pittsburgh-Pennsylvania', 'Allentown-Pennsylvania',
          #Rhode Island
          'Providence-Rhode-Island',
          # South Carolina
          'Columbia-South-Carolina', 'Charleston-South-Carolina',
          'North-Charleston-South-Carolina',
          # South Dakota
          'Sioux-Falls-South-Dakota',
          # Tennessee
          'Memphis-Tennessee', 'Nashville-Davidson-Tennessee',
          'Metropolitan-Government-Tennessee', 'Knoxville-Tennessee',
          'Chattanooga-Tennessee', 'Clarksville-Tennessee',
          'Murfreesboro-Tennessee',
          # Texas
          'Houston-Texas', 'San-Antonio-Texas', 'Dallas-Texas', 'Austin-Texas',
          'Fort-Worth-Texas', 'El-Paso-Texas', 'Northeast-Tarrant-Texas',
          'Arlington-Texas', 'Corpus-Christi-Texas', 'Southeast-Montgomery-Texas',
          'Plano-Texas', 'Laredo-Texas', 'Lubbock-Texas', 'Garland-Texas',
          'Irving-Texas', 'Amarillo-Texas', 'Grand-Prairie-Texas',
          'Brownsville-Texas', 'McKinney-Texas', 'Pasadena-Texas', 'Frisco-Texas',
          'Mesquite-Texas', 'McAllen-Texas', 'Killeen-Texas', 'Waco-Texas',
          'Carrollton-Texas', 'Denton-Texas', 'Midland-Texas',
          'Southeast-Hidalgo-Texas', 'Abilene-Texas', 'Beaumont-Texas',
          'Odessa-Texas', 'Round-Rock-Texas', 'East-Jefferson-Texas',
          'Richardson-Texas', 'Wichita-Falls-Texas', 'College-Station-Texas',
          'Pearland-Texas', 'Lewisville-Texas', 'Tyler-Texas',
          # Utah
          'Salt-Lake-City-Utah', 'North-Davis-Utah', 'West-Valley-City-Utah',
          'Provo-Utah', 'West-Jordan-Utah', 'South-Davis-Utah',
          # Virginia
          'Virginia-Beach-Virginia', 'Norfolk-Virginia', 'Richmond-Virginia',
          'Arlington-Virginia', 'Newport-News-Virginia', 'Alexandria-Virginia',
          'Hampton-Virginia',
          # Vermont
          'Burlington-Vermont',
          # Washington
          'Seattle-Washington', 'East-Seattle-Washington', 'Spokane-Washington',
          'Tacoma-Washington', 'Vancouver-Washington', 'Bellevue-Washington',
          'Kent-Washington', 'Everett-Washington',
          # Wisconsin
          'Milwaukee-Wisconsin', 'Madison-Wisconsin', 'Green-Bay-Wisconsin',
          # West Virginia
          'Charleston-West-Virginia',
            # Wyoming
          'Cheyenne-Wyoming']

for item in cities:
    url = f"https://www.city-data.com/city/{item}.html"
    urls.append(url)

for item in urls:
    response = requests.get(item)
    response_html = response.text

    soup = BeautifulSoup(response_html, features = 'lxml')
    print(item)

    #Population
    population_box = soup.find("section", attrs={'class': "city-population"})
    if population_box != None:
        population_num = population_box.text.split(':')[1].split()[0]
        try:
                population_change = population_box.text.split(':')[2].split()[0]
        except IndexError:
                population_change = np.nan

    else:
        population_num = np.nan
        population_change = np.nan
    
    #median age of population
    pop_age = soup.find("section", attrs={'class': "median-age"})
    if pop_age != None:
        median_age = pop_age.text.split()[2].strip()[4:]
    else:
        median_age = np.nan
    
    #median income
    income = soup.find("section", attrs={'class': "median-income"})
    if income != None:
        median_income = income.text.split(':')[1].split()[0]
    #Per capita income
        per_capita_income = income.text.split(':')[3].split()[0]
    #Median House Value
        if (income.text.split(':')[5].split()[0]) == 'over':
                med_house_val = income.text.split(':')[5].split()[1]
        else:
                med_house_val = income.text.split(':')[5].split()[0]
    else:
        median_income = np.nan
        per_capita_income = np.nan 
        med_house_val = np.nan

    #median rent
    rent = soup.find("section", attrs={'class': "median-rent"})
    if rent != None:
        median_rent = rent.text.split()[-1]
    else:
        median_rent = np.nan
    
    #cost_of_living_index
    index = soup.find("section", attrs={'class': "cost-of-living-index"})
    if index != None:
        cost_of_living_index = index.text.split(':')[1].split()[0]
    else:
        cost_of_living_index = np.nan
    
    #Poverty
    poverty = soup.find("section", attrs={'class': "poverty-level"})
    if poverty != None:
        percent_below_poverty_lvl = poverty.text.split(':')[1].split()[0]
    else:
        percent_below_poverty_lvl = np.nan
    
    #Crime
    crime = soup.find("section", attrs={'class': "crime"})
    
    if crime != None:
        crime_ind = crime.text.split('average')[1]
        crime_every_year = crime_ind.split()[1].split('.')
        crime_index_score = crime_every_year[-2][1:]+'.'+crime_every_year[-1]
    else:
        crime_every_year = np.nan
        crime_index_score = np.nan

    #Population Density
    pop_den = soup.find("section", attrs={'class': "population-density"})
    if pop_den != None:
        population_density = pop_den.text.split(':')[2].split()[0]
    else:
        population_density = np.nan
    
    # unemployment rate
    unemployment = soup.find("section", attrs={'class': "unemployment"})
    if unemployment != None:
        unemployment_percent = unemployment.text.split(':')[2].partition('%')[0]+'%'
    else: 
        unemployment_percent = np.nan
    
    #Most common industries
    ind = soup.find("section", attrs={'class': "most-common-industries"}).text.split('Most')
    if ind !=  ['']:
        industries = ind[1].split('Females')[1].split('\n')
        industries = [value for value in industries if value != '']
        most_common_indus_both = int(len(industries)/3)
        most_common_industries = industries[:most_common_indus_both]
    else:
        most_common_industries = np.nan
    
    #Taxes
    taxes = soup.find("section", attrs={'class': "real-estate-taxes"})
    if taxes != None:
        if taxes.text.split(':')[1].split()[0].startswith("$"):
            tax_mortgage = taxes.text.split(':')[1].split()[0]
        else:
            tax_mortgage = taxes.text.split(':')[2].split()[1][1:7]
        #tax_no_mortgage = tax[2].split()[0]
    else:
        tax_mortgage = np.nan
        #tax_no_mortgage = np.nan
    
    #Co-ordinates
    coordinates = soup.find("section", attrs={'class': "coordinates"})
    if coordinates != None:
        Latitude = coordinates.text.split()[1]+' N'
        Longitude = coordinates.text.split()[4]+' W'
    else:
        Latitude = Longitude = np.nan

    
     #Avg Commute time
    education = soup.find("section", attrs={'class': "education-info"})
    if education !=  None:
        try:
            avg_commute = education.text.split('(commute): ')[1].split('\n')[0]
        except IndexError:
            avg_commute = np.nan     
    else:
        avg_commute = np.nan

    #AQI
    air_poll = soup.find("section", attrs={'class': "air-pollution"})
    if air_poll != None:
        try:
            aqi = air_poll.text.split('(AQI)')[1].split()[4]
        except IndexError:
            aqi = np.nan
    else:
        aqi = np.nan

    #nickname
    name = soup.find("section", attrs={'class': "city-nicknames"})
    if name != None:
        nickname = name.text.split(':')[1]
    else:
        nickname = np.nan

    file_exists = os.path.isfile('city.csv')

    with open('city.csv', 'a') as csv_file:
        headers = {'city':None, 'population':None, 'population_change':None, 'Median_Age':None,'Median_Income':None, 
                   'per_capita_Income':None,'Median_House_Value':None,'Median Rent':None,'Cost_of_Living_Index':None,
                   'Percent_below_Poverty':None,'Crime_rate':None,'Population_Density':None,'Unemployment_rate':None,
                   'Most_Common_Industries':None,'Property_taxes':None,'Laitude':None,'Longitude':None,
                   'Average_Commute_Time':None,'AQI':None, 'Nickname':None}
        writer = csv.DictWriter(csv_file, fieldnames = headers)
        if not file_exists:
                writer.writeheader()
        writer.writerows([{'city': item, 'population': population_num, 'population_change': population_change, 'Median_Age':median_age, 
                        'Median_Income':median_income,'per_capita_Income':per_capita_income ,'Median_House_Value':med_house_val,
                        'Median Rent':median_rent,'Cost_of_Living_Index':cost_of_living_index,'Percent_below_Poverty':percent_below_poverty_lvl,
                        'Crime_rate':crime_index_score,'Population_Density':population_density,
                        'Unemployment_rate':unemployment_percent,'Most_Common_Industries':most_common_industries,
                        'Property_taxes':tax_mortgage,'Laitude':Latitude,'Longitude':Longitude,'Average_Commute_Time':avg_commute,
                        'AQI':aqi,'Nickname':nickname}])
