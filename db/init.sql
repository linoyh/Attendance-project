CREATE DATABASE [IF NOT EXISTS] linoy_attendance;
use linoy_attendance;

CREATE USER jeff indentified by '12345';

grant all privileges on `linoy_attendance`.* to jeff;

CREATE TABLE if not exists final_attendance (
    id integer not null auto_increment primary key,
    name VARCHAR(50),
    `attendance duration` INTEGER,
    `attendance percentage` FLOAT);

CREATE TABLE if not exists attendance_csv (
    id integer not null auto_increment primary key,
    `meeting start time` timestamp,
    `meeting end time` timestamp,
    name varchar(128),
    email varchar(128) not null,
    `join time` timestamp,
    `leaving time` timestamp,
    `attendance duration` varchar(128));

