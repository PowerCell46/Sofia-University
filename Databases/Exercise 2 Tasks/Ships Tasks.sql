
use ships

/*
SELECT name 
FROM ships
JOIN classes ON classes.class = ships.class
WHERE DISPLACEMENT > 35000;


SELECT 
	ship,
	displacement,
	numguns
FROM OUTCOMES
	JOIN ships ON outcomes.ship = ships.name
	JOIN classes ON ships.CLASS = classes.class
 WHERE battle = 'Guadalcanal';
*/

SELECT 
	*
FROM battles 
JOIN OUTCOMES ON BATTLEs.name= OUTCOMES.BATTLE
ORDER BY name, date;


SELECT battles.name AS battle_name
FROM battles 
JOIN OUTCOMES ON battles.name = OUTCOMES.battle
GROUP BY battles.name
HAVING MAX(OUTCOMES.result) = 'sunk'
ORDER BY battles.name;


SELECT ship
FROM OUTCOMES
GROUP BY ship
HAVING SUM(CASE WHEN result = 'sunk' THEN 1 ELSE 0 END) > 0;
/* All ships that have been sunk */
