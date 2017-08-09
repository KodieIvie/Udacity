This is the catalog project for the udacity full stack nano degree program.
It provides a place to create catalog categories and items in the catalog.
It uses a 3rd party Oauth registration and login in system,
which ensures only authorized users can manage data in the db.

****** secure api endpoint *******
It also has a secure api endpoint which you can access at
http://localhost:5000/api/json 
- username = world | password = hello -


******** getting started *********
first install the following in your python environment.

sqlalchemy, flask, itsdangerous, passlib, flask_httpauth, oauth2client

then run application.py and open http://localhost:5000 in your browser