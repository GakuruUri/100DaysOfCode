/*
Using SQL, create a table to identify
1)	customer_id: customer who reached cumulative minimum deposit of $500.
2)	deposit_date: on what day customer reached cumulative minimum deposit of $500.
*/

# create database

DROP DATABASE IF EXISTS deposit;
CREATE DATABASE deposit;
USE deposit; 

# create schema

CREATE TABLE account (
			customer_id INTEGER,
			account_id INTEGER,
			account_type VARCHAR(100),
            PRIMARY KEY (account_id)
);

CREATE TABLE deposit (
			account_id INTEGER,
			deposit_date DATE,
			deposit_amount INTEGER,
			FOREIGN KEY (account_id) REFERENCES account (account_id)
);

INSERT INTO account (customer_id, account_id, account_type)
VALUES		
			(1,11,'Checking'),
			(1,12,'Savings'),
			(2,21,'Checking'),
			(2,22,'Savings'),
			(3,31,'Checking');

INSERT INTO deposit (account_id, deposit_date, deposit_amount)
VALUES		
			(11,'2020-01-01',100),
			(11,'2020-01-02',300),
			(11,'2020-01-05',200),
			(12,'2020-01-01',50),
			(12,'2020-01-02',200),
			(12,'2020-01-03',400),
			(12,'2020-01-04',100),
			(21,'2020-01-02',29),
			(21,'2020-01-04',18),
			(21,'2020-01-05',29),
			(22,'2020-01-03',100),
			(22,'2020-01-04',200),
			(22,'2020-01-05',300),
			(31,'2020-01-02',10),
			(31,'2020-01-03',40);

# solve problem

SELECT customer_id,
       deposit_date
FROM   (SELECT *,
               Row_number()
                 OVER (
                   partition BY customer_id
                   ORDER BY deposit_date) AS row_num
        FROM   (SELECT *,
                       Sum(deposit_amount)
                         OVER (
                           partition BY customer_id
                           ORDER BY deposit_date) AS deposit_amount_cum
                FROM   (SELECT customer_id,
                               deposit_date,
                               Sum(deposit_amount) AS deposit_amount
                        FROM   account a
                               INNER JOIN deposit b
                                       ON a.account_id = b.account_id
                        GROUP  BY customer_id,
                                  deposit_date
                        ORDER  BY customer_id,
                                  deposit_date) AS x) AS y
        WHERE  deposit_amount_cum >= 500) AS z
WHERE  row_num = 1; 