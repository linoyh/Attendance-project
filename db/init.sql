CREATE DATABASE if not exists linoy_attendance;

USE linoy_attendance;

DROP USER `jeff`;

CREATE USER 'jeff'@'%' IDENTIFIED BY '12345';

GRANT ALL PRIVILEGES ON `linoy_attendance_%`.* to jeff;

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

