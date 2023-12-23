use ships;

SELECT COUNT(*) FROM classes;

SELECT 
	AVG(Numguns) AS "Average Numguns"
FROM SHIPS
JOIN CLASSES ON
	ships.class = classes.CLASS;


SELECT 
    CLASSES.CLASS,
    (SELECT TOP 1 
		LAUNCHED
     FROM SHIPS s12
     WHERE s12.CLASS = classes.class AND 
           s12.LAUNCHED = (SELECT MIN(LAUNCHED) FROM SHIPS WHERE s12.CLASS = CLASS)
    ) AS "First Year",
    (SELECT TOP 1 
		LAUNCHED
     FROM SHIPS s13
     WHERE s13.CLASS = classes.class AND 
           s13.LAUNCHED = (SELECT MAX(LAUNCHED) FROM SHIPS WHERE s13.CLASS = CLASS)
    ) AS "Second Year"
FROM CLASSES
JOIN SHIPS ON CLASSES.CLASS = SHIPS.CLASS
GROUP BY classes.CLASS
ORDER BY CLASSES.CLASS;

SELECT 
	class,
	count(ship) as "Number of Sunk Ships"
	FROM OUTCOMES
JOIN SHIPS ON 
	OUTCOMES.ship = ships.name
WHERE RESULT = 'sunk'
GROUP BY class;

SELECT 
	class,
	count(ship) as "Number of Sunk Ships"
FROM outcomes
JOIN ships on
	outcomes.ship = ships.name
WHERE 
	result = 'sunk' AND 
	class in (
		SELECT 
			class
		FROM ships
	GROUP BY class
	HAVING count(name) > 4)
GROUP BY class;

SELECT 
	country,
	AVG(Displacement) as "Average Displacement"
FROM classes
GROUP BY COUNTRY;
