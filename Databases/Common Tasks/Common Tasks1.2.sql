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
