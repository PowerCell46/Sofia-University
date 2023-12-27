/*
	Без повторение заглавията и годините на всички филми, заснети преди 1982, в които е играл поне един актьор
	(актриса), чието име не съдържа нито буквата 'k', нито 'b'. Първо да се изведат най-старите филми.
*/

SELECT 
	title,
	year
FROM MOVIE
WHERE 
	year < 1982 AND 
	(
	SELECT	
		COUNT(*)
	FROM MOVIE M1
	JOIN STARSIN ON
		M1.TITLE = STARSIN.MOVIETITLE
	WHERE 
		M1.TITLE = MOVIE.TITLE AND 
		STARNAME NOT LIKE '%k%' AND 
		STARNAME NOT LIKE '%b%'
	) > 0
ORDER BY year;

/*
	Заглавията и дължините в часове (length е в минути) на всички филми, които са от същата година, от която е и филмът
	Terms of Endearment, но дължината им е по-малка или неизвестна.
*/

SELECT 
	TITLE,
	LENGTH * 1.0 / 60 AS "Length in Hours"
FROM MOVIE
WHERE 
	YEAR = (
	SELECT 
		year 
	FROM MOVIE
	WHERE title = 'Terms of Endearment'
	) AND (LENGTH < (
	SELECT 
		length
	FROM MOVIE
	WHERE title = 'Terms of Endearment'
	) OR LENGTH IS NULL
);

/*
	Имената на всички продуценти, които са и филмови звезди и са играли в поне един филм преди 1980 г. и поне един
	след 1985 г.
*/

SELECT 
	DISTINCT MOVIESTAR.NAME
FROM MOVIESTAR
LEFT JOIN STARSIN ON
	MOVIESTAR.NAME = STARSIN.STARNAME
WHERE 
	 NAME IN (
		SELECT NAME FROM MOVIEEXEC)
	AND (
		SELECT 
			COUNT(*)
		FROM STARSIN S1
		JOIN MOVIE ON
			S1.MOVIETITLE = MOVIE.TITLE
		WHERE 
			S1.STARNAME = STARSIN.STARNAME AND 
			YEAR > 1985
	) > 0 AND (
		SELECT 
			COUNT(*)
		FROM STARSIN S2
		JOIN MOVIE ON
			S2.MOVIETITLE = MOVIE.TITLE
		WHERE 
			S2.STARNAME = STARSIN.STARNAME AND 
			YEAR < 1980
	) > 0;

/*
	Всички черно-бели филми, записани преди най-стария цветен филм (InColor='y'/'n') на същото студио.
*/

SELECT 
	* 
FROM MOVIE
WHERE 
	INCOLOR = 'N' AND 
	YEAR < (
	SELECT TOP 1
	YEAR
FROM MOVIE 
JOIN STUDIO S1 ON
	S1.NAME = MOVIE.STUDIONAME
WHERE 
	S1.NAME = (SELECT STUDIONAME FROM MOVIE WHERE INCOLOR = 'N') AND 
	INCOLOR = 'Y'
ORDER BY YEAR);
 
/*
	Имената и адресите на студиата, които са работили с по-малко от 5 различни филмови звезди. Студиа, за които няма
	посочени филми или има, но не се знае кои актьори са играли в тях, също да бъдат изведени. Първо да се изведат
	студиата, работили с най-много звезди. Напр. ако студиото има два филма, като в първия са играли A, B и C, а във
	втория - C, D и Е, то студиото е работило с 5 звезди общо
*/

SELECT 
	NAME,
	ADDRESS
FROM STUDIO
WHERE(
		SELECT SUM(actor_movie_count) FROM (
		SELECT 
			COUNT(STARNAME) AS actor_movie_count
		FROM STUDIO S1
		JOIN MOVIE ON 
			S1.NAME = MOVIE.STUDIONAME
		JOIN STARSIN ON
			STARSIN.MOVIETITLE = MOVIE.TITLE
		WHERE 
			S1.NAME = STUDIO.NAME
		GROUP BY STARNAME) AS subquery
	) < 5 OR NAME IN (
		SELECT 
			NAME
		FROM STUDIO
		LEFT JOIN MOVIE ON 
			STUDIO.NAME = MOVIE.STUDIONAME
		WHERE MOVIE.TITLE IS NULL
	) OR NAME IN (
	SELECT 
		NAME 
	FROM STUDIO
	JOIN MOVIE ON 
		STUDIO.NAME = MOVIE.STUDIONAME
	LEFT JOIN STARSIN ON
		MOVIE.TITLE = STARSIN.MOVIETITLE
	WHERE MOVIETITLE IS NULL
	)
ORDER BY (
	SELECT SUM(actor_movie_count) FROM (
	SELECT 
		COUNT(STARNAME) AS actor_movie_count
	FROM STUDIO S1
	JOIN MOVIE ON 
		S1.NAME = MOVIE.STUDIONAME
	JOIN STARSIN ON
		STARSIN.MOVIETITLE = MOVIE.TITLE
	WHERE 
		S1.NAME = STUDIO.NAME
	GROUP BY STARNAME) AS subquery
) DESC;

/*
	За всеки кораб, който е от клас с име, несъдържащо буквите i и k, да се изведе името на кораба и през коя година е
	пуснат на вода (launched). Резултатът да бъде сортиран така, че първо да се извеждат най-скоро пуснатите кораби.
*/
use ships;

SELECT 
	name, 
	launched
FROM SHIPS
WHERE
	NAME NOT LIKE '%i%' AND 
	NAME NOT LIKE '%k%'
ORDER BY LAUNCHED DESC;

/*
	Да се изведат имената на всички битки, в които е повреден (damaged) поне един японски кораб.
*/

SELECT 
	BATTLES.NAME 
FROM BATTLES
JOIN OUTCOMES ON 
	BATTLES.NAME = OUTCOMES.BATTLE
JOIN SHIPS ON 
	OUTCOMES.BATTLE = BATTLES.NAME
JOIN CLASSES ON 
	SHIPS.CLASS = CLASSES.CLASS
WHERE 
	COUNTRY = 'Japan' AND 
	RESULT = 'damaged'
GROUP BY BATTLES.NAME;

/*
	Да се изведат имената и класовете на всички кораби, пуснати на вода една година след кораба 'Rodney' и броят на
	оръдията им е по-голям от средния брой оръдия на класовете, произвеждани от тяхната страна.
*/

SELECT 
	SHIPS.NAME,
	SHIPS.CLASS
FROM SHIPS 
JOIN CLASSES ON
	SHIPS.CLASS = CLASSES.CLASS
WHERE 
	LAUNCHED = (SELECT LAUNCHED + 1 FROM SHIPS WHERE NAME = 'Rodney') AND 
	CLASSES.NUMGUNS > (
	SELECT 
		AVG(NUMGUNS)
	FROM CLASSES C1
	JOIN SHIPS ON 
		C1.CLASS = SHIPS.CLASS
	WHERE C1.CLASS = CLASSES.CLASS
	GROUP BY C1.CLASS
	);

/*
	Да се изведат американските класове, за които всички техни кораби са пуснати на вода в рамките на поне 10 години
	(например кораби от клас North Carolina са пускани в периода от 1911 до 1941, което е повече от 10 години, докато
	кораби от клас Tennessee са пуснати само през 1920 и 1921 г.).
*/

SELECT
	CLASSES.CLASS
FROM CLASSES
WHERE 
	COUNTRY = 'USA' AND 
	(
		SELECT 
			MAX(LAUNCHED)
		FROM CLASSES C1
		JOIN SHIPS ON
			C1.CLASS = SHIPS.CLASS
		WHERE C1.CLASS= CLASSES.CLASS
	) -
	(
		SELECT 
			MIN(LAUNCHED)
		FROM CLASSES C2
		JOIN SHIPS ON
			C2.CLASS = SHIPS.CLASS
		WHERE C2.CLASS= CLASSES.CLASS
	) < 10;

/*
	За всяка битка да се изведе средният брой кораби от една и съща държава (например в битката при Guadalcanal са
	участвали 3 американски и един японски кораб, т.е. средният брой е 2).
*/

SELECT 
	NAME,
	(
	SELECT AVG(CAST(avg_ships AS DECIMAL)) FROM (
		SELECT 
			COUNT(SHIP) as avg_ships
		FROM BATTLES B1
		JOIN OUTCOMES ON	
			B1.NAME = OUTCOMES.BATTLE
		JOIN SHIPS ON 
			OUTCOMES.SHIP = SHIPS.NAME
		JOIN CLASSES ON 
			SHIPS.CLASS = CLASSES.CLASS
		WHERE 
			B1.NAME = BATTLES.NAME
		GROUP BY COUNTRY) AS subquery
	) AS "Average Number of Ships per Country"
FROM BATTLES;
