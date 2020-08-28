# Find Your City

<img src="https://github.com/Lambda-School-Labs/juxta-city-data-ds/blob/master/dash-app/Both_apps_IntoOne/assets/find%20your%20city%2018.png" width="700" />

You can find the project at [findur.city](http://www.findur.city/).

## Contributors

### Labs 11 - Second Product Cycle

#### Team Lead

Kelly Moreira [Github](https://github.com/misskellymore) | [Linkedin](https://www.linkedin.com/in/kemore/)

#### Data Scientists

Arturo Obregon | [Github](https://github.com/artbrgn) | [Linkedin](https://www.linkedin.com/in/arturo-obregon/)

Ashley Gaskins | [Github](https://github.com/ash827) | [Linkedin](https://www.linkedin.com/in/ashley-gaskins-17b87474/)

James Barciz | [Github](https://github.com/JamesBarciz) | [Linkedin](https://www.linkedin.com/in/james-barciz-6b440413a/)

Pedro Escobedo | [Github](https://github.com/pedroescobedob) | [Linkedin](https://www.linkedin.com/in/pedroescobedob/)

### Labs 7 - First Product Cycle

#### Team Lead

Haden Moore [Github](https://github.com/HadenMoore) | [Linkedin](https://www.linkedin.com/in/hadenmoore/)

#### Data Scientists

Anika Zolman-Nacey | [Github](https://github.com/AnikaZN)

Karthik Mahendra | [Github](https://github.com/kmk028)

Raul Harrington, Jr. | [Github](https://github.com/cicbeast)                                       



## Directory Structure
```
├─── findurcity
│   ├─── notebooks
│   │   ├─── Close Matches - Anika.ipynb
│   │   ├─── covid_exploration.ipynb
│   │   ├─── Exploration and Testing - Anika.ipynb
│   │   ├─── heart_disease_cdc_exploration.ipynb
│   │   ├─── heart_disease_data_split.ipynb
│   │   ├─── plotly_exploration.ipynb
│   │   ├─── COVID_19_County_file.ipynb
│   │   ├─── heart_disease_dash.ipynb
│   │   └─── Weather - Anika.ipynb
│   │   
│   ├─── src
│   │   ├─── database
│   │   │   ├─── city_scraping.py
│   │   │   ├─── covid_to_pg.py
│   │   │   ├─── FindUrCity-Entity_2.pdf
│   │   │   └─── pg_insert.py
│   │   │
│   │   ├─── datasets
│   │   │   ├─── covid_data.csv
│   │   │   ├─── economy_data.csv
│   │   │   ├─── heart_data.csv 
│   │   │   ├─── housing_data.csv 
│   │   │   ├─── job_data.csv 
│   │   │   ├─── location_data.csv 
│   │   │   ├─── people_stats_data.csv 
│   │   │   └─── referenes.csv
│   │   │
│   │   └─── extraneous_datasets
│   │       └─── ...23 misc datasets...
│   │ 
│   ├─── dash-app
│   │   ├─── .idea
│   │   ├─── .ipynb_checkpoints
│   │   ├─── Mapbox_countiesGeoJson
│   │   ├─── Both_apps_IntoOne
│   │   ├─── Covid19_app
│   │   ├─── HeartDisease_app
│   │   ├─── README.md
│   │
│   ├─── templates
│   │   ├─── about.html
│   │   ├─── homepage.html
│   │   └─── team.html
│   │
│   └─── Twitter_stream_app
│       ├─── app
│       │   ├─── api.py
│       │   ├─── app.py
│       │   ├─── slistener.py
│       │   └─── streamer.py
│       │
│       ├─── Dockerfile
│       ├─── requirements.txt
│       └─── two.sh
│   
├─── labspt11_documents
│   ├─── code_of_conduct.md
│   └─── pull_request_template.md
│
├─── test
│   ├── test_data
│   │   └── test_datasets.py
│   │
│   └── test_database
│       └── test_postgres.py
│
├─── .gitignore
├─── LICENSE
├─── Procfile
├─── README.md
└─── requirements.txt
```



## Project Overview


[Trello Board](https://trello.com/b/R2QOaAEe/labspt7-juxta-city-data)

[Product Canvas](https://www.notion.so/ab80ad6b9a9341e38ea49eece4c10498?v=e7d7bf0069e34cad85e28b0d315d6675)

An app that analyzes data from cities such as populations, cost of living, crime rates and many other social and economic factors that are important in deciding where someone would like to live. This app will present such important data in an intuitive and easy to understand interface.

[Deployed Front End](http://www.findur.city/)

### Tech Stack

Python

Heroku

Flask

Docker

Plotly Dash

SQLite

Google Cloud Platform - BigQuery

AWS SageMaker

Import.io

Mapbox


### Data Sources
-   [City-Data.com] (https://www.city-data.com/)

-   [Twitter.com] (https://twitter.com/home)

-   [GCP] (https://cloud.google.com/)

-   [CDC] (https://www.cdc.gov/heartdisease/facts.htm)

-   [Johns Hopkins] (https://coronavirus.jhu.edu/us-map)

### Python Notebooks

[City Data Testing](https://github.com/Lambda-School-Labs/juxta-city-data-ds/blob/master/CityDataTesting.ipynb)

[Cleaning and JSON](https://github.com/Lambda-School-Labs/juxta-city-data-ds/blob/master/Cleaning%20and%20JSON%20-%20Anika.ipynb)

[Exploration and Testing](https://github.com/Lambda-School-Labs/juxta-city-data-ds/blob/master/Exploration%20and%20Testing%20-%20Anika.ipynb)

[Photos, Filtering, and Recommendation](https://github.com/Lambda-School-Labs/juxta-city-data-ds/blob/master/Photos%2C%20Filtering%2C%20and%20Recommendation%20-%20Anika.ipynb)

[Close Matches](https://github.com/Lambda-School-Labs/juxta-city-data-ds/blob/master/Close%20Matches%20-%20Anika.ipynb)

[Weather](https://github.com/Lambda-School-Labs/juxta-city-data-ds/blob/master/Weather%20-%20Anika.ipynb)


### How to connect to the data API

The data API can be found at https://junta-test.herokuapp.com. Listed below are the routes and the aspects of the data they access.

#### City Name

https://junta-test.herokuapp.com/name?id= {0-7127}

Example: https://junta-test.herokuapp.com/name?id=2126

Returns the city name which corresponds with the given id

#### Top 25 Cities

https://junta-test.herokuapp.com/top25

Returns all data for all of the top 25 cities according to their "Livability Score"

#### All Data

https://junta-test.herokuapp.com/data?city= {City, State}

Example: https://junta-test.herokuapp.com/data?city=Birmingham, Alabama

Returns all data for the given city

#### Search

https://junta-test.herokuapp.com/search?search= {Any characters}

Example: https://junta-test.herokuapp.com/search?search=bir

Returns all city names which start with the given characters

#### Recommendation

http://junta-test.herokuapp.com/recommend?state=None&population=0&population_change=0&median_age=0&house_cost=0&rental_cost=0&population_density=0&cost_of_living=0&average_commute=0&air_quality=0 {adjust values as appropriate}

Returns 1-5 cities based on the given filters, ranked by "Livability Score"

### Twitter Streaming App




## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a [code of conduct](./code_of_conduct.md.md). Please follow it in all your interactions with the project.

### Issue/Bug Request

 **If you are having an issue with the existing project code, please submit a bug report under the following guidelines:**
 - Check first to see if your issue has already been reported.
 - Check to see if the issue has recently been fixed by attempting to reproduce the issue using the latest master branch in the repository.
 - Create a live example of the problem.
 - Submit a detailed bug report including your environment & browser, steps to reproduce the issue, actual and expected outcomes,  where you believe the issue is originating from, and any potential solutions you have considered.

### Feature Requests

We would love to hear from you about new features which would improve this app and further the aims of our project. Please provide as much detail and information as possible to show us why you think your new feature should be implemented.

### Pull Requests

If you have developed a patch, bug fix, or new feature that would improve this app, please submit a pull request. It is best to communicate your ideas with the developers first before investing a great deal of time into a pull request to ensure that it will mesh smoothly with the project.

Remember that this project is licensed under the MIT license, and by submitting a pull request, you agree that your work will be, too.

#### Pull Request Guidelines

- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Update the README.md with details of changes to the interface, including new plist variables, exposed ports, useful file locations and container parameters.
- Ensure that your code conforms to our existing code conventions and test coverage.
- Include the relevant issue number, if applicable.
- You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### Attribution

These contribution guidelines have been adapted from [this good-Contributing.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426).

## Documentation

See [Backend Documentation](https://github.com/Lambda-School-Labs/juxta-city-data-be/blob/master/README.md) for details on the backend of our project.

See [Front End Documentation](https://github.com/Lambda-School-Labs/juxta-city-data-fe/blob/master/README.md) for details on the front end of our project.

