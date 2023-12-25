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
