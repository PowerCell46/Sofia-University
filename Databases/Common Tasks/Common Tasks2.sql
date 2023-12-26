use ships;

/*
	Намерете броя на потъналите американски кораби за всяка проведена битка с поне един потънал
	американски кораб.
*/

SELECT 
	BATTLES.NAME,
	COUNT(SHIPS.NAME) AS "Number of American Sunken Ships"
FROM CLASSES 
JOIN SHIPS ON 
	CLASSES.CLASS = SHIPS.CLASS
JOIN OUTCOMES ON 
	SHIPS.NAME = OUTCOMES.SHIP
JOIN BATTLES ON
	OUTCOMES.BATTLE = BATTLES.NAME
WHERE 
	COUNTRY = 'USA' AND
	RESULT = 'sunk'
GROUP BY BATTLES.NAME;

/*
	Битките, в които са участвали поне 3 кораба на една и съща страна.
*/

SELECT 
    NAME
FROM BATTLES
WHERE (
    SELECT MAX(ship_count)
    FROM (
        SELECT 
            country,
            COUNT(ships.name) AS ship_count
        FROM BATTLES B1
        JOIN OUTCOMES ON B1.NAME = OUTCOMES.BATTLE
        JOIN SHIPS ON OUTCOMES.SHIP = SHIPS.NAME
        JOIN CLASSES ON CLASSES.CLASS = SHIPS.CLASS
        WHERE B1.NAME = BATTLES.NAME
        GROUP BY country
    ) AS subquery_alias
) >= 3;

/*
	Имената на класовете, за които няма кораб, пуснат на вода след 1921 г., но имат пуснат поне един
	кораб.
*/

SELECT CLASS FROM CLASSES

WHERE (
	SELECT 
		COUNT(NAME)
	FROM CLASSES C1
	JOIN SHIPS ON
		C1.CLASS = SHIPS.CLASS
	WHERE 
		C1.CLASS = CLASSES.CLASS AND
		LAUNCHED > 1921
) = 0 AND (
	SELECT 
		COUNT(NAME)
	FROM CLASSES C2
	JOIN SHIPS ON 
		C2.CLASS = SHIPS.CLASS
	WHERE 
		C2.CLASS = CLASSES.CLASS
) >= 1 
GROUP BY CLASS;

/*
	За всеки кораб броя на битките, в които е бил увреден (result = ‘damaged’). Ако корабът не е участвал
	в битки или пък никога не е бил увреждан, в резултата да се вписва 0.
*/

SELECT 
	NAME,
	(
		SELECT SUM(damaged_count) AS total_damaged_count
	FROM (
		SELECT 
			CASE 
				WHEN RESULT = 'damaged' THEN 1
				ELSE 0
			END AS damaged_count
		FROM BATTLES 
		JOIN OUTCOMES ON 
			BATTLES.NAME = OUTCOMES.BATTLE
		RIGHT JOIN SHIPS S1 ON
			OUTCOMES.SHIP = S1.NAME
		WHERE S1.name = SHIPS.NAME
	) AS subquery_alias) AS "Number of being Damaged"
FROM SHIPS
GROUP BY NAME
ORDER BY 
	"Number of being Damaged" DESC,
	SHIPS.NAME ASC;

/*
	За всяка държава да се изведе броят на корабите и броят на потъналите кораби.
*/

SELECT 
	COUNTRY,
	(
		SELECT 
			COUNT(SHIPS.NAME)	
		FROM SHIPS 
		JOIN CLASSES C1 ON
			SHIPS.CLASS = C1.CLASS
		WHERE C1.COUNTRY = CLASSES.COUNTRY
	) AS "Number of Ships",
	(
		SELECT 
			COUNT(SHIPS.NAME)
		FROM SHIPS 
		JOIN CLASSES C2 ON
			C2.CLASS = SHIPS.CLASS
		JOIN OUTCOMES ON
			SHIPS.NAME = OUTCOMES.SHIP
		WHERE 
			C2.COUNTRY = CLASSES.COUNTRY AND 
			RESULT = 'sunk'
	) AS "Number of Sunken Ships"
FROM CLASSES 
GROUP BY COUNTRY;

/*
	 За всяка държава да се изведе броят на повредените кораби и броят на потъналите кораби. Всяка от
	бройките може да бъде и нула.
*/

SELECT 
	COUNTRY,
	CASE 
		WHEN (
			SELECT SUM(damaged_sum) FROM (
				SELECT 
					CASE 
						WHEN result = 'damaged' THEN 1	
						ELSE 0
					END AS damaged_sum
				FROM SHIPS
				LEFT JOIN OUTCOMES ON 
					SHIPS.NAME = OUTCOMES.SHIP
				JOIN CLASSES C1 ON
					SHIPS.CLASS = C1.CLASS
				WHERE C1.COUNTRY = CLASSES.COUNTRY
			) as subquery
		) IS NULL THEN 0
		ELSE (
			SELECT SUM(damaged_sum) FROM (
				SELECT 
					CASE 
						WHEN result = 'damaged' THEN 1	
						ELSE 0
					END AS damaged_sum
				FROM SHIPS
				LEFT JOIN OUTCOMES ON 
					SHIPS.NAME = OUTCOMES.SHIP
				JOIN CLASSES C1 ON
					SHIPS.CLASS = C1.CLASS
				WHERE C1.COUNTRY = CLASSES.COUNTRY
			) as subquery
		)
		END	AS "Damaged Ships",
	CASE 
		WHEN (
			SELECT SUM(sunk_sum) FROM (
				SELECT 
					CASE 
						WHEN result = 'sunk' THEN 1	
						ELSE 0
					END AS sunk_sum
				FROM SHIPS
				LEFT JOIN OUTCOMES ON 
					SHIPS.NAME = OUTCOMES.SHIP
				JOIN CLASSES C2 ON
					SHIPS.CLASS = C2.CLASS
				WHERE C2.COUNTRY = CLASSES.COUNTRY
			) as subquery
		) IS NULL THEN 0
		ELSE (
			SELECT SUM(sunk_sum) FROM (
				SELECT 
					CASE 
						WHEN result = 'sunk' THEN 1	
						ELSE 0
					END AS sunk_sum
				FROM SHIPS
				LEFT JOIN OUTCOMES ON 
					SHIPS.NAME = OUTCOMES.SHIP
				JOIN CLASSES C2 ON
					SHIPS.CLASS = C2.CLASS
				WHERE C2.COUNTRY = CLASSES.COUNTRY
			) as subquery
		)
	END	AS "Sunken Ships"
FROM CLASSES
GROUP BY COUNTRY;

/*
	Намерете за всеки клас с поне 3 кораба броя на корабите от този клас, които са победили в битка
	(result = 'ok')
*/

SELECT 
	CLASS,
	(
		SELECT 
			COUNT(SHIPS.NAME)
		FROM CLASSES C1
		JOIN SHIPS ON
			C1.CLASS = SHIPS.CLASS
		JOIN OUTCOMES ON
			SHIPS.NAME = OUTCOMES.SHIP
		WHERE C1.CLASS = CLASSES.CLASS
		AND RESULT = 'ok'
	) AS "Number of Victory Ships"
FROM CLASSES
WHERE 
	(
		SELECT 
			COUNT(SHIPS.NAME)
		FROM CLASSES C1
		JOIN SHIPS ON
			C1.CLASS = SHIPS.CLASS
		JOIN OUTCOMES ON
			SHIPS.NAME = OUTCOMES.SHIP
		WHERE C1.CLASS = CLASSES.CLASS
		AND RESULT = 'ok'
	) >= 3
GROUP BY CLASS;
