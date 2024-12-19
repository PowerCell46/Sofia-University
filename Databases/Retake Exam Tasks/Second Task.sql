use ships;

SELECT 
	NAME,
	NUMGUNS,
	(
		SELECT 
			COUNT(RESULT)
		FROM SHIPS 
		LEFT JOIN OUTCOMES ON
			SHIPS.NAME = OUTCOMES.SHIP
		LEFT JOIN BATTLES ON
			OUTCOMES.BATTLE = BATTLES.NAME
		WHERE 
			SHIPS.NAME = S1.NAME
	) AS "Number of battles"
FROM SHIPS S1
JOIN CLASSES ON
	S1.CLASS= CLASSES.CLASS;