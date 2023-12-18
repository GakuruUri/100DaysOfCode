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

load data local infile 'D:/WeCloudData/bi-bootcamp-prep/Coffee Chain/csv/Product.csv'
into table Product
fields terminated by ','
enclosed by '"'
lines terminated by '/r/n'
ignore 1 lines;

load data local infile 'D:/WeCloudData/bi-bootcamp-prep/Coffee Chain/csv/Location.csv'
into table Location
fields terminated by ','
enclosed by '"'
lines terminated by '/r/n'
ignore 1 lines;

load data local infile 'D:/WeCloudData/bi-bootcamp-prep/Coffee Chain/csv/Date.csv'
into table Date
fields terminated by ','
enclosed by '"'
lines terminated by '/r/n'
ignore 1 lines;

load data local infile 'D:/WeCloudData/bi-bootcamp-prep/Coffee Chain/csv/Fact.csv'
into table Fact
fields terminated by ','
enclosed by '"'
lines terminated by '/r/n'
ignore 1 lines;

############ answer questions ############

#1. Which Area Code was 25th place in Sales for Espresso? 318

select	Area_Code,
		sum(Sales) Sales
from	Fact f,
		Product p
where	f.Product_Id = p.Product_Id
		and Product_Type = 'Espresso'
group	by Area_Code
order	by Sales desc
limit	24, 1;

#2. Which State in the East Market has the lowest Profit for Espresso? New Hampshire

select	State,
		sum(Profit) Profit
from	Fact f,
		Location l,
        Product p
where	f.Area_Code = l.Area_Code
		and f.Product_Id = p.Product_Id
		and Market = 'East'
        and Product_Type = 'Espresso'
group	by State
order	by Profit
limit	1;

#3. What is the difference in Budget Profit, in 2012Q3 from the previous quarter for Major Market? 630

select	Quarter,
		Budget_Profit_Diff
from	(select	Quarter,
				sum(Budget_Profit) - lag (sum(Budget_Profit), 1) over (order by Quarter) Budget_Profit_Diff
		from	Fact f,
				Date d,
				Location l
		where	f.Date = d.Date
				and f.Area_Code = l.Area_Code
				and Market_Size = 'Major Market'
		group	by Quarter
		order 	by Quarter) x
where	Quarter = '2012Q3';

#4. In which Month did the running Sales cross $30,000 for Decaf in Colorado and Florida? 201305

select 	Month
from	(select	*,
				row_number() over (order by Month) Row_Num
		from	(select	Month,
						sum(Sales) Sales,
						sum(sum(Sales)) over (order by Month) Sales_Cum
				from	Fact f,
						Date d,
						Location l,
						Product p
				where	f.Date = d.Date
						and f.Area_Code = l.Area_Code
						and f.Product_Id = p.Product_Id
						and State in ('Colorado', 'Florida')
						and Product_Category = 'Decaf'
				group	by Month) x
		where	Sales_Cum >=30000) y
where	Row_Num = 1;

#5. Create a bar chart with Product Type, Product, and Profit. Identify which product falls below the overall 99.9% Confidence Interval Distribution (Table across)? Green Tea
#6. Using quartiles, identify which of the following Espresso product has the highest distribution of sales? Regular Espresso
#7. In 2013, identify the State with the highest Profit in the West Market? California

select	State,
		sum(Profit) Profit
from	Fact f,
		Date d,
		Location l
where	f.Date = d.Date
		and f.Area_Code = l.Area_Code
		and Year = '2013'
		and Market = 'West'
group	by State
order	by Profit desc
limit	1;

#8. Create a scatter plot with State, Sales, and Profit. Identify the Trend Line with ‘R-Squared’ value between 0.7 to 0.8? Polynomial Trend Line with Degree 2
#9. Identify the % Expenses / Sales of the State with the lowest Profit. 45.58%

select	State,
		sum(Profit) Profit,
        sum(Expenses)/sum(Sales) Expenses_To_Sales_Ratio
from	Fact f,
		Location l
where	f.Area_Code = l.Area_Code
group	by State
order	by Profit
limit	1;

#10. Create a Combined Field with Product and State. Identify the highest selling Product and State. (Colombian, California), (Colombian, New York)
# row_number() attributes a unique value to each row
# rank() attributes the same row number to the same value, leaving 'holes'
# dense_rank() attributes the same row number to the same value, leaving no 'holes'
/*
+--------+------------+------+------------+
| Salary | row_number | rank | dense_rank |
+--------+------------+------+------------+
|    300 |          1 |    1 |          1 |
|    200 |          2 |    2 |          2 |
|    200 |          3 |    2 |          2 |
|    100 |          4 |    4 |          3 |
+--------+------------+------+------------+
*/

select	Product_State
from	(select	concat('(',Product,', ',State,')') Product_State,
				sum(Sales) Sales,
				dense_rank() over (order by sum(Sales) desc) Num
		from	Fact f,
				Location l,
				Product p
		where	f.Area_Code = l.Area_Code
				and f.Product_Id = p.Product_Id
		group	by Product_State) x
where	Num = 1;

#11. What is the contribution of Tea to the overall Profit in 2012? 20.42%

select	Profit_Pct_Total
from	(select	Product_Type,
				sum(Profit)/sum(Sum(Profit)) Over () Profit_Pct_Total
		from	Fact f,
				Date d,
				Product p
		where	f.Date = d.Date
				and f.Product_Id = p.Product_Id
				and Year = '2012'
		group	by Product_Type
		order 	by Product_Type) x
where	Product_Type = 'Tea';

#12. What is the average % Profit / Sales for all the Products starting with C? 34.52%

select	sum(Profit)/sum(Sales) Profit_To_Sales_Ratio
from	Fact f,
		Product p
where	f.Product_Id = p.Product_Id
		and Product like "C%";

#13. What is the distinct count of Area Codes for the State with the lowest Budget Margin in Small Market? 1

select	State,
		sum(Budget_Margin) Budget_Margin,
		count(distinct f.Area_Code) Area_Code_Distinct_Count
from	Fact f,
		Location l
where	f.Area_Code = l.Area_Code
		and Market_Size = 'Small Market'
group	by State
order	by Budget_Margin
limit	1;

#14. Which Product Type does not have any of its Product within the Top 5 Products by Sales? Tea

select	distinct Product_Type
from	Product
where	Product_Type not in (select	distinct Product_Type
							from 	(select	Product_Type,
											f.Product_Id,
											sum(Sales) Sales
									from	Fact f,
											Product p
									where	f.Product_Id = p.Product_Id
									group	by Product_Type, f.Product_Id
									order	by Sales desc
									limit	5) x);

#15. In the Central Market, the Top 5 Products by Sales contributed _% of the Expenses. 60.92% 

select	Expenses_Cum_Pct_Total
from	(select	*,
				sum(Expenses) over (order by Sales desc) Expenses_Cum,
                sum(Expenses) over () Expenses_Total,
				sum(Expenses) over (order by Sales desc) / sum(Expenses) over () Expenses_Cum_Pct_Total,
				row_number() over (order by Sales desc) Row_Num
		from	(select	Product,
						sum(Sales) Sales,
						sum(expenses) Expenses
				from	Fact f,
						Location l,
						Product p
				where	f.Area_Code = l.Area_Code
						and f.Product_Id = p.Product_Id
						and Market = 'Central'
				group	by Product
				order	by Sales desc) x) y
where	Row_Num = 5;