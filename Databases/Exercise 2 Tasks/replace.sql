
/*
USE movies

SELECT 
	movietitle,
	starname,
	address, 
	gender, 
	birthdate
FROM starsin 
JOIN moviestar ON starsin.starname = moviestar.name
WHERE movietitle = 'Terms of Endearment';


SELECT 
	starname 
FROM starsin
JOIN movie on starsin.movietitle = movie.title
WHERE studioname = 'MGM' 
AND movieyear = 1995;

*/

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



SELECT 
	product.model
FROM product
JOIN PC ON product.model = pc.model
WHERE pc.speed > 500
GROUP BY product.model; -- Incorrect probably
