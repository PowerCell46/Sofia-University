CREATE TABLE TempLaptopPc (
    price INT
);

INSERT INTO TempLaptopPc
SELECT 
	price
FROM product
JOIN PC ON product.model = PC.model
WHERE maker = 'B';

INSERT INTO TempLaptopPc
SELECT
	price
FROM product
JOIN LAPTOP ON 
	product.model = laptop.model
WHERE maker = 'B';

SELECT 
	AVG(PRICE) AS "Average Price"
FROM TempLaptopPc;

SELECT 
	speed,
	AVG(PRICE) as "Average Price"
FROM PC
GROUP BY speed;

SELECT 
	maker,
	COUNT(pc.model) AS "Number of Models"
FROM PRODUCT
JOIN PC ON
	product.model = pc.model
GROUP BY maker
HAVING COUNT(pc.model) >= 3;

SELECT TOP 1
	maker
 FROM PRODUCT
JOIN PC ON
	PC.model = product.model
GROUP BY maker
ORDER BY AVG(PRICE) DESC;

SELECT  
	model,
	(SELECT TOP 1
	price
FROM PC p1
WHERE 
	p1.model = pc.model AND 
	price = 
		(SELECT MAX(price) FROM pc 
		WHERE p1.model = pc.model)) AS "Max Model Price"
FROM pc
GROUP BY model;
