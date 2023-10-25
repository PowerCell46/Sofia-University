USE PC

SELECT 
	model, 
	speed AS MHz, 
	hd AS GB 
FROM pc 
WHERE price < 1200;

SELECT 
	model, 
	price * 1.1 as [Price in Euro]
FROM pc 
ORDER BY price ASC;


SELECT 
	model, 
	ram,
	screen
FROM laptop
WHERE price > 1000;


 SELECT 
	* 
FROM printer 
WHERE color = 'y';


SELECT 
	model, 
	speed,
	hd 
FROM pc 
WHERE price <2000 
AND (cd = '12x' or cd = '16x');


SELECT 
	code, 
	model,
	(speed + ram + (screen * 10)) as rating
FROM laptop
ORDER BY (speed + ram + (screen * 10)), code;
