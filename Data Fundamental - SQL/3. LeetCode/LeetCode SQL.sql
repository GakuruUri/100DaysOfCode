#SQL OnLine IDE			: https://sqliteonline.com/
#SQL Formatter			: https://www.dpriver.com/pp/sqlformat.htm
#LeetCode SQL			: https://leetcode.com/problemset/database/
#LeetCode SQL Unlocked	: https://leetcode.ca/all/problems.html

DROP DATABASE IF EXISTS leetcode;
CREATE DATABASE leetcode;
USE leetcode;

#175. Combine Two Tables: report firstName, lastName, city, state for each person in Person table, regardless if there is an address: left join

CREATE TABLE Person (
	personId  INT,
	lastName  VARCHAR(255),
	firstName VARCHAR(255)
);

CREATE TABLE Address (
	addressId int,
	personId int,
	City varchar(255),
	State varchar(255)
);

INSERT INTO Person (personId, lastName, firstName)
VALUES
	('1','Wang','Allen'),
	('2','Alice','Bob');

INSERT INTO Address (addressId, personId, City, State)
VALUES
	('1','2','New York City','New York'),
	('2','3','Leetcode','California');

SELECT firstName,
	   lastName,
	   City,
	   State
FROM   Person p
       LEFT JOIN Address a
              ON p.personId = a.personId
UNION

SELECT firstName,
	   lastName,
	   City,
	   State
FROM   Person p
       RIGHT JOIN Address a
              ON p.personId = a.personId;

#176. Second Highest Salary: ranking, order by, limit offset, rank(). select records 16 - 25, limit 10 offset 15, limit 15, 10

CREATE TABLE Employee (
	id int,
	salary int
);

INSERT INTO Employee (id, salary)
VALUES
	('1','100'),
	('2','200'),
	('3','300');

SELECT  MAX(salary) secondHighestSalary
FROM	Employee
WHERE	salary < (SELECT MAX(salary)
				 FROM	 Employee); #2nd highest < 1st highest

SELECT	DISTINCT salary secondHighestSalary
FROM	Employee
ORDER	BY salary DESC
LIMIT 1 OFFSET 1;

SELECT	DISTINCT salary secondHighestSalary
FROM	(SELECT	salary,
				DENSE_RANK() OVER (ORDER BY Salary DESC) num
		FROM	Employee) e
WHERE	num = 2;

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

#178. Rank Scores: ties receive same ranking, followed by next consecutive integer i.e. no 'holes' between ranks: dense_rank

CREATE TABLE Scores (
     id    INT,
     score DECIMAL(3, 2)
);

INSERT INTO Scores (id, score)
VALUES
	(1,3.5),
    (2,3.65),
    (3,4.0),
    (4,3.85),
    (5,4.0),
    (6,3.65);

SELECT score,
       Dense_rank() OVER (ORDER BY score DESC) num
FROM   scores
ORDER  BY score DESC;

#182. Duplicate Emails

CREATE TABLE Person (
	id int,
	email varchar(256)
);
	
INSERT INTO Person (id, email)
VALUES
	(1,'a@b.com'),
    (2,'c@d.com'),
    (3,'a@b.com');

SELECT 	email
FROM	Person
GROUP	BY email
having	COUNT(*) > 1;

#183. Customers Who Never Order: left join + is null, not in

CREATE TABLE Customers (
	id int,
	name varchar(256)
);

CREATE TABLE Orders (
	id int,
	customerId int
);

INSERT INTO Customers (id, name)
VALUES
	(1,'Joe'),
    (2,'Henry'),
    (3,'Sam'),
    (4,'Max');

INSERT INTO Orders (id, customerId)
VALUES
	(1,3),
    (2,1);

SELECT	c.name customer
FROM	Customers c
		LEFT JOIN Orders o
			   ON c.id = o.customerId
WHERE	O.customerId IS NULL;

SELECT	name customer
FROM	Customers
WHERE	id NOT IN (SELECT DISTINCT customerId
				  FROM Orders); #Customers Who Ordered

#185. Department Top 3 Salaries: find employees who earn top 3 salaries in each department

CREATE TABLE Employee (
	id int,
	name varchar(256),
	salary int,
	departmentId int
);

CREATE TABLE Department (
	id int,
	name varchar(256)
);

INSERT INTO Employee (id, name, salary, departmentId)
VALUES
	(1,'Joe',85000,1),
	(2,'Henry',80000,2),
	(3,'Sam',60000,2),
	(4,'Max',90000,1),
	(5,'Janet',69000,1),
	(6,'Randy',85000,1),
	(7,'Will',70000,1);

INSERT INTO Department (Id, Name)
VALUES
	(1,'IT'),
    (2,'Sales');

SELECT	d.name department,
		e.name employee,
		e.salary
FROM 	(SELECT	departmentId,
				name,
				salary,
				DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) num
		FROM	Employee) e, Department d
WHERE	e.departmentId = d.id
		AND e.num <= 3;