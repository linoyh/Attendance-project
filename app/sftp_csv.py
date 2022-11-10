#!/usr/bin/python3
import pysftp
import dotenv
from dotenv import load_dotenv
import os
import sys

 
def activate_sftp():
    load_dotenv("./.env")
    remote_course_machine = os.getenv('REMOTE_COURSE_MACHINE')
    remote_user = os.getenv('REMOTE_USER')
    remote_password = os.getenv('REMOTE_PASS')

    #cnopts = pysftp.CnOpts(knownhosts='185.164.16.144 ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDVSYKHRRj6NfUW7ehCfPDj3f5g9KCFOLVZXK9X/EgNj6KND+85DJ5Jh7iLbxQqrMfjK1SZqMtVWtdEaFm99ZZUdA6yBYPVGavaQFdzg20szZlfMDYkDNjsTWKuk9fIWwcGKzZJbXI/Drkt5Ol430kstsxtBOcqbgfJeSNii0M49rqk0J0F2LyKnV7bGlpaOc8XKimp5OzIqdkmvEZyqSrqsTIaWVCIE1tvjO4Up5rAgzx1vL3kqUxVK1ucYWN47xS3F9ae0/g0d0FGcMn4mamTOJcocudGlGgY9901yTPF6vw1zWrrpU5e/5TGSnKswhFJQmD59LZZaF5O+REgvdYE8CwHXSGwzzlRNJSoeKRNoDV5faDoc1La+Tk82Ud+c8I7Gy9X0ZgeMYCSQQMydOh+MI27HIlTxEaU0jdsxWBGXuFg+brtBwkNnBf2DMy4ZsfzOUGFPro82nCRWxLzq/4DeOImHHg3jqvWWCzX2WQAMO9HbAMSZF+tEgFzLbjn9jU=')
    #cnopts.hostkeys.load('/home/attendance_user/.ssh/known_hosts')
    #cnopts = pysftp.CnOpts()
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    try:
        with pysftp.Connection(host=remote_course_machine, username=remote_user, password=remote_password, cnopts=cnopts) as sftp:
            print("Connection succesfully stablished ... ")
    
            # The remote directory path
            remoteDirPath = os.getenv('REMOTE_DIR_PATH')
            sftp.cwd(remoteDirPath)
            files_attributes = sftp.listdir_attr()
    
                    # , stat.S_IROTH stat.S_IWOTH, stat.S_IXOTH)
            #os.chmod("./csv_files_final/*", stat.S_IROTH, stat.S_IWOTH, stat.S_IXOTH)
            #chmod 777 ./csv_files_final/*
    
            for attr in files_attributes:
                file_name = attr.filename
                #print(file_name)
                remoteFilePath = os.path.join(os.getenv('REMOTE_DIR_PATH'), file_name)
    
            # Set local path where the file will be saved and give attendance user full permission on it
                localFilePath = os.path.join(os.getenv('LOCAL_ORIGIN_DIR_PATH'), file_name)
                #os.chown(localFilePath, 1000, 1000)
                #os.chmod(localFilePath, 777)
    
                sftp.get(remoteFilePath, localFilePath)
                
    except:

        os.environ["LOCAL_ORIGIN_DIR_PATH"] = "./csv_files_origin_offline"
        print(os.environ['LOCAL_ORIGIN_DIR_PATH'])  # outputs 'newvalue'

        # Write changes to .env file.
        dotenv.set_key("./.env.py", "LOCAL_ORIGIN_DIR_PATH", os.environ["LOCAL_ORIGIN_DIR_PATH"])


if __name__ == "__main__":
    activate_sftp()
