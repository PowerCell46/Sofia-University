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
