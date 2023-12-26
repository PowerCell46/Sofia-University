use ships;

/*
  Имената и годините на пускане на всички кораби, които имат същото име като
  своя клас.
*/

SELECT 
	NAME,
	LAUNCHED
FROM SHIPS
WHERE CLASS = Name;

/*
	Всички филми, чието заглавие съдържа едновременно думите 'Star' и 'Trek' (не
	непременно в този ред). Резултатите да се подредят по година (първо най-новите
	филми), а филмите от една и съща година - по азбучен ред.
*/

use movies;

SELECT * FROM MOVIE
WHERE 
	TITLE LIKE '%Star%' AND 
	TITLE LIKE '%Trek%'
ORDER BY 
	YEAR DESC,
	TITLE ASC;

/*
	Заглавията и годините на филмите, в които са играли звезди, родени между
	1.1.1970 и 1.7.1980.
*/

SELECT 
	TITLE,
	YEAR
FROM MOVIE
JOIN STARSIN ON
	MOVIE.TITLE = STARSIN.MOVIETITLE
JOIN MOVIESTAR ON
	STARSIN.STARNAME = MOVIESTAR.NAME
WHERE BIRTHDATE BETWEEN '1970-01-01' AND '1980-07-01';

/*
	Имената на всички кораби, за които едновременно са изпълнени следните
	условия: (1) участвали са в поне една битка и (2) имената им (на корабите)
	започват с C или K.
*/

use ships;

SELECT 
	NAME 
FROM SHIPS 
WHERE NAME IN (
	SELECT NAME FROM SHIPS
	WHERE 
		NAME LIKE 'C%' OR 
		NAME LIKE 'K%'
) AND NAME IN (
	SELECT SHIPS.NAME FROM SHIPS 
	JOIN OUTCOMES ON 
		SHIPS.NAME = OUTCOMES.SHIP
);

/*
	Всички държави, които имат потънали в битка кораби.
*/

SELECT 
	COUNTRY
FROM CLASSES
JOIN SHIPS ON 
	CLASSES.CLASS = SHIPS.CLASS
JOIN OUTCOMES ON
	SHIPS.NAME = OUTCOMES.SHIP
WHERE RESULT = 'sunk'
GROUP BY COUNTRY;

/*
	Всички държави, които нямат нито един потънал кораб.
*/


SELECT COUNTRY FROM CLASSES
WHERE COUNTRY NOT IN (
	SELECT 
		COUNTRY	
	FROM CLASSES
	JOIN SHIPS ON 
		CLASSES.CLASS = SHIPS.CLASS
	LEFT JOIN OUTCOMES ON
		SHIPS.NAME = OUTCOMES.SHIP
	WHERE RESULT = 'sunk'
	GROUP BY COUNTRY
)
GROUP BY COUNTRY;

/*
	(От държавен изпит) Имената на класовете, за които няма кораб, пуснат на вода
	(launched) след 1921 г. Ако за класа няма пуснат никакъв кораб, той също трябва
	да излезе в резултата.
*/

SELECT 
	CLASS 
FROM CLASSES 
WHERE CLASS NOT IN (
	SELECT
		CLASSES.CLASS
	FROM CLASSES
	LEFT JOIN SHIPS ON 
		CLASSES.CLASS = SHIPS.CLASS
	WHERE LAUNCHED > 1921
	GROUP BY CLASSES.CLASS
);

use ships;

/*
	Името, държавата и калибъра (bore) на всички класове кораби с 6, 8 или 10
	оръдия. Калибърът да се изведе в сантиметри (1 инч е приблизително 2.54 см).
*/

SELECT DISTINCT
	CLASSES.CLASS,
	COUNTRY,
	BORE * 2.54
FROM CLASSES
JOIN SHIPS ON
	CLASSES.CLASS = SHIPS.CLASS
WHERE COUNTRY IN (
	SELECT COUNTRY FROM CLASSES CL1
	JOIN SHIPS ON
		CLASSES.CLASS = SHIPS.CLASS
	WHERE  
		CL1.COUNTRY = CLASSES.COUNTRY AND 
		BORE IN (6, 8, 10)
)
ORDER BY 
	COUNTRY,
	CLASS;

/*
	Държавите, които имат класове с различен калибър (напр. САЩ имат клас с 14
	калибър и класове с 16 калибър, докато Великобритания има само класове с 15).
*/

SELECT DISTINCT
	COUNTRY 
FROM CLASSES
WHERE 1 < (
	SELECT 
	COUNT(DISTINCT BORE)
FROM CLASSES C1
WHERE C1.COUNTRY = CLASSES.COUNTRY
);

/*
	Страните, които произвеждат кораби с най-голям брой оръдия (numguns).
*/

SELECT 
	COUNTRY,
	AVG(BORE) AS "Average Number of Numguns"
FROM CLASSES
JOIN SHIPS ON
	CLASSES.CLASS = SHIPS.CLASS
GROUP BY COUNTRY
ORDER BY AVG(BORE) DESC;

SELECT 
	COUNTRY,
	MAX(BORE) AS "Biggest Number of Numguns"
FROM CLASSES
JOIN SHIPS ON
	CLASSES.CLASS = SHIPS.CLASS
GROUP BY COUNTRY
ORDER BY MAX(BORE) DESC;

/*
	Компютрите, които са по-евтини от всеки лаптоп на същия производител
*/

use pc;

SELECT * FROM PRODUCT 
JOIN PC ON 
	PRODUCT.model = PC.model
WHERE MAKER IN (
	SELECT 
		MAKER
	FROM PRODUCT
	WHERE (
		SELECT 
			MAX(PRICE)
		FROM product p1
		JOIN PC ON
			p1.model = pc.model
		WHERE p1.MAKER = product.maker
	) < (
		SELECT 
			MAX(PRICE)
		FROM product p2
		JOIN LAPTOP ON
			p2.model = laptop.model
		WHERE p2.MAKER = product.maker
	)
	GROUP BY Maker
)
ORDER BY 
	MAKER,
	PRODUCT.MODEL;

/*
	Компютрите, които са по-евтини от всеки лаптоп и принтер на същия
	производител.
*/

SELECT * FROM PRODUCT 
JOIN PC ON 
	PRODUCT.model = PC.model
WHERE MAKER IN (
	SELECT 
		MAKER
	FROM PRODUCT
	WHERE (
		SELECT 
			MAX(PRICE)
		FROM product p1
		JOIN PC ON
			p1.model = pc.model
		WHERE p1.MAKER = product.maker
	) < (
		SELECT 
			MAX(PRICE)
		FROM product p2
		JOIN LAPTOP ON
			p2.model = laptop.model
		WHERE p2.MAKER = product.maker
	)
	GROUP BY Maker
) AND MAKER IN (
	SELECT 
		MAKER
	FROM PRODUCT
	WHERE (
		SELECT 
			MAX(PRICE)
		FROM product p1
		JOIN PC ON
			p1.model = pc.model
		WHERE p1.MAKER = product.maker
	) < (
		SELECT 
			MAX(PRICE)
		FROM product p2
		JOIN printer ON
			p2.model = printer.model
		WHERE p2.MAKER = product.maker
	)
	GROUP BY Maker
)
ORDER BY 
	MAKER,
	PRODUCT.MODEL;

use movies;

/*
	За всяка филмова звезда да се изведе името, рождената дата и с кое студио е записвала най-много
	филми. (Ако има две студиа с еднакъв брой филми, да се изведе кое да е от тях)
*/

SELECT 
	DISTINCT NAME ,
	BIRTHDATE,
	(
	SELECT TOP 1
	STUDIO.NAME
FROM STUDIO 
JOIN MOVIE ON 
	STUDIO.NAME = MOVIE.STUDIONAME
JOIN STARSIN ON
	MOVIE.TITLE = STARSIN.MOVIETITLE
JOIN MOVIESTAR M1 ON
	STARSIN.STARNAME = M1.NAME
WHERE M1.NAME = MOVIESTAR.NAME
GROUP BY STUDIO.NAME
ORDER BY COUNT(STUDIO.ADDRESS)
)
FROM MOVIESTAR;

/*
	Намерете за всички производители на поне 2 лазерни принтера броя на произвежданите от тях PC-та
	(конкретни конфигурации), евентуално 0.
*/

Use pc;

SELECT 
	maker,
	CASE 
		WHEN COUNT(CODE) IS NULL THEN 0
		ELSE COUNT(code) 
	END	AS "Number of PC configurations"
FROM PRODUCT
JOIN PC ON 
	PRODUCT.model = PC.model
WHERE MAKER IN (
	SELECT 
		MAKER
	FROM product
	JOIN PRINTER ON
		product.model = printer.model
	WHERE 
		printer.type = 'Laser'	
	GROUP BY maker
	HAVING count(product.model) > 1
)
GROUP BY MAKER;

/*
	Да се изведат всички производители, за които средната цена на произведените компютри е по-ниска
	от средната цена на техните лаптопи
*/

SELECT 
	DISTINCT MAKER 
FROM PRODUCT
WHERE (
SELECT 
	AVG(PRICE) 
FROM PRODUCT P1
JOIN PC ON 
	P1.MODEL = PC.MODEL
WHERE P1.maker = PRODUCT.MAKER
GROUP BY MAKER
) < (
SELECT 
	AVG(PRICE) 
FROM PRODUCT P2
JOIN LAPTOP ON 
	P2.MODEL = laptop.MODEL
WHERE P2.maker = PRODUCT.MAKER
GROUP BY MAKER
);

/*
	Един модел компютри може да се предлага в няколко конфигурации с евентуално различна цена. Да
	се изведат тези модели компютри, чиято средна цена (на различните му конфигурации) е по-ниска от
	най-евтиния лаптоп, произвеждан от същия производител.
*/

CREATE TABLE #temp_avg_prices (
    model INT,
    avg_price DECIMAL(10, 2)
);

INSERT INTO #temp_avg_prices (model, avg_price)
SELECT 
    product.model,
    AVG(PRICE) AS avg_price
FROM PRODUCT
JOIN PC ON PRODUCT.model = PC.model
GROUP BY product.model;

SELECT
	*
FROM #temp_avg_prices
JOIN PRODUCT ON
	#temp_avg_prices.model = product.model
WHERE avg_price < (
	SELECT 
		MIN(PRICE)
	FROM PRODUCT P1
	JOIN LAPTOP ON 
		P1.model = LAPTOP.model
	WHERE P1.maker = product.maker
)
ORDER BY #temp_avg_prices.model;
