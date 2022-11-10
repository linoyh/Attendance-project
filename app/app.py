#!/usr/bin/python3
from flask import Flask, render_template
from dotenv import load_dotenv
import os
import MySQLdb
import subprocess

#using bash set command -x the shell throws logs, -u throws a error if there is undefines variable, -e exit the terminal if the exit code is not 0
os.system("set -exu")

app = Flask(__name__)

def db_connection():
  load_dotenv("./.env.py")
  CONTAINER_DB_HOST = os.getenv('CONTAINER_DB_HOST')
  CONTAINER_DB_USER = os.getenv('MYSQL_USER')
  CONTAINER_DB_PWD = os.getenv('MYSQL_PASSWORD')
  CONTAINER_DB_NAME = os.getenv('MYSQL_DATABASE')
  CONTAINER_DB_PORT = os.getenv('CONTAINER_DB_PORT')
  conn_db = MySQLdb.connect(host=CONTAINER_DB_HOST, port=int(CONTAINER_DB_PORT), user=CONTAINER_DB_USER, password=CONTAINER_DB_PWD, database=CONTAINER_DB_NAME)

  '''
  load_dotenv(".env.py")
  ATTENDANCE_HOST=os.getenv('ATTENDANCE_HOST')
  ATTENDANCE_DB_USER=os.getenv('ATTENDANCE_DB_USER')
  MYSQL_ATTENDANCE_PWD=os.getenv('MYSQL_ATTENDANCE_PWD')
  MYSQL_DB_NAME=os.getenv('MYSQL_DB_NAME')
  conn_db = MySQLdb.connect(host=ATTENDANCE_HOST, port=3306, user=ATTENDANCE_DB_USER, password=MYSQL_ATTENDANCE_PWD, database=MYSQL_DB_NAME)
  '''

  cursor = conn_db.cursor()
  cursor.execute("SELECT * FROM final_attendance;")
  att_quary = cursor.fetchall()
  return att_quary

def json_att(att_quary):
  json_att_ready = []
  for item in att_quary:
    obj = {
      'Name': item[1],
      'Duration': item[2],
      'Percentage': item[3]
    }
    json_att_ready.append(obj)
  return json_att_ready

json_att_ready = None

@app.route('/')
def index():
  return render_template('index.html', attendance=json_att_ready)

#The main function run all the other scripts one by one, finally present the DB data in the browser
if __name__ == "__main__":
  subprocess.call("python3 sftp_csv.py", shell=True)
  subprocess.call("python3 attendance.py", shell=True)
  subprocess.call("python3 import_csv_to_db1.py", shell=True)
  att_quary = db_connection()
  json_att_ready = json_att(att_quary)
  app.run(host='0.0.0.0', debug=True, port=5000)

