USE ships

  
SELECT 
	class, 
	country 
FROM classes
WHERE numguns < 10;


SELECT 
	name as shipName
FROM ships
WHERE launched < 1918;


SELECT 
	ship, 
	battle
FROM outcomes WHERE result = 'sunk';


SELECT 
	name
FROM ships 
WHERE name = class;


SELECT 
	name 
FROM ships 
WHERE name LIKE 'R%';


SELECT 
	name 
FROM ships 
WHERE LEN(REPLACE(name, ' ', '')) + 1 = LEN(name);
