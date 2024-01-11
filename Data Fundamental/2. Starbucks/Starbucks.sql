# starbucks

DROP DATABASE IF EXISTS starbucks;
CREATE DATABASE starbucks;
USE starbucks;

# schema

CREATE TABLE products (
			product_id INTEGER,
			food VARCHAR(100),
			size VARCHAR(100),
			price FLOAT,
            PRIMARY KEY (product_id)
);

CREATE TABLE sales (
			sale_id INTEGER, 
			line_id INTEGER,
			product_id INTEGER,
			quantity INTEGER,
			PRIMARY KEY (sale_id, line_id),
			FOREIGN KEY (product_id) REFERENCES products (product_id)
);

INSERT INTO products (product_id, food, size, price)
VALUES
			(1,'Caffe Latte','Tall',2.95),
			(2,'Cappuccino','Tall',2.95),
			(3,'Caramel Macchiato','Tall',3.75),
			(4,'Caffe Mocha','Tall',3.25),
			(5,'White Chocolate Mocha','Tall',3.45),
			(6,'Caffe Americano','Tall',2),
			(7,'Cinnamon Dolce Latte','Tall',3.95),
			(8,'Steamer','Tall',2.25),
			(9,'Drip Coffee','Tall',1.75),
			(10,'Caffe Latte','Grande',3.75),
			(11,'Cappuccino','Grande',3.65),
			(12,'Caramel Macchiato','Grande',3.95),
			(13,'Caffe Mocha','Grande',3.95),
			(14,'White Chocolate Mocha','Grande',4.15),
			(15,'Caffe Americano','Grande',2.4),
			(16,'Cinnamon Dolce Latte','Grande',4.75),
			(17,'Steamer','Grande',2.5),
			(18,'Drip Coffee','Grande',1.95),
			(19,'Caffe Latte','Vinti',4.15),
			(20,'Cappuccino','Vinti',4.15),
			(21,'Caramel Macchiato','Vinti',4.25),
			(22,'Caffe Mocha','Vinti',4.4),
			(23,'White Chocolate Mocha','Vinti',4.55),
			(24,'Caffe Americano','Vinti',2.75),
			(25,'Cinnamon Dolce Latte','Vinti',5.15),
			(26,'Steamer','Vinti',2.75),
			(27,'Drip Coffee','Vinti',2.05);

INSERT INTO sales (sale_id, line_id, product_id, quantity) 
VALUES		
			(1,1,4,1),
			(1,2,13,2),
			(1,3,22,3),
			(1,4,5,1),
			(2,1,1,1),
			(3,1,10,1),
			(4,1,7,1),
			(4,2,8,1),
			(4,3,5,2);

# Entity Relationship Diagram: Database > Reverse Engineer > Next > Next > starbucks > Next > Execute > Next > Finish

# price of Grande Caffe Latte

SELECT food,
       size,
       price
FROM   products
WHERE  food = 'Caffe Latte'
       AND size = 'Grande';

# sales amount of the first sale

SELECT Round(Sum(p.price * s.quantity), 2) AS sales_first
FROM   products AS p,
       sales AS s
WHERE  p.product_id = s.product_id
       AND s.sale_id = 1;

# sales amount of Tall drinks

SELECT Round(Sum(p.price * s.quantity), 2) AS sales_tall
FROM   products AS p,
       sales AS s
WHERE  p.product_id = s.product_id
       AND p.size = 'Tall';

# average price of Caffe Mocha

SELECT Round(Avg(price), 2) AS average_price_caffe_mocha
FROM   products
WHERE  food = 'Caffe Mocha';

# sale amount of Tall Caffe Mocha

SELECT Sum(p.price * s.quantity) AS sales_tall_caffe_mocha
FROM   products AS p,
       sales AS s
WHERE  p.product_id = s.product_id
       AND p.food = 'Caffe Mocha'
       AND p.size = 'Tall';