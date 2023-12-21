use ships;

SELECT 
	name,
	classes.country,
	NUMGUNS,
	LAUNCHED
FROM ships
JOIN CLASSES ON
	ships.class = classes.class;


SELECT 
	SHIP
FROM BATTLES
JOIN OUTCOMES ON
	BATTLES.name = OUTCOMES.BATTLE
WHERE YEAR(DATE) = 1942;
