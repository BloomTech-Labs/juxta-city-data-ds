# Find Ur City

You can find the project at [findur.city](http://www.findur.city/).

## Contributors


|                                       [Anika Zolman-Nacey](https://github.com/AnikaZN)                                        |                                       [Karthik Mahendra](https://github.com/kmk028)                                        |                                       [Raul Harrington, Jr.](https://github.com/cicbeast)                                        |
| :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: |
|                      [<img src="https://ca.slack-edge.com/T4JUEB3ME-UJ24AE9UN-a7a80435887f-512" width = "200" />](https://github.com/AnikaZN)                       |                      [<img src="https://ca.slack-edge.com/T4JUEB3ME-U7ZHKHH1C-89bec4c1baf5-512" width = "200" />](https://github.com/kmk028)                       |                      [<img src="https://ca.slack-edge.com/T4JUEB3ME-UHZ6UE2G4-e86f386a7ac0-512" width = "200" />](https://github.com/cicbeast)                       |
|                 [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/AnikaZN)                 |            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/kmk028)             |           [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/cicbeast)            |          [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/NandoTheessen)           |            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/wvandolah)             |
| [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/anika-zolman-nacey/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/karthik-mahendra-a63a4324/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/raul-harrington-1b490a56/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) |



## Project Overview


[Trello Board](https://trello.com/b/R2QOaAEe/labspt7-juxta-city-data)

[Product Canvas](https://www.notion.so/ab80ad6b9a9341e38ea49eece4c10498?v=e7d7bf0069e34cad85e28b0d315d6675)

An app that analyzes data from cities such as populations, cost of living, crime rates and many other social and economic factors that are important in deciding where someone would like to live. This app will present such important data in an intuitive and easy to understand interface.

[Deployed Front End](http://www.findur.city/)

### Tech Stack

Python

Heroku

Flask

SQLite

Google Cloud Platform - BigQuery

AWS SageMaker

Import.io


### Data Sources
-   [City-Data.com] (https://www.city-data.com/)

### Python Notebooks

🚫  Add to or delete python notebook links as needed for your project

[Python Notebook 1](🚫add link to python notebook here)

[Python Notebook 2](🚫add link to python notebook here)

[Python Notebook 3](🚫add link to python notebook here)


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

Returns 1-5 cities based on the given filters, ranked by "Livability Scored"


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

