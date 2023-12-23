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
