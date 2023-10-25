USE movies

SELECT 
	address 
FROM Studio 
WHERE name = 'MGM';


SELECT 
	birthdate 
FROM MOVIESTAR 
WHERE name = 'Sandra Bullock';


SELECT 
	starname as [Name] 
FROM starsin 
WHERE movieyear = 1980 
AND movietitle like 'Empire%'; 


SELECT 
	name 
FROM movieexec 
WHERE networth > 10000000;


SELECT 
	* 
FROM moviestar 
WHERE gender = 'M' OR [address] LIKE '%Malibu%';
