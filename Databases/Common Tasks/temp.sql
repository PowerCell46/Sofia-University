
/*
	За всяка държава да се изведе: броят на корабите от тази държава; броя на битките, в които е участвала; броя на
	битките, в които неин кораб е потънал ('sunk') (ако някоя от бройките е 0 – да се извежда 0).
*/

SELECT 
	DISTINCT COUNTRY,
	(
		SELECT 
			COUNT(NAME)
		FROM CLASSES C1
		JOIN SHIPS ON 
			C1.CLASS = ships.CLASS
		WHERE C1.COUNTRY = CLASSES.COUNTRY
	),
	(
		SELECT COUNT(BATTLE) FROM (
			SELECT 
				BATTLE
			FROM CLASSES C2
			JOIN SHIPS ON 
				C2.CLASS = SHIPS.CLASS
			JOIN OUTCOMES ON 
				SHIPS.NAME = OUTCOMES.SHIP
			WHERE C2.COUNTRY = CLASSES.COUNTRY
			GROUP BY BATTLE
		) AS subquery
	),
	(
		SELECT COUNT(BATTLE) FROM (
			SELECT 
				BATTLE
			FROM CLASSES C3
			JOIN SHIPS ON 
				C3.CLASS = SHIPS.CLASS
			JOIN OUTCOMES O1 ON 
				SHIPS.NAME = O1.SHIP
			WHERE 
				C3.COUNTRY = CLASSES.COUNTRY AND 
				O1.RESULT = 'sunk'
			GROUP BY BATTLE
		) as subquery
	)
FROM CLASSES;
