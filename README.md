# Attendance

Attendance is an app for calculate the Attendance time rates for the Devops 8200-dev-bynet course participants.

## Installation
cd into the docker-compose direcory location and write the command:

docker-compose up --build

## preparation

There are 2 docker containers in the project:
#### mysqldb 
pulled from docker hub by docker-compose.
init.sql file do all the db quaries - create linoy_attendance db
using special priviliged user to create attendance_csv table- contain all csv files from the course and final_attendance the main table which contain the proccessed data from the attendance.py script
#### app
created by docker file, build by it and defined in the docker-compose 
 
#### app.py
activated by the docker file "CMD ["python3", "./app.py"]"

attached to templates directory which contain index.html - our frontend to present the project nicely in the browser
activate 3 scripts:
* sftp_csv.py- takes all the csv files fron the remote course machine into the db container
* attendance.py -the main backend script - 
* import_csv_to_db1.py - import the final csv file - the final result of the attendance script to the db


#### .env file
contain  environment variables for all the scripts and logics 

