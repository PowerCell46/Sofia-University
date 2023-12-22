USE PC;

SELECT 
	AVG(SPEED) AS "Average Speed" 
FROM PC;

SELECT 
	MAKER,
	AVG(SCREEN) AS "Average Screen"
FROM PRODUCT
JOIN LAPTOP ON 
	PRODUCT.model = laptop.model
GROUP BY maker;

SELECT 
	AVG(SPEED) AS "Average Speed"
FROM laptop
WHERE PRICE > 1000;

SELECT 
	maker,
	AVG(price) 
	FROM PRODUCT
JOIN PC ON 
	PRODUCT.model = pc.model
WHERE maker = 'A'
GROUP BY maker;

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
