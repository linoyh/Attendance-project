#!/usr/bin/python3

# import the relevant modules
import pandas as pd
import os
import sys
import glob
from dotenv import load_dotenv

#checks if the path is a directorry, if not- exit thr script
def is_dir(input_dir_path):
    if not os.path.isdir(input_dir_path):
        print("please insert directory")
        sys.exit(1)

#creat list of all the files fron thr given directory
def get_files_names_from_dir(input_dir_path):
    files_list = []
    files_list = os.listdir(input_dir_path)
    return(files_list)


# one file bottom to top treatments:
# reads Name, Meeting Start Time, Meeting End Time and Attendance Duration cols from the csv files only
# calculate the time of each meet and sum the total time of all the meetings
# remove mins from attendance col
# sum the minutes of attendance for each participant
# write all changes back to the files and place them in a new dir
def df_treatments(filels_list):
    joined_list = []
    total_meetings_time = 0
    for file in filels_list:
        file_input_path = os.path.join(input_dir_path, file)
        file_output_path = os.path.join(output_dir_path, file)
        df = pd.read_csv(file_input_path, usecols=["Name", "Meeting Start Time", "Meeting End Time", "Attendance Duration"], encoding="UTF-16LE", sep="\t")
        df[['Start_date', 'start_min']] = df['Meeting Start Time'].str.split(' ', expand=True)
        df[['End_date', 'end_min']] = df['Meeting End Time'].str.split(' ', expand=True)
        df['start_min'] = df['start_min'].str.replace('"', '')
        df['end_min'] = df['end_min'].str.replace('"', '')
        df['Total Time'] = pd.to_datetime(df['end_min'], errors='coerce') - pd.to_datetime(df['start_min'], errors='coerce')
        df['Total Time'] = df['Total Time'].dt.total_seconds().div(60).astype(int)
        total_time_loop = df.iloc[0]['Total Time']
        total_meetings_time += total_time_loop
        df['Name'] = df['Name'].str.lower()
        df["Attendance Duration"] = df["Attendance Duration"].str.replace("mins", "").astype('int')
        df = df.groupby('Name', as_index=False).sum()
        df.to_csv(file_output_path)
        joined_list = glob.glob(f"{output_dir_path}/*.csv")
    return joined_list, total_meetings_time


# merge all csv files to one
# combine duplicate names
# sum attendance duration for each participant
# remove the temporary col of total time and the Unnamed cols that were added by pa.concat
# add a column that calculate the % of attendance in all the meetings for each participant
# write it all to the attendance file
def merge_csv_files_to_one(joined_list, total_meetings_time):
    df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
    df = pd.DataFrame(df)
    df = df.groupby("Name", as_index=False).sum()
    df.drop(df.filter(regex="Unnamed"), axis=1, inplace=True)
    df.drop(["Total Time"], axis=1, inplace=True)
    df["Attendance Percentage"] = (df["Attendance Duration"] / total_meetings_time)*100
    final_file_path = os.path.join(output_dir_path, "final_par_file.csv")
    df.to_csv(final_file_path, index=False)


# The main function that control the script
# all the actions and calls describesin here by the order
if __name__ == "__main__":
    load_dotenv("/home/linoy/exercises/for_practice/docker-flask-app-att/.env.py")
    input_dir_path = os.getenv('LOCAL_ORIGIN_DIR_PATH')
    output_dir_path = os.getenv('FINAL_CSV_DIR_PATH')
    print(input_dir_path)
    is_dir(input_dir_path)
    files_list = get_files_names_from_dir(input_dir_path)
    joined_list, total_meetings_time = df_treatments(files_list)
    merge_csv_files_to_one(joined_list, total_meetings_time)
