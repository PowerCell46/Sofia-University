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
