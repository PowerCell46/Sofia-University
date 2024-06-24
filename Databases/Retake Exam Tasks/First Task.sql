use ships;

SELECT 
	COUNTRY 
FROM classes
WHERE 
	class like 'A%' AND 
	numguns > 5 AND 
	numguns < 10
GROUP BY 
	COUNTRY
ORDER BY 
	COUNTRY ASC;
