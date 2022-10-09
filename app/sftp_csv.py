#!/usr/bin/python3
import pysftp
from dotenv import load_dotenv
import os
import sys


def activate_sftp():
    load_dotenv("/home/linoy/exercises/for_practice/Attendance-project/.env.py")
    remote_course_machine = os.getenv('REMOTE_COURSE_MACHINE')
    remote_user = os.getenv('REMOTE_USER')
    remote_password = os.getenv('REMOTE_PASS')

    with pysftp.Connection(host=remote_course_machine, username=remote_user, password=remote_password) as sftp:
        print("Connection succesfully stablished ... ")

        # The remote directory path
        remoteDirPath = os.getenv('REMOTE_DIR_PATH')
        sftp.cwd(remoteDirPath)
        files_attributes = sftp.listdir_attr()

        for attr in files_attributes:
            file_name = attr.filename
            #print(file_name)
            remoteFilePath = os.path.join(os.getenv('REMOTE_DIR_PATH'), file_name)

        # Local path where the file will be saved
            localFilePath = os.path.join(os.getenv('LOCAL_ORIGIN_DIR_PATH'), file_name)

            sftp.get(remoteFilePath, localFilePath)

if __name__ == "__main__":
    activate_sftp()
