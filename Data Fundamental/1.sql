/*
enable load data local infile

server
cd c:/program files/mysql/mysql server 8.0/bin
mysql -u root -p
show global variables like 'local_infile';
set global local_infile = 1;

client
load data local infile: right click Connection > Edit Connection > Advanced > Others > add 'OPT_LOCAL_INFILE=1'
*/

/*
SQL order of execution:
FROM	... tables
WHERE	... filter rows: compare dimensions/values
GROUP BY... group rows by dimensions: determine level of details
HAVING	... filter groups: compare aggregated measures/values
SELECT	... select columns: dimensions and (aggregated) measures
ORDER BY... sort rows by dimensions or (aggregated) measures: ascending or descending
LIMIT	... rank rows: bottom n or top n
*/

############ create a database ############

drop database if exists coffee_chain;
create database coffee_chain;
use coffee_chain;

############ create tables ############

create table Product (
	Product_Id varchar(100),
    Product varchar(100),
    Product_Type varchar(100),
    Product_Category varchar(100),
	Primary key (Product_Id));
    
create table Location (
	Area_Code char(3),
    State varchar(100),
    Market varchar(100),
    Market_Size varchar(100),
	primary key (Area_Code));

create table Date (
	Date date,
    Month char(6),
    Quarter char(6),
    Year char(4),
	primary key (Date));

create table Fact (
	Product_Id varchar(100),
    Area_Code char(3),
    Date date,
    Sales integer,
    COGS integer,
    Margin integer,
    Expenses integer,
    Profit integer,
    Marketing integer,
    Inventory integer,
    Budget_Sales integer,
    Budget_COGS integer,
    Budget_Margin integer,
    Budget_Profit integer,
    foreign key (Product_Id) references Product (Product_Id),
    foreign key (Area_Code) references Location (Area_Code),
    foreign key (Date) references Date (Date));

############ load data ############

load data local infile 'C:\Users\ugakuru\OneDrive\100DaysOfCode\Data Fundamental - SQL\1. Coffee Chain\csv'
into table Product
fields terminated by ','
enclosed by '"'
lines terminated by '\r\n'
ignore 1 lines;


load data local infile 'C:\Users\ugakuru\OneDrive\100DaysOfCode\Data Fundamental - SQL\1. Coffee Chain\csv'
into table Date
fields terminated by ','
enclosed by '"'
lines terminated by '\r\n'
ignore 1 lines;

load data local infile 'C:\Users\ugakuru\OneDrive\100DaysOfCode\Data Fundamental - SQL\1. Coffee Chain\csv'
into table Fact
fields terminated by ','
enclosed by '"'
lines terminated by '\r\n'
ignore 1 lines;
