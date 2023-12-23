USE PC;

SELECT 
	AVG(Price)
FROM PC
WHERE CASE
	WHEN SPEED > 800 THEN 1
	WHEN SPEED <= 800 THEN 0
END = 1
GROUP BY CASE
	WHEN SPEED > 700 THEN 1
	WHEN SPEED <= 800 THEN 0
END;

SELECT 
	AVG(HD) as "Average Storage Space"
	FROM product 
JOIN PC ON
	product.model = pc.model
WHERE maker in (
	SELECT maker FROM PRODUCT 
	JOIN PRINTER ON
		printer.model = product.model
	GROUP BY maker)
GROUP BY CASE 
	WHEN hd > -1 THEN 1
	WHEN 1!=1 THEN 0
END;

SELECT 
    screen,
    (SELECT MAX(price) FROM laptop l2 WHERE l2.screen = laptop.screen) - 
    (SELECT MIN(price) FROM laptop l3 WHERE l3.screen = laptop.screen) AS "Price Difference"
FROM laptop
ORDER BY screen;
