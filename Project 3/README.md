This is the News articles log Project for Udacity. Using python's psycopg2 module for the Postgresql 'news' database in the vagrant 
environment as user "vagrant".

Views were created to answer the third question. below is the code I used in my program, or you can just simply run the 'reporting-tool.py' in your python3 interpreter. Must have the news database. 

a snapshot of this program is included.
PEP8 tested.

Please create each of the views below in the news Database prior to running reporting-tool.py  

""" 

# First view creates a view with total requests for 'Third query question'
# Second view creates a view of requests with errors.
# Third view creates a view for percent.

CREATE OR REPLACE VIEW requests AS 
SELECT to_char(time, 'FMMonth FMDD, YYYY') AS date, 
COUNT(status) AS total 
FROM log 
GROUP BY date 
ORDER BY date ASC; 

CREATE OR REPLACE VIEW errors AS 
SELECT to_char(time, 'FMMonth FMDD, YYYY') AS date, 
COUNT(status) AS err, status 
FROM log 
WHERE status != '200 OK' 
GROUP BY date, status 
ORDER BY date ASC; 

CREATE OR REPLACE VIEW percent AS 
SELECT e.date, e.err, r.total, (e.err/r.total::decimal) AS perc 
FROM errors AS e JOIN requests AS r ON e.date = r.date 
ORDER BY date ASC;

"""

Above is only the code necessary to CREATE VIEWS to answer the Third question in the project.
Below are the questions for which this program queries the database for.

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors?
