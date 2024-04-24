# Project-3

This project utilized the extract, transform and load process to create a non-sql database and an sql database. The non-sql database is housed in MongoDB Atlas and the sql data base is housed in Postgres AWS.

Extract:
Amazon.ca bestsellers data was pulled from the Rainforest API. See references for the url. The data pulled was in JSON.

Load and Transform:
The JSON data was then loaded into three separate MongoDB collections: video game bestsellers, books bestsellers and electronics bestsellers.
The collections were transformed by dropping the pagination documents. The intention here was to practice dropping data in MongoDB.

Load and Transform:
Four tables were created in Postgres AWS: prices, category, ratings and bestsellers_books using Python.
To populate the data into these four tables, the collections data from MongoDB was transformed and loaded using Python.

The psycopg adapter was utilized to create tables and load data in Postgres SQL.

A config.py file will need to be created to handle the following credentials:

For MongoDB Atlas, you will need to define user_name and password.

For Postgres AWS, you will need to define the following: postgres_user, postgres_password, postgres_host, postgres_port and postgres_database.

For the Rainforest API, you will need a unique API key.


References:

The source of the Amazon.ca data is Rainforest API. 
https://www.rainforestapi.com/

To create collections with the JSON data from the Rainforest API, we used code produced by Mahesh Peiris. The code Mahesh provided can be found at the following GitHub repo:
https://github.com/maheshpeiris0/mongodb_test_projects

Used to format the price column: 

DataFrame.apply()
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html

Lambdas
https://docs.python.org/3/reference/expressions.html#lambda

Instances
https://docs.python.org/3/library/functions.html#isinstance

Format
https://docs.python.org/3/library/string.html#format-string-syntax

Python Replace
https://docs.python.org/3/library/stdtypes.html#str.replace

Used to assist in generating plots:

Pandas
https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#plotting

Matplotlib
https://matplotlib.org/stable/users/index.html

Used to help with general inquires:ChatGPT
chat.openai.com