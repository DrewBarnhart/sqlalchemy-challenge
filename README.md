# sqlalchemy-challenge

This project ncorporates SQLAlchemy to do basic climate analysis and data exploration of a climate database. Specifically it utilizes SQLAlchemy ORM queries, Pandas, and Matplot lib. 

The code generated is based from two files: Climate_starter.ipynb ad hawaii.sqlit


Here is the listed procedure within the jupyter notebook: 
1. Use the SQLAlchemy create_engine() function to connect to your SQLite database.

2. Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.

3. Link Python to the database by creating a SQLAlchemy session.


### After this initial analysis was completed.... 
 Flask to create your routes as follows:

/

Start at the homepage.

List all the available routes.

/api/v1.0/precipitation

Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

Return the JSON representation of your dictionary.

/api/v1.0/stations

Return a JSON list of stations from the dataset.
/api/v1.0/tobs

Query the dates and temperature observations of the most-active station for the previous year of data.

Return a JSON list of temperature observations for the previous year.

/api/v1.0/<start> and /api/v1.0/<start>/<end>

Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
