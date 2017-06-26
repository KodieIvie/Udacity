#!/usr/bin/env python3

import psycopg2

# Connect to an existing database
conn = psycopg2.connect("dbname=news user=vagrant")

# Open a cursor to perform database operations
cur = conn.cursor()

# First query question
cur.execute("SELECT articles.title, COUNT(*) AS pop "
            "FROM articles, log "
            "WHERE log.path LIKE '%' || articles.slug "
            "GROUP BY articles.title "
            "ORDER BY pop DESC LIMIT 3;")

topViews = cur.fetchall()
print("\n1. What are the most popular three articles of all time?\n")
for e in topViews:
    print('"' + e[0] + '"' + ' - ' + str(e[1]) + ' views')

# Second question query
cur.execute("SELECT authors.name, COUNT(*) AS pop "
            "FROM articles, authors, log "
            "WHERE authors.id = articles.author "
            "AND log.path LIKE '%' || articles.slug "
            "GROUP BY authors.name "
            "ORDER BY pop DESC;")

topAuthor = cur.fetchall()
print("\n2. Who are the most popular article authors of all time?\n")
for e in topAuthor:
    print(e[0] + ' - ' + str(e[1]) + ' Views')

# Third query question
# create a view with total requests
cur.execute("CREATE OR REPLACE VIEW requests AS "
            "SELECT to_char(time, 'Month DD, YYYY') AS date, "
            "COUNT(status) AS total "
            "FROM log "
            "GROUP BY date "
            "ORDER BY date ASC;")

# create a view of requests with errors.
cur.execute("CREATE OR REPLACE VIEW errors AS "
            "SELECT to_char(time, 'Month DD, YYYY') AS date, "
            "COUNT(status) AS err, status "
            "FROM log "
            "WHERE status = '404 NOT FOUND' "
            "GROUP BY date, status "
            "ORDER BY date ASC;")

# create a view for > 1% errors a day.
cur.execute("CREATE OR REPLACE VIEW percent AS "
            "SELECT e.date, e.err, r.total, (e.err/r.total::decimal) AS perc "
            "FROM errors AS e JOIN requests AS r ON e.date = r.date "
            "ORDER BY date ASC;")

cur.execute("SELECT date, round(perc*100.0, 1) from percent "
            "WHERE perc > .01 "
            "ORDER BY date ASC;")

showErr = cur.fetchall()
print("\n3. On which days did more than 1% of requests lead to errors?\n")
for e in showErr:
    print(e[0] + ' - ' + str(e[1]) + '% errors')

# Close communication with the database
cur.close()
conn.close()

# give credit where credit is due.
"""Thanks to psycopg2 documentation for the skeleton template and all the \n
great info, postgresql documentation, also the Udacity forums, \n
stack overflow and google"""
