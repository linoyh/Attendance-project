# Development settings

#Remote course machine- get all raw csv files by sftp_csv.py
REMOTE_COURSE_MACHINE='185.164.16.144'
REMOTE_USER='linoyh'
REMOTE_PASS='123456'

#my VBox machine
ATTENDANCE_HOST='192.168.56.101'
ATTENDANCE_USER='linoy'
ATTENDANCE_PASS='060495'

#my VBox machine- connect to my local DB details
ATTENDANCE_DB_USER="jeff"
MYSQL_ATTENDANCE_PWD="12345"
MYSQL_DB_NAME="linoyhdb"

#DB container details
CONTAINER_DB_HOST='db'
CONTAINER_DB_USER="jeff"
CONTAINER_DB_PWD="12345"
CONTAINER_DB_ROOT_PWD='123456'
CONTAINER_DB_NAME="linoy_attendance"
CONTAINER_DB_PORT='3306'

#my VBox machine- connect to my local DB
REMOTE_DIR_PATH='/var/tmp/csv_files'
LOCAL_ORIGIN_DIR_PATH='/home/linoy/exercises/for_practice/docker-flask-app-att/app/csv_files_origin'
FINAL_CSV_DIR_PATH='/home/linoy/exercises/for_practice/docker-flask-app-att/app/csv_files_final'
FINAL_ATT_FILE='/home/linoy/exercises/for_practice/docker-flask-app-att/app/csv_files_final/final_par_file.csv'
