# starbucks

DROP DATABASE IF EXISTS starbucks;
CREATE DATABASE starbucks;
USE starbucks;

# pivot

CREATE TABLE products_long (
			food VARCHAR(100),
			size VARCHAR(100),
			price FLOAT);

INSERT INTO products_long (food, size, price) 
VALUES 		('Caffe Latte','Tall',2.95),
			('Cappuccino','Tall',2.95),
			('Caramel Macchiato','Tall',3.75),
			('Caffe Mocha','Tall',3.25),
			('White Chocolate Mocha','Tall',3.45),
			('Caffe Americano','Tall',2),
			('Cinnamon Dolce Latte','Tall',3.95),
			('Steamer','Tall',2.25),
			('Drip Coffee','Tall',1.75),
			('Caffe Latte','Grande',3.75),
			('Cappuccino','Grande',3.65),
			('Caramel Macchiato','Grande',3.95),
			('Caffe Mocha','Grande',3.95),
			('White Chocolate Mocha','Grande',4.15),
			('Caffe Americano','Grande',2.4),
			('Cinnamon Dolce Latte','Grande',4.75),
			('Steamer','Grande',2.5),
			('Drip Coffee','Grande',1.95),
			('Caffe Latte','Vinti',4.15),
			('Cappuccino','Vinti',4.15),
			('Caramel Macchiato','Vinti',4.25),
			('Caffe Mocha','Vinti',4.4),
			('White Chocolate Mocha','Vinti',4.55),
			('Caffe Americano','Vinti',2.75),
			('Cinnamon Dolce Latte','Vinti',5.15),
			('Steamer','Vinti',2.75),
			('Drip Coffee','Vinti',2.05);

SELECT food,
       Round(Max(CASE
                   WHEN size = 'Tall' THEN price
                   ELSE NULL
                 END), 2) tall,
       Round(Max(CASE
                   WHEN size = 'Grande' THEN price
                   ELSE NULL
                 END), 2) grande,
       Round(Max(CASE
                   WHEN size = 'Vinti' THEN price
                   ELSE NULL
                 END), 2) vinti
FROM   products_long
GROUP  BY food; 

# unpivot

CREATE TABLE products_wide (
			 food   VARCHAR(100),
			 tall   FLOAT,
			 grande FLOAT,
			 vinti  FLOAT);

INSERT INTO products_wide (food, tall, grande, vinti)
VALUES		('Caffe Latte',2.95,3.75,4.15),
			('Cappuccino',2.95,3.65,4.15),
			('Caramel Macchiato',3.75,3.95,4.25),
			('Caffe Mocha',3.25,3.95,4.40),
			('White Chocolate Mocha',3.45,4.15,4.55),
			('Caffe Americano',2.00,2.40,2.75),
			('Cinnamon Dolce Latte',3.95,4.75,5.15),
			('Steamer',2.25,2.50,2.75),
			('Drip Coffee',1.75,1.95,2.05);

SELECT food,
       'Tall' AS size,
       tall   AS price
FROM   products_wide
UNION ALL
SELECT food,
       'Grande' AS size,
       grande   AS price
FROM   products_wide
UNION ALL
SELECT food,
       'Vinti' AS size,
       vinti   AS price
FROM   products_wide;

SELECT     t.food,
           x.*
FROM       products_wide t
CROSS JOIN lateral
           (
                  SELECT 'Tall',
                         tall
                  UNION ALL
                  SELECT 'Grande',
                         grande
                  UNION ALL
                  SELECT 'Vinti',
                         vinti ) x (size, price);
