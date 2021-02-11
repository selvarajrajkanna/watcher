Backend Test - FullThrottle Labs

Django application with User and ActivityPeriod models, write a custom management command to populate the database with some dummy data, and design an API to serve that data in the json format given above.

Requirements.txt

asgiref==3.3.1

Django==3.1.6

pytz==2021.1

sqlparse==0.4.1



Technology used:
Framework - Django
Database - SQLite(default)



I created a simple web application using only Django and default sqlite database to create couple of sample users and filled user activity with dummy data. This is a very simple application as the requirement was basic.
I created two users with following details 
{
  "id": "W012A3CDE", "real_name": "Egon Spengler", "tz": "America/Los_Angeles", 
  "id": "W07QCRPA4", "real_name": "Glinda Southgood", "tz": "Asia/Kolkata"
}


API end points:
1) https://selvarajrajkanna.pythonanywhere.com/activity/create/dummy - to insert dummy activity for all available users.
2) https://selvarajrajkanna.pythonanywhere.com/activity/all - the requested output.
