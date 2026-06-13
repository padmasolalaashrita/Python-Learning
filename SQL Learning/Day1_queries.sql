create database if not exists college_DB;
use college_DB;
create table if not exists Student_details(ID int, Student_name varchar(50), age int, mobile_number varchar(10));
insert into Student_details values (1, "Ashrita Padmasolala",22,"8925921101"),(2, "Jayanth",21,"8712355142");
select * from Student_details;