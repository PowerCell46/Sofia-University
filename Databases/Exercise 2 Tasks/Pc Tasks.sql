use PC

SELECT 
	maker,
	speed
FROM laptop
JOIN product on laptop.model = product.model
WHERE hd >= 9;


SELECT 
	laptop.model,
	price
FROM product
JOIN laptop ON product.model = laptop.model
WHERE maker = 'B';


SELECT hd FROM PC 
GROUP BY hd
HAVING COUNT(*) >= 2;


SELECT 
	speed as 'Mhz',
	hd as 'GB'
FROM pc
GROUP BY speed, hd
ORDER BY speed DESC, GB DESC;


use pc
SELECT 
	maker,
	COUNT(*) AS 'Number of Pcs'
FROM product
JOIN PC ON product.model = pc.model
GROUP BY maker
HAVING COUNT(*) > 1; 
