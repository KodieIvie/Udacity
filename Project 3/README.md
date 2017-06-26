This is the News articles log Project for Udacity. Using python's psycopg2 module for the Postgresql 'news' database in the vagrant 
environment as user "vagrant".

Views were created to answer the third question. below is the code I used in my program, or you can just simply run the 'reporting-tool.py' in your python3 interpreter. Must have the news database. 

a snapshot of this program is included.
PEP8 tested.


""" 

# create a view with total requests for 'Third query question'

CREATE OR REPLACE VIEW requests AS 
SELECT to_char(time, 'Month DD, YYYY') AS date, 
COUNT(status) AS total 
FROM log 
GROUP BY date 
ORDER BY date ASC; 

# to create a view of requests with errors.

CREATE OR REPLACE VIEW errors AS 
SELECT to_char(time, 'Month DD, YYYY') AS date, 
COUNT(status) AS err, status 
FROM log 
WHERE status = '404 NOT FOUND' 
GROUP BY date, status 
ORDER BY date ASC;"

# create a view for > 1% errors a day.

CREATE OR REPLACE VIEW percent AS 
SELECT e.date, e.err, r.total, (e.err/r.total::decimal) AS perc 
FROM errors AS e JOIN requests AS r ON e.date = r.date 
ORDER BY date ASC;

SELECT date, round(perc*100.0, 1) from percent 
WHERE perc > .01 
ORDER BY date ASC;

"""


'Third query question'
3. On which days did more than 1% of requests lead to errors?