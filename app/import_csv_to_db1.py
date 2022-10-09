#!/usr/bin/python3
import MySQLdb
import csv
from dotenv import load_dotenv
import sys
import os
import datetime

# in order to evoid writing passwords in the code i will use dotenv to query environment variable (also os.environ is a good option)
# using .get() to evoid erors >> if we will get error it would take the 2nd param

load_dotenv("/home/linoy/exercises/for_practice/Attendance-project/.env.py")
CONTAINER_DB_HOST = os.getenv('CONTAINER_DB_HOST')
CONTAINER_DB_USER = os.getenv('MYSQL_USER')
CONTAINER_DB_PWD = os.getenv('MYSQL_PASSWORD')
CONTAINER_DB_NAME = os.getenv('MYSQL_DATABASE')
CONTAINER_DB_PORT = os.getenv('CONTAINER_DB_PORT')
conn_db = MySQLdb.connect(host=CONTAINER_DB_HOST, port=CONTAINER_DB_PORT, user=CONTAINER_DB_USER,
                          password=CONTAINER_DB_PWD, database=CONTAINER_DB_NAME)
'''
load_dotenv("/home/linoy/exercises/for_practice/docker-flask-app-att/.env.py")
CONTAINER_DB_HOST=os.getenv('CONTAINER_DB_HOST')
CONTAINER_DB_USER=os.getenv('CONTAINER_DB_USER')
CONTAINER_DB_PWD=os.getenv('CONTAINER_DB_PWD')
CONTAINER_DB_NAME=os.getenv('CONTAINER_DB_NAME')
CONTAINER_DB_PORT=os.getenv('CONTAINER_DB_PORT')
conn_db = MySQLdb.connect(host=CONTAINER_DB_HOST, port=CONTAINER_DB_PORT, user=CONTAINER_DB_USER, password=CONTAINER_DB_PWD, database=CONTAINER_DB_NAME)
'''
cursor = conn_db.cursor()
cursor.execute("SHOW tables;")
m = cursor.fetchall()
print(m)

#import and write all raw csv files to DB
input_dir_path = os.getenv('LOCAL_ORIGIN_DIR_PATH')
files = os.listdir(input_dir_path)
for file in files:
    csv_input_path = os.path.join(input_dir_path, file)
    with open(csv_input_path, 'r', encoding='utf-16', newline='') as csvfile:
        '''dialect = csv.Sniffer().sniff(csvfile.readline())
        csvfile.seek(0)'''
        csv_data = csv.reader(csvfile, delimiter='\t')
        #header = next(csv_data)
        included_cols = [1,2,3,4,5,6,7]

        row_counter = 0
        for row in csv_data:
            if row_counter == 0:
                row_counter += 1
                continue

            content = list(row[i] for i in included_cols)
            for i in [0, 1, 4, 5]:
                content[i] = datetime.datetime.strptime(content[i][2:-1], '%Y-%m-%d %H:%M:%S')

            cursor = conn_db.cursor()
            cursor.execute(
                    "INSERT INTO attendance_csv(`meeting start time`, `meeting end time`, name, email, `join time`, `leaving time`, `attendance duration`) VALUES (%s, %s, %s, %s ,%s, %s, %s)",
                    content)
            conn_db.commit()
            cursor = conn_db.cursor()
            cursor.close()

#import and write final csvfile to DB
cursor = conn_db.cursor()
csv_data = csv.reader(open(os.getenv('FINAL_ATT_FILE')))
header = next(csv_data)

for row in csv_data:
    cursor.execute(
        "INSERT INTO final_attendance (name,`attendance duration`,`attendance percentage`) VALUES (%s, %s, %s)", row)

conn_db.commit()
cursor.close()
print('Done')

