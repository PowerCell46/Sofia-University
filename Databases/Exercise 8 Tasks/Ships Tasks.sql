USE ships;

INSERT INTO CLASSES(CLASS, TYPE, COUNTRY, NUMGUNS, BORE, DISPLACEMENT)
VALUES 
	('Nelson', 'bb', 'Gt.Britain', 9, 16, 34000);

INSERT INTO SHIPS(NAME, CLASS, LAUNCHED)
VALUES 
	('George Brydges Rodney', 'Nelson', 1927),
	('1st Baron Rodney', 'Nelson', 1927);

DECLARE @ShipsToDelete TABLE (Ship VARCHAR(100));
INSERT INTO @ShipsToDelete
SELECT name FROM SHIPS
JOIN OUTCOMES ON
	SHIPS.NAME = OUTCOMES.SHIP
WHERE RESULT = 'sunk';

DELETE FROM OUTCOMES 
WHERE OUTCOMES.SHIP IN (SELECT Ship FROM @ShipsToDelete);

DELETE FROM SHIPS
WHERE SHIPS.NAME IN (SELECT Ship FROM @ShipsToDelete);

UPDATE CLASSES 
SET 
	BORE = BORE * 2.54,
	DISPLACEMENT = DISPLACEMENT * 1.1;
	

DECLARE @ClassesToDelete TABLE (Class VARCHAR(100));
INSERT INTO @ClassesToDelete
SELECT CLASSES.CLASS FROM CLASSES
LEFT JOIN SHIPS ON
	CLASSES.CLASS = SHIPS.CLASS
GROUP BY CLASSES.CLASS
HAVING COUNT(SHIPS.NAME) < 3;

DELETE FROM OUTCOMES
WHERE SHIP IN (SELECT NAME FROM SHIPS WHERE CLASS IN (SELECT CLASS FROM @ClassesToDelete));

DELETE FROM SHIPS
WHERE CLASS IN (SELECT CLASS FROM @ClassesToDelete);

DELETE FROM CLASSES 
WHERE CLASS IN (SELECT CLASS FROM @ClassesToDelete);

SELECT * FROM CLASSES
WHERE CLASS = 'Bismarck';

UPDATE CLASSES 
SET BORE = (SELECT BORE 
FROM CLASSES
WHERE CLASS = 'Bismarck')
WHERE CLASS = 'Iowa';

UPDATE CLASSES
SET DISPLACEMENT = (SELECT DISPLACEMENT 
FROM CLASSES
WHERE CLASS = 'Bismarck')
WHERE CLASS = 'Iowa';
