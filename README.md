# Project-3


This project utilized the extract, transform and load process.

Extract:
Amazon.ca bestsellers data was pulled from the Rainforest API. See references for the url. The data pulled was in JSON.

Load and Transform:
The JSON data was then loaded into three separate MongoDB collections: video game bestsellers, books bestsellers and electronics bestsellers.
The collections were transformed by dropping the pagination documents. The intention here was to practice dropping data in MongoDB.

Load and Transform:
Four tables were created in Postgres AWS: prices, category, ratings and bestsellers_books using Python.
To populate the data into these four tables, the collections data from MongoDB was transformed and loaded using Python.


References:

The source of the Amazon.ca data is Rainforest API. 
https://www.rainforestapi.com/

To create collections with the JSON data from the Rainforest API, we used code produced by Mahesh Peiris. The code Mahesh provided can be found at the following GitHub repo:
https://github.com/maheshpeiris0/mongodb_test_projects